# Source: https://docs.architect.co/getting-started-with-python.md

# Getting started with Python

{% embed url="<https://github.com/architect-xyz/architect-py>" %}

{% embed url="<https://pypi.org/project/architect-py/>" fullWidth="false" %}

## Installation

```bash
pip install architect-py
```

## Typechecking

`architect-py` is fully typed, so you can use it with an IDE that supports type checking (e.g. VSCode with the Pylance extension). Generally speaking, the package will work if it typechecks.

## Example

In this example, we'll use the **architect-py** SDK to place a limit order on CME's Micro Ethereum (MET) futures front month contract, 10% below the current best bid.

```python
import asyncio
import time
from decimal import Decimal

from architect_py import AsyncClient, OrderStatus, OrderDir


async def main():
    c = await AsyncClient.connect(
        endpoint="app.architect.co",
        api_key="<api key>",
        api_secret="<api secret>",
        paper_trading=False,
    )

    symbol = "ES 20281215 CME Future/USD"
    venue = "CME"

    # Get ticker for a single instrument
    print()
    print(f"Ticker for {symbol}")
    ticker = await c.get_ticker(symbol=symbol, venue=venue)
    print(f"Best bid: {ticker.bid_price}")
    print(f"Best ask: {ticker.ask_price}")

    # List your FCM accounts
    print()
    print("Your FCM accounts:")
    accounts = await c.list_accounts()
    for account in accounts:
        print(f"{account.account.name}")

    account_id = accounts[0].account.id

    # Place a limit order $100 below the best bid
    best_bid = ticker.bid_price
    if best_bid is None:
        raise ValueError("No bid price available")
    limit_price = best_bid - Decimal(100)
    quantity = Decimal(1)
    account = accounts[0]
    order = None
    
    if (
        input(
            f"Place a limit order to BUY 1 LIMIT {limit_price} on account {account.account.name}? [y/N]"
        )
        == "y"
    ):
        order = await c.place_limit_order(
            symbol=symbol,
            execution_venue=venue,
            dir=OrderDir.BUY,
            quantity=quantity,
            limit_price=limit_price,
            account=str(account_id),
        )
    else:
        raise ValueError("Order was not placed")
    print(f"Order placed with ID: {order.id}")

    # Poll order status until rejected or fully executed
    # After 5 seconds, cancel the order
    i = 0
    while OrderStatus.Open == order.status:
        time.sleep(1)
        print(f"...order state: {order.status}")
        order = await c.get_order(order.id)
        assert order is not None
        i += 1
        if i == 5:
            print("Canceling order")
            await c.cancel_order(order.id)

    # Print final order state
    if OrderStatus.Rejected == order.status:
        print(f"Order was rejected: {order.reject_message}")
    elif OrderStatus.Canceled == order.status:
        print("Order was canceled")
    elif OrderStatus.Out == order.status:
        print(f"Order was filled for qty: {order.filled_quantity}")
        print(f"Average execution price: {order.average_fill_price}")


if __name__ == "__main__":
    asyncio.run(main())
```

## Async vs sync

Using the `AsyncClient` is preferred, but the Python SDK also includes a sync version which can be imported as `from architect_py import Client`. Its interface is identical to the async client with the following exceptions:

* Methods starting with `stream_` are not available
* Methods starting with `subscribe_` are not available
* `orderflow` bidirectional channel is unavailable

When following the documentation, simply omit the `await` keyword from the examples when using the sync client.

## Additional examples

Additional examples can be found in the [GitHub repository](https://github.com/architect-xyz/architect-py/tree/main/examples).
