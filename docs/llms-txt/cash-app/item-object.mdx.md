# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/data-models/item-object.mdx

***

## stoplight-id: p003qail9irke

# Item object

## Attributes

| Attribute             | Type                                                                         | Status   | Description                                                                                                                                                                                             |
| --------------------- | ---------------------------------------------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name                  | string                                                                       | required | Product name. Limited to 255 characters.                                                                                                                                                                |
| sku                   | string                                                                       |          | Product SKU. Limited to 128 characters.                                                                                                                                                                 |
| quantity              | integer                                                                      | required | The quantity of the item, stored as a signed 32-bit integer.                                                                                                                                            |
| pageUrl               | string                                                                       |          | The canonical URL for the item's Product Detail Page. Limited to 2048 characters.                                                                                                                       |
| imageUrl              | string                                                                       |          | A URL for a web-optimised photo of the item, suitable for use directly as the `src` attribute of an `img` tag. Limited to 2048 characters.                                                              |
| price                 | [Money](/cash-app-afterpay/api-reference/reference/data-models/money-object) | required | The unit price of the individual item. Must be a positive value.                                                                                                                                        |
| categories            | \[]                                                                          |          | An array of arrays to accommodate multiple categories that apply to the item. Each array represents a hierarchical path to a category, with the left-most category being the top-level parent category. |
| estimatedShipmentDate | string                                                                       |          | The estimated date when the order will be shipped, in YYYY-MM or YYYY-MM-DD format.                                                                                                                     |
| preorder              | boolean                                                                      |          | If this item is not expected to be fulfilled immediately, and therefore should be marked as a preorder at checkout, set to `true`. Set to `false` otherwise.                                            |

## Example Item object

```json
{
  "name": "Blue Carabiner",
  "sku": "12341234",
  "quantity": 1,
  "pageUrl": "https://merchant.example.com/carabiner-354193.html",
  "imageUrl": "https://merchant.example.com/carabiner-7378-391453-1.jpg",
  "price": {
    "amount": "40.00",
    "currency": "USD"
  },
  "categories": [
    ["Sporting Goods", "Climbing Equipment", "Climbing", "Climbing Carabiners"],
    ["Sale", "Climbing"]
  ],
  "estimatedShipmentDate": "2024-03-01"
}
```
