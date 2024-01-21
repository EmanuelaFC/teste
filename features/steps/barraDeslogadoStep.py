from behave import given, then, when

from pages.barraDeNavegacaoPage import BarraDeNavegacaoPage


@given(u'que eu estou na home')
def step_impl(context):
    context.barraDeNavegacao = BarraDeNavegacaoPage(context.browser)
    context.barraDeNavegacao.paginaHome()


@when(u'clico na logo')
def step_impl(context):
    context.barraDeNavegacao.clicarNaLogo()


@then(u'valido o direcionamento para pagina home')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaHome()


@when(u'clico no menu resultado')
def step_impl(context):
    context.barraDeNavegacao.clicarMenuResultado()


@then(u'valido o direcionamento para pagina resutado')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaResultado()


@when(u'clico no menu comprar telesena')
def step_impl(context):
    context.barraDeNavegacao.clicarMenuComprarTelesena()


@then(u'valido o direcionamento para pagina compra passo1')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaCompraPasso1()


@when(u'clico no menu resgate')
def step_impl(context):
    context.barraDeNavegacao.clicarMenuResgate()


@then(u'valido o direcionamento para pagina resgate')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaResgate()


@when(u'clico no menu promocoes')
def step_impl(context):
    context.barraDeNavegacao.clicarMenuPromocoes()


@then(u'valido o direcionamento para pagina promocoes')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaPromocoes()


@when(u'clico no menu cadastrar tele sena')
def step_impl(context):
    context.barraDeNavegacao.clicarMenuCadastrarTeleSena()


@then(u'valido o direcionamento para pagina login')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaLogin()


@when(u'clico no menu entre ou cadastre-se')
def step_impl(context):
    context.barraDeNavegacao.clicarMenuEntreOuCadastreSe()


@when(u'clico no icone carrinho deslogado')
def step_impl(context):
    context.barraDeNavegacao.clicarIconeCarrinhoDeslogado()


@then(u'valido o direcionamento para pagina de compra carrinho')
def step_impl(context):
    context.barraDeNavegacao.verificarSeEstaNaPaginaCompraCarrinho()
