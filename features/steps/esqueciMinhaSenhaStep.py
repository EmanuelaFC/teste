import time

from behave import given, when, then

from pages.esqueciMinhaSenhaPage import EsqueciMinhaSenhaPage
from utils.utils import Utils as info


@given(u'que estou na pagina esqueci minha senha')
def step_impl(context):
    context.esqueciMinhaSenha = EsqueciMinhaSenhaPage(context.browser)
    context.esqueciMinhaSenha.paginaEsqueciMinhaSenha()


# ------------------------ link breadcrumb

@when(u'clico no link breadcrumb login')
def step_impl(context):
    context.esqueciMinhaSenha.clicarBreadCrumb2()


@then(u'valido o direcionamento para a página login')
def step_impl(context):
    context.esqueciMinhaSenha.verificarSeEstaNaPaginaLogin()


@when(u'clico no link breadcrumb home')
def step_impl(context):
    context.esqueciMinhaSenha.clicarBreadCrumb1()


@then(u'valido o direcionamento para a página home')
def step_impl(context):
    context.esqueciMinhaSenha.verificarSeEstaNaPaginaHome()


# ------------------------- clicar no botao cancela
@when(u'clico no botao cancelar')
def step_impl(context):
    context.esqueciMinhaSenha.clicarNoBotaoCancelar()


# --------------------botao enviar codigo desativado com dados em branco

@given(u'que o campo cpf esteja em branco')
def step_impl(context):
    context.esqueciMinhaSenha.dadosEmBrancoNoCampoCPF()


@then(u'valido o botao enviar codigo desativado')
def step_impl(context):
    context.esqueciMinhaSenha.validarBotaoDesativado()


# ------------------------------Cpf invalido

@when(u'preencho o campo com dados invalidos {dado}')
def step_impl(context, dado):
    context.esqueciMinhaSenha.preencherCampoCpf(dado)


@then(u'valido a mensagem de erro')
def step_impl(context):
    context.esqueciMinhaSenha.validarMensagemDeErro('Preencha seu CPF corretamente.')


# -----------------------------------Cpf valido mas não cadastrado

@when(u'preencho o campo com  dados validos e nao cadastrado {dado}')
def step_impl(context, dado):
    context.esqueciMinhaSenha.preencherCampoCpf(dado)


@when(u'clico no botao enviar codigo')
def step_impl(context):
    context.esqueciMinhaSenha.clicarNoBotaoEnviarCodigo()


@then(u'valido o modal com a mensagem de sucesso')
def step_impl(context):
    context.esqueciMinhaSenha. \
        validarMensagemModal('Foi enviado um e-mail para ' + info.EMAIL_CADASTRADO +
                             ' com orientações para reativação de sua conta')


# -----------------------------  Informar cpf com dados válidos e cadastrados

@when(u'preencho o campo com dados validos')
def step_impl(context):
    context.esqueciMinhaSenha.preencherCampoCpf(info.CPF_CADASTRADO)


@when(u'clico no botao ok do modal')
def step_impl(context):
    context.esqueciMinhaSenha.clicarBotaoOkModal()


@then(u'clico no botao ok do modal')
def step_impl(context):
    context.esqueciMinhaSenha.clicarBotaoOkModal()


@then(u'valido o direcionamento para ativacao do esqueci a minha senha')
def step_impl(context):
    context.esqueciMinhaSenha.verificarSeEstaNaPaginaAtivacaoEsqueciMinhaSenha()


# -------------------------------------- pagina ativação
# -------------------------------- breadcrumb
@when(u'clico no link breadcrumb Esqueci Minha Senha')
def step_impl(context):
    context.esqueciMinhaSenha.clicarBreadCrumb2()


@then(u'valido o direcionamento para a página Esqueci Minha Senha')
def step_impl(context):
    context.esqueciMinhaSenha.verificarSeEstaNaPaginaEsqueciMinhaSenha()


@when(u'clico no link breadcrumb login pagina ativacao')
def step_impl(context):
    context.esqueciMinhaSenha.clicarBreadCrumb1()


@then(u'valido o direcionamento para a página login pagina ativacao')
def step_impl(context):
    context.esqueciMinhaSenha.verificarSeEstaNaPaginaLogin()


# --------------------------------clicar no botao cancela

@when(u'clico no botao cancelar ativacao')
def step_impl(context):
    context.esqueciMinhaSenha.clicarNoBotaoCancelarAtivacao()


# ---------------------------------  codigo de ativao em branco
@given(u'que o campo do codigo de ativacao esteja em branco')
def step_impl(context):
    context.esqueciMinhaSenha.campoCodigoDeAtivacaoEmBranco()


