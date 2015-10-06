from importd import d


@d('/')
def index(request):
    return d.HttpResponse('HELLO, WORLD!')
