# Shipping module

## Overview

The shipping module presents shipping details to a buyer during the Pay with PayPal and Pay with Venmo flow. The merchant has several options available for controlling how shipping addresses and shipping options are handled. The server-side shipping callbacks allow you to update the shipping and order amount information as buyers make changes on the review page.

### Merchant and buyer interaction

Buyers can use the shipping module to specify the shipping address and shipping options on the review page. The system sends a callback to the merchant's URL with the updated shipping information.

When the buyer provides their shipping address, a callback is sent to the merchant server with the buyer's address using the server-side shipping callbacks. In response, the merchant can send the shipping options and updated order cost amounts.

You can use server-side callbacks to:

- Verify that you support the shipping method.
- Update shipping costs.
- Change line items in the cart.
- Inform the buyer that you do not support their shipping method.

**info**
While both server-side and client-side callbacks are possible, it is generally recommended to use server-side callbacks, as client-side callbacks may not be available in all situations. For example, client-side callbacks using JS-SDK are designed primarily for web-based integrations and are incompatible with Venmo. They may not be suitable for native mobile applications that often require different APIs or SDKs tailored for mobile platforms.

The following sample PayPal and Venmo review pages show a buyer's shipping address and options:

![image](https://www.paypalobjects.com/devdoc/ShipModPWVReviewUpdates.png)

## How it works

The shipping address and options callback process involves the following steps:

- A buyer clicks on the PayPal or Venmo button displayed on the merchant site.
- The merchant makes a Create Order API request to set up the flow, including the parameters needed to enable the server-side callbacks.
- The buyer is taken to the flow where they are authenticated and shown the review page.
- A server-side callback is created to the merchant's server with the default shipping address from the buyer's wallet.
- The merchant processes the callback and responds with shipping options for the address and updated order amount.
- The review page updates to reflect the merchant's revised order amount and shipping options.
- If the buyer changes the shipping address or shipping options, a callback is made to the merchant. The merchant's response updates the review page.
- The buyer clicks the pay button on the review page to complete the transaction, which is returned to the merchant.
- The merchant may make a Show Order Details API call to get the final order information and verify it still matches the information in their system.
- The merchant captures the order to complete the transaction.

## Create order

Use the Orders v2 API [Create Order](https://developer.paypal.com/studio/checkout/standard/integrate#create-order) request to set up the flow used by the buyer to approve a transaction. Both Pay with PayPal and Pay with Venmo support the shipping module. The request can utilize either payment\_source:paypal or payment\_source:venmo. There are several ways to determine how the shipping address and options are displayed on the review page and which events create callbacks when the buyer interacts with them.

### Enabling server-side callbacks

The payment\_source.\*\.experience\_context.order\_update\_callback\_config object is used to enable and configure server-side callbacks during the flow. The callback\_url field specifies the endpoint on your servers where the callback request is sent. The callback\_events array specifies which callback events you support. The flow supports the following events:

- SHIPPING\_ADDRESS : This event happens when the review page loads for the first time and when the buyer changes their shipping address. We recommend merchants to subscribe only to SHIPPING\_ADDRESS . This requires a merchant to respond with all the shipping options and amounts calculated on the initial callback. Since all options have been returned, the merchant callback does not have to be called when the selection option changes. This method reduces delays and the number of requests.
- SHIPPING\_OPTIONS : This event happens when the buyer selects new shipping options and when they change shipping options. We recommend merchants subscribe to this if they want to be notified or need to recalculate amounts with their callback URL when a selected shipping option changes for the current address. If SHIPPING\_OPTIONS is not needed by the merchant, they should subscribe to SHIPPING\_ADDRESS .

### Configuring shipping preferences

The shipping preference is set using the payment\_source.\*\.experience\_context.shipping\_preference field. There are 3 possible values:

- GET\_FROM\_FILE : This default preference retrieves the customer-provided shipping address from their wallet.
- NO\_SHIPPING : This option removes the shipping address information from the review page and the API response. However, the shipping.phone\_number and shipping.email\_address fields are returned for digital goods delivery.
- SET\_PROVIDED\_ADDRESS : The review page shows the shipping address provided by the merchant in the create order request. The buyer cannot change this address on the review page. If the merchant does not pass an address, the buyer can choose the address on the review page.

If you do not pass a shipping preference, the default behavior is GET\_FROM\_FILE . The review page shows the default shipping address from the buyer's wallet. The buyer can select a different shipping address from their wallet or add a new address. Callbacks happen if the shipping preference is GET\_FROM\_FILE .

### Passing a shipping address

If you have a shipping address from the buyer, pass it to Pay with PayPal or Pay with Venmo on the create order request. If you pass a shipping address with a shipping preference of GET\_FROM\_FILE , it will display on the review page, where the buyer can change the shipping address. You can use the shipping preference SET\_PROVIDED\_ADDRESS to prevent the buyer from changing the shipping address on the review page. If your transaction does not involve shipping, you can pass the shipping preference NO\_SHIPPING and no shipping information will be displayed on the review page.

Here is a sample Create Order API request to a merchant with a callback config for Pay with PayPal (payment\_source:paypal) and Pay with Venmo (payment\_source:venmo).

#### `Pay with PayPal`

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'Content-Type: application/json' \
-H 'PayPal-Request-Id: 7b92603e-77ed-4896-8e78-5dea2050476a' \
-H 'Authorization: Bearer 6V7rbVwmlM1gFZKW_8QtzWXqpcwQ6T5vhEGYNJDAAdn3paCgRpdeMdVYmWzgbKSsECednupJ3Zx5Xd-g' \
-d '{\
      "intent": "CAPTURE", "payment_source": {\
        "paypal": {\
          "experience_context": {\
            "user_action": "PAY_NOW",\
            "shipping_preference": "GET_FROM_FILE",\
            "return_url": "https://example.com/returnUrl",\
            "cancel_url": "https://example.com/cancelUrl",\
            "order_update_callback_config": {\
              "callback_events": ["SHIPPING_ADDRESS", "SHIPPING_OPTIONS"],\
              "callback_url": "https://example.com/orders?cart_id=h98h98h\u0026session_id=89h788fg8"
            }
          }
        }
      }, "purchase_units": [{\
        "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",\
        "items": [{\
          "name": "T-Shirt",\
          "description": "Super Fresh Shirt",\
          "unit_amount": {\
            "currency_code": "USD",\
            "value": "50.00"
          },\
          "quantity": "1",\
          "category": "PHYSICAL_GOODS",\
          "sku": "sku01",\
          "image_url": "https://example.com/static/images/items/1/tshirt_green.jpg",\
          "url": "https://example.com/url-to-the-item-being-purchased-1",\
          "upc": {\
            "type": "UPC-A",\
            "code": "123456789012"
          }
        }, {\
          "name": "Shoes",\
          "description": "Running, Size 10.5",\
          "sku": "sku02",\
          "unit_amount": {\
            "currency_code": "USD",\
            "value": "25.00"
          },\
          "quantity": "2",\
          "category": "PHYSICAL_GOODS",\
          "image_url": "https://example.com/static/images/items/1/shoes_running.jpg",\
          "url": "https://example.com/url-to-the-item-being-purchased-2",\
          "upc": {\
            "type": "UPC-A",\
            "code": "987654321012"
          }
        }],\
        "amount": {\
          "currency_code": "USD",\
          "value": "100.00",\
          "breakdown": {\
            "item_total": {\
              "currency_code": "USD",\
              "value": "100.00"
            }
          }
        }
      }]
    }'
