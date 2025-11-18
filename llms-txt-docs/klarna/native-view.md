# Source: https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/reactnative/native-view.md

# Native View - React Native

## Adding Klarna payments to your application is as easy as adding a view and performing the payment operations on it.

Klarna’s Mobile SDK is the official toolkit for integrating Klarna products into native iOS apps. It enables you to offer Klarna’s payment methods with a seamless in-app user experience. The SDK is designed to provide the optimal integration and, under the hood, the SDK handles web-based flows in a mobile-friendly way to reduce friction and ensures that all the features listed below are fully supported for a superior customer experience across all mobile platforms.

<img alt="React native checkout view" height="670" src="1_overview.png" title="React native checkout view" width="670"/> **Feature support with Klarna’s Mobile SDK:**

- Remember Returning Customers: enable faster checkouts and improved conversion by reducing friction for returning users.
- Device-Wide Login Experience: simplify repeat purchases by enabling customers to remain logged in to Klarna across merchant apps on the same device.
- Passkey Support: offer biometric-based login for enhanced security and a frictionless user authentication experience.
- Application Redirects: seamlessly redirect users to external apps (e.g. bank or identity verification apps) and ensure a smooth return back into your app to complete payments without disruption.
- Camera Access for ID Verification: improve acceptance by enabling secure and instant identity verification within the app.
- Secure Browser Context: provide a secure, embedded browser environment for displaying Klarna-hosted content (payment pages or terms).
- File Sharing and Download for T&Cs: Let customers download or share terms and conditions directly from the app for full transparency.

### **How it works**

For a Mobile SDK integration your Payment Server and Mobile App must work together to complete the purchase flow:

{{#mermaid:
sequenceDiagram
participant Consumer
participant Merchant App
participant Mobile SDK
participant Merchant Server
participant Klarna API
Consumer->>Merchant App: Navigate to checkout screen
Merchant App->>Merchant Server: Create payment session
Merchant Server->>Klarna API: Create Klarna Payment session
Note over Merchant Server, Klarna API: "intent" should be set in relevance to the desired use case
Klarna API-->>Merchant Server: Klarna payment session response
Merchant Server-->>Merchant App: Klarna payment session client_token
Merchant App->>Mobile SDK: Create the Payment View
Note over Merchant App: Includes 'Klarna' category and an eventListener
Merchant App->>Mobile SDK: Initialize the payment session using client_token
Merchant App->>Mobile SDK: Load the Payment View
Consumer->>Merchant App: Select Klarna in Payment selector
Merchant App->>Merchant App: Display the KlarnaPaymentView
Consumer->>Merchant App: Click "Continue with Klarna"
Merchant App->>Mobile SDK: Authorize the session
Note over Merchant App: Consumer completes to purchase flow.
Mobile SDK-->>Merchant App: Provide authorization token (valid for 60 minutes)
Merchant App->>Merchant Server: Sends the authorization token for creating order
Merchant Server->>Klarna API: Create Order POST (setup/payments/v1/authorizations/{authorizationToken}/order)
Klarna API-->>Merchant Server: Provide order_id and redirect_url
Merchant Server-->>Merchant App: Provide order details
Merchant App->>Consumer: Redirected to order confirmation screen
}}

