# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/open-click-bot-detect.md

# Open and Click Bot Detection

Mailgun uses tracking pixels and URL redirects to track when a user opens the message and clicks links in the email. However, there are various third-party automated systems that will automatically open and message and follow the links for virus scanning and user activity obfuscation, such as [Apple Mail Privacy Protection.](https://support.apple.com/guide/iphone/use-mail-privacy-protection-iphf084865c7/ios)

Because automated systems can affect the accuracy of open and click tracking, Mailgun will attempt to detect when one of the systems retrieves the tracking pixel or clicks a link. When a bot is detected opening or clicking a link in the email, Mailgun will indicate this via the client-info.bot field in the open/click events.


```JSON
{
    "client-info": {
      "client-name": "unknown",
      "client-type": "unknown",
      "user-agent": "Mozilla/5.0",
      "device-type": "unknown",
      "client-os": "unknown",
      "bot": "apple"
    },
    "tags": [],
    "timestamp": 1652883435.279025,
    "recipient": "bot@apple.com",
    "geolocation": {
      "region": "Unknown",
      "country": "US",
      "city": "Unknown"
    },
    "event": "opened",
}
```

The bot field can have one of the possible values:

| **Value** | **Description** |
|  --- | --- |
| `apple` | Indicates Apple MPP bot |
| `gmail` | Indicates a Gmail bot |
| `generic` | Indicate an unknown bot (mostly likely a firewall or anti-virus scan) |
| `(empty)` | If the bot field is empty, no bot was detected. |


## Tracking Unsubscribes

Every time a recipient requests to unsubscribe from mailings, Mailgun can keep track of it. When you enable unsubscribe tracking, Mailgun will insert unsubscribe links and remove those recipients from your mailings automatically for you.

To see unsubscribes, go to the Logs tab, or see counters of unsubscribes aggregated by tags found on the Analytics tab of the Control Panel. You can also get notifications through a webhook, or get data programmatically through the Events or Bounces API

Mailgun supports three types of unsubscribe levels: domain, tag, Mailing Lists

| **Unsubscribe Level** | **Description** |
|  --- | --- |
| `Domain Level` | Once a recipient selects to unsubscribe from the domain, they will not receive any more messages from that sending domain. |
| `Tag Level` | Sometimes traffic needs to be separated by different types of mailings, such as newsletters, security updates and other types. You may have recipients who would like to unsubscribe to a specific type of mailing you're sending out. For this reason, you can use tags by marking your messages with the appropriate X-Mailgun-Tag header, and use the special %tag_unsubscribe_url% variable (See the table below) |
| `Mailing Lists Level` | When a recipient unsubscribes from a Mailing List, they will still be a member of the Mailing List, however, they will be flagged as unsubscribed, and Mailgun will no longer send messages from the Mailing List to the unsubscribed recipient. |