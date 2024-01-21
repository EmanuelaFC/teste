
Funcionalidade: navegar e validar as paginas de cadastro


    Esquema do Cenario: navegacao na pagina de cadastro cadastro com dados em branco <botao>
        Dado que estou na pagina cadastro <pagina inicial>
        Quando clico no <botao>
        Entao valido o modal cadastro com a mensagem Certifique-se que este formulario foi preenchido corretamente.

        Exemplos:
        |pagina inicial|botao           |breadcrumb      |pagina|
        |passo1        |dados de contato|Dados de Contato|cadastro passo2|
        |passo1        |senha e aceites |Senha e Aceites |cadastro passo3|





