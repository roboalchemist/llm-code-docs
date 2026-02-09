# Integrate Card Payments in iOS Apps

In certain countries, Apple allows apps to link to an external website for processing payments. Use these guides to learn on how to enable this type of flow using PayPal.

Please refer to this repository for sample integration: [https://github.com/paypal-examples/paypal-ios-sdk-demo-app](https://github.com/paypal-examples/paypal-ios-sdk-demo-app)

Accept PayPal, credit, and debit card payments in a web or native experience using the PayPal Mobile iOS SDK. Use customizable PayPal buttons with your custom checkout UI to align with your business branding. For more implementation details, see the [PayPal GitHub repository](https://github.com/paypal/paypal-ios/).

## Know before you code

### You need a developer account to get sandbox credentials

PayPal uses the following REST API credentials, which you can get from the developer dashboard:

- **Client ID**: Authenticates your account with PayPal and identifies an app in your sandbox.
- **Client secret**: Authorizes an app in your sandbox. Keep this secret safe and don't share it.

### You'll need both PayPal and third-party tools

You need a combination of PayPal and third-party tools:

- [iOS SDK](https://github.com/paypal/paypal-ios/): Adds PayPal-supported payment methods for iOS.
- [Orders REST API](/docs/api/orders/v2/): Create, update, retrieve, authorize, and capture orders.

### Explore PayPal APIs with Postman

You can use Postman to explore and test PayPal APIs. Learn more in our [Postman guide](/api/rest/postman).

## Before you begin

### Check your account setup for advanced card payments

This integration requires a sandbox business account with the Advanced Credit and Debit Card Payments capability. Your account should automatically have this capability.

To confirm that Advanced Credit and Debit Card Payments are enabled for you, check your sandbox business account as follows:

- Log into the [**PayPal Developer Dashboard**](/dashboard/) , toggle **Sandbox** , and go to **Apps & Credentials** .
- In **REST API apps** , select the name of your app.
- Go to **Features** \> **Accept payments** .
- Select the **Advanced Credit and Debit Card Payments** checkbox and select **Save Changes** .

**Note:** If you created a sandbox business account through [sandbox.paypal.com](https://www.sandbox.paypal.com/?_ga=1.158343865.248280996.1670866755) , and the advanced credit and debit card payments status for the account is disabled, [complete the sandbox onboarding steps](https://www.sandbox.paypal.com/bizsignup/#/checkAccount) .

### Check 3D Secure requirements

Add 3D Secure to reduce the chance of fraud and improve the payment experience by authenticating a cardholder through their card issuer.

Visit our [3D Secure](/docs/checkout/advanced/customize/3d-secure/) page to see if 3D Secure is required in your region and learn more about implementing 3D Secure in your app.

## Integrate the SDK into your app

Integrate 3 different types of payments using the PayPal Mobile SDK:

- **Card payments:** Add card fields that align with your branding.
- **PayPal native payments:** Launch a checkout page within your app, instead of a popup.
- **PayPal web payments:** A lighter integration that launches a checkout page in a browser within your app.

### Card

### Integrate with card payments

Build and customize the card fields to align with your branding.

### 1. Add card payments module to your app

Add the CardPayments package dependency for your app using **Swift Package Manager** or **CocoaPods** :

#### Swift Package Manager

- Open Xcode.
- [Follow the guide](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app) to add package dependencies to your app.
- Enter [https://github.com/paypal/paypal-ios/](https://github.com/paypal/paypal-ios/) as the repository URL.
- Select the checkbox for the CardPayments framework.

#### CocoaPods

Include PayPal/CardPayments in your Podfile:

```ruby
pod 'PayPal/CardPayments'
```

### 2. Create CardClient

A CardClient helps you attach a card to a payment.

In your iOS app:

- Use the CLIENT_ID to construct a CoreConfig .
- Construct a CardClient using your CoreConfig object.

```swift
let coreConfig = CoreConfig(clientID: "CLIENT_ID", environment: .sandbox)
let cardClient = CardClient(config: coreConfig)
```

### 3. Get Order ID

On your server:

- Create an ORDER_ID by using the [Orders v2 API](/docs/api/orders/v2) .
- Pass your ACCESS_TOKEN in the Authorization header. To get an ACCESS_TOKEN , use the [Authentication API](/api/rest/authentication/) .
- Pass the intent . You'll need to pass either AUTHORIZE or CAPTURE as the intent type. This type must match the /authorize or /capture endpoint you use to process your order.

#### Sample request

```bash
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw '{\
    "intent": "CAPTURE|AUTHORIZE",\
    "purchase_units": [{"amount": {"currency_code": "USD", "value": "5.00"}}
  ]}'
```

#### Sample response

```json
{
  "id": "ORDER_ID",
  "status": "CREATED"
}
```

When a buyer starts a payment, send the ORDER_ID from your server to your client app.

### 4. Create card request

A CardRequest object:

- Attaches a card to an ORDER_ID .
- Launches 3D Secure when a payment requires additional authentication.

#### 1. Collect card payment details

Build a card object with the buyer's card details:

```swift
let card = Card(number: "4005519200000004", expirationMonth: "01", expirationYear: "2025", securityCode: "123", cardholderName: "Jane Smith", billingAddress: Address(addressLine1: "123 Main St.", addressLine2: "Apt. 1A", locality: "City", region: "IL", postalCode: "12345", countryCode: "US"))
```

Collecting a billing address can reduce the number of authentication challenges to customers.

#### 2. Build CardRequest

Build a CardRequest with the card object and your ORDER_ID :

```swift
let cardRequest = CardRequest(orderID: "ORDER_ID", card: card, sca: .scaAlways// default value is .scaWhenRequired)
```

### 3. Set up payment delegate

Set a PayPalNativeCheckoutDelegate to listen for result notifications from the SDK:

```swift
extension MyViewController: PayPalNativeCheckoutDelegate {
    func paypal(_ payPalClient: PayPalNativeCheckoutClient, didFinishWithResult result: PayPalNativeCheckoutResult) {
        // order was approved and is ready to be captured/authorized (see step 5)
    }
    
    func paypal(_ payPalClient: PayPalNativeCheckoutClient, didFinishWithError error: CoreSDKError) {
        // handle the error by accessing `error.localizedDescription`
    }
    
    func paypalDidCancel(_ payPalClient: PayPalNativeCheckoutClient) {
        // the user canceled
    }
    
    func paypalWillStart(_ payPalClient: PayPalNativeCheckoutClient) {
        // the PayPal paysheet is about to show up. Handle loading views, spinners, etc.
    }
}
```

### 4. Listen for shipping details

When a payer chooses to use shipping details from their PayPal profile, use PayPalNativeShippingDelegate to listen for changes to their shipping address or shipping method.

You can only implement PayPalNativeShippingDelegate if the [shipping_preference](/docs/api/orders/v2/#definition-experience_context_base) in the order ID is set to GET_FROM_FILE.

**Note:** Skip this step if you created your order ID with shipping_preference set to NO_SHIPPING or SET_PROVIDED_ADDRESS .

Set a shippingDelegate on the PayPalNativeCheckoutClient to send notifications to your app when the user updates their shipping address or shipping method.

```swift
extension MyViewModel: PayPalNativeShippingDelegate {
    func setup() {
        payPalNativeClient.delegate = self
        payPalNativeClient.shippingDelegate = self
    }
    
    func paypal(_ payPalClient: PayPalNativeCheckoutClient, didShippingAddressChange shippingAddress: PayPalNativeShippingAddress, withAction shippingActions: PayPalNativePaysheetActions) {
        // called when the user updates their chosen shipping address
        // you must call shippingActions.approve() or shippingActions.reject() in this callback
        shippingActions.approve()
        
        // OPTIONAL: you can optionally patch your order. Once complete, call shippingActions.approve() if successful or shippingActions.reject() if not.
    }
    
    func paypal(_ payPalClient: PayPalNativeCheckoutClient, didShippingMethodChange shippingMethod: PayPalNativeShippingMethod, withAction shippingActions: PayPalNativePaysheetActions) {
        // called when the user updates their chosen shipping method
        // patch your order server-side with the updated shipping amount.
        // Once complete, call `shippingActions.approve()` or `shippingActions.reject()`
    }
}
```

### 5. Approve order

Submit your ORDER_ID for authorization or capture when the PayPal iOS SDK calls the onPayPalWebSuccess method on PayPalWebCheckoutListener .

Call the [authorize](/docs/api/orders/v2/#orders_authorize) endpoint of the Orders V2 API to place the money on hold:

#### Sample request: Authorize order

```bash
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER_ID/authorize' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw '{\
    "intent": "CAPTURE|AUTHORIZE",\
    "purchase_units": [{"amount": {"currency_code": "USD", "value": "5.00"}]
  }'
```

#### Sample request: Capture order

```bash
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER_ID/capture' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw '{\
    "intent": "CAPTURE|AUTHORIZE",\
    "purchase_units": [{"amount": {"currency_code": "USD", "value": "5.00"}]
  }'
```

## Fraud protection

The FraudProtection module helps you collect data about a customer's device and match it with a session identifier on your server. For more information, see [Fraud protection](/docs/checkout/advanced/customize/fraud-protection/) .

### 1. Add FraudProtection to your app

Add the FraudProtection package dependency for your app using **Swift Package Manager** or **CocoaPods** :

#### Swift Package Manager

- Open Xcode.
- [Follow the guide](https://developer.apple.com/documentation/swift_packages/adding_package_dependencies_to_your_app) to add package dependencies to your app.
- Enter [https://github.com/paypal/paypal-ios/](https://github.com/paypal/paypal-ios/) as the repository URL.
- Select the checkbox for the FraudProtection framework.

#### CocoaPods

Include PayPal/FraudProtection in your Podfile:

```ruby
pod 'PayPal/FraudProtection'
```

### 2. Create PayPalDataCollector

In your iOS app:

- Use the CLIENT_ID to construct a CoreConfig .
- Construct a PayPalDataCollector using your CoreConfig object.

```swift
let coreConfig = CoreConfig(clientID: "CLIENT_ID", environment: .sandbox)
let dataCollector = PayPalDataCollector(config: coreConfig)
```

### 3. Collect client metadata

Collect the client metadata ID before starting a payment from a mobile device:

```swift
val clientMetadataId = dataCollector.collectDeviceData()
```

Pass the result to your server, and include the client metadata ID in the payment request you send to PayPal. Don't cache or store this value.

## Go live

If you have fulfilled the requirements for accepting Advanced Credit and Debit Card Payments for your [business account](https://www.paypal.com/myaccount/bundle/business/upgrade) , review the [Move your app to production](/api/rest/production/) page to learn how to test and go live.

If this is your first time testing in a live environment, follow these steps:

- Log into the [PayPal Developer Dashboard](/dashboard/) with your PayPal business account.
- Complete [production onboarding](https://www.paypal.com/bizsignup/entry?_ga=1.171321763.248280996.1670866755) so you can process card payments with your live PayPal business account.
- Request [Advanced Credit and Debit Card Payments](https://www.paypal.com/signin/client?flow=provisionUser&country.x=US&locale.x=en_US&ga=1.95899167.248280996.1670866755) for your business account.

**Important:** The code for the integration checks eligibility requirements, so the payment card fields only display when the production request is successful.