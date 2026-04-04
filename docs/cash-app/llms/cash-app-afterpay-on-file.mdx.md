# Source: https://developers.cash.app/cash-app-afterpay/guides/api-development/additional-features/cash-app-afterpay-on-file.mdx

***

## stoplight-id: 1u97rqm6w3jhj

# Cash App Afterpay On File

Cash App Afterpay On File allows customers to save Cash App Afterpay as a payment method on your website. Similar to storing a credit card on file, this simplifies future transactions and supports recurring payments like subscriptions.

Benefits include:

* **Payment flexibility:** You can offer both one-time and recurring purchases to your customers using Cash App Afterpay.
* **Faster checkout:** Once a customer links their Cash App Afterpay account, they’re not required to input their Cash App Afterpay account details for future Cash App Afterpay purchases. This reduces friction – which is especially important for mobile transactions and frequent purchases.
* **Improved conversion and retention:** A simpler repeat purchase experience encourages customers to return, boosts conversion rates, and increases customer lifetime value.

Supported use cases:

* **Customer-initiated transaction (CIT):** A payment initiated by the customer using their saved Cash App Afterpay account details, while the customer is present on your website.
  * Example: any one-off customer-initiated purchase on your website
* **Merchant-initiated transaction (MIT):** A payment initiated by the merchant, while the customer is not present on your website. These payments can be fixed or variable amounts.
  * Example: regular and ongoing subscriptions and memberships.

When a customer saves Cash App Afterpay as a payment method, a grant is created. A grant is a payment token associated with a specific customer that merchants can use to initiate future payments. After any on file payments are processed, the customer receives a Cash App Afterpay order confirmation email, regardless of whether the payment is customer-initiated or merchant-initiated.

<Info title="Important">
  On file payment functionality is available only in Australia, New Zealand, and the United States. It's supported only on API v2.

  You must be assessed and approved by Cash App Afterpay before you can make Cash App Afterpay On FFile available to your customers. Reach out to your Cash App Afterpay account manager for more information.
</Info>

## Set up Cash App Afterpay On File

There are two ways to implement Cash App Afterpay On File: customers can save their Cash App Afterpay details in a virtual wallet outside the checkout flow, or they can save their Cash App Afterpay details during the checkout process itself.

### Add Cash App Afterpay to a virtual wallet

Create a Cash App Afterpay grant outside of a checkout flow, in a virtual wallet for your store.

#### Step 1: Start the approval process

Call the Create Grant Approval endpoint [(/v2/grants/approvals)](/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/start-grant-approval). This provides Cash App Afterpay with customer information, grant information, and the URL to direct the customer to when they complete the Cash App Afterpay approval flow.

**Request**

```json
{
    "consumer": {
        "phoneNumber": "3526669673",
        "givenNames": "John",
        "surname": "Doe",
        "email": "{{email}}"
    },
    "merchant": {
        "redirectConfirmUrl": "https://www.afterpay-merchant.com/confirm",
        "redirectCancelUrl": "https://www.afterpay-merchant.com/cancel"
    },
    "grants": [
        {
            "type": "ON_FILE",
            "merchantReference": "merchant-internal-ref"
        }
    ]
}
```

**Response**

```json
{
    "token": "001.euuugalpi1oj0kr34h9h0a72h6uqgq9ni6kcc6a0frrkpv1h",
    "expires": "2025-07-23T18:39:58.634Z",
    "redirectCheckoutUrl": "https://portal.afterpay.com/us/checkout/?token=001.euuugalpi1oj0kr34h9h0a72h6uqgq9ni6kcc6a0frrkpv1h"
}
```

#### Step 2: Redirect to checkout

Redirect the customer to checkout using the `redirectCheckoutUrl` returned from the Create Grant Approval call. See [Create a Checkout](/cash-app-afterpay/guides/api-development/api-quickstart/create-a-checkout) for instructions on launching a checkout.

#### Step 3: Create on file grant