```

#### `Pay with Venmo`

```curl
curl -v -X POST https://api-m.sandbox.paypal.com/v2/checkout/orders \
-H 'Content-Type: application/json' \
-H 'PayPal-Request-Id: 7b92603e-77ed-4896-8e78-5dea2050476a' \
-H 'Authorization: Bearer 6V7rbVwmlM1gFZKW_8QtzWXqpcwQ6T5vhEGYNJDAAdn3paCgRpdeMdVYmWzgbKSsECednupJ3Zx5Xd-g' \
-d '{\
      "intent": "CAPTURE", "payment_source": {\
        "venmo": {\
          "experience_context": {\
            "user_action": "PAY_NOW",\
            "shipping_preference": "GET_FROM_FILE",\
            "return_url": "https://example.com/returnUrl",\
            "cancel_url": "https://example.com/cancelUrl",\
            "order_update_callback_config": {\
              "callback_events": ["SHIPPING_ADDRESS", "SHIPPING_OPTIONS"],\
              "callback_url": "https://example.com/orders?cart_id=h98h98h\u0026session_id=89h788fg8"
            }
          }
        }
      }, "purchase_units": [{\
        "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",\
        "items": [{\
          "name": "T-Shirt",\
          "description": "Super Fresh Shirt",\
          "unit_amount": {\
            "currency_code": "USD",\
            "value": "50.00"
          },\
          "quantity": "1",\
          "category": "PHYSICAL_GOODS",\
          "sku": "sku01",\
          "image_url": "https://example.com/static/images/items/1/tshirt_green.jpg",\
          "url": "https://example.com/url-to-the-item-being-purchased-1",\
          "upc": {\
            "type": "UPC-A",\
            "code": "123456789012"
          }
        }, {\
          "name": "Shoes",\
          "description": "Running, Size 10.5",\
          "sku": "sku02",\
          "unit_amount": {\
            "currency_code": "USD",\
            "value": "25.00"
          },\
          "quantity": "2",\
          "category": "PHYSICAL_GOODS",\
          "image_url": "https://example.com/static/images/items/1/shoes_running.jpg",\
          "url": "https://example.com/url-to-the-item-being-purchased-2",\
          "upc": {\
            "type": "UPC-A",\
            "code": "987654321012"
          }
        }],\
        "amount": {\
          "currency_code": "USD",\
          "value": "100.00",\
          "breakdown": {\
            "item_total": {\
              "currency_code": "USD",\
              "value": "100.00"
            }
          }
        }
      }]
    }'
