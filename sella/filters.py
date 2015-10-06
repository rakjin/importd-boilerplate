import json

import jinja2


@jinja2.contextfilter
def tojson(ctx, val):
    return json.dumps(val)
