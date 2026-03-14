# Source: https://documentation.onesignal.com/docs/en/journeys-messages.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Journey messages

> Send messages in all channels within Journeys

## Send a push notification

Select the Message Template you would like to send. We strongly encourage naming the template something recognizable so you can easily find it in the dropdown.

Message scheduling is not currently supported. When a user reaches this step in your Journey they will be sent the message immediately.

## Send an in-app message

First, ensure that you’re set up to support [sending In-App Messages](./in-app-messages-setup).

Once set up, you can add an In-App Message (IAM) node to your Journey by clicking on the (+) and selecting “In-App Message”. This will open up a side panel where you can manage the content and format of your message via [drag and drop](./design-your-in-app-message) or [HTML editor](./design-your-in-app-message-with-html).

Aside from the content of the message, you also have the option to set [trigger conditions](./iam-triggers) for the message as well as a delivery schedule. Triggers define when the message should display and the Delivery Schedule defines the duration of time the user has to open the app to receive the message.

Currently for IAMs to display, the user must have reached the Journey IAM node before a new session. A new session is when the app is out of focus for 30 seconds+ and put back into focus. After the user reaches the IAM node, they are eligible to get the message based on the trigger conditions and delivery schedule. Users that enter the IAM node during the current session are not eligible to get the IAM until a new session begins.

Example: a user gets a [Data Tag](./add-user-data-tags) set using the SDK. This enters them into the journey and they pass the IAM step. The user will not get the IAM until they close the app for 30+ seconds, then open it again because this starts the new session. If the user entered the Journey and passed the IAM step before opening the app, then they should see the IAM once the trigger conditions are met assuming they are within the Delivery Schedule.

<Info>
  Currently, In-App Messages within a Journey will only show once and never
  again to that user. Even if the user re-enters the Journey, the message will
  not display again to that user.
</Info>

## Send an email

First ensure you’ve set up your app to support [sending email](./email-setup).

Select the Message Template you would like to send. We strongly encourage naming the template something recognizable so you can easily find it in the dropdown.

Message scheduling is not currently supported. When a user reaches this step in your Journey they will be sent the message immediately.

## Send an SMS

First ensure you’re set up to support [sending SMS](./sms-messaging).

Next, make sure you’ve created an SMS template with the messaging you’d like to send out from your Journey. You can access this by:

* Clicking on “Messages” at the top of your screen
* Then click on “Templates”
* Finally click “(+) New Template” where you’ll select “New SMS Template”

Then, in your Journey, click on the (+) to add an SMS node. This will open up the side panel where you can select the template you’d like to send out at that specific point in the Journey. Once users reach that step in the Journey, SMS messages will send out to them immediately.

***

Built with [Mintlify](https://mintlify.com).
