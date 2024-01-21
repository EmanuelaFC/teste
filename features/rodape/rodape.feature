
Funcionalidade: navegacao no rodape

  Contexto: abrir pagina do site da tele sena
    Dado que estou em uma pagina da tele sena

  Esquema do Cenario: (Links) Menus rodape (<opcao>)
    navegacao entre as pagina pelo link do rodape

    Quando clico no menu do rodape <opcao>
    Entao verifico o direcionamento para pagina <escolhida>

    Exemplos:
    | opcao                         | escolhida |
    | comprar tele senas            | compra    |
    | resultados                    | resultado |
    | promocoes                     | promocoes |
    | resgates                      | resgate   |
    | cadastrar tele sena deslogado | login     |
    | minhas tele senas deslogado   | login     |


  Esquema do Cenario: (Links) Redes Sociais (<opcao> - pagina rodape)
  Quando clico no icone <opcao>
  Entao valido o direcionamento para pagina <escolhida>

  Exemplos:
  | opcao     | escolhida |
  | facebook  | facebook  |
  | instagram | instagram |
  | youtube   | youtube   |
  | twitter   | twitter   |


#
#Retirado na versão 2.3.0
#  Esquema do Cenario: Central de atendimento - telefones
#  Quando seleciona o contato <opcao>
#  Entao valido o numero <escolhido>
#
#  Exemplos:
#  | opcao     | escolhido        |
#  | telefone1 | 0800-7010319   |
##  | telefone2 | (11) 3188-5090 |
##  | ouvidoria | 0800-7715936    |
##  | whatsapp  | (11) 2182-2015 |
##  | tts       | 0800-7051212   |
#
#  Esquema do Cenario: Central de atendimento - conferir texto
#  Quando selecionado o texto da central de atendimento
#  Entao valido o paragrafo <descricao> da central de atendimento <paragrafo>
#
#  Exemplos:
#  | descricao | paragrafo                                        |
#  |         0 | De segunda a sexta-feira das 9:00hs às 17:00hs |
#  |         1 | e aos sábados das 9:00hs às 15:00hs            |
#  |         2 | exceto aos feriados.                          |
#
#  Esquema do Cenario: TTS - conferir texto
#  Quando selecionado o texto
#  Entao valido o texto <descricao> do central de atendimento <paragrafo>
#
# Exemplos:
#  | descricao | paragrafo                             |
#  |         0 | TTS                                    |
#  |         2 | Exclusivo para deficientes auditivos. |
#  |         3 | Utilize um aparelho telefônico        |
#  |         4 | adaptado com dispositivo TDD.         |


  Esquema do Cenario: Institucional <link>
  Quando clico no link <link>
  Entao valido do direcionamento para pagina <pagina>

 Exemplos:
  |link|pagina|
  |A TELE SENA | a tele sena|
  |Assessoria de Imprensa | assessoria de imprensa |


  Cenario: Acesse a central de atendimento
    Quando clico no link Acesse a central de atendimento
    Então valido do direcionamento para pagina atendimento

  Esquema do Cenario: Termos do site (<opcao>)
    Quando clico no link <opcao>
    Entao valido o direcionamento para pagina <escolhida>

    Exemplos:
      | opcao                   | escolhida               |
      | Termos de uso           | Termos de uso           |
      | politica de privacidade | politica de privacidade |
      | politica de cookies     | politica de cookies     |
      | termos legais           | termos legais           |
      | condicoes gerais        | condicoes gerais        |

  Esquema do Cenario: Links GSS <opcao>
    Quando clico no link <opcao>
    Entao valido o direcionamento para pagina <escolhida>

    Exemplos:
      | opcao                   | escolhida               |
      | Grupo ss                | Grupo ss                |
      | Lideranca capitalizacao | Lideranca capitalizacao |
      | jequiti                 | jequiti                 |
      | sbt                     | sbt                     |

# retirado na versão 2.7.0
#  Cenario: link susep rodape
#    Quando clico no link do site susep
#    Entao valido o direcionamento para pagina da susep


  Cenario: numero da susep
    Entao valido no rodape o numero susep

  Esquema do Cenario: Baixe o novo app da Tele Sena e tenha tudo em suas mãos
    Quando clico no icone <imagem>
    Entao valido o direcionamento para pagina da <pagina>

    Exemplos:
    |imagem|pagina|
    |app store|app store|
    |google play|google play|