@then(u'valido que o botao confirmar codigo esteja desativado')
def step_impl(context):
    context.esqueciMinhaSenha.validarBotaoConfirmarCodigoDesativado()


# --------------------------------codigo de ativação invalida
@when(u'preencho o campo de codigo de ativacao com {dado}')
def step_impl(context, dado):
    context.esqueciMinhaSenha.preencherCampoCodigoDeAtivacao(dado)


@when(u'clico no botao confirmar codigo')
def step_impl(context):
    context.esqueciMinhaSenha.clicarBotaoConfirmarCodigo()


@then(u'valido o modal com a mensagem {msg}')
def step_impl(context, msg):
    context.esqueciMinhaSenha.validarMensagemModal(msg)


# -------------------- clicar no link enviar codigo novamente
@when(u'clico no link enviar o codigo novamente')
def step_impl(context):
    context.esqueciMinhaSenha.clicarNoLinkEnviarOCodigoNovamente()


# -----------------------------------------------------ir para renovacao de senha

@when(u'obtenho o codigo de ativacao')
def step_impl(context):
    context.chave = context.esqueciMinhaSenha.obterChaveDeAtivacao(info.CPF_CADASTRADO)


@when(u'preencho com o codigo de ativacao valido')
def step_impl(context):
    context.esqueciMinhaSenha.preencherCampoCodigoDeAtivacao(context.chave)


@then(u'valido que estou na pagina alterar senha')
def step_impl(context):
    context.esqueciMinhaSenha.verificarSeEstaNaPaginaRenovarSenha()


# -------------------------------------------------------- pagina de renovacao de senha - esqueco minha senha
@when(u'clico no icone olho para exibir senha')
def step_impl(context):
    context.esqueciMinhaSenha.clicarNoIconeOlhoCampoSenha()


# ------------------------------------------- cancelar renovacao de senha
@when(u'clico no botao cancelar renovacao')
def step_impl(context):
    context.esqueciMinhaSenha.clicarNoBotaoCancelarRenovacao()


@then(u'valido o direcionamento de renovacao de senha para a pagina de login')
def step_impl(context):
    context.esqueciMinhaSenha.verificarSeEstaNaPaginaLogin()


# ------------------------------------------- dados em branco

@when(u'aperto a tecla tab no campo senha renovacao')
def step_impl(context):
    context.esqueciMinhaSenha.apertarTabCampoSenha()
    time.sleep(3)


@when(u'aperto a tecla tab no campo confirmar senha renovacao')
def step_impl(context):
    context.esqueciMinhaSenha.apertarTabCampoConfirmarSenha()


@then(u'valido a mensagem de {msg} no campo senha')
def step_impl(context, msg):
    context.esqueciMinhaSenha.verificarMensagemDeErroCampoSenha(msg)


@then(u'valido a mensagem de {msg} no campo confirmar senha')
def step_impl(context, msg):
    context.esqueciMinhaSenha.verificarMensagemDeErroCampoConfirmarSenha(msg)


# -------------------------------------------------- dados invalidos campo senha
@when(u'preencho o campo senha com {dado}')
def step_impl(context, dado):
    context.esqueciMinhaSenha.preencherCampoSenha(dado)


@then(u'valido o a mensagem de erro {msg}')
def step_impl(context, msg):
    context.esqueciMinhaSenha.verificarMensagemDeErroCampoSenha(msg)


@then(u'valido o botao confirmar alteracao esta desabilitado')
def step_impl(context):
    context.esqueciMinhaSenha.validarBotaoConfirmarAlteracaoDesativado()


# -------------------------------------------------- dados invalidos campo confirmar senha

@when(u'preencho o campo confirmar senha com {msg}')
def step_impl(context, msg):
    context.esqueciMinhaSenha.preencherCampoConfirmarSenha(msg)


@when(u'clico no icone olho para exibir confirmar senha')
def step_impl(context):
    context.esqueciMinhaSenha.clicarNoIconeOlhoCampoConfirmarSenha()


@then(u'valido o campo confirmar senha com a mensagem de erro {msg}')
def step_impl(context, msg):
    context.esqueciMinhaSenha.verificarMensagemDeErroCampoConfirmarSenha(msg)


# ---------------------------------------- informar senha igual a anterior

@when(u'preencho o campo com a senha anterior')
def step_impl(context):
    context.esqueciMinhaSenha.preencherCampoSenha(info.SENHA_CADASTRADO)


@when(u'preencho o campo confirmar com a senha anterior')
def step_impl(context):
    context.esqueciMinhaSenha.preencherCampoConfirmarSenha(info.SENHA_CADASTRADO)


@when(u'clico no botao confirmar alteracao')
def step_impl(context):
    context.esqueciMinhaSenha.clicarNoBotaoConfirmarAlteracao()
