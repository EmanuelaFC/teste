
Funcionalidade: esqueci minha senha

    Contexto: abrir pagina esqueci minha senha
      Dado que estou na pagina esqueci minha senha

    Esquema do Cenario: links breadCrumb - pagina esqueci minha senha
      Quando clico no link breadcrumb <link>
      Entao valido o direcionamento para a página <link>

    Exemplos:
    |link|
    |login|
    |home|

    Cenario: clicar no botao cancela - pagina esqueci minha senha
      Quando clico no botao cancelar
      Entao valido o direcionamento para a página login

    Cenario: botao enviar codigo desativado com dados em branco - pagina esqueci minha senha
      Dado que o campo cpf esteja em branco
      Entao valido o botao enviar codigo desativado


    Cenario: Cpf invalido - pagina esqueci minha senha
      Quando preencho o campo com dados invalidos 12345678945
      Entao valido a mensagem de erro

    Cenario: Cpf valido mas não cadastrado - pagina esqueci minha senha
      Quando preencho o campo com  dados validos e nao cadastrado 71138220027
      E clico no botao enviar codigo
      Entao valido o modal com a mensagem Cliente não cadastrado


    Cenario: Informar cpf com dados válidos e cadastrados - pagina esqueci minha senha
      Quando preencho o campo com dados validos
      E clico no botao enviar codigo
      Entao valido o modal com a mensagem de sucesso
      E clico no botao ok do modal
      E valido o direcionamento para ativacao do esqueci a minha senha