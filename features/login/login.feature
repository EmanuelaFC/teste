
Funcionalidade: teste na pagina login

  Contexto: abrir pagina login
    Dado que estou na pagina login

  Cenario: Link breadCrumb pagina login
    Quando clico no link breadcrumb home da pagina login
    Entao valido o direcionamento da pagina login para a página home


  Cenario: Esqueci a minha senha - pagina login
    Quando clico no link esqueci minha senha
    Entao valido o direcionamento da pagina login para esqueci minha senha

Cenario: Cadastre-se agora - pagina login
    Quando clico no link cadastre se agora
    Entao valido o direcionamento da pagina login para cadastro

  Cenario: Não recebi o e-mail de ativação - pagina login
    Quando clico no link Nao recebi o e-mail de ativacao
    Entao valido o modal com as instrucoes Para receber o email de ativação, siga o fluxo de login colocando seu CPF e sua senha!

  Esquema do Cenario: Login com cpf inválidos - pagina login
    Quando preencho o campo cpf com <dados>
    E clico no campo senha
    Entao verifico a mensagem de erro <msg> no campo cpf

  Exemplos:
  |dados|msg|
  |50926166019|Preencha seu CPF corretamente.|



  Esquema do Cenario: Campo obrigatorio - dados em branco - pagina login
    Quando o campo <campo> esteja em branco
    Entao valido a mensagem <msg> no campo <campo> na pagina login
    E valido que o botao fazer login esteja desabilitado

  Exemplos:
  |campo|msg|
  |senha|Por favor digite sua senha|

