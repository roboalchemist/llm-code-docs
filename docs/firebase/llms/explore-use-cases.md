# Source: https://firebase.google.com/docs/in-app-messaging/explore-use-cases.md.txt

<br />

Engage your audience in meaningful ways with modifications to the style, targeting, and scheduling of your messages entirely through the[Firebase console](https://console.firebase.google.com/project/_/messaging).Firebase In-App Messagingoffers message templates for you to experiment with and customize to your liking.

## Customize your message UI

You can style your messages with templates that are designed for creating engaging and clean user interfaces. Here are the available templates:

| Message Template |                                                 Description                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------|
| **Card**         | - Structured message with two action buttons - Offers users a choice                                        |
| **Modal**        | - Flexible message dialog with one action button - Only the message title is required --- use what you need |
| **Image only**   | - Upload your custom designed message - Easy to incorporate your aesthetics                                 |
| **Banner**       | - Notification-like message - Doesn't take up a lot of screen space                                         |

<br />

[Learn more about messaging templates](https://firebase.google.com/docs/in-app-messaging/compose-campaign#style-and-content)

Use the**Image only**message template, uploading your designed message to:

- Incorporate the exact colors, fonts, and formatting that are tailored to your app's aesthetic and branding.
- Offer a themed promotion. Send out your Halloween discount in a message with a custom scary font and background pattern. The entire message is clickable for the user to learn more or dismiss the message.

<br />

![](https://firebase.google.com/static/docs/in-app-messaging/images/image-only.png)

<br />

Want even more freedom? Modify the display of Firebase's message templates through code.

[Learn more](https://firebase.google.com/docs/in-app-messaging/customize-messages)

## Target specific users

For each campaign, you can target messages to certain audiences based on their behavior, language, engagement, and more.

Consider combining a**Card**message with a deep linking solution, configuring the targeting of the message to:

- Target users with a**Last app engagement**between one to seven days to make sure they are active. Ask your engaged users if they are enjoying your app. Depending on their answer, use a smart link to direct them to Google Play for a review or to a feedback survey.
- Let users explore your social media app without pressures to register for an account. Target your authentication message at users that**First Open**your app at least two days ago, and use an in-app linking system to guide them to the relevant screen.

<br />

![](https://firebase.google.com/static/docs/in-app-messaging/images/card-visual.png)

<br />

[Learn more](https://firebase.google.com/docs/in-app-messaging/compose-campaign#target-your-users)

## Schedule messages with contextual triggers

Messages only appear while users are in your app and are triggered by certain events, ensuring that the messages stay relevant and contextual for your users. You don't want to distract users who might be in the middle of a high-score- setting game or an important purchase.

For instance, you can configure the scheduling of your**Banner**message to:

- Congratulate users whenever they level up in your game app by setting a`level_up`event as a trigger.

Avoid spamming your users by setting a per-device frequency limit for your**Banner**message to:

- Gently remind users to update your app by setting the number of messages to no more than one message every 15 days. Users can easily click to engage or dismiss with a swipe up.

<br />

![](https://firebase.google.com/static/docs/in-app-messaging/images/banner-visual.png)

<br />

[Learn more](https://firebase.google.com/docs/in-app-messaging/compose-campaign#schedule-your-message)

## Track your app's performance

You can combineFirebase In-App Messagingwith[Google Analytics](https://firebase.google.com/docs/analytics)to reveal important details about your users' preferences and satisfaction with your app.

Enable Analytics events as conversions and track users' interactions with your messages. For example:

- Offer a promotional message with the**Modal**template's action button to discounted items. Firebase lets you know how many users received the message, how many clicked on it, and how many completed conversion event such as an e-commerce purchase.

Utilize callbacks to create a personalized experience for your users.

- Tackle important, text-heavy messages such as a terms of service update with the**Modal**template's flexible dialog orientation. Track which users consented to your terms of service and use callbacks to add users to an Analytics audience for better targeting.

<br />

![](https://firebase.google.com/static/docs/in-app-messaging/images/modal-visual.png)

<br />

[Learn more](https://firebase.google.com/docs/in-app-messaging/compose-campaign#conversion-events)