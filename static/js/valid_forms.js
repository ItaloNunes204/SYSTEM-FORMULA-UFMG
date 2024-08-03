let senha = document.querySelector('#senha')
let labelSenha = document.querySelector('#labelSenha')
senha.addEventListener('keyup', () => {
    let eye = document.querySelector('.bi-eye')
    if(senha.value.length === 0){
        labelSenha.setAttribute('style','color: #2c11f5')
        labelSenha.innerHTML = 'Senha'
        senha.setAttribute('style','border-color: #2c11f5')
        eye.setAttribute('style','color: #2c11f5')
    }else if(senha.value.length <= 4){
        labelSenha.setAttribute('style','color: red')
        labelSenha.innerHTML = 'Coloque pelomenos 5 caracteres'
        senha.setAttribute('style','border-color: red')
        eye.setAttribute('style','color: red')
    }else{
            labelSenha.setAttribute('style','color: green')
            labelSenha.innerHTML = 'Senha'
            senha.setAttribute('style','border-color: green')
            eye.setAttribute('style','color: green')
    }
})