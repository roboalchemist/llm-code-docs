# Source: https://developers.cash.app/cash-app-afterpay/api-reference/reference/data-models/order-details-object.mdx

***

## stoplight-id: ppft83vwa01za

# Order Details object

## Attributes

| Attribute      | Type                                                                                               | Description                                            |
| -------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| consumer       | [Consumer](/cash-app-afterpay/api-reference/reference/data-models/consumer-object)(required)       | The customer who placed or is placing the order.       |
| billing        | [Contact](/cash-app-afterpay/api-reference/reference/data-models/contact-object)                   | The customer's billing address.                        |
| shipping       | [Contact](/cash-app-afterpay/api-reference/reference/data-models/contact-object)                   | The customer's shipping address.                       |
| courier        | [Shipping Courier](/cash-app-afterpay/api-reference/reference/data-models/shipping-courier-object) | The customer's chosen shipping courier.                |
| items          | [Item](/cash-app-afterpay/api-reference/reference/data-models/item-object)                         | An array of order items.                               |
| discounts      | [Discount](/cash-app-afterpay/api-reference/reference/data-models/discount-object)                 | An array of discounts.                                 |
| taxAmount      | [Money](/cash-app-afterpay/api-reference/reference/data-models/money-object)                       | The included tax amount, after applying all discounts. |
| shippingAmount | [Money](/cash-app-afterpay/api-reference/reference/data-models/money-object)                       | The shipping price charged to the customer.            |

## Example Order Details object

```
{
  "consumer": {  
    "phoneNumber": "(415) 200-0000",
    "givenNames": "Joe",
    "surname": "Customer",
    "email": "test@example.com"
  },
  "billing": {
    "name": "Joe Customer",
    "line1": "3655 Lawton St",
    "area1": "San Francisco",
    "region": "CA",
    "postcode": "94122",
    "countryCode": "US",
    "phoneNumber": "(415) 200-0000"
  },
  "shipping": {
    "name": "Joe Customer",
    "line1": "3655 Lawton St",
    "area1": "San Francisco",
    "region": "CA",
    "postcode": "94122",
    "countryCode": "US",
    "phoneNumber": "(415) 200-0000"
  },
  "courier" : {
    "shippedAt" : "2024-01-01T00:00:00-08:00",
    "name" : "FedEx",
    "tracking" : "000 000 000 000",
    "priority" : "STANDARD"
  },
  "items": [  
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
      ]
    },
    {
      "name": "LED Lantern",
      "sku": "12346789",
      "quantity": 1,
      "pageUrl": "https://merchant.example.com/lantern-836599.html",
      "imageUrl": "https://merchant.example.com/lantern-3417-983451-1.jpg",
      "price": {
        "amount": "60.00",
        "currency": "USD"
      },
      "categories": [
        ["Camping & Outdoor", "Lighting", "Lanterns"]
      ]
    }
  ],
  "discounts": [
    {
      "displayName": "10% Off Subtotal",
      "amount": {
        "amount": "10.00",
        "currency": "USD"
      }
    }
  ],
  "taxAmount": {  
    "amount": "0.00",
    "currency": "USD"
  },
  "shippingAmount": {  
    "amount": "20.00",
    "currency": "USD"
  }
}

```
