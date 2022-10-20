from flasgger import Swagger

from src.routes import *
from src.config import Config

config = Config().config_swag()

if __name__ == '__main__':
    app.config['SWAGGER'] = config
    swagger = Swagger(app)
    app.run(host='0.0.0.0', debug=True)