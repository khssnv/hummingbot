from decimal import Decimal
from functools import partial
from typing import Optional

from hummingbot.client.config.config_var import ConfigVar
from hummingbot.client.config.config_validators import (
    validate_exchange,
    validate_market_trading_pair,
    validate_decimal,
)
from hummingbot.client.settings import AllConnectorSettings, required_exchanges



def validate_trading_pair(market_idx: int, value: str) -> Optional[str]:
    market = cross_arbitrage_config_map.get(f"market_{market_idx}").value
    return validate_market_trading_pair(market, value)


def trading_pair_prompt(market_idx: int):
    market = cross_arbitrage_config_map.get(f"market_{market_idx}").value
    example = AllConnectorSettings.get_example_pairs().get(market)
    return "Enter the token trading pair you would like to trade on %s%s >>> " \
           % (market, f" (e.g. {example})" if example else "")


cross_arbitrage_config_map = {
    "strategy": ConfigVar(
        key="strategy",
        prompt="",
        default="cross_arbitrage"
    ),
    "market_1": ConfigVar(
        key="market_1",
        prompt="Enter your 1-st spot connector >>> ",
        prompt_on_new=True,
        validator=validate_exchange,
        on_validated=required_exchanges.append,
    ),
    "market_2": ConfigVar(
        key="market_2",
        prompt="Enter your 2-nd spot connector >>> ",
        prompt_on_new=True,
        validator=validate_exchange,
        on_validated=required_exchanges.append,
    ),
    "market_3": ConfigVar(
        key="market_3",
        prompt="Enter your 3-nd spot connector >>> ",
        prompt_on_new=False,
        required_if=lambda: False,
        validator=validate_exchange,
        on_validated=required_exchanges.append,
    ),
    "market_4": ConfigVar(
        key="market_4",
        prompt="Enter your 4-th spot connector >>> ",
        prompt_on_new=False,
        required_if=lambda: False,
        validator=validate_exchange,
        on_validated=required_exchanges.append,
    ),
    "market_5": ConfigVar(
        key="market_5",
        prompt="Enter your 5-th spot connector >>> ",
        prompt_on_new=False,
        required_if=lambda: False,
        validator=validate_exchange,
        on_validated=required_exchanges.append,
    ),
    "market_1_trading_pair": ConfigVar(
        key="market_1_trading_pair",
        prompt=trading_pair_prompt,
        prompt_on_new=True,
        validator=partial(validate_trading_pair, 1),
    ),
    "market_2_trading_pair": ConfigVar(
        key="market_2_trading_pair",
        prompt=trading_pair_prompt,
        prompt_on_new=True,
        validator=partial(validate_trading_pair, 2),
    ),
    "market_3_trading_pair": ConfigVar(
        key="market_3_trading_pair",
        prompt=trading_pair_prompt,
        prompt_on_new=True,
        required_if=lambda: False,
        validator=partial(validate_trading_pair, 3),
    ),
    "market_4_trading_pair": ConfigVar(
        key="market_4_trading_pair",
        prompt=trading_pair_prompt,
        prompt_on_new=True,
        required_if=lambda: False,
        validator=partial(validate_trading_pair, 4),
    ),
    "market_5_trading_pair": ConfigVar(
        key="market_5_trading_pair",
        prompt=trading_pair_prompt,
        prompt_on_new=True,
        required_if=lambda: False,
        validator=partial(validate_trading_pair, 5),
    ),
    "min_profitability": ConfigVar(
        key="min_profitability",
        prompt="What is the minimum profitability for you to make a trade? (Enter 1 to indicate 1%) >>> ",
        prompt_on_new=True,
        default=Decimal("0.3"),
        validator=lambda v: validate_decimal(v, Decimal(-100), Decimal("100"), inclusive=True),
        type_str="decimal",
    ),
}
