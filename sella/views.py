from importd import d


@d('/', name='sella.index')
def index(request):
    return d.render_to_response('index.jinja2')
