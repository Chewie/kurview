import os
import json
import krakenex
import flask
import requests

app = flask.Flask(__name__)
CRYPTONATOR_TICKER = 'https://api.cryptonator.com/api/ticker/'
CURRENCY_MAPPING = {'XXBT': 'BTC', 'XETH': 'ETH'}
FIAT = 'EUR'

KRAKEN_KEY = os.environ['KRAKEN_KEY']
KRAKEN_SECRET = os.environ['KRAKEN_SECRET']
kraken = krakenex.API(key=KRAKEN_KEY, secret=KRAKEN_SECRET)

@app.route('/')
def index():
    try:
        kraken_currencies = kraken.query_private('Balance')

        currencies = {}
        for k, v in kraken_currencies['result'].items():
            currencies[CURRENCY_MAPPING[k]] = {'balance': float(v)}

        for currency, dic in currencies.items():
            req = requests.get(CRYPTONATOR_TICKER + currency + '-' + FIAT)
            ticker = req.json()['ticker']
            dic['rate'] = float(ticker['price'])
            dic['change'] = float(ticker['change'])
            dic['total'] = float(dic['balance']) * float(dic['rate'])
        result = {'currencies': currencies}
        result['total'] = sum(c['total'] for c in currencies.values())

        return flask.render_template('index.html', result=result)
    except:
        return flask.render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4251, debug=True)
