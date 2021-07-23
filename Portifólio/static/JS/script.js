/* Cria a variável inputNome e coloca nela o elemento que possui o id nome */
let inputNome = document.querySelector('#nome')
let inputEmail = document.querySelector('#email')
let textareaMensagem = document.querySelector('#mensagem')
let btEnviar = document.querySelector('#enviar')
let nomeOk = false /* variável de controle para o botão */
let emailOk = false /* variável de controle para o botão */
let msgOk = false /* variável de controle para o botão */
btnEnviar.disabled = true /* Desabilita o botão assim que inicia a página html */
/* Só posso utilziar a arrow function (=>) quando a função não tiver nome */
inputNome.addEventListener('keyup', () => { 
   if(inputNome.value.length <= 2) {
      inputNome.style.borderColor = 'red'
      nomeOk = false
   } else {
      inputNome.style.borderColor = 'green'
      nomeOk = true
   }

   if(inputNome.value == '' || inputNome.value == undefined || inputNome.value == null) {
      inputNome.style.borderColor = '#ccc'
   }

   /* Se todas as variáveis forem true habilita o botão */
   if (nomeOk && emailOk && msgOk) {
      btnEnviar.disabled = false
   } else { /* se não, desabilita */
      btnEnviar.disabled = true
   }


})

inputEmail.addEventListener('keyup',() => {
   if(inputEmail.value.indexOf('@') == -1 || inputEmail.value.indexOf('.') == -1){
        inputEmail.style.borderColor = 'red' /* Troca a cor da borda do input para red */
        emailOk = false
   } else {
        inputEmail.style.borderColor = 'green'
        emailOk = true
   }
   if (nomeOk && emailOk && msgOk) {
      btnEnviar.disabled = false
   } else { /* se não, desabilita */
      btnEnviar.disabled = true
   }
})

textareaMensagem.addEventListener('keydown', ()=>{
    /* Verifica se o tamanho do valor do textareaMensagem é maior que 100  */
    if(textareaMensagem.value.length > 100){
       textareaMensagem.style.borderColor = 'red' /* Troca a cor da borda do input para red */
       msgOk = false
    } else {
       textareaMensagem.style.borderColor = 'green' /* Troca a cor da borda do input para green */
       msgOk = true
   }
   if (nomeOk && emailOk && msgOk) {
      btnEnviar.disabled = false
   } else { /* se não, desabilita */
      btnEnviar.disabled = true
   }
 })
 
 btnEnviar.addEventListener('click', () => {
   /* Pega a div de carregamento */
   let carregamento = document.querySelector('#carregamento')
   /* Mostra a div de carregamento, adicionando o 'flex' ao display */
   carregamento.style.display = 'flex'

   /* Pega o Form */
   let form = document.querySelector('form')
   /* Esconde o Form, mudando o display pra 'none' */
   form.style.display = 'none'
})
