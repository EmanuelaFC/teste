Funcionalidade: Pagina home
  Contexto: esta na pagina principal do site tele sena
    Dado que estou na pagina home

  Cenario: mensagem de cookie
    Entao verifico o texto da mensagem do cookie Usamos cookies para oferecer a melhor experiência e facilitar a navegação de forma segura. Para maiores informações consulte nossa Política de Cookies clicando aqui ou para continuar clica em Entendi
    E validar se ta ativo o botao Entendi

  Cenario: direcionamento pagina compra passo1 clicando no banner - Pagina home
    Quando clico no banner da campanha
    Entao valido o direcionamento da pagina home pra compra passo1

  Esquema do Cenario: verificando o direcionamento clicando no botao <botao> - Pagina home
    Quando clico no botao <botao>
    Entao valido o direcionamento da pagina home pra <url>

  Exemplos:
  |botao|url|
  |resultado|resultado|
  |ir para minhas tele senas deslogado|login|
  |compre ja a sua|compra passo1|
  |cadastre aqui deslogado| login|
  |compre agora| compra passo1|



  Cenario: Cadastre-se na nossa newslette - botao desativado(dados em branco) - Pagina home
    Dado que o campo nome esteja em branco
    E o campo email esteja em branco
    Entao valido o botao desativado

  Cenario: Cadastre-se na nossa newslette - botao desativado(nome em branco) - Pagina home
    Dado que o campo nome esteja em branco
    Quando preencho campo email com email@test.com
    Entao valido o botao desativado

  Cenario: Cadastre-se na nossa newslette - botao desativado(email em branco) - Pagina home
    Quando preencho campo nome com NomeTest
    Dado o campo email esteja em branco
    Entao valido o botao desativado


  Cenario: Cadastre-se na nossa newslette - email Invalido - Pagina home
    Quando preencho campo nome com NomeTest test
    E preencho campo email com email@test
    Entao valido o botao desativado


  Cenario: Cadastre-se na nossa newslette - dados valido - Pagina home
    Quando preencho campo nome com NomeTest teste
    E preencho campo email com email@test.com
    E clico no Botao cadastrar newsletter
    Entao valido modal com a mensagem INCLUSÃO REALIZADA COM SUCESSO


