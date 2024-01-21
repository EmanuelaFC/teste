from behave import given, when, then

from pages.resultadosPage import ResultadosPage


@given(u'que estou na pagina de resultado')
def step_impl(context):
    context.resultados = ResultadosPage(context.browser)
    context.resultados.abrirPaginaResultados()


@when(u'clico no breadcrumb home')
def step_impl(context):
    context.resultados.clicarNoBreadCrumbHome()


@then(u'valido o direcionamento para home')
def step_impl(context):
    context.resultados.validarPaginaHome()


# ---------------------------navegacao
@when(u'seleciono o ano {ano}')
def step_impl(context, ano):
    context.resultados.selecionarAno(ano)


@when(u'seleciono a campanha {evento}')
def step_impl(context, evento):
    context.resultados.selecionarEnvento(evento)


@when(u'clico no botao filtrar campanha')
def step_impl(context):
    context.resultados.clicarNoBotaoFiltrarCampanha()


@then(u'valido o direcionamento para a pagina {campanha}')
def step_impl(context, campanha):
    context.resultados.validarPaginaResultado(campanha)
