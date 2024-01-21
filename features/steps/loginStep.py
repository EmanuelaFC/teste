from behave import given, when, then

from pages.loginPage import LoginPage


@given(u'que estou na pagina login')
def step_impl(context):
    context.login = LoginPage(context.browser)
    context.login.paginaLogin()


# ------------------------------Link breadCrumb pagina login
@when(u'clico no link breadcrumb home da pagina login')
def step_impl(context):
    context.login.clicarNoBreadcrumbHome()


@then(u'valido o direcionamento da pagina login para a página home')
def step_impl(context):
    context.login.verificarSeEstaNaPaginaHome()


# ---------------------------- esqueci minha senha
@when(u'clico no link esqueci minha senha')
def step_impl(context):
    context.login.clicarNoLinkEsqueciMinhaSenha()


@then(u'valido o direcionamento da pagina login para esqueci minha senha')
def step_impl(context):
    context.login.verificarSeEstaNaPaginaEsqueciMinhaSenha()


# ----------------------------Cadastre-se agora
@when(u'clico no link cadastre se agora')
def step_impl(context):
    context.login.clicarNoLinkCadastreSeAgora()


@then(u'valido o direcionamento da pagina login para cadastro')
def step_impl(context):
    context.login.verificarSeEstaNaPaginaCadastro()


# --------------------------------- Não recebi o e-mail de ativação
@when(u'clico no link Nao recebi o e-mail de ativacao')
def step_impl(context):
    context.login.clicarNoLinkNaoRecebiOEmailDeAtivacao()


@then(u'valido o modal com as instrucoes {msg}')
def step_impl(context, msg):
    context.login.verificarMensagemModal(msg)


# ---------------------------------- Login com cpf inválidos

@when(u'preencho o campo cpf com {dados}')
def step_impl(context, dados):
    context.login.preencherCpf(dados)


@when(u'clico no campo senha')
def step_impl(context):
    context.login.clicarNoCampoSenha()


@then(u'verifico a mensagem de erro {msg} no campo cpf')
def step_impl(context, msg):
    context.login.verificarMensagemDeErroCpf(msg)


# ---------------------------------- Campo obrigatorio - dados em branco
@when(u'o campo cpf esteja em branco')
def step_impl(context):
    context.login.apertarTabNoCampoCpf()


@when(u'o campo senha esteja em branco')
def step_impl(context):
    context.login.apertarTabNoCampoSenha()


@then(u'valido a mensagem {msg} no campo cpf na pagina login')
def step_impl(context, msg):
    context.login.verificarMensagemDeErroSenha(msg)


@then(u'valido a mensagem {msg} no campo senha na pagina login')
def step_impl(context, msg):
    context.login.verificarMensagemDeErroSenha(msg)


@then(u'valido que o botao fazer login esteja desabilitado')
def step_impl(context):
    context.login.validarBotaoDesativado()
