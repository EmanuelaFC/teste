import time

from behave import given, then, when

from pages.rodapePage import RodapePage


@given(u'que estou em uma pagina da tele sena')
def step_impl(context):
    context.rodape = RodapePage(context.browser)
    context.rodape.paginaHome()


""" --------------------------------------------- Redes sociais ----------------------------------------------"""


@when(u'clico no icone facebook')
def step_impl(context):
    context.rodape.clicarIconeFacebook()


@then(u'valido o direcionamento para pagina facebook')
def step_impl(context):
    time.sleep(1)
    context.rodape.verificarSeEstaNaPaginaFacebook()


@when(u'clico no icone instagram')
def step_impl(context):
    context.rodape.clicarIconeInstagram()


@then(u'valido o direcionamento para pagina instagram')
def step_impl(context):
    time.sleep(1)
    context.rodape.verificarSeEstaNaPaginaInstagram()


@when(u'clico no icone youtube')
def step_impl(context):
    context.rodape.clicarIconeYoutube()


@then(u'valido o direcionamento para pagina youtube')
def step_impl(context):
    time.sleep(1)
    try:
        context.rodape.verificarSeEstaNaPaginaYoutube()
    except:
        context.rodape.verificarSeEstaNaPaginaYoutube2()


@when(u'clico no icone twitter')
def step_impl(context):
    context.rodape.clicarIconeTwitter()


@then(u'valido o direcionamento para pagina twitter')
def step_impl(context):
    time.sleep(1)
    context.rodape.verificarSeEstaNaPaginaTwitter()


""" --------------------------------------------- navBar menu rodape ----------------------------------------------"""


@when(u'clico no menu do rodape comprar tele senas')
def step_impl(context):
    context.rodape.clicarNavbarRodapeCompra()


@then(u'verifico o direcionamento para pagina compra')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaCompraPasso1()


@when(u'clico no menu do rodape resultados')
def step_impl(context):
    context.rodape.cicarNavBarRodapeResultados()


@then(u'verifico o direcionamento para pagina resultado')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaResultado()


@when(u'clico no menu do rodape promocoes')
def step_impl(context):
    context.rodape.cicarNavBarRodapePromocoes()


@then(u'verifico o direcionamento para pagina promocoes')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaPromocoes()


@when(u'clico no menu do rodape resgates')
def step_impl(context):
    context.rodape.cicarNavBarRodapeResgates()


@then(u'verifico o direcionamento para pagina resgate')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaResgate()


@when(u'clico no menu do rodape cadastrar tele sena deslogado')
def step_impl(context):
    context.rodape.cicarNavBarRodapeCadatrarTeleSena()


@then(u'verifico o direcionamento para pagina login')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaLogin()


@when(u'clico no menu do rodape minhas tele senas deslogado')
def step_impl(context):
    context.rodape.cicarNavBarRodapeMinhasTeleSenas()


# """ ----------------------------------   Institucional   ----------------------------------------------------------"""

@when(u'clico no link A TELE SENA')
def step_impl(context):
    context.rodape.clicarNoLinkATeleSena()


@then(u'valido do direcionamento para pagina a tele sena')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaATeleSena()


@when(u'clico no link Assessoria de Imprensa')
def step_impl(context):
    context.rodape.clicarNoLinkAssessoriaDeImprensa()


@then(u'valido do direcionamento para pagina assessoria de imprensa')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaAssessoriaDeImprensa()


""" ----------------------------------   Suporte Online   ----------------------------------------------------------"""


@when(u'clico no link Acesse a central de atendimento')
def step_impl(context):
    context.rodape.clicarNoLinkFAQ()


@then(u'valido do direcionamento para pagina atendimento')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaAtendimento()


# ----------------------------------   Termos do site   ------------------------------------------------------

@when(u'clico no link Termos de uso')
def step_impl(context):
    context.rodape.clicarNoLinkTermosDeUso()


@then(u'valido o direcionamento para pagina Termos de uso')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaTermosDeUso()


@when(u'clico no link politica de privacidade')
def step_impl(context):
    context.rodape.clicarNoLinkPoliticaDePrivacidade()


@then(u'valido o direcionamento para pagina politica de privacidade')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaPoliticaDePrivacidade()

@when(u'clico no link politica de cookies')
def step_impl(context):
    context.rodape.clicarNoLinkPoliticaDeCookies()


@then(u'valido o direcionamento para pagina politica de cookies')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaPoliticaDeCookies()


@when(u'clico no link termos legais')
def step_impl(context):
    context.rodape.clicarNoLinkTermosLegais()


@then(u'valido o direcionamento para pagina termos legais')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaTermosLegais()


@when(u'clico no link condicoes gerais')
def step_impl(context):
    context.rodape.clicarNoLinkCondicoesGerais()


@then(u'valido o direcionamento para pagina condicoes gerais')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaCondicoesGerais()


### ----------------------------------   Links GSS   ------------------------------------------------------

@when(u'clico no link Grupo ss')
def step_impl(context):
    context.rodape.clicarNoLinkGss()


@then(u'valido o direcionamento para pagina Grupo ss')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaGss()


@when(u'clico no link Lideranca capitalizacao')
def step_impl(context):
    context.rodape.clicarNoLinkLiderancaCapitalizacao()


@then(u'valido o direcionamento para pagina Lideranca capitalizacao')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaLiderancaCapitalizacao()


@when(u'clico no link jequiti')
def step_impl(context):
    context.rodape.clicarNoLinkJequiti()


@then(u'valido o direcionamento para pagina jequiti')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaJequiti()


@when(u'clico no link sbt')
def step_impl(context):
    context.rodape.clicarNoLinkSBT()


@then(u'valido o direcionamento para pagina sbt')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaSBT()


# ------------------------------------------ numero da susep

@then(u'valido no rodape o numero susep')
def step_impl(context):
    context.rodape.validarNumeroSUSEP()


# ----------------------------------------------link susep rodape
@when(u'clico no link do site susep')
def step_impl(context):
    context.rodape.clicarNoLinkSUSEP()


@then(u'valido o direcionamento para pagina da susep')
def step_impl(context):
    time.sleep(2)
    context.rodape.verificarSeEstaNaPaginaSUSEP()


# --------------------------------------------Baixe o novo app da Tele Sena e tenha tudo em suas mãos!
@when(u'clico no icone app store')
def step_impl(context):
    context.rodape.clicarNaAppStore()


@then(u'valido o direcionamento para pagina da app store')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaAppStore()


@when(u'clico no icone google play')
def step_impl(context):
    context.rodape.clicarNaGooglePlay()


@then(u'valido o direcionamento para pagina da google play')
def step_impl(context):
    context.rodape.verificarSeEstaNaPaginaGooglePlay()
