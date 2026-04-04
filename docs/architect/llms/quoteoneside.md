# Source: https://docs.architect.co/algos-book/quoteoneside.md

# QuoteOneSide

The algo is similar to a limit order on the surface, but provides additional execution functionality in a couple of critical ways:&#x20;

* This algo will always put out a limit order with a price that is equal to or less aggressive than the set `limit price`&#x20;
* However, it will attempt to only post liquidity, so it will not cross the market unless the market moves toward the order while the order is in flight. In the `JOIN` mode, it joins the best bid (when buying) or offer (when selling)
* It can be parameterized with the `IMPROVE` mode to improve the market by one tick to gain queue priority, as long as the price is less aggressive than the `limit price`

The algorithm continuously monitors the market and repositions the quote as needed to maintain\
competitiveness while respecting the specified constraints. It will have at most one order at a time out in the market.&#x20;

### Use Cases

* While executing passively, to get filled at favorable prices without crossing the market
* While spread trading, to quote the passive side of a spread while maintaining price competitiveness
* While market making, to provide liquidity to one side of the market

### QuoteOneSideParams

| Parameter                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| dir *(OrderDir)*                    | Designate your order as buy or sell with the binary enums `OrderDir.BUY` or `OrderDir.SELL`                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| quantity *(decimal)*                | The quantity to execute. The algorithm terminates when filled to the nearest lot less than or equal to quantity                                                                                                                                                                                                                                                                                                                                                                                                                       |
| limit\_price *(decimal)*            | The most aggressive price the algo will quote at                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| max\_ticks\_outside  *(decimal)*    | <p>Maximum number of ticks less aggressive than the BBO to quote </p><ul><li> <code>None</code>: No constraint on distance from BBO — will quote at any valid price up to the limit price</li><li> <code>n</code>: Will only quote if within n ticks of the best same-side price (BBO) </li></ul><p>Orders beyond this distance are cancelled as they're unlikely to fill</p><ul><li>Example: With <code>5</code> for a buy order, if best bid is 100, will only quote between 95-100</li></ul><p>This must be a positive integer</p> |
| improve\_or\_join *(ImproveOrJoin)* | Designate whether to improve the market or join at the current best price with the binary enums `ImproveOrJoin.Join` or `ImproveOrJoin.Improve`                                                                                                                                                                                                                                                                                                                                                                                       |
| quantity\_filled *(decimal)*        | This is used to synchronize and track fill quantities when modifying the QuoteOneSide algo. Set it to 0 if initiating a new algo order                                                                                                                                                                                                                                                                                                                                                                                                |
| symbol *(str)*                      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| marketdata\_venue *(str)*           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| exchange\_venue *(str)*             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| account *(str, optional)*           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### QuoteOneSideStatus

| Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| front\_of\_queue      | <p>Indicates whether the current quote is at the front of the queue (best price on our side). Being front of queue provides priority for fills.</p><ul><li>For Buy orders: <code>true</code> when our quote price > previous best bid on the market </li><li>For Sell orders: <code>true</code> when our quote price < previous best ask on the market </li><li>Also <code>true</code> when we're the first to establish a quote on our side (no existing bid/ask) </li></ul><p>This status updates dynamically as market conditions change and other orders arrive/cancel </p> |
| is\_cancelling        | Indicates whether the algorithm is currently cancelling an order                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| orders\_sent          | Number of orders sent by the algo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| quantity\_filled      | Quantity filled by the algo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| current\_quote\_price | The active quote price                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| realized\_avg\_price  | The average filled price of the algo                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### Example

{% tabs %}
{% tab title="Python" %}

```python
from architect_py import QuoteOneSideParams, ImproveOrJoin, OrderDir

symbol = "NQ 20251219 CME Future"
tp = f"{symbol}/USD"
venue = "CME"
account="PAPER:example@email.com"
params = QuoteOneSideParams.new(
    dir=OrderDir.BUY,
    execution_venue=venue,
    marketdata_venue=venue,
    quantity_filled=0,
    improve_or_join=ImproveOrJoin.Join,
    limit_price = 26000,
    quantity=1,
    symbol=tp,
)
order = await client.place_algo_order(params=params, account=account)
```

{% endtab %}
{% endtabs %}

### API Reference

{% embed url="<https://docs.rs/architect-api/latest/architect_api/algo/quote_one_side/struct.QuoteOneSideParams.html>" %}
