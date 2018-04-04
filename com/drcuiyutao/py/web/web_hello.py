def application(environment, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s</h1>' % (environment['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
