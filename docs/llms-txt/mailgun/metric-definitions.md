# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/reporting/metric-definitions.md

# Metric Definitions

Mailgun's Metrics API offers endpoints to access summarized data, including counts, rates, and dimensions. It supports up to 10 counts and rates, as well as 3 dimensions.

## Metric Definitions

| Metric Label | API Variable Name | Calculation  | Description  |
|  --- | --- | --- | --- |
| Accepted | accepted_count | accepted_incoming_count + accepted_outgoing_count | A sum of incoming and outgoing accepted events. This includes all accepted emails to be sent as well as routes, forwards, mailing lists, and batch events. To only view accepted events on emails sent to recipients, use the Accepted Outgoing metric. Accepted events are not associated to IP addresses. The âprocessedâ metric can be used in place of accepted to view similar data by IP.  |
| Accepted incoming | accepted_incoming_count | Sum of all raw accepted_incoming events. | Mailgun accepted the API request to forward, and the message has been put in your queue. These accepted events only cover routes, forwards, and mailing lists. Mailing lists will record a single accepted incoming event, with emails sent to recipients recording their own accepted outgoing events. |
| Accepted outgoing | accepted_outgoing_count | Sum of all raw accepted_outgoing events. | Mailgun accepted the API request to send, and the message was put in your queue. Batch sends will result in one additional accepted outgoing event to record the initial batch request. Accepted events are not associated to IP addresses. The âprocessedâ metric can be used in place of accepted to view data by IP.  |
| Bounced (all) | bounced_count | permanent_failed_count -(suppressed_bounces_count + suppressed_complaints_count + suppressed_unsubscribed_count) | A sum of all soft and hard bounces. Permanent failures fall into three categories, soft bounces, hard bounces, and suppressions. This field is equal to permanent failures minus suppressions. |
| Clicked | clicked_count | Sum of all raw clicked events | The email recipient clicked on a link in the email. Click tracking must be turned on and the CNAME record must be pointing to mailgun.org. |
| Complained | complained_count | Sum of all raw complained events | The email recipient clicked on the spam complaint button and the recipient's email server provides feedback loops to Mailgun for these complaints.  |
| Delayed bounces | delayed_bounce_count | Sum of all raw failed events with a severity equal to âpermanentâ and is-delayed-bounce equals true. | Emails were initially marked as delivered, but later received a permanent failure from the mailbox provider. |
| Delayed first attempt | delayed_first_attempt_count | delivered_two_plus_attempts_count + permanent_failed_old_count | Emails that were temporarily rejected on the first delivery attempt. These emails will have been retried until delivery or until a âtoo oldâ permanent failure is generated.   |
| Delivered | delivered_count | delivered_http_count + delivered_smtp_count | Mailgun sent the email and it was accepted by the recipient email server.   |
| Delivered first attempt | delivered_first_attempt_count | Sum of all raw delivered events with delivery-status.attempt-no equal to 1. | Emails that were delivered on the first delivery attempt without being delayed or bounced.   |
| Delivered HTTP | delivered_http_count | Sum of all raw delivered_http events at the hourly, daily, and monthly resolutions. | The count of delivered events for routes and forwards.   |
| Delivered optimized | delivered_optimized_count | Sum of all raw delivered events that had optimized set to true. | Emails delivered with Send Time Optimization.  |
| Delivered SMTP | delivered_smtp_count | Sum of all raw delivered_smtp events. | The count of delivered events for emails sent to recipient addresses.  |
| Delivered two plus attempts | delivered_two_plus_attempts_count | Sum of all raw delivered events with delivery-status. Attempt-no greater than or equal to 2. | Emails that were delivered after two or more delivery attempts. This indicates the emails received at least one temporary failure. |
| ESP blocked | esp_block_count | Sum of all raw failed events with a severity that does not equal âpermanentâ and a reason equal to âespblockâ. | Emails that were temporarily blocked by the ESP for policy errors and reputation rate limiting.  |
| Failed (all) | failed_count | permanent_failed_count + temporary_failed_count | A sum of all permanent and temporary failures. |
| Hard bounces | hard_bounces_count | Sum of all raw failed events with a severity equal to âpermanentâ, a reason equal to âbounceâ, and is-delayed-bounce equal to false. | A hard bounce is a message that cannot be delivered to its intended recipient due to an invalid recipient address or non-existent mailbox. These addresses will be automatically added to your suppressions list when you receive a hard bounce to prevent subsequent hard bounces. |
| Opened | opened_count | Sum of all raw opened events at the hourly, daily, and monthly resolutions. | The email recipient opened the email and enabled image viewing. Tracking must be turned on. |
| Permanent failed | permanent_failed_count | Sum of all raw failed events with a severity equal to âpermanentâ. | Mailgun could not deliver the email to the recipient email server, and will drop the message without retrying sending. |
| Permanent failed optimized | permanent_failed_optimized_count | Sum of all raw failed events with a severity equal to âpermanentâ, a reason equal to âbounceâ, and i-delivery-optimizer is not empty. | Events that were sent with send time optimization, but received a permanent failure. |
| Permanent failed old | permanent_failed_old_count | Sum of all raw failed events with a severity equal to âpermanentâ and âreasonâ equal to âoldâ. | Mailgun attempted to deliver the email for the maximum number of retry attempts, but received a temporary failure each time. Upon the last retry attempt, the message was classified as a âToo Oldâ permanent failure. |
| Processed | processed_count | delivered_count + permanent_failed_count - webhook_count - delayed_bounce_count | Messages processed after being accepted. Processed messages are billed to your account at the end of the month. |
| Sent | sent_count | (delivered_http_count + delivered_smtp_count + permanent_failed_count) - (suppressed_bounces_count + suppressed_complaints_count + suppressed_unsubscribed_count) | A count of all sent messages. This includes delivered and failed messages, but does not include suppressed messages. |
| Soft bounces | soft_bounces_count | Sum of all raw failed events with a severity equal to "permanent", a reason equal to "generic", "greylisted", "blacklisted", or "espblock", and is-delayed-bounce equal to false. | A soft bounce is a message that cannot be delivered to its intended recipient due to a temporary delivery issue, often stemming from a server outage, full mailbox, oversize files/messages, blocklistings, or reputation issues.
Mailgun treats soft bounces as permanent failures, meaning we will not automatically attempt to redeliver the message. The recipient address will not be added to the suppression list, and the next time you attempt to send a message to this recipient we will attempt to deliver. |
| Suppressed: bounced | suppressed_bounces_count | Sum of all raw failed events with a severity equal to âpermanentâ and a reason equal to âsuppress-bounceâ. | The email was suppressed due to a previous bounce with the recipient address. No delivery attempt was made. |
| Suppressed: complaints | suppressed_unsubscribed_count | Sum of all raw failed events with a severity equal to âpermanentâ and a reason equal to âsuppress-complaintâ. | The email was suppressed due to a previous complaint from the recipient. No delivery attempt was made. |
| Suppressed: unsubscribed | unsubscribed_rate | Sum of all raw failed events with a severity equal to âpermanentâ and a reason equal to âsuppress-unsubscribeâ. | The unsubscribe rate accounts for the total number of unsubscribes divided by the total number of emails delivered and multiplied by 100, expressed as a percentage. |
| Temporary failed | temporary_failed_count | Sum of all raw failed events with a severity that does not equal âpermanentâ. | Mailgun could not deliver the email to the recipient email server, but will retry. |
| Unique clicked | unique_clicked_count | Sum of all unique_clicked events. A unique click event is for a particular messageID, recipient, and bot. Only a single click event is stored for the particular {messageID, recipient,bot} combination. | A unique count of click events. Clicks are deduplicated on a rolling seven days. If youâre viewing two weeks of data, itâs possible to see two unique click events for a single delivered event. Keep in mind date ranges when viewing unique clicks, if your date filter doesnât include the delivery event, you may see more unique clicks than delivered events. |
| Unique opened | unique_opened_count | Sum of all unique_opened events. A unique open event is for a particular messageID, recipient, and bot. Only a single open event is stored for the particular {messageID, recipient,bot} combination. | A unique count of open events. Opens are deduplicated on a rolling seven days. If youâre viewing two weeks of data, itâs possible to see two unique open events for a single delivered event.Keep in mind date ranges when viewing unique opens, if your date filter doesnât include the delivery event, you may see more unique opens than delivered events. |
| Unsubscribed | unsubscribed_count | Sum of all raw unsubscribed events at the hourly, daily, and monthly resolutions | The email recipient clicked on the unsubscribe link. Unsubscribe tracking must be turned on. |
| Webhook Failed | webhook_count | Sum of all raw failed events with a severity equal to âpermanentâ and is-callback equals true. | A count of failed webhook events. |


