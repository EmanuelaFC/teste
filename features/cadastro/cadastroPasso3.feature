
Funcionalidade: Pagina cadastro - senha e aceites passo 3
	#não precisa preencher totalmente para exibir as mensagens de erros

	Contexto: abrir pagina cadastro do site da tele sena
    		Dado que estou na pagina cadastro passo3


	Cenario: botao desabilitado - cadastro passo3
    	#verificar o botao desabilitado com dados em branco
			Entao verifico que o botao proximo passo 3 esta desabilitado


	Cenario: campo em branco senha - cadastro passo3
		Quando clico a tecla tab no campo senha
		E no campo confirme a sua senha
		Entao valido a mensagem Preenchimento obrigatório de erro no campo senha
		E valido a mensagem Preenchimento obrigatório no campo confirme a sua senha


	Esquema do Cenario: dados invalido - senha - cadastro passo3
		Quando preencho o campo senha com dados <invalido>
		E preencho o campo confirme a sua senha com dados <invalido>
		Entao valido a mensagem no campo senha <mensagem>
		E valido a mensagem no campo confirme a sua senha <mensagem>

		Exemplos:
		|invalido|mensagem|
		|@@@@@@|Apenas caracteres alfanuméricos|
		|12345|Mínimo de 6 caracteres|
		|123456789123456789123|Máximo de 20 caracteres|


	Cenario: dados diferentes - cadastro passo3
		Quando preencho o campo senha com dados 123456
		E preencho o campo confirme a sua senha com dados 654321
		Entao valido a mensagem no campo confirme a sua senha As senhas não estão iguais


	Cenario: uso de dados - cadastro passo3
		Quando clico no link uso de dados
		Entao valido o texto do modal autorizacao de uso de dados “Autorizo, de forma gratuita, a empresa Liderança Capitalização S/A. a promover, divulgar, transmitir e utilizar os meus dados e informações pessoais, tais como: Nome, Sobrenome, Cidade, Estado e Premiação, em todos os meios de comunicação, inclusive TV, rádio, nas mídias sociais Facebook, Twitter e Instagram, em caso de contemplação, pelo prazo de 5 (cinco) anos”.


	Esquema do Cenario: links dos documentos
		Quando clico no link <link> no cadastro passo 3
		Entao valido o direcionamento para a pagina <pagina>

		Exemplos:
		|link|pagina|
		|Termos de uso | termos de uso|
		|Politica de Privacidade| politica de privacidade|




