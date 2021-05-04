from sanic import Sanic
from .middlewares import setup_middlewares
from .routes import setup_routes
from src.core.settings import Settings

app = Sanic(__name__)


def api_run():
    print('api running')

    config = Settings()
    app.update_config(config)
    # setup_database(app)
    setup_routes(app)
    setup_middlewares(app)
    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        auto_reload=app.config.DEBUG,
    )


# if __name__ == '__main__':
#     api_run()
