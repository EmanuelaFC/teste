from behave import given, when, then

from pages.promocoesPage import PromocaoPage


@given(u'que estou em uma pagina de promocao')
def step_impl(context):
    context.promo = PromocaoPage(context.browser)
    context.promo.paginaPromocoes()


# ----------------------- Promoções vigentes e não vigentes

@when(u'seleciono todas as promocoes')
def step_impl(context):
    context.promo.selecionarTodasAsPromocoes()


@then(u'verifico se a primeira campanha esta vigente')
def step_impl(context):
    context.promo.verificarCampanhaAtiva()


@then(u'as demais nao estao vigente')
def step_impl(context):
    context.promo.verificarCampanhaEncerrada()


# ---------------------- navegacao no site promocao


@when(u'clico no link {pagina} da campanha de promocao {campanha}')
def step_impl(context, pagina, campanha):
    context.promo.clicarNoLinkPromocoes(pagina, campanha)


@then(u'verifico o direcionamento para a pagina de promocoes {pagina}')
def step_impl(context, pagina):
    context.promo.verificarSeEstarNaPaginaPromocoes(pagina)
