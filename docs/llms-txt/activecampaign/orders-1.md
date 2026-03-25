# Source: https://developers.activecampaign.com/reference/orders-1.md

# Orders

# Orders

When created in the Ecommerce GraphQL API, orders go through a multiple step asynchronous process as follows:

1. API call to create order
2. Custom Object saved to Custom Object data store (see: [Ecommerce GraphQL API and Custom Objects](https://developers.activecampaign.com/reference/graphql-overview#ecommerce-graphql-api-and-custom-objects))
3. Order data written to v3, DeepData [order](https://developers.activecampaign.com/reference/orders) and [customer](https://developers.activecampaign.com/reference/customers) APIs.

When an API call is made to create an order, a contact and an Ecommerce Customer are immediately created in ActiveCampaign. Asynchronously (usually within a few seconds), the Custom Object records are written. After those are completed, another asynchronous step runs to copy that order data into the v3 DeepData data store.

If a user writes directly to the v3 DeepData order API, that data will never be copied back into the Custom Object data store. The data will be out of sync. For this reason, we suggest never using the v3 DeepData order API directly. Rather, write all orders to the GraphQL API.

The `Order Created` and `Order Updated` triggers happen on Custom Object data.

The `Makes a Purchase` trigger happens on v3 DeepData order data.

Segments such as `Last Order` and `Any Order` trigger from the v3 DeepData order data.

Segments on `Order` trigger on Custom Object data, and specifically, on any Custom Object order under that contact. When an automation uses a Custom Object trigger, such as `Order Created` or `Order Updated`, then a new type of segment is available: `This Order`. `This Order` refers to the Custom Object order that triggered this automation.

## Contact information

The following describes how fields from the GraphQL API are used to create contacts in ActiveCampaign.

| Contact Field | GraphQL Order Field                                                                                                                                                                         |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `email`       | `email`                                                                                                                                                                                     |
| `firstName`   | If `customerData.firstName` is provided in order, that will be used. Otherwise, `shippingAddress.firstName` will be used. If that is not provided, `billingaddress.firstName` will be used. |
| `lastName`    | If provided,`customerData.lastName` will be used. Otherwise, `shippingAddress.lastName` will be used. If that is not provided, `billingaddress.lastName` will be used.                      |
| `phone`       | If provided,`customerData.phone` will be used. Otherwise, `shippingAddress.phone` will be used. If that is not provided, `billingaddress.phone` will be used.                               |
| orgname       | `customerData.company`                                                                                                                                                                      |

In addition, the updating or creating an order in the GraphQL API will update or create an [ecommerce customer object](https://developers.activecampaign.com/reference/customers) with the following mappings:

| Customer Field        | GraphQL Field                      |
| :-------------------- | :--------------------------------- |
| `connectionid`        | `legacyConnectionId`               |
| `externalid`          | `storeCustomerId`                  |
| `email`               | `email`                            |
| `acceptsMarketing`    | `acceptsMarketing`                 |
| `smsMarketingState`   | `customerData.smsMarketingState`   |
| `smsOptInLevel`       | `customerData.smsOptInLevel`       |
| `smsConsentUpdatedAt` | `customerData.smsConsentUpdatedAt` |

# Abandoned Carts

Data for [carts](https://developers.activecampaign.com/reference/e-commerce-abandoned-carts), which triggers the abandoned cart automation, is only available in the v3 DeepData APIs.

Shopify and WooCommerce integrations follow this pattern for carts:

1. When a cart is created, it is tracked using the v3 order API.
2. When a user places an order for that cart, the cart transitions to an order, and that order is written to the GraphQL API. The cart in the v3 API will then transition to a v3 order (for more info on this, see: [abandoned carts](https://developers.activecampaign.com/reference/e-commerce-abandoned-carts)).

# Queries

## getOrder

Used for retrieving a single order by primary identifiers.

### Example Payload

```Text GraphQL
{
  getOrder(
    legacyConnectionId: 1, 
    storeOrderId: "storeOrder123"
  ) 
  {
    storeOrderId
    email
    lineItems {
      name
      quantity
      priceAmount
    }
    # Additional order fields may be requested here.
  }
}
```

### Example Response

```Text json
{
    "data": {
        "getOrder": {
            "storeOrderId": "4372658389131",
            "email": "jstolltest@activecampaign.com",
            "lineItems": [
                {
                    "name": "Red Spatula,
                    "quantity": 1,
                    "priceAmount": 90.00
                }
            ]
        }
    }
}
```

**Return Type**: [Order](https://developers.activecampaign.com/reference/orders-1#order-object)

**Arguments for `getOrder`**

| Name                     | Description                       |
| :----------------------- | :-------------------------------- |
| legacyConnectionId (int) | the order's legacy connection id. |
| storeOrderId (string)    | the order's store order id.       |

## searchOrder

### Example Payload

```text GraphQL
{  searchOrder (filter: {
    email: {
        value: "spatula@activecampaign.com"
        filterOperator: EQ
        sort: ASC
    }
    # Alternate filters may be applied here.
  })
  {
    storeOrderId
    email
    orderNumber
    # Additional order fields may be requested here in response
  }
}
```

```Text json
{
    "data": {
        "searchOrder": [
            {
                "storeOrderId": "4372658389131",
                "email": "spatulas@activecampaign.com",
                "orderNumber": "1001"
            },
            {
                "storeOrderId": "4697224478859",
                "email": "spatulas@activecampaign.com",
                "orderNumber": "1004"
            }
        ]
    }
}
```

For information on how filters and search requests work, see: [Searches](https://developers.activecampaign.com/reference/searches).

**Return Type**: [Order\[\]](https://developers.activecampaign.com/reference/orders-1#order-object)

**Arguments for `searchOrder`**

| Name                 | Description       |
| :------------------- | :---------------- |
| filter (OrderFilter) | The order filter. |

# Mutations

## upsertOrder

Insert a single order, or update it if is already exists. Existence is based on a combination of legacyConnectionId and sotreOrderId.

### upsertOrder Example Payload

```Text GraphQL
mutation {
  upsertOrder(
    order: 
      {
        email: "spatulas@activecampaign.com"
        legacyConnectionId: 1
        storeOrderId: "storeId123"
        storeCustomerId: "storeCustomer123"
        orderNumber: "123"
        cartId: "cart123"
        storeExternalOrderId: "storeExternal123"
        creationSource: REAL_TIME
        storeCreatedDate: "2023-05-03T10:48:23Z"
        storeModifiedDate: "2023-05-03T10:48:23Z"
        storeStatus: "Order_Complete"
        normalizedStatus: COMPLETED
        locationId: "dinosaur_colorado"
        shippingMethod: "express"
        orderUrl: "https://myStore.com/orders/123"
        isTestOrder: false
        createdByRecurringPayment: false
        acceptsMarketing: true
        customerLocale: "EN_US"
        salesChannel: "web_store"
        currency: "USD"
        finalAmount: 100.01
        shippingAmount: 25.25
        discountsAmount: 12.25
        paymentMethod: "credit_card"

        billingAddress: {
          firstName: "Jane"        
					lastName: "Doe"
          address1: "1 N. Deerborn St."
          address2: "Unit #5"
          address3: "Door #3"
          city: "Chicago"
          province: "IL"
          country: "US"
          postal: "60601"
          phone: "6005550125"
          company: "ActiveCampaign"
          email:  "spatulas@activecampaign.com"
        }
        shippingAddress: {
          firstName: "Jane"        
					lastName: "Doe"
          address1: "1 N. Deerborn St."
          address2: "Unit #5"
          address3: "Door #3"
          city: "Chicago"
          province: "IL"
          country: "US"
          postal: "60601"
          phone: "6005550125"
          company: "ActiveCampaign"
          email:  "spatulas@activecampaign.com"
        }
        lineItems: [
          {
            name: "SuperSpatula"
            quantity: 500
            priceAmount: 12.20
            productStorePrimaryId: "SUUUUPER"
            storeBaseProductId: "BaseyBase"
          }
        ]
        customerData: {
          firstName: "Jane"
          lastName: "Doe"
          phone: "6005550125"
          company: "ActiveCampaign"
          smsConsentUpdatedDate: "2041-11-16T10:48:23Z"
          smsMarketingState: UNSUBSCRIBED
          smsOptInLevel: UNKNOWN
        }
        discounts: [
          {
             name: "Shipping Promo"
             type: SHIPPING
             discountAmount: 12.25
          }
        ]
        notes: [
          "Order was delayed for customer"
          "Customer complaint received"
        ]
      }
  ) {
      storeOrderId
			connectionId
			email
			creationSource
      # More fields may be requested here.
  }
}

```

#### Input fields for `UpsertOrder`

`order` (`[[OrderInput](https://developers.activecampaign.com/reference/orders-1#order-object)](https://developers.activecampaign.com/reference/orders-1#order-object)`)

#### Return fields for `UpsertOrder`

`[[Order](https://developers.activecampaign.com/reference/orders-1#order-object)](https://developers.activecampaign.com/reference/orders-1#order-object)`

## bulkUpsertOrders

Insert multiple orders, or update it if is already exists. Existence is based on a combination of legacyConnectionId and sotreOrderId.

#### Input fields for `[bulkUpsertOrders](https://developers.activecampaign.com/reference/orders-1#order-object)`

`orders` (`[[OrderInput](https://developers.activecampaign.com/reference/orders-1#order-object)](https://developers.activecampaign.com/reference/orders-1#order-object)[]`)

#### Return fields for `bulkUpsertOrders`

`[[Order](https://developers.activecampaign.com/reference/orders-1#order-object)](https://developers.activecampaign.com/reference/orders-1#order-object)[]`

## bulkUpsertOrdersAsync

bulkUpsertOrdersAsync is similar to the bulkUpsertOrders API, except that the data store write happens completely asynchronously. Thus, it is much higher throughput. This API is recommended for all stores.

```Text GraphQL
mutation {
  bulkUpsertOrdersAsync(
    orders: [
      {
        email: "spatulas@activecampaign.com"
        legacyConnectionId: 1
        storeOrderId: "storeId123"
        storeCustomerId: "storeCustomer123"
        orderNumber: "123"
        cartId: "cart123"
        storeExternalOrderId: "storeExternal123"
        creationSource: REAL_TIME
        storeCreatedDate: "2023-05-03T10:48:23Z"
        storeModifiedDate: "2023-05-03T10:48:23Z"
        storeStatus: "Order_Complete"
        normalizedStatus: COMPLETED
        locationId: "dinosaur_colorado"
        shippingMethod: "express"
        orderUrl: "https://myStore.com/orders/123"
        isTestOrder: false
        createdByRecurringPayment: false
        acceptsMarketing: true
        customerLocale: "EN_US"
        salesChannel: "web_store"
        currency: "USD"
        finalAmount: 100.01
        shippingAmount: 25.25
        discountsAmount: 12.25
        paymentMethod: "credit_card"

        billingAddress: {
          firstName: "Jane"        
					lastName: "Doe"
          address1: "1 N. Deerborn St."
          address2: "Unit #5"
          address3: "Door #3"
          city: "Chicago"
          province: "IL"
          country: "US"
          postal: "60601"
          phone: "6005550125"
          company: "ActiveCampaign"
          email:  "spatulas@activecampaign.com"
        }
        shippingAddress: {
          firstName: "Jane"        
					lastName: "Doe"
          address1: "1 N. Deerborn St."
          address2: "Unit #5"
          address3: "Door #3"
          city: "Chicago"
          province: "IL"
          country: "US"
          postal: "60601"
          phone: "6005550125"
          company: "ActiveCampaign"
          email:  "spatulas@activecampaign.com"
        }
        lineItems: [
          {
            name: "SuperSpatula"
            quantity: 500
            priceAmount: 12.20
            productStorePrimaryId: "SUUUUPER"
            storeBaseProductId: "BaseyBase"
          }
        ]
        customerData: {
          firstName: "Jane"
          lastName: "Doe"
          phone: "6005550125"
          company: "ActiveCampaign"
          smsConsentUpdatedDate: "2041-11-16T10:48:23Z"
          smsMarketingState: UNSUBSCRIBED
          smsOptInLevel: UNKNOWN
        }
        discounts: [
          {
             name: "Shipping Promo"
             type: SHIPPING
             discountAmount: 12.25
          }
        ]
        notes: [
          "Order was delayed for customer"
          "Customer complaint received"
        ]
      }
    ]
    # More Orders may be inserted here.
  ) {
    recordId
  }
}

```

#### Input fields for `bulkUpsertOrdersAsync`

`orders` (`[[OrderInput](https://developers.activecampaign.com/reference/orders-1#order-object)](https://developers.activecampaign.com/reference/orders-1#order-object)`)

#### Return fields for `bulkUpsertOrdersAsync`

[BulkAsyncResponse](https://developers.activecampaign.com/reference/shared-objects#bulkasync-response)

# Objects

### Order Object

`Order` and `OrderInput` objects have nearly the same fields. However, in GraphQL, input and return objects must be of different types, so in the GraphQL schema, they have the types `Order` and `Order Input`.

The only difference between `Order` and `OrderInput` models is that customerData only exists on `OrderInput`.

| Name                                                                                                  | Description                                                                                                                                                                                                                                                          | Equivalent v3 DeepData Order Field         |
| :---------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------- |
| storeOrderId (`String`) **Required**                                                                  | Id of order in external service. Within a connection, this serves as the primary identifier of this order record.                                                                                                                                                    | externalid                                 |
| legacyConnectionId  (`Int!`)  **Required**                                                            | Integer connection identifier matching the v3 API DeepData Connection ID.                                                                                                                                                                                            | connectionId                               |
| lineItems ([LineItem](https://developers.activecampaign.com/reference/orders-1#line-item-object) \[]) | The line items of the order.                                                                                                                                                                                                                                         | orderProducts                              |
| orderNumber (`String`)                                                                                | Order number for the order. Order numbers are defined by the store and are generally human readable, as opposed to `storeOrderId`, which often is not human readable. Some stores do not have an order number. In this case, set this equal to `storeOrderId`.       | orderNumber                                |
| cartId (`String`)                                                                                     | Id of cart associated with the order.                                                                                                                                                                                                                                | externalcheckoutid                         |
| storeExternalOrderId (`String`)                                                                       | An order ID listed as external by the store. This means that the store has imported this order ID from another place.                                                                                                                                                |                                            |
| creationSource (`Enum`)                                                                               | Source of the creation. HISTORICAL for historical sync. REAL\_TIME for real-time or webhook orders. Historical orders will not trigger automations.                                                                                                                  | source                                     |
| email (`String`)                                                                                      | The email address associated with the order.                                                                                                                                                                                                                         | email                                      |
| storeCustomerId (`String`)                                                                            | Primary identifier in the store for this customer                                                                                                                                                                                                                    |                                            |
| shippingAddress (`Address`)                                                                           | The order's shipping address.                                                                                                                                                                                                                                        |                                            |
| billingAddress (`Address`)                                                                            | The order's billing address.                                                                                                                                                                                                                                         |                                            |
| storeCreatedDate (`String`) **Required**                                                              | Date order was created in the store.                                                                                                                                                                                                                                 | externalCreatedDate                        |
| storeModifiedDate (`String`)                                                                          | Date order was last modified in the store.                                                                                                                                                                                                                           |                                            |
| storeStatus (`String`)                                                                                | Status of the order, as noted in the store. This field can be any valid string, but for data integrity, each store status should map to a single, predefined status in ActiveCampaign in the field `normalizedStatus`.                                               |                                            |
| normalizedStatus (`ActiveCampaignOrderState`)                                                         | Normalized Status of the order in ActiveCampaign. Unlike `storeStatus`, this is a predefined list of statuses managed by ActiveCampaign. Must be one of: `PENDING, COMPLETED, ABANDONED, RECOVERED, WAITING, CANCELLED, REFUNDED, FAILED, RETURNED, PENDING_PAYMENT` | state                                      |
| notes (`String[]`)                                                                                    | Notes related to the order.                                                                                                                                                                                                                                          |                                            |
| discounts ([Discount](https://developers.activecampaign.com/reference/orders-1#discount) )            | Discounts that have been applied to this order.                                                                                                                                                                                                                      | orderDiscounts                             |
| locationId (`String`)                                                                                 | The location id of the order.                                                                                                                                                                                                                                        |                                            |
| shippingMethod (`String`)                                                                             | The shipping method of the order.                                                                                                                                                                                                                                    | shippingMethod                             |
| orderUrl (`String`)                                                                                   | The order URL.                                                                                                                                                                                                                                                       | orderUrl                                   |
| isTestOrder (`Boolean`)                                                                               | Is the order a test order?                                                                                                                                                                                                                                           |                                            |
| createdByRecurringPayment(`Boolean`)                                                                  | Whether or not this order was created by a Recurring Payment.                                                                                                                                                                                                        |                                            |
| acceptsMarketing (`Boolean`)                                                                          | Did the customer accept marketing?                                                                                                                                                                                                                                   |                                            |
| customerLocale (`String`)                                                                             | Locale code that the customer uses in the store, for example, EN\_US.                                                                                                                                                                                                |                                            |
| salesChannel (`String`)                                                                               | The order's sales channel.                                                                                                                                                                                                                                           |                                            |
| currency (`String`)                                                                                   | The order's currency.                                                                                                                                                                                                                                                | currency                                   |
| shippingAmount                                                                                        | The shipping amount paid for this order                                                                                                                                                                                                                              | shippingAmount (stored in number of cents) |
| finalAmount (`BigDecimal`) **Required**                                                               | The final amount paid for this order, including tax and shipping.                                                                                                                                                                                                    | totalPrice (stored in number of cents)     |
| discountAmount (`BigDecimal`)                                                                         | The discount amount of the order.                                                                                                                                                                                                                                    | discountAmount (stored in number of cents) |
| customerData ([CustomerData](https://developers.activecampaign.com/reference/orders-1#customerdata) ) | An object that represents fields on an order that are not saved into the Custom Object order but rather directly saved into the ecommerce contact and customer.                                                                                                      |                                            |

### Line Item Object

| Name                                       | Description                                                                                                                                                                                                                                | Equivalent field in v3 DeepData Order Product               |
| :----------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| legacyConnectionId  (`Int!`)  **Required** | Integer connection identifier matching the v3 API DeepData Connection ID.                                                                                                                                                                  |                                                             |
| storeLineItemId (String)                   | String identifier from the store that uniquely identifies the line item.                                                                                                                                                                   |                                                             |
| productStorePrimaryId (String)             | Primary identifier for this product within a store. For stores with variants, the `productStorePrimaryId`is generally a unique identifier on the variant. This will match `storePrimaryId` on the ActiveCampaign Product object.           | externalid (only if GraphQL  storeBaseProductId is not set) |
| storeBaseProductId (String)                | The store's primary unique identifier for the base/parent product. Matches `storeBaseProductId` on the ActiveCampaign Product object.                                                                                                      | externalid                                                  |
| productUrl (String)                        | URL in the store of the detail page for the product of this line item.                                                                                                                                                                     | productUrl                                                  |
| normalizedOrderStatus (Enum)               | ActiveCampaign defined status of the order for this line item (matches normalizedStatus in the Order object). Must be one of:  `PENDING, COMPLETED, ABANDONED, RECOVERED, WAITING, CANCELLED, REFUNDED, FAILED, RETURNED, PENDING_PAYMENT` |                                                             |
| category (String)                          | The category or collection this Line Item is in within the store.                                                                                                                                                                          | category                                                    |
| name: (String)                             | Name of the line item.                                                                                                                                                                                                                     | name                                                        |
| quantity (Int)                             | Quantity of this line item purchased in this order.                                                                                                                                                                                        | quantity                                                    |
| sku: (String)                              | Stock Keeping Unit (SKU) of product for this line item.                                                                                                                                                                                    | sku                                                         |
| imageUrl (String)                          | URL of one image for the product for this line item.                                                                                                                                                                                       | imageUrl                                                    |
| priceAmount (BigDecimal)                   | Decimal currency amount of the total cost of this line item (not the per-item cost).                                                                                                                                                       | price (stored in number of cents)                           |
| lineItemType (String)                      | Type of the product for this line item, for example a digital or physical product.                                                                                                                                                         |                                                             |
| fulfillmentStatus (String)                 | The fulfillment status of this line item.                                                                                                                                                                                                  |                                                             |
| isOnSale (Boolean)                         | Was this line item was purchased while on sale?                                                                                                                                                                                            | onSale                                                      |
| averageRating (BigDecimal)                 | The average customer rating of the product for this line item.                                                                                                                                                                             | averageRating                                               |
| brand (String)                             | The brand (also sometimes called vendor) of the product for this line item.                                                                                                                                                                | brand                                                       |
| tags: (String\[])                          | A list of all tags of the product for this line item.                                                                                                                                                                                      | tags                                                        |

## Discount

| Name                          | Description                                                          |
| :---------------------------- | :------------------------------------------------------------------- |
| name (`String`)               | Name or discount code of the discount                                |
| type (`Enum`)                 | Type of the discount. Must be one of: ORDER, SHIPPING                |
| discountAmount (`BigDecimal`) | Decimal amount of currency representing how much the discount is for |

## CustomerData

| Name                             | Description                                                                                                        |
| :------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| firstName (`String`)             | First name of customer. If set, this will be used in updating the first name of the contact in ActiveCampaign.     |
| lastName (`String`)              | Last name of customer. If set, this will be used in updating the last name of the contact in ActiveCampaign.       |
| phone (`String`)                 | Phone number of customer. If set, this will be used in updating the phone number of the contact in ActiveCampaign. |
| company (`String`)               | Company of customer. If set, this will be used in updating the orgname of the contact in ActiveCampaign.           |
| smsMarketingState (`Enum`)       | Sms Marketing State of customer. Must be one of: `NOT_SUBSCRIBED, PENDING, REDACTED, SUBSCRIBED, UNSUBSCRIBED`     |
| smsOptInLevel (`Enum`)           | Opt in level for SMS marketing. Must be one of: `CONFIRMED_OPT_IN    SINGLE_OPT_IN UNKNOWN`                        |
| smsConsentUpdatedDate (`String`) | Date when the SMS consent was last updated. Must be in format 2019-11-16T10:48:23Z                                 |