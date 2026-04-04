# Source: https://docs.architect.co/algos-book/one-triggers-other-oto.md

# One Triggers Other (OTO)

### Triggering Behavior

* The `primary` order is placed immediately when the algo starts
* &#x20;The `secondary` orders are only placed after the `primary` order is filled&#x20;
* If `trigger_in_proportion` is true, the other orders are triggered proportionally based on the fill quantity of the primary order. The quantities are rounded down where necessary
  * For example, if `primary` has quantity 10, and `secondary` is a single order of quantity 5, then if `primary` is filled 5 lots and `trigger_in_proportion` is true, `other` will fire for 2 lots: (5/10) \* 5 = 2.5, rounded down
  * If `primary` subsequently receives another fill for 5 lots, `secondary` will fire its remaining 3 lots, and the algo will complete once `secondary` gets that filled
* If `trigger_in_proportion` is false, the other orders are only triggered after the primary order is completely filled

The OTO algo completes when:

* If `primary` is OUT and `secondary`  are [OUT](https://docs.architect.co/concepts/orderflow) /cancelled/rejected
* If `primary` is rejected or at any point cancelled.&#x20;

{% hint style="warning" %}
You cannot modify the algo once it is sent, you must cancel and send a new one if you want different parameters. You also cannot pause the algo, it will just cancel when you send a pause.
{% endhint %}

### Use Cases

* Executing a hedging strategy after an initial position is established
* Implementing conditional order sequences where subsequent orders depend on initial fills

### OneTriggersOtherParams

| Parameter                        | Description                                                                                                                                                                                             |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| primary *(OrderInfo)*            | Designate your `primary` order, which is placed immediately upon algo start. See [OrderInfo](#orderinfo).                                                                                               |
| secondary *(List\[OrderInfo])*   | A list of orders (use a singleton list for just one order) that will simultaneously trigger after the `primary` order is filled (depending on `trigger_in_proportion`).                                 |
| trigger\_in\_proportion *(bool)* | If true, `secondary` orders are triggered proportionally based on the fill quantity of the `primary` order. If false, `secondary` orders are only placed once the `primary` order is completely filled. |

### OrderInfo

OrderInfo is very similar to a [PlaceOrderRequest](https://docs.architect.co/sdk-reference/order-entry#order-request-fields). This contains the order information for each leg of the OTO algo. Note that you cannot nest other algos.

<table><thead><tr><th width="166.6875">Field</th><th width="104.08984375">Required</th><th>Description</th></tr></thead><tbody><tr><td>symbol</td><td>Y</td><td>Tradable product</td></tr><tr><td>dir</td><td>Y</td><td>Order side; BUY or SELL</td></tr><tr><td>quantity</td><td>Y</td><td>Order quantity</td></tr><tr><td>order_type</td><td>Y</td><td>Order type (Limit, Stop-loss, Market)</td></tr><tr><td>limit_price</td><td>N*</td><td>Required for certain order types</td></tr><tr><td>post_only</td><td>N*</td><td>Required for certain order types</td></tr><tr><td>trigger_price</td><td>N*</td><td>Required for certain order types</td></tr><tr><td>time_in_force</td><td>Y</td><td>Order time-in-force instruction</td></tr><tr><td>execution_venue</td><td>Y</td><td>Execution venue for the order. Unlike PlaceOrderRequest, this is required</td></tr></tbody></table>

### Example

```python
from architect_py import (
    OneTriggersOtherParams,
    OrderInfo,
    OrderDir,
    TimeInForce,
    OrderType,
)

symbol1 = 'NQ 20251219 CME Future' 
symbol2 = 'MNQ 20251219 CME Future'
tp1 = f"{symbol1}/USD"
tp2 = f"{symbol2}/USD"
account = "PAPER:example@email.com"
venue = "CME"
params = OneTriggersOtherParams.new(
    primary=OrderInfo.new(
        symbol=tp1,
        execution_venue=venue, 
        dir=OrderDir.BUY, 
        quantity=10, 
        limit_price=24940,
        post_only=False,
        time_in_force=TimeInForce.IOC,
        order_type=OrderType.LIMIT,
    ),
    secondary= [
        OrderInfo.new(
            symbol=tp2,
            execution_venue=venue, 
            dir=OrderDir.SELL, 
            quantity=100, 
            limit_price=25000,
            post_only=False,
            time_in_force=TimeInForce.IOC,
            order_type=OrderType.LIMIT,
        )
    ],
    trigger_in_proportion=True,
)

order = await client.place_algo_order(params=params, account=account)
```
