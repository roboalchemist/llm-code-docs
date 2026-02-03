# Pass line-item details

You can pass the details of the items a buyer purchases, to PayPal, through the [Create order request](#create-an-order-and-pass-line-item-details). When a buyer checks out their purchase, PayPal displays these invoice-line-item details, such as the item name, quantity, detailed description, price, for buyer verification.

## Buyer experience

The details you pass to PayPal are presented to the buyer:

- On the PayPal review page during the Pay with PayPal flow.
- In the post-purchase email sent to the buyer about their payment transaction.
- In the buyer’s PayPal account **Activity** > **Transactions** > **All transactions** section.

Displaying the purchase details:

- Enhances buyer experience.
- Provides greater transparency and increases conversion.
- Minimizes disputes as buyers can verify the specifics of their purchase.
- Enhances dispute management by providing merchants with specifics about the disputed item.

The following image shows a PayPal review page with the line-item details.

![Paysheet,with,line-item,details](https://www.paypalobjects.com/devdoc/Paysheet%20with%20line-item%20details.png)

## How it works

- [Pass the buyer's purchase details to PayPal](#create-an-order-and-pass-line-item-details). PayPal displays these details on the PayPal review page for buyer verification.
- [Optional] [Confirm whether the PayPal review page details match the details in your system](#optional-retrieve-line-item-details).
- [Handle buyer updates to the shipping addresses or options](#handle-shipping-updates-that-modify-line-items) that modify line-items.
- [Handle buyer updates to the purchases](#handle-buyer-updates-to-line-items) before you capture the order and complete payment processing.

In your app code, when you [Create an Order](https://developer.paypal.com/studio/checkout/standard/integrate#create-order), as part of the request body,

- Send the line-item details in the `purchase_units[].items[]` array. If multiple line items exist, send multiple `item` objects in the array. Use the following attributes:
  - `name`: Name of the purchased item.
  - `quantity`: Quantity of the item, specified as a whole number.
  - `unit_amount`: Price or rate for a single unit of item, specified as an object with two keys - `currency_code` and `value`.
  - `description`: Detailed item description.
  - `sku`: Stock keeping unit (SKU) for the item.
  - `url`: URL to the purchased item. Visible to buyer and used in buyer experiences.
  - `category`: Item category type. **Possible values**: **DIGITAL_GOODS**, **PHYSICAL_GOODS**, **DONATION**
  - `image_url`: URL of the item's image. File type and size restrictions apply. An image that violates these restrictions will not be honored.
  - `tax`: The item tax for each unit, specified as an object. **Note**: If `tax` is specified, ensure to enter a valid value for `purchase_units[].amount.breakdown.tax_total`.

- Send additional details, such as the total amount breakdown in [purchase_units[].amount.breakdown](https://developer.paypal.com/docs/api/orders/v2/#orders_create!ct=application/json<path=purchase_units/amount/breakdown>t=request).

After a successful processing of the Create order request and subsequent buyer log-in, PayPal displays the line-item details on a PayPal review page for buyer verification.

**Sample request**

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'Content-Type: application/json' \
-H 'PayPal-Request-Id: REQUEST-ID' \
-H 'Authorization: Bearer ACCESS-TOKEN' \
-d '{ \
    "intent": "CAPTURE", \
    "purchase_units": [ \
        { \
            "invoice_id": "90210", \
            "items": [ \
                { \
                    "name": "T-Shirt", \
                    "description": "Super Fresh Shirt", \
                    "unit_amount": { \
                        "currency_code": "USD", \
                        "value": "20.00" \
                    }, \
                    "quantity": "1", \
                    "category": "PHYSICAL_GOODS", \
                    "sku": "sku01", \
                    "image_url": "https://example.com/static/images/items/1/tshirt_green.jpg", \
                    "url": "https://example.com/url-to-the-item-being-purchased-1", \
                    "upc": { \
                        "type": "UPC-A", \
                        "code": "123456789012" \
                    }, \
                    "tax": { \
                        "currency_code": "USD", \
                        "value": "10.00" \
                    } \
                }, \
                { \
                    "name": "Shoes", \
                    "description": "Running, Size 10.5", \
                    "sku": "sku02", \
                    "unit_amount": { \
                        "currency_code": "USD", \
                        "value": "100.00" \
                    }, \
                    "quantity": "2", \
                    "category": "PHYSICAL_GOODS", \
                    "image_url": "https://example.com/static/images/items/1/shoes_running.jpg", \
                    "url": "https://example.com/url-to-the-item-being-purchased-2", \
                    "upc": { \
                        "type": "UPC-A", \
                        "code": "987654321012" \
                    }, \
                    "tax": { \
                        "currency_code": "USD", \
                        "value": "5.00" \
                    } \
                } \
            ], \
            "amount": { \
                "currency_code": "USD", \
                "value": "230.00", \
                "breakdown": { \
                    "item_total": { \
                        "currency_code": "USD", \
                        "value": "220.00" \
                    }, \
                    "shipping": { \
                        "currency_code": "USD", \
                        "value": "10.00" \
                    }, \
                    "tax_total": { \
                        "currency_code": "USD", \
                        "value": "20.00" \
                    } \
                } \
            } \
        } \
    ] \
}
'
```

To confirm whether the line-item(s) details with PayPal match the details in your system, you can use the [Show order details](https://developer.paypal.com/docs/api/orders/v2/#orders_get) API request to retrieve the details in an order and verify them.

**Note**: In the request, ensure to specify the order ID of the order (whose details you want to retrieve), as the path parameter.

**Sample request**

```curl
curl -v -X GET https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER-ID \
-H 'Authorization: Bearer ACCESS-TOKEN'
```

**Sample response**

```json
{
    "intent": "CAPTURE",
    "purchase_units": [
        {
            "invoice_id": "90210",
            "amount": {
                "currency_code": "USD",
                "value": "230.00",
                "breakdown": {
                    "item_total": {
                        "currency_code": "USD",
                        "value": "220.00"
                    },
                    "shipping": {
                        "currency_code": "USD",
                        "value": "10.00"
                    },
                    "tax_total": {
                        "currency_code": "USD",
                        "value": "20.00"
                    }
                }
            },
            "items": [
                {
                    "name": "T-Shirt",
                    "description": "Super Fresh Shirt",
                    "unit_amount": {
                        "currency_code": "USD",
                        "value": "20.00"
                    },
                    "quantity": "1",
                    "category": "PHYSICAL_GOODS",
                    "sku": "sku01",
                    "image_url": "https://example.com/static/images/items/1/tshirt_green.jpg",
                    "url": "https://example.com/url-to-the-item-being-purchased-1",
                    "upc": {
                        "type": "UPC-A",
                        "code": "123456789012"
                    },
                    "tax": {
                        "currency_code": "USD",
                        "value": "10.00"
                    }
                },
                {
                    "name": "Shoes",
                    "description": "Running, Size 10.5",
                    "sku": "sku02",
                    "unit_amount": {
                        "currency_code": "USD",
                        "value": "100.00"
                    },
                    "quantity": "2",
                    "category": "PHYSICAL_GOODS",
                    "image_url": "https://example.com/static/images/items/1/shoes_running.jpg",
                    "url": "https://example.com/url-to-the-item-being-purchased-2",
                    "upc": {
                        "type": "UPC-A",
                        "code": "987654321012"
                    },
                    "tax": {
                        "currency_code": "USD",
                        "value": "5.00"
                    }
                }
            ]
        }
    ]
}
```