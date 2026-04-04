# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/tracking-messages/tracking-spam-complaints.md

# Tracking Spam Complaints

Email service providers (ESP) are very sensitive to users clicking on spam complaint buttons. It's important to monitor that activity to maintain a good sending reputation. While not all ESP supports Feedback Loop (FBL) notifications, Mailgun makes sure that you get data on all the ones that you do, will not remove recipients from future messages if the complaint has been filed by the recipient, Mailgun automatically tracks all messages recipients report as spam.

You can view spam complaints on the control panel by clicking on the **logs** tab or by clicking on the **Analytics** tab to see counters of complaints aggregated by tags. You can also be notified through a webhook. When a recipient report one of your emails as spam, Mailgun will invoke the complained webhook with the following payload. Another way to track complaints is to get the data programmatically through the Events API or the Complaints API. You can Mailgun provides the Spam Complaint API to programmatically manage lists of users who have complained.