import time

from behave import given, then, when

from pages.cadastroPage import CadastroPage
from utils.utils import Utils as info


@given(u'que estou na pagina cadastro passo1')
def step_impl(context):
    context.cadastro = CadastroPage(context.browser)
    context.cadastro.paginaCadastroPasso1()


@given(u'que estou na pagina cadastro passo2')
def step_impl(context):
    context.cadastro = CadastroPage(context.browser)
    context.cadastro.paginaCadastroPasso2()


@given(u'que estou na pagina cadastro passo3')
def step_impl(context):
    context.cadastro = CadastroPage(context.browser)
    context.cadastro.paginaCadastroPasso3()


## ------------------------------navegar e validar as paginas de cadastro -------------------------------------------
# ------------------------------ navegacao na pagina de cadastro cadastro
@when(u'clico em sim no botao Você é ou tem parentesco com político ou agente público')
def step_impl(context):
    context.cadastro.clicarEmSimPPE()


@then(u'verifico que o botao proximo passo esteja habilitado')
def step_impl(context):
    context.cadastro.verificarBotaoProximoPassoAtivo()


@when(u'clico no botao proximo passo')
def step_impl(context):
    context.cadastro.clicarNoBotaoProximoPasso()


@when(u'preencho o campo email com {dado}')
def step_impl(context, dado):
    context.cadastro.inserirEmail(dado)


@when(u'preencho o campo confirme o seu email com {dado}')
def step_impl(context, dado):
    context.cadastro.inserirConfirmeEmail(dado)


@when(u'preencho o campo cep com {dado}')
def step_impl(context, dado):
    context.cadastro.inserirCEP(dado)


@when(u'preencho o campo numero com {dado}')
def step_impl(context, dado):
    context.cadastro.inserirNumeroEndereco(dado)


# --------------------------------------------------------
@when(u'preencho o campo cpf na pagina login com {cpf}')
def step_impl(context, cpf):
    context.cadastro.inserirCPF(cpf)


@when(u'clico no dados de contato')
def step_impl(context):
    context.cadastro.clicarLinkDadosDeContato()


@then(u'valido o breadcrumb {dado}')
def step_impl(context, dado):
    context.cadastro.validarOBreadCrumb3(dado)


@then(u'valido o direcionamento para pagina cadastro passo2')
def step_impl(context):
    context.cadastro.verificarSeEstaNaPaginaCastroPasso2()


@when(u'clico no senha e aceites')
def step_impl(context):
    context.cadastro.clicarLinkSenhaEAceites()


@then(u'valido o direcionamento para pagina cadastro passo3')
def step_impl(context):
    context.cadastro.verificarSeEstaNaPaginaCastroPasso3()


@when(u'clico no dados pessoais')
def step_impl(context):
    context.cadastro.clicarLinkDadosPessoais()


@then(u'valido o direcionamento para pagina cadastro passo1')
def step_impl(context):
    context.cadastro.verificarSeEstaNaPaginaCastroPasso1()


# ------------------------------------------------- navegação com dados em branco
@then(u'valido o modal cadastro com a mensagem {msg}')
def step_impl(context, msg):
    context.cadastro.verificarMensagemModal(msg)


# ------------------------------botao desabilitado -----------------------------------------------------------
@then(u'verifico que o botao proximo passo esta desabilitado')
def step_impl(context):
    context.cadastro.verificarBotaoProximoPasso()


# ------------------------------cpf invalido -----------------------------------------------------------
@when(u'inserir dados no campo cpf com{cpf}')
def step_impl(context, cpf):
    context.cadastro.inserirCPF(cpf)


@then(u'valido o campo cpf com a mensagem de erro {msg}')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroCPFInvalido(msg)


# -------------------------------nome incompleto------------------------------------------------------------------------
@when(u'preencho o campo nome com dados {nome}')
def step_impl(context, nome):
    context.cadastro.inserirNome(nome)


@then(u'valido a mensagem de erro "Por favor digite seu nome completo"')
def step_impl(context):
    context.cadastro.verificarMensagemDeErroNome("Por favor digite seu nome completo")


##-------------------------------data invalida----------------------------------------------------------------------
@when(u'preencho o campo data de nascimento com dados {dados}')
def step_impl(context, dados):
    context.cadastro.inserirData(dados)


