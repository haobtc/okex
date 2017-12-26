import requests

OKEX_CONF = ('', '')

from okex.client import OkexClient, OkexTradeClient

class TestOkexTradeClient():
    def setUp(self):
        self.tc = OkexTradeClient(*OKEX_CONF)
        self.tcGet = OkexClient(*OKEX_CONF)

    def test_instantiate_tradeclient(self):
        self.assertIsInstance(self.tc, OkexTradeClient)

    def test_get_active_orders_returns_json(self):
        ao = self.tc.active_orders()
        self.assertIsInstance(ao, list)

    def test_get_active_positions_returns_json(self):
        ap = self.tc.active_positions()
        self.assertIsInstance(ap, list)

    def test_get_full_history(self):
        ap = self.tc.active_positions()
        self.assertIsInstance(ap, list)

    def test_balances(self):
        print self.tc.balances()

    def test_history(self):
        print 'call test_history'
        print self.tc.history('bch_btc', 0)

    def test_ticker(self):
        print 'call test_ticker'
        print self.tcGet.ticker('bch_btc')

    def test_sell(self):
        print 'call place_order'
        print self.tc.place_order('0.2', '0.1', 'buy', symbol='bch_btc')

aa = TestOkexTradeClient()
aa.setUp()
aa.test_history()
aa.test_balances()
aa.test_ticker()
aa.test_sell()

