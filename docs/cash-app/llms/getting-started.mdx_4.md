# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-i-os/getting-started.mdx

# Pay Kit iOS: Getting Started

## Code language

To control and modify the Pay Kit iOS SDK, you can use the Swift language or the Objective-C language. The code examples and states on this page are in Swift.

See the [Objective-C Examples and States](#objective-c-examples-and-states) section at the bottom of this page for code examples and states in Objective-C.

## Prerequisites

* All integrations require a Client ID provided by Cash App (see [Deliverables: Cash App Pay Partner Engineering](/cash-app-pay-partner-api/guides/partnerships/partner-onboarding-requirements))
* To authorize payments for a specific Merchant or Brand, you'll need to [create a Merchant](/cash-app-pay-partner-api/api-reference/network-api/create-merchant) or [create a Brand](/cash-app-pay-partner-api/api-reference/network-api/create-brand) using the Cash App REST APIs.

<Info>
  One-time payments can be authorized for a Merchant, Brand, or Client. On-file payments can only be authorized for a Brand or Client.
</Info>

## Step 1 Implement the Cash App Pay Observer Protocol

To receive updates from Pay Kit, you’ll need to implement the Cash App Pay Observer protocol. Your checkout view controller can conform to this protocol, or you can create a dedicated observer class.

The `CashAppPayObserver` protocol contains only one method:

```swift
func stateDidChange(to state: CashAppPayState) {
	// handle state changes
}
```

Your implementation should switch on the `state` parameter and respond to each of the [state changes](#states). Below is a partial implementation of the most important states.

```swift
func stateDidChange(to state: CashAppPayState) {
    switch state {
    case let .readyToAuthorize(customerRequest):
        // The customer is ready to authorize the Customer Request by deep linking in to Cash App.
        // Enable the Cash App Pay Button.
    case let .approved(request: customerRequest, grants: grants):
        // The customer has deep linked back to your App from Cash App and they approved the Customer Request!
        // The checkout is now complete.
    case let .declined(customerRequest):
        // The customer has deep linked back to your App from Cash App and the Customer Request is declined.
        // This Customer Request is in a terminal state and any subsequent actions on this Customer Request will yield an error.
        // To retry the customer will need to restart the Customer Request flow.
        // You should make sure customers can select other payment methods at this point.
    case .redirecting:
        // The customer is being redirected to Cash App you can present a loading spinner if desired.
        // NOTE: In the event that the customer does not have Cash App installed and navigates back to your app then it is
        // up to you to set a reasonable timeout after which you dismiss the loading spinner and treat the Customer Request as failed.
    case .integrationError:
        // There is an issue with the way you are transitioning between states. Refer to the documentation to ensure you are
        // moving between states in the correct order.
        // You can perform a valid transition from this state.
    case .apiError:
        // Cash App Pay API is suffering degraded performance. You can can retry your event or discard this checkout.
        // Retrying may fix the issue or reach out to Developer Support for additional help.
    case .unexpectedError:
        // This should never happen however in the event you receive this please reach out to Developer Support to diagnose the issue.
    case .networkError:
        // The Cash App Pay SDK attempts to retry network failures however in the event that a customer is unable
        // to perform their checkout due to network connectivity issues you may want to retry the checkout.
    ...
    // handle the other state changes
    ...
    }
}
```

Some of these possible states are for information only, but most drive the logic of your integration. A full list of states to handle are listed in the table below:

### States

> You must update your UI in response to these state changes.

| State              | Description                                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| `readyToAuthorize` | Show a Cash App Pay button in your UI and call `authorizeCustomerRequest()` when it is tapped.                    |
| `approved`         | Grants are ready for your backend to use to create a payment.                                                     |
| `declined`         | Customer has declined the Cash App Pay authorization and must start the flow over or choose a new payment method. |

### Terminal states

These states cannot transition further and attempting to action on a Customer Request that is in a terminal state will result in an error.

| State      | Description                                                                                                       |
| ---------- | ----------------------------------------------------------------------------------------------------------------- |
| `approved` | Grants are ready for your backend to use to create a payment.                                                     |
| `declined` | Customer has declined the Cash App Pay authorization and must start the flow over or choose a new payment method. |

<Warning>
  Customer Requests can fail for a number of reasons, such as when customer exits the flow prematurely or are declined by Cash App for risk reasons. You must respond to these state changes and be ready to update your UI appropriately.
</Warning>

### Error states

| State              | Description                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| `integrationError` | A fixable bug in your integration.                                                                      |
| `apiError`         | A degradation of Cash App Pay server APIs. Your app should temporarily hide Cash App Pay functionality. |
| `unexpectedError`  | A bug outside the normal flow. Report this bug (and what caused it) to Cash App Developer Support.      |
| `networkError`     | A networking error, likely due to poor internet connectivity.                                           |

### Informational states

| State                     | Description                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `notStarted`              | Ready for a Create Customer Request to be initiated.                                                               |
| `creatingCustomerRequest` | CustomerRequest is being created. For information only.                                                            |
| `updatingCustomerRequest` | CustomerRequest is being updated. For information only.                                                            |
| `redirecting`             | SDK is redirecting to Cash App for authorization. Show loading indicator if desired.                               |
| `polling`                 | SDK is retrieving authorized CustomerRequest. Show loading indicator if desired.                                   |
| `refreshing`              | CustomerRequest is being refreshed as a result of the AuthFlowTriggers expiring. Show loading indicator if desired |

## Step 2 Implement URL handling

To use Pay Kit iOS, Cash App must be able to call a URL that will redirect back to your app. The simplest way to accomplish this is via [Custom URL Schemes](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app), but if your app supports [Universal Links](https://developer.apple.com/ios/universal-links/) you can use those URLs as well.

Choose a unique scheme for your application and register it in Xcode from the **Info** tab of your application’s Target. For example, the TipMyCAP application that exercises the SDK functionality configures a scheme as follows:

![configure\_scheme.png](https://files.buildwithfern.com/cash-app.docs.buildwithfern.com/2026-02-13T14:24:26.350Z/cash-api-docs/assets/images/configure_scheme.png)

You’ll pass a URL that uses this scheme (or a Universal Link your app handles) into the `createCustomerRequest()` method that starts the authorization process.

When your app is called back by Cash App, post the `CashAppPay.RedirectNotification` from your `AppDelegate` or `SceneDelegate`, and the SDK will handle the rest:

```swift
import UIKit
import PayKit

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
    func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
        if let url = URLContexts.first?.url {
            NotificationCenter.default.post(
                name: CashAppPay.RedirectNotification,
                object: nil,
                userInfo: [UIApplication.LaunchOptionsKey.url : url]
            )
        }
    }
}
```

<Error title="Do Not Skip This Step!">
  This step is vital to ensuring the integration works correctly! You may find that in testing environments this step is not required however in production environments you will see a high number of customers not being able to complete their checkout because the SDK never enters the polling state.
</Error>

## Step 3 Instantiate Pay Kit iOS

When you’re ready to authorize a payment using Cash App Pay,

1. Instantiate the SDK with your Client ID.
2. The SDK defaults to point to the `.production` endpoint. For development, set the endpoint to `.sandbox`.
3. Add your observer to the SDK.

For example, from your checkout view controller that implements the `CashAppPayObserver` protocol, you might instantiate the SDK to be:

```swift
private let sandboxClientID = "YOUR_CLIENT_ID"
private lazy var sdk: CashAppPay = {
    let sdk = CashAppPay(clientID: sandboxClientID, endpoint: .sandbox)
    sdk.addObserver(self)
    return sdk
}()
```

<Warning title="Make Sure You Retain The SDK!">
  You must strongly retain the SDK otherwise you will never recieve state changes.
</Warning>

## Step 4 Create a Customer Request

You can create a customer request as soon as you know the amount you’d like to charge or if you'd like to create an on-file payment request. You must create this request as soon as your checkout view controller loads, so that your customer can authorize the request without delay.

### Example

To charge \$5.00, your `createCustomerRequest` call might look like this:

```swift
private let sandboxBrandID = "YOUR_BRAND_ID"

override func viewDidLoad() {
    super.viewDidLoad()
    // load view hierarchy
    sdk.createCustomerRequest(
        params: CreateCustomerRequestParams(
            actions: [
                .oneTimePayment(
                    scopeID: brandID,
                    money: Money(amount: 500, currency: .USD)
                )
            ],
            channel: .IN_APP,
            redirectURL: URL(string: "tipmycap://callback")!,
            referenceID: nil,
            metadata: nil
        )
    )
}
```

Your Observer's state changes to `.creatingCustomerRequest`, then `.readyToAuthorize` with the created `CustomerRequest` structure as an associated value.

## Step 5 Authorize the Customer Request

Once the SDK is in the `.readyToAuthorize` state, you can store the associated `CustomerRequest` and display a Cash App Pay button. When the customer taps the button, you can authorize the customer request.

### Example

```swift
@objc func cashAppPayButtonTapped() {
    sdk.authorizeCustomerRequest(request)
}
```

Your app will redirect to Cash App for authorization. When authorization is completed, your redirect URL will be called and the `RedirectNotification` will post. Then the SDK will fetch your authorized request and return it to your Observer, as part of the change to the `.approved` state.

### Unhappy Path

If the Customer does not have Cash App installed on their device then they will redirect to a webpage prompting them to download Cash App. In the event the customer does not download Cash App, then the SDK will remain in the `polling` state. The SDK does not handle this edge case and instead it is up to the implementor to set a reasonable timeout and treat the checkout as failed once that timeout is exceeded. It is suggested to dismiss any loading states and restart the Cash App Pay flow as to not block the customer from checking out.

## Step 6 Pass Grants to the Backend and Create Payment

The approved `CustomerRequest` will have `Grants` associated with it that can be used with Cash App's [Create Payment](/cash-app-pay-partner-api/api-reference/network-api/create-payment) API. Pass those grants to your backend and call the Create Payment API as a server-to-server call to complete your payment.
