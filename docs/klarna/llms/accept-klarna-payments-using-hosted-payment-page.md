# Source: https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/integrate-via-hpp/before-you-start/accept-klarna-payments-using-hosted-payment-page.md

# Accept Klarna Payments

This guide will lead you through all the steps required to accept payments with **Klarna Payments**using the **Hosted Payment Page**. At the end you will be able to accept payments with Klarna without hosting any web component on your own pages.

## Ecosystem


![klarna docs image](3bbb7172-2c66-4564-b202-629ae50c7c3f_HPP+for+KP.jpeg)image

## Sequence diagrams

You will find here the usual integration flow of the Hosted Payment Page using a Klarna Payments session. In this flow, actors are defined as follow:

- **Consumer**: a physical person that wants to buy something.
- **Browser**: the browser that the **Consumer** is able to control, for example on a desktop or a mobile.
- **Merchant Backend**: your backend that will do the API calls to HPP, KP and Order Management.
- **HPP**: the Hosted Payment Page API
- **Klarna Payments**: the Klarna Payments API

### Sequence where you host a part of the Consumer flow

{{#mermaid:
sequenceDiagram
autonumber
participant A as Consumer
participant B as Browser
participant C as Merchant Backend
participant D as HPP
participant E as Klarna Payments
A -->> C: Intent of buying. May be given on website, by phone call, etc
C ->> E: Create session
E -->>C: session
C ->>D: Create session
D ->>C: URL to redirect to
alt Synchronous flow
C -->>B: Redirection to redirect_url
else Asynchronous flow
C -> D: Distribute session, method
D -->>A: SMS or e-mail containing an url
A ->>B: Reads and click
end
B ->>D: Request url
D -->>B: HPP with Merchant's customization
note over A,E: Consumer will be able to see basic order details, choose payment methos if none is enforced. If he is a Klarna user,<br/> he will be able to pay in a few click and benefit from our Smoooth experience.
B ->>D: Presses pay button
D -->>B: Redirection to merchant_urls.success with authorization_token or order_id
B ->>C: Requires success
alt Custom place order
note over A,E: When place_order_mode is not defined, you get an authorization_token and need to place the order. The token has a limited lifespan (usually 1 hour)
C ->>E: Place order with authorization_token
end
C -->>B: Order confirmation
}}

1.  **Your consumer wants to proceed to a payment** using one of Klarna’s payment methods: depending on the integration, this interaction can be on a website when the Consumer choose to pay with Klarna, with a telesales by phone…
2.  **Create sessions on Klarna Payments and Hosted Payment Page**

a\. **Create a Payment session on Klarna Payments**: After receiving this consumer intent, create a Payment session with Klarna Payments API. b. **Associate the Payment session to an Hosted Page session**: Using the session identifier provided by Klarna Payments API, create the corresponding HPP session.

1.  **Distribution of the Payment session to your consumer**
    - a\. **Distribution can be done by yourself**, using a redirection URL given by HPP.
    - b\. **Request that HPP distribute** the Payment session directly to your Consumer.
2.  *\[Invisible step for you\]* **Consumer gets to Hosted Payment Page**: Consumer goes to the Payment page using the received link, either by you or by SMS/Email received from Klarna.
3.  *\[Invisible step for you\]* **Authorization of payment**: When the Consumer presses the buy button on the Payment page, payment authorization will be given to the Consumer. HPP will proceed to the redirection of the Consumer to your Backend using the URL given in the session creation.
4.  **Confirmation and Authorization Token**
    - a\. **Redirection of the Consumer after a successful authorization**: The Consumer’s browser is redirected to the success URL you defined.
    - b\. **Validation of the HPP Session outcome**: Depending on your HPP Session, you will be able to retrieve an authorization_token or an order_id from the URL parameters, but you can also checks the HPP Session status using our endpoint. The authorization_token will let you place the order manually, whereas the order_id will let you do the post-purchase experience.
5.  **Place the order**: By not defining any place_order_mode when creating the HPP Session, you will need to place an order using the Authorization Token you just got. This will let you check that everything is still correct before validating the payment. This returns you an order_id that will let you do the post-purchase experience.
6.  **Confirmation of the order**: You should show the customer that the payment authorization is successful and that the order has been validated.
7.  *\[This step can be asynchronous\]* **Capture payment**: When you want the payment to actually happen, usually when goods are shipped, use the Order Management API to capture the amount on the order. When creating the KP Session, you can also ask the capture to be automatic.

### Success flow

