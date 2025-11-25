# Source: https://dub.co/docs/sdks/client-side-mobile/installation-guides/swift.md

# Swift

> How to add the Dub iOS SDK to your Swift project

## Prerequisites

Before you get started, make sure you have the following:

1. Obtain your [publishable key](/api-reference/publishable-keys) (`DUB_PUBLISHABLE_KEY`) from
   your [workspace's Analytics settings page](https://app.dub.co/settings/analytics) and select
   your domain (`DUB_DOMAIN`) from your [workspace's Custom Domains settings page](https://app.dub.co/links/domains).

2. (Optional) If you plan to track conversions, follow the [Dub Conversions quickstart guide](/conversions/quickstart) to [enable conversion tracking for your links](/conversions/quickstart#step-1%3A-enable-conversion-tracking-for-your-links).

## Quickstart

This quick start guide will show you how to get started with Dub iOS SDK in your Swift project.

<Steps titleSize="h3">
  <Step title="Install the Dub iOS SDK">
    Before installing, ensure your environment meets these minimum requirements:

    **Build Tools:**

    * Xcode 16+
    * Swift 4.0+

    **Platforms:**

    * iOS 16.0+
    * macOS 10.13 (Ventura)+

    The Dub iOS SDK can be installed using the [Swift Package Manager](https://docs.swift.org/swiftpm/documentation/packagemanagerdocs/).

    In Xcode, select **File** > **Add Package Dependencies** and add `https://github.com/dubinc/dub-ios` as the repository URL. Select the latest version of the SDK from the [release page](https://github.com/dubinc/dub-ios/releases).
  </Step>

  <Step title="Initialize the SDK">
    You must call `Dub.setup` with your publishable key and domain prior to being able to use the `dub` instance.

    <CodeGroup>
      ```swift iOS (SwiftUI) theme={null}
      import SwiftUI
      import Dub

      @main
      struct DubApp: App {
          // Step 1: Obtain your Dub domain and publishable key
          private let dubPublishableKey = "<DUB_PUBLISHABLE_KEY>"
          private let dubDomain = "<DUB_DOMAIN>"

          init() {
              // Step 2: Initialize the Dub SDK by calling `setup`
              Dub.setup(publishableKey: dubPublishableKey, domain: dubDomain)
          }

          var body: some Scene {
              WindowGroup {
                  ContentView()
                      // Step 3: Expose the `dub` instance as a SwiftUI environment value
                      .environment(\.dub, Dub.shared)
              }
          }
      }
      ```

      ```swift iOS (UIKit) theme={null}
      import UIKit
      import Dub

      @main
      class AppDelegate: UIResponder, UIApplicationDelegate {

          var window: UIWindow?

          // Step 1: Obtain your Dub domain and publishable key
          private let dubPublishableKey = "<DUB_PUBLISHABLE_KEY>"
          private let dubDomain = "<DUB_DOMAIN>"

          func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
              // Step 2: Initialize the Dub SDK by calling `setup`
              Dub.setup(publishableKey: dubPublishableKey, domain: dubDomain)
              return true
          }
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Track deep link open events" id="track-open">
    Call `trackOpen` on the `dub` instance to track deep link and deferred deep link open events.
    The `trackOpen` function should be called once without a `deepLink` parameter on first launch, and then
    again with the `deepLink` parameter whenever the app is opened from a deep link.

    <CodeGroup>
      ```swift iOS (SwiftUI) expandable theme={null}
      // ContentView.swift
      import SwiftUI
      import Dub

      struct ContentView: View {

          @Environment(\.dub) var dub: Dub

          @AppStorage("is_first_launch") private var isFirstLaunch = true

          var body: some View {
              NavigationStack {
                  VStack {
                      // Your app content
                  }
                  .onOpenURL { url in
                      trackOpen(deepLink: url)
                  }
                  .onAppear {
                      if isFirstLaunch {
                          trackOpen()
                          isFirstLaunch = false
                      }
                  }
              }
          }

          private func trackOpen(deepLink: URL? = nil) {
              Task {
                  do {
                      let response = try await dub.trackOpen(deepLink: deepLink)

                      // Obtain the destination URL from the response
                      guard let url = response.link?.url else {
                          return
                      }

                      // Navigate to the destination URL
                  } catch let error as DubError {
                      print(error.localizedDescription)
                  }
              }
          }
      }
      ```

      ```swift iOS (UIKit) expandable theme={null}
      import UIKit
      import Dub

      @main
      class AppDelegate: UIResponder, UIApplicationDelegate {

          var window: UIWindow?

          private let dubPublishableKey = "<DUB_PUBLISHABLE_KEY>"
          private let dubDomain = "<DUB_DOMAIN>"

          private var isFirstLaunch: Bool {
              get {
                  UserDefaults.standard.object(forKey: "is_first_launch") as? Bool ?? true
              }
              set {
                  UserDefaults.standard.set(newValue, forKey: "is_first_launch")
              }
          }

          func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
              Dub.setup(publishableKey: dubPublishableKey, domain: dubDomain)

              // Track first launch
              if isFirstLaunch {
                  trackOpen()
                  isFirstLaunch = false
              }

              // Override point for customization after application launch.
              return true
          }

          func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
              handleDeepLink(url: url)
              return true
          }

          func handleDeepLink(url: URL) {
              trackOpen(deepLink: url)
          }

          private func trackOpen(deepLink: URL? = nil) {
              // Call the tracking endpoint with the full deep link URL
              Task {
                  do {
                      let response = try await Dub.shared.trackOpen(deepLink: deepLink)

                      print(response)

                      // Navigate to final link via link.url
                      guard let destinationUrl = response.link?.url else {
                          return
                      }

                      // Navigate to the destination URL
                  } catch let error as DubError {
                      print(error.localizedDescription)
                  }
              }
          }
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Track lead events (optional)">
    To track lead events, call `trackLead` on the `dub` instance with your customer's external ID, name, and email.

    <CodeGroup>
      ```swift iOS (SwiftUI) expandable theme={null}
      // ContentView.swift
      import SwiftUI
      import Dub

      struct ContentView: View {

          @Environment(\.dub) var dub: Dub

          var body: some View {
             // ... your app content ...
          }

          private func trackLead(customerExternalId: String, name: String, email: String) {
              Task {
                  do {
                      let response = try await dub.trackLead(
                          eventName: "User Sign Up",
                          customerExternalId: customerExternalId,
                          customerName: name,
                          customerEmail: email
                      )

                      print(response)
                  } catch let error as DubError {
                      print(error.localizedDescription)
                  }
              }
          }
      }
      ```

      ```swift iOS (UIKit) expandable theme={null}
      // ViewController.swift
      import UIKit
      import Dub

      class ViewController: UIViewController {
          // View controller lifecycle...

          private func trackLead(customerExternalId: String, name: String, email: String) {
              Task {
                  do {
                      let response = try await Dub.shared.trackLead(
                          eventName: "User Sign Up",
                          customerExternalId: customerExternalId,
                          customerName: name,
                          customerEmail: email
                      )

                      print(response)
                  } catch let error as DubError {
                      print(error.localizedDescription)
                  }
              }
          }
      }
      ```
    </CodeGroup>

    <Accordion title="Lead event attributes">
      Here's the full list of attributes you can pass when sending a lead event:

      | Property             | Required | Description                                                                                                                                                                                                                                                                                                                                                                       |
      | :------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `clickId`            | **Yes**  | The unique ID of the click that the lead conversion event is attributed to. You can read this value from `dub_id` cookie. If an empty string is provided (i.e. if you're using [tracking a deferred lead event](/conversions/leads/deferred)), Dub will try to find an existing customer with the provided `customerExternalId` and use the `clickId` from the customer if found. |
      | `eventName`          | **Yes**  | The name of the lead event to track. Can also be used as a unique identifier to associate a given lead event for a customer for a subsequent sale event (via the `leadEventName` prop in `/track/sale`).                                                                                                                                                                          |
      | `customerExternalId` | **Yes**  | The unique ID of the customer in your system. Will be used to identify and attribute all future events to this customer.                                                                                                                                                                                                                                                          |
      | `customerName`       | No       | The name of the customer. If not passed, a random name will be generated (e.g. "Big Red Caribou").                                                                                                                                                                                                                                                                                |
      | `customerEmail`      | No       | The email address of the customer.                                                                                                                                                                                                                                                                                                                                                |
      | `customerAvatar`     | No       | The avatar URL of the customer.                                                                                                                                                                                                                                                                                                                                                   |
      | `mode`               | No       | The mode to use for tracking the lead event. `async` will not block the request; `wait` will block the request until the lead event is fully recorded in Dub; `deferred` will defer the lead event creation to a subsequent request.                                                                                                                                              |
      | `metadata`           | No       | Additional metadata to be stored with the lead event. Max 10,000 characters.                                                                                                                                                                                                                                                                                                      |
    </Accordion>
  </Step>

  <Step title="Track sale events (optional)">
    To track sale events, call `trackSale` on the `dub` instance with your customer's user ID and purchase information.

    <CodeGroup>
      ```swift iOS (SwiftUI) expandable theme={null}
      // ContentView.swift
      import SwiftUI
      import Dub

      struct ContentView: View {

        @Environment(\.dub) var dub: Dub

        var body: some View {
           // ... your app content ...
        }

        private func trackSale(
            customerExternalId: String,
            amount: Int,
            currency: String = "usd",
            eventName: String? = "Purchase",
            paymentProcessor: PaymentProcessor = .custom,
            invoiceId: String? = nil,
            metadata: Metadata? = nil,
            leadEventName: String? = nil,
            customerName: String? = nil,
            customerEmail: String? = nil,
            customerAvatar: String? = nil
        ) {
            Task {
                do {
                    let response = try await dub.trackSale(
                        customerExternalId: customerExternalId,
                        amount: amount,
                        currency: currency,
                        eventName: eventName,
                        paymentProcessor: paymentProcessor,
                        invoiceId: invoiceId,
                        metadata: metadata,
                        leadEventName: leadEventName,
                        customerName: customerName,
                        customerEmail: customerEmail,
                        customerAvatar: customerAvatar
                    )

                    print(response)
                } catch let error as DubError {
                    print(error.localizedDescription)
                }
            }
        }
      }
      ```

      ```swift iOS (UIKit) expandable theme={null}
      // ViewController.swift
      import UIKit
      import Dub

      class ViewController: UIViewController {
          // View controller lifecycle...

        private func trackSale(
            customerExternalId: String,
            amount: Int,
            currency: String = "usd",
            eventName: String? = "Purchase",
            paymentProcessor: PaymentProcessor = .custom,
            invoiceId: String? = nil,
            metadata: Metadata? = nil,
            leadEventName: String? = nil,
            customerName: String? = nil,
            customerEmail: String? = nil,
            customerAvatar: String? = nil
        ) {
            Task {
                do {
                    let response = try await Dub.shared.trackSale(
                        customerExternalId: customerExternalId,
                        amount: amount,
                        currency: currency,
                        eventName: eventName,
                        paymentProcessor: paymentProcessor,
                        invoiceId: invoiceId,
                        metadata: metadata,
                        leadEventName: leadEventName,
                        customerName: customerName,
                        customerEmail: customerEmail,
                        customerAvatar: customerAvatar
                    )

                    print(response)
                } catch let error as DubError {
                    print(error.localizedDescription)
                }
            }
        }
      }
      ```
    </CodeGroup>

    <Accordion title="Sale event attributes">
      Here are the properties you can include when sending a sale event:

      | Property             | Required | Description                                                                                                                                                |
      | :------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `customerExternalId` | **Yes**  | The unique ID of the customer in your system. Will be used to identify and attribute all future events to this customer.                                   |
      | `amount`             | **Yes**  | The amount of the sale in cents.                                                                                                                           |
      | `paymentProcessor`   | No       | The payment processor that processed the sale (e.g. [Stripe](/conversions/sales/stripe), [Shopify](/conversions/sales/shopify)). Defaults to "custom".     |
      | `eventName`          | No       | The name of the event. Defaults to "Purchase".                                                                                                             |
      | `invoiceId`          | No       | The invoice ID of the sale. Can be used as a idempotency key – only one sale event can be recorded for a given invoice ID.                                 |
      | `currency`           | No       | The currency of the sale. Defaults to "usd".                                                                                                               |
      | `metadata`           | No       | An object containing additional information about the sale.                                                                                                |
      | `clickId`            | No       | **\[For direct sale tracking]**: The unique ID of the click that the sale conversion event is attributed to. You can read this value from `dub_id` cookie. |
      | `customerName`       | No       | **\[For direct sale tracking]**: The name of the customer. If not passed, a random name will be generated.                                                 |
      | `customerEmail`      | No       | **\[For direct sale tracking]**: The email address of the customer.                                                                                        |
      | `customerAvatar`     | No       | **\[For direct sale tracking]**: The avatar URL of the customer.                                                                                           |
    </Accordion>
  </Step>
</Steps>

## Examples

Here are some open-source code examples that you can reference:

<CardGroup cols={2}>
  <Card title="Swift (SwiftUI)" icon="github" href="https://github.com/dubinc/dub-ios/tree/main/Examples/SwiftUI" color="#333333">
    See the full example on GitHub.
  </Card>

  <Card title="Swift (UIKit)" icon="github" href="https://github.com/dubinc/dub-ios/tree/main/Examples/UIKit" color="#333333">
    See the full example on GitHub.
  </Card>
</CardGroup>
