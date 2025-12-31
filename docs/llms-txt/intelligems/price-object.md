# Source: https://docs.intelligems.io/developer-resources/javascript-api/price-object.md

# Price Object

## Overview

If your Shopify theme has a lot of custom javascript, you will likely need to use this API to make price tests work. Common use cases for custom javascript are things like:

* Custom bundle and pack builders
* Custom upsells for an item
* Custom in-cart upsells
* PDPs with lots of customization that don't use a typical `<form type="/cart/add">`

## Get Price by Variant ID

To get the price for a product, you can use `window.igData?.price.getPriceByVariantId()`. This will return the price as a string in currency (i.e. `"29.95"`)

If there is no price test running or this product is not in a price test, we will return null.

#### **Example**

```javascript
...
// Imagine item = product.variant;
// You want the price for that item
const itemPrice = window.igData?.price.getPriceByVariantId(item.id) || item.price;
...
```

## Get Price by Product ID

You may not have a specific variant ID, in which case you intend to look up the price for a product. Since different variants on the product may contain different prices, you must specify if you want the *minimum* or *maximum* price for a given product id. For example:

```javascript
const itemMinPrice = window.igData?.price.getMinPriceByProductId(product.id);
const itemMaxPrice = window.igData?.price.getMaxPriceByProductId(product.id);
```

## Get Compare Price by Variant ID

To get the compare price for a product, you can use `window.igData?.price.getComparePriceByVariantId()`. This will return the compare price as a string in currency (i.e. `"29.95"`)

If there is no price test running or this product is not in a price test, we will return null.

## Get Subscription Discount

To get the price for a product, you can use `window.igData?.price.getSubscriptionDiscountByVariantId()`. This will return the discount object: `{subscriptionDiscount: 10, subscriptionDiscountType: "percentage"}`

The types for subscription discount are: `"percentage" | "dollar"`

#### **Example**

```javascript
...
// Imagine item = product.variant;
// You want the subscription discount for that item
const igSubDisc = window.igData?.price.getSubscriptionDiscountByVariantId(item.id);
console.log("Discount:", igSubDisc?.subscriptionDiscount)
// Discount: 10
...
```
