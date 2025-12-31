# Source: https://firebase.google.com/docs/in-app-messaging/compose-campaign.md.txt

<br />

## Before you begin

Make sure you complete the steps in[Get Started](https://firebase.google.com/docs/in-app-messaging/get-started)to ensure you have an app with Firebase enabled and have added the latestFirebase In-App MessagingSDK.

## Create a new campaign

Set up your new campaign in theFirebaseconsole's[Messaging page](https://console.firebase.google.com/project/_/messaging).

- If you are a first time user, click**Create your first campaign**.
- If not, click**New campaign**.

### Step 1: Style and content

In the console, useFirebase In-App Messagingmessage templates to incorporate different features to serve different purposes with your in-app messages.

[Explore use cases](https://firebase.google.com/docs/in-app-messaging/explore-use-cases)to see examples for stylizing the messages templates.

|              Message Template Type               ||||        Feature        |                                                                                                                                                Feature Description                                                                                                                                                 |
| Feature | Feature Description |
|---------|---------------------|------------|--------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Card    | Modal               | Image only | Banner |
| lens    | lens                | lens       | lens   | Image                 | Provide an HTTPS Image URL. You can use[Firebase Hosting](https://firebase.google.com/docs/hosting)to host your images.                                                                                                                                                                                            |
| lens    | lens                | lens       | lens   | Action                | Use weblinks or deep links to send your users to external pages or specific pages in your app. You can use[Firebase Dynamic Links](https://firebase.google.com/docs/dynamic-links)to create and manage deep links. Templates**Modal** and**Image only**include an X button, allowing users to dismiss the message. |
| lens    | lens                |            | lens   | Text/background color | Customize the message visuals by entering the Hex Color Code or using the color gradient to find the specific hue that matches your brand.                                                                                                                                                                         |
| lens    | lens                |            | lens   | Message title/body    | Catch your user's attention with a relevant header and a concise description. Firebase automatically translates and scales your text to accommodate your users.                                                                                                                                                    |
| lens    | lens                |            |        | Primary button        | The default button action is set to dismiss the message. Provide a URL to redirect users as the action.                                                                                                                                                                                                            |
| lens    |                     |            |        | Secondary button      | The default button action is set to dismiss the message. Provide a URL to redirect users as the action.                                                                                                                                                                                                            |

<br />

1. InFirebaseconsole's**Compose campaign**window, customize your message to your liking with the features available to each template.

2. On the right-hand side of the**Compose campaign**window, preview your message in landscape or portrait orientation for a phone or tablet device.

   The in-console preview provides a general idea of how your message appears on a mobile device. Actual message rendering varies depending on the device.[Test with a real device to see the exact rendering](https://firebase.google.com/docs/in-app-messaging/get-started#send_a_test_message).
3. If desired, define custom metadata for your campaign. This metadata will be available on the client side using SDK callbacks when a campaign is displayed to a user. For example, you might want to tag the campaign with a promo code that you can use on the client.

### Step 2: Target your users

1. Enter a name for your campaign.

   This name is used for campaign reporting and is not part of the visible message.
2. (Optional) Provide a campaign description.

   This description is used for campaign reporting and is not part of the visible message.
3. Click on the**Select app**dropdown and identify which app you want to associate with this campaign.

4. (Optional) Click the**and**button to further narrow down your target users.

   Use the**Select**dropdown to choose additional specifications.
5. View the percentage of potential users that are eligible for this campaign.

   This number is estimated based on active users who contacted the service in the last 7 days. Eligible users only see this message if a trigger condition occurs.
6. (Optional) If your app targets users in multiple languages, you will be prompted to localize the campaign in those languages. Use the dialog to either add your own translations or use Google Translate to localize the campaign easily.

### Step 3: Scheduling your message

1. Describe a start date and time for your campaign.

   Your campaign can start when you publish the campaign or have a scheduled start.
2. Describe an end date and time for your campaign.

   Your campaign can run indefinitely or have a scheduled endpoint.
3. Click Event + to add at least one trigger event.

   - You can enter default events or[events logged through Firebase Analytics](https://firebase.google.com/docs/analytics/android/events)to trigger your in-app message. These events can be user actions, system events, or errors.
   - Your in-app message is triggered when any of your events occur.
4. Specify your per-device frequency limit. The limit allows you to control how often your users see your message.

   - By default, a campaign is not shown after it has been viewed by (that is, impressed on) the user once.
   - Or, you can set the frequency of messages in days.

### Step 4: Conversion events (optional)

Firebase tracks the number of impressions that result in a completed conversion event.

1. In the**Compose campaign** window, use the**Select conversion event**dropdown to choose from:

   - The default conversion events.
   - Any[events you enabled as conversions](https://support.google.com/firebase/answer/6317522#enable).
2. After you publish the campaign, go to the[Messaging page](https://console.firebase.google.com/project/_/messaging)and click on the campaign's name to see data related to the campaign's conversion history.

## Publishing your campaign

After modifying your campaign, you can click**Save as draft**for the option to return and edit the campaign in draft status.

Or, you can click**Publish**to release your message to targeted users on the scheduled date. You can edit your campaign after it has been published.

Once you stop a published campaign, you will not be able to publish it again. However, you may stop or edit a running campaign at any time. You can also duplicate an existing one to make slight variations and avoid creating a completely new campaigns.

## Get AI insights for messaging campaigns with Gemini inFirebase

Gemini inFirebaseprovides messaging campaign summarization, insights, and guidance to improve yourFirebase Cloud MessagingandIn-App Messagingcampaign performance. By analyzing campaign data, Gemini inFirebasecan help you understand your campaigns' reach and impact and suggests strategies to improve user engagement and growth.

### Access AI insights for messaging campaigns

To use messaging campaign AI insights, make sure that your project has the following:

- Gemini inFirebaseis enabled for your project. Learn more at[Set up Gemini inFirebase](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase/set-up-gemini).

- Firebase Cloud MessagingorIn-App Messagingis enabled in your Firebase project.

- At least one campaign exists and appears in theFirebaseconsole.

After ensuring these requirements are met:

1. Open[**Messaging**](https://console.firebase.google.com/project/_/messaging)in theFirebaseconsole to access campaign data.

2. After your campaign data loads, click**Generate AI insights**.

   A summary and analysis of your messaging campaigns appears.

### Pricing

See[Gemini inFirebasepricing](https://firebase.google.com/docs/ai-assistance/gemini-in-firebase#pricing)for more information.