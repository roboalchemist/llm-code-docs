# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-android/getting-started.mdx

# Pay Kit Android: Getting Started

## Prerequisites

* All integrations require a Client ID provided by Cash App (see [Deliverables: Cash App Pay Partner Engineering](/cash-app-pay-partner-api/guides/partnerships/partner-onboarding-requirements))
* To authorize payments for a specific Merchant or Brand, you'll need to [create a Merchant](/cash-app-pay-partner-api/api-reference/network-api/create-merchant) or [create a Brand](/cash-app-pay-partner-api/api-reference/network-api/create-brand) using the Cash App REST APIs.

<Note>
  One-time payments can be authorized for a Merchant, Brand, or Client. On-file payments can only be authorized for a Brand or Client.
</Note>

## General SDK information

* Minimum Android supported SDK: `21`
* Target Android SDK: `36`

## Step 1: Import the dependency

Get the latest version of the SDK from Maven.

**Gradle**

```
implementation "app.cash.paykit:core:X.Y.Z"
```

**Gradle version catalogs**

```
paykit-core = { group = "app.cash.paykit", name = "core", version.ref = "paykit" }
```

For the latest released version, check [GitHub Releases](https://github.com/cashapp/cash-app-pay-android-sdk/releases) or [Cash App Pay Android SDK on Maven Central](https://central.sonatype.com/artifact/app.cash.paykit/core/versions).

## Step 2: Create an SDK instance

<Tip>
  Use the [Sandbox environment](/cash-app-pay-partner-api/guides/technical-guides/sandbox/sandbox-overview) during the development phase and use the production environment for your actual production releases. Use the [Sandbox App](/cash-app-pay-partner-api/guides/technical-guides/sandbox/sandbox-app) to more closely simulate a production experience while on Sandbox environment. This application is optional, but highly recommended as it will simulate Cash App, and allow you to easy trigger edge-cases for testing.
</Tip>

Use `CashAppPayFactory` to create an instance of the SDK.

* During setup, specify the development environment you will use: Sandbox or Production.
* To create a new instance of the SDK, pass `client ID`. This is a required field.
* The function `createSandbox()` will create an SDK instance in the Sandbox environment.

Creating a Sandbox SDK instance:

```kotlin
val cashAppPay : CashAppPay = CashAppPayFactory.createSandbox(sandboxClientID)
```

Creating a Production SDK instance:

```kotlin
val cashAppPay : CashAppPay = CashAppPayFactory.create(clientID)
```

## Step 3: Register for state updates

To receive updates from Pay Kit, implement the `CashAppPayListener` interface.

1. The interface exposes a single function, which gets called whenever there’s an internal state change emitted by the SDK.

```kotlin
interface CashAppPayListener {
   fun cashAppPayStateDidChange(newState: CashAppPayState)
}
```

2. Register with the SDK instance you’ve created above:

```kotlin
cashAppPay.registerForStateUpdates(this)
```

3. Use the `unregister` function after you have finished using the SDK:

```kotlin
cashAppPay.unregisterFromStateUpdates()
```

### States

`CashAppPayState` is a sealed class parameter. We recommend that you use a Kotlin `when` statement when integrating with the SDK.  The following are examples of critical states:

| State                      | Description                                                                                                                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ReadyToAuthorize`         | Show a Cash App Pay button in your UI and call `authorizeCustomerRequest()` when it is tapped.                                                                                       |
| `Approved`                 | Grants are ready for your backend to use to create a payment.                                                                                                                        |
| `Declined`                 | Customer has declined the Cash App Pay authorization and must start the flow over or choose a new payment method.                                                                    |
| `CashAppPayExceptionState` | The general wrapper state for exceptions. These can range from ***integration*** errors to **network** errors. The exception states are emitted only for unrecoverable error states. |

## Step 4: Handling Deep Linking

The authorization flow brings Cash App to the foreground on the Customer’s device. After the Customer either authorizes or declines the request, your app must be returned to the foreground.

To call your app back to the foreground, [declare an incoming intent filter](https://developer.android.com/training/app-links/deep-linking#adding-filters) on your app's Android Manifest. When creating a customer request, pass a corresponding redirect URI that uses the SDK.

### Example integration

`AndroidManifest`

```xml
<intent-filter>
    <action android:name="android.intent.action.VIEW" />

    <category android:name="android.intent.category.DEFAULT" />
    <category android:name="android.intent.category.BROWSABLE" />

    <!-- Register the Cash Pay Kit redirect URI or URL. Change this accordingly in your app. -->
    <data
        android:scheme="cashapppay"
        android:host="checkout" />
  </intent-filter>
```

## Step 5: Create a Customer Request

Create a Customer Request as soon as you know the amount you want to charge or if you want to create an on-file payment request. We recommend that you create this request as soon as your checkout view controller loads, so that the Customer can authorize the request immediately.

**Note**: If you're using Afterpay SDK together with Cash App Pay SDK, the `merchantId` contained within that data is the same as `scopeId` in this context.

### Example of a One-Time Payment

To charge \$5.00 as a one-time payment, the create request call might look like this:

```kotlin
val redirectUri = "yourapp://return_path"

val oneTimePayment = OneTimeAction(currency = USD, amount = 123, scopeId = "YOUR SCOPE ID HERE")
cashAppPay.createCustomerRequest(oneTimePayment, redirectUri)
```

### Example of an On-File Payment

```kotlin
val redirectUri = "yourapp://return_path"

val onFilePayment = OnFileAction(scopeId = "YOUR SCOPE ID HERE")
cashAppPay.createCustomerRequest(onFilePayment, redirectURI)
```

### Example of a Payout

With payouts you can send money to a user's Cash App account.
For mobile development the Pay Kit SDK, the payout workflow is identical to the two above.

```kotlin
val redirectUri = "yourapp://return_path"

val onFilePayout = OnFileAction(scopeId = "YOUR SCOPE ID HERE")
cashAppPay.createCustomerRequest(onFilePayout, redirectUri)
```

## Step 6: Authorize the Customer Request

After the SDK is in the `ReadyToAuthorize` state, display the enabled Cash App Pay button. When the Customer taps the button, you can authorize the Customer Request.

**Example**

```kotlin
cashAppPay.authorizeCustomerRequest()
```

<Note>
  The Button provided by the SDK is unmanaged. It is a stylized button that isn't aware of SDK events out-of-the-box. It is the developer's responsibility to call the above method when the button is clicked and also manage any disabled and loading states.
</Note>

Your app will redirect to Cash App for authorization. When the authorization is completed, your redirect URI is called to open your app. The SDK fetches your authorized request and returns it to your callback listener as one of 2 states: `Approved` or `Declined`.

## Step 7: Pass Grants to the Backend and Create Payment

The `Approved` state contains a `Grants` list object associated with it and it can be used with the Cash App [Create Payment API](/cash-app-pay-partner-api/api-reference/network-api/create-payment). Pass these grants to your backend and call the `CreatePayment` API as a server-to-server call to complete your payment.
