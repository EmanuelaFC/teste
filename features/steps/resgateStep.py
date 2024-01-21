from behave import given, when, then

from pages.resgatePage import ResgatePage


@given(u'que estou na pagina de resgate')
def step_impl(context):
    context.resgate = ResgatePage(context.browser)
    context.resgate.paginaResgate()


# ----------------------------------------- breadcrumb home > resgate


@when(u'clico no breadcrumb home na pagina resgate')
def step_impl(context):
    context.resgate.clicarNoBreadCrumb1()


@then(u'verifico o direcionamento para home')
def step_impl(context):
    context.resgate.verificarSeEstaNaPaginaHome()


# --------------------------------------------selecionar ano <ano> da pagina de resgate
@when(u'seleciono o resgate do ano {ano}')
def step_impl(context, ano):
    context.resgate.selecionoOAnoDeResgate(ano)


@then(u'verifico o direcionamento para a pagina {ano} de resgate')
def step_impl(context, ano):
    context.resgate.validarPaginaResgasteDoAno(ano)


# --------------------------------------clicar nos botoes (resgate tele sena e calcular resgate) deslogado
@when(u'clico no botao RESGATAR TELE SENA')
def step_impl(context):
    context.resgate.clicarNoBotaoResgatarTeleSena()


@then(u'valido o direcionamento da pagina resgate para pagina login')
def step_impl(context):
    context.resgate.verificarSeEstaNaPaginaLogin()


@when(u'clico no botao CALCULAR RESGATE')
def step_impl(context):
    context.resgate.clicarNoBotaoCalcuarResgate()


@then(u'valido o direcionamento da pagina resgate para pagina calcular resgate')
def step_impl(context):
    context.resgate.validarSeEstarNaPaginaCalcularResgate()


# ------------------------------------------- dados ivalidos

@when(u'preencho codigo loterico com dados invalidos {dado}')
def step_impl(context, dado):
    context.resgate.preencherCodigoLoterico(dado)


# --------------------------------------cenarios de codigo de loterico
@given(u'que estou na pagina calculo de resgate')
def step_impl(context):
    context.resgate = ResgatePage(context.browser)
    context.resgate.irParaPaginaResgate()


@when(u'clico no botao <Pesquisar>')
def step_impl(context):
    context.resgate.clicarNoBotaoPesquisar()


@when(u'preencho codigo loterico com dados validos {dado}')
def step_impl(context, dado):
    context.resgate.preencherCodigoLoterico(dado)


@then(u'valido o modal calcular resgate com a mensagem {msg}')
def step_impl(context, msg):
    context.resgate.verificarMensagemCodigoLoterico(msg)


@when(u'preencho cogido loterico com dados validos {dado}')
def step_impl(context, dado):
    context.resgate.preencherCodigoLoterico(dado)


@then(u'valido a exibicao dos dados do loterico contendo a {msg}')
def step_impl(context, msg):
    context.resgate.verificarNomeCodigoLoterico(msg)


@when(u'informo a quantidade do calculo {dado}')
def step_impl(context, dado):
    context.resgate.informarQuantidadeResgate(dado)


@when(u'clico no botao <adicionar>')
def step_impl(context):
    context.resgate.clicarNoBotaoAdicionar()


@when(u'clico no botao <imprimir>')
def step_impl(context):
    context.resgate.clicarNoBotaoImprimirCalculo()


@then(u'valido a exibicao dos dados na tela de calculo de resgate {dado}')
def step_impl(context, dado):
    context.resgate.verificarDadosTelaResgate(dado)


@when(u'insiro o ano do calculo de resgate {ano}')
def step_impl(context, ano):
    context.resgate.escolhoAnoCalculoResgate(ano)


@when(u'insiro a campanha do calculo de resgate {campanha}')
def step_impl(context, campanha):
    context.resgate.escolhoCampanhaCalculoResgate(campanha)


@when(u'clico no botao Pesquisar')
def step_impl(context):
    context.resgate.clicarNoBotaoPesquisar()


@when(u'clico no botao adicionar')
def step_impl(context):
    context.resgate.clicarNoBotaoAdicionarCalculo()


@when(u'clico no botao imprimir')
def step_impl(context):
    context.resgate.clicarNoBotaoImprimirCalculo()


@then(u'verifico se estou na pagina de impressao do calculo de resgate')
def step_impl(context):
    context.resgate.validarSeEstarNaPaginaImpressaoCalculoResgate()


@then(u'verifico a exibicao do ano na tela de calculo de resgate impressao {ano}')
def step_impl(context, ano):
    context.resgate.validarDadosAnoTelaCalculoResgate(ano)


@then(u'verifico a campanha na tela de calculo de resgate impressao {campanha}')
def step_impl(context, campanha):
    context.resgate.validarDadosCampanhaTelaCalculoResgate(campanha)


@then(u'verifico a quantidade na tela de calculo de resgate impressao {QUANTIDADE}')
def step_impl(context, QUANTIDADE):
    context.resgate.validarDadosQuantidadeTelaCalculoResgate(QUANTIDADE)


@when(u'pressiono o botao TAB')
def step_impl(context):
    context.resgate.clicarNoBotaoTab()


@then(u'verifico a mensagem {MSG} no campo quantidade')
def step_impl(context, MSG):
    context.resgate.verificarMensagemQuantidadeEmBranco(MSG)


@then(u'valido que o botao Imprimir Calculo esta desabilitado')
def step_impl(context):
    context.resgate.verificarBotaoImprimirCalculo()


@then(u'verifico a mensagem do modal com a campanha {CAMPANHA} e a {QUANTIDADE}')
def step_impl(context, CAMPANHA, QUANTIDADE):
    soma = int(QUANTIDADE) * 2
    context.resgate.verificarMensagemMesmaCampanha(
        f"""Você acrescentou mais títulos a campanha já incluída de {CAMPANHA}.
A quantidade de títulos para esta campanha passou de {QUANTIDADE} para {str(soma)}.""")


@then(u'verifico a exibicao do ano sem loterico na tela de calculo de resgate impressao {ano_sem_loterico}')
def step_impl(context, ano_sem_loterico):
    context.resgate.validarDadosAnoTelaCalculoResgateSemLoterico(ano_sem_loterico)


@then(u'verifico a campanha sem loterico na tela de calculo de resgate impressao {campanha_impressao_sem_loterico}')
def step_impl(context, campanha_impressao_sem_loterico):
    context.resgate.validarDadosCampanhaTelaCalculoResgateSemLoterico(campanha_impressao_sem_loterico)


@then(u'verifico a quantidade sem loterico na tela de calculo de resgate impressao {quantidade_sem_loterico}')
def step_impl(context, quantidade_sem_loterico):
    context.resgate.validarDadosQuantidadeTelaCalculoResgateSemLoterico(quantidade_sem_loterico)
