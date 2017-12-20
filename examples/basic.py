from okex.client import OkexClient

client = OkexClient(None, None)

symbol = 'ltc_btc'

print client.ticker(symbol)
print client.trades(symbol)
print client.depth(symbol)
