from okex.client import OkexClient, OkexTradeClient

proxies = {
    'http': 'socks5h://127.0.0.1:1080',
    'https': 'socks5h://127.0.0.1:1080'
}

client = OkexClient(None, None, proxies)

symbol = 'ltc_btc'

print client.ticker(symbol)
print client.trades(symbol)
print client.depth(symbol)

authClient = OkexTradeClient('', '', proxies=proxies)
print authClient.balances()

print authClient.history('bcc_btc', 1, 500)