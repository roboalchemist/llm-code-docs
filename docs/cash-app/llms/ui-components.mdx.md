# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/pay-kit-sdk/pay-kit-i-os/ui-components.mdx

# Pay Kit iOS: UI Components

`PayKitUI` provides an unmanaged `CashAppPayButton` and a `CashAppPaymentMethod` view in both `UIKit` and `SwiftUI`.

These views accept a `SizingCategory` to specify the preferred size of the view within your app. They also support light/dark themes by default.
These views must be used as-is, without modification.

### CashAppPayButton

This is an example of `CashAppPayButton`:

<img noZoom img width="368" alt="image" src="https://user-images.githubusercontent.com/8743061/216639753-159f2b3e-21be-4113-8a92-fd77e93acd12.png" />

You can use the following example for instantiating the button:

```swift
let button = CashAppPayButton(size: .small, onClickHandler: {})
```

### CashAppPaymentMethod

This is an example of `CashAppPaymentMethod`:

<img noZoom img width="250" alt="image" src="https://user-images.githubusercontent.com/8743061/216639415-49591e1e-046e-49a0-b480-b6249394254d.png" />

You can use the following example for instantiating the button:

```swift
let paymentMethod = CashAppPaymentMethod(size: .small)
paymentMethod.cashTag = "$jack"
```