1.  **[Prepare](https://docs.klarna.com#prepare):** Make sure you have the credentials for Klarna Payments.
2.  **[Initiate payment](https://docs.klarna.com#initiate-payment-server-side)** (Server-side): Create a payment session from your backend and pass `client_token` to your app.
3.  **[Set up your app](https://docs.klarna.com#setup-your-app)** (Mobile App): Install the Klarna SDK using your package manager.
4.  **[Render payment view](https://docs.klarna.com#render-payment-view-mobile-app)** (Mobile App): Present Klarna’s native view to display Klarna in your checkout.
5.  **[Authorize the session](https://docs.klarna.com#authorize-the-session-mobile-app)** (Mobile App): Trigger the authorization through the SDK and handle the callback.
6.  **[Create an order](https://docs.klarna.com#create-an-order-server-side)** (Server-side): Pass the resulting authToken to your backend to finalize the payment and create an order.

**Presenting Klarna in your mobile checkout** To maximize conversion and usability, you must dynamically retrieve Klarna’s branding, payment descriptors, and payment widget via Klarna’s API and SDK to present accurate, localized, and up-to-date payment options.


![iOS_payment_widget.png](iOS_payment_widget.png)
*iOS_payment_widget.png*

1.  **Payment Descriptor:** Dynamically populated in Klarna Payment session response, in the `payment_method_categories.name` field.
2.  **Payment Sub header:** Added by merchant.
3.  **Widget:** Provided with the `KlarnaPaymentView` from the Mobile SDK.
4.  **Klarna Badge:** Dynamically populated in Klarna Payment session response, in the `payment_method_categories.asset_urls.standard` field.

## Prepare

When you integrate Klarna payments into your online store, your customers see Klarna as an option when they select a payment method for their purchases. If your customers select Klarna for their purchase, they are redirected to log into their Klarna account. Your customers select their preferred Klarna payment option (pay now, pay later, pay in parts) once they're logged into their Klarna account. We handle the Klarna account user flow, so you don't have to worry about it.

### Prerequisites

Before you start integrating Klarna payments, there are a few things you need to prepare in advance:

- Access to the Merchant portal
  - To access the test Merchant portal, you can [sign up to create a new test account](https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test/#accessing-the-test-merchant-portal-creating-a-new-test-account) or log in with a test existing account.
- API keys for the Klarna Payments API
  - To test your Klarna API integration, you need a set of [test credentials](https://docs.klarna.com/resources/developer-tools/testing-payments/before-you-test/#getting-test-credentials-for-apis).
- [The API reference](https://docs.klarna.com/api/payments/). You can download the Open API specification for the Klarna payments API and use the specification to [generate](https://openapi-generator.tech/) an API SDK for your programming language.
- [Sample customer data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-customer-data/) and [sample payment data](https://docs.klarna.com/resources/developer-tools/sample-data/sample-payment-data/)

## <span>Initiate payment (Server-side)</span>

When your customer wants to pay with Klarna, you have to open a payment session and share the shopping cart details in a `POST` request to the `{apiURL}/payments/v1/sessions` endpoint. In that request, you also specify if the payment is one-time or recurring. Once you start a payment session, it stays open for 48 hours or until you place an order. You can also send a separate `POST` request to cancel the session.

### <span>Request</span>

#### <span>Authentication</span>

Klarna payments API uses HTTP basic authentication. To authenticate, use your API credentials that consist of:

- A username linked to your Klarna merchant ID (MID)
- A password associated with your username

If you're using an API platform that lets you store your credentials, you can add them in relevant fields. Otherwise, make sure to include the Base64-encoded username:password in the Authorization header field of each API request, as shown below.

``` json
Authorization: Basic pwhcueUff0MmwLShJiBE9JHA==
```

###### *A sample authorization request header with Base64-encoded credentials.*

#### <span>Common Parameters</span>

To get a success response, include the following required parameters in your `POST {apiURL}/payments/v1/sessions` request.

| Parameter | Description |
|----|----|
| `locale` | The language of information presented on the Klarna widget. Learn more about [using locale in API calls](https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales/). |
| `purchase_country` *required* | The country where the purchase is made. Learn more about [supported countries](https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales/). |
| `purchase_currency` *required* | The currency in which the customer is charged. Learn more about [supported currencies](https://docs.klarna.com/payments/web-payments/before-you-start/data-requirements/puchase-countries-currencies-locales/). |
| `order_amount` *required* | The total price of the order, including tax and discounts. |
| `order_lines` *required* | The details of order lines in the purchase. |
| `intent` | The purpose of the payment session. |
| `merchant_urls.authorization` | Get a callback once the customer has completed the flow and you can create an order. |

### <span>Response</span>

#### <span>Success Response</span>

In response to a create session call, you receive:

- `session_id`, a payment session identifier you can use to \[ update the session\] and \[ retrieve session\] details
- `client_token`, a token you pass to the [JavaScript SDK](https://docs.klarna.com/payments/web-payments/additional-resources/klarna-payments-sdk-reference/) or Mobile SDK([Android](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/klarna-payments/#authorizing-the-session), [iOS](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/ios/klarna-payments/#authorizing-the-session) and [React Native](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/reactnative/klarna-payments/#authorize)) to launch the Klarna widget
- `payment_method_categories`, an array that lists the grouped Klarna payment methods available for the session. We can respond with one or more categories depending on the market and account configuration.

``` json
{
"session_id": "068df369-13a7-4d47-a564-62f8408bb760",
"client_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjAwMDAwMDAwMDAtMDAwMDAtMDAwMC0wMDAwMDAwMC0wMDAwIiwidXJsIjoiaHR0cHM6Ly9jcmVkaXQtZXUua2xhcm5hLmNvbSJ9.A_rHWMSXQN2NRNGYTREBTkGwYwtm-sulkSDMvlJL87M",
"payment_method_categories": [
{
"identifier": "klarna"
"name" : "Pay with Klarna",
"asset_urls" : {
"descriptive" : "https://x.klarnacdn.net/payment-method/assets/badges/generic/klarna.svg",
"standard" : "https://x.klarnacdn.net/payment-method/assets/badges/generic/klarna.svg"
}
}
]
}
```

###### *A sample success response to the create session call.*

#### <span>Error Response</span>

If your request doesn't pass our validation, you'll receive an error response.

``` json
{
"correlation_id": "6a9b1cb1-73a3-4936-a030-481ba4bb203b",
"error_code": "BAD_VALUE",
"error_messages": [
"Bad value: order_lines"
]
}
```

###### *A sample error response caused by incorrect order line details.*

​Go to [Error Handling](https://docs.klarna.com/resources/developer-tools/error-handling/error-codes-and-messages-for-klarna-payments/) to learn more about common errors and troubleshooting suggestions. You can use the value in `correlation_id` to find entries related to the request under **Logs** in the Merchant portal.

## Setup your app

### Package Managers

#### NPM

If you want to add the SDK via `npm` use the following to add library dependency:

``` bash
npm install react-native-klarna-inapp-sdk --save
```

#### Yarn

If you are using yarn, then use the following to add library dependency:

``` shell
yarn add react-native-klarna-inapp-sdk
```

For installing native dependencies for iOS, go to your `ios` directory and run `pod install`.

### Android

You need to add a reference to the repository in your own app’s build.gradle which can be done by adding the lines between the comments below:

``` groovy
allprojects {
    repositories {
        ...
        // Required configuration to fetch native Android SDK
        maven {
            url 'https://x.klarnacdn.net/mobile-sdk/'
        }
    }
}
```

#### Return URL

Mobile SDK integrations might, at some point, open third-party applications. To automatically return the user, these third-party applications need to know how to build a return intent or URL. To do that, you’ll need to provide the SDK with what we call the “Return URL” parameter. If you haven’t done so already, follow this [documentation](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/android/get-started/) for Android and this [documentation](https://docs.klarna.com/payments/mobile-payments/integrate-with-mobile-sdk/ios/get-started/) for iOS.

### iOS

#### Return URL

Klarna purchase flows might require authorizations in other applications (e.g. bank apps) or do a handover to the Klarna app. In such cases, a return URL to your application ensures seamless return to the flow in your app, hence setting up a return URL is required. It is expected that redirects to this URL should only open your application without any changes in the UI state, ensuring the customer can continue the flow prior to external navigation. You can set up a Return URL app scheme to your application by [configuring a custom URL scheme](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app).**Important:** The return URL string passed to Klarna must include `://` after the scheme name. For example, if you defined `myApp` as the scheme, you must use `"myApp://"` as the return URL argument to Klarna.To avoid a Klarna specific app scheme, you can use a host in a common scheme for Klarna redirects, e.g. `myApp://klarna-redirect` , this can allow you to differentiate and handle these redirect in your handler. Considering the return URL is a constant value in `Constants.klarnaReturnUrl`, you can handle redirects to your return URL as such: 

### SceneDelegate


``` swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<uiopenurlcontext>) {
    guard let url = URLContexts.first?.url else {
        return
    }
    if (url.absoluteString.starts(with: Constants.klarnaReturnUrl.absoluteString)) {
        // This is a return URL for Klarna – skip deep linking
        return
    }
    // This was not a return URL for Klarna
}
```



### AppDelegate


``` swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey: Any] = [:]) -> Bool {
    if (url.absoluteString.starts(with: Constants.klarnaReturnUrl.absoluteString)) {
        // This is a return URL for Klarna – skip deep linking
        return true
    }
    // This was not a return URL for Klarna
    return false
}
```



### SwiftUI


``` swift
@main
struct MyApp: App {
    var body: some Scene {
        WindowGroup {
            // This is the root content view of your application
            AppContentView()
                .onOpenURL { incomingURL in
                    if (url.absoluteString.starts(with: Constants.klarnaReturnUrl.absoluteString)) {
                        // This is a return URL for Klarna – skip deep linking
                        return
                    }
                    // This was not a return URL for Klarna
                }
        }
    }
}
```

#### Klarna App URL Queries

Klarna flows on mobile utilize Application Queries for Klarna app schemes to offer seamless app handover experience to customers. In order for the SDK to check availability of the Klarna app, we need you to enable querying Klarna app on the device by adding Klarna app schemes to [LSApplicationQueriesSchemes](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/plist/info/LSApplicationQueriesSchemes). This can be configured easily in XCode by going to your project setting and under "Info"(alternatively this is also available in your `Info.plist` file) you should see an entry list for `Queried URL Schemes`, this list should contain the `klarna` and `klarnaconsent` schemes:


![mobile-sdk-queried-url-schemes-xcode.png](mobile-sdk-queried-url-schemes-xcode.png)
*mobile-sdk-queried-url-schemes-xcode.png*

### Import the SDK

In order to use the SDK from your React Native application import it by:

``` javascript
import KlarnaPaymentView from 'react-native-klarna-inapp-sdk';
```

## <span>Render payment view (Mobile App)</span>

You can import the KlarnaPaymentView from the library. You’ll then be able to add it as a component to your app. This component exposes callbacks as props and methods you can call via the component’s ref. The view will auto-size height-wise and grow to fill it’s containing view’s width.

### Creating the View

You can add the view to your layout as shown below:

``` typescript
const paymentViewRef = useRef<klarnapaymentview>(null);
const createPaymentView = () => {
    return (
        <klarnapaymentview =="" category='{"klarna"}' oninitialized="{()" ref="{paymentViewRef}" returnurl="{'returnUrl://'}" style="{styles.paymentView}"> {
              // handle onInitialized
            }}
            onLoaded={() => {
              // handle onLoaded
            }}
            onLoadedPaymentReview={() => {
              // handle onLoadedPaymentReview
            }}
            onAuthorized={(approved, authToken, finalizeRequired) => {
              // handle onAuthorized
            }}
            onReauthorized={(approved, authToken) => {
              // handle onReauthorized
            }}
            onFinalized={(approved, authToken) => {
              // handle onFinalized
            }}
            onError={(error: KlarnaPaymentsSDKError) => {
              // handle onError
            }}
          />
    )
}
```

| **Name** | **Type** | **Description** |
|----|----|----|
| `returnUrl` | String | App scheme URL as defined in set up to return from external applications. |
| `category` | String | Should always be set to `"klarna"` as it's the preferred payment category. |
| `onInitialized` | () =\> {} | The initialize call succeeded. |
| `onLoaded` | () =\> {} | The load call succeeded. |
| `onLoadedPaymentReview` | () =\> {} | The load payment review call succeeded. |
| `onAuthorized` | ({}) =\> {} | The authorize call succeeded. |
| `onReauthorized` | ({}) =\> {} | The reauthorize call succeeded. |
| `onFinalized` | ({}) =\> {} | The finalize call succeeded. |
| `onError` | ({}) =\> {} | An error occurred. |

### <span>Initialize the session</span>

Before content is rendered into a payment view or an authorization, payment session with it's client token needs to be initialized. This can be done by calling `initialize` and handling result in `klarnaInitialized`.

``` typescript
// initilize with clientToken for session created from server-side
paymentViewRef.current?.initialize(props.clientToken);
```

| **Param** | **Type** | **Description** |
|----|----|----|
| `clientToken` | String | The client token you get from Klarna Payments API session response. |

If successful, `onInitialized` will be called in the property you supplied. If it’s not successful, `onError` will be called instead.

``` typescript
onInitialized={() => {
    paymentViewRed.current?.load() // optionally load payment widget upon initialize 
}
```

If successful, `klarnaInitialized` from `KlarnaPaymentEventListener` will be called in the listener you supplied. If it’s not successful, `klarnaFailed` will be called instead. <span>Load payment widget</span>

### <span>Load payment widget</span>

Once you’ve initialized the view and you’re ready to display the payment widget, simply by calling `load`.

``` typescript
// load optional payment widget
paymentViewRef.current?.load();
```

| **Param** | **Type** | **Description** |
|----|----|----|
| `sessionData` | String \| string \| undefined | An optional string to update the session. Formatted as JSON. |

If successful, `onLoaded` will be called in property you supplied and for errors `onError` will be called instead.

``` typescript
onLoaded={() => {
    // Content has finished loading and if you have any loader you could hide it here.
}
```

## Authorize the session (Mobile App)

Once the user has confirmed that they want to pay with Klarna, it’s time to authorize the session. This is done by calling `authorize`, and similar to `load`, you can supply an optional JSON string with `jsonData` parameter to update the session. You can also specify whether auto-finalization should be turned off(on by default) and in that case you might be required to finalize the session after.

``` typescript
// authorize the payment session
paymentViewRef.current?.authorize();
```

| **Param** | **Type** | **Description** |
|----|----|----|
| `autoFinalize` | Boolean \| boolean \| undefined | An optional flag used to turn off auto-finalization for direct bank transfer. |
| `sessionData` | String \| string \| undefined | An optional string to update the session. Formatted as JSON. |

If successful, `onAuthorized` will be called in property you supplied and for errors `onError` will be called instead.

``` typescript
onAuthorized={(approved, authToken, finalizeRequired) => {
    if (authToken && approved) {
        // authorization is successful, backend may create order
    }
    
    if (finalizeRequired) {
        // finalize() call is required
    }
}
```

### Finalize

This is only needed if you set `autoFinalize` to `false` in [authorize](https://docs.klarna.com#authorize-the-session-mobile-app) call.If a specific payment method needs you to trigger a second authorization, call finalize when you’re ready.

``` typescript
// authorize the payment session
paymentViewRef.current?.authorize();
```

| **Param** | **Type** | **Description** |
|----|----|----|
| `sessionData` | String \| undefined | An optional string to update the session. Formatted as JSON. |

If successful, `onFinalized` will be called in property you supplied and for errors `onError` will be called instead.

``` typescript
onFinalized={(approved, authToken) => {
    if (authToken && approved) {
        // finalize is successful, backend may create order
    }
}
```

## Create an order (Server-side)

To continue with the purchase, you have to create an order in Klarna's system. This step takes place in the server side through the Klarna payments API.

### Create an order

To create an order for a one-time payment, send a `POST` request to the `{apiUrl}/payments/v1/authorizations/{authorizationToken}/order` endpoint and include `authorization_token` in the path. For example, if the `authorization_token` is `b4bd3423-24e3`, send your request to the `{apiUrl}/payments/v1/authorizations/b4bd3423-24e3/order` endpoint.

``` json
{
"purchase_country": "US",
"purchase_currency": "USD",
"billing_address": {
"given_name": "John",
"family_name": "Doe",
"email": "john@doe.com",
"title": "Mr",
"street_address": "Lombard St 10",
"street_address2": "Apt 214",
"postal_code": "90210",
"city": "Beverly Hills",
"region": "CA",
"phone": "333444555",
"country": "US"
},
"shipping_address": {
"given_name": "John",
"family_name": "Doe",
"email": "john@doe.com",
"title": "Mr",
"street_address": "Lombard St 10",
"street_address2": "Apt 214",
"postal_code": "90210",
"city": "Beverly Hills",
"region": "CA",
"phone": "333444555",
"country": "US"
},
"order_amount": 10,
"order_tax_amount": 0,
"order_lines": [
{
"type": "physical",
"reference": "19-402-USA",
"name": "Battery Power Pack",
"quantity": 1,
"unit_price": 10,
"tax_rate": 0,
"total_amount": 10,
"total_discount_amount": 0,
"total_tax_amount": 0,
"product_url": "https://www.estore.com/products/f2a8d7e34",
"image_url": "https://www.exampleobjects.com/logo.png"
}
],
"merchant_urls": {
"confirmation": "https://example.com/confirmation",
"notification": "https://example.com/pending"
},
"merchant_reference1": "45aa52f387871e3a210645d4",
}
```

###### *A`POST` request to create an order for a one-time payment.*

#### Success response

When you receive a success response, the customer gets charged and the Klarna payments session is closed. As part of the response, you receive the following details:

- `order_id`, an order identifier that you can later use to capture or refund the order using the [Order management API](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-3-create-an-order/)
- `redirect_url`, a URL to which you redirect the customer. This isn't included in the response received if you didn't include the URL when [initiating a payment](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-1-initiate-a-payment/)
- `fraud_status`, an indicator of whether the transaction is suspected to be legitimate or [fraudulent](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-3-create-an-order/#special-considerations-for-one-time-payments)
- `authorized_payment_method`, the payment method selected by your customer for this purchase

``` json
{
"order_id": "3eaeb557-5e30-47f8-b840-b8d987f5945d",
"redirect_url": "https://payments.klarna.com/redirect/...",
"fraud_status": "ACCEPTED",
"authorized_payment_method": "invoice"
}
```

###### *A success response to the order creation request for a one-time payment.*

Send the customer browser to `redirect_url` provided in the response. Klarna places a cookie in the browser and redirects the customer back to the confirmation URL you provided when creating the session. This makes the checkout faster the next time the customer chooses to pay with Klarna.

#### Error response

If your request doesn't pass our validation, you'll receive an error response. The most common reasons why creating an order fails are:

- placing the order more than 60 minutes after authorization
- modifying purchase details after authorization without updating the payment session

``` json
{
"correlation_id": "6a9b1cb1-73a3-4936-a030-481ba4bb203b",
"error_code": "ERROR_CODE",
"error_messages": [
"ERROR_MESSAGE"
]
}
```

###### *An error response to the order creation request for a one-time payment.*

Here are examples of common errors with troubleshooting suggestions. You can use the value in `correlation_id` to find entries related to the request under **Logs** in the Merchant portal.

| Error code | Error message | Description |
|----|----|----|
| `NOT_FOUND` | `Invalid authorization token` | The authorization token has expired because the order was placed more than 60 minutes after authorization. To fix the error, [request a new `authorization_token`](https://docs.klarna.com/payments/web-payments/integrate-with-klarna-payments/step-3-create-an-order/#authorize-call) and use it to place the order. |
| `BAD_VALUE` | `Not matching fields: [billing_address.postal_code]` | The data shared with Klarna in a previous step (`create_session`, `load()`, or `authorize()`) have been modified causing the validation to fail. |
| `BAD_VALUE` | `Not matching fields: [Incorrect number of items in the cart. Expected: 2, Actual: 3]` | The order lines or the cart were updated after the `authorize()` call. Please ensure that the cart is kept as-is or send a new authorization request. |
| `REJECTED` | `Rejected` | This is an edge case reason, but can be triggered in case the merchant is configured with being allowed to update the cart. This could be updated from the authorize to the place order in such a way that a new authorize is triggered. In this case this is rejected. |

## What's next

Klarna Mobile SDK provides a full suite of mobile-first integrations, including Klarna products like:

<table>
<tbody>
<tr>
<td>
![Pink_Standard_Consumer_(1).png](Pink_Standard_Consumer_(1).png)
*Pink_Standard_Consumer_(1).png*</td>
<td>
![Pink_Standard_Consumer_(2).png](Pink_Standard_Consumer_(2).png)
*Pink_Standard_Consumer_(2).png*</td>
<td>
![Pink_Standard_Consumer_(3).png](Pink_Standard_Consumer_(3).png)
*Pink_Standard_Consumer_(3).png*</td>
</tr>
<tr>
<td style="vertical-align:middle;text-align:center;"><p>Sign in with Klarna</p></td>
<td style="vertical-align:middle;text-align:center;"><p>On-site Messaging</p></td>
<td style="vertical-align:middle;text-align:center;"><p>Express Checkout</p></td>
</tr>
</tbody>
</table>

- **On-site Messaging**: Show contextual messaging let your customers know about the available payment options in pre-checkout: click [here](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-for-mobile/) to learn more.
- **Sign in with Klarna**: Seamlessly identify and let users login via their Klarna account: click [here](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/) to learn more.
- **Express Checkout**: Accelerate your checkout process and boost conversion by offering a one-click checkout, click [here](https://docs.klarna.com/conversion-boosters/express-checkout/before-you-start/) to learn more (Mobile SDK support available soon).

Complete your integration with

- [Order management](https://docs.klarna.com/payments/after-payments/order-management/before-you-start/what-is-order-management/)
- [Settlements](https://docs.klarna.com/payments/after-payments/settlements/settlement-files/)
- [End-to-end testing](https://docs.klarna.com/resources/developer-tools/testing-payments/test-cases/)
- [Prepare for go live](https://docs.klarna.com/resources/developer-tools/testing-payments/go-live-checklist/)</klarnapaymentview></klarnapaymentview></uiopenurlcontext>