# Source: https://documentation.onesignal.com/docs/en/app-version-update.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Target outdated app versions to encourage app updates

> Learn how to target outdated app versions with OneSignal In-App Messages using version-aware triggers to prompt users to update. Includes segmentation strategy and setup guidance.

In-app messages (IAMs) are a powerful tool to notify users on older versions of your app that a newer version is available and encourage them to update.

***

## Requirements

* Your app must be using the latest v5 version of the OneSignal SDK

***

## Setup

**Example scenario**: The latest version of our app is `1.0.1`. We want to target users on version `1.0.0` and older with an in-app message prompting them to update.

### 1. Get your latest app version

OneSignal detects `App Version` based on the following:

**iOS**: The `Version` found in Xcode **your main app Target > General > Identity**

<Frame caption="iOS App Version found in Xcode">
  <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/mobile/ios-version.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=4c6582a16d72787f02bce216ff5cd1c4" width="2104" height="1294" data-path="images/mobile/ios-version.png" />
</Frame>

**Android**: The `versionCode` found in your app `build.gradle` file

<Frame caption="Android App Version found in your app build.gradle">
  <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/mobile/android-version.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=ded4166d51b66edd8727904db655eee7" width="2302" height="1390" data-path="images/mobile/android-version.png" />
</Frame>

<Note>
  If you don't have access to Xcode and/or Android Studio, ask your developer for these values.
</Note>

<Warning>
  Notice the App Versions for iOS and Android are different! This is one reason why we need to create two separate segments and in-app messages.

  The 2nd reason we should use two separate segments is because the in-app message may contain links different for iOS and Android as we will see next.
</Warning>

### 2. Setup the segments

You will need to create two segments, one for iOS and one for Android.

**iOS**:

* Segment Name: `iOS App version less than 1.0.1`
* Filters: `App Version` is `less than` `1.0.1` AND `Device Type` is `iOS`.

<Frame caption="iOS Segment Filters">
  <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/segments/ios-appversion-segment.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=bf7436894a85d48780dfdade4c98f8d4" width="1498" height="902" data-path="images/segments/ios-appversion-segment.png" />
</Frame>

**Android**:

* Segment Name: `Android App version less than 10001`
* Filters: `App Version` is `less than` `10001` AND `Device Type` is `Android`.

<Frame caption="Android Segment Filters">
  <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/segments/android-appversion-segment.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=6411b3af8ff1a210fd876a62e1951820" width="1498" height="902" data-path="images/segments/android-appversion-segment.png" />
</Frame>

### 3. Setup the in-app messages

Navigate to **Messages > In-App > New Message > New In-App**.

Start from the pre-built design **New Feature Announcement** or create your own from scratch.

<Frame caption="New Feature Announcement">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/new-in-app-message-select.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=672e45bec1d7b137040c0e4cfda951a9" width="2310" height="1888" data-path="images/iam/new-in-app-message-select.png" />
</Frame>

Name the message something to reflect this is for iOS users.

#### Add your audience

Select the particular segment **iOS App version less than 1.0.1**.

#### Update the message

Update the message as you see fit.

To navigate the user to your app store listing, add a URL click action to a Button or multiple elements

<Frame caption="URL click action">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/url-click-action.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=c9895a060ca2edb109e395a232b920b5" width="1732" height="1164" data-path="images/iam/url-click-action.png" />
</Frame>

You can enter the store link as the URL. Details on how to get the correct store link for your app can be found in the following links:

* iOS - [https://developer.apple.com/library/archive/qa/qa1633/\_index.html](https://developer.apple.com/library/archive/qa/qa1633/_index.html)
* Android - [https://developer.android.com/distribute/marketing-tools/linking-to-google-play.html](https://developer.android.com/distribute/marketing-tools/linking-to-google-play.html)

### 3. Triggers

We recommend using the **On app open** trigger to ensure the message is shown when the user opens the app.

### 4. Schedule and frequency

If you scheduled the app update to be some time in the future, you can schedule the message to start showing at that time.

Depending on how aggressive you want to be with your update prompts, you can set the "How often do you want to show this message?" frequency to:

* **Every time trigger conditions are satisfied** - which means every time they open the app in this example.
* **Multiple times** - set the total number of times to show the message and what delay in between. For example, 100 times with a gap of 3 days in between. Will show the message every 3 days for up to 100 times.

### 5. Save as Draft and duplicate for Android

Click the **Save as Draft** button to save the message.

In the **In-App Messages** page, click **Options > Duplicate** next to the message you just saved.

Update the following for your Android users:

* The IAM name to reflect this is for Android users
* Set the Segment to **Android App version less than 10001**
* Update the URL to the Android store link
* Add any additional changes to the message to make it unique for Android users

Click **Save as Draft** to save the message.

***

## Testing

Before publishing your messages, we suggest testing them with the following steps:

<Steps>
  <Step title="Find your test device and set as a Test Subscription">
    * Find your test device and set it as a [Test Subscription](./find-set-test-subscriptions).
    * Make sure the test device is on the lower version of your app.
  </Step>

  <Step title="Update the Segment to include Test Users">
    * Open the in-app message you want to test.
    * Click the Segment and add an **And** filter for **Test Users**.
      * This will ensure the message only shows for your test devices
    * For example, if your test device is on iOS, the segment will look like this:
      <Frame caption="iOS Segment Filters">
        <img src="https://mintcdn.com/onesignal/FXJz6yFfOqztaEND/images/segments/ios-appversion-testusers-segment.png?fit=max&auto=format&n=FXJz6yFfOqztaEND&q=85&s=37a6a36b28f368cded643dac4fccf298" width="1406" height="946" data-path="images/segments/ios-appversion-testusers-segment.png" />
      </Frame>
    * Click **Update Segment** to save the changes.
  </Step>

  <Step title="Publish the message">
    * Click **Update Message** to update the in-app message.
    * Click **Options > Resume** next to the message to set it live.
  </Step>

  <Step title="Verify the message is shown">
    * Close the app on the test device.
    * Wait 1 minute.
    * Open the app on your test device.
    * You should see the message if:
      * The device is a Test Subscription
      * The device is on the lower version of your app.
      * The segment is set to **Test Users**.
  </Step>
</Steps>

***

## Go live checklist

When you are ready to go live:

* Update the Segments to remove the `Test Users` filter.
* Check the Schedule to make sure it is set to the correct date and time.
* Click **Update Message** to update the in-app message.

<Check>
  You're done! Any users that open your app on an older version will get notified of your App Update.

  Return to the in-app message after some time to check progress. You can also get in-app message analytics with [Event Streams](./event-streams) or 3rd party [Integrations](./integrations).
</Check>

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
