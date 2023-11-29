document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('minhaTabela');
    container.scrollTop = container.scrollHeight; // Rola até o final do container

});

function fecharDiv() {
    var divParaFechar = document.getElementById("Alerta");
    divParaFechar.style.display = "none";
}

function validarFormulario() {
    var numero = document.getElementById('Desconto').value;
    if (isNaN(numero)) {
        alert('Por favor, insira apenas números!');
        return false;
    }
    return true;
}

function Desconto(){
    var valortotal = parseFloat(document.getElementById("valortotal").value) || 0;
    var desconto = parseFloat(document.getElementById("Desconto").value) || 0;
    
    var descontos= valortotal*(desconto / 100);
    var precioConDescuento = valortotal - descontos;
    document.getElementById("valortotal").value = precioConDescuento

}

function apagariten(id) {



    var divToClose = document.getElementById("sim-nao");
    divToClose.style.display = "flex";

    var meuLink = document.getElementById('simBtn');
    meuLink.href =('deletar/'+id);
    
}
function fechar(){
    var divToClose = document.getElementById("sim-nao");
    divToClose.style.display = "none";
    const meuLink = document.getElementById('simBtn');

    // Para limpar o valor do atributo href (torná-lo vazio)
    meuLink.setAttribute('href', '');
}