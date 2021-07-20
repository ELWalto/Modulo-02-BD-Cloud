const elementoNome = document.getElementById('nome');
const elementoSituacao = document.querySelector('#situacao');
const elementoImg = document.querySelector('#imagem') 
let elementoBtn = document.querySelector('#alterar') 

elementoBtn.addEventListener('click', () =>{
    if(elementoBtn.value == 'primeiro'){
        elementoImg.src = './assets/img/Santo-guitarrista.png' 
        elementoNome.innerText = 'Santo Paulo Guitarrista' 
        elementoSituacao.innerText = 'Primeiro na tabela' 
        elementoBtn.value = 'segundo' 
    } else if(elementoBtn.value == 'segundo') { 
        elementoImg.src = './assets/img/sp-pistola-redimensionada.png' 
        elementoNome.innerText = 'Santo Paulo pistola' 
        elementoSituacao.innerText = 'Zona de rebaixamento' 
        elementoBtn.value = 'terceiro'  
    } else { 
        elementoImg.src = './assets/img/Santo-Paulo-Feliz.png'
        elementoNome.innerText = 'Santo Paulo conformado' 
        elementoSituacao.innerText = 'Meio da  tabela '
        elementoBtn.value = 'primeiro' 
    }
})