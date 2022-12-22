"""
First Server main script
"""
from wsgiref.simple_server import make_server
from jinja2 import Environment, FileSystemLoader, Template

env: Environment = Environment(loader=FileSystemLoader('templates'))


def application(environ: dict, start_response) -> list[bytes]:
    """
    WSGI Application interface
    :param environ: environment data
    :type environ: dict
    :param start_response: reference of method for response application
    :type start_response: method
    :return: byte content of template response rendered at UTF-8
    :rtype: list[bytes]
    """
    status: str = '200 OK'
    context: dict = {
        'username': 'Cody',
        'courses': ['Python', 'Django', 'Flask', 'FastAPI']}
    path: str = environ.get('PATH_INFO')
    template: Template = None
    if path == '/':
        template = env.get_template('index.html')
    elif path == '/users':
        template = env.get_template('users.html')
    response: str = template.render(**context)
    start_response(status, [])  # MetaData
    return [bytes(response, 'UTF-8')]  # Client response


PORT: int = 4000

with make_server('localhost', PORT, application) as server:
    print(f">>> The server is listening port: {PORT}")
    server.serve_forever()
