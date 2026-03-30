# Source: https://docs.architect.co/sdk-reference/order-entry.md

# Order entry

* [Order entry](#order-entry)
  * [Place limit order](#place-limit-order)
    * [Order request fields](#order-request-fields)
    * [Order types](#order-types)
    * [Time-in-force instructions](#time-in-force-instructions)
  * [Cancel order](#cancel-order)
  * [Cancel all orders](#cancel-all-orders)
  * [Batch cancel orders](#batch-cancel-orders)
  * [Reconcile out orders](#reconcile-out-orders)
  * [Orderflow channel](#orderflow-channel)
  * [Stream orderflow](#stream-orderflow)

## Place limit order

Place a limit order for a tradable product. If an execution venue isn't specified, the default venue for the symbol will be used. Depending on the time-in-force instruction, the order may require additional parameters.

{% tabs %}
{% tab title="Python" %}

```python
from decimal import Decimal
from architect_py import OrderDir

order = await client.place_limit_order(
    symbol="BTC Crypto/USD",
    execution_venue="COINBASE",
    account=None,                   # required for some venues
    dir=OrderDir.BUY,
    quantity=Decimal(1),
    limit_price=Decimal(10000),
    post_only=True,                 # optional
)

print(order.status)
```

{% endtab %}
{% endtabs %}

### Order request fields

<table><thead><tr><th width="166.6875">Field</th><th width="104.08984375">Required</th><th>Description</th></tr></thead><tbody><tr><td>id</td><td>N</td><td>Order ID to assign to the order; if not specified, the Architect OEMS will assign one randomly.</td></tr><tr><td>symbol</td><td>Y</td><td>Tradable product</td></tr><tr><td>dir</td><td>Y</td><td>Order side; BUY or SELL</td></tr><tr><td>quantity</td><td>Y</td><td>Order quantity</td></tr><tr><td>trader</td><td>N</td><td>Trader effecting the order; if not specified, Architect uses the logged-in user</td></tr><tr><td>account</td><td>N</td><td>Account for the order; if not specified, Architect will use the trader's default account configured for the execution venue.</td></tr><tr><td>order_type</td><td>Y</td><td>Order type</td></tr><tr><td>limit_price</td><td>N*</td><td>Required for certain order types</td></tr><tr><td>post_only</td><td>N*</td><td>Required for certain order types</td></tr><tr><td>trigger_price</td><td>N*</td><td>Required for certain order types</td></tr><tr><td>time_in_force</td><td>Y</td><td>Order time-in-force instruction</td></tr><tr><td>execution_venue</td><td>N</td><td>Execution venue for the order; if not specified, Architect will use the primary venue for the symbol.</td></tr></tbody></table>

### Order types

<table><thead><tr><th width="205.31640625">Order type</th><th width="281.23046875">Description</th><th>Required fields</th></tr></thead><tbody><tr><td>LIMIT</td><td>Limit order; execute no worse than the limit price specified.</td><td><ul><li><strong>limit_price</strong></li><li><strong>post_only</strong>: only place the order if it would rest in the book; do not take</li></ul></td></tr><tr><td>STOP_LOSS_LIMIT</td><td>Stop-limit order; if the trigger price is breached, place a limit order at the price specified.</td><td><ul><li><strong>limit_price</strong></li><li><strong>trigger_price</strong></li></ul></td></tr><tr><td>TAKE_PROFIT_LIMIT</td><td>Take-profit order; if the trigger price is breached, place a limit order at the price specified. (Not implemented currently; please message if interested in using)</td><td><ul><li><strong>limit_price</strong></li><li><strong>trigger_price</strong></li></ul></td></tr><tr><td>MARKET</td><td>A market order.</td><td></td></tr></tbody></table>

### Time-in-force instructions

<table><thead><tr><th width="147.65234375">TIF instruction</th><th>Description</th></tr></thead><tbody><tr><td>GTC</td><td>Good-til-cancel</td></tr><tr><td>GTD</td><td>Good-til-date; datetime must be specified</td></tr><tr><td>DAY</td><td>Day order</td></tr><tr><td>IOC</td><td>Immediate-or-cancel</td></tr><tr><td>FOK</td><td>Fill-or-kill</td></tr><tr><td>ATO</td><td>At-the-open</td></tr><tr><td>ATC</td><td>At-the-close</td></tr></tbody></table>

## Place batch order

Place a batch order. Batch orders are multiple orders intended to be executed in a batch. The difference in placing a batch order instead of sending multiple place-orders depends on the specific venue. Some venues have optimized batch order placement APIs or atomicity guarantees that would differentiate it from vanilla multiple orders.

{% tabs %}
{% tab title="Python" %}

```python
from decimal import Decimal
from architect_py import OrderDir
from architect_py.batch_place_order import BatchPlaceOrder

batch = BatchPlaceOrder()

# call `place_order` for each order in the batch;
# orders are added to the batch but not yet submitted
await batch.place_order(
    symbol="BTC Crypto/USD",
    execution_venue="COINBASE",
    account=None,                   
    dir=OrderDir.BUY,
    quantity=Decimal(1),
    limit_price=Decimal(10000),
    post_only=True,                 
)

# send batch order to OMS
await client.place_batch_order(batch)
```

{% endtab %}
{% endtabs %}

## Cancel order

Request to cancel an order by order ID. Cancel requests are asynchronous and return immediately. The order is canceled when the exchange confirms the cancellation.

{% hint style="warning" %}
A working order is only canceled when the exchange confirms the cancellation, which can be checked by polling the order status.
{% endhint %}

{% tabs %}
{% tab title="Python" %}

```python
cancel = await client.cancel_order("12345678-1234-5678-1234-567812345678:0")  

print(cancel.status)
```

{% endtab %}
{% endtabs %}

## Cancel all orders

Request to cancel all orders matching the selectors.

{% tabs %}
{% tab title="Python" %}

```python
await client.cancel_all_orders(execution_venue="CME")
```

{% endtab %}
{% endtabs %}

## Batch cancel orders

Cancel multiple order IDs in one batch. This may or may not have different semantics from individually canceling each order, depending on the venue. Order IDs to be canceled will be batched by their execution venues.

{% tabs %}
{% tab title="Python" %}

```python
await client.batch_cancel_orders(order_ids=[])
```

{% endtab %}
{% endtabs %}

## Reconcile out orders

In cases where the state of an order falls out of sync, e.g. Architect thinks an order is still open but the order is known to be out/canceled by a human, use this manual reconciliation endpoint to force the order out. This is particular common in the case of staled orders.

{% tabs %}
{% tab title="Python" %}

```python
await client.reconcile_out(order_id="a0bcb1f4-4f9d-45c1-8bad-6d1239f0a2e2:0")

# or, reconcile out multiple orders
await client.reconcile_out(order_ids=[])
```

{% endtab %}
{% endtabs %}

## Orderflow channel

The most efficient way to trade using the Architect OEMS is to use the bidirectional orderflow channel. This is similar to a websocket or FIX session where one connection is opened and maintained for an entire trading session. The client will send place order and cancel order requests and receive order status updates and fills in realtime.

The specific mechanics of using the orderflow channel depend on the specific language SDK's implementation.

{% tabs %}
{% tab title="Python" %}
{% hint style="info" %}
Example coming soon
{% endhint %}
{% endtab %}
{% endtabs %}

## Stream orderflow

Subscribe to orderflow events, order status updates, fills from the Architect OEMS. The events streamed are the same as those received by the `orderflow` bidirectional channel.

{% tabs %}
{% tab title="Python" %}
{% hint style="info" %}
See [examples/orderflow\_streaming.py](https://github.com/architect-xyz/architect-py/blob/main/examples/orderflow_streaming.py) for a more comprehensive example.
{% endhint %}

```python
async for event in client.stream_orderflow():
    print(event)
```

{% endtab %}
{% endtabs %}

## Get open orders

Get all open orders matching the selectors.

{% tabs %}
{% tab title="Python" %}

```python
orders = await client.get_open_orders()

for order in orders:
    print(order.id)
```

{% endtab %}
{% endtabs %}

## Get historical orders

Get all historical orders (orders whose statuses are not `PENDING` nor `OPEN`) matching the selectors. If `order_ids` is not specified, then `from_inclusive` and `to_exclusive` are required.

{% tabs %}
{% tab title="Python" %}

```python
orders = await client.get_historical_orders()

for order in orders:
    print(order.id)
```

{% endtab %}
{% endtabs %}

## Get fills

Get all fills matching the selectors.

{% tabs %}
{% tab title="Python" %}

```python
res = await client.get_fills()

for fill in res.fills:
    print(fill.id)
```

{% endtab %}
{% endtabs %}

### Fill IDs

Architect attempts to uniquely identify fills, executions, or trades across all venues. They are typically UUIDv5s which are derived from exchange fill IDs and other characteristics of the fill necessary to make the identifications unambiguous.
