# Source: https://documentation.onesignal.com/docs/en/in-app-messages-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# In-app overview

> Display targeted, customizable messages inside your mobile app to drive engagement, collect feedback, and prompt actions like push opt-in.

In-app messages (IAM) are customizable, targeted messages that display within your mobile app. They enable you to:

* Prompt User actions like subscribing to push notifications or updating their location
* Promote new or underutilized features to targeted Users
* Display announcements and news in real time without releasing an app update
* Create surveys and carousels
* Help with onboarding and educational content

<Frame caption="In-app message examples">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/iam_marketing.jpg?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=4e09e43dc57956f4c33ad761f403aea5" alt="Examples of in-app messages including promotions, surveys, and feature announcements" width="1280" height="720" data-path="images/iam/iam_marketing.jpg" />
</Frame>

***

## In-app setup

You must have the OneSignal SDK installed in your app to use in-app messages. Once the SDK is integrated, you can create and send in-app messages from the OneSignal dashboard without writing any code. The SDK also provides methods for advanced use cases like:

* Triggering the message at specific times
* Click handling and deep linking
* Pausing the message
* Lifecycle management

<Columns cols={2}>
  <Card title="Mobile SDK setup" icon="mobile" href="./mobile-sdk-setup">
    Add OneSignal to your mobile app codebase.
  </Card>

  <Card title="In-app message SDK methods" icon="code" href="./mobile-sdk-reference#in-app-messages">
    Access trigger, click handler, and lifecycle APIs.
  </Card>

  <Card title="In-app triggers" icon="bolt" href="./iam-triggers">
    Control when messages appear based on User behavior or app activity.
  </Card>

  <Card title="In-app click actions" icon="hand-pointer" href="./iam-click-actions">
    Define what happens when Users interact with your message.
  </Card>
</Columns>

***

## Send in-app messages

You can send in-app messages from the OneSignal dashboard and within Journeys.

<Frame caption="How to create and send in-app messages in OneSignal">
  <iframe width="560" height="315" src="https://www.youtube.com/embed/TSkqp4e-ya0?si=vbNStROmopkSWxWd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

<Columns cols={2}>
  <Card title="Dashboard" icon="window-maximize" href="#send-from-the-dashboard">
    Compose and send in-app messages from the OneSignal dashboard.
  </Card>

  <Card title="Journeys" icon="route" href="./journeys-overview">
    Build automated, multi-step, and multi-channel flows.
  </Card>
</Columns>

### Send from the dashboard

<Steps>
  <Step title="Select the message channel" icon="window-maximize">
    Select **Create...** then choose your message channel. You can also navigate to **Messages** or **Templates** to view previous messages.

    <Frame caption="Create a new message in the OneSignal dashboard.">
      <img src="https://mintcdn.com/onesignal/UDk6E5NjA3sdGdRN/images/dashboard/create-message.png?fit=max&auto=format&n=UDk6E5NjA3sdGdRN&q=85&s=97504cf71555ac4aeb263a36ad2d28b3" alt="OneSignal dashboard showing create message options" width="2128" height="1374" data-path="images/dashboard/create-message.png" />
    </Frame>
  </Step>

  <Step title="Choose a composition method" icon="pencil">
    * Start from scratch with the [Block Editor](./design-your-in-app-message) or [HTML Editor](./design-your-in-app-message-with-html)
    * Use a pre-built [template](./templates)
  </Step>

  <Step title="Set a name and label" icon="tag">
    Add internal metadata for tracking and reporting. API equivalent: `name`
  </Step>

  <Step title="Select your audience" icon="users">
    Choose which users receive the message. You can include and exclude [segments](./segmentation) to target specific groups. Defaults to all "Subscribed Users" if no segment is set.

    <Frame caption="Name, label, and audience segment selection in the dashboard.">
      <img src="https://mintcdn.com/onesignal/ciRrThfP6xMpI7GY/images/dashboard/message-name-label-audience.png?fit=max&auto=format&n=ciRrThfP6xMpI7GY&q=85&s=1f41b0e42d31211b1c1badf87ba84056" alt="Dashboard fields for message name, label, and audience segment selection" width="1650" height="518" data-path="images/dashboard/message-name-label-audience.png" />
    </Frame>

    <Note>
      In-app messages are delivered to all [mobile Subscriptions](./subscriptions) in the Segment, regardless of push opt-in status. However, if your message contains a push prompt [click action](#click-actions), it will not show to subscribed (opted-in) mobile Subscriptions.
    </Note>
  </Step>
</Steps>

### Message design

Use the visual drag-and-drop editor or the HTML editor for more control.

<Frame caption="In-app message block editor interface">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/b7df349-Screenshot_2022-12-10_at_12.52.59_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=4930228c3107db798dadc1bf69b4b0d6" alt="OneSignal in-app message block editor showing drag-and-drop design interface" width="2134" height="1736" data-path="images/docs/b7df349-Screenshot_2022-12-10_at_12.52.59_PM.png" />
</Frame>

<Columns cols={2}>
  <Card title="Design with drag-and-drop" icon="paintbrush" href="./design-your-in-app-message">
    Use the visual editor to quickly build messages.
  </Card>

  <Card title="Design with HTML" icon="code" href="./design-your-in-app-message-with-html">
    Full control for developers to customize messages.
  </Card>

  <Card title="Pre-built HTML templates" icon="clone" href="./in-app-html-templates">
    Start from tested layouts and campaigns.
  </Card>

  <Card title="In-app JavaScript APIs for HTML" icon="brackets-curly" href="./in-app-message-api">
    Add OneSignal click actions to your HTML messages.
  </Card>

  <Card title="Message personalization" icon="wand-magic-sparkles" href="./message-personalization">
    Add dynamic content to personalize messages for each User.
  </Card>

  <Card title="Multi-language messaging" icon="language" href="./multi-language-messaging">
    Localize your content for global audiences.
  </Card>
</Columns>

### Click actions

Customize what happens when Users click elements in your message.

<Frame caption="Click action options in the in-app message editor">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/click_action_dropdown.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=4edea63fce3704ec2c343eacfc77f248" alt="OneSignal in-app message editor showing click action dropdown options" width="518" height="525" data-path="images/iam/click_action_dropdown.png" />
</Frame>

<Columns cols={2}>
  <Card title="Click actions" icon="hand-pointer" href="./iam-click-actions">
    Configure what happens when Users click elements in your message.
  </Card>

  <Card title="Event Streams" icon="signal-stream" href="./event-streams">
    Track interactions with the message.
  </Card>

  <Card title="SDK click handler" icon="code" href="./mobile-sdk-reference#addclicklistener-in-app">
    React to click events with the mobile SDK.
  </Card>

  <Card title="Deep linking" icon="arrow-up-right-from-square" href="./deep-linking">
    Navigate Users to specific screens on click.
  </Card>
</Columns>

### Triggers

Define when messages should appear during app sessions.

<Frame caption="Trigger setup options for in-app messages">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/5578ae6-image.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=d70aa26e6fa87244d4fa8f4527d9b449" alt="OneSignal dashboard showing in-app message trigger configuration options" width="1766" height="884" data-path="images/docs/5578ae6-image.png" />
</Frame>

Four trigger types are available:

* **On app open**: Display when the User launches the app.
* **Session duration**: Delay a set number of seconds after app open.
* **Since last message**: Delay a set time after the last in-app message was shown.
* **[Custom triggers](./iam-triggers)**: Controlled via the SDK `addTrigger(s)` method for precise timing based on User behavior.

### Dismiss behavior

Messages can dismiss:

* On User interaction (click, swipe)
* After a set time (auto-dismiss)

<Frame caption="Auto-dismiss configuration set to 90 seconds">
  <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/8dcc001876557819348b804906ed63aee17d83bce300e63e91cc11c54eface2f-Screenshot_2025-04-08_at_2.00.07_PM.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=59d61042bc7d3e1855e4c90f9a83e562" alt="OneSignal dashboard showing in-app message auto-dismiss timer set to 90 seconds" width="1342" height="530" data-path="images/docs/8dcc001876557819348b804906ed63aee17d83bce300e63e91cc11c54eface2f-Screenshot_2025-04-08_at_2.00.07_PM.png" />
</Frame>

### Schedule and frequency

* **Start showing**: When the message becomes eligible to display
* **Stop showing**: Set an end date/time or "Show forever"

#### Display frequency

* **Only once** (default)
* **Every time** trigger conditions are met
* **Multiple times** with custom repeat logic

Examples:

* Show **2 times** with a **1 hour** gap
* Show **12 times** with a **30 day** gap

<Frame caption="Frequency configuration: show the message 12 times every 30 days">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e66d013-Screenshot_2022-12-10_at_1.27.10_PM.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=0cfe8f5e92ea5d02aa5ae3c659b5538c" alt="OneSignal dashboard showing in-app message frequency set to 12 times every 30 days" width="2100" height="756" data-path="images/docs/e66d013-Screenshot_2022-12-10_at_1.27.10_PM.png" />
</Frame>

***

## How in-app messages are shown

In-app messages are not actively pushed. Instead, they're pulled at app start based on audience, then displayed based on trigger logic.

<Frame caption="In-app message display logic flow">
  <img src="https://mintcdn.com/onesignal/Z6xkXGfmy814If53/images/docs/e1ce302cd1350e6c9e5616937a8068329fe61619884cd62889cd1772fd29999d-1c688b0-lifecycle-of-an-in-app.png?fit=max&auto=format&n=Z6xkXGfmy814If53&q=85&s=7a7552973b2746cd2ffa36137e743675" alt="Flowchart showing the lifecycle of an in-app message from audience check to display" width="2036" height="815" data-path="images/docs/e1ce302cd1350e6c9e5616937a8068329fe61619884cd62889cd1772fd29999d-1c688b0-lifecycle-of-an-in-app.png" />
</Frame>

The message displays if:

1. The User meets audience criteria **before** a new session starts.
   * A new session starts when the User opens your app after it has been in the background or closed for at least 30 seconds.
   * If the User has the app open when the message goes live or enters the Segment during the same session, they must close or background the app for at least 30 seconds to be eligible.
2. The trigger conditions are met.
3. The scheduled time and frequency are valid.

If Segment criteria change mid-session, the User must reopen the app to see the message.

### Testing

<Steps>
  <Step title="Add verbose logging to your app">
    Add the [`setLogLevel` method set to `Verbose`](./mobile-sdk-reference#setloglevel) in your app to get more detailed logs.
  </Step>

  <Step title="Make sure your Subscription is in the Segment">
    As explained in [How in-app messages are shown](#how-in-app-messages-are-shown), the User must match the audience criteria **before a new session starts**.

    * See [Find devices and set test Users](./find-set-test-subscriptions) if you don't know your device's Subscription ID.
    * Make sure your device's Subscription is in the included Segment(s) and not in the excluded Segment(s).

    <Tip>
      Add your device as a test Subscription and create or update the Segment to include the **Test Users** filter.
    </Tip>
  </Step>

  <Step title="Close or background the app for at least 30 seconds">
    This ensures you open the app to create a new session and become eligible for the message.
  </Step>

  <Step title="Check trigger conditions">
    Make sure you satisfy the [triggers](#triggers) for the message to be shown.
  </Step>

  <Step title="Check the schedule and frequency">
    * Make sure the "Start showing" and "Stop showing" dates are set correctly.
    * Set [display frequency](#display-frequency) to "Every time trigger conditions are satisfied" while testing.
  </Step>

  <Step title="Update the message and make sure it is active">
    Once the message is active, open the app on your device. You should see the message display based on your trigger conditions.
  </Step>
</Steps>

### Test and preview

The **Test & Preview** button sends a push notification to your selected test device. When you click the push to open the app, the in-app message displays.

Requirements and notes:

* Your device must be a [test User](./find-set-test-subscriptions)
* Your device must be subscribed to push — test in-app messages are triggered via push notification
* Push is only sent for testing purposes and will not be sent when the message is live
* Tag substitution does not work for test in-app messages
* If you are not seeing the message, follow the [testing steps](#testing) above

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

## Tutorials and use cases

<Columns cols={2}>
  <Card title="Personalize in-app messages" icon="wand-magic-sparkles" href="./example-tag-substitution">
    Personalize your in-app message content with Tags.
  </Card>

  <Card title="Target outdated app versions" icon="mobile" href="./app-version-update">
    Prompt Users to update their app.
  </Card>

  <Card title="App store review prompts" icon="star" href="./example-app-store-review">
    Increase your ratings with timely review requests.
  </Card>

  <Card title="Create User surveys" icon="square-poll-vertical" href="./example-create-a-survey">
    Collect feedback inside your app.
  </Card>

  <Card title="Push permission prompts" icon="bell" href="./prompt-for-push-permissions">
    Improve push opt-in rates with pre-permission prompts.
  </Card>

  <Card title="Location permission prompts" icon="location-dot" href="./location-opt-in-prompt">
    Ask Users to enable location tracking.
  </Card>

  <Card title="Set up a tutorial" icon="graduation-cap" href="./example-create-a-tutorial">
    Guide Users through new features of your app.
  </Card>
</Columns>

***

## Analytics

Track message performance and engagement.

<Columns cols={2}>
  <Card title="In-app message reports" icon="chart-line" href="./in-app-message-reports">
    Impressions, clicks, dismissals, and conversion metrics for in-app messages.
  </Card>

  <Card title="Analytics overview" icon="chart-bar" href="./analytics-overview">
    All analytics options available in OneSignal.
  </Card>

  <Card title="Event Streams" icon="signal-stream" href="./event-streams">
    Stream push events to your data warehouse or BI tools in real time.
  </Card>
</Columns>

***

## FAQ

### Do in-app messages require push notification permission?

No. In-app messages are delivered to all mobile Subscriptions in the target Segment, regardless of push opt-in status. They display inside the app during an active session.

### Why isn't my in-app message showing?

The most common cause is that the User's session didn't refresh. The User must close or background the app for at least 30 seconds, then reopen it to start a new session. Also verify the User is in the target Segment and that trigger conditions are met. See [Testing](#testing) for a full checklist.

### Can I send in-app messages via the API?

Yes. You can create in-app messages via the [Create message API](/reference/create-message). You can also trigger them within [Journeys](./journeys-overview) for automated flows.

### How are in-app messages different from push notifications?

In-app messages display inside your app while the User is actively using it. Push notifications appear on the device's notification tray and can reach Users even when the app is closed. In-app messages do not require push permission and are pulled at session start rather than pushed from the server.

### Can I use in-app messages on web?

No. In-app messages are only available for mobile apps with the OneSignal mobile SDK installed. For web, consider using [web push notifications](./web-push-setup) instead.

Built with [Mintlify](https://mintlify.com).