If the checkout is successful, Cash App Afterpay redirects the customer to the URL you specified in the Create Grant Approval call. Next, create the grant by calling the Create Grant endpoint [(/v2/grants)](/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/create-grant). This call creates a grant and returns a grant ID. Save this ID for your customer’s future transactions.

**Request**

```json
{  
         "requestId": "{{$randomUUID}}",
         "token": "001.euuugalpi1oj0kr34h9h0a72h6uqgq9ni6kcc6a0frrkpv1h"
}
```

**Response**

```json
{
    "grant": {
        "id": "001.nkqn2oag22ehaamdo71gq1il2nnlroo85i5rj6fir8818epm4m64rjf0n0chu6kq",
        "created": "2025-07-23T16:46:55.476Z",
        "type": "ON_FILE",
        "status": "ACTIVE",
        "merchantReference": "merchant-internal-ref"
        "email": "tes***@s***.com",
        "consumerReference": "90b2a80866ed0e7dd7f99305d3bcd8521bfad0a1eb32c63206ff11f04045d5ba"
    }
}
```

<Note>
  Grants can be revoked by the customer or merchant at any time. We recommend subscribing to the [AgreementStatusUpdated](/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/grant-status-updated) webhook.
</Note>

### Save Cash App Afterpay details during checkout

Create a Cash App Afterpay grant during the checkout flow. For example, a customer can purchase a monthly subscription and pay for the first installment.

<Note>
  Create the grant **before** finalizing the purchase. If the purchase is finalized first, the grant can't be created.
</Note>

#### Step 1: Create a checkout

Create a checkout using the Create Checkout endpoint [(/v2/checkouts)](/cash-app-afterpay/api-reference/reference/checkouts/create-checkout-1) using the Grants object with type `ON_FILE`. See [here](/cash-app-afterpay/guides/api-development/api-quickstart/create-a-checkout) for instructions on launching a checkout.

**Request**

```json
{
    "amount": {
        "amount": "15.00",
       "currency" : "{{currency}}"
    },
    "consumer": {
        "phoneNumber": "61450675141",
        "givenNames": "",
        "surname": "",
        "email": "{{email}}"
    },
    "merchant": {
        "redirectConfirmUrl": "https://www.afterpay-merchant.com/confirm",
        "redirectCancelUrl": "https://www.afterpay-merchant.com/cancel"
    },
    "merchantReference": "merchantOrder-1234",
    "grants": [
        {
        "type": "ON_FILE",
        "merchantReference": "merchant-grant-internal-ref"
        }
    ]
}
```

**Response**

```json
{
    "token": "001.euuugalpi1oj0kr34h9h0a72h6uqgq9ni6kcc6a0frrkpv1h",
    "expires": "2025-07-23T18:39:58.634Z",
    "redirectCheckoutUrl": "https://portal.afterpay.com/us/checkout/?token=001.euuugalpi1oj0kr34h9h0a72h6uqgq9ni6kcc6a0frrkpv1h"
}
```

#### Step 2: Create and store the on file grant

If the checkout is successful, Cash App Afterpay redirects the customer to the URL you specified in the Create Checkout call. Next, create the grant by calling the Create Grant endpoint [(/v2/grants)](/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/create-grant). This endpoint creates a grant and returns a grant ID. Save this ID for your customer’s future transactions.

**Request**

```json
{  
         "requestId": "{{$randomUUID}}",
         "token": "001.euuugalpi1oj0kr34h9h0a72h6uqgq9ni6kcc6a0frrkpv1h"
}
```

**Response**

```json
{
    "grant": {
        "id": "001.nkqn2oag22ehaamdo71gq1il2nnlroo85i5rj6fir8818epm4m64rjf0n0chu6kq",
        "created": "2025-07-23T16:46:55.476Z",
        "type": "ON_FILE",
        "status": "ACTIVE",
        "merchantReference": "merchant-grant-internal-ref"
        "email": "tes***@s***.com",
        "consumerReference": "90b2a80866ed0e7dd7f99305d3bcd8521bfad0a1eb32c63206ff11f04045d5ba"
    }
}
```

