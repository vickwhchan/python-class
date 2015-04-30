from __future__ import division


class PriceRange(object):
    def __init__(self, symbol, low, high):
        self.symbol = symbol
        self.low = low
        self.high = high

    @property  # -- midpoint = property(midpoint)
    def midpoint(self):
        return (self.low + self.high) / 2

    midpoint = property(midpoint)

    @property
    def low(self):
        return self.get_low

    def get_low(self, low):
        self._low = low

    low = property(get_low, set_low)


p = PriceRange('CSCO', 20, 29)
