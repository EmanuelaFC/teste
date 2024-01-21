
Funcionalidade: pagina de ativação do esqueci minha senha

  Contexto: direcionamento para pagina de ativação do esqueci minha senha
    Dado que estou na pagina esqueci minha senha
    Quando preencho o campo com dados validos
    E clico no botao enviar codigo
    E clico no botao ok do modal
    Entao valido o direcionamento para ativacao do esqueci a minha senha


  Esquema do Cenario: links breadCrumb <link> - pagina de ativação do esqueci minha senha
      Quando clico no link breadcrumb <link>
      Entao valido o direcionamento para a página <link>

    Exemplos:
    |link|
    |Esqueci Minha Senha|
    |login pagina ativacao|

   Cenario: clicar no botao cancela - pagina de ativação do esqueci minha senha
      Quando clico no botao cancelar ativacao
      Entao valido o direcionamento para a página login

  Cenario: codigo de ativao em branco - pagina de ativação do esqueci minha senha
      Dado que o campo do codigo de ativacao esteja em branco
      Entao valido que o botao confirmar codigo esteja desativado


   Esquema do Cenario: codigo de ativação invalida - pagina de ativação do esqueci minha senha
      Quando preencho o campo de codigo de ativacao com <dado>
      E clico no botao confirmar codigo
      Entao valido o modal com a mensagem Chave inválida

    Exemplos:
    |dado|
    |1235|
    |1865|

  Cenario: clicar no link enviar o codigo novamente - pagina de ativação do esqueci minha senha
    Quando clico no link enviar o codigo novamente
    Entao valido o modal com a mensagem de sucesso

  Cenario: ir para renovacao de senha - pagina de ativação do esqueci minha senha
    Quando obtenho o codigo de ativacao
    E preencho com o codigo de ativacao valido
    E clico no botao confirmar codigo
    Entao valido que estou na pagina alterar senha
