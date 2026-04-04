# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/events/events.md

# Introduction to Events

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
| `list_member_uploaded` | This event occurs after successfully adding a member to a mailing list. |
| `list_member_upload_error` | This even occurs if an error occurs adding a member to a mailing list. |
| `list_uploaded` | This event occurs after successfully uploading a large list of members to a mailing list. |


You can access Events through a few interfaces:

- [Webhooks](/docs/mailgun/user-manual/events/webhooks) (we POST data to your configured URL(s))
- [The Logs API](/docs/mailgun/api-reference/send/mailgun/logs).
- The Logs tab of the Control Panel (GUI)


A request should define a time range and can specify a set of filters to apply. In response, a page of events is returned along with URLs that can be used to retrieve the next and previous result pages. To traverse the entire range, you should keep requesting the next page URLs returned along with result pages until an empty result page is reached.

Both the Next and Previous page URLs are always returned.

- Previous Page URL for the First Result Page: If you are on the first page of results and request the previous page, it will return an empty result page because there are no events before the first page.
- Next Page URL for the Last Result Page: Similarly, if you are on the last page of results and request the next page, it will return an empty result page because there are no events after the last page.