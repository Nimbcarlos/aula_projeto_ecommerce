from loja.models import SiteSetup, Cores


def site_setup(request):
    setup = SiteSetup.objects.order_by('-id').first()

    return {
        'site_setup': setup,
    }

def escolha_cor(request):
    setup = Cores.objects.order_by('-id').first()

    return {
        'escolha_cor': setup,
    }