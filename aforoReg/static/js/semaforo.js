function iniciarSemaforo (numPersonas) {
    var verde = document.getElementById("verde");
    var amarillo = document.getElementById("amarillo");
    var rojo = document.getElementById("rojo");

    if (numPersonas <=5) {
        verde.style.opacity=1;
        amarillo.style.opacity=.3;
        rojo.style.opacity=.3;
    } else if (numPersonas > 5 && numPersonas < 10) {
        verde.style.opacity=.3;
        amarillo.style.opacity=1;
        rojo.style.opacity=.3;
    } else {
        verde.style.opacity=.3;
        amarillo.style.opacity=.3;
        rojo.style.opacity=1;
    }
}

var timer=setInterval(function(){
    fetch('/semaforo')
        .then(response => response.json())
        .then(data => {
            iniciarSemaforo(data.personas);
        })
        .catch(error => {
            console.error('Error al obtener el numero de personas: ', error);
        })
}, 12000);

fetch('/semaforo')
    .then(response => response.json())
    .then(data => {
        iniciarSemaforo(data.personas);
    })
    .catch(error => {
        console.error('Error al reobtener el numero de personas: ', error);
    });