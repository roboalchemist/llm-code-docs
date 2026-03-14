# Source: https://developers.smtp2go.com/docs/webhooks-overview.md

# Webhooks Overview

Webhooks allow SMTP2GO to notify your web service via an HTTP or HTTPS POST request whenever an email or SMS event happens in your account. For example, you can choose to be instantly notified if an email bounces, when an open occurs or if a spam complaint is recorded.

> 📘 Slack
>
> If your notification needs are simple, consider using our [Slack ](https://developers.smtp2go.com/docs/slack-app)integration instead.

The setup and management of Webhooks are handled on the "**Settings > Webhooks**" page in the SMTP2GO App or via the API. View the [Setup a Webhook](https://developers.smtp2go.com/docs/setup-a-webhook) page for the steps involved.

Webhooks can be set for selected SMTP Users, API Keys or Authenticated IPs.

<Image align="center" border={false} src="https://files.readme.io/c445a875813d5e1613d205913634e5607b73fa8913b627021b9387064acd6e8c-WebhookNew2.png" />

## Webhook Events - Email

The events you can select to be notified of include:

| Event       | Description                                                                                                                                                                                                                                                                                                                                                                        |
| :---------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Processed   | The email was received by our incoming servers and is being processed for delivery. If multiple delivery attempts are occurring and not yet successful, the email will remain in the Processed status.                                                                                                                                                                             |
| Delivered   | The email was successfully delivered to the recipient and this is confirmed when the recipient server provides a “250” response.                                                                                                                                                                                                                                                   |
| Open        | The email was opened by the recipient. A new open event can be triggered each time the recipient opens the email. For full details regarding open tracking and its limitations, view our open tracking article.                                                                                                                                                                    |
| Click       | The recipient clicked a tracked link in the email. A new click event can be triggered each time the recipient clicks on a link.                                                                                                                                                                                                                                                    |
| Bounce      | The email was bounced by the recipient server when delivery was attempted. Bounces are classified as Soft or Hard depending on the response from the recipient server.                                                                                                                                                                                                             |
| Spam        | The recipient marked an email as spam or manually moved it to their spam folder. When this occurs, it triggers a spam complaint and the recipient email address is indefinitely added to your Suppressions page. The address can be managed on the “Reports > Suppressions” page in the App or via the API. If delivery is attempted to a suppressed address, it will be rejected. |
| Unsubscribe | A recipient unsubscribed from receiving your emails using the Unsubscribe Footer. When this occurs, the address will be indefinitely added to your account’s Suppressions page. It can be managed on the “Reports > Suppressions” page in the App or via the API. If delivery is attempted to a suppressed address, it will be rejected.                                           |
| Resubscribe | A recipient went to the unsubscribe link they previously unsubscribed via and resubscribed or the address has been removed from the Suppressions page.                                                                                                                                                                                                                             |
| Reject      | An email will be rejected if you attempt to send it to an address that is listed on the account’s "Reports > Suppressions" page or if sending is attempted from an unverified sender, or the SMTP User/Authenticated IP/API Key status is set to [Sandboxed](https://support.smtp2go.com/hc/en-gb/articles/29736421853337-Sandbox-Mode).                                           |

## Webhook Parameters - Email

The Webhook URL will receive an HTTP or HTTPS POST request with the following parameters:

| Parameter       | Description                                                                                                                                             |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------ |
| event           | What happened: "processed", "delivered", "open", "click", "bounce", "spam", "unsubscribe", "resubscribe", or "reject".                                  |
| time            | UTC timestamp of when the event happened.                                                                                                               |
| sendtime        | UTC timestamp of when the email was sent to our server.                                                                                                 |
| sender          | The 'envelope-from' email address.                                                                                                                      |
| from            | The display name (where available) and email address the email was sent from.                                                                           |
| from\_address   | The email address the email was sent from.                                                                                                              |
| from\_name      | The display name set to accompany the email address (where available).                                                                                  |
| rcpt            | The email address the email was addressed to.                                                                                                           |
| recipients      | The email addresses the email was sent to.                                                                                                              |
| auth            | The SMTP Username, API Key or IP Address used to send the email.                                                                                        |
| host            | The recipient server that bounced the message (bounce only).                                                                                            |
| message         | The error message we got (where available).                                                                                                             |
| context         | Contains additional information on the event (where available).                                                                                         |
| email\_id       | An identifier that uniquely identifies the email, which can be used to retrieve further details of the email delivery.                                  |
| id              | The unique id for the webhook.                                                                                                                          |
| message-id      | The unique id from the sender.                                                                                                                          |
| bounce          | This parameter will be included for a bounce event, and will be either hard or soft, depending on how we classify the bounce type.                      |
| subject         | The subject of the email.                                                                                                                               |
| user-agent      | The "User-Agent" header of the device that opened the email (where applicable)                                                                          |
| read-secs       | The number of seconds an email was open - in five second increments up to a maximum of 30 (where applicable).                                           |
| client          | The reported client that clicked/opened the link (based on the User-Agent).                                                                             |
| client-device   | The reported device type of the User-Agent associated with the open/click event (where available).                                                      |
| client-os       | The reported device operating system of the User-Agent associated with the open/click event (where available).                                          |
| geoip-continent | A 2 character continent code based on a geoip lookup of the IP address associated with the open/click event (where available).                          |
| geoip-country   | A 2 character country code based on a geoip lookup of the IP address associated with the open/click event (where available).                            |
| geoip-city      | The name of the city based on a geoip lookup of the IP address associated with the open/click event (where available).                                  |
| srchost         | The IP address of the end-user associated with an open/click event (where available) or the IP address that submitted the email (for processed events). |

## Webhook Events - SMS

The events you can select to be notified of include:

| Event     | Description                                                                                                                                                                                                            |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sending   | The SMS is currently being processed.                                                                                                                                                                                  |
| Submitted | The SMS has been submitted to the downstream provider - i.e. a local SMS network provider. Messages with this status have often been delivered successfully, but the downstream provider hasn't provided confirmation. |
| Delivered | The SMS is sent and delivery is confirmed by the downstream provider.                                                                                                                                                  |
| Failed    | The SMS failed to be delivered, for a reason such as: a message validity check failed, a gateway failure occurred, the message was dropped, the message was detected as duplicate and dropped, etc.                    |
| Rejected  | The SMS was blocked by the SMS network. e.g. the destination address has blocked the sender.                                                                                                                           |
| Opt-Out   | Event indicating the recipient has opted out of further communications.                                                                                                                                                |

## Webhook Parameters - SMS

The Webhook URL will receive an HTTP or HTTPS POST request with the following parameters:

| Parameter            | Description                                                                                           |
| :------------------- | :---------------------------------------------------------------------------------------------------- |
| event                | What happened: "sms\_submitted", "sms\_delivered", "sms\_rejected", "sms\_sending", or "sms\_failed". |
| destination\_number  | The number the SMS is being sent to.                                                                  |
| email\_subject       | The subject of the email (if email to SMS).                                                           |
| id                   | The unique id for the webhook.                                                                        |
| message\_content     | The body content of the SMS message.                                                                  |
| message\_id          | The unique id for the SMS.                                                                            |
| received\_timestamp  | UTC timestamp of the event.                                                                           |
| region               | The destination based on the number's country code.                                                   |
| retry\_count         | The number of attempts to send the SMS.                                                               |
| sender\_email        | The From email address.                                                                               |
| source\_number       | The pool/number the SMS was delivered from.                                                           |
| status\_code         | The status code of the SMS.                                                                           |
| submitted\_timestamp | UTC timestamp of when the SMS was submitted to the downstream provider.                               |

## Webhook Request

SMTP2GO sends a POST (not a GET) request to your URL with the data output type of "JSON" or "Form encoded" depending on what type is defined in the webhook's settings.

## URL Format

Each 'URL of web service' that you enter must follow the URI standard.\
E.g.\
PROTOCOL "://" USER ":" PASSWORD "@" HOST "/" PATH "?" QUERY "#" FRAGMENT

with most parts of that being optional.

PROTOCOL can be either HTTP or HTTPS.\
USER and PASSWORD are only required if you choose to password protect your web service.

## Secure the URL

You can optionally secure your public URL with a username/password, with formats such as the following (the URLs given below are just examples):

`https://USERNAME:PASSWORD@host.yourdomain.com/webhook/smtp2go`

`https://host.yourdomain.com/webhook/smtp2go?p=PASSWORD`

or simply make the name of the endpoint hard to guess:

`https://host.yourdomain.com/webhook/smtp2go_PASSWORD`

## Secure the Endpoint

You can optionally further secure your endpoint with our webhook delivery IP addresses by using the A record for "[webhooks.smtp2go.com](https://mxtoolbox.com/SuperTool.aspx?action=a%3awebhooks.smtp2go.com\&run=networktools)".

## Optional Email Headers

Custom email headers can optionally be reported along with the standard data above. You can specify the headers you wish to receive for the specific Webhook on its "Settings" section in the App or via the API.

***any\_custom\_header***\
any custom header that is sent in your emails.

You can add multiple headers to be returned.

## Webhook Retries and Timeout

Webhook failures will retry for up to 48 hours, a maximum of 35 times with the following timings:

* 5 times in the first 30 minutes
* Every hour for the next 24 hours
* Every 6 hours for the next 24 hours
* Every 12 hours for the next 24 hours
* Once final attempt after 24 hours

Failures can be seen in the App on the "Settings > Webhooks > Failed Notifications" section where you can view, retry, and cancel any failed notification attempts. You can delve into specific failures to see a summary, request data and all attempts.

The default timeout for a Webhook is 10 seconds. A timeout will occur if we do not receive any response headers in that timeframe.

## Number of Webhooks

Accounts on the free plan are limited to 1 webhook and accounts on paid plans can create up to 10.

## Testing Webhooks

A good way to start testing is to deploy a local version of [RequestBin](https://requestbin.com/), which will let you see exactly what data we send to you. Another option to try is [Beeceptor](https://beeceptor.com/).