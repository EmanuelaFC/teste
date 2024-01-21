
Funcionalidade: pagina termo de uso

  Contexto: abrir pagina termo de uso
    Dado que estou na pagina termo de uso


  Cenario: breadcrumbs termo de uso para home
    Quando clico no link breadcrumb home da pagina termo de uso
    Entao valido o direcionamento de termos para pagina home


  Esquema do Cenario: Validar link da pagina termo de uso para <link>
    Quando clico no <link>
    Então valido o direcionamento de termos para pagina <pagina>

  Exemplos:
  |link|pagina|
  |tele sena texto destaque| home|
  |tele sena I| home|
  |promocoes I|promocoes|
  |servico de atendimento ao cliente II|pagina atendimento|
  |tele sena VI|home|