#### Step 3: Capture payment

Now that you have a successful checkout pre-approval and an on file grant, choose when you want to capture the payment. You can either capture immediately or authorize and capture at a later time (authorizations last for 13 days before automatically expiring).

* **Immediate capture:** Call the Capture Full Payment endpoint [(/v2/payments/capture)](/cash-app-afterpay/api-reference/reference/payments/capture-full-payment), following the instructions [here](/cash-app-afterpay/guides/api-development/api-quickstart/immediate-capture).
* **Deferred capture:** Call the Auth endpoint [(/v2/payments/auth)](/cash-app-afterpay/api-reference/reference/payments/auth), following the instructions [here](/cash-app-afterpay/guides/api-development/api-quickstart/deferred-capture).

**Request**

```json
{
  "requestid": "d22f5305-05f3-48a0-9131-a4e6e5f58b9a",
  "token": "001.euuugalpi1oj0kr34h9h0a72h6uqgq9ni6kcc6a0frrkpv1h",
  "merchantReference": "merchant-order-123"
}
```

**Response**

```json
{
  "id": "300000016189",
  "token": "001.euuugalpi1oj0kr34h9h0a72h6uqgq9ni6kcc6a0frrkpv1h",
  "status": "APPROVED",
  "created": "2024-03-11T20:11:42.487Z",
  "originalAmount": {
    "amount": "37.00",
    "currency": "USD"
  },
  "openToCaptureAmount": {
    "amount": "0.00",
    "currency": "USD"
  },
  "paymentState": "AUTH_APPROVED",
  "merchantReference": "updated-k6-reference-utaddnpx",
  "refunds": [],
  "orderDetails": {
    "consumer": {},
    "billing": {
      "name": "Joe Customer",
      "line1": "1004 New Avenue",
      "postcode": "94121",
      "countrycode": "US",
      "phoneNumber": "2120000000"
    },
    "shipping": {
      "name": "Joe Customer",
      "line1": "1004 New Avenue",
      "postcode": "94121",
      "countrycode": "US",
      "phoneNumber": "2120000000"
    },
    "courier": {
      "shippedAt": "2024-01-01T08:00:00Z",
      "name": "FedEx",
      "tracking": "000 000 000 000",
      "priority": "STANDARD"
    },
    "items": {
      "name": "Blue Carabiner",
      "sku": "12341234",
      "quantity": 1,
      "price": {
        "amount": "40.00",
        "currency": "USD"
      }
    },
    "categories": {
      "name": "Jeans",
      "sku": "123412345",
      "quantity": 1,
      "price": {
        "amount": "20.00",
        "currency": "USD"
      },
      "categories": null
    }
  },
  "discounts": [],
  "shippingAmount": {
    "amount": "10.00",
    "currency": "USD"
  },
  "taxAmount": {
    "amount": "0.00",
    "currency": "USD"
  },
  "events": {
    "id": "2dYbLXpOtEPQbg1DT7x9D8R4oCY",
    "created": "2024-03-11T20:11:43.897Z",
    "expires": null,
    "type": "CAPTURED",
    "amount": {
      "amount": "37.00",
      "currency": "USD"
    },
    "paymentEventMerchantReference": "k6-gsrdqspusf"
  }
}
```

## Create an on file payment

Once a grant is created, you can use the grant ID to place additional Cash App Afterpay orders.

To create an order with the grant, call the Orders API [(/v2/orders)](/cash-app-afterpay/api-reference/reference/orders/create-grant) and include the stored grant ID in the request.

Cash App Afterpay checks the customer’s eligibility at order creation, so we recommend making this call at the beginning of your checkout process if Cash App Afterpay is the selected payment method. If the order amount changes before the on file payment is created, create a new order with the updated amount; the original order is automatically deleted by Cash App Afterpay.

Once you've successfully created an order, use the token from the response to call either the Auth endpoint [(/v2/payments/auth)](/cash-app-afterpay/api-reference/reference/payments/auth) or the Capture Full Payment endpoint [(/v2/payments/capture)](/cash-app-afterpay/api-reference/reference/payments/capture-full-payment).

