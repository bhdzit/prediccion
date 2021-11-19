
let tituloBusqueda = document.getElementById("tituloDeBusqueda");
let cambioDeTexto = false;
let tablaDeEmpleos=null;
document.getElementById("buscarForm").onsubmit = function (e) {
  e.preventDefault();
  document.getElementsByClassName("preloader")[0].classList.remove("d-none");
  let cicloDeCambioDeTiempo = setInterval(() => {
    if (cambioDeTexto) {
      tituloBusqueda.innerText = "Buscando Empleos...";
      cambioDeTexto = false;
    }
    else {
      tituloBusqueda.innerText = "Esto puede demorar unos minutos ...";
      cambioDeTexto = true;
    }
  }, 3000);

  var form = new FormData(document.getElementById('buscarForm'));
  fetch("/buscar", {
    method: "POST",
    body: form
  }).then(response => response.json())
    .catch(error =>{
       console.error('Error:', error)
      alert("Parece que hubo un error...");
      clearInterval(cicloDeCambioDeTiempo);
      })
    .then(response =>{
    console.log(response[0]);
      clearInterval(cicloDeCambioDeTiempo);
      document.getElementsByClassName("preloader")[0].classList.add("d-none");
      let cuerpoDeTabla=$("#cuerpo");
    let filas="";
    cuerpoDeTabla.html("");
      for(i in response){
        cuerpoDeTabla.append("<tr><td>"+response[i].titulo+"</td>"      
        +"<td><a href=\""+response[i].url+"\">ver</a></td>"        
        +"<td>"+response[i].descripcion+"</td>"        
        +"<td>"+response[i].empresa+"</td>"        
        +"<td>"+response[i].fecha+"</td>"
        +"<td>"+response[i].plataforma+"</td>"
        +"<td>"+response[i].salario+"</td>"
        +"<td>"+response[i].ubicacion+"</td>"        
        +"</tr>");
      }
    if(tablaDeEmpleos!=null){
        tablaDeEmpleos.table.destroy();
    }  
    tablaDeEmpleos = $('#example').DataTable();
    document.getElementById("example").classList.remove("d-none");
        
  
    });

};