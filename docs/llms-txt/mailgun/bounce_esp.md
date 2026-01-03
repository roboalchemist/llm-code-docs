# Source: https://documentation.mailgun.com/docs/mailgun/email-best-practices/bounce_esp.md

# Bounce and MBP Feedback Handling

A big part of maintaining your email reputation is processing bounces properly. While most major MBPs (Mailbox Providers) give bounce replies "on the wire" during the SMTP session, there are some that send bounce messages via email. In order to receive these emailed bounce messages, you must have the appropriate return path header included with your email so that recipients know where to reply with bounce information.

You must also process this bounce data and act accordingly. In addition, many MBPs will soft bounce your initial attempts at delivery. This is also called grey-listing or throttling. If you continue to send emails to bad addresses or you do not listen to MBPs feedback, you will get filtered and eventually your emails will just get dropped.

Mailgun automatically processes bounce information and reacts accordingly. A good portion of Mailgun's technology is devoted to the parsing of this feedback and adjusting your sending in accordance with this feedback so that you maintain a good reputation.

If we receive a hard bounce, we will stop sending to that address immediately and will not attempt future deliveries to that address. We will stop sending to an address after multiple soft bounces, according to the MBPs' guidelines. It is possible to remove addresses from the flagged list in your Control Panel or through the API, in case it was a temporary issue.