<Note>
  On file payments require extra metadata, such as payment initiation actor and subscription details, to ensure compliant usage and improve underwriting decisions. Required fields may include:

  * enrichments.initiation.actor (required)
  * enrichments.subscription.type (required if subscription)
  * enrichments.subscription.interval (required if subscription)
  * enrichments.subscription.intervalCount (required if subscription)
</Note>

**Request**

```json
{  
         "requestId": "{{$randomUUID}}",
         "grantId": "001.nkqn2oag22ehaamdo71gq1il2nnlroo85i5rj6fir8818epm4m64rjf0n0chu6kq",
         "amount": {
            "amount": "125.00",
            "currency": "USD"
        },
        "enrichments": {
            "initiation": {
                "actor": "CUSTOMER"
            }
        }
}
```

**Response**

```json
{
    "token": "001.1hrgccv8a6th0pklh7mqranu58tb1lllau9fhngl77i44rtk",
    "expires": "2025-07-23T19:28:06.880Z"
}
```

## Manage existing grants

Once a grant has been created, you can use it to initiate new on file payments or retrieve the grant details using the Retrieve Grant endpoint [(/v2/grants/\{grantId})](/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/get-grant).

If a customer decides to remove Cash App Afterpay as a saved payment method on your website, use the Revoke Grant endpoint [(/v2/grants/\{grantId}/revoke)](/cash-app-afterpay/api-reference/reference/grants-cash-app-afterpay/revoke-grant) so that the grant ID can be deactivated by Cash App Afterpay.

**Response**

```json
{
    "grant": {
        "id": "001.nkqn2oag22ehaamdo71gq1il2nnlroo85i5rj6fir8818epm4m64rjf0n0chu6kq",
        "created": "2025-07-23T16:46:55.476Z",
        "type": "ON_FILE",
        "status": "CANCELLED",
        "merchantReference": "merchant-internal-ref"
        "cancelled": "2025-07-23T18:15:09.316Z",
        "email": "tes***@s***.com",
        "consumerReference": "90b2a80866ed0e7dd7f99305d3bcd8521bfad0a1eb32c63206ff11f04045d5ba"
    }
}
```

Customers can also revoke a grant within the Cash App Afterpay app. Merchants should subscribe to the [GrantStatusUpdated](/cash-app-afterpay/api-reference/reference/grants-cash-app-pay/schemas/grant-status-updated) webhook.

```json
{
  "type": "on_file_grant.status.updated",
  "eventId": "87f5ded7-2747-4e31-95ee-8993e0ae8663",
  "createdAt": "2025-08-22T19:34:37.497Z",
  "data": {
    "id": "001.nkqn2oag22ehaamdo71gq1il2nnlroo85i5rj6fir8818epm4m64rjf0n0chu6kq",
    "type": "ON_FILE_GRANT",
    "object": {
      "grant": {
        "id": "001.nkqn2oag22ehaamdo71gq1il2nnlroo85i5rj6fir8818epm4m64rjf0n0chu6kq",
        "created": "2025-07-23T16:46:55.476Z",
        "type": "ON_FILE",
        "status": "CANCELLED",
        "cancelled": "2025-08-22T19:34:35.012Z"
      }
    }
  }
}
```

<Note>
  Merchants can use the `consumerReference` field associated with a grant ID to map to their own customer identifier. The email field, which is masked, can be used as a customer-facing identifier.
</Note>

## Considerations

1. Customers should be able to revoke grants (unlink Cash App Afterpay as a saved payment method) on your website. Customers should also be notified of any price change to a subscription at least 30 days in advance, or in adherence to any applicable laws and legal requirements.
2. Merchants are strongly encouraged to implement Cash App Afterpay's [checkout widget](/cash-app-afterpay/guides/api-development/additional-features/checkout-widget#with-on-file-grant) for grants, as it allows merchants to show the required disclosures and payment schedule details on their checkout page prior to customers finalizing their purchases.
