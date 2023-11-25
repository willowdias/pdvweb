document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('minhaTabela');
    container.scrollTop = container.scrollHeight; // Rola até o final do container
});

function fecharDiv() {
    var divParaFechar = document.getElementById("Alerta");
    divParaFechar.style.display = "none";
}