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

inputEmail.addEventListener('keyup',() => {
    if(inputEmail.value.indexOf('@') == -1 || inputEmail.value.indexOf('.') == -1){
        inputEmail.style.borderColor = 'red' /* Troca a cor da borda do input para red */
     } else {
        inputEmail.style.borderColor = 'green'
     }

})

textareaMensagem.addEventListener('keyup', ()=>{
    /* Verifica se o tamanho do valor do textareaMensagem é maior que 100  */
    if(textareaMensagem.value.length > 100){
       textareaMensagem.style.borderColor = 'red' /* Troca a cor da borda do input para red */
    } else {
       textareaMensagem.style.borderColor = 'green' /* Troca a cor da borda do input para green */
    }
 })
 
 /* Adiciona um evento de click no btnEnviar e realiza a função */
 btnEnviar.addEventListener('click', () => {
    alert('Formulário enviado com sucesso!') /* Mostra um alerta na tela com essa mensagem */
 })
 

