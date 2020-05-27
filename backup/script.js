function validar() {

    const nome_cliente = document.getElementById('nome_cliente');
    const login = document.getElementById('login');
    const senha = document.getElementById('senha');
    const cpf = document.getElementById('cpf');


    if (nome_cliente.value === 'Digite o Nome') {
        alert("Digite seu Nome.");
        return false;
    }
    if (login.value === 'Login do usuario') {
        alert("Insira seu Login.");
        return false;
    }
    if (senha.value == "Digite a senha") {
        alert("Insira sua senha.");
        return false;
    }
    if (cpf.value == "CPF do Usuario") {
        alert("Insira seu CPF.");
        return false;
    }                
    return true;
}

function salvar() {
    if (!validar()) return;
    document.getElementById("form_principal").submit();
}
