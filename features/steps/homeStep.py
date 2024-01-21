from behave import given, when, then

from pages.homePage import HomePage


@given(u'que estou na pagina home')
def step_impl(context):
    context.home = HomePage(context.browser)
    context.home.paginaHome()


# ----------------------- direcionamento pagina compra passo1 clicando no banner
@when(u'clico no banner da campanha')
def step_impl(context):
    context.home.clicarNoBannerCampanha()


# -----------------  mensagem de cookie
@then(u'verifico o texto da mensagem do cookie {msg}')
def step_impl(context, msg):
    context.home.validarMensagemCookie(msg)


@then(u'validar se ta ativo o botao Entendi')
def step_impl(context):
    context.home.validarBotaoCookie()


# --------------------------verificando o direcionamento clicando no botao <botao>
@when(u'clico no botao resultado')
def step_impl(context):
    context.home.clicarBotaoResultado()


@then(u'valido o direcionamento da pagina home pra resultado')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaResultado()


@when(u'clico no botao ir para minhas tele senas deslogado')
def step_impl(context):
    context.home.clicarNoBotaoIrParaMinhasTeleSenas()


@then(u'valido o direcionamento da pagina home pra login')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaLogin()


@when(u'clico no botao compre ja a sua')
def step_impl(context):
    context.home.clicarBotaoCompreJaASua()


@then(u'valido o direcionamento da pagina home pra compra passo1')
def step_impl(context):
    context.home.verificarSeEstaNaPaginaCompraPasso1()


@when(u'clico no botao cadastre aqui deslogado')
def step_impl(context):
    context.home.clicarBotaoCadastreAqui()


@when(u'clico no botao compre agora')
def step_impl(context):
    context.home.clicarBotaoCompreAgora()


# -------------------------- Cadastre-se na nossa newslette - botao desativado(dados em branco)


@given(u'que o campo nome esteja em branco')
def step_impl(context):
    context.home.tabNoCampoNome()


@given(u'o campo email esteja em branco')
def step_impl(context):
    context.home.tabNoCampoEmail()


@then(u'valido o botao desativado')
def step_impl(context):
    context.home.conferirBotaoCadastrarNewsLetterDesativado()


# ----------------------------- Cadastre-se na nossa newslette - botao desativado(nome em branco)


@when(u'preencho campo email com {email}')
def step_impl(context, email):
    context.home.preencherCampoEmail(email)


# ----------------------------- Cadastre-se na nossa newslette - botao desativado(email em branco)


@when(u'preencho campo nome com {nome}')
def step_impl(context, nome):
    context.home.preencherCampoNome(nome)


# ------------------------------- Cadastre-se na nossa newslette - email Invalido

@when(u'clico no Botao cadastrar newsletter')
def step_impl(context):
    context.home.clicarBotaoCadastrarNewsLetter()


@then(u'valido modal com a mensagem {msg}')
def step_impl(context, msg):
    context.home.validarMensagemModalNewsLetter(msg)
