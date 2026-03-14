# Source: https://documentation.onesignal.com/docs/en/iam-click-actions.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# In-app click actions

> How to create Click Actions for an In-App Message.

<Frame caption="Image. Shows the flow of using Click Actions to form Location and Push prompts for iOS">
  <img src="https://mintcdn.com/onesignal/yt4lRKoquAlWvRvF/images/iam/a800e8b-Click_Action.png?fit=max&auto=format&n=yt4lRKoquAlWvRvF&q=85&s=3aa66c522aa9ed079e096e3386c2bff9" width="2574" height="1244" data-path="images/iam/a800e8b-Click_Action.png" />
</Frame>

## Click actions

Click Actions are specific events that can be added to in-app messages to make them more interactive. They can be added to blocks when using the drag-and-drop editor or to any element in the HTML editor (see [In-app JavaScript API](./in-app-message-api)).

Click actions include the following abilities:

### URL

Leaves the app and opens the default browser to the URL you specify.

Maps to the `openUrl` method when using the [In-App JS Library](./in-app-message-api).

### Push permission prompt

Shows the native iOS or Android Push Permission Prompt.

* If the iOS or Android device is currently subscribed, the In-App Message will not show.
* If the iOS or Android device is currently unsubscribed and has been prompted previously, it will show a native alert asking the user to enable push notifications in the app settings.

Maps to the `triggerPushPrompt` method when using the [In-App JS Library](./in-app-message-api).

### Location permission prompt

Shows the native operating system prompt to ask permission for location tracking. Requires [location tracking permissions](./mobile-sdk-reference#location) to be added to your app. See [Location Opt-In Prompt](./location-opt-in-prompt) for details on setup.

Maps to the `triggerLocationPrompt` method when using the [In-App JS Library](./in-app-message-api).

### Send Outcome

Tracks user interaction for analytics purposes. Outcomes sent through In-App messages will show as "Unattributed" Outcomes and will set a [Tag](./add-user-data-tags) on the user in format `outcome name : true`. See [Custom Outcomes](./custom-outcomes) for more details.

Maps to the `sendOutcome` method when using the [In-App JS Library](./in-app-message-api).

### Tag user

Adds a [Tag](./add-user-data-tags) to the user to express interest and later segment into another group based on user response to send more targeted messaging.

Maps to the `tagUser` method when using the [In-App JS Library](./in-app-message-api).

### Custom Action ID

Pass a custom value that, when clicked, can be read within the app using the [OneSignal SDK IAM Click Listener method](./mobile-sdk-reference#addclicklistener-in-app)

Used for custom action handling like:

* Click detection to perform custom event like send data to your own server or analytics vendor.
* [Deep Linking within the app](./deep-linking).

Maps to the `addClickName` method when using the [In-App JS Library](./in-app-message-api).

***

## How to collect custom click actions

When an Image or Button block is clicked, you can use the **Custom Action ID** and set a value to identify that block was clicked. This Action ID can then be detected through the [OneSignal SDK IAM Click Listener method](./mobile-sdk-reference#addclicklistener-in-app) and that data can be sent to your server/date base/analytics vendor.

<Accordion title="Example: create a poll" icon="square-poll-vertical">
  ### Example: create a poll

  If you want to survey your users with a multiple choice questionnaire and then display their choices within the app. You can setup the Action ID per button to be a unique identifier for that option. Whenever that option is clicked, it will be detected in the [OneSignal SDK IAM Click Listener method](./mobile-sdk-reference#addclicklistener-in-app). From there, you can make an API request to your server to store that data and access it within the app later to display to your users.
</Accordion>

***

## How to deep link within the app

See [Deep Linking](./deep-linking) for details.

***

## How to create a rating action

There are several ways to get reviews from your users.

The simplest way is to use the URL click action to deep link directly to the App Store.

* iOS: [Apple's documentation](https://developer.apple.com/library/archive/qa/qa1633/_index.html)
* Android: [Linking to Google Play](https://developer.android.com/distribute/marketing-tools/linking-to-google-play.html)

You can also trigger native APIs via the Action ID to display the review prompt directly in the app.

* iOS: [RequestReviewAction documentation](https://developer.apple.com/documentation/storekit/requestreviewaction)
* Android: [Google Play In-App Reviews API documentation](https://developer.android.com/guide/playcore/in-app-review)

More details, see [Example: Ask for App Store Rating](./example-app-store-review).

***

Built with [Mintlify](https://mintlify.com).
