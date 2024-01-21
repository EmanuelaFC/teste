@testeCadastro2
Funcionalidade: Pagina cadastro - dados de contado passo 2
	#não precisa preencher totalmente para exibir as mensagens de erros

	Contexto: abrir pagina cadastro do site da tele sena
    		Dado que estou na pagina cadastro passo2

    Cenario: botao desabilitado cadastro passo2
    	#verificar o botao desabilitado com dados em branco
			Entao verifico que o botao proximo passo esta desabilitado


    Esquema do Cenario: dados em branco <campo>
        Quando aperto a tecla tab no campo <campo>
        Entao valido a mensagem " <mensagem> " no campo <campo>

        Exemplos:
        |campo|mensagem|
        |telefone|Telefone é obrigatório|
        |email|Preenchimento obrigatório|
        |Confirme o seu E-mail|Preenchimento obrigatório|
        |CEP|Por favor digite o seu CEP|
        |Numero|Digite o número de sua residência|
        |endereco|Por favor preencha o seu endereço|
        |bairro|Digite o seu bairro|
        |cidade|Por favor digite sua cidade|
        |estado|Por favor selecione um estado|



    Esquema do Cenario: telefone invalido - cadastro passo2
        Quando preencho o <campo> com dados invalido <dado1>
        Entao valido campo <tipo> valido a mensagem de erro <msg>

        Exemplos:
        |campo|tipo| dado1|msg|
        |ddd|principal|0040028922|Telefone inválido|
        |telefone|principal| 11111111|Telefone inválido|
#        |ddd alternativo |alternativo|0040028922|Telefone inválido|
#        |telefone alternativo |alternativo| 11111111|Telefone inválido|

    Esquema do Cenario: email invalido - cadastro passo2
        Quando preencho o campo email com <dado1>
        E preencho o campo confirme o seu email com <dado2>
        Entao valido a mensagem de erro <mensagem1> email1
        E valido a mensagem de erro <mensagem2> confirmar email

        Exemplos:
        |dado1| dado2| mensagem1| mensagem2|
        |email|email|Email inválido|Email inválido|


    Esquema do Cenario: email diferente - cadastro passo2
        Quando preencho o campo email com <dado1>
        E preencho o campo confirme o seu email com <dado2>
        Entao valido a mensagem de erro <mensagem2> email2

        Exemplos:
        |dado1| dado2| mensagem2|
        |email@test.com|emailDiferente@test.com|Os e-mails não são iguais|



     Cenario: cep invalido (com letras) - cadastro passo2
        Quando preencho o campo cep invalido asdinjin
        Entao valido a mensagem de erro Por favor digite o seu CEP

#   na atualização 2.8.1 é possivel inserir o endereço manualmente
#    Cenario: cep invalido - cadastro passo2
#        Quando preencho o campo cep invalido 12345123
#        Entao valido o campo cep com a mensagem de erro CEP não encontrado
