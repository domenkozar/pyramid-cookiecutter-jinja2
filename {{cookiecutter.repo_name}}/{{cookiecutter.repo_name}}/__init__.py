from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings.setdefault('jinja2.i18n.domain', '{{ cookiecutter.project_name }}')

    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_translation_dirs('locale/')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