```

## Server-side shipping callbacks

The Server-Side Callback API request to a merchant is consistent with GET orders and includes selected addresses and options outside of the order object.

- Sending order data is structurally similar to making a GET request.
- Updated shipping addresses and options separately sent from the order to avoid confusion.
- If the address or option is incomplete, it will not be set in order to prevent misunderstandings.
- The cart identifier will be embedded in the callback URL if merchants cannot associate their shopping cart with the order.
- Merchants with client-side shopping carts should include item details when they create the order for server-side shipping callbacks.

### Callback request to merchant for shipping address event

The following sample is a server-side callback request to the merchant for a shipping event. The callback identifies the order, shipping\_address , shipping\_option and purchase\_units .

**warning**
The initial callback to the merchant does not include the "shipping\_option" section.

#### `Sample - Callback request to merchant for shipping address event`

```javascript
{
  "id": "5O190127TN364715T",
  "shipping_address": {
    "country_code": "US",
    "admin_area_1": "TX",
    "admin_area_2": "Dallas",
    "postal_code": "75001"
  },
  "shipping_option": {
    "id": "2",
    "amount": {
      "currency_code": "USD",
      "value": "20.00"
    },
    "type": "SHIPPING",
    "label": "Free Shipping"
  },
  "purchase_units": [{
    "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
    "amount": {
      "currency_code": "USD",
      "value": "100.00"
    }
  }]
}
```

### Callback request fields

| **Field** | **Description** | **Data type** |
| --- | --- | --- |
| id | Unique identifier for the shipping order. For example, 5O190127TN364715T . | string |
| shipping\_address | Shipping address information. Includes country\_code , admin\_area\_1 , admin\_area\_2 , and postal\_code . | object |
| country\_code | Identifies the shipping address country. For example, US . | string |
| admin\_area\_1 | Identifies the shipping address state or region. For example, TX . | string |
| admin\_area\_2 | Identifies the shipping address, city, or municipality. For example, Dallas . | string |
| postal\_code | Identifies the postal code. For example, 7500 . | number |
| shipping\_option | Shipping option information. Includes id , amount , type , label , and selected . | string |
| selected | Determines which option is selected by default.Possible values aretrueorfalse | boolean |
| id | Indicates the type of shipping option. For example, 2 . | number |
| amount | Shipping option amount. Includes currency\_code and value . | object |
| currency\_code | Indicates the type of currency. For example, USD . | string |
| value | String denoting the purchase price and shipping option price, formatted as X.XX . For example, 2.00 . | number |
| type | An enum that indicates the type of shipping. For example, SHIPPING or PICKUP . | string |
| label | Dropdown menu option selected by the buyer. Indicates whether the shipping is free or not. For example, Free Shipping . | string |
| purchase\_units | Defines the purchase unit. Includes reference\_id and amount . | object |
| reference\_id | Identifier associated with the purchase units. For example, d9f80740-38f0-11e8-b467-0ed5f89f718b . | string |

The merchant response to a server-side callback request is similar to an order. A change to the customer’s shipping address or options can affect the following fields within the data structure:

- purchase\_units\[\].shipping.options represent the shipping modules associated with the purchase units within the order. The purchase order field includes contact and delivery information, including phone number, account email address, order ID, and reference ID.
- purchase\_units\[\].amount represents the purchase unit amount in the order.

Buyer changes can be managed through one of the following approaches:

- Asking the merchant to return an updated order limited to the fields that can be changed.
- Asking the merchant to return a list of patch operations.

### Merchant success response

When the order request is acceptable, the merchant responds with a success message that contains amount and shipping option changes.

Here is a sample HTTP 200 OK callback response from a merchant with shipping options and amount updates.

#### `Code sample, Merchant success response`

```javascript
{
  "id": "8HFTASDATTV",
  "purchase_units": [{
    "reference_id": "d9f80740-38f0-11e8-b467-0ed5f89f718b",
    "amount": {
      "currency_code": "USD",
      "value": "105.00",
      "breakdown": {
        "item_total": {
          "currency_code": "USD",
          "value": "100.00"
        },
        "tax_total": {
          "currency_code": "USD",
          "value": "5.00"
        },
        "shipping": {
          "currency_code": "USD",
          "value": "0.00"
        }
      }
    },
    "shipping_options": [{
      "id": "1",
      "amount": {
        "currency_code": "USD",
        "value": "0.00"
      },
      "type": "SHIPPING",
      "label": "Free Shipping",
      "selected": true
    }, {
      "id": "2",
      "amount": {
        "currency_code": "USD",
        "value": "7.00"
      },
      "type": "SHIPPING",
      "label": "USPS Priority Shipping",
      "selected": false
    }, {
      "id": "3",
      "amount": {
        "currency_code": "USD",
        "value": "10.00"
      },
      "type": "SHIPPING",
      "label": "1-Day Shipping",
      "selected": false
    }]
  }]
}
```