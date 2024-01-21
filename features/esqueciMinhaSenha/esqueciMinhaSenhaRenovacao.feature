
Funcionalidade: pagina de renovacao de senha - esqueco minha senha


  Contexto: direcionamento para pagina de ativação do esqueci minha senha
    Dado que estou na pagina esqueci minha senha
    Quando preencho o campo com dados validos
    E clico no botao enviar codigo
    E clico no botao ok do modal
    Entao valido o direcionamento para ativacao do esqueci a minha senha
    Quando obtenho o codigo de ativacao
    E preencho com o codigo de ativacao valido
    E clico no botao confirmar codigo
    Entao valido que estou na pagina alterar senha

  Cenario: cancelar renovacao de senha - pagina de renovacao de senha
    Quando clico no botao cancelar renovacao
    Entao valido o direcionamento de renovacao de senha para a pagina de login

  Cenario: dados em branco - pagina de renovacao de senha
    Quando aperto a tecla tab no campo senha renovacao
    E aperto a tecla tab no campo confirmar senha renovacao
    Entao valido a mensagem de Preenchimento obrigatório no campo senha
    E valido a mensagem de Preenchimento obrigatório no campo confirmar senha

  Esquema do Cenario: dados invalidos campo senha - pagina de renovacao de senha
    Quando preencho o campo senha com <dados>
    E aperto a tecla tab no campo senha renovacao
    E clico no icone olho para exibir senha
    Entao valido o a mensagem de erro <msg>
    E valido o botao confirmar alteracao esta desabilitado

    Exemplos:
    |dados|msg|
    |12345|Mínimo de 6 caracteres|
    |asdfr|Mínimo de 6 caracteres|
    |Qa2|Mínimo de 6 caracteres|
    |12d|Mínimo de 6 caracteres|
    |132456789456123130325|Máximo de 20 caracteres|
    |hasaksnkasnnknaknkjaa|Máximo de 20 caracteres|
    |132456789456123130325132456789456123130325|Máximo de 20 caracteres|
    |hasaksnkasnnknaknkjahasaksnkasnnknaknkja|Máximo de 20 caracteres|
    |@@@@@@|Apenas caracteres alfanuméricos|
    |!!!!!!|Apenas caracteres alfanuméricos|
    |++++++|Apenas caracteres alfanuméricos|
    |++++++ijasdl|Apenas caracteres alfanuméricos|
    |askdmçl++++++ijasdl|Apenas caracteres alfanuméricos|
    |askdmçl++++++13215|Apenas caracteres alfanuméricos|
    |181651++++++13215|Apenas caracteres alfanuméricos|
    |181651++++++uasdnl|Apenas caracteres alfanuméricos|
    |181651++++++13215|Apenas caracteres alfanuméricos|
    |110081651++++++|Apenas caracteres alfanuméricos|


  Esquema do Cenario: dados invalidos campo confirmar senha - pagina de renovacao de senha
    Quando preencho o campo confirmar senha com <dados>
    E aperto a tecla tab no campo confirmar senha renovacao
    E clico no icone olho para exibir confirmar senha
    Entao valido o campo confirmar senha com a mensagem de erro <msg>
    E valido o botao confirmar alteracao esta desabilitado

    Exemplos:
    |dados|msg|
    |12345|Mínimo de 6 caracteres|
    |asdfr|Mínimo de 6 caracteres|
    |Qa2|Mínimo de 6 caracteres|
    |12d|Mínimo de 6 caracteres|
    |132456789456123130325|Máximo de 20 caracteres|
    |hasaksnkasnnknaknkjaa|Máximo de 20 caracteres|
    |132456789456123130325132456789456123130325|Máximo de 20 caracteres|
    |hasaksnkasnnknaknkjahasaksnkasnnknaknkja|Máximo de 20 caracteres|
    |@@@@@@|Apenas caracteres alfanuméricos|
    |!!!!!!|Apenas caracteres alfanuméricos|
    |++++++|Apenas caracteres alfanuméricos|
    |++++++ijasdl|Apenas caracteres alfanuméricos|
    |askdmçl++++++ijasdl|Apenas caracteres alfanuméricos|
    |askdmçl++++++13215|Apenas caracteres alfanuméricos|
    |181651++++++13215|Apenas caracteres alfanuméricos|
    |181651++++++uasdnl|Apenas caracteres alfanuméricos|
    |181651++++++13215|Apenas caracteres alfanuméricos|
    |110081651++++++|Apenas caracteres alfanuméricos|

  Cenario: alteracao com senhas diferentes - pagina de renovacao de senha
    Quando preencho o campo senha com 300300
    E preencho o campo confirmar senha com 200200
    E clico no icone olho para exibir confirmar senha
    Entao valido o campo confirmar senha com a mensagem de erro As senhas não estão iguais
    E valido o botao confirmar alteracao esta desabilitado

  Cenario: informar senha igual a anterior - pagina de renovacao de senha
    Quando preencho o campo com a senha anterior
    E preencho o campo confirmar com a senha anterior
    E clico no botao confirmar alteracao
    Entao valido o modal com a mensagem A nova senha não pode ser igual a última senha utilizada.