from utils.setup import Setup as setup


def before_all(context):
    setup.escolherBrowser(context)
    setup.desejaTirarPrint(context)
    setup.desejaConfirgurarOUsuario(context)


def before_scenario(context, scenario):
    setup.abrirBrowser(context)


def after_scenario(context, scenario):
    try:
        setup.gerarPrint(context, scenario, scenario.status)
    except:
        context.browser.quit()
    context.browser.quit()
