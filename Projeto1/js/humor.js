var element = document.getElementById('Imagem');
element.onclick = function() {
    if (element.src.match("img/sp-feliz.jpg")) {
        element.src = "sp-feliz.jpg";
    } 
    else {
        element.src="sp-pistola.jpg";
    }
}

