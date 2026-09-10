document.addEventListener('DOMContentLoaded', () => {
    // Controle do Menu Lateral (Drawer)
    const toggleBtn = document.getElementById('menu-toggle');
    const closeBtn = document.getElementById('menu-close');
    const sidebar = document.getElementById('sidebar');

    if (toggleBtn && sidebar && closeBtn) {
        toggleBtn.addEventListener('click', () => sidebar.classList.add('active'));
        closeBtn.addEventListener('click', () => sidebar.classList.remove('active'));
    }

    // Manipulação do Formulário de Inscrição
    const formInscricao = document.getElementById('form-inscricao');
    const formMessage = document.getElementById('form-message');

    if (formInscricao) {
        formInscricao.addEventListener('submit', async (e) => {
            e.preventDefault();

            const nome = document.getElementById('nome').value.trim();
            const telefone = document.getElementById('telefone').value.trim();
            const email = document.getElementById('email').value.trim();

            formMessage.textContent = "Processando inscrição...";
            formMessage.className = "form-message loading";

            try {
                const response = att_response = await fetch('/api/inscricoes', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ nome, telefone, email })
                });

                const resultado = await response.json();

                if (response.ok && resultado.success) {
                    formMessage.textContent = resultado.message;
                    formMessage.className = "form-message success";
                    formInscricao.reset();
                } else {
                    formMessage.textContent = resultado.message || "Ocorreu um erro ao realizar a inscrição.";
                    formMessage.className = "form-message error";
                }
            } catch (error) {
                formMessage.textContent = "Erro de conexão com o servidor.";
                formMessage.className = "form-message error";
            }
        });
    }
});