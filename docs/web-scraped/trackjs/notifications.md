# Source: https://docs.trackjs.com/notifications/

Title: Notifications

URL Source: https://docs.trackjs.com/notifications/

Markdown Content:
You can manage your notifications from the [Dashboard Notifications page](https://my.trackjs.com/Account/Notifications). You can customize which notifications you receive and where they’re delivered.

[Channels](https://docs.trackjs.com/notifications/#channels "Permalink Here")
-----------------------------------------------------------------------------

Notifications are sent to “Channels”. We currently support Email, Slack and Microsoft Teams. The channel list is on the right-hand side of the page. You may see your existing channels, the number of notifications they’re subscribed to, and the ability to create new channels.

[Notification Types](https://docs.trackjs.com/notifications/#notification-types "Permalink Here")
-------------------------------------------------------------------------------------------------

On the left-side, you’ll see each type of notification that can be sent, settings, and which channels to send the notification to. You can route different kinds of notifications to different channels. For example, you can send the Daily Summary to the full dev team, but New Errors perhaps only to the front-end developers.

Both the type of Notifications and Channels are configurable per [application](https://docs.trackjs.com/data-management/applications/).

### [Daily Summaries](https://docs.trackjs.com/notifications/#daily-summaries "Permalink Here")

Sent daily at a configurable time via email. This notification contains error rate, error delta, top errors for various categories and other information. It’s a rollup view of the previous 24 hours. It can only be sent to email channels.

### [New Errors](https://docs.trackjs.com/notifications/#new-errors "Permalink Here")

Sent when TrackJS records a never-before-seen error message in your account. You may also customize this, and have it only alert if more than one user is affected. This is handy when a single user is responsible for many one-off errors.

### [Trending Errors](https://docs.trackjs.com/notifications/#trending-errors "Permalink Here")

Sent when there is a substantial increase in the frequency of an existing error. That is, the error was previously seen, but it is now occurring more frequently. This is particularly useful for high traffic sites when there are hundreds or thousands of unique error messages.

We record the ranking of the errors in your accounts, you can see this in the [Trending Errors Report](https://my.trackjs.com/trends). The Trending Notification will be sent if an error gains more than 10 places or if a new error is in the top 10 most common errors on your site. In order to keep noise to a minimum, we require an error to be seen a minimum of 10 times before an alert is sent.

### [Error Rate Increase](https://docs.trackjs.com/notifications/#error-rate-increase "Permalink Here")

Sent when the overall error rate for an application increases 20% above the previous high. We look back several days to ensure it’s not just a cyclical traffic increase. Please note that if your incoming error rate is high enough to cause [throttling](https://docs.trackjs.com/data-management/limits/#capture-throttle), the error rate increase alerts may also be affected.

[Saved Filter Notifications](https://docs.trackjs.com/notifications/#saved-filter-notifications "Permalink Here")
-----------------------------------------------------------------------------------------------------------------

In addition to the options above, it’s also possible to make custom notifications using saved filters.

#### [Saving a Filter](https://docs.trackjs.com/notifications/#saving-a-filter "Permalink Here")

To make a custom notification, the first thing you need to do is create a filter for the errors you care about. After you’ve filtered to the relevant errors, click the “share” dropdown in the upper right hand corner of the UI. A menu will appear and you can enter a name for your filter. Click the **Save** button.

![Image 1](https://docs.trackjs.com/assets/images/saved-filter-share-dropdown.min.png)

#### [Configuring Alerts for a Saved Filter](https://docs.trackjs.com/notifications/#configuring-alerts-for-a-saved-filter "Permalink Here")

Once saved, you can click the [Manage Alerts](https://my.trackjs.com/account/notifications/saved-filter) link from the same “share” dropdown. You’ll see a list of all your saved filters, and any pre-existing notification channels.

![Image 2](https://docs.trackjs.com/assets/images/notification-screen.min.png)

Find the saved filter you want to configure alerts for and click the “+ Add Notification” link.

#### [Customizing Notifications](https://docs.trackjs.com/notifications/#customizing-notifications "Permalink Here")

The new saved filter notifications work using four different strategies (more on that below). Those strategies are based on a **Lookback Period** and an **Error Threshold**.

![Image 3](https://docs.trackjs.com/assets/images/notification-modal.min.png)

The **Lookback Period** is how large of a time window to use when considering a filter’s error volume. The **Error Threshold** is the minimum number of errors that must occur during the lookback period before an alert is sent.

For example, if a filter has a high base level of errors, it might make sense to set the error threshold high, and a short lookback window. This way you’ll need a decent spike in a short period of time to cause an alert.

On the other hand, if there’s a situation where you want an alert any time an error matches a filter - a longer window with a lower threshold will make the alert more sensitive.

#### [How it Works](https://docs.trackjs.com/notifications/#how-it-works "Permalink Here")

We use four different strategies when determining whether to alert. Each strategy will decide to trigger or not based on the filter’s error volume over time. **Two** of the strategies must be triggered in order for a notification to be sent (this cuts down on noise and false positives). We use the following strategies:

*   _Simple Historical Average_: This simple strategy compares the filter’s historical average error volume to the lookback period’s current volume and, if the current volume exceeds a multiple, triggers.
*   _Standard Deviation_: This strategy triggers if a filter’s current error volume is multiple standard deviations higher than the historical volume.
*   _Moving Average_: If the moving average of the error volume in the lookback period is several multiples higher than the historical volume, the strategy is triggered.
*   _ML Detection Strategy_: An ML prediction strategy which finds spikes in time series data based on adaptive kernel density estimations and martingale scores. If the confidence is over 99.9% the strategy triggers.
