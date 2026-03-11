# Source: https://docs.architect.co/algos-book/bracket.md

# Bracket

A bracket order consists of an entry limit order, a take-profit order, and a stop-loss order.\
The take-profit and stop-loss orders are managed via a One-Cancels-Other (OCO) algo as a subalgo.<br>

&#x20;All orders are placed simultaneously when the algo starts.

### Order Structure

* **Entry Order**: A limit order that initiates the position
* **Take-Profit Order**: A limit order placed at `take_profit_price` to exit at a profit
* **Stop-Loss Order**: A stop-limit order with `stop_loss_trigger_price` and `stop_loss_limit_price` to exit at a loss

### Execution Behavior

1. The entry order is placed immediately when the algo starts
2. When the entry order receives fills, the exit orders (take-profit and stop-loss) are placed as an OCO pair
3. If `trigger_in_proportion` is true, exit orders are sized proportionally to the filled quantity of the entry order
4. If `trigger_in_proportion` is false, exit orders are only placed after the entry order is fully filled
5. When either exit order is filled, the other is immediately cancelled via the OCO subalgo

### Price Validation

**For BUY entries:**

* `take_profit_price` must be greater than entry `limit_price`
* `stop_loss_trigger_price` must be less than entry `limit_price`
* `stop_loss_limit_price` must be less than or equal to `stop_loss_trigger_price`

**For SELL entries:**

* `take_profit_price` must be less than entry `limit_price`
* `stop_loss_trigger_price` must be greater than entry `limit_price`
* `stop_loss_limit_price` must be greater than or equal to `stop_loss_trigger_price`

### &#x20;Completion

The bracket algo completes when:

* The entry order is outed/cancelled before any fills, OR
* All exit orders are fully filled or cancelled after entry fills

{% hint style="warning" %}
You **cannot modify the algo** once it is sent, you must cancel and send a new one if you want different parameters.

You also **cannot pause the algo**, it will just cancel when you send a pause.

It is technically **possible for both secondary orders to be filled** if they execute simultaneously
{% endhint %}

### Use Cases

* Automating profit-taking and risk management for a position
* Ensuring disciplined exits without manual intervention
* Managing trades with predefined risk/reward ratios

### BracketParams

| Parameter                                                                                        | Description                                                  |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| entry *(*[*OrderInfo*](https://docs.architect.co/algos-book/one-triggers-other-oto#orderinfo)*)* | The entry order information                                  |
| take\_profit\_price *(Decimal)*                                                                  | Limit price for the take-profit exit order                   |
| stop\_loss\_trigger\_price (*Decimal*)                                                           | Trigger price for the stop-loss order                        |
| stop\_loss\_limit\_price (*Decimal*)                                                             | Limit price for the stop-loss order (after triggered)        |
| trigger\_in\_proportion (bool)                                                                   | If true, exit orders are sized proportionally to entry fills |

### Example

```python
from architect_py import (
    BracketParams,
    OrderInfo,
    OrderDir,
    TimeInForce,
    OrderType,
)

symbol = 'NQ 20251219 CME Future'
tp = f"{symbol}/USD"
account = "PAPER:example@email.com"
venue = "CME"

params = BracketParams.new(
    entry=OrderInfo.new(
        symbol=tp,
        execution_venue=venue,
        dir=OrderDir.BUY,
        quantity=10,
        limit_price=24940,
        post_only=False,
        time_in_force=TimeInForce.GTC,
        order_type=OrderType.LIMIT,
    ),
    take_profit_price=25100,
    stop_loss_trigger_price=24800,
    stop_loss_limit_price=24790,
    trigger_in_proportion=True,
)


order = await client.place_algo_order(params=params, account=account)
```
