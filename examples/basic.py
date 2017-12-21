from okex.client import OkexClient, OkexTradeClient

client = OkexClient(None, None)

symbol = 'ltc_btc'

print client.ticker(symbol)
print client.trades(symbol)
print client.depth(symbol)

authClient = OkexTradeClient('ee8241b2-5af2-4eee-a057-3a5189d7f39b', '4811AA5AA4F60E7463AD52CBBF921C36')
print authClient.balances()