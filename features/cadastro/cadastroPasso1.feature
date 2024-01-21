
Funcionalidade: Pagina cadastro - dados pessoais passo 1
	#não precisa preencher totalmente para exibir as mensagens de erros no span

	Contexto: abrir pagina cadastro do site da tele sena
    		Dado que estou na pagina cadastro passo1


  	Cenario: botao desabilitado cadastro passo 1
    	#verificar o botao desabilitado com dados em branco
			Entao verifico que o botao proximo passo esta desabilitado


	Esquema do Cenario: cpf invalido pagina cadastro
		Quando inserir dados no campo cpf com <cpf>
		Entao valido o campo cpf com a mensagem de erro CPF Inválido

		Exemplos:
			|cpf|
			|11111111111|
			|22222222222|
			|asdasdkjfidni|

	Esquema do Cenario: nome incompleto pagina cadastro
		Quando preencho o campo nome com dados <invalido>
		Entao valido a mensagem de erro "Por favor digite seu nome completo"

		Exemplos:
			|invalido|
			|test|
			|nome|



	Esquema do Cenario: data nascimento invalido pagina cadastro
		Quando preencho o campo data de nascimento com <dado> <invalido>
		Entao valido a mensagem de erro no campo data <mensagem>

	Exemplos:
			|dado|invalido|mensagem|
			|dia|00122000|Data inválida|
			|dia|32122000|Data inválida|
			|mes|10002000|Data inválida|
			|mes|15132000|Data inválida|
			|ano|10052007|Não é permitido o cadastro de menores de 16 anos|
			|ano|15042026|Não é permitido o cadastro de menores de 16 anos|
#			|ano|15041800|Data invalida|
			|letras|shualsnu|Data inválida|


	Cenario: ja e cadastrado pagina cadastro
		Quando clico no link faca login
		Entao verifico o direcionamento para pagina de login


	Esquema do Cenario: dados em branco - cadastro passo 1
		Quando foco no campo <campo>
		Entao verifico a mensagem " <msg>  " no campo <campo>

	Exemplos:
			|campo|msg|
			|cpf|CPF Inválido|
			|nome|Por favor digite seu nome completo|
			|data|Data inválida|


	Cenario: cpf valido e ja cadastrado
		Quando preencho o campo cpf com dados validos e cadastrado
		Entao valido a mensagem CPF já cadastrado no campo cpf