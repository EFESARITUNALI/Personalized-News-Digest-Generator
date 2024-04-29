import configparser

config = configparser.ConfigParser()
config.read('config.ini')

NEWS_API_KEY = config['API_KEYS']['news_api_key']
COHERE_API_KEY = config['API_KEYS']['cohere_api_key']