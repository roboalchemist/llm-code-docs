# Source: https://documentation.onesignal.com/docs/en/engagement-analytics.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Engagement trends

> Track user engagement across push, email, and SMS with the Engagement Trends report in OneSignal. View delivery, click-through rates, unsubscribe data, and more—exportable as CSV for detailed analysis.

The OneSignal dashboard allows you to track how users engage with your messages. The Engagement Trends chart and statistics include data from all push, in-app, email, and SMS messages, including those sent via the API, or as part of a journey, and give a clear at-a-glance view of your user engagement, which can be easily be exported to a CSV file.
The Engagement Trends chart retains data for up to two years depending on your pricing plan. This report has data available beginning January 10, 2025.

<Frame caption="Engagement Trends chart">
  <img src="https://mintcdn.com/onesignal/Xl2NHJvxakrK4JbL/images/docs/engagement_chart.png?fit=max&auto=format&n=Xl2NHJvxakrK4JbL&q=85&s=fdda34889c960653f066fa43845fc8e9" alt="Engagement Trends chart" width="1638" height="640" data-path="images/docs/engagement_chart.png" />
</Frame>

## Data shown in the Engagement Trends report

<Tabs>
  <Tab title="Push">
    | Metric                       | Description                                                                                                                                                                                                                                                                                                                    |
    | :--------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Delivered                    | The number of push notifications that were sent from OneSignal to the Push Servers (Google (FCM), Apple (APNs), Huawei (HMS), etc.).                                                                                                                                                                                           |
    | Clicked                      | The number of clicks on messages.                                                                                                                                                                                                                                                                                              |
    | Unsubscribed                 | Number of Subscriptions marked unsubscribed due to their push token being unregistered. Devices become unsubscribed either explicitly or due to [token expiration](./fcm-expired-token-faq). These Subscriptions won't receive further notifications unless they re-subscribe. Learn more in [Subscriptions](./subscriptions). |
    | Click-Through Rate           | Calculated as `(Clicked / Delivered) * 100%`.                                                                                                                                                                                                                                                                                  |
    | Confirmed Delivery Rate      | Number of devices that successfully received the notification. <br />Calculated as `(Confirmed Deliveries / Delivered) * 100%`.                                                                                                                                                                                                |
    | Unsubscribe Rate             | Calculated as `(Unsubscribed / Delivered) * 100%`.                                                                                                                                                                                                                                                                             |
    | Confirmed Click-Through Rate | Calculated as `(Clicked / Confirmed Deliveries) * 100%`.                                                                                                                                                                                                                                                                       |

    <Note>
      More details about push metrics can be found in [Push message reports](./push-notification-message-reports). For canonical metric definitions, see the [Metrics Glossary](./analytics-metrics-glossary).
    </Note>
  </Tab>

  <Tab title="In-app">
    | Metric             | Description                                                                                                                                                      |
    | :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Impressions        | The number of times the in-app message has been displayed on users' devices (depending on your in-app settings, a single user may register multiple impressions) |
    | Clicks             | The number of times any clickable part of the in-app message has been clicked.                                                                                   |
    | Click Through Rate | The ratio of clicks to impressions, expressed as a percentage.                                                                                                   |

    <Note>
      More details about in-app metrics can be found in [In-app message reports](./in-app-message-reports). For canonical metric definitions, see the [Metrics Glossary](./analytics-metrics-glossary).
    </Note>
  </Tab>

  <Tab title="Email">
    | Metric             | Description                                                                                                                                                                                                          |
    | :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Delivered          | The number of emails confirmed to be successfully delivered to the recipient's inbox.                                                                                                                                |
    | Opened             | The number of unique email opens. User privacy settings could affect these numbers. See [Email message reports](./email-message-reports) for more.                                                                   |
    | Clicked            | The number of unique clicks for links in this email.                                                                                                                                                                 |
    | Unsubscribed       | The number of recipients who opted out of further emails using the [unsubscribe link](./unsubscribe-links-email-subscriptions). Email Subscriptions are marked as unsubscribed immediately upon receiving the event. |
    | Click-Through Rate | Calculated as `(Clicked / Delivered) * 100%`.                                                                                                                                                                        |
    | Open Rate          | Calculated as `(Opened / Delivered) * 100%`.                                                                                                                                                                         |
    | Unsubscribe Rate   | Calculated as `(Unsubscribed / Delivered) * 100%`.                                                                                                                                                                   |
    | Complaint Rate     | Calculated as `(Spam reports / Delivered) * 100%`.                                                                                                                                                                   |

    <Note>
      More details about email metrics can be found in [Email message reports](./email-message-reports). For canonical metric definitions, see the [Metrics Glossary](./analytics-metrics-glossary).
    </Note>
  </Tab>

  <Tab title="SMS">
    | Metric              | Description                                                                                                               |
    | :------------------ | :------------------------------------------------------------------------------------------------------------------------ |
    | Delivered           | The number of SMS requests successfully sent to Twilio.                                                                   |
    | Replied (keywords)  | The number of [keywords](./keywords) that have been received by OneSignal excluding consent keywords.                     |
    | Unsubscribed        | The number of [opt-out keywords](./sms-consent-keyword-management#opt-out-keywords) that have been received by OneSignal. |
    | Keywords Reply Rate | Calculated as `(Replied (keywords) / Delivered) * 100%`.                                                                  |
    | Unsubscribe Rate    | Calculated as `(Unsubscribed / Delivered) * 100%`.                                                                        |

    <Note>
      More details about SMS metrics can be found in [SMS message reports](./sms-message-reports). For canonical metric definitions, see the [Metrics Glossary](./analytics-metrics-glossary).
    </Note>
  </Tab>

  <Tab title="Live Activities">
    | Metric             | Description                                                                                                                             |
    | :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
    | Sent               | Live activities sent from OneSignal to Apple Push Notification service (APNs). Includes push-to-start and push-to-update notifications. |
    | Confirmed Delivery | Live activities confirmed delivered to devices (requires iOS SDK 5.2.15+ and OneSignal setup method).                                   |
    | Failed             | Live activities that failed to deliver.                                                                                                 |
    | Unsubscribed       | Subscriptions marked unsubscribed when users dismiss a Live Activity or disable Live Activities in settings.                            |
    | Clicked            | Total clicks across all Live Activities. Multiple clicks by the same user are counted separately.                                       |

    <Note>
      More details about Live Activities metrics can be found in [Live Activities](./live-activities). For canonical metric definitions, see the [Metrics Glossary](./analytics-metrics-glossary).
    </Note>
  </Tab>
</Tabs>

## Exporting Engagement Trends Data

To export engagement data, first ensure that your chart is filtered for the required time range and messaging channel. Next, click the export button to the top right of the chart and a CSV file with the relevant data will be sent to the email address associated with your current OneSignal user account. The CSV file will contain the engagement statistics for each date in the filtered time range.

***

Built with [Mintlify](https://mintlify.com).
