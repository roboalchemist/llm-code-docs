# Source: https://zinc-staging.vercel.app/docs/v2/api-reference/orders/multiple-products-quantities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://zinc-staging.vercel.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Multiple Products & Quantities

> How to order multiple products and specify quantities in a single API request

The Zinc API allows you to order multiple products in a single request and specify quantities for each item.

## Products Array

The `products` array in your order request accepts multiple `OrderProduct` objects. Each product is processed as part of the same order.

<Warning>
  All products in an order must be from the same retailer. You cannot mix products from different retailers in a single order request.
</Warning>

```json  theme={null}
{
  "products": [
    {
      "url": "https://www.amazon.com/dp/B07JGBW826"
    },
    {
      "url": "https://www.amazon.com/dp/B09V3KXJPB"
    }
  ],
  "shipping_address": { ... },
  "max_price": 5000
}
```

## Setting Quantities

Each product can include a `quantity` field to specify how many units to order. What
will be accepted by the retailer depends on the product and availability. We will return
an error code, `product_quantity_not_available` if we are unable to purchase the amount
specified.

* **Range**: 1 to 100
* **Default**: 1 (if omitted)

```json  theme={null}
{
  "products": [
    {
      "url": "https://www.amazon.com/dp/B07JGBW826",
      "quantity": 3
    }
  ],
  "shipping_address": { ... },
  "max_price": 3000
}
```

## Combining with Variants

When ordering products with variants (size, color, etc.), you can combine the `variant` array with `quantity`:

```json  theme={null}
{
  "products": [
    {
      "url": "https://www.amazon.com/dp/B07JGBW826",
      "quantity": 2,
      "variant": [
        {
          "label": "Color",
          "value": "Black"
        },
        {
          "label": "Size",
          "value": "Large"
        }
      ]
    }
  ],
  "shipping_address": { ... },
  "max_price": 4000
}
```

## Complete Example

Here's an example ordering multiple products with different quantities and variants:

```json  theme={null}
{
  "products": [
    {
      "url": "https://www.amazon.com/dp/B07JGBW826",
      "quantity": 2,
      "variant": [
        {
          "label": "Color",
          "value": "Navy"
        }
      ]
    },
    {
      "url": "https://www.amazon.com/dp/B09V3KXJPB",
      "quantity": 1
    },
    {
      "url": "https://www.amazon.com/dp/B08N5WRWNW",
      "quantity": 3,
      "variant": [
        {
          "label": "Size",
          "value": "Medium"
        }
      ]
    }
  ],
  "shipping_address": {
    "name": "John Smith",
    "address_line_1": "123 Main Street",
    "city": "Seattle",
    "state": "WA",
    "postal_code": "98101",
    "country": "US",
    "phone": "206-555-0100"
  },
  "max_price": 15000
}
```

## Max Price Considerations

The `max_price` field applies to the **total order amount** across all products and quantities combined.

<Warning>
  If the total order cost (including all products, quantities, taxes, and shipping) exceeds `max_price`, the order will fail with an error. Set your `max_price` high enough to account for the full order total.
</Warning>

When calculating `max_price`, consider:

* Unit price × quantity for each product
* Applicable taxes
* Shipping costs
* Any additional fees


Built with [Mintlify](https://mintlify.com).