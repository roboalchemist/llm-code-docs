# Source: https://documentation.onesignal.com/docs/en/sms-message-reports.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# SMS message reports

> View SMS delivery and message statistics in OneSignal.

SMS message reports help you understand how an SMS was sent, who it reached, and whether delivery succeeded or failed.

You can use these reports to:

* Confirm messages were accepted and delivered
* Identify delivery failures and opt-outs
* Export recipient-level results for troubleshooting or compliance

Find SMS message reports in Messages > SMS, then click a sent message.

<Frame caption="SMS message report showing delivery stat cards and totals">
  <img src="https://mintcdn.com/onesignal/3PUtCumasMeFG2p0/images/docs/sms-stats-cards.png?fit=max&auto=format&n=3PUtCumasMeFG2p0&q=85&s=ee04cf641829b8050017c37103063ba6" alt="SMS message report with delivery statistics and Twilio status cards" width="1673" height="559" data-path="images/docs/sms-stats-cards.png" />
</Frame>

***

## Delivery statistics

| Metric                   | Definition                                                                                                                                                                                                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Sent**                 | The number of messages successfully sent to Twilio.                                                                                                                                                                                                                                                                                   |
| **Total Attempted**      | The number of phone numbers we attempted to send to. This includes messages successfully sent to Twilio, as well as failures. This is a **derived** metric and is a sum of successes, failures and errors while attempting to send to the provider. This is a **subset** of the audience, as it does not include suppressed messages. |
| **Audience**             | The number of subscriptions in the targeted segment(s).                                                                                                                                                                                                                                                                               |
| **Delivered**            | The number of messages successfully delivered as reported by Twilio. Confirmed Delivery metrics are categorized further to distinguish between SMS/MMS and RCS.                                                                                                                                                                       |
| **Failed**               | The number of messages that failed to be sent to Twilio.                                                                                                                                                                                                                                                                              |
| **Suppressed**           | The number of messages not sent to the recipient because they opted out of receiving messages from the sender.                                                                                                                                                                                                                        |
| **Rejected**             | The number of messages not delivered by the carrier due to number blockage, velocity blockage, or the recipient is on a block list. This is a **derived** metric and is a sum of provider errors and provider failures.                                                                                                               |
| **Provider Errored**     | This number counts the phone numbers for which Twilio failed to send the message.                                                                                                                                                                                                                                                     |
| **Provider Undelivered** | This counts the phone numbers for which Twilio sent the message, but failed to deliver it.                                                                                                                                                                                                                                            |
| **Read**                 | The number of recipients that read an RCS message.                                                                                                                                                                                                                                                                                    |
| **Total Clicks**         | Total number of times a link in the message was clicked. Includes when a single link was clicked multiple times.                                                                                                                                                                                                                      |
| **Unique Clicks**        | The number of unique link clicks across all links in the message. These are unique per subscriber.                                                                                                                                                                                                                                    |
| **Replied**              | The number of keywords that have been received by OneSignal excluding consent keywords.                                                                                                                                                                                                                                               |
| **Unsubscribed**         | The number of opt-out keywords that have been received by OneSignal.                                                                                                                                                                                                                                                                  |

The following metrics are specific to SMS message reports:

| Metric                       | Description                                                                                                                                        |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Delivery rate**            | The percentage of messages that were successfully delivered.                                                                                       |
| **Failure & Rejection rate** | The percentage of messages that were not delivered or suppressed.                                                                                  |
| **Click-through rate (CTR)** | The percentage of the total number of recipients that have clicked links in this message. See [Links](./links) for more details on click tracking. |

For detailed metric definitions across all channels, see the [Metrics Glossary](./analytics-metrics-glossary).

<Warning> SMS messages and reports are retained for approximately **30 days**. Export message or audience data if you need long-term records. See [Exporting data](./exporting-data). </Warning>

## Audience Activity

Audience Activity shows recipient-level results for the message.

For each user and subscription, you can see:

* Whether the message was sent, delivered, failed, or suppressed
* Failure or rejection reasons (when available)

You can export this data for audits or troubleshooting, or access it programmatically via the [Export audience activity CSV API](/reference/export-csv-of-events).

<Note> Audience activity is available for 30 days from the time the message is displayed. </Note>

## Conversions

<Info>
  **Coming soon** — [Conversion metrics](/docs/en/conversion-metrics) will be available on message reports. Once available, you will see attributed and influenced conversions for each message directly in its report. See [Conversion metrics](/docs/en/conversion-metrics) for details on the attribution model and setup instructions.
</Info>

***

## Message Settings

The Message Settings is a visual of all data sent within the message including which segment or filters used to target and total number of recipients (number of users targeted).

## SMS failure reasons

There are several reasons why an SMS message may fail to deliver. The most common reasons are:

| Reason          | Description                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Invalid Number  | The phone number is invalid or not in a supported format.                                                                    |
| Carrier Blocked | The phone number is blocked by the carrier.                                                                                  |
| Opt Out         | The recipient has opted out of receiving messages from the sender.                                                           |
| Failed to Send  | The message failed to send.                                                                                                  |
| Suppressed      | The message was not sent to the recipient because they opted out of receiving messages from the sender.                      |
| Rejected        | The message was not delivered by the carrier due to number blockage, velocity blockage, or the recipient is on a block list. |

***

Built with [Mintlify](https://mintlify.com).
