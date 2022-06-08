#!/usr/bin/env python

from typing import NamedTuple

from hummingbot.strategy.market_trading_pair_tuple import MarketTradingPairTuple


class CrossArbitrageMarkets(NamedTuple):
    """Specifies markets for cross arbitrage."""

    _1: MarketTradingPairTuple
    _2: MarketTradingPairTuple
    _3: MarketTradingPairTuple
    _4: MarketTradingPairTuple
    _5: MarketTradingPairTuple

    def markets(self):
        return [
            getattr(self, f"_{i}") for i in range(1,6)
        ]
