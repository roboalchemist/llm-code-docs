# Source: https://docs.intelligems.io/developer-resources/custom-add-to-cart-and-order-completed-events.md

# Custom Add to Cart and Order Completed Events

## Add to Carts

Intelligems automatically tracks add-to-carts using a mixture of client-side and server-side data. This automatic tracking is very robust, and can detect add-to-carts where other tools, even Shopify’s reporting, fail to. However, it’s not compatible with headless setups that do not use Shopify’s cart backend. In these cases, you can send a [custom event](https://docs.intelligems.io/analytics/custom-events/custom-javascript-events) to Intelligems on add-to-carts so that built-in add-to-cart reporting works normally:

```javascript
{
    event: "igAddToCart",
    properties: {
        productVariants: [{variantId: 1234, productId: 1234}]
    }
}
```

## Order tracking

For orders to count towards experiment analytics, Intelligems needs to be able to associate orders with the visitor session that created the order. For nearly all setups, this works automatically out-of-the-box. However, if you are creating orders in a custom way or through a third-party app, Intelligems may not receive the data it needs to match orders to sessions. In this case, you can send a [custom event](https://docs.intelligems.io/analytics/custom-events/custom-javascript-events) to Intelligems on order creation with the Shopify order ID:

```javascript
{
    event: "orderPlaced",
    properties: {
       orderId: 123
    }
}
```
