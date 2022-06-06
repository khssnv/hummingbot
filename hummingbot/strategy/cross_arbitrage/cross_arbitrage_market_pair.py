#!/usr/bin/env python

from typing import NamedTuple

from hummingbot.strategy.market_trading_pair_tuple import MarketTradingPairTuple


class CrossArbitrageMarketPair(NamedTuple):
    """
    Specifies a pair of markets for cross_arbitrage
    """
    first: MarketTradingPairTuple
    second: MarketTradingPairTuple
