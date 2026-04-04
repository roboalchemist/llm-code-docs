# Integrate card payments in Android

Accept PayPal, credit, and debit card payments in a web or native experience using the PayPal Mobile Android SDK. Use customizable PayPal buttons with your custom checkout UI to align with your business branding. For more implementation details, see the [PayPal GitHub repository](https://github.com/paypal/paypal-android/) .

## Know before you code

You need a [developer account](https://developer.paypal.com/tools/sandbox/accounts/) to get sandbox credentials:

- PayPal uses REST API credentials which you can get from the [developer dashboard](https://developer.paypal.com/dashboard/).
- Client ID: Authenticates your account with PayPal and identifies an app in your sandbox.
- Client secret: Authorizes an app in your sandbox. Keep this secret safe and don’t share it.

Read [Get started with PayPal APIs](https://developer.paypal.com/api/rest/) for more information.

You need a combination of PayPal and third-party tools:

- [Android SDK](https://github.com/paypal/paypal-android): Adds PayPal-supported payment methods for Android.
- [Orders REST API](https://developer.paypal.com/docs/api/orders/v2/): Create, update, retrieve, authorize, and capture orders.

Use Postman to explore and test PayPal APIs.

## Before you begin your integration

### Check your account setup for advanced card payments

This integration requires a sandbox business account with the Advanced Credit and Debit Card Payments capability. Your account should automatically have this capability.

To confirm that Advanced Credit and Debit Card Payments are enabled for you, check your sandbox business account as follows:

- Log into the [**PayPal Developer Dashboard**](https://developer.paypal.com/dashboard/) , toggle **Sandbox** , and go to **Apps & Credentials** .
- In **REST API apps** , select the name of your app.
- Go to **Features** \> **Accept payments** . Select the **Advanced Credit and Debit Card Payments** checkbox and select **Save Changes** .

**Note:** If you created a sandbox business account through [sandbox.paypal.com](https://www.sandbox.paypal.com/?_ga=1.158343865.248280996.1670866755) , and the advanced credit and debit card payments status for the account is disabled, [complete the sandbox onboarding steps](https://www.sandbox.paypal.com/bizsignup/#/checkAccount) .

### Check 3D Secure requirements

Add 3D Secure to reduce the chance of fraud and improve the payment experience by authenticating a cardholder through their card issuer.

Visit our [3D Secure](https://developer.paypal.com/docs/checkout/advanced/customize/3d-secure/) page to see if 3D Secure is required in your region and learn more about implementing 3DS in your app.

The PayPal Mobile SDK is available through Maven Central. Add the mavenCentral repository to the build.gradle file of your project root:

#### **`Integrate the SDK into your app Demo`**

```javascript
allprojects {
  repositories {
    mavenCentral()
  }
}
```

### Snapshot builds

You can also use snapshot builds to test upcoming features before release. To include a snapshot build:

#### 1. Add snapshots repository

Add the snapshots repository to the build.gradle file of your project root.

```javascript
allprojects {
  repositories {
    mavenCentral()
    maven {
      url 'https://oss.sonatype.org/content/repositories/snapshots/'
    }
  }
}
```

#### 2. Add snapshot to dependencies

Then, add a snapshot build by adding -SNAPSHOT to the current dependency version. For example, if you want to add a snapshot build for CardPayments , add the following:

```javascript
dependencies {
  implementation 'com.paypal.android:card-payments:CURRENT-VERSION-SNAPSHOT'
}
```

### Payment integrations

Integrate 3 different types of payments using the PayPal Mobile SDK:

- **Card payments:** Add card fields that align with your branding.
- **PayPal native payments:** Launch a checkout page within your app, instead of a popup.
- **PayPal web payments:** A lighter integration that launches a checkout page in a browser within your app.

### Card

### Integrate with card payments

Build and customize the card fields to align with your branding.

#### 1. Add card payments module to your app

Add the card-payments package dependency in your app's build.gradle file:

```javascript
dependencies {
  implementation "com.paypal.android:card-payments:CURRENT-VERSION"
}
```

### 2. Create CardClient

A CardClient helps you attach a card to a payment.

In your Android app:

- Use the CLIENT_ID to construct a CoreConfig .
- Construct a CardClient using your CoreConfig object.

```javascript
val config = CoreConfig("CLIENT_ID", environment = Environment.SANDBOX)
val cardClient = CardClient(config)
```

### 3. Get Order ID

On your server:

- Create an ORDER_ID by using the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/).
- Pass your ACCESS_TOKEN in the Authorization header. To get an ACCESS_TOKEN , use the [Authentication API](https://developer.paypal.com/api/rest/authentication/).

- Pass the intent . You'll need to pass either AUTHORIZE or CAPTURE as the intent type. This type must match the /authorize or /capture endpoint you use to process your order.

#### **`Sample request`**

```javascript
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw '{
    "intent": "CAPTURE|AUTHORIZE",
    "purchase_units": [
      {
        "amount": {
          "currency_code": "USD",
          "value": "5.00"
        }
      }
    ]
  }'
```

#### **`Sample response`**

```javascript
{
  "id":"ORDER_ID",
  "status":"CREATED"
}
```

When a buyer starts a payment, send the ORDER_ID from your server to your client app.

### 4. Create card request

A CardRequest object:

- Attaches a card to an ORDER_ID .
- Launches 3D Secure when a payment requires additional authentication.

#### 1. Collect card payment details

Build a card object with the buyer's card details:

```javascript
val card = Card(
  number = "4005519200000004",
  expirationMonth = "01",
  expirationYear = "2025",
  securityCode = "123",
  billingAddress = Address(
    streetAddress = "123 Main St.",
    extendedAddress = "Apt. 1A",
    locality = "Anytown",
    region = "CA",
    postalCode = "12345",
    countryCode = "US"
  )
)
```

Collecting a billing address can reduce the number of authentication challenges to customers.

#### 2. Build CardRequest

Build a CardRequest with the card object and your ORDER_ID :

```javascript
val cardRequest  = CardRequest(
  orderID = "ORDER_ID",
  card = card,
  returnUrl = "myapp://return_url", // custom URL scheme needs to be configured in AndroidManifest.xml
  sca = SCA.SCA_ALWAYS // default value is SCA.SCA_WHEN_REQUIRED
)
```

### 3. Set up your app for browser switching

The sca challenge launches in a browser within your application. Your app needs to handle the browser switch between the sca challenge and the checkout page. Set up a return URL that returns to your app from the browser.

#### 4. Create a return URL

Provide a returnUrl so the browser returns to your application after the sca challenge finishes.

The myapp:// portion of the returnUrl is a custom URL scheme that you need to register in your app's AndroidManifest.xml .

#### 5. Add card payment activity to the Android manifest

Update your app's AndroidManifest.xml with details about the card payment activity that will return the user to your app after completing the SCA check. Include the following elements:

- Set the activity launchMode to singleTop .
- Set the android:scheme on the Activity that will be responsible for handling the deep link back into the app.
- Add an intent-filter .
- Register the myapp:// custom URL scheme in the intent-filter .

Note: android:exported is required if your app compile SDK version is API 31 (Android 12) or later.

```xml
<activity android:name=".MyCardPaymentActivity" android:launchMode="singleTop" android:exported="true">
  ...
  <intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <data android:scheme="myapp" />
  </intent-filter>
</activity>
```

### 6. Connect the card payment activity

Add onNewIntent to your activity:

```javascript
override fun onNewIntent(newIntent: Intent?) {
  super.onNewIntent(intent)
  intent = newIntent
}
```

### 5. Approve order

After your CardRequest has the card details, call cardClient.approveOrder() to process the payment.

```javascript
class MyCardPaymentActivity: FragmentActivity {
  fun cardCheckoutTapped(cardRequest: CardRequest) {
    cardClient.approveOrder(this, cardRequest)
  }
}
```

### 6. Handle payment result scenarios

Set up your ApproveOrderListener to handle successful payments, errors, cancellations, and 3D Secure transaction flows.

```javascript
class MyCardPaymentActivity: FragmentActivity, ApproveOrderListener {
  fun cardCheckoutTapped(cardRequest: CardRequest) {
    val result = cardClient.approveOrder(this, cardRequest)
  }
  fun setupCardClient() {
    cardClient.listener = this
  }
  fun onApproveOrderSuccess(result: CardResult) {
    // order was approved and is ready to be captured/authorized (see step 6)
  }
  fun onApproveOrderFailure(error: PayPalSDKError) {
    // inspect 'error' for more information
  }
  fun onApproveOrderCanceled() {
    // 3D Secure flow was canceled
  }
  fun onApproveOrderThreeDSecureWillLaunch() {
    // 3D Secure flow will launch
  }
  fun onApproveOrderThreeDSecureDidFinish() {
    // 3D Secure auth did finish successfully
  }
}
```

### 7. Authorize and capture order

Submit your ORDER_ID for authorization or capture when the PayPal Android SDK calls the onApproveOrderSuccess method.

Call the [authorize](https://developer.paypal.com/docs/api/orders/v2/#orders_authorize) endpoint of the Orders V2 API to place the money on hold:

#### Sample request: Authorize order

```javascript
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw '{
    "intent": "CAPTURE|AUTHORIZE",
    "purchase_units": [
      {
        "amount": {
          "currency_code": "USD",
          "value": "5.00"
        }
      }
    ]
  }'
```

Call the [capture](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) endpoint of the Orders V2 API to capture the money immediately:

#### Sample request: Capture order

```javascript
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER_ID/capture' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw ''
```

## Web payments

### PayPal Web Payments

Integrate PayPalWebPayments to add a lighter checkout integration to your app. The checkout experience is launched in a browser within your application, reducing the size of the SDK.

Follow these steps to integrate PayPalWebPayments :

### 1. Add PayPalWebPayments to your app

Add the paypal-web-payments package dependency in your app's build.gradle file:

```javascript
dependencies {
  implementation "com.paypal.android:paypal-web-payments:CURRENT-VERSION"
}
```

### 2. Set up your app for browser switching

PayPalWebPayments launches a checkout page in a browser within your application. Your app needs to handle the browser switch between the checkout page and your app. Set up a return URL that returns to your app from the browser.

Update your app's AndroidManifest.xml with details about the card payment activity that will return the user to your app after completing the payment. Include the following elements:

- Set the activity launchMode to singleTop .
- Set the android:scheme on the Activity that will be responsible for handling the deep link back into the app.
- Add an intent-filter .
- Register the myapp:// custom URL scheme in the intent-filter .

Note: android:exported is required if your app compile SDK version is API 31 (Android 12) or later.

```xml
<activity android:name=".MyCardPaymentActivity" android:launchMode="singleTop" android:exported="true">
  ...
  <intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <data android:scheme="myapp" />
  </intent-filter>
</activity>
```

### 3. Create PayPalWebCheckoutClient

Use the following steps to set up the PayPal Native Checkout client for your app:

#### 1. Construct CoreConfig

In your Android app, use the CLIENT_ID to construct a CoreConfig .

```javascript
val config = CoreConfig("CLIENT_ID", environment = Environment.SANDBOX)
val dataCollector = PayPalDataCollector(coreConfig = coreConfig)
```

#### 2. Create return URL

Set a return URL using the custom scheme you configured in the ActivityManifest.xml :

```javascript
val returnUrl = "custom-url-scheme"
```

#### 3. Create web checkout request

Create a PayPalWebCheckoutClient to approve an order with a PayPal payment method:

```javascript
val payPalWebCheckoutClient = PayPalWebCheckoutClient(requireActivity(), config, returnUrl)
```

#### 4. Set up payment listener

Set a PayPalWebCheckoutListener on the PayPalWebCheckoutClient to receive payment flow callbacks:

```javascript
payPalWebCheckoutClient.listener = object : PayPalWebCheckoutListener {
  override fun onPayPalWebSuccess(result: PayPalWebCheckoutResult) {
    // order was approved and is ready to be captured/authorized (see step 7)
  }
  override fun onPayPalWebFailure(error: PayPalSDKError) {
    // inspect 'error' for more information
  }
  override fun onPayPalWebCanceled() {
    // 3D Secure flow was canceled
  }
  override fun onPayPalWebThreeDSecureWillLaunch() {
    // 3D Secure flow will launch
  }
  override fun onPayPalWebThreeDSecureDidFinish() {
    // 3D Secure auth did finish successfully
  }
}
```

### 5. Get Order ID

On your server:

- Create an ORDER_ID by using the [Orders v2 API](https://developer.paypal.com/docs/api/orders/v2/).
- Pass your ACCESS_TOKEN in the Authorization header. To get an ACCESS_TOKEN , use the [Authentication API](https://developer.paypal.com/api/rest/authentication/).

- Pass the intent . You'll need to pass either AUTHORIZE or CAPTURE as the intent type. This type must match the /authorize or /capture endpoint you use to process your order.

#### **`Sample request`**

```javascript
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw '{
    "intent": "CAPTURE|AUTHORIZE",
    "purchase_units": [
      {
        "amount": {
          "currency_code": "USD",
          "value": "5.00"
        }
      }
    ]
  }'
```

#### **`Sample response`**

```javascript
{
  "id":"ORDER_ID",
  "status":"CREATED"
}
```

When a buyer starts a payment, send the ORDER_ID from your server to your client app.

### 6. Create web checkout request

Configure your PayPalWebCheckoutRequest with the ORDER_ID . You can also specify one of the following funding sources for your order: PayPal (default), PayLater , or PayPalCredit .

```javascript
val payPalWebCheckoutRequest = PayPalWebCheckoutRequest("ORDER_ID", fundingSource = PayPalWebCheckoutFundingSource.PAYPAL)
```

### 7. Approve order

Call payPalWebCheckoutClient.start() to process the payment.

```javascript
class MyCardPaymentActivity: FragmentActivity {
  fun cardCheckoutTapped(cardRequest: CardRequest) {
    payPalWebCheckoutClient.start(cardRequest)
  }
}
```

### 8. Handle payment result scenarios

Set up your ApproveOrderListener to handle successful payments, errors, cancellations, and 3D Secure transaction flows.

```javascript
class MyCardPaymentActivity: FragmentActivity, ApproveOrderListener {
  fun cardCheckoutTapped(cardRequest: CardRequest) {
    val result = cardClient.approveOrder(this, cardRequest)
  }
  fun setupCardClient() {
    cardClient.listener = this
  }
  fun onApproveOrderSuccess(result: CardResult) {
    // order was approved and is ready to be captured/authorized (see step 6)
  }
  fun onApproveOrderFailure(error: PayPalSDKError) {
    // inspect 'error' for more information
  }
  fun onApproveOrderCanceled() {
    // 3D Secure flow was canceled
  }
  fun onApproveOrderThreeDSecureWillLaunch() {
    // 3D Secure flow will launch
  }
  fun onApproveOrderThreeDSecureDidFinish() {
    // 3D Secure auth did finish successfully
  }
}
```

For more information, visit the [Update order](https://developer.paypal.com/docs/api/orders/v2/#orders_patch) endpoint of the Orders v2 API.

## Fraud protection

### Protect from fraud

The FraudProtection module helps you collect data about a customer's device and match it with a session identifier on your server. For more information, see [Fraud protection](https://developer.paypal.com/docs/checkout/advanced/customize/fraud-protection/) .

**Note:** If you integrated 3D Secure before June 2020, the liabilityShifted , authenticationStatus , and AuthenticationReason parameters are no longer supported, but continue to work on the server.

### 1. Add FraudProtection to your app

Add the fraud-protection package dependency in your app's build.gradle file:

```javascript
dependencies {
  implementation "com.paypal.android:fraud-protection:CURRENT-VERSION"
}
```

### 2. Create PayPalDataCollector

In your Android app:

- Use the CLIENT_ID to construct a CoreConfig .
- Construct a PayPalDataCollector using your CoreConfig object.

```javascript
val config = CoreConfig("CLIENT_ID", environment = Environment.SANDBOX)
val dataCollector = PayPalDataCollector(coreConfig = coreConfig)
```

### 3. Collect client metadata

Collect the client metadata ID before starting a payment from a mobile device:

**Important:** User Data Consent Merchant applications are responsible for collecting user data consent. If your app has obtained consent from the user to collect location data in compliance with [Google Play Developer Program policies](https://support.google.com/googleplay/android-developer/answer/10144311#personal-sensitive) , set hasUserLocationConsent to true . This flag enables PayPal to collect necessary information required for Fraud Detection and Risk Management.

**Merchant App Disclosure** Merchant applications may be required to display a disclosure before collecting user location data in accordance with Google’s [Best practices for prominent disclosures and consent](https://support.google.com/googleplay/android-developer/answer/11150561?hl=en&ref_topic=12797379&sjid=10421482417907285178-NC) . By setting hasUserLocationConsent to true , your app is enabled to share device location data with a third party (PayPal) for Fraud Detection and Risk Management.

```javascript
val dataCollectorRequest = PayPalDataCollectorRequest(hasUserLocationConsent)
val clientMetadataId = payPalDataCollector.collectDeviceData(context, dataCollectorRequest)
```

Pass the result to your server, and include the client metadata ID in the payment request you send to PayPal. Don't cache or store this value.

### 4. Set up your app for browser switching

The sca challenge launches in a browser within your application. Your app needs to handle the browser switch between the sca challenge and the checkout page. Set up a return URL that returns to your app from the browser.

#### 5. Create a return URL

Provide a returnUrl so the browser returns to your application after the sca challenge finishes.

The myapp:// portion of the returnUrl is a custom URL scheme that you need to register in your app's AndroidManifest.xml .

#### 6. Add card payment activity to the Android manifest

Update your app's AndroidManifest.xml with details about the card payment activity that will return the user to your app after completing the SCA check. Include the following elements:

- Set the activity launchMode to singleTop .
- Set the android:scheme on the Activity that will be responsible for handling the deep link back into the app.
- Add an intent-filter .
- Register the myapp:// custom URL scheme in the intent-filter .

Note: android:exported is required if your app compile SDK version is API 31 (Android 12) or later.

```xml
<activity android:name=".MyCardPaymentActivity" android:launchMode="singleTop" android:exported="true">
  ...
  <intent-filter>
    <action android:name="android.intent.action.VIEW" />
    <data android:scheme="myapp" />
  </intent-filter>
</activity>
```

### 7. Connect the card payment activity

Add onNewIntent to your activity:

```javascript
override fun onNewIntent(newIntent: Intent?) {
  super.onNewIntent(intent)
  intent = newIntent
}
```

### 5. Approve order

Submit your ORDER_ID for authorization or capture when the PayPal Android SDK calls the onApproveOrderSuccess method.

Call the [authorize](https://developer.paypal.com/docs/api/orders/v2/#orders_authorize) endpoint of the Orders V2 API to place the money on hold:

#### Sample request: Authorize order

```javascript
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw '{
    "intent": "CAPTURE|AUTHORIZE",
    "purchase_units": [
      {
        "amount": {
          "currency_code": "USD",
          "value": "5.00"
        }
      }
    ]
  }'
```

Call the [capture](https://developer.paypal.com/docs/api/orders/v2/#orders_capture) endpoint of the Orders V2 API to capture the money immediately:

#### Sample request: Capture order

```javascript
curl --location --request POST 'https://api-m.sandbox.paypal.com/v2/checkout/orders/ORDER_ID/capture' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer ACCESS_TOKEN' \
  --data-raw ''
```

## Go live

If you have fulfilled the requirements for accepting Advanced Credit and Debit Card Payments for your [business account](https://www.paypal.com/myaccount/bundle/business/upgrade) , review the [Move your app to production](https://www.paypal.com/api/rest/production/) page to learn how to test and go live.

If this is your first time testing in a live environment, follow these steps:

- Log into the [PayPal Developer Dashboard](https://developer.paypal.com/dashboard/) with your PayPal business account.
- Complete [production onboarding](https://www.paypal.com/bizsignup/entry?_ga=1.171321763.248280996.1670866755) so you can process card payments with your live PayPal business account.
- Request [Advanced Credit and Debit Card Payments](https://www.paypal.com/signin/client?flow=provisionUser&country.x=US&locale.x=en_US&ga=1.95899167.248280996.1670866755) for your business account.

**Note:** The code for the integration checks eligibility requirements, so the payment card fields only display when the production request is successful.