# Source: https://docs.architect.co/user-guide/architect-platform/trade/order-types.md

# Order Types

Orders can be submitted with differing behaviors depending on the parameters they are sent with, which allow traders better control of their executions in the market.&#x20;

Because of the added risks and unpredictable execution quality, Architect does not natively support Market Orders.&#x20;

## Limit Orders

A limit order is an order with a specified price. A buy order will only be executed at or below the limit price, and a sell order will only be executed at or above the limit price.&#x20;

## Stop Loss / Take Profit

A stop order is an order that does not immediately go live, but instead waits for a price condition to be satisfied before becoming active. These are not supported by every exchange.&#x20;

For a Stop Loss order, managing a long position as an example, the stop loss trigger price will generally be a price below the current market price. If the market falls to the trigger price, a sell order will entered into the market with the specified limit price, which enables the trader to reduce further losses by closing the long position.&#x20;

For a Take Profit order, managing a long position as an example, the take profit trigger price will generally be a price above the current market price. If the market rises to the trigger price, a sell order will be entered into the market with the specified limit price, which enables the trader to realize the gains by closing the long position.&#x20;

## Time in Force (TIF)

Architect currently supports three different choices for Time in Force. Not all are supported by every exchange.

* Good Till Cancel (GTC): These orders remain active until they are completely executed or canceled.
* Good Till Date (GTD): These orders remain active until they are completely executed or canceled. If the specified date is reached, the order will expire and be canceled.
* Immediate or Cancel (IOC): These orders will cancel any remaining portion of the order that does not get immediately filled. Note that for the CME, this is described as a Fill-And-Kill (FAK) order.

## Post-Only

This is a limit order that will only be added to the order book if it does not immediately interact with an existing order, and thus will only be a "maker" and never a "taker". Note that CME does not support this order attribute.

## Ladder

This is Architect's clickable interface for entering limit orders. After specifying an order size, clicking on a price level will send an order to join with the same limit price and direction.&#x20;
