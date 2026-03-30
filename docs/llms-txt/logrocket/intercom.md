# Source: https://docs.logrocket.com/docs/intercom.md

# Intercom

Integrating LogRocket with [Intercom](https://intercom.com)

The LogRocket integration with Intercom makes it easier to reproduce issues reported by users over Intercom.

### Basic Integration

After setting up the integration, our helpful bot will provide a link to a list of all of the relevant user's sessions with every customer support request:

<Image align="center" src="https://files.readme.io/417629da29b51d1d18ff84d93b250a1127587b4d2a333ca28619d5ea83fce035-Group_8_1.png" />

### AI-Powered Summaries from Galileo Highlights

[Galileo Highlights](https://docs.logrocket.com/docs/galileo-highlights-beta) helps you quickly pinpoint key moments in LogRocket sessions. With this AI-powered tool, you can effortlessly find the exact interaction you're looking for in a session. When the Highlights Intercom integration is enabled, LogRocket automatically posts a private comment summarizing each user’s activity leading up to their support request. The focus is on the context and content of their question, giving you immediate insight into the issue.

Key Benefits:

* Instant Context: Get a concise summary of what the user did before submitting their request, allowing you to understand the problem at a glance.
* Quick Access: Direct links to the full session are provided, enabling you to dive deeper whenever necessary.\
  With Galileo Highlights, resolving support issues has never been faster or more intuitive.
* Visual Insights: View screenshots of significant moments from the session, so you can grasp the situation without needing to watch the entire session.

Contact [support@logrocket.com](mailto:support@logrocket.com) for access to this feature, which is available for Pro and Enterprise plans. We offer a complimentary trial period followed by a range of pricing options.

<Image align="center" src="https://files.readme.io/87fe964cbd6f400466baf143fbf93bf2c73c2cc9114d9f27709095791de2b521-Screenshot_2024-08-21_at_3.14.06_PM.png" />

<br />

## Install

In the Integrations tab of the settings page, simply click on the Intercom integration button to automatically set it up. You will be redirected to Intercom to authenticate. After that you can click that button again to change settings.

![](https://files.readme.io/e97c088-Screen_Shot_2018-01-29_at_11.00.57_AM.png "Screen Shot 2018-01-29 at 11.00.57 AM.png")

> 🚧 Troubleshooting
>
> If you're not getting a note posted in your conversations, be sure of the following:
>
> 1. The app you are recording sessions on has the integration enabled.
> 2. You are identifying your users using [`LogRocket.identify()`](https://docs.logrocket.com/reference/identify) and through Intercom using the same user ID or email.
> 3. LogRocket sessions exist for that user and the user is not blocking LogRocket.
> 4. At least 15 seconds has elapsed after calling `LogRocket.identify()` before a user started a conversation for the first time. This is due to network lag and server-side processing time.

<br />

> 🚧 Important Limitation
>
> You can **not** link the same Intercom app to multiple LogRocket organizations

## Adding Profile Links

While the integration covers most use cases, you can also add LogRocket session links to your Intercom user profiles.

To set this it up, add this code to your Intercom-enabled app:

```javascript
Intercom('update', {
  // TODO: replace YOUR_ORG/YOUR_APP below with your AppID, and userID with your user's ID.
  logrocketURL: `https://app.logrocket.com/YOUR_ORG/YOUR_APP/sessions?u=${userID}`,
});
```

We then recommend you add this "logrocketURL" to the User List:

![](https://files.readme.io/779934d-Image_2017-06-09_at_4.13.44_PM.public.png "Image 2017-06-09 at 4.13.44 PM.public.png")

The URL will then appear in the "User Pane" during a conversation:

![](https://files.readme.io/3bc99cc-Image_2017-06-09_at_4.16.01_PM.public.png "Image 2017-06-09 at 4.16.01 PM.public.png")

You can also track LogRocket session URLs to have them appear in the user activity timeline:

```javascript
LogRocket.getSessionURL(function (sessionURL) {
  Intercom('trackEvent', 'LogRocket', { sessionURL: sessionURL });
});
```

You will then see a list of LogRocket events in the Intercom pane for every user:

![](https://files.readme.io/2c3477c-Screenshot_2016-09-28_08.00.07.png "Screenshot 2016-09-28 08.00.07.png")