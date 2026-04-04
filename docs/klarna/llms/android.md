# Source: https://docs.klarna.com/conversion-boosters/express-checkout/integrate-express-checkout/mobile-sdk-integration/android.md

# Integrate Express Checkout - Android

## <span>This guide will show you how to use Klarna Mobile SDK to implement Express Checkout in your Android mobile application, providing a fast and simple shopping experience for your users.</span>

Please review [this brief guide](https://docs.klarna.com/conversion-boosters/express-checkout/before-you-start/) first to ensure you are prepared to offer this integration to your customers.


![Klarna Express Checkout Button|center|670x670px](kec-item-page.png)
*Klarna Express Checkout Button|center|670x670px*

## Integration steps

1.  **[Prepare](https://docs.klarna.com#prepare):** Make sure you have the credentials and setup for Klarna Express Checkout.
2.  **[Present the button](https://docs.klarna.com#present-the-button-mobile-app):** (Mobile App) Create an instance of `KlarnaExpressCheckoutButton` with session parameters and present in your native app.
3.  **[Handle authorization](https://docs.klarna.com#handle-authorization-mobile-app):** (Mobile App) Once the customer clicks the button and authorizes the payment, handle response from the SDK.
4.  **[Create an order](https://docs.klarna.com#create-an-order-server-side):** (Server-side) Once a session is authorized, create an order with authorization token via your backend.

### **How it works**

For a Mobile SDK integration your Payment Server and Mobile App must work together to offer one-click checkout experience:

{{#mermaid:
sequenceDiagram
participant Consumer
participant Merchant App
participant Mobile SDK
participant Merchant Server
participant Klarna API
Consumer->>Merchant App: Navigate to checkout, shopping cart, product or wishlist page
Merchant App->>Mobile SDK: Create Express Checkout Button with session information
Merchant App->>Merchant App: Display the Express Checkout Button
Consumer->>Mobile SDK: Click the Express Checkout Button
Note over Mobile SDK: Consumer completes to purchase flow.
Mobile SDK-->>Merchant App: Provide authorization token (valid for 60 minutes)
Merchant App->>Merchant Server: Sends the authorization token for creating order
Merchant Server->>Klarna API: Create Order POST (setup/payments/v1/authorizations/{authorizationToken}/order)
Klarna API-->>Merchant Server: Provide order_id and redirect_url
Merchant Server-->>Merchant App: Provide order details
Merchant App->>Consumer: Redirected to order confirmation screen
}}

## Prepare

### Choose applicable placements

The right placement of the Express button can significantly enhance your user experience, leading to higher conversion rates and increased sales.


![ You can place the Express checkout button at multiple stages of the shopping journey.](5a558ef7-52d7-4fad-a3fa-7abbde893601_PlacementOverview.jpeg)
*You can place the Express checkout button at multiple stages of the shopping journey.*

To learn more about placements, check out [this section](https://docs.klarna.com/conversion-boosters/express-checkout/additional-resources/button-placement/).

### Prerequisites

Before you integrate Express checkout, check that you meet the following prerequisites:

1.  Make sure to have a payment solution with Klarna. Before integrating Express checkout into your website, you need to have a merchant account with Klarna and [Klarna payments](https://docs.klarna.com/payments/web-payments/before-you-start/prepare-your-integration/#preapre-your-integration) or [Klarna checkout](https://docs.klarna.com/conversion-boosters/express-checkout/before-you-start/) integrated in your checkout.  
2.  Make sure to allowlist the domain of the page on which Express checkout will be integrated.If not all the domains are added to the allowlist, Express checkout will still load, however, the customer will see a "We couldn't load the next screen" error.

To allowlist the domain URLs, follow these steps: 

- Log into Klarna Merchant portal. If you want to test Express checkout, log into the playground Merchant portal. If you want to build a live integration, log into the production Merchant portal.
- Once logged in, go to **Payment settings**\> **Client Identifiers**. In the **Allowed Origins for your integrations** section, click **Manage origins**.   
- In the **Register new origin** field, add your domain’s URL. Then, click **Register**. The registered domain is now listed in **Allowed origins**.

3\. Generate a client identifier that will let you authenticate requests sent to Klarna:

- Log into Klarna Merchant portal.
- Once logged in, go to **Payment settings**\> **Client Identifiers**.
- To generate a new client identifier, navigate to **Client Identifiers for your integrations** and click **Generate client identifier**. 

If you’ve previously generated a client identifier for your store, you can use it to build your Express checkout integration.

## <span>Set up your app</span>

### <span>Import the SDK</span>

#### <span>Add the Repository</span>

Add the Klarna Mobile SDK maven repository: 

### Kotlin


``` kotlin
repositories {
    maven("https://x.klarnacdn.net/mobile-sdk/")
}
```



### Groovy


``` groovy
repositories {
    maven {
        url 'https://x.klarnacdn.net/mobile-sdk/'
    }
}
```

#### <span>Add the Dependency</span>

Add the SDK as a dependency to your app: 

### Kotlin


``` kotlin
dependencies {
    implementation("com.klarna.mobile:sdk:2.x.x")
}
```



### Groovy


``` groovy
dependencies {
    implementation 'com.klarna.mobile:sdk:2.x.x'
}
```

To read more about Mobile SDK versioning policy, check out [this section.](https://docs.klarna.com#versioning-policy)

## **Present the button (Mobile App)**

Create an instance of the `KlarnaExpressCheckoutButton` when your cart page or product detail page is loaded. This ensures that the button is readily available for user interaction. Depending on your integration setup, you can create and initiate the Express Checkout button using either a client-side session or a server-side session:

- **Client-side session:** Use this method if you prefer to set a client ID from the Merchant Portal. This approach is typically used when the session management is handled entirely on the client side. You would need to provide the order details in this approach.
- **Server-side session:** Choose this method if you have a client token generated by the backend for the server-side session. This is suitable when you want to manage sensitive session data on the server. You do not need to provide the order details with this approach.

Once the button is created, add it to your screen. This involves adding the button to the appropriate view hierarchy in your application's user interface.

``` kotlin
val sessionOptions: KlarnaExpressCheckoutSessionOptions = KlarnaExpressCheckoutSessionOptions.ClientSideSession(
    clientId =”myClientId”,
    autoFinalize = true,
    collectShippingAddress = true,
    sessionData = mySessionData
)
val expressCheckoutButtonOptions = KlarnaExpressCheckoutButtonOptions(
    locale =”en-US”,
    sessionOptions = sessionOptions,
    styleConfiguration = styleConfiguration,
    environment = KlarnaEnvironment.PRODUCTION,
    region = KlarnaRegion.NA,
    theme = KlarnaTheme.LIGHT,
    callback = myCallback,
    loggingLevel = KlarnaLoggingLevel.Verbose
)
val expressCheckoutButton = KlarnaExpressCheckoutButton(
    context = this,
    options = expressCheckoutButtonOptions
)
expressCheckoutButton.layoutParams = LayoutParams(
    LayoutParams.MATCH_PARENT,
    LayoutParams.WRAP_CONTENT
)
parent.addView(expressCheckoutButton)
```

#### Parameters

##### <span>**KlarnaExpressCheckoutButton**</span>

| Param | Description |
|----|----|
| `Context` | <span>The context of the Activity the button is in.</span> |
| <span>`KlarnaExpressCheckoutButtonOptions`</span> | <span>Contains all the options for the button.</span> |

##### <span>**KlarnaExpressCheckoutButtonOptions**</span>

| Param | Description |
|----|----|
| <span>`KlarnaExpressCheckoutSessionOptions`</span> | <span>Authorization options that will be used for authorization upon a user click.</span> |
| <span>`KlarnaExpressCheckoutButtonCallback`</span> | <span>Callback that the merchant can use to get notified of the key events happening in the flow.</span> |
| <span>`locale`</span> | <span>Locale of the button text. </span><span>The default is “en-US”.</span> |
| <span>`KlarnaExpressCheckoutButtonStyleConfiguration?`</span> | <span>Style configuration for the button, including button theme, button shape, and style.</span> |
| `KlarnaEnvironment` | <span>Operating environment of the button. The default is \`PRODUCTION\`".</span> |
| <span>`KlarnaRegion`</span> | <span>Geographical region for the button’s API requests. The default is \`NA\`.</span> |
| <span>`KlarnaTheme`</span> | <span>Theme of the flow. The default is \`LIGHT\`.</span> |
| <span>`KlarnaLoggingLevel`</span> | <span>Logging level of the integration. The default is \`off\`.</span> |

##### <span>**KlarnaExpressCheckoutSessionOptions.ClientSideSession**</span>

| Param | Type | Description |
|----|----|----|
| <span>`clientId`</span> | <span>String</span> | <span>Partner client ID from Merchant Portal.</span> |
| <span>`sessionData`</span> | <span>String</span> | <span>JSON string used to update the session.</span> |
| <span>`autoFinalize`</span> | <span>Boolean</span> | <span>Whether the authorization should automatically be finalized. The default is true.</span> |
| <span>`collectShippingAddress`</span> | <span>Boolean</span> | <span>Whether the merchant needs the customer's shipping address from Klarna. The default is false.</span> |

##### <span>**KlarnaExpressCheckoutSessionOptions.ServerSideSession**</span>

| Param | Type | Description |
|----|----|----|
| `clientToken` | String | <span>Client token generated by the backend for the server-side session.</span> |
| `sessionData` | String | <span>JSON string used to update the session. The default value is null.</span> |
| `autoFinalize` | Boolean | <span>Whether the authorization should automatically be finalized. The default is true.</span> |
| `collectShippingAdress` | Boolean | <span>Whether the merchant needs the customer's shipping address from Klarna. The default is false.</span> |

##### **KlarnaExpressCheckoutButtonStyleConfiguration**

| Param | Description |
|----|----|
| <span>`KlarnaButtonTheme?`</span> | <span>Color theme of the button. The default is \`DARK\`.</span> |
| <span>`KlarnaButtonShape?`</span> | <span>Shape of the button. The default is \`ROUNDED_RECT\`.</span> |
| <span>`KlarnaButtonStyle?`</span> | <span>Style of the button. The default is \`FILLED\`.</span> |

## **Handle authorization (Mobile App)**

Once a customer clicks the Express Checkout button, the Klarna payment authorization process will begin. You must provide a callback object when creating the button, which will handle Klarna's response. This callback is essential for managing the payment flow and updating the UI based on the authorization result.

### Authorization Callback

If the authorization is successful, you will receive an authorization token from the authorization response within the callback object.

``` kotlin
override fun onAuthorized(
   view: KlarnaExpressCheckoutButton,
   response: KlarnaExpressCheckoutButtonAuthorizationResponse){
   if (response.approved && !response.authorizationToken.isNullOrBlank()) {
        // authorization is successful, backend may create order
    }
    if (response.finalizeRequired) {
        // finalize call is required, only applicable if you are setting autoFinalize to false
        // use response.clientToken to finalize
    }
}
```

#### Parameters

##### <span>**KlarnaExpressCheckoutButtonAuthorizationResponse**</span>

| Param | Type | Description |
|----|----|----|
| <span>`approved`</span> | <span>Boolean</span> | <span>Indicates whether the payment was approved.</span> |
| <span>`showForm`</span> | <span>Boolean</span> | <span>Indicates whether the payment is still available for authorization.</span> |
| <span>`finalizeRequired`</span> | <span>Boolean</span> | <span>Indicates whether the session requires finalization.</span> |
| <span>`authorizationToken`</span> | <span>String</span> | <span>The authorization token for the payment, if applicable.</span> |
| <span>`clientToken`</span> | <span>String</span> | <span>The client token for the session, if applicable, intended to be used for finalization.</span> |
| <span>`sessionId`</span> | <span>String</span> | <span>The ID of the Klarna Payments session.</span> |
| <span>`collectedShippingAddress`</span> | <span>String</span> | <span>Shipping address collected during the session, if applicable.</span> |
| <span>`merchantReference1`</span> | <span>String</span> | <span>Merchant references provided in the session creation.</span> |
| <span>`merchantReference2`</span> | <span>String</span> | <span>Additional merchant reference provided in the session creation.</span> |

#### Error Callback

In case an error happen in the SDK or technical errors during authorization, SDK will notify you via the `onError` method:

``` kotlin
override fun onError(view: KlarnaExpressCheckoutButton, error: KlarnaExpressCheckoutError) {
    // Handle different failure scenarios by checking the error name
    if (error.name == KlarnaExpressCheckoutError.AuthorizationFailed) {
        // Handle the AuthorizationFailed error
        println("Authorization failed: ${error.message}")
    }
    // ...
}
```

##### Parameters

###### <span>**KlarnaExpressCheckoutError**</span>

| Param | Type | Description |
|----|----|----|
| <span>`name`</span> | <span>String</span> | <span>Unique name of the error.</span> |
| <span>`message`</span> | <span>String</span> | <span>Elaborate description of the error.</span> |
| <span>`isFatal`</span> | <span>Boolean</span> | <span>Determines whether the error is fatal. If the error is fatal, the button should not be shown any further.</span> |
| <span>`sessionId`</span> | <span>String</span> | <span>Mobile SDK’s session ID.</span> |
| <span>`params`</span> | <span>String</span> | <span>A key-value map/dictionary of any additional error parameters.</span> |

<span>The table below lists all the different error names defined as constant values in the `KlarnaExpressCheckoutError`:</span>

| Error Name | Description |
|----|----|
| <span>`InvalidClientID`</span> | <span>Indicates that the client ID is not valid; for example, it is null or blank.</span> |
| <span>`InvalidClientToken`</span> | <span>Indicates that the client ID is not valid. For example it is null or blank.</span> |
| `MissingCallbackReference` | Indicates that the callback reference is lost. |
| <span>`AlreadyInProgress`</span> | <span>Indicates that the Klarna Express Checkout flow is already in progress.</span> |
| <span>`AuthorizationFailed`</span> | <span>Indicates that the authorization has failed.</span> |
| <span>`ButtonRenderFailed`</span> | <span>Indicates that the button could not be rendered successfully.</span> |
| <span>`InvalidAuthorizationResponseParams`</span> | <span>Indicates that the authorization response could not be parsed caused by invalid/missing params.</span> |

### Finalize the session

This is only required of `autoFinalize` is set to `false` in session options.If the session needs to be finalized, you’ll need to perform this last step to get an authorization token from your checkout confirmation screen. This can be done via [KlarnaPaymentView](https://docs.klarna.com), using the `clientToken` from <span>`KlarnaExpressCheckoutButtonAuthorizationResponse` to initialize the view and calling `finalize` method of that view.</span>

## <span>**Create an order (Server-side)**</span>
<span>Once you have the authorization token, you can [create an order](https://docs.klarna.com/api/payments/#operation/createOrder). When creating the order, make sure the shipping address provided in the request matches the collected shipping address returned alongside the authorization token.</span> To continue with the purchase, you have to create an order in Klarna's system. This step takes place in the server side through the Klarna payments API.

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

## Button styling

This section will help you customize the Express checkout button to ensure a seamless and trustworthy checkout experience, while leveraging Klarna’s strong brand to boost your conversions. Styling the Express checkout button is crucial for integrating it into your application in a way that complements your brand and encourages user engagement. To modify the style of the button, edit the source code as explained in this guide.

### <span>Theme</span>

The theme defines the button’s color. You can change the theme by setting the value of the theme attribute. Apart from the default dark theme, you can apply the light theme to have the button displayed in white or choose auto mode so the theme is selected automatically based on the device’s configuration. The button’s default theme color is dark. As the theme attribute is optional, the default theme is applied both when you set the attribute to default or if you omit it from the source code altogether. There are three theme values available, `DARK` (default), `LIGHT` and `AUTO`.


![Dark theme (default)|center|320x320px](kec-button-roundedrect-dark.png)
*Dark theme (default)|center|320x320px*

![Light theme|center|320x320px](kec-button-roundedrect-light.png)
*Light theme|center|320x320px*

``` kotlin
val buttonStyleConfiguration = KlarnaExpressCheckoutButtonStyleConfiguration(
    theme = KlarnaButtonTheme.DARK,
    shape = …,
    style = …
)
```

### <span>**Shape**</span>

Customizing the shape of the button to match your application’s look and feel is a key step in creating a visually cohesive and engaging user experience. To control the button's shape, change the value of the shape attribute. There are three shapes available with the Express checkout button: `ROUNDED_RECT` (default), `RECTANGLE` and `PILL`.


![KlarnaButtonShape.ROUNDED_RECT|center|320x320px](kec-button-roundedrect-dark.png)
*KlarnaButtonShape.ROUNDED_RECT|center|320x320px*

![KlarnaButtonShape.PILL|center|320x320px](kec-button-pill-dark.png)
*KlarnaButtonShape.PILL|center|320x320px*

![KlarnaButtonShape.RECTANGLE|center|320x320px](kec-button-rect-dark.png)
*KlarnaButtonShape.RECTANGLE|center|320x320px*

``` kotlin
val buttonStyleConfiguration = KlarnaExpressCheckoutButtonStyleConfiguration(
    theme = KlarnaButtonShape.ROUNDED_RECT,
    shape = …,
    style = …
)
```

### <span>**Style**</span>
<span>Use the outlined style to make the button visible on all backgrounds. To apply this style, set the `KlarnaButtonStyle` attribute to `OUTLINED`, otherwise default value `FILLED` will be used instead.</span>

![Outlined style|center|320x320px](kec-button-roundedrect-outlined.png)
*Outlined style|center|320x320px*

``` kotlin
val buttonStyleConfiguration = KlarnaExpressCheckoutButtonStyleConfiguration(
    style = KlarnaButtonStyle.OUTLINED,
    shape = …,
    theme = …
)
```

## <span>Optional</span>

### Enable logging

The SDK will log events and errors while it’s running, which you can read in **logcat** console. You can set the logging level for the SDK through the `loggingLevel` property of integration instance.

``` kotlin
klarnaExpressCheckoutButton.loggingLevel = KlarnaLoggingLevel.Verbose
```

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
![Android_native_checkout_.png](Android_native_checkout_.png)
*Android_native_checkout_.png*</td>
</tr>
<tr>
<td style="vertical-align:middle;text-align:center;"><p>Sign in with Klarna</p></td>
<td style="vertical-align:middle;text-align:center;"><p>On-site Messaging</p></td>
<td style="vertical-align:middle;text-align:center;"><p>Payments</p></td>
</tr>
</tbody>
</table>

- **On-site Messaging**: Show contextual messaging let your customers know about the available payment options in pre-checkout: click [here](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-for-mobile/) to learn more.
- **Sign in with Klarna**: Seamlessly identify and let users login via their Klarna account: click [here](https://docs.klarna.com/conversion-boosters/sign-in-with-klarna/integrate-sign-in-with-klarna/mobile-integration/) to learn more.
- **Payments**: Enhance your mobile app conversion with a seamless payment UX, click [here](https://docs.klarna.com) to learn more.

Complete your integration with

- [Order management](https://docs.klarna.com/payments/after-payments/order-management/before-you-start/what-is-order-management/)
- [Settlements](https://docs.klarna.com/payments/after-payments/settlements/settlement-files/)
- [End-to-end testing](https://docs.klarna.com/resources/developer-tools/testing-payments/test-cases/)
- [Prepare for go live](https://docs.klarna.com/resources/developer-tools/testing-payments/go-live-checklist/)