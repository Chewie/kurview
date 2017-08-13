# Kurview: A kraken currency viewer

## What is it?

This dead simple app displays the cryptocurrencies currently present on your [Kraken](https://kraken.com) account, and converts them to fiat currency according to the [Cryptonator](https://www.cryptonator.com/api) average for easy viewing.

## Configuration

The app needs to environment variables to function:

* `KRAKEN_KEY`: The API key used to make queries to the API
* `KRAKEN_SECRET`: The private key used to sign API messages

The API key can be found on the settings tab of you Kraken account.