After a successful authorization, the Consumer’s browser will be redirected to your success URL defined when you created the HPP session (see Step 3). HPP will use merchant_urls.success to generate the URL, it should contain the authorization_token or order_id depending on your place_order_mode, but can also use some additional parameters. Please see HPP Create Session Parameters and Options for dynamic parameters.

### Rejection and cancellation flows

When the Consumer decides to abort the process or gets rejected by Klarna for payment authorization, the Consumer’s browser is redirected to one of the URLs defined when you created the HPP session (see Step 3).

- merchant_urls.failure: Consumer is redirected there after being refused by Klarna.
- merchant_urls.cancel: Consumer is redirected there after clicking on the Cancel button.

Please see [HPP Create Session Parameters and Options](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/create-session.md) for dynamic parameters.

### Alternative Sequence: no hosting of the Consumer flow

This alternative sequence is almost the same except that you don’t need to host any page that should be shown to the Consumer. As you can’t rely on any redirection to get the status of the session, your backend needs to poll the HPP API to get it. You can decide whether you want to host these pages by yourself or rely on HPP ones by defining the merchant_urls. You can give HPP a success url but not a cancellation one.

{{#mermaid:
sequenceDiagram
autonumber
participant A as Consumer
participant B as Browser
participant C as Merchant Backend
participant D as Klarna Payments
participant E as HPP
A -->> C: Intent of buying. May be given on website, by phone call, in-store etc
C ->> D: Create session
D -->>C: session
C ->>E: Create session
E ->>C: URL to redirect to
C ->>E: Distribute session, method
E -->>A: SMS or e-mail containing an url
A ->>B: Reads and click
B ->>E: Request url
E -->>B: HPP with Merchant's customization
note over A,E: Consumer will be able to see basic order details, choose payment methos if none is enforced. If he is a Klarna user,<br/> he will be able to pay in a few click and benefit from our Smoooth experience.
B ->>E: Presses pay button
note over A,E: When initiated without a value for merchant_urls.success, HPP will render a basic payment confirmation page to the consumer.
E -->>B: Display of payment confirmation page
note over A,E: Your backend should poll the session status until the status is COMPLETE
C ->>E: Get session status
E -->>C: status = COMPLETE with authorization_token or order_id
alt Custom place order
note over A,E: When place_order_mode is not defined, you get an authorization_token and need to place the order. The token has a limited lifespan (usually 1 hour)
C ->>D: Place order with authorization_token
end
}} **6. b. Confirmation and Authorization Token** **Polling to get the successful outcome**: The Consumer’s browser is shown a simple payment confirmation page, your Backend will need to get the Authorization Token using HPP API. that you will need to use to place the order if the order is still valid.

### Success flow

After a successful authorization, the read session endpoint will give you the status of the Session and the Authorization Token to place the order with.

### Rejection and cancellation flows

When the Consumer decides to abort the process or gets rejected by Klarna for payment authorization, the status of the session will also be updated. The Consumer will see a simple cancel or rejection page.

## Step by step integration

### 1. Create KP Session with the Payments API

The first step is to create a **KP Session** with the **Klarna Payment API** in order to be able to host it using the **Hosted Payment Page API**. This is where you are going to define all you know already about your Consumer, what is the content of the order and the metadata associated to the purchase. This call corresponds to **Step 2a**in the sequence diagram.

| **Description** | **Creates a session with KP-API** |
|----|----|
| Reference | For a full list of accepted (optional) parameters, possible returns and error codes you can reference the KP-API documentation |
| Url structure | <https: %7bendpoint%7d="" payments="" sessions="" v1=""> |
| Example | curl -X POST <https:></https:><endpoint>/payments/v1/sessions --header "Authorization: Basic <token> " --header "Content-Type: application/json" --header “Cache-Control: no-cache” --data “<parameters>” |

### Create a session KP: Request

``` json
{
"purchase_country": "us",
"purchase_currency": "usd",
"locale": "en-US",
"order_amount": 20000,
"order_tax_amount": 0,
"order_lines": [
{
"image_url": "https://www.exampleobjects.com/logo.png",
"type": "physical",
"reference": "Could be a Product Id or SKU #",
"name": "Cool Bike",
"quantity": 1,
"unit_price": 20000,
"tax_rate": 0,
"total_amount": 20000,
"total_discount_amount": 0,
"total_tax_amount": 0
}
],
"billing_address": {
"given_name": "John",
"family_name": "Doe",
"email": "email+require_signup@example.com",
"title": "Mr",
"street_address": "2425 Example Rd",
"street_address2": "",
"postal_code": "43221",
"city": "Columbus",
"region": "OH",
"phone": "6145675309",
"country": "US"
}
}
```

### Create a session KP: Response

``` json
{
"session_id" : "<kp_session_id>",
"client_token" : "<jwt>", // Ignore this field when using KP with HPP
"payment_method_categories": [
{
"identifier": "pay_later",
"name": "Pay later.",
"asset_urls": {
"descriptive": "https://x.klarnacdn.net/payment-method/assets/badges/generic/klarna.svg",
"standard": "https://x.klarnacdn.net/payment-method/assets/badges/generic/klarna.svg"
}
}
]
}
```

### How to create the Request

Please read the session creation guide of **Klarna Payments API** to get all details on fields and how you can use them. As you will use the Hosted Payment Page API to host your KP Session, you don’t need to read the step after. As you won’t own and host the page that displays Klarna Payments’ Client, you have to respect additional guidelines that will depend on the use case of your integration see see special rules . Depending on your integration use case (ie *eCommerce*, *In Store*or*Telesales*), you may have to respect some guidelines when creating the KP Session, see \[ special rules\].

#### How to interpret the Response

The KP Session is created on a successful response. On the fields present in it, only the session_id is useful when KP is used with Hosted Payment Page API. You will have to use it to build HPP’s `payment_session_url`. [`https://api.klarna.com/payments/v1/sessions/`](https://api.klarna.com/payments/v1/sessions/)<kp_session_id>

## 2. Create HPP Session with Hosted Payment Page API

The second step is to create the **HPP Session** using the **KP Session** you have just created. Sessions will have a tied lifecycle meaning that the HPP Session will expire 1 hour before the KP Session, see session lifetimes. Multiple HPP Sessions can be linked to the same KP Session if you need to have multiple customization at the same time, although it is considered as a bad practice. This call corresponds to **Step 2b**in the sequence diagram.

### How to create the Request

Please read the [session creation call reference of HPP](https://docs.klarna.com/payments/other-products/hosted-payment-page/api-documentation/create-session.md)**session creation call reference of HPP** to get all details on fields and how you can use them. As you will use the Hosted Payment Page API to host a KP Session, you have additional options that you can use.

#### Specific Klarna Payments parameters when creating an HPP Session

A successful HPP Session can lead to three different outcomes for the KP Session, depending on your use-case and the flexibility needed by your integration upon Customer’s authorization. Use this to speed up your integration and let HPP do the work for you:

- **Authorized Payment** (default): the Consumer selected a payment method and was authorized by Klarna for the order amount of the KP Session. Your service will get an authorization_token back and will need to use it to *Place an Order* with KP API. One of the reason for you to choose this mode is if you want to make additional validation after the consumer was authorized and before actually placing the order (for example, stock management). In some cases, you may use the token to place an order on a lower amount. This could also let you create customer token for recurring payments.
- **Placed Order**: the Consumer selected a payment method, was authorized by Klarna and HPP automatically placed the corresponding order. Your service will get an order_id back, you will then need to *Capture Order* with the Order Management API. Capturing order should happen when goods are sent to the customer. Klarna creates the order even in case of failed redirection to merchant_urls.success. Keep track of the HPP session status using by [polling HPP's read endpoint or via callback mechanism.](https://docs.klarna.com/hosted-payment-page/get-started/tracking-session-status)
- **Captured Order**: the Consumer selected a payment method, was authorized by Klarna and HPP automatically placed the corresponding order and captured it. Your service will get an order_id back, you won’t need any additional call. This option should be used when goods are directly given to the Consumer (Digital goods, In-store…). Klarna creates the order even in case of failed redirection to merchant_urls.success. Keep track of the HPP session status using by [polling HPP's read endpoint or via callback mechanism.](https://docs.klarna.com/hosted-payment-page/get-started/tracking-session-status)

The call corresponding to **Step 7**in the sequence diagram becomes obsolete when using PLACE_ORDER or CAPTURE_ORDER as a values for place_order_mode.

| Key | **place_order_mode** |
|----|----|
| Description | Defines the outcome of the KP Session when the HPP Session is successful. |
| Type | List values from an Enum |
| Default Value | NONE |
| Accepted Values | NONE, PLACE_ORDER, CAPTURE_ORDER |

``` json
{
"options": {
"place_order_mode": "CAPTURE_ORDER"
}
}
```

**Payment Methods and Categories** **NOTE: We're introducing a new customer purchase flow where we handle everything related to the payment widget, so you don't have to worry about it. If you're using the new purchase flow, skip this section. Otherwise, if you still handle the widget, read more about it in this section.** HPP lets you define what *Payment Method Categories* should be made available to the Consumer when seeing the Klarna Payment Widget on HPP. Payment Categories are *Pay Now*, *Pay Later* or *Slice It (Pay over time)*, and will differ depending on what Products are available for you at Klarna. When you create a *KP Session* in **Step 2a**, *Klarna Payments API* sends you back as a result all available payment categories for the *KP Session*. You have to use this values to configure the *HPP Session*. This parameter will define what the Consumer will when first loading the Payment Page.

1.  Display only one Payment Method Category using the field payment_method_category
2.  Display a defined list of Payment Method Categories using the field payment_method_categories
3.  Display all available Payment Method Categories by omitting both parameters

Defining both fields payment_method_category and payment_method_categories at the same time will end up in a refused request.

#### 1. Display only one Payment Method Category

| Key | payment_method_category |
|----|----|
| Description | Consumer will be able to select a Payment Method from a single Category. The value has to be one of the payment categories sent back by KP API when creating the*KP Session*. |
| Type | Enum |
| Accepted Values | PAY_NOW, PAY_LATER, PAY_OVER_TIME, DIRECT_DEBIT, DIRECT_BANK_TRANSFER |

``` json
{
"options": {
"payment_method_category": "pay_later"
}
}
```

#### 2. Display a list of Payment Method Categories

| Key | payment_method_categories |
|----|----|
| Description | Consumer will be able to select a Payment Method from a list of Categories. Values have to be one of the payment categories sent back by KP API when creating the*KP Session*. |
| Type | List values from an Enum |
| Accepted Values | PAY_NOW, PAY_LATER, PAY_OVER_TIME, DIRECT_DEBIT, DIRECT_BANK_TRANSFER |

``` json
{
"options": {
"payment_method_categories": [
"pay_later",
"pay_now"
]
}
}
```

#### 3. Display all available Payment Method Categories

When none of the above parameters are given on the create call, all the available payment categories will be made available to the consumer. When activated, the *Fallback flow* will make sure that the Consumer is declined for all payment categories of the *KP Session* before going through the *Rejection flow*. In combination with the two first initial display options, it is possible to activate a **fallback flow** that will happen only when the Consumer is declined for the payment categories that were defined. This *fallback* works as follow:

1.  The KP Session is created and *Pay Now*, *Pay Later* and *Slice It* are all available
2.  The HPP Session is created with the *Slice It* category because the Consumer’s choice has been made before going to HPP
3.  The Consumer arrives on the Payment Page and sees only *Slice It* options. The Consumer applies for one of the *Slice It* options and for some reason gets declined
4.  The *fallback flow* isn’t activated (default behavior) or has already happened, the Consumer will go through the *Rejection flow*.

The *fallback flow*may be transparent for the Consumer and is not a guarantee of authorization. The Consumer may be declined for additional payment method categories while applying for one.

| Key | payment_fallback |
|----|----|
| Description | When true, the *Fallback flow*will make sure that the Consumer is declined for all payment categories of the *KP Session*before going through the*Rejection flow*. |
| Type | Boolean |
| Accepted Values | true, false |

``` json
{
"options": {
"payment_method_categories": [
"pay_later",
"pay_now"
]
}
}
```

#### 3. Distribute Session with HPP (Optional)

Outside of typical eCommerce flow, you will need to distribute the link to the Hosted Payment Page to the Consumer, for example by email or SMS, or by QR code. The Consumer will then be able to access the page and complete the payment. This call corresponds to **Step 3b**in the sequence diagram.

### 4. Retrieve the result of the HPP Session

Once the Consumer has completed the flow on HPP, the status of the HPP Session will change to reflect the outcome of their actions. Your system will then need to retrieve this outcome to be able to act on it, either by placing an order on Klarna Payment, creating a consumer token, or just storing the order_id that was created by HPP for post-purchase purposes. The outcome of the HPP Session can be retrieved either via the redirection of the Consumer to your own website or by making an API Call to get the status of the session.

#### 4. a. From the Consumer redirection

You can get the outcome of the KP Session from the link that the Consumer will be redirected to as stated in our redirection guide. It is still advised to make a call to the HPP API to get the exact state of the HPP Session and not rely only on the consumer redirection. Parameters that will be required to handle the outcome are given to you by replacing the place holders you have set up in the merchant_urls.success at the creation of the HPP Session. You just need to extract the values from there. This call corresponds to **Step 6a**in the sequence diagram. It is advised to use both method to make sure that your system is actually placing the order whenever the Consumer has gotten a confirmation of payment by Klarna.

- On create call: [`https://example.com/success?sid=`](https://example.com/success?sid=)`&authorization_token=`
- When user gets redirect: [`https://example.com/success?sid=39a1c773-bafd-754d-af1f-b30c592f1267&authorization_token=a1a8f727-2756-6058-bd3c-40069be0994b`](https://example.com/success?sid=39a1c773-bafd-754d-af1f-b30c592f1267&authorization_token=a1a8f727-2756-6058-bd3c-40069be0994b)
- On create call: [`https://example.com/success?sid=`](https://example.com/success?sid=)`&oder_id=`
- When user gets redirect: [`https://example.com/success?sid=39a1c773-bafd-754d-af1f-b30c592f1267&oder_id=a1a8f727-2756-6058-bd3c-40069be0994b`](https://example.com/success?sid=39a1c773-bafd-754d-af1f-b30c592f1267&oder_id=a1a8f727-2756-6058-bd3c-40069be0994b)

#### 4. b. From the HPP Session Status

This token can be retrieved by making a read session call to the HPP API or registering for callback. You can for example use a polling mechanism to check the status of the session. When the HPP Session gets successful because your Consumer gets an authorization, the status will change to `COMPLETE`. Depending on the value of `place_order_mode`, you will be able to extract the `authorization_token` from the server response or directly the `order_id` if the order is placed by HPP. Please read our track session status guide to get all details on how you can get the status of the session.

### 5. Handle the result of the HPP Session

The HPP Session was completed successfully and you need now to act depending on your parameters.

- With `place_order_mode` to its default value (`NONE`), you now need to place an Order with Klarna Payments API.
- With `place_order_mode` set to `PLACE_ORDER`, you will need to store the order_id to capture the payment once the goods are shipped.
- With `place_order_mode` set to `CAPTURE_ORDER`, you need only to store the order_id to do post-purchase operations such as refunds.

#### 5. a. Place Order with Klarna Payments API

As described in the objects overview, when a Consumer gets a *Payment Authorization*, your backend will need to use a **KP Authorization Token** to place the Order. Now that the Consumer has gotten an Authorization from Klarna for the Payment, you have to use the Authorization Token that you retrieved in the redirection to Place the Order. After this call, Klarna will consider that the Order is actually valid and that you will be able to capture the payment when the goods are being delivered. Please read the place order guide of Klarna Payments to get all details. Depending on your integration use case (ie *eCommerce*,*In Store*or *Telesales*), you may have to respect some guidelines when placing the order, see special rules. To ease your integration and depending on your use case, you can count on the auto_capture feature of the KP API to automatically capture the order after its creation. Please read the place order guide of Klarna Payments to get all details. This call corresponds to **Step 7**in the sequence diagram.

### Place order request

``` json
{
"purchase_country": "GB",
"purchase_currency": "GBP",
"locale": "en-GB",
"order_amount": 57064,
"order_tax_amount": 9511,
"order_lines": [
{
"image_url": "https://www.exampleobjects.com/logo.png",
"type": "physical",
"reference": "Could be a Product Id or SKU #",
"name": "Cool Bike",
"quantity": 1,
"unit_price": 20000,
"tax_rate": 0,
"total_amount": 20000,
"total_discount_amount": 0,
"total_tax_amount": 0
}
]
}
```

### Place order response

``` json
{
"order_id": "41c001ca-f6d4-4240-bbc5-5d2c036a2de4",
"fraud_status": "ACCEPTED"
}
```

### 5. b. Capture Payment with Order Management API

Orders that are created without auto_capture will need to be captured using the **Order Management API**. This can happen when you create the Order by yourself (see previous step) or when you use CAPTURE_ORDER as place_order_mode value. No payment will occur until the order has been captured. This is for use in transactions where the purchased goods are not immediately delivered but are made available at a later time. Please read the capture guide of Order Management to get all details.

## Edge cases

### Disabling an HPP Session by Merchant initiative

If for any reason the payment session has to be canceled (expiration of an offer, order was paid using another payment method, etc), the HPP API gives to the Merchant the possibility to disable an *HPP Session*. To do that, it is required to send a delete request on the HPP Session resource. Please read the disable session call reference of HPP</kp_session_id></jwt></kp_session_id></parameters></token></endpoint></https:>