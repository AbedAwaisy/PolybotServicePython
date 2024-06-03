import flask
from flask import request
import os
from bot import Bot, QuoteBot, ImageProcessingBot
import logging

app = flask.Flask(__name__)

TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_APP_URL = os.environ['TELEGRAM_APP_URL']

logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET'])
def index():
    return 'Ok'


@app.route(f'/{TELEGRAM_TOKEN}/', methods=['POST'])
def webhook():
    req = request.get_json()
    app.logger.debug(f"Received webhook: {req}")
    try:
        bot.handle_message(req['message'])
    except Exception as e:
        app.logger.error(f"Error handling message: {e}")
        return 'Ok'
    return 'Ok'


if __name__ == "__main__":
    # bot = Bot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)
    # bot = QuoteBot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)
    bot = ImageProcessingBot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)
    app.run(host='0.0.0.0', ssl_context=('/home/ubuntu/prod-bot.pem', '/home/ubuntu/prod-bot.key') , port=8443)


