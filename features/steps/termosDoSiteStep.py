from behave import given, then, when

from pages.termosDoSitePage import TermosDoSitePage


@given(u'que estou na pagina termo de uso')
def step_impl(context):
    context.termo = TermosDoSitePage(context.browser)
    context.termo.paginaTermoDeUso()


@given(u'que estou na pagina politica de privacidade')
def step_impl(context):
    context.termo = TermosDoSitePage(context.browser)
    context.termo.paginaPoliticaDePrivacidade()


@given(u'que estou na pagina termos legais')
def step_impl(context):
    context.termo = TermosDoSitePage(context.browser)
    context.termo.paginaTermosLegais()


@then(u'valido o direcionamento de termos para pagina home')
def step_impl(context):
    context.termo.verificarSeEstaNaPaginaHome()


# ------------------------------------ breadcrumbs termo de uso para home
@when(u'clico no link breadcrumb home da pagina termo de uso')
def step_impl(context):
    context.termo.clicoNobreadCrumbHome()


# ------------------------------------ alidar link da pagina termo de uso para <link>
@when(u'clico no tele sena texto destaque')
def step_impl(context):
    context.termo.clicoNoLinkTeleSenaTextoDestaque()


@when(u'clico no tele sena I')
def step_impl(context):
    context.termo.clicoNoLinkTeleSenaI()


@when(u'clico no promocoes I')
def step_impl(context):
    context.termo.clicoNoLinkPromocoesI()


@then(u'valido o direcionamento de termos para pagina promocoes')
def step_impl(context):
    context.termo.verificarSeEstaNoSitePromocoes()


@when(u'clico no servico de atendimento ao cliente II')
def step_impl(context):
    context.termo.clicoNoLinkServicoAtendimentoAoClienteII()


@then(u'valido o direcionamento de termos para pagina pagina atendimento')
def step_impl(context):
    context.termo.verificarSeEstaNaPaginaAtendimento()


@when(u'clico no tele sena VI')
def step_impl(context):
    context.termo.clicoNoLinkTeleSenaVI()


# ------------------------ breadcrumbs politica de privacidade para home
@when(u'clico no link breadcrumb home da pagina politica de privacidade')
def step_impl(context):
    context.termo.clicoNobreadCrumbHome()


# ------------------------ breadcrumbs breadcrumbs termos legais para home


@when(u'clico no link breadcrumb home da pagina termos legais')
def step_impl(context):
    context.termo.clicoNobreadCrumbHome()


# ------------------------- verificar numero da susep no texto destaque - pagina termos legais

@then(u'valido o numero da susep na pagina termos legais')
def step_impl(context):
    context.termo.verificarNumeroSusepTermosLegais()


# --------------------------- validar link susep - termos legais
@when(u'clico no link da susep')
def step_impl(context):
    context.termo.clicoNoLinkSusep()


@then(u'valido o direcionamento da pagina termos legais para o site da susep')
def step_impl(context):
    context.termo.verificarSeEstaNaPaginaSUSEP()


