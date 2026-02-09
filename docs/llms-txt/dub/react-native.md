# Source: https://dub.co/docs/sdks/client-side-mobile/installation-guides/react-native.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dub.co/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# React Native

> How to add the Dub React Native SDK to your React Native project

## Prerequisites

Before you get started, make sure you have the following:

1. Obtain your [publishable key](/api-reference/publishable-keys) (`DUB_PUBLISHABLE_KEY`) from
   your [workspace's Analytics settings page](https://app.dub.co/settings/analytics) and select
   your domain (`DUB_DOMAIN`) from your [workspace's Custom Domains settings page](https://app.dub.co/links/domains).

2. (Optional) If you plan to track conversions, follow the [Dub Conversions quickstart guide](/conversions/quickstart) to [enable conversion tracking for your links](/conversions/quickstart#step-1%3A-enable-conversion-tracking-for-your-links).

## Quickstart

This quick start guide will show you how to get started with Dub React Native SDK in your React Native app.

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

  <Step title="Track deep link open events" id="track-open">
    Call `trackOpen` on the `dub` instance to track deep link and deferred deep link open events.
    The `trackOpen` function should be called once without a `deepLink` parameter on first launch, and then
    again with the `deepLink` parameter whenever the app is opened from a deep link.

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
  </Step>

  <Step title="Track lead events (optional)">
    To track lead events, call `trackLead` on the `dub` instance with your customer's external ID, name, and email.

    ```typescript React Native theme={null}
    import dub from "@dub/react-native";

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
    ```

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

    ```typescript React Native theme={null}
    import dub from "@dub/react-native";

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
    ```

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
  <Card title="React Native" icon="github" href="https://github.com/dubinc/dub-react-native/tree/main/example" color="#333333">
    See the full example on GitHub.
  </Card>
</CardGroup>
