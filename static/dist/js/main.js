let tituloBusqueda = document.getElementById("tituloDeBusqueda");
let cambioDeTexto = false;
let tablaDeEmpleos = null;
document.getElementById("buscarForm").onsubmit = function (e) {
  e.preventDefault();
  document.getElementsByClassName("preloader")[0].classList.remove("d-none");
  let cicloDeCambioDeTiempo = setInterval(() => {
    if (cambioDeTexto) {
      tituloBusqueda.innerText = "Buscando Empleos...";
      cambioDeTexto = false;
    } else {
      tituloBusqueda.innerText = "Esto puede demorar unos minutos ...";
      cambioDeTexto = true;
    }
  }, 3000);

  var form = new FormData(document.getElementById('buscarForm'));
  fetch("/buscar", {
      method: "POST",
      body: form
    }).then(response => response.json())
    .catch(error => {
      console.error('Error:', error)
      alert("Parece que hubo un error...");
      clearInterval(cicloDeCambioDeTiempo);
    })
    .then(response => {
      clearInterval(cicloDeCambioDeTiempo);
      document.getElementsByClassName("preloader")[0].classList.add("d-none");
      let cuerpoDeTabla = $("#cuerpo");
      let filas = "";
      cuerpoDeTabla.html("");
      let numeroDeVacantesList=response[0].numeroDeEmpleos;
      let fechaVacatesList=response[2].fechasDeVacantes;
      response=response[1].empleos;
      for (i in response) {
        cuerpoDeTabla.append("<tr><td>" + response[i].titulo + "</td>" +
          "<td><a href=\"" + response[i].url + "\">ver</a></td>" +
          "<td>" + response[i].descripcion + "</td>" +
          "<td>" + response[i].empresa + "</td>" +
          "<td>" + response[i].fecha + "</td>" +
          "<td>" + response[i].plataforma + "</td>" +
          "<td>" + response[i].salario + "</td>" +
          "<td>" + response[i].ubicacion + "</td>" +
          "</tr>");
      }
      if (tablaDeEmpleos != null) {
        tablaDeEmpleos.table.destroy();
      }
      tablaDeEmpleos = $('#example').DataTable();
      dibujarGrafcaNumeroVacantes(JSON.parse(numeroDeVacantesList));
      dibujarFechaVacantes(JSON.parse(fechaVacatesList));
      document.getElementById("example").classList.remove("d-none");


    });

};


function dibujarGrafcaNumeroVacantes(json){
  let vacantes=[];
  let cantidadDeVacantes=[];
  for(i in json){
    vacantes.push(i);
    cantidadDeVacantes.push(json[i]);    
  }
  const ctx = document.getElementById('myChart').getContext('2d');
  const myChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: vacantes,
          datasets: [{
              label: '# of Votes',
              data: cantidadDeVacantes,
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });
}

function dibujarFechaVacantes(json){
  let fechas=[];
  let cantidadDeVacantesPorFecha=[];
  for(i in json){
    fechas.push(i);
    cantidadDeVacantesPorFecha.push(json[i]);    
  }
  const ctx = document.getElementById('fechas-chart').getContext('2d');
  const myChart = new Chart(ctx, {
      type: 'line',
      data: {
          labels: fechas,
          datasets: [{
              label: '# of Votes',
              data: cantidadDeVacantesPorFecha,
              backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(54, 162, 235, 0.2)',
                  'rgba(255, 206, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)',
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(255, 159, 64, 0.2)'
              ],
              borderColor: [
                  'rgba(255, 99, 132, 1)',
                  'rgba(54, 162, 235, 1)',
                  'rgba(255, 206, 86, 1)',
                  'rgba(75, 192, 192, 1)',
                  'rgba(153, 102, 255, 1)',
                  'rgba(255, 159, 64, 1)'
              ],
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });
}