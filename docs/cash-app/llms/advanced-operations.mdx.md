# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-i-os/advanced-operations.mdx

# Pay Kit iOS: Advanced Operations

## Analytics

If you want to monitor your integration to ensure customers are appropritately transitioning through the Cash App Pay funnel then you can track a metric in each of the `CashAppPayState`'s and build a funnel using the Customer Request ID.

## (iOS only) Pay Kit mobile redirect limitations

iOS has a limitation that causes an interstitial page to show, requiring an extra user interaction. This happens if the time taken between the user clicking the Cash App Pay button and Pay Kit attempting to deep link exceeds 1 second.

### Issue Description

[Universal linking](https://developer.apple.com/ios/universal-links/) on iOS has a limitation based on an "interaction threshold". A customer input (for example, touch, click) is required for a universal link to open an app. If the linking is done programmatically, by updating `location.href` for example, there is a limit of 1 second between the interaction and the actual redirection for a universal link to properly deep link into an app. If the limit is exceeded, the universal link is opened as a normal webpage instead.

When Pay Kit is managing the Cash App Pay button, the 1 second threshold will never be exceeded. However, when using the `manage` option to control Pay Kit manually, you must take care that the 1 second threshold is not hit.

Examples for how this may happen are: adding additional API calls after the Customer has interacted with the button but before Pay Kit is called, or running other types of form validation. Any such work should be done prior to the customer interacting with the button to avoid any extra work that might exceed the 1 second threshold which will cause the interstitial to show.

## Objective-C Examples and States

### General Information

| **Swift**                         | **Objective-C**                              |
| --------------------------------- | -------------------------------------------- |
| `CashAppPayObserver`              | `CAPCashAppPayObserver`                      |
| `CashAppPay.RedirectNotification` | `[CAPCashAppPay RedirectNotification]`       |
| `.production / .sandbox`          | `CAPEndpointProduction / CAPEndpointSandbox` |

### Step 1

[Step 1 Implement the Cash App Pay Observer Protocol](#step-1-implement-the-cash-app-pay-observer-protocol)

The `CashAppPayObserver` protocol contains only one method:

Swift code:

```swift
func stateDidChange(to state: CashAppPayState) {
    // handle state changes
}
```

The `CAPCashAppPayObserver` protocol contains only one method:

Objective-C code:

```Objective-C
-  (void)stateDidChangeTo:(CAPCashAppPayState *)state {
    // handle state changes
}
```

**States**

> You must update your UI in response to these state changes.

| **Swift**          | **Objective-C**                      |
| ------------------ | ------------------------------------ |
| `readyToAuthorize` | `CAPCashAppPayStateReadyToAuthorize` |
| `approved`         | `CAPCashAppPayStateApproved`         |
| `declined`         | `CAPCashAppPayStateDeclined`         |

### Terminal states

| **Swift**  | **Objective-C**              |
| ---------- | ---------------------------- |
| `approved` | `CAPCashAppPayStateApproved` |
| `declined` | `CAPCashAppPayStateDeclined` |

**Error States**

| **Swift**          | **Objective-C**                      |
| ------------------ | ------------------------------------ |
| `integrationError` | `CAPCashAppPayStateIntegrationError` |
| `apiError`         | `CAPCashAppPayStateApiError`         |
| `unexpectedError`  | `CAPCashAppPayStateUnexpectedError`  |
| `networkError`     | `CAPCashAppPayStateNetworkError`     |

### Informational states

| **Swift**                 | **Objective-C**                             |
| ------------------------- | ------------------------------------------- |
| `notStarted`              | `CAPCashAppPayStateNotStarted`              |
| `creatingCustomerRequest` | `CAPCashAppPayStateCreatingCustomerRequest` |
| `updatingCustomerRequest` | `CAPCashAppPayStateUpdatingCustomerRequest` |
| `redirecting`             | `CAPCashAppPayRedirecting`                  |
| `polling`                 | `CAPCashAppPayStatePolling`                 |
| `refreshing`              | `CAPCashAppPayStateRefreshing`              |
| `redirecting`             | `CAPCashAppPayStateRedirecting`             |

### Step 2

[Step 2 Implement URL Handling](#step-2-implement-url-handling)

When your app is called back by Cash App, post the `CashAppPay.RedirectNotification` from your `AppDelegate` or `SceneDelegate`, and the SDK will handle the rest:

Swift code:

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

When your app is called back by Cash App, post the `[CashAppPay.RedirectNotification]` from your `AppDelegate` or `SceneDelegate`, and the SDK will handle the rest:

Objective-C code:

```Objective-C
@import PayKit;

- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
    if ([URLContexts count] > 0) {
        NSURL *url = ((UIOpenURLContext*)[[URLContexts allObjects] firstObject]).URL;
        [[NSNotificationCenter defaultCenter]
         postNotificationName:[CAPCashAppPay RedirectNotification]
         object:NULL
         userInfo:@{UIApplicationLaunchOptionsURLKey: url}
        ];
    }
}
```

<Error title="Do Not Skip This Step!">
  This step is vital to ensuring the inetgration works correctly! You may find that in testing environments this step is not required however in production environments you will see a high number of customers not being able to complete their checkout because the SDK never enters the polling state.
</Error>

### Step 3

[Step 3 Instantiate Pay Kit iOS](#step-3-instantiate-pay-kit-ios)

For example, from your checkout view controller that implements the `CashAppPayObserver` protocol, you might instantiate the SDK to be:

Swift code:

```swift
private let sandboxClientID = "YOUR_CLIENT_ID"
private lazy var sdk: CashAppPay = {
    let sdk = CashAppPay(clientID: sandboxClientID, endpoint: .sandbox)
    sdk.addObserver(self)
    return sdk
}()
```

<Warning title="Make Sure You Retain The SDK!">You must strongly retain the SDK otherwise you will never recieve state changes.</Warning>
For example, from your checkout view controller that implements the `CashAppPayObserver` protocol, you might instantiate the SDK to be:

Objective-C code:

```Objective-C
In the .h file:
@property (nonatomic, strong) CAPCashAppPay *sdk;

In the .m file:
NSString *sandboxClientID = @"YOUR_CLIENT_ID";
self.sdk = [[CAPCashAppPay alloc]initWithClientID:sandboxClientID endpoint:CAPEndpointSandbox];
[_sdk addObserver:self];
```

### Step 4

[Step 4 Create a Customer Request](#step-4-create-a-customer-request)

To charge \$5.00, your `createCustomerRequest` call might look like this:

Swift code:

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

To charge \$5.00, your `createCustomerRequestWithParams` call might look like this:

Objective-C code:

```Objective-C
- (void)viewDidLoad {
    [super viewDidLoad];
    // load view hierarchy
    NSString *sandboxBrandID = @"YOUR_BAND_ID";
    CAPMoney *oneDollar = [[CAPMoney alloc] initWithAmount:500 currency:CAPCurrencyUSD];
    [_sdk createCustomerRequestWithParams:[
        [CAPCreateCustomerRequestParams alloc]
        initWithActions:@[[CAPPaymentAction oneTimePaymentWithScopeID:sandboxBrandID money:oneDollar]]
        redirectURL:[[NSURL alloc]initWithString:@"paykitdemo://callback"]
        referenceID:NULL
        metadata:NULL
    ]
    ];
}
```

### Step 5

[Step 5 Authorize the Customer Request](#step-5-authorize-the-customer-request)

When the customer taps the button, you can authorize the customer request.

**Example**

Swift code:

```swift
@objc func cashAppPayButtonTapped() {
    sdk.authorizeCustomerRequest(request)
}
```

When the customer taps the button, you can authorize the customer request.

**Example**

Objective-C code:

```Objective-C
- (IBAction)cashAppPayButtonTapped:(id)sender {
    [_sdk authorizeCustomerRequest:request]
}

```

### Unhappy Path

If the Customer does not have Cash App installed on their device then they will redirect to a webpage prompting them to download Cash App. In the event the customer does not download Cash App, then the SDK will remain in the `polling` state. The SDK does not handle this edge case and instead it is up to the implementor to set a reasonable timeout and treat the checkout as failed once that timeout is exceeded. It is suggested to dismiss any loading states and restart the Cash App Pay flow as to not block the customer from checking out.
