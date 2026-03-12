# Source: https://documentation.onesignal.com/docs/en/template-analytics.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Template analytics

> Analyze delivery statistics and audience engagement for messaging templates across push, email, and SMS channels in OneSignal. Leverage detailed reports, channel-specific metrics, and exportable audience data to optimize template performance.

## Template analytics overview

Template analytics provide insight into how your messaging templates perform across all supported channels—push, email, and SMS. With easy access to template reports, you can review delivery rates, engagement metrics, and troubleshoot issues, helping you optimize messaging strategies for better results.

A Template Report is available when you click any template in your dashboard. To make changes to the template, use the **Edit** button.

<Frame caption="Delivery statistics for a push template">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/85bc126e3da7a982997135243536bc4c474ad296286f30b60a996853faa7ceec-Screenshot_2025-05-01_at_14.42.53.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=9e3cdef17572b54fe84404dbed421d12" width="3066" height="2060" data-path="images/docs/85bc126e3da7a982997135243536bc4c474ad296286f30b60a996853faa7ceec-Screenshot_2025-05-01_at_14.42.53.png" />
</Frame>

<Note>
  🗃️ Data retention started April 16, 2025.

  Reports store template analytics for up to two years, depending on your [pricing plan](https://onesignal.com/pricing).
</Note>

***

## How to access and use template analytics

<Steps>
  <Step title="Go to Templates">
    In your OneSignal dashboard, navigate to **Messages > Template**

    Select a template being used or create a new template and send a test message.
  </Step>

  <Step title="Review analytics and statistics">
    The Template Report displays key performance metrics and delivery statistics, organized by channel (push, email, or SMS).

    Use these metrics to monitor engagement, troubleshoot delivery issues, and evaluate template effectiveness.
  </Step>

  <Step title="Edit or export data">
    To modify the template, click **Edit** at the top of the report.

    Use the **Export** button to download detailed activity logs.
  </Step>
</Steps>

***

## Template statistics by channel

Each messaging channel provides unique, channel-specific analytics to help you understand delivery and engagement. Below is a summary of available metrics for each channel. For canonical metric definitions across all channels, see the [Metrics Glossary](./analytics-metrics-glossary).

<Tabs>
  <Tab title="Push">
    #### Statistic summary

    | Name                         | Description                                                                                                                                                                                                                      |
    | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Delivered                    | The number of messages that were sent from OneSignal to the Push Servers (Google (FCM), Apple (APNS), Huawei (HMS), etc.).                                                                                                       |
    | Click-Through Rate           | Click-Through-Rate (CTR) is measured by (total clicks/delivered) \* 100%.                                                                                                                                                        |
    | Confirmed Click-Through Rate | Confirmed Click-Through-Rate (CCTR) is measured by (total clicks/confirmed delivered) \* 100%.                                                                                                                                   |
    | Influenced Opens             | Influenced Opens are tracked when a user does not directly click on a notification received, but opens your app within the "Influenced time period" set in your OneSignal App's **Settings > Push & In-app > Influenced Opens**. |

    #### Delivery statistics

    | Name         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
    | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Sent         | The total number of messages sent from OneSignal. This value includes failures.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
    | Delivered    | The number of messages that were sent from OneSignal to the Push Servers (Google (FCM), Apple (APNS), Huawei (HMS), etc.).                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | Confirmed    | The number of devices that sent us a received confirmation for this message. Note that a few factors may impact this count. See [Confirmed Delivery](./confirmed-delivery) for details.                                                                                                                                                                                                                                                                                                                                                     |
    | Unsubscribed | A failure reason. The number of devices that were unreachable and likely due to being unsubscribed from push notifications. Once a device has been detected as unsubscribed, it will be marked as unsubscribed and future notifications will not be sent to it unless it re-subscribes to notifications again. Older, inactive subscriptions, may also become unsubscribed by [Google FCM expiring the device token.](./fcm-expired-token-faq) [Learn more about causes of Unsubscribes.](./push-notification-message-reports#unsubscribed) |
    | Failed       | The message failed to be sent due to some kind of error. Common errors and troubleshooting steps can be found in this [reference to push errors](./push-notification-message-reports#failed).                                                                                                                                                                                                                                                                                                                                               |
    | Remaining    | The number of notifications that are queued to be sent.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
    | Capped       | The number of notifications that were not sent due to your frequency capping settings. See [Frequency capping](./frequency-capping) for details.                                                                                                                                                                                                                                                                                                                                                                                            |

    #### Conversion statistics

    <Info>
      **Coming soon** — [Conversion metrics](./conversion-metrics) will be available on template reports. Once available, you will see attributed and influenced conversions aggregated across all messages sent from this template.
    </Info>

    #### Outcome statistics (legacy)

    <Warning>Custom Outcomes is being deprecated and replaced by [Conversion metrics](./conversion-metrics).</Warning>

    | Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
    | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | Clicks             | Tracks number of clicks/opens on a push message. Clicks are always measured with direct attribution                                                                                                                                                                                                                                                                                                                                                                                                          |
    | Confirmed Delivery | The number of devices that sent us a received confirmation for this message. Note that a few factors may impact this count. See [Confirmed Delivery](./confirmed-delivery) for details. [Paid plan required](https://onesignal.com/pricing) .                                                                                                                                                                                                                                                                |
    | Sessions           | Represented as either a *count* of sessions, or a *sum* of cumulative sessions (in seconds) resulting from a push message. OneSignal only counts a session after the user has left the app for over 30 seconds. If a user has fully quit your app or website and reopens it, the session data will apply to Session. If the app or website is still in the background, and the user brings it to the foreground, a new session will not apply. [Professional plan required](https://onesignal.com/pricing) . |
    | Custom Outcomes    | Additionally, you can set up custom outcomes such as purchase amount, action taken by the user, or any other outcome of interest. These are configured in your app's code. To learn more, read [Custom Outcomes](./custom-outcomes).                                                                                                                                                                                                                                                                         |
  </Tab>

  <Tab title="Email">
    #### Statistic summary

    | Name               | Description                                                                                                                                                                                        |
    | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Open Rate          | Measured by (Unique Clicks/Unique Opens) \* 100%.                                                                                                                                                  |
    | Click-Through Rate | The number of unique recipients, that have clicked links in this email. [Click Tracking must be enabled](./unsubscribe-links-email-subscriptions) . Measured by (Unique Clicks/Deliveries) \* 100% |
    | Unsubscribes       | The number of recipients who opted out of your emails using the unsubscribe link in this email. Email address subscriptions are marked as unsubscribed immediately upon receiving the event.       |

    #### Delivery statistics

    | Name         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
    | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | Audience     | The number of email addresses included in the audience at the time of sending.                                                                                                                                                                                                                                                                                                                                                                                                             |
    | Sent         | The total number of messages sent from OneSignal.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
    | Delivered    | The number of messages confirmed to be successfully delivered to the Recipient's Inbox.                                                                                                                                                                                                                                                                                                                                                                                                    |
    | Remaining    | The number of notifications that are queued to be sent.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    | Total Clicks | The total number of clicks for links in this email. Includes when a single email link was clicked multiple times. See [URLs, Links and Deep Links](./links) for more.                                                                                                                                                                                                                                                                                                                      |
    | Total Opens  | The total number of times the email was opened. Includes when a single email was opened multiple times. User privacy settings could affect these numbers. See below FAQ [Why are Open events low?](#why-are-open-events-low) for details.                                                                                                                                                                                                                                                  |
    | Unsubscribed | The number of recipients who opted out of your emails using the unsubscribe link in this email. Email address subscriptions are marked as unsubscribed immediately upon receiving the event.                                                                                                                                                                                                                                                                                               |
    | Bounced      | A "bounce" generally occurs when sending to email addresses that: - do not exist/spelled incorrectly - have full inboxes - are too old and not used anymore - block domains with poor sender reputation (too many spam complaints) - have a restrictive DMARC record for your sending domain. Bounced email addresses are added to the [Email Reputation & Suppression List](./email-deliverability) . See [How to improve email deliverability](./email-deliverability) for more details. |
    | Failed       | OneSignal could not deliver the email to the recipient's inbox and will drop the message. See below FAQ [Why are emails marked as failed?](#why-are-my-emails-marked-as-failed) for details.                                                                                                                                                                                                                                                                                               |
    | Suppressed   | Emails not sent due to previous spam report or bounce in order to protect your reputation as an email sender. (Available for [OneSignal Email Only](./email-setup))                                                                                                                                                                                                                                                                                                                        |
  </Tab>

  <Tab title="SMS">
    #### Summary statistics

    | Name                     | Description                            |
    | ------------------------ | -------------------------------------- |
    | Delivery Rate            | (Total Delivered ÷ Total Sent) × 100%. |
    | Failure & Rejection Rate | (Total Failed ÷ Total Sent) × 100%.    |

    #### Delivery statistics

    | Name       | Description                                                                                                                                           |
    | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Audience   | The number of phone numbers included in the audience at the time of sending.                                                                          |
    | Sent       | The message was successfully sent to the carrier. *This does not necessarily mean the user has received these messages.*                              |
    | Delivered  | OneSignal has received confirmation of message delivery from the carrier. *This does not necessarily mean the recipient has received these messages.* |
    | Failed     | The message failed to send.                                                                                                                           |
    | Suppressed | The message was not to the recipient because they opted out of receiving messages from the sender.                                                    |
    | Rejected   | The message was not delivered by the carrier due to number blockage, velocity blockage, or the recipient is on a block list.                          |
  </Tab>
</Tabs>

***

## Audience activity

Audience activity reports give you a detailed breakdown of each recipient's engagement with your messages. This helps you segment users for retargeting and understand subscription health.

<Tabs>
  <Tab title="Push">
    * Lists each device subscription and its delivery results (sent, confirmed, clicked, failed, unsubscribed, etc.).
    * To export a full list of subscriptions in your message audience, you can click **Export**.
    * If one of the line items has "()" in the Device column, this means this subscription was deleted.
  </Tab>

  <Tab title="Email">
    See which email address subscriptions were delivered, opened, clicked, unsubscribed, bounced, failed, and complained. Timestamps show most recent event, and definitions for each event are above.

    * **Export** activity data for all information, including the failure message reasons.
    * **Retarget** users based on activity data to follow up. See [Retargeting Messages](./retargeting) for more details.
  </Tab>

  <Tab title="SMS">
    Audience Activity displays a list of subscriptions that were sent, delivered, or failed to receive an SMS. See [Retargeting Messages](./retargeting) for more details.
  </Tab>
</Tabs>

<Warning>
  For all channels, audience activity is available for 30 days from the time the message is displayed.
</Warning>

***

## FAQ

### How long is template data stored?

Template data follows the standard analytics data retention policy. See [Analytics data retention](./billing-faq#analytics-data-retention) for details by plan.

***

Built with [Mintlify](https://mintlify.com).
