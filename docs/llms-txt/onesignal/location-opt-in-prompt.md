# Source: https://documentation.onesignal.com/docs/en/location-opt-in-prompt.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Request location permissions with in-app messages

> Guide users to enable location tracking in your mobile app using a soft pre-prompt in OneSignal before triggering the native Android or iOS location permission request.

Easily request location access from users by using a OneSignal in-app message as a soft pre-prompt before showing the required native system-level location permission dialog. This improves opt-in rates and gives you more control over when and how to ask. Alternatively, you can directly trigger the system prompt using our [Mobile SDK location methods](./mobile-sdk-reference#location).

***

## Requirements

Before creating your in-app message:

* Add location tracking permissions to your app (for both Android and iOS).
  * Refer to our [Mobile SDK location reference](./mobile-sdk-reference#location) for platform-specific setup instructions.
* Enable location sharing with OneSignal in your app code.

***

## Create your message

<Steps>
  <Step title="Create your message">
    In the OneSignal dashboard, go to: **Messages > In-App > New In-App**
  </Step>

  <Step title="Audience">
    * If all users should see the prompt, select **Show to all users**.
    * Otherwise, target a specific Segment.
  </Step>

  <Step title="Message design">
    * Clearly explain why location access benefits the user. E.g., "Enable location to receive relevant local updates."
    * Be concise but specific to increase opt-in likelihood.

    <Frame caption="Image showing in-app blocks and ability to add click actions alongside preview">
      <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/d79589d-iam-setup.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=dfc599957a14fae1da44feaca697cc8d" width="1922" height="1650" data-path="images/docs/d79589d-iam-setup.png" />
    </Frame>
  </Step>
</Steps>

***

## Add the Location Permission Prompt Click Action

<Steps>
  <Step title="Add a button or image">
    Add a button or image with a clear call to action (e.g., “Enable Location”).
  </Step>

  <Step title="Add a click action">
    In the options:

    * Click **Add Click Action**
    * Select **Location Permission Prompt**

    When clicked, OneSignal will trigger the native, required system-level location prompt.

    **If location is already enabled, the message won’t show to avoid unnecessary prompts.**

    <Info>
      Both Android and iOS limit how frequently system-level prompts can appear. Using this soft pre-prompt helps avoid those limitations and allows for repeat attempts if needed.
    </Info>

    <Frame caption="Image showing in-app blocks and ability to add click actions">
      <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3ee94da-iam-setup-add-buttons.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=bea5041690d177a6b2c74b970bac178d" width="561" height="767" data-path="images/docs/3ee94da-iam-setup-add-buttons.png" />
    </Frame>
  </Step>
</Steps>

***

## Trigger the in-app message

You can control when and how the prompt is shown.

### Option 1: Time-based triggers

Show the message after a user has been in the app for a set amount of time (e.g., after 30 seconds).

<Frame caption="Image showing session in-app trigger.">
  <img src="https://mintcdn.com/onesignal/KSCNwSpBCNSQ8xdF/images/docs/fb26c9cc44f0ff633869613177c204987850f8a45de908f153387b6c18211e3d-Screenshot_2025-04-03_at_6.34.31_PM.png?fit=max&auto=format&n=KSCNwSpBCNSQ8xdF&q=85&s=aa5c748b14350c0c35165194daf0b567" width="1566" height="688" data-path="images/docs/fb26c9cc44f0ff633869613177c204987850f8a45de908f153387b6c18211e3d-Screenshot_2025-04-03_at_6.34.31_PM.png" />
</Frame>

### Option 2: Programmatic triggers

Control exactly when the prompt appears via the SDK:

<Steps>
  <Step title="Add the trigger code to the app.">
    Use our SDK's [`addTrigger` method](./mobile-sdk-reference#in-app-messages) to set a key like `location_prompt` and value like `true`. Then call this whenever you want inside your app.
  </Step>

  <Step title="Add the trigger to the message">
    Set the same trigger key (`location_prompt`) and value (`true`) in your in-app message settings.

    <Frame caption="Image showing programmatic In-app trigger.">
      <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/a1073246e17c826da317ef34f1fb4b4171e924a2de9f199cef9c154a0470c9aa-Screenshot_2025-04-03_at_6.35.33_PM.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=aa22c76661dc1cbf6ddac693fd471a1a" width="1566" height="742" data-path="images/docs/a1073246e17c826da317ef34f1fb4b4171e924a2de9f199cef9c154a0470c9aa-Screenshot_2025-04-03_at_6.35.33_PM.png" />
    </Frame>
  </Step>
</Steps>

***

## Set the message frequency

To avoid spamming users:

* Choose **Multiple times**
* Set a number of times to show the message
* Set a gap between each attempt

Example setting: show up to 5 times, with a 4-week gap between each attempt

This allows monthly reminders for up to 5 months, striking a balance between persistence and user experience.

<Frame caption="Example scheduling configuration for repeat prompts.">
  <img src="https://mintcdn.com/onesignal/6tscVAtiSqz353kV/images/docs/9e87626b6069826d65baa160acf278f9ada4724ea1a4155b63a2bd3be9e1fc64-Screenshot_2025-04-03_at_7.02.24_PM.png?fit=max&auto=format&n=6tscVAtiSqz353kV&q=85&s=00f77c150cdb1f667aef561d09cd5998" width="1566" height="722" data-path="images/docs/9e87626b6069826d65baa160acf278f9ada4724ea1a4155b63a2bd3be9e1fc64-Screenshot_2025-04-03_at_7.02.24_PM.png" />
</Frame>

***

## Best Practices

* Always explain the benefit of location access to users.
* Use segmentation or triggers to avoid asking at a bad time.
* Pre-prompts increase opt-in rates and avoid operating system limits.
* Ensure location permissions are correctly configured in your app before triggering the in-app message.

***

<Check>
  You will start to see location points being tracked in your Users and Subscriptions pages.

  Create [Location-triggered messages](./location-triggered-event).
</Check>

***

Built with [Mintlify](https://mintlify.com).
