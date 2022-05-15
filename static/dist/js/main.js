let tituloBusqueda = document.getElementById("tituloDeBusqueda");
let cambioDeTexto = false;
let tablaDeEmpleos = null;

document.getElementById("fechaInicio").onchange = function () {
  buscarPredficcion();
};
document.getElementById("empresa").onchange = function () {
  buscarPredficcion();
};

function buscarHistorico() {
  document.getElementsByClassName("preloader")[0].classList.remove("d-none");
  let cicloDeCambioDeTiempo = setInterval(() => {
    if (cambioDeTexto) {
      tituloBusqueda.innerText = "Buscando Prediccion...";
      cambioDeTexto = false;
    } else {
      tituloBusqueda.innerText = "Esto puede demorar unos minutos ...";
      cambioDeTexto = true;
    }
  }, 3000);

  fetch(
    "http://localhost:8000/buscar?startDate=" +
      document.getElementById("fechaInicio").value+
      "&empresa="+document.getElementById("empresa").value
  )
    .then((response) => response.json())
    .then((data) => {
      clearInterval(cicloDeCambioDeTiempo);
      document.getElementsByClassName("preloader")[0].classList.add("d-none");
      getDataPointsFromCSV(data);
    });
}

function buscarPredficcion() {
  document.getElementsByClassName("preloader")[0].classList.remove("d-none");
  let cicloDeCambioDeTiempo = setInterval(() => {
    if (cambioDeTexto) {
      tituloBusqueda.innerText = "Buscando Prediccion...";
      cambioDeTexto = false;
    } else {
      tituloBusqueda.innerText = "Esto puede demorar unos minutos ...";
      cambioDeTexto = true;
    }
  }, 3000);
  fetch("http://localhost:8000/ggplot?empresa="+document.getElementById("empresa").value)
    .then((response) => response.json())
    .then((data) => {
      clearInterval(cicloDeCambioDeTiempo);
      document.getElementsByClassName("preloader")[0].classList.add("d-none");
      buscarHistorico();
      dibujarPredicion(data);
    });
}