@when(u'preencho o campo data de nascimento com dia {invalido}')
def step_impl(context, invalido):
    context.cadastro.inserirData(invalido)


@when(u'preencho o campo data de nascimento com mes {invalido}')
def step_impl(context, invalido):
    context.cadastro.inserirData(invalido)


@when(u'preencho o campo data de nascimento com ano {invalido}')
def step_impl(context, invalido):
    context.cadastro.inserirData(invalido)


@when(u'preencho o campo data de nascimento com letras {invalido}')
def step_impl(context, invalido):
    context.cadastro.inserirData(invalido)


@then(u'valido a mensagem de erro no campo data {msg}')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroData(msg)


##-------------------------------ja e cadastrado----------------------------------------------------------------------

@when(u'clico no link faca login')
def step_impl(context):
    context.cadastro.clicarLinkFacaLogin()


@then(u'verifico o direcionamento para pagina de login')
def step_impl(context):
    context.cadastro.verificarSeEstaNaPaginaLogin()


##------------------------------------dados em branco - cadastro passo 1 ---------------------------------------------

@when(u'foco no campo cpf')
def step_impl(context):
    context.cadastro.apertarTABNoCPF()


@then(u'verifico a mensagem " {msg}  " no campo cpf')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroCPFInvalido(msg)


@when(u'foco no campo nome')
def step_impl(context):
    context.cadastro.apertarTABNoNome()


@then(u'verifico a mensagem " {msg}  " no campo nome')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroNome(msg)


@when(u'foco no campo data')
def step_impl(context):
    context.cadastro.apertarTABNaData()


@then(u'verifico a mensagem " {msg}  " no campo data')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroData(msg)


##-----------------------------------cpf valido e ja cadastrado ------------------------------------------------------------
@when(u'preencho o campo cpf com dados validos e cadastrado')
def step_impl(context):
    context.cadastro.inserirCPF(info.CPF_CADASTRADO)


@then(u'valido a mensagem {msg} no campo cpf')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroCPFInvalido(msg)


##------------------------------------cadastro passo 2 --------------------------------------------
##----------------------------------------dados em branco--------------------------------------------------------------
@when(u'aperto a tecla tab no campo telefone')
def step_impl(context):
    context.cadastro.apertarTABNoTelefone()


@then(u'valido a mensagem " {msg} " no campo telefone')
def step_impl(context, msg):
    context.cadastro.verificarMensagemTelefoneEmBranco(msg)


@when(u'aperto a tecla tab no campo email')
def step_impl(context):
    context.cadastro.apertarTABNoEmail()


@then(u'valido a mensagem " {msg} " no campo email')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroEmail(msg)


@when(u'aperto a tecla tab no campo Confirme o seu E-mail')
def step_impl(context):
    context.cadastro.apertarTABNoConfEmail()


@then(u'valido a mensagem " {msg} " no campo Confirme o seu E-mail')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroConfEmail(msg)


@when(u'aperto a tecla tab no campo CEP')
def step_impl(context):
    context.cadastro.apertarTABNoCep()


@then(u'valido a mensagem " {msg} " no campo CEP')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroCEP(msg)


@when(u'aperto a tecla tab no campo Numero')
def step_impl(context):
    context.cadastro.apertarTABNoNumeroEndereco()


@then(u'valido a mensagem " {msg} " no campo Numero')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroNumeroEndereco(msg)


@when(u'aperto a tecla tab no campo endereco')
def step_impl(context):
    context.cadastro.apertarTABNoEndereco()


@then(u'valido a mensagem " {msg} " no campo endereco')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroEndereco(msg)


@when(u'aperto a tecla tab no campo bairro')
def step_impl(context):
    context.cadastro.apertarTABNoBairro()


@then(u'valido a mensagem " {msg} " no campo bairro')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroBairro(msg)


@when(u'aperto a tecla tab no campo cidade')
def step_impl(context):
    context.cadastro.apertarTABNoCidade()


@then(u'valido a mensagem " {msg} " no campo cidade')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroCidade(msg)


@when(u'aperto a tecla tab no campo estado')
def step_impl(context):
    context.cadastro.apertarTABNoEstado()


@then(u'valido a mensagem " {msg} " no campo estado')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroEstado(msg)


# ----------------------------------------------telefone invalido - campo obrigatorio-----------------------------------
@when(u'preencho o telefone valido com dados {dado}')
def step_impl(context, dado):
    context.cadastro.inserirDDDPrincipal(dado)


@when(u'preencho o ddd com dados invalido {dado}')
def step_impl(context, dado):
    context.cadastro.inserirDDDPrincipal(dado)


@when(u'preencho o telefone com dados invalido {dado}')
def step_impl(context, dado):
    context.cadastro.inserirDDDPrincipal(dado)


@when(u'preencho o ddd alternativo com dados invalido {dado}')
def step_impl(context, dado):
    context.cadastro.inserirDDDAlternativo(dado)


@when(u'preencho o telefone alternativo com dados invalido {dado}')
def step_impl(context, dado):
    context.cadastro.inserirDDDAlternativo(dado)


@then(u'valido campo principal valido a mensagem de erro {msg}')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroTelefonePrincipal(msg)


# ----------------------------------------------email invalido-----------------------------------

@then(u'valido a mensagem de erro {msg} email1')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroEmailInvalido(msg)


@then(u'valido a mensagem de erro {msg} confirmar email')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroConfEmailInvalido(msg)


# ----------------------------------------------email diferente-----------------------------------
@then(u'valido a mensagem de erro {msg} email2')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroConfEmailDiferente(msg)


# ----------------------------------------------cep invalido (com letras)-----------------------------------
@when(u'preencho o campo cep invalido {dado}')
def step_impl(context, dado):
    context.cadastro.inserirCEP(dado)
    time.sleep(0.5)


@then(u'valido a mensagem de erro {msg}')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroCEP(msg)


# ----------------------------------------------cep invalido -----------------------------------


@then(u'valido o campo cep com a mensagem de erro {msg}')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroCEPComDadosInvalidos(msg)


##------------------------------------cadastro passo 3 --------------------------------------------

##----------------------------------------botao desabilitado----------------------------------------------------------
@then(u'verifico que o botao proximo passo 3 esta desabilitado')
def step_impl(context):
    context.cadastro.verificarBotaoProximoPassoFinalizar()


##----------------------------------------dados em branco--------------------------------------------------------------

@when(u'clico a tecla tab no campo senha')
def step_impl(context):
    context.cadastro.apertarTABNaSenha()


@when(u'no campo confirme a sua senha')
def step_impl(context):
    context.cadastro.apertarTABNoConfSenha()


@then(u'valido a mensagem {msg} de erro no campo senha')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroSenha(msg)


@then(u'valido a mensagem {msg} no campo confirme a sua senha')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroConfSenha(msg)


##----------------------------------------dados invalido - senha--------------------------------------------------------

@when(u'preencho o campo senha com dados {dado}')
def step_impl(context, dado):
    context.cadastro.inserirSenha(dado)


@when(u'preencho o campo confirme a sua senha com dados {dado}')
def step_impl(context, dado):
    context.cadastro.inserirConfSenha(dado)


@then(u'valido a mensagem no campo senha {msg}')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroSenha(msg)


@then(u'valido a mensagem no campo confirme a sua senha {msg}')
def step_impl(context, msg):
    context.cadastro.verificarMensagemDeErroConfSenha(msg)


##----------------------------------uso de dados -------------------------------------------------------------------
@when(u'clico no link uso de dados')
def step_impl(context):
    context.cadastro.clicarLinkUsoDeDados()


@then(u'valido o texto do modal autorizacao de uso de dados {msg}')
def step_impl(context, msg):
    context.cadastro.verificarMensagemUsoDeDados(msg)


##-----------------------------------links dos documentos ------------------------------------------------------------

@when(u'clico no link Termos de uso no cadastro passo 3')
def step_impl(context):
    context.cadastro.clicarLinkTermosDeUso()


@when(u'clico no link Politica de Privacidade no cadastro passo 3')
def step_impl(context):
    context.cadastro.clicarLinkPoliticaDePrivacidade()


@then(u'valido o direcionamento para a pagina termos de uso')
def step_impl(context):
    context.cadastro.verificarSeEstaNaPaginaTermosDeUso()


@then(u'valido o direcionamento para a pagina politica de privacidade')
def step_impl(context):
    context.cadastro.verificarSeEstaNaPaginaPoliticaDePrivacidade()
