# Source: https://checklyhq.com/docs/communicate/alerts/notification-log.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Alert Notification Log

Checkly tries to deliver all your failure, degradation and recovery notifications as reliably as possible, but sometimes
life happens. A token expires, a URL has a typo or some other unforeseen issue causes a notification to get lost.

To troubleshoot any delivery issues, browse and filter the
**[Alert Notification Log](https://app.checklyhq.com/alerts/notifications)** for any failed messages. You can also directly
access the notifications for a specific channel by clicking the small "log" icon next to the configured channel name.

Here's an example:

<img src="https://mintcdn.com/checkly-422f444a/riTtJrRZAx73iREC/images/docs/images/alerting/alert-notification-log.png?fit=max&auto=format&n=riTtJrRZAx73iREC&q=85&s=b2a4dc09d311eb63270f117398ce8fe0" alt="alert notification log" width="1283" height="975" data-path="images/docs/images/alerting/alert-notification-log.png" />

In the above example, we see:

1. SMS and Email were correctly delivered.
2. The OpsGenie notification failed though. The notification result shows we got a `422` status code back and the error
   message states our API key was invalid.
3. We also see the configuration used to instrument our call to the OpsGenie API.
4. We see some extra meta data about the notification: What channel was used, what check triggered the alert, when it was
   sent etc.

## Known limitations

There are some limits to how we track notifications currently.

1. SMS delivery can not be tracked up to your phone correctly receiving the SMS. We currently only track if our SMS
   provider ([AWS SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-mobile-phone-number-as-subscriber.html)) has correctly
   received our request to send the SMS.
2. Email delivery is tracked up to our request to our email provider. We use [Postmark](https://postmarkapp.com/) to send our emails.
3. Many alert channels are retried transparently: we only show you the result of the last retry.
4. SSL certificate expiration alerts are not shown in the notification log.


Built with [Mintlify](https://mintlify.com).