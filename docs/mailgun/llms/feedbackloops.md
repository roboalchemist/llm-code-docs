# Source: https://documentation.mailgun.com/docs/mailgun/email-best-practices/feedbackloops.md

# Feedback Loops and Spam Complaints

Most of the major MBPs (Mailbox Providers) other than Gmail provide feedback loops through which they give you information about spam complaints. Here is a thorough [list from Word to the Wise](https://wordtothewise.com/isp-information/). It is important that you sign up for these feedback loops and pay attention to the feedback you are getting. Ignoring this feedback will lead to MBPs throttling you and eventually blocking you completely.

Mailgun registers all of our IPs for these feedback loops. You can access this information through the Control Panel, the API or Webhooks. In addition, we process spam complaints automatically and will stop sending to email addresses after a recipient complains. It is possible to remove addresses from the flagged list in your Control Panel or through the API.