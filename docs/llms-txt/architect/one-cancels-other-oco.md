# Source: https://docs.architect.co/algos-book/one-cancels-other-oco.md

# One Cancels Other (OCO)

An OCO order consists of multiple orders where the fill of any one order automatically cancels all other orders in the group.

&#x20;All orders are placed simultaneously when the algo starts.

### Cancel Behavior

* When any order is fully filled, the remaining orders are immediately cancelled
* If `cancel_in_proportion` is **true**, partial fills trigger proportional cancellations of the remaining orders based on the fill quantity
  * This will be calculated based on "percent\_done", which is SUM(filled\_for\_a\_given\_order/order\_quantity) for all of the orders
  * For example, if you have three orders for quantities 10, 15, 20 and you have gotten filled on 1, 3, 10 respectively, you will have 1/10 + 3/15 + 10/20 = 80% done, so each order will have 20% left.\
    Thus, the remaining order quantities will be 2, 3, 4
  * Any fractional orders are rounded to the nearest quantity increment
* &#x20;If `cancel_in_proportion` is **false**, only a complete fill of one order triggers cancellation of all other orders

The OCO algo completes when:

* all orders are fully outed/cancelled

{% hint style="warning" %}
You **cannot modify the algo** once it is sent, you must cancel and send a new one if you want different parameters.

You also **cannot pause the algo**, it will just cancel when you send a pause.

If an order is rejected, the algo will continue operating with the remaining orders.

It is technically **possible for all orders to be filled** if they execute simultaneously
{% endhint %}

### Use Cases

* Placing orders on multiple exchanges where you only want one to execute
* Implementing profit target and stop loss orders simultaneously
* Managing risk by ensuring only one side of a position is filled

### OneCancelsOtherParams

| Parameter                       | Description                                                                                                                                                            |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| orders *(vec\<OrderInfo>)*      | The orders in the OCO set                                                                                                                                              |
| cancel\_in\_proportion *(bool)* | If true, orders are replaced proportionally based on the fill quantity of any given order. If false, orders are only cancelled once the an order is completely filled. |

### OrderInfo

OrderInfo is very similar to a [PlaceOrderRequest](https://docs.architect.co/sdk-reference/order-entry#order-request-fields). This contains the order information for each leg of the OCO algo.

<table><thead><tr><th width="166.6875">Field</th><th width="104.08984375">Required</th><th>Description</th></tr></thead><tbody><tr><td>symbol</td><td>Y</td><td>Tradable product</td></tr><tr><td>dir</td><td>Y</td><td>Order side; BUY or SELL</td></tr><tr><td>quantity</td><td>Y</td><td>Order quantity</td></tr><tr><td>order_type</td><td>Y</td><td>Order type</td></tr><tr><td>limit_price</td><td>N*</td><td>Required for certain order types</td></tr><tr><td>post_only</td><td>N*</td><td>Required for certain order types</td></tr><tr><td>trigger_price</td><td>N*</td><td>Required for certain order types</td></tr><tr><td>time_in_force</td><td>Y</td><td>Order time-in-force instruction</td></tr><tr><td>execution_venue</td><td>Y</td><td>Execution venue for the order. Unlike PlaceOrderRequest, this is required</td></tr></tbody></table>

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
params = OneCancelsOtherParams.new(
    orders=[OrderInfo.new(
        symbol=tp1,
        execution_venue=venue, 
        dir=OrderDir.BUY, 
        quantity=10, 
        limit_price=24940,
        post_only=False,
        time_in_force=TimeInForce.IOC,
        order_type=OrderType.LIMIT,
        ),
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
    cancel_in_proportion=True,
)

order = await client.place_algo_order(params=params, account=account)
```
