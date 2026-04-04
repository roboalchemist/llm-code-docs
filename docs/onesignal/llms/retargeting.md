# Source: https://documentation.onesignal.com/docs/en/retargeting.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Retargeting Messages

> Learn how to retarget users based on their past message interactions using OneSignal. Boost engagement by sending follow-up messages to users who did or did not interact with your original messages.

Sending a message is just the first step in building strong customer relationships. The real impact comes from how you follow up based on user interactions with those messages. OneSignal makes it easy to retarget users who interacted—or didn’t—with your previous messages, enabling smarter engagement strategies.

***

## How to Retarget Users

Retargeting users in OneSignal is quick and effective. Follow these steps to identify message engagement and send follow-up messages.

<Steps>
  <Step title="Open a Sent Message">
    Go to the **Messages** or **Delivery** tab in the OneSignal Dashboard and select the message you want to retarget users from.

    <Frame caption="Select a sent message">
      <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/7169ef3-Screenshot_2023-07-25_at_1.46.52_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=13cb079c79299c39372401743d107c03" width="2246" height="1146" data-path="images/docs/7169ef3-Screenshot_2023-07-25_at_1.46.52_PM.png" />
    </Frame>
  </Step>

  <Step title="View Audience Activity">
    Navigate to the **Audience Activity** section. Here you can see how users interacted with your message—such as opened, clicked, or ignored.
  </Step>

  <Step title="Start Retargeting">
    Click the **Send a Retargeted Message** button next to the event you want to retarget on.

    <Frame caption="Send a retargeted message button">
      <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1a4b53b-Screenshot_2023-07-25_at_2.01.48_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=b33c2b45e592241a560b03f1f1c2bc45" width="2246" height="1310" data-path="images/docs/1a4b53b-Screenshot_2023-07-25_at_2.01.48_PM.png" />
    </Frame>
  </Step>

  <Step title="Create Your Retargeting Message">
    * Enter a **Message Name** so you can find it later.
    * The **Audience** will automatically be set based on the interaction type you selected.

    <Frame caption="Retargeting message setup">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/docs/01ebded-Screenshot_2023-07-25_at_2.02.42_PM.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=1c7429d46a2d1eab36e94fefd18e9bc5" width="2246" height="960" data-path="images/docs/01ebded-Screenshot_2023-07-25_at_2.02.42_PM.png" />
    </Frame>
  </Step>

  <Step title="Compose and Send">
    Write your retargeting message as you normally would using the message editor.
  </Step>
</Steps>

<Warning>
  Retargeting messages must be scheduled within **30 days** of the original
  message's send date.
</Warning>

***

## Retargeting FAQ

### Why don’t I see my previously sent notifications?

Notifications sent via the **API** or as **Automated Messages** are automatically deleted after approximately **30 days**. Once deleted, they will no longer appear in your message history or be available for retargeting.

### Why can’t I retarget older messages?

Only messages created within the last **30 days** are eligible for retargeting. Messages older than this timeframe are no longer retained for retargeting purposes.

Additionally, if you recently upgraded to a plan that includes retargeting, messages sent **before** the upgrade are **not** retroactively stored. Retargeting data collection begins only after your account gains access to the feature.

### How long is message data retained for retargeting?

Message interaction data used for retargeting is stored for **30 days** from the original send date. After this period, the data is automatically purged and the message becomes ineligible for retargeting.

<Info>
  Need help?

  Chat with our Support team or email `support@onesignal.com`

  Please include:

* Details of the issue you're experiencing and steps to reproduce if available
* Your OneSignal App ID
* The External ID or Subscription ID if applicable
* The URL to the message you tested in the OneSignal Dashboard if applicable
* Any relevant [logs or error messages](/docs/en/capturing-a-debug-log)

  We're happy to help!
</Info>

***

Built with [Mintlify](https://mintlify.com).
