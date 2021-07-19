/* Cria a variável inputNome e coloca nela o elemento que possui o id nome */
let inputNome = document.querySelector('#nome')
let inputEmail = document.querySelector('#email')
let textareaMensagem = document.querySelector('#mensagem')
let btEnviar = document.querySelector('#enviar')
/* Só posso utilziar a arrow function (=>) quando a função não tiver nome */
inputNome.addEventListener('keyup', () => { 
   if(inputNome.value.length <= 2) {
      inputNome.style.borderColor = 'red'
   } else {
      inputNome.style.borderColor = 'green'
   }
})

inputEmail.addEventListener('keyup',() =>{
    if (inputEmail.value.indexOF('@') == -1 || inputEmail.value.indexOF('.') == -1){
        inputEmail.style.borderColor = 'red'
    } else{
        inputEmail.style.borderColor = 'green'
    }

})

