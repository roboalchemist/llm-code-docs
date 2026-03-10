# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/integrating-with-cash-app-pay/api-integration-quickstart.mdx

# API Integration Quickstart

We recommend that partners use the [Pay Kit SDK](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/pay-kit-benefits) to integrate with Cash App Pay.

<Note Title="Prerequisites">
  Before getting started, confirm with the Cash App Pay Partner Engineering team that the API-only approach is right for you. Make sure that you have access to:

  * API credentials and API access
  * Cash App Sandbox App

  We recommend reading the following pages:

  * [Cash App Pay Integration Basics](/cash-app-pay-partner-api/guides/technical-guides/cash-app-pay-integration-basics)
  * [Making Requests](/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/making-requests)
  * [Sandbox App](/cash-app-pay-partner-api/guides/technical-guides/sandbox/sandbox-app)
</Note>

## Integrate with the Cash App Pay API

### Step 1: Create a Brand and Merchant

First, create a Brand and associate a Merchant with that brand.

1. Create a [Brand](/cash-app-pay-partner-api/api-reference/network-api/create-brand)
   ```curl
   curl --location 'https://sandbox.api.cash.app/network/v1/brands' \
   --header 'Authorization: {{api_creds}}' \
   --header 'Content-Type: application/json' \
   --header 'Accept: application/json' \
   --header 'X-Region: PDX' \
   --data '{
     "brand": {
          "name": "Cash App",
          "reference_id": "external-id"
     },
     "idempotency_key": "224841f7-31be-4bc6-b1df-e102a8fa476f"
   }'
   ```

2. Create a [Merchant](/cash-app-pay-partner-api/api-reference/network-api/create-merchant)

   ```curl
   curl --location 'https://sandbox.api.cash.app/network/v1/merchants' \
   --header 'Authorization: {{api_creds}}' \
   --header 'Content-Type: application/json' \
   --header 'Accept: application/json' \
   --header 'X-Region: PDX' \
   --data '{
        "merchant": {
            "address": {
                  "address_line_1": "1 Market Street",
                  "locality": "San Francisco",
                  "country": "US",
                  "postal_code": "94105",
                  "administrative_district_level_1": "CA"
             },
             "name": "Cash App Pay on Market Street",
             "brand_id": "BRAND_bifwxjq70mfk06l9nr6q4q1f9",
             "country": "US",
            "currency": "USD",
             "category": "5500",
             "reference_id": "external-id"
        },
       "idempotency_key": "b12fa940-d07a-48c6-a08a-89511547661f"
    }'
   ```

<Note>
  These APIs are server-side between your website or application and Cash App Pay.
</Note>

### Step 2: Link a Customer to the Merchant, Brand, or Client

To link a Customer to the Merchant, Brand, or Client, do the following:

1. Create a customer request with one Channel and at least one Action.

   | Available Actions                                          | Available Channels                    |
   | ---------------------------------------------------------- | ------------------------------------- |
   | One Time Payment <br /> On File Payment <br />Link Account | IN\_APP <br />ONLINE <br /> IN PERSON |

   <Note>
     See the list of supported actions and channels [here](/cash-app-pay-partner-api/api-reference/customer-request-api/create-request). You can have many actions but only one channel.
   </Note>

2. Save the Request ID and the URL from the `auth_flow_triggers` object in the response.
   <Note>
     When you call `create customer request`, a customer request is returned to you with `auth_flow_triggers` populated. This gives you access to URLs including the QR Code URL, Mobile URL, and Desktop URL.
   </Note>

3. Listen for updates to the customer request.

4. When the request enters the `approved` state, stop polling.

5. Save the Grant IDs listed in the `grants` array to [create a payment](#step-3-create-a-payment) later.

   <Note>
     To test the customer request, you can use the Sandbox App or Sandbox Web to scan and approve the request. See more at [Sandbox App](/cash-app-pay-partner-api/guides/technical-guides/sandbox/sandbox-app) and [Developer Sandbox](/cash-app-pay-partner-api/guides/technical-guides/sandbox/developer-sandbox).
   </Note>

#### Listen for updates to the customer request

You can listen for updates to the customer request in two ways:

* **Polling (recommended):** Call [retrieve customer request](/cash-app-pay-partner-api/api-reference/customer-request-api/retrieve-request) repeatedly (ideally once per second or more frequently).
* **Webhooks:** Subscribe to the `customer_request.state.updated` event.

QR codes rotate every 30 seconds and expire every 60 seconds, so you must get the latest QR code. This will change based on how you listen for customer request updates:

* If you are using polling, set the image tag’s URL to the latest QR code that is returned after each polling response. Since you poll more frequently than QR codes rotate, you don’t need to keep track of the `refreshes_at` value.
* If using webhook, there is no webhook event for QR code rotation. Instead, you should fetch the latest customer request once the current timestamp is after the `refreshes_at` value. The auth flow triggers will contain the newest, valid QR code.

<Note>
  These APIs are client-side from the browser to Cash App.
</Note>

**Example - Create Customer Request**

```curl
curl --location 'https://sandbox.api.cash.app/customer-request/v1/requests' \
--header 'Authorization: Client {{client ID}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
    "request": {
         "actions": [
              {
                   "amount": 1234,
                   "currency": "USD",
                   "scope_id": "{{client_id || brand_id || merchant_id}}",
                   "type": "ONE_TIME_PAYMENT"


              }
         ],
         "reference_id": "external-id",
         "channel": "ONLINE"
    },
    "idempotency_key": "cd8b0b0a-0ffb-478e-ae8f-e31aef666a1a"
}'
```

**Example - Retrieve Customer Request**

```curl
curl --location --globoff 'https://sandbox.api.cash.app/customer-request/v1/requests/{{customer_request_id}}' \
--header 'Authorization: Client {{client_id}}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json'
```

### Step 3: Create a Payment

You can now create a payment using the Grant ID and Merchant ID from the previous steps using the [Create a payment request](/cash-app-pay-partner-api/api-reference/network-api/create-payment) endpoint. You can use void, capture, or refund actions depending on the state of the payment.

<Note>
  We use magic values in the amount field to determine outcomes for payments in the sandbox environment.  You can use any amount, but [these amounts](/cash-app-pay-partner-api/guides/technical-guides/sandbox/developer-sandbox#magic-values) will result in specific outcomes.
</Note>

**Example - Create Payment**

```curl
curl --location 'https://sandbox.api.cash.app/network/v1/payments' \
--header 'Authorization: {{api_creds}}' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-Region: PDX' \
--data '{
    "payment": {
         "capture": true,
         "amount": 1234,
         "currency": "USD",
         "merchant_id": "{{merchant_id}}",
         "grant_id": "{{grant_id}}",
         "reference_id": "external-id"
    },
    "idempotency_key": "2a77b3a5-9104-4587-9517-53ac5d968f25"
}'
```

## Notes

### Pay Kit SDK

Pay Kit is the name of the Cash App Pay SDK.  This SDK specifically handles linking a Customer to a Merchant and uses the [Customer Request API](../../reference/Customer-Request-API.v1.yaml) underneath.  Instead of using the SDK, you can call the APIs directly as described in the steps to integrate with the Cash App Pay API above. To know more about our SDK, see [Pay Kit](/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-web-overview/getting-started).

### Signatures

Cash App Pay Network API and Management API require that all requests be signed.  However, when using Sandbox, you can skip this by setting `x-signature` to the value `sandbox:skip-signature-check`. Use these [Magic Values](/cash-app-pay-partner-api/guides/technical-guides/sandbox/developer-sandbox#magic-values) to control the behavior in Sandbox and to produce preset outcomes.
