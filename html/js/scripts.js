

var btn = document.getElementById('boton');
var img = document.getElementById('imagen');
btn.onclick = function() {
    var texto = document.getElementById('texto_1').value
    img.src = "http://0.0.0.0:5000/text/".concat(texto)
};