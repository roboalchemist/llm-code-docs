# Source: https://documentation.onesignal.com/docs/en/example-create-a-tutorial.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Onboard users with banner in-app messages

> Guide users with contextual top and bottom banner in-app messages that don't block your app UI.

Banner In-App Messages (IAMs) let you guide users without blocking your app UI. You display short, contextual messages at the top or bottom of the screen while users continue interacting with your app.

You typically use banner IAMs when users need extra context at a specific moment, such as the first time they reach a screen or start a key workflow.

<Info>
  In-App Messages display only when their trigger conditions are met. You control exactly when a banner appears by setting triggers from your app.
</Info>

***

## When to use banner IAMs

Use banner IAMs for onboarding when you want to:

* Explain a screen as the user reaches it
* Guide users through multi-step flows
* Highlight actions users should take next
* Keep onboarding visible but non-intrusive

If you need a structured, multi-screen walkthrough, use a card or carousel IAM instead.

***

## Example onboarding flow

When a user opens your site or app for the first time, a top banner welcomes them and prompts exploration. When the user taps a product to view details, a bottom banner guides them on what to do next. Each banner appears only when the user reaches the relevant screen.

This approach ensures users see guidance only when it is relevant.

### Visual example: E-commerce onboarding

Here's how banner IAMs guide users through an e-commerce app. This example uses **two separate IAMs**, each with a **3-second auto-dismiss**. When the first banner dismisses, the trigger for the second banner activates, creating a smooth sequential flow:

<Columns cols={2}>
  <Card title="Initial welcome banner" icon="hand-wave">
    <Frame>
      <img src="https://mintcdn.com/onesignal/0cGYn6VDLSrZ4Cta/images/iam-onboarding-welcome-banner.png?fit=max&auto=format&n=0cGYn6VDLSrZ4Cta&q=85&s=0d8cc4972e4e7d512a47dac5543b65fa" alt="Welcome banner displaying 'Tap on any product to learn more and start shopping!'" width="819" height="1723" data-path="images/iam-onboarding-welcome-banner.png" />
    </Frame>

    When users first open the app, a bottom banner prompts them to explore products.
  </Card>

  <Card title="Product selection banner" icon="cart-shopping">
    <Frame>
      <img src="https://mintcdn.com/onesignal/0cGYn6VDLSrZ4Cta/images/iam-onboarding-product-banner.png?fit=max&auto=format&n=0cGYn6VDLSrZ4Cta&q=85&s=2c8483ec47f96082c038b0d836bdfb8d" alt="Product banner displaying 'You're viewing a product! Check out all the details and add it to your cart when you're ready.'" width="776" height="1485" data-path="images/iam-onboarding-product-banner.png" />
    </Frame>

    When a user taps on a product, a banner provides guidance for the product detail view.
  </Card>
</Columns>

***

## Prerequisites

Before you begin, make sure you have:

* An active OneSignal app
* OneSignal SDK installed in your app
* The ability to trigger events or call methods from your app code
* [User consent](./mobile-sdk-reference#privacy) granted for the OneSignal SDK (required for In-App Messaging)

***

## Create a banner in-app message

<Steps>
  <Step title="Navigate to In-App Messages">
    In the OneSignal dashboard, go to **Messages → In-App Messages** and select **New In-App Message**.
  </Step>

  <Step title="Choose banner type">
    Under **Message Type**, choose **Top** or **Bottom**.
  </Step>

  <Step title="Design your content">
    Include a short heading that explains the purpose of the screen, optional supporting text if needed, and an optional button to guide the next action.
  </Step>

  <Step title="Configure triggers">
    Add one or more **[In-App Message triggers](./iam-triggers)** that define when the banner should appear. Optionally add conditions or limits to control how often the message displays.
  </Step>

  <Step title="Set display duration">
    Choose between auto-dismiss (banner disappears after 3-10 seconds) or user-dismissible (banner remains until the user taps close).
  </Step>

  <Step title="Activate the message">
    Save and activate your banner In-App Message.
  </Step>
</Steps>

<Note>
  Use top banners for high-visibility guidance and bottom banners for subtle prompts that align with primary actions. For onboarding, use auto-dismiss to keep the flow moving without requiring user action.
</Note>

<Warning>
  Avoid long explanations. Banner IAMs are not designed for detailed onboarding or tutorials.
</Warning>

***

## Trigger the banner from your app

You trigger the banner IAM when the user reaches a specific screen or completes an action using In-App Message triggers. Triggers are key–value pairs that you set from your app code. When the trigger conditions match the IAM's display rules, the banner displays.

<CodeGroup>
  ```javascript JavaScript theme={null}
  // Trigger when the user views the dashboard
  OneSignal.addTrigger('dashboard_viewed', 'true');
  ```

  ```swift iOS theme={null}
  // Trigger when the user views the dashboard
  OneSignal.addTrigger("dashboard_viewed", value: "true")
  ```

  ```kotlin Android theme={null}
  // Trigger when the user views the dashboard
  OneSignal.addTrigger("dashboard_viewed", "true")
  ```

</CodeGroup>

<Info>
  Triggers persist for the session unless you remove or update them. Make sure each trigger represents a clear, intentional onboarding moment.
</Info>

### Remove triggers when no longer needed

To prevent banners from reappearing unintentionally, remove triggers when they're no longer needed:

<CodeGroup>
  ```javascript JavaScript theme={null}
  // Remove trigger after the user completes onboarding
  OneSignal.removeTrigger('dashboard_viewed');
  ```

  ```swift iOS theme={null}
  // Remove trigger after the user completes onboarding
  OneSignal.removeTrigger("dashboard_viewed")
  ```

  ```kotlin Android theme={null}
  // Remove trigger after the user completes onboarding
  OneSignal.removeTrigger("dashboard_viewed")
  ```

</CodeGroup>

***

## Chain banner messages (optional)

You can guide users through a flow by creating **multiple IAMs**, each with its own trigger. Set each banner to **auto-dismiss after 3 seconds** so the next banner can appear. Remove the previous trigger before adding the next one to prevent overlapping banners.

<Tip>
  For smooth sequential onboarding, create one IAM per step, set each to auto-dismiss after 3 seconds, and chain them by removing the previous trigger when adding the next one.
</Tip>

### Example: E-commerce onboarding flow

1. Page loads → Trigger `iam_welcome` → Banner: "🎉 Welcome! Explore our products"
2. User taps product → Trigger `iam_product_view` → Banner: "👀 Tap ❤️ to save favorites"
3. User adds to cart → Trigger `iam_add_to_cart` → Banner: "✅ Great choice! View cart anytime"
4. User views cart → Trigger `iam_cart_view` → Banner: "🛒 Review your items here"
5. User checks out → Trigger `iam_checkout` → Banner: "🎊 Thanks for your order!"

<CodeGroup>
  ```javascript JavaScript theme={null}
  // Move from step 1 to step 2
  OneSignal.removeTrigger('iam_welcome');
  OneSignal.addTrigger('iam_product_view', 'true');
  ```

  ```swift iOS theme={null}
  // Move from step 1 to step 2
  OneSignal.removeTrigger("iam_welcome")
  OneSignal.addTrigger("iam_product_view", value: "true")
  ```

  ```kotlin Android theme={null}
  // Move from step 1 to step 2
  OneSignal.removeTrigger("iam_welcome")
  OneSignal.addTrigger("iam_product_view", "true")
  ```

</CodeGroup>

This creates progressive onboarding without overwhelming the user.

***

## Verify the setup

<Check>
  The banner appears only when the trigger fires and does not block the app UI.
</Check>

If the banner does not appear:

* Confirm the trigger key and value match exactly (case-sensitive)
* Verify the IAM is Active in the dashboard
* Check Frequency Limits - the IAM may be rate-limited
* Ensure user meets Targeting Rules (if any)
* Check console logs for OneSignal trigger events
* Verify In-App Messaging consent has been granted (if required)

***

## Next steps

* Announce new features using banner In-App Messages
* Create a full onboarding experience with card or carousel IAMs
* Segment users to show different onboarding messages based on experience level
* [A/B test](./journeys-actions#abn-tests-multivariate-testing) different banner messages to optimize engagement

Built with [Mintlify](https://mintlify.com).
