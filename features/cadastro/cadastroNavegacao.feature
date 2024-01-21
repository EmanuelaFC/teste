
Funcionalidade: navegar e validar as paginas de cadastro
    Contexto: preencher todos os campos passo1 e passo2
        Dado que estou na pagina cadastro passo1
        Quando preencho o campo cpf na pagina login com 43016513064
        E preencho o campo nome com dados jose da silva
        E preencho o campo data de nascimento com dados 20071994
        E clico em sim no botao Você é ou tem parentesco com político ou agente público
        Entao verifico que o botao proximo passo esteja habilitado
        Quando clico no botao proximo passo
        Entao valido o direcionamento para pagina cadastro passo2
        Quando preencho o telefone valido com dados 11940028922
        E preencho o campo email com testEmail@test.com
        E preencho o campo confirme o seu email com testEmail@test.com
        E preencho o campo cep com 01513010
        E preencho o campo numero com 4000
        Entao verifico que o botao proximo passo esteja habilitado
        Quando clico no botao proximo passo
        Entao valido o direcionamento para pagina cadastro passo3

    Esquema do Cenario: navegacao na pagina de cadastro cadastro <breadcrumb> <pagina>
        Dado que estou na pagina cadastro <pagina inicial>
        Quando clico no <botao>
        Entao valido o breadcrumb <breadcrumb>
        E valido o direcionamento para pagina <pagina>

        Exemplos:
        |pagina inicial|botao           |breadcrumb      |pagina|
        |passo1        |dados de contato|Dados de Contato|cadastro passo2|
        |passo1        |senha e aceites |Senha e Aceites |cadastro passo3|
        |passo2        |dados pessoais  |Dados Pessoais  |cadastro passo1|