## Rate Definitions

html
table
tr
th
Rate Label
th
API Variable Name
th
Calculation
th
Definition (Used in tooltip)
tr
td
Bounced
td
bounce_rate
td
bounced_count / processed_count
td
Bounce rate measures the percentage of emails that bounce back, or the number of emails that couldnât be delivered to users over the total number of emails sent.
tr
td
Clicked
td
clicked_rate
td
clicked_count / delivered_count
td
The rate at which delivered emails are clicked. This calculation uses total clicks, not unique clicks. Use the unique click rate if percentages exceed 100%.
tr
td
Complained
td
complained_rate
td
complained_count / delivered_count
td
Complaint rate measures the percentages of delivered emails reported as spam by recipients. This rate should be kept below 0.1%. Please note that Gmail does not provide complaints, to see Gmail complaint data, sign up for Google Postmaster Tools.
tr
td
Delayed
td
delayed_rate
td
delivered_two_plus_attempts_count / delivered_count
td
The percentage of emails that were delivered with two or more delivery attempts. This rate does not include delayed emails that could not be delivered.
tr
td
Delivered
td
delivered_rate
td
delivered_count / sent_count
td
The rate at which sent emails are delivered to recipient addresses. This calculation does not include suppressed emails.
tr
td
Failed
td
permanent_fail_rate
td
permanent_failed_count / processed_count
td
The percentage of sent emails that resulted in a permanent failure. These emails could not be delivered and will not be retried.
tr
td
Opened
td
opened_rate
td
opened_count / delivered_count
td
The rate at which delivered emails are opened. This calculation uses total opens, not unique opens. Use the unique open rate if percentages exceed 100%.
tr
td
Unique clicked
td
unique_clicked_rate
td
unique_clicked_count / delivered_count
td
The percentage of delivered emails that resulted in a unique click event. This calculation will exceed 100% if your date filter excludes a large amount of delivery events.
tr
td
Unique opened
td
unique_opened_rate
td
unique_opened_count / delivered_count
td
The percentage of delivered emails that resulted in a unique open event. This calculation will exceed 100% if your date filter excludes a large amount of delivery events.
tr
td
Unsubscribed
td
unsubscribed_rate
td
unsubscribed_count / delivered_count
td
The unsubscribe rate accounts for the total number of unsubscribes divided by the total number of emails delivered and multiplied by 100, expressed as a percentage.
# Metrics API and Usage Reporting

Mailgun collects a variety of different events and generates analytic reports based on both account and usage metrics. Visit [Metrics API](https://documentation.mailgun.com/docs/mailgun/api-reference/openapi-final/tag/Metrics/) for more details.

Note:
Usage data is available starting 09/01/24.

# Events

Mailgun retains event data for 30 days. Access to this data varies by plan. Refer to our [Pricing page](https://www.mailgun.com/pricing/) for details.

## Tracked Events

| Event | Description |
|  --- | --- |
| `accepted` | Mailgun accepted the request to send/forward the email and the message has been placed in queue. |
| `rejected` | Mailgun rejected the request to send/forward the email. |
| `delivered` | Mailgun sent the email, and it was accepted by the recipient email server. |
| `failed` | Mailgun could not deliver the email to the recipient email server. |
| `opened` | The email recipient opened the email and enabled image viewing. Open tracking must be enabled in the Mailgun control panel, and the CNAME record must be pointing to mailgun.org. |
| `clicked` | The email recipient clicked on a link in the email. Click tracking must be enabled in the Mailgun control panel, and the CNAME record must be pointing to mailgun.org. |
| `unsubscribed` | The email recipient clicked on the unsubscribe link. Unsubscribe tracking must be enabled in the Mailgun control panel. |
| `complained` | The email recipient clicked on the spam complaint button within their email client. Feedback loops enable the notification to be received by Mailgun. |
| `stored` | Mail has stored an incoming message. |


You can access Events through a few interfaces:

- Webhooks (we POST data to your configured URL(s))
- [The Logs API](https://documentation.mailgun.com/docs/mailgun/api-reference/openapi-final/tag/Logs/).
- The **Logs** tab of the Control Panel (GUI)


## Filter Field

Log Records can be filtered by the following fields:

| Filter | Comparators | Description |
|  --- | --- | --- |
| `event` | =,!= | An event type. For a complete list of all events written to the log see the Event Types table below. |
| `mailing_list_address` | contains, not contains | The email address of a mailing list the message was originally sent to. |
| `attachment_filename` | =,!= | A name of an attached file |
| `from` | =, !=, contains, not contains | An email address mentioned in the from MIME header. |
| `message_id` | =, != | A Mailgun message id returned by the messages API |
| `subject` | =, !=, contains, not contains | A subject line |
| `to` | contains, not contains | An email address mentioned in the MIME header |
| `size` | >,< | Message size. |
| `recipients` | contains, not contains | This field tracks all the potential message recipients. |
| `tag` | =, != | User defined tag |
| `severity` | =,!= | Temporary or Permanent. Used to filter events based on severity, if exists. (Currently failed events only) |
| `recipient` | =, !=, contains, not contains | The recipient of the message. |
| `domain` | =, !=, contains, not contains | The domain of a sender. |
| `ip` | =, != | IP address the event originated from. |
| `ip_pool` | =, != | The sending ip pool. |
| `recipient_domain` | =, != | The domain of the recipient. |
| `recipient_provider` | =, != | The provider of the recipient. |
| `country` | =, != | Two-letter country code (as specified by [ISO3166](http://www.iso.org/iso/country_codes.htm)) the event came from or âunknownâ if it couldnât be determined. |
| `bot` | =, !=, contains, not contains | The bot that opened the message (only present on opened/click events if bot performed the action). |
| `subaccount` | =, != | The subaccount for which the message was sent. |
| `device` | =, !=, contains, not contains | Device type the link was clicked on. Can be âdesktopâ, âmobileâ, âtabletâ, âotherâ or âunknownâ. |
| `id` | =, != | The id of the log statement. |
| `user_variables` | contains, not contains | The user variables from the message. |
| `delivery_status_code` | =, != | The SMTP delivery status code. |
| `delivery_status_message` | contains, not contains | The SMTP delivery status message. |
| `is_routed ` | =, != | Indicates the message has been processed by a route. |
| `i_classification_rule_id` | =, != | The classification rule id. |