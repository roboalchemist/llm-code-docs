# Source: https://documentation.onesignal.com/docs/en/notification-ctr.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Notification CTR

> Troubleshooting low notification click through rates

Click Through Rate (CTR) is measured by (clicks / delivered) \* 100% and represents how many notifications were clicked based on how many were delivered to the FCM/APNS servers who then send it to your subscribers. For detailed metric definitions, see the [Metrics Glossary](./analytics-metrics-glossary). CTR does not count:

* swiping away the notification
* clicking "Dismiss"
* clearing notifications

## Best practices

CTR for push notifications varies widely among different platforms (Android, iOS, Web), vertical (news, games, travel, ecommerce, etc), type of notification (message from a friend, promotion, informative update), country, etc. Not unlike email, the variance is so wide as to make averaging a bit muddy.

To help with maximizing clicks on push, we regularly publish blog posts and best practices on how to utilize OneSignal to get the maximum engagement from users.

A common best practice to increase CTR and user engagement is to send subscribers messages based on topics they are interested in. If your app publishes a wide range of topics and you send more than 1 notification a day, your users likely don't want to know about every push you send.

Websites can easily ask users what they would like notifications about using our [Category Slidedown Prompt](./permission-requests). This will allow you to group users by the different topics you offer so you can setup [Segments](./segmentation) and target users with the notifications they care about.

More actionable ideas:

* [Increase Your Push Notification CTR with Intelligent Delivery](https://onesignal.com/blog/increase-open-rates-by-up-to-23-percent-with-intelligent-delivery)
* [6 Best Practices for Push Notifications](https://onesignal.com/blog/6-best-practices-for-push-notifications)
* [Best Practices for News Publications: Push Notification Frequency & Content](https://onesignal.com/blog/news-publishers-5-best-practices-for-sending-push-notifications)

## Troubleshooting low CTR

There are a couple reasons that CTR could be dropping, review the below questions for common issues and solutions:

### Who are you targeting?

Over time, your users will get new devices. They will likely not unsubscribe from your app or website on the old device, but they may subscribe to your app or website on the new device. In this case, there will be 2 subscriptions for this user. You can clean up older subscriptions by [Deleting Users](./delete-users).

<Card title="Free plan limitations">
  Free plans can only target 10,000 Web Push subscribers. No limits on Mobile App subscribers. If you have more than 10,000 web push subscribers, you may be sending to older devices. You can [Delete Users](./delete-users) to target newer subscribers or upgrade to a paid plan.
</Card>

<Card title="Changed sending patterns">
  Have you or your team started sending more or less notifications since the drop? Perhaps you started sending more API messages and less Marketing Messages.

  Did you change any of the segments being targeted? For instance did you used to send notifications to all users, but around the date of the drop, you started sending to less users within the segments.
</Card>

### What metrics are you specifically tracking?

Are you only tracking marketing messages, transactional messages, or are you tracking all messages?

Clicks would be the actual click event, where CTR could change based on how many devices are being sent to. This can vary depending on the message type, so it is important to know what you are measuring.

### What are you sending?

You could be suffering from boring notifications. Data shows adding flare to the notification gets more clicks. This can be emojis, images, icons, personalizations, localizations or just engaging words.

<Card title="Some examples of this can be found in our blog and documentation">
  * [Using Emojis](https://onesignal.com/blog/how-to-use-emojis-push-notifications/)
  * [Notification Appearance](./push)
  * [Message Personalization](./message-personalization)
  * [Language & Localization](./multi-language-messaging)
</Card>

### When did you the drop start?

Its important to check what specific timeframes are you comparing and ask, what date did you start seeing a decrease in clicks and what dates in the past are you comparing with?

If you are comparing CTR to a timeframe when you were sending at a different volume, had less subscribers, etc. then CTR may not be comparable.

### How are you gathering analytics data?

What reporting tools are you reviewing and how is the data generated?

OneSignal provides a [Dashboard](./analytics-overview) that shows the number of clicks and CTR for each message sent. You can also export the [Audience Activity](./push-notification-message-reports#audience-activity) to see the list of users that received the message, and what they registered a click event.

### How many notifications are you sending?

If you are sending too many notifications, this can be perceived as spam to users. How many is too many?

This can be different depending on the platform and type of notifications you are sending, but if you are sending excessively to users every few hours with content they may not be interested in, that usually leads to low CTR.

### Did anything change?

Below are examples of code changes that could affect your click metrics.

<Card title="OneSignal not active on all pages or initialized">
  Websites should include OneSignal on all or most pages of the site for best performance.

  Mobile Apps should initialize OneSignal in the specific ways discussed in our [Mobile Quickstart](./mobile-sdk-setup) guides.
</Card>

<Card title="Multiple service workers">
  Web Push Notifications require Service Workers to run on the browser so the user can receive push. Adding multiple Service Workers on a website (for example a service worker for PWA) can cause issues with push being received and CTR.

  Please see our [Guide on adding multiple Service Workers to your site](./onesignal-service-worker)

  If you have already fixed this or removed the other service worker, then users will need to return to the site for our service worker to be added again.
</Card>

<Card title="Notification Service Extensions">
  For Mobile Push, if you setup the Android [Notification Service Extension](./service-extensions) and are calling `complete(null)` and displaying your own notification with Android API then this will stop clicks.

  `complete(null)` suppresses the SDK's notification so OneSignal can't know that you generated a notification and therefore can't count click events.

  iOS Apple does not allow the remote notification to be suppressed like Android. So this can't be an issue for iOS.
</Card>

***

Built with [Mintlify](https://mintlify.com).
