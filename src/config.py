"""
Settings file to configure the application
"""

class Config(object):
    """
    Common configurations
    """
    # Put any configurations here that are common across all environments
    def config_swag(self):
        SWAGGER_CONFIG = {
            'title': 'API Rest com Flask e Swagger',
            'description': """
                Este é um exemplo de API Rest com Flask e Swagger.
                Caso precise de ajuda para utilizar a API, acesse a documentação.
            """,
            'uiversion': 3
        }
        
        return SWAGGER_CONFIG