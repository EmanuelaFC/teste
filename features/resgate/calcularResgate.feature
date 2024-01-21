
Funcionalidade: selecionar ano e verificar a exibicao das campanhas

  Contexto: abrir a pagina resgate
    Dado que estou na pagina calculo de resgate


  Cenario: informando código de loterico invalido
    Quando preencho codigo loterico com dados invalidos 12345678
    E clico no botao <Pesquisar>
    Entao valido o modal calcular resgate com a mensagem LOTÉRICO NÃO ENCONTRADO


  Cenario: informando código de loterico válido
    Quando preencho codigo loterico com dados validos 30014395
    E clico no botao <Pesquisar>
    Entao valido a exibicao dos dados do loterico contendo a THOME SESAFIM DE COUTO


  Esquema do Cenario: codigo loterico valido - imprimir
    Quando preencho codigo loterico com dados validos 30014395
    E clico no botao Pesquisar
    E insiro o ano do calculo de resgate <ANO>
    E insiro a campanha do calculo de resgate <CAMPANHA>
    E informo a quantidade do calculo <QUANTIDADE>
    E clico no botao adicionar
    E clico no botao imprimir
    Entao verifico se estou na pagina de impressao do calculo de resgate
    E verifico a exibicao do ano na tela de calculo de resgate impressao <ANO>
    E verifico a campanha na tela de calculo de resgate impressao <CAMPANHA IMPRESSAO>
    E verifico a quantidade na tela de calculo de resgate impressao <QUANTIDADE>

  Exemplos:
  |ANO|CAMPANHA|QUANTIDADE|CAMPANHA IMPRESSAO|
  |2021|0|2| ANO NOVO/2021|


  Esquema do Cenario: quantidade de resgate com dados em branco
    Quando preencho codigo loterico com dados validos 30014395
    E clico no botao Pesquisar
    E insiro o ano do calculo de resgate <ANO>
    E insiro a campanha do calculo de resgate <CAMPANHA>
    E pressiono o botao TAB
    Entao verifico a mensagem <MSG> no campo quantidade


  Exemplos:
  |ANO|CAMPANHA|MSG|
  |2021|0|Por favor insira um número válido maior que zero.|

  Cenario: imprimir calculo com dados em branco
    Quando preencho codigo loterico com dados validos 30014395
    E clico no botao <Pesquisar>
    Entao valido que o botao Imprimir Calculo esta desabilitado


  Esquema do Cenario: adicionando dados da mesma campanha
    Quando preencho codigo loterico com dados validos 30014395
    E clico no botao Pesquisar
    E insiro o ano do calculo de resgate <ANO>
    E insiro a campanha do calculo de resgate <COD_CAMPANHA>
    E informo a quantidade do calculo <QUANTIDADE>
    E clico no botao adicionar
    E insiro o ano do calculo de resgate <ANO>
    E insiro a campanha do calculo de resgate <COD_CAMPANHA>
    E informo a quantidade do calculo <QUANTIDADE>
    E clico no botao adicionar
    Entao verifico a mensagem do modal com a campanha <CAMPANHA> e a <QUANTIDADE>

  Exemplos:
  |ANO|COD_CAMPANHA|QUANTIDADE|CAMPANHA|
  |2021|0|8|ANO NOVO/2021|


  Esquema do Cenario: Imprimir calculo e validar dados exibidos
    Quando insiro o ano do calculo de resgate <ANO>
    E insiro a campanha do calculo de resgate <CAMPANHA>
    E informo a quantidade do calculo <QUANTIDADE>
    E clico no botao adicionar
    E clico no botao imprimir
    Entao verifico se estou na pagina de impressao do calculo de resgate
    E verifico a exibicao do ano sem loterico na tela de calculo de resgate impressao <ANO_SEM_LOTERICO>
    E verifico a campanha sem loterico na tela de calculo de resgate impressao <CAMPANHA_IMPRESSAO_SEM_LOTERICO>
    E verifico a quantidade sem loterico na tela de calculo de resgate impressao <QUANTIDADE_SEM_LOTERICO>

  Exemplos:
  |ANO|CAMPANHA|QUANTIDADE|ANO_SEM_LOTERICO|CAMPANHA_IMPRESSAO_SEM_LOTERICO |QUANTIDADE_SEM_LOTERICO|
  |2021|0|2|2021| ANO NOVO/2021|2|


    Esquema do Cenario: Somatória dos resgates com dados válidos
    Quando insiro o ano do calculo de resgate <ANO>
    E insiro a campanha do calculo de resgate <CAMPANHA>
    E informo a quantidade do calculo <QUANTIDADE>
    E clico no botao adicionar
    E clico no botao imprimir
    Entao verifico se estou na pagina de impressao do calculo de resgate

  Exemplos:
  |ANO|CAMPANHA|QUANTIDADE|
  |2021|0|2|