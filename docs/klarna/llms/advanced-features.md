# Source: https://docs.klarna.com/platform-solutions/e-commerce-platforms/salesforce-commerce-cloud/payments/advanced-features.md

# Advanced Features in Salesforce Commerce Cloud

## This section introduces Klarna’s ability to apply payment method-based promotions, allowing you to configure product, order, and shipping discounts based on payment choices. It also explains how Klarna’s API handles price adjustments and taxation, offers details on “Buy Online, Pickup In Store” (BOPIS) integration, and discusses subscription product configurations, including recurring order handling.

### Klarna Payment method based promotions

Starting with the B2C 20.7 release, merchants can use payment methods as qualifiers for product, order, and shipping promotions. By default, when a promotion is configured to use a payment method as a qualifier, the total order amount is shown to the customer upon reaching the review page. This can cause the Klarna authorization call to be made for a higher amount than the final total. To resolve this, when a customer selects a payment option in the billing section, a backend call is triggered. This call recalculates the basket totals, including any applicable promotions, and updates the Klarna session details. Consequently, the Klarna iframe widgets and the mini summary section on the storefront are refreshed to display the final order details. For payment methods other than Klarna, this logic should be customized by the merchant to handle any third-party payment integrations.

### Price adjustment taxation handling

Out of the box, the Klarna API sends product and shipping method details along with relevant discounts as separate line items, as shown below:

``` json
"order lines": [
    {
        "type": "discount",
        "name": "5 Off Ties Promotion"
        "reference": "682875540326M_$5_off_ties_promotion",
        "quantity": 1,
        "merchant_data": "5ties",
        "unit_price": -500,
        "tax_rate": 500,
        "total_amount": -500,
        "total_tax_amount": 0,
        "total_discount_amount": 0,
        "product_url": null,
        "image_url": null
    },
    {
        "type": "physical",
        "name": "Checked Silk Tie",
        "reference": "682875540326M",
        "quantity": 1,
        "unit_price": 1919,
        "tax_rate": 500,
        "total_amount": 1919,
        "total_tax_amount": 68,
        "total_discount_amount": 0
    }
```

#### Handling gross taxation with adjusted prices

Merchants using gross taxation might opt to enable the “Tax Products and Shipping Only Based on Adjusted Price” preference. This preference is located under **Merchant Tools\> Site Preferences\> Pricing and Promotion**, and ensures that price adjustments are not taxed. The setting `kpPromoTaxation` has been introduced for this purpose. Merchants should update this setting to match their promotion configuration as follows:

- **Price (Based on Price):**The product, shipping, and their discounts will be sent as separate line items. This is the default setting.
- **Adjustment (Based on Adjusted Price):** When selected, the product or shipping method line item will be sent with the attribute `total_amount` matching the prorated price and the attribute `total_discount_amount` matching the total sum of all discounts for this item.

``` json
"order lines": [
    {
        "type": "physical",
        "name": "Checked Silk Tie",
        "reference": "682875540326M",
        "quantity": 1,
        "unit_price": 1919,
        "tax_rate": 2200,
        "total_amount": 1419,
        "total_tax_amount": 256,
        "total_discount_amount": 500,
        "product_url": null,
        "image_url": null
    }
```

Enabling this setting is not required for storefronts using net taxation, as the tax is not included in the product's base price. In such cases, the total order sales tax is sent to Klarna as a separate line item, not at the product or shipping line-item level.

### Buy online, pickup in store (BOPIS)

When store pickup is enabled on the storefront, the integration sends store details to Klarna during the authorization request and when placing the Klarna order. Store information is only sent after the customer interacts with the Klarna payment method widgets.

#### Address handling

The store address(es) are included in the Enhanced Merchant Data (EMD) attachment under the `other_delivery_address` attribute when applicable. The handling of addresses in Klarna orders with store pickup is as follows:

- **Orders with Only Store Pickup Shipments:** If there is no home delivery address, the shipping address in the Klarna order will be set to the first store shipment's details.
- **Orders with Both Store Pickup and Home Delivery Shipments:**The home delivery address will be used as the shipping address in the Klarna calls.
- **Orders with No Store Pickups:** No information is sent in the `other_delivery_address` attribute.

``` json
{
    "attachment": {
        "content_type": "application/vnd.klarna.internal.emd-v2+json",
        "body": {
            "other_delivery_address": [{
                "shipping_method": "store pick-up",
                "shipping_type": "normal",
                "first_name": "Test",
                "last_name": "Customer",
                "street_address": "1487 Bay St",
                "street_number": "",
                "postal_code": "01109",
                "city": "Springfield",
                "country": "US"
            }]
        }
    }
}
```

For more information on the options, refer to the [Klarna API reference](https://docs.klarna.com/payments/web-payments/additional-resources/use-cases/extra-merchant-data.md).

### Subscriptions

#### Existing basket subscriptions

The Klarna cartridge supports subscription handling, allowing merchants to offer products as subscriptions, manage subscription details, and handle recurring orders seamlessly.

##### Configuration

Subscription details are configured at the product level. Products can be set as subscription-only, standard, or both. The trial period must be an integer value.


![ Product subscription configuration](ZvMitrVsGrYSv4_A_SFCC-Productsubscriptionconfiguration.jpeg)
*Product subscription configuration*

##### Cart page

There are two types of subscription products:

- **Subscription-only Products**: These are automatically added to the shopping cart as subscription line items.
- **Dual-purpose Products**: For products that can be either subscription or standard, users can select their preference on the cart page.


![ Subscription products on cart page](ZvMjC7VsGrYSv5AT_SFCC-Subscriptionproductsoncartpage.jpeg)
*Subscription products on cart page*

The checkout process will not proceed if the cart contains a mix of standard and subscription products with different trial periods, or if some products have a trial period while others do not. Dropdown menus with predefined values appear on the cart page when there is at least one subscription product in the cart. These values can be configured in the Administration panel under **Site Development\> System Object Types\> Basket - Attribute Definitions**. The attributes available for configuration are:

- `kpSubscriptionFrequency`
- `kpSubscriptionPeriod`


![ Subscriptions details in cart page](ZvMjY7VsGrYSv5Bu_SFCC-Subscriptionsdetailsincartpage.jpeg)
*Subscriptions details in cart page*

##### Checkout

Only logged-in users can complete a subscription checkout. Session intent is defined based on the basket content:

- `tokenize`**tokenize**: Basket contains products with a trial period; user is not charged on order creation.
- `buy_and_tokenize`**buy_and_tokenize**: Basket contains subscription products without a trial period.
- `buy`**buy**: Basket contains only standard products, no subscription products.

For intents `tokenize` and `buy_and_tokenize`, a Klarna customer token for recurring payments is created and stored in the customer profile for future use. Upon order creation, the user profile is updated with subscription data:

1.  **token**: Subscription token.
2.  **enabled**: Status of the subscription.
3.  **nextChargeDate**: Calculated date for the next subscription charge.
4.  **subscriptionPeriod**: Enumerated value representing the subscription period ('week', 'month', or 'year').
5.  **subscriptionFrequency**: Numeric value representing the frequency of the subscription (1, 2, 3, 4, 5, 6, 15).
6.  **subscriptionProductID**: ID of the corresponding subscription product.
7.  **lastOrderID**: ID of the last order for the subscription.

##### Account subscription dashboard

Users can view a full list of their subscriptions in the My Account section. They can cancel subscriptions, which will be displayed with an Inactive status. The Cancel Subscription button deactivates the customer token, preventing further charges.


![ My Account Subscription dashboard](ZvMj97VsGrYSv5EK_sfcc-MyAccountSubscriptiondashboard.jpeg)
*My Account Subscription dashboard*

#### Recurring subscription order creation

A back-end job processes recurring subscriptions for each user in SFCC if subscriptions exist. The job iterates through customers and checks for subscriptions due for payment on the same day.

##### Order creation process

**Create new order**: Using data from`lastOrderID`, a new order is created, and a charge call is made to Klarna using the token and price from `lastOrderID`. **Update details on success**: On success, `nextChargeDate` is updated based on `subscriptionPeriod`, and `lastOrderID` is set to the ID of the newly placed order. The Subscription Dashboard is updated accordingly.

##### Handling failures

**Retry mechanism**: Merchants can configure a retry mechanism with specific retry intervals. If retries fail, the subscription can be deactivated.

- **Retry**: Boolean field (Yes/No).
- **Number of retries**: Number of retries (1, 2, etc.).
- **Retry frequency**: Interval in days (1, 2, etc.).

**Cancel subscription**: If retry is disabled, the subscription is canceled. Orders with trial period subscriptions are paid after the trial period ends. On the next charge date, a new order is created with the channel type set to `SUBSCRIPTIONS`.

#### New `inlineitem` subscripion

##### PDP

Merchants can customize the PDP templates to display the subscription input and customize the KEC or add-to-bag button functionality to send these subscription details in the KEC or add to bag request. Additionally, merchants can choose in which custom attributes these subscription details should be stored for example, SFCC lineitem attribute.


![PDP](PDP.png)
*PDP*
<span>Merchants can customize the cart templates to display the subscription details which the customer selected in PDP page. The subscription details can only be added from PDP and not from cart.</span>

![Checkout](Checkout.png)
*Checkout*

##### Checkout

Both guest and logged-in customers can purchase subscription purchase. The subscription details for each line item are passed to KEC request. Session intent is defined based on the basket content:

- `tokenize`: Basket contains subscription products with a trial period; user is not charged on order creation. Merchants should handle the lineitem unit price calculation. For trial products, the unit price should be set as zero.
- `buy_and_default_tokenize`: Basket contains at least one subscription products without a trial period or both subscription and standard products.
- `buy`: Basket contains only standard products, no subscription products.

===== Subscription object is added to each order line item as below:

``` json
{
    "order_lines": [
        {
            "type": "physical",
            "subscription": {
                "name": "Savings Subscription  {{1234834}}",
                "interval": "MONTH",
                "interval_count": 1
            },
            "reference": "19-402",
            "name": "Prater Ink Cartridges",
            "quantity": 1,
            "unit_price": 360,
            "tax_rate": 0,
            "total_amount": 360,
            "total_discount_amount": 0,
            "total_tax_amount": 0
        }
    ]
}
```

Order `lineitem` sorting ===== <span>The order line items are sorted in each session and order request payload according to priority, with frequency taking precedence, followed by amount. The interval and interval count are converted into days, and the line items are then organized by priority. Products with the longest duration in days are listed first, followed by standard products. For monthly periods, the duration is set to 30 days, and for yearly periods, it is set to 360 days. If two products have the same frequency, the product with the higher price will take priority.</span>

| **Interval** | **Converted days** |
|--------------|--------------------|
| Day          | 1 day              |
| Week         | 7 days             |
| Month        | 30 days            |
| Year         | 360 days           |

## Compatibility

This cartridge has been tested against API Version 22.6 (Compatibility Mode: 22.7) and SFRA version 7.0.0.

## Privacy and payment

### GDPR compliance

The cartridge is compliant with GDPR recommendations and follows best practices to ensure only necessary Personally Identifiable Information (PII) is transmitted to authorize the payment method. For detailed guidelines, refer to the implementation best practices [here](https://docs.klarna.com/policies/payment-solutions-guidelines/eu).

### EMD (Extra Merchant Data)

The cartridge supports sending additional information on the customer's past purchase history and "Buy Online, Pickup in Store" (BOPIS) store addresses when enabled in custom preferences under "Attachments" (`kpAttachments`). The types of data that can be sent as an attachment are detailed[here](https://docs.klarna.com/api/extra-merchant-data/). EMD is required for certain types of merchant orders and generally improves acceptance rates (e.g., `customer_account_info`: past interactions with the merchant store). EMD is included as part of the authorization step in the Commerce Cloud checkout. The data sent to Klarna is customizable and can be viewed in `int_klarna_payments/scripts/payments/additionalCustomerInfo.js`. This script should return a JSON string to be used as the value for the body sub-field of the attachment field as described [here](https://docs.klarna.com/api/extra-merchant-data/). **Example schema for additional customer information** If the example `additionalCustomerInfo.js` file is used unchanged, the data sent to Klarna follows this schema:

``` json
{
    "$schema": "http://json-schema.org/draft-03/schema#",
    "id": "http://klarna.com/v2/emd#",
    "description": "Extended Merchant Data Payload Schema",
    "type": "object",
    "properties": {
        "customer_account_info": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "unique_account_identifier": {
                        "type": "string",
                        "maxLength": 24
                    },
                    "account_registration_date": {
                        "description": "ISO 8601 e.g. 2012-11-24T15:00",
                        "type": "string",
                        "format": "date-time",
                        "pattern": "^[0-9]{4}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-5][0-9](:[0-5][0-9])?Z?$"
                    },
                    "account_last_modified": {
                        "description": "ISO 8601 e.g. 2012-11-24T15:00",
                        "type": "string",
                        "format": "date-time",
                        "pattern": "^[0-9]{4}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-5][0-9](:[0-5][0-9])?Z?$"
                    }
                }
            }
        },
        "payment_history_full": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                    "unique_account_identifier": {
                        "type": "string"
                    },
                    "payment_option": {
                        "type": "string",
                        "enum": ["card", "direct banking", "non klarna credit", "sms", "other"]
                    },
                    "number_paid_purchases": {
                        "type": "integer"
                    },
                    "total_amount_paid_purchases": {
                        "type": "number"
                    },
                    "date_of_last_paid_purchase": {
                        "description": "ISO 8601 e.g. 2012-11-24T15:00",
                        "type": "string",
                        "format": "date-time",
                        "pattern": "^[0-9]{4}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-5][0-9](:[0-5][0-9])?Z?$"
                    },
                    "date_of_first_paid_purchase": {
                        "description": "ISO 8601 e.g. 2012-11-24T15:00",
                        "type": "string",
                        "format": "date-time",
                        "pattern": "^[0-9]{4}-[0-1][0-9]-[0-3][0-9]T[0-2][0-9]:[0-5][0-9](:[0-5][0-9])?Z?$"
                    }
                }
            }
        },
        "other_delivery_address": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                    "shipping_method": {
                        "type": "string",
                        "enum": ["store pick-up", "pick-up point", "registered box", "unregistered box"]
                    },
                    "shipping_type": {
                        "type": "string",
                        "enum": ["normal", "express"]
                    },
                    "first_name": {
                        "type": "string"
                    },
                    "last_name": {
                        "type": "string"
                    },
                    "street_address": {
                        "type": "string"
                    },
                    "street_number": {
                        "type": "string"
                    },
                    "postal_code": {
                        "type": "string"
                    },
                    "city": {
                        "type": "string"
                    },
                    "country": {
                        "type": "string"
                    }
                }
            }
        }
    }
}
```

**Example data**

``` json
{
    "attachment": {
        "content_type": "application/vnd.klarna.internal.emd-v2+json",
        "body": {
            "customer_account_info": [{
                "unique_account_identifier": "5509d9f7c8720c0e4575154b",
                "account_registration_date": "2015-03-18T20:03:03Z",
                "account_last_modified": "2015-03-18T20:03:03Z"
            }],
            "payment_history_full": [{
                "unique_account_identifier": "5509d9f7c8720c0e4575154b",
                "payment_option": "card",
                "number_paid_purchases": 23,
                "total_amount_paid_purchases": 140023,
                "date_of_last_paid_purchase": "2015-03-18T20:03:03Z",
                "date_of_first_paid_purchase": "2015-03-18T20:03:03Z"
            }],
            "other_delivery_address": [{
                "shipping_method": "store pick-up",
                "shipping_type": "normal",
                "first_name": "Test",
                "last_name": "Customer",
                "street_address": "1487 Bay St",
                "street_number": "",
                "postal_code": "01109",
                "city": "Springfield",
                "country": "US"
            }]
        }
    }
}
```

When the customer uses Guest Checkout, the EMD sent includes `payment_history_full[0].unique_account_identifier` (cqcid value set by SFCC), and all other fields are empty.

### PCI-DSS compliance

The virtual card (MCSv3) solution enables settlements using individual virtual cards issued against a Klarna order. To comply with PCI-DSS requirements, merchants must ensure that data is securely maintained and transmitted as part of their operation in their live store environment. The required steps must be completed in consultation with your payment service provider/acquirer before going live. Review the order export details required for virtual card-based Klarna orders in advance. Any historical decrypted PCI data should be expunged, regardless of the VCN validity date. **DO NOT SAVE UNENCRYPTED PCI DATA ON THE SERVER!**