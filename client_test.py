import unittest
from client3 import getDataPoint
from client3 import getRatio
class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      stock = quote['stock']
      price = (bid_price + ask_price)/2
      testOutput = stock,bid_price,ask_price,price
      self.assertEqual(getDataPoint(quote),testOutput)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      bid_price = quote['top_bid']['price']
      ask_price = quote['top_ask']['price']
      stock = quote['stock']
      price = (bid_price + ask_price)/2
      testOutput = stock,bid_price,ask_price,price
      self.assertEqual(getDataPoint(quote),testOutput)


  """ ------------ Add more unit tests ------------ """

  def test_getRatio_calculateRatio(self):
    price_a =5.4
    price_b = 7.5

    self.assertEqual(getRatio(price_a,price_b),price_a/price_b)




if __name__ == '__main__':
    unittest.main()
