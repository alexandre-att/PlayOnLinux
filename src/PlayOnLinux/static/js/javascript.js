document.addEventListener('DOMContentLoaded', function () {
    const copyButtons = document.querySelectorAll('.copyButton');

    copyButtons.forEach(function (button) {
        button.addEventListener('click', function (evento) {
            const textToCopy = evento.target.previousElementSibling;
            //const textToCopy = document.getElementById(textToCopyId).textContent;

            // Seleciona o texto
            const range = document.createRange();
            const selection = window.getSelection();
            range.selectNodeContents(textToCopy);
            selection.removeAllRanges();
            selection.addRange(range);

            // Tenta copiar o texto selecionado
            try {
                document.execCommand('copy');
                alert('Texto copiado com sucesso!');
            } catch (err) {
                console.error('Erro ao copiar texto:', err);
                alert('Erro ao copiar texto. Por favor, copie manualmente.');
            }

            // Limpa a seleção
            selection.removeAllRanges();
        });
    });
});        
