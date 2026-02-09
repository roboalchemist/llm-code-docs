# Source: https://dub.co/docs/concepts/deep-links/attribution.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Deep link attribution

> Learn how to use deep link attribution to track conversions events with Dub.

<Note>
  Deep link attribution requires a [Business plan](https://dub.co/pricing)
  subscription or higher.
</Note>

Dub's powerful [attribution platform](https://dub.co/analytics) lets you understand how well your deep links are translating to actual users and revenue dollars inside your app.

<Frame>
  <img src="https://assets.dub.co/blog/introducing-dub-conversions.webp" alt="Conversion analytics" />
</Frame>

<Note>
  This feature is currently only available for iOS (Swift). React Native and
  Android support are coming soon. If you'd like early access, please [contact
  us](https://dub.co/contact/support).
</Note>

## Prerequisites

First, you'll need to enable conversion tracking for your Dub links to be able to start tracking conversions:

<Tip>
  If you're using [Dub Partners](/partners/quickstart), you can skip this step
  since partner links will have conversion tracking enabled by default.
</Tip>

<AccordionGroup>
  <Accordion title="Option 1: On a workspace-level">
    To enable conversion tracking for all future links in a workspace, you can do the following:
    To enable conversion tracking for all future links in a workspace, you can do the following:

    1. Navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics).
    2. Toggle the **Workspace-level Conversion Tracking** switch to enable conversion tracking for the workspace.

    <Frame>
      <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=f810945d33a42f45de3e06647b2cfd15" alt="Enabling conversion tracking for a workspace" data-og-width="3082" width="3082" data-og-height="1529" height="1529" data-path="images/conversions/enable-conversion-tracking-workspace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=514f7549b9a65a40fc4224ea68859e06 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=9c002882f7093efb76ae4be72e5f0312 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=d4da71527556174d30b71c0f9acdad6f 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=c887363f92b258c3493267e2f4a3dd8e 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=e1b23eb5cf148df63105fdc572e6936b 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/enable-conversion-tracking-workspace.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=1623f4206427342d87df828a17d66438 2500w" />
    </Frame>

    This option will enable conversion tracking in the [Dub Link Builder](https://dub.co/help/article/dub-link-builder) for all future links.
  </Accordion>

  <Accordion title="Option 2: On a link-level">
    If you don't want to enable conversion tracking for all your links in a workspace, you can also opt to enable it on a link-level.

    To enable conversion tracking for a specific link, open the [Dub Link Builder](https://dub.co/help/article/dub-link-builder) for a link and toggle the **Conversion Tracking** switch.

    <Frame>
      <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4153d4a981e2a13324464ca3d30625cd" alt="Enabling conversion tracking for a link" data-og-width="2345" width="2345" data-og-height="908" height="908" data-path="images/conversions/enable-conversion-tracking.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=0984b50a4b6987e7bc4f8f3975559d0e 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=673093d978579d5cd19e22b2c786f6a4 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=94cb269be979162dd8bb74b2a5b614e9 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4572ec2e03c96b50d1da93f8b3f04636 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=f0a017e718cc81ae682e89809e4dab25 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/enable-conversion-tracking.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=078ec13ca0166c3b751d24271c1d2171 2500w" />
    </Frame>

    <Tip>
      You can also use the `C` keyboard shortcut when inside the link builder to
      quickly enable conversion tracking for a given link.
    </Tip>
  </Accordion>

  <Accordion title="Option 3: Via the API">
    Alternatively, you can also enable conversion tracking programmatically via the [Dub API](/api-reference/introduction). All you need to do is pass `trackConversion: true` when creating or updating a link:

    <CodeGroup>
      ```javascript Node.js theme={null}
      const link = await dub.links.create({
        url: "https://dub.co",
        trackConversion: true,
      });
      ```

      ```python Python theme={null}
      link = d.links.create(url="https://dub.co", track_conversion=True)
      ```

      ```go Go theme={null}
      link, err := d.Links.Create(ctx, &dub.CreateLinkRequest{
          URL: "https://dub.co",
          TrackConversion: true,
      })
      ```

      ```ruby Ruby theme={null}
      s.links.create_many(
        ::OpenApiSDK::Operations::CreateLinkRequest.new(
          url: "https://dub.co",
          track_conversion: true,
        )
      )
      ```
    </CodeGroup>
  </Accordion>
</AccordionGroup>

Then, you'll need generate a [publishable key](/api-reference/publishable-keys) from your Dub workspace to track conversions on the client-side.

To do that, navigate to your [workspace's Analytics settings page](https://app.dub.co/settings/analytics) and generate a new publishable key under the **Publishable Key** section.

<Frame>
  <img src="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=76add1f30a997ba897f10acdc21b51b5" alt="Enabling conversion tracking for a workspace" data-og-width="2985" width="2985" data-og-height="2021" height="2021" data-path="images/conversions/publishable-key.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=280&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=f0f995d217914793d81c0a42ccda502a 280w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=560&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=62a390272e2b24b6ae8cf3ba98dac66f 560w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=840&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=cdb86db75f933f33be21d4a0e8293227 840w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=1100&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ab9b7ec6577587e197e1fefeaa250216 1100w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=1650&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=ab5f37e61472d2c6118f7b640a5fdb50 1650w, https://mintcdn.com/dub/7gz73MV2fRr5fJas/images/conversions/publishable-key.png?w=2500&fit=max&auto=format&n=7gz73MV2fRr5fJas&q=85&s=6d83d47d0988ee0d895606f8b2e683c6 2500w" />
</Frame>

Once these are set up, we can start tracking conversion events for your deep links.

## Step 1: Install the client-side Mobile SDK

<Tabs>
  <Tab title="React Native">
    Install the [Dub React Native SDK](/sdks/client-side-mobile/installation-guides/react-native) and initialize it with your publishable key and short link domain.

    <Steps titleSize="h3">
      <Step title="Install the Dub React Native SDK">
        ```sh  theme={null}
        # With npm
        npm install @dub/react-native

        # With yarn
        yarn add @dub/react-native

        # With pnpm
        pnpm add @dub/react-native
        ```
      </Step>

      <Step title="Initialize the SDK">
        You must call `init` on your `dub` instance with your publishable key and domain prior to being able to use the `dub` instance. We provide two ways to initialize the SDK:

        **Option 1**: Use the `DubProvider` to wrap your app

        ```typescript  theme={null}
        import { DubProvider } from "@dub/react-native";

        export default function App() {
          return (
            <DubProvider
              publishableKey="<DUB_PUBLISHABLE_KEY>"
              dubDomain="<DUB_DOMAIN>"
            >
              // Your app content...
            </DubProvider>
          );
        }
        ```

        **Option 2**: Manually initialize the Dub SDK

        ```typescript  theme={null}
        import dub from "@dub/react-native";

        export default function App() {
          useEffect(() => {
            dub.init({
              publishableKey: "<DUB_PUBLISHABLE_KEY>",
              domain: "<DUB_DOMAIN>",
            });
          }, []);

          // Return your app...
        }
        ```
      </Step>
    </Steps>
  </Tab>

  <Tab title="iOS">
    Install the [Dub iOS SDK](/sdks/client-side-mobile/installation-guides/swift) and initialize it with your publishable key and short link domain.

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
      </Step>
    </Steps>
  </Tab>
</Tabs>

## Step 2: Track deep link open events

Once the SDK has been initialized, you can start tracking deep link and deferred deep link events.

Call `trackOpen` on the `dub` instance to track deep link and deferred deep link open events. The `trackOpen` function should be called once without a `deepLink` parameter on first launch, and then again with the `deepLink` parameter whenever the app is opened from a deep link.

<CodeGroup>
  ```typescript React Native expandable theme={null}
  import { useState, useEffect, useRef } from "react";
  import { Linking } from "react-native";
  import AsyncStorage from "@react-native-async-storage/async-storage";
  import dub from "@dub/react-native";

  export default function App() {
    useEffect(() => {
      dub.init({
        publishableKey: "<DUB_PUBLISHABLE_KEY>",
        domain: "<DUB_DOMAIN>",
      });

      // Check if this is first launch
      const isFirstLaunch = await AsyncStorage.getItem("is_first_launch");

      if (isFirstLaunch === null) {
        await handleFirstLaunch();
        await AsyncStorage.setItem("is_first_launch", "false");
      } else {
        // Handle initial deep link url (Android only)
        const url = await Linking.getInitialURL();

        if (url) {
          await handleDeepLink(url);
        }
      }

      const linkingListener = Linking.addEventListener("url", (event) => {
        handleDeepLink(event.url);
      });

      return () => {
        linkingListener.remove();
      };
    }, []);

    const handleFirstLaunch = async (
      deepLinkUrl?: string | null | undefined
    ): Promise<void> => {
      try {
        const response = await dub.trackOpen(deepLinkUrl);

        const destinationURL = response.link?.url;
        // Navigate to the destination URL
      } catch (error) {
        // Handle error
      }
    };

    // Return your app...
  }
  ```

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

If the deep link was successfully resolved and correlated to the original click, the `response` object will contain the destination URL, which you can use to navigate the user to the appropriate screen.

It will also contain the `clickId`, which the `dub` instance will persist internally.

## Step 3: Track conversion events

You may track conversion events directly in your app with the `trackLead` and `trackSale` methods.

<CodeGroup>
  ```typescript React Native expandable theme={null}
  import dub from "@dub/react-native";

  function trackLead(user: User) {
    try {
      await dub.trackLead({
        eventName: "User Sign Up",
        customerExternalId: user.id,
        customerName: user.name,
        customerEmail: user.email,
      });
    } catch (error) {
      // Handle sale tracking error
    }
  }

  function trackSale(user: User, product: Product) {
    try {
      await dub.trackSale({
        customerExternalId: user.id,
        amount: product.price.amount,
        currency: "usd",
        eventName: "Purchase",
      });
    } catch (error) {
      // Handle sale tracking error
    }
  }
  ```

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
                      eventName: "Sign Up",
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

      private func trackSale(
          customerExternalId: String,
          amount: Int,
          currency: String = "usd",
          eventName: String? = "Purchase",
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
      // View controller lifecycle

      private func trackLead(customerExternalId: String, name: String, email: String) {
          Task {
              do {
                  let response = try await dub.trackLead(customerExternalId: customerExternalId, name: name, email: email)
              } catch let error as DubError {
                  print(error.localizedDescription)
              }
          }
      }

      private func trackSale(customerExternalId: String, amount: Int, currency: String = "usd", eventName: String? = "Purchase", customerName: String? = nil, customerEmail: String? = nil, customerAvatar: String? = nil) {
          Task {
              do {
                  let response = try await dub.trackSale(customerExternalId: customerExternalId, amount: amount, currency: currency, eventName: eventName, customerName: customerName, customerEmail: customerEmail, customerAvatar: customerAvatar)
              } catch let error as DubError {
                  print(error.localizedDescription)
              }
          }
      }
  }
  ```
</CodeGroup>

Alternatively, you can [track conversion events server-side](/conversions/quickstart#step-3%3A-install-the-dub-server-side-sdk-%2B-track-conversion-events) for [lead events](/conversions/leads/introduction) and [sale events](/conversions/sales/introduction) by sending the `clickId` resolved from the deep link to your backend and then calling off to either:

* [`POST /track/lead`](https://dub.co/docs/api-reference/endpoint/track-lead)
* [`POST /track/sale`](https://dub.co/docs/api-reference/endpoint/track-sale)

## Step 4: View your conversions

Once you've enabled conversion tracking for your links, all your tracked conversions will show up on your [Analytics dashboard](https://app.dub.co/analytics). We provide 3 different views to help you understand your conversions:

* **Time-series**: A [time-series view](https://app.dub.co/dub/analytics?view=timeseries) of the number clicks, leads and sales.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=7380bc6120ade538b2b65eefdc76d3ed" alt="Time-series line chart" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/timeseries-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=430758e529cd22c5d28f976ee7da5379 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=9cf861c9aa7cf680f46ce32585303d2b 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=999b05a7805bd208b4649fc67a3b45e0 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=42baa1d9d42c26ed191875fef033128a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=127ee673f66f2079f236985ec754416e 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/timeseries-chart.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=1c0696bb18043dd86388f03d09aed450 2500w" />
</Frame>

* **Funnel chart**: A [funnel chart view](http://app.dub.co/analytics?view=funnel) visualizing the conversion & dropoff rates across the different steps in the conversion funnel (clicks → leads → sales).

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=6275caafcfc3be6d8b498149222f225e" alt="Funnel chart view showing the conversion & dropoff rates from clicks → leads → sales" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/funnel-chart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=df57b14d04dd585c5236f6fcf16a4963 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=fc1689a06ce8ceecf1487faca8730d06 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=b69533d460a2bc95964d7f6d2e5f23f4 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=43b86431662a4c214a36fbf5405abb4a 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=687f900f0b8732301c43c8ee18ca7dd4 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/funnel-chart.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=aed9e63c7fd1fb67c463920c73911cba 2500w" />
</Frame>

* **Real-time events stream**: A [real-time events stream](https://app.dub.co/events) of every single conversion event that occurs across all your links in your workspace.

<Frame>
  <img src="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=c2467f9fa2e755f06b3e7b147fa0bd81" alt="The Events Stream dashboard on Dub" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/conversions/events-table.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=280&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=8e747ccc2f01015e014a9b4fbc98d588 280w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=560&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=4a0c65b37cf99181b712beb063e46dc2 560w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=840&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=345d5b0b36c6f2093ea7b6a97d73ff49 840w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=1100&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=5deb48ab5e08bf2e31447fd32615c05e 1100w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=1650&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=33d6f27b5c067eb8586cfea15fe0a040 1650w, https://mintcdn.com/dub/F9cdc9nB_SI4yl65/images/conversions/events-table.png?w=2500&fit=max&auto=format&n=F9cdc9nB_SI4yl65&q=85&s=132a7592c8ecf518b31c043dad2093f4 2500w" />
</Frame>
