# Source: https://www.courier.com/docs/tutorials/monitoring/how-to-debug-delivery-issues.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Debug Email Delivery Issues

> Troubleshoot email delivery problems using Courier message logs. Understand message statuses, identify common causes, and resolve issues across providers.

When recipients report they haven't received an email, Courier's [Message Logs](/platform/analytics/message-logs) are your starting point. This guide walks you through reading the logs, understanding what each status means, and narrowing down where the problem is.

## Understand Message Statuses

Every message in Courier progresses through a series of statuses. The most important distinction for email troubleshooting is the difference between **Sent** and **Delivered**.

| Status            | What it means                                                                                       | What it does NOT mean                                                                                              |
| ----------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Sent**          | Courier handed the message to your email provider and the provider accepted it.                     | The email reached the recipient's inbox. A `200` from the provider is an acknowledgment, not a delivery guarantee. |
| **Delivered**     | The provider confirmed the recipient's mail server accepted the message.                            | The email is in the recipient's inbox. The mail server may still filter or quarantine it internally.               |
| **Undeliverable** | The provider reported a hard failure: bounce, block, or suppression.                                | Nothing further will happen; Courier will not retry.                                                               |
| **Filtered**      | Courier filtered the message before sending, due to preferences, send conditions, or routing rules. | The message was never sent to a provider.                                                                          |

<Warning>
  "Delivered" means the recipient's mail server accepted the email at the SMTP level. Enterprise email security gateways (Proofpoint, Mimecast, Barracuda, etc.) may still quarantine the message after acceptance. If a message shows Delivered but the recipient hasn't received it, the issue is on the recipient's side.
</Warning>

## Debug with Message Logs

<Steps>
  <Step title="Find the message">
    Open [Message Logs](https://app.courier.com/logs) and filter by recipient email address, notification template, or date range. Click the message to open the detail view.
  </Step>

  <Step title="Read the timeline">
    The timeline shows every step from request to delivery. Look for where the message stopped progressing:

    * **Request Received** → Courier accepted the API call
    * **Event Mapped** → The notification template was resolved
    * **Routed** → Channel routing completed
    * **Rendered** → Content was generated for the provider
    * **Sent** → Provider accepted the message
    * **Delivered** → Provider confirmed mail server acceptance

    If an error occurred at any step, click the event to see the error message and provider response.
  </Step>

  <Step title="Check the provider response">
    Click the **Sent** event to see the raw provider response. This tells you exactly what the provider returned (HTTP status code, message ID, error details). Use this information to cross-reference with your provider's dashboard.
  </Step>
</Steps>

## Common Scenarios

### Message stuck at "Sent"

The provider accepted the message but hasn't reported a delivery outcome yet.

**Possible causes:**

* **Polling delay.** For providers that use polling-based delivery tracking (SendGrid, Postmark, Mailgun), Courier checks the provider's API periodically. Status updates can take a few minutes.
* **Missing delivery tracking config.** AWS SES requires [SNS webhook setup](/external-integrations/email/aws-ses#aws-ses-delivery-tracking) to report delivery status back to Courier. Without it, messages stay at "Sent" indefinitely.
* **Deferred delivery.** The recipient's mail server accepted the message but deferred final delivery. The provider may still be retrying.

**What to do:**

1. Wait 15-30 minutes; polling-based providers need time to report status
2. Check your provider's dashboard for the message status (SendGrid Activity Feed, Postmark Activity, etc.)
3. If you use AWS SES, verify that [SNS delivery tracking](/external-integrations/email/aws-ses#aws-ses-delivery-tracking) is configured

### Message shows "Undeliverable"

The provider reported a hard failure.

**Possible causes:**

* **Hard bounce.** The email address doesn't exist or the domain is invalid.
* **Soft bounce.** The recipient's mailbox is full or temporarily unavailable. Some providers retry automatically before reporting failure.
* **Block.** The recipient's mail server or provider blocked the message based on sender reputation, content, or policy.
* **Suppression list.** The email address is on the provider's suppression list from a previous bounce or spam complaint. Check your provider's suppression list management.

**What to do:**

1. Click the Undeliverable event in the timeline to see the provider's error message
2. Check your provider's dashboard for bounce details and suppression list entries
3. If the address is valid, verify your sender authentication (see [Sender Authentication Checklist](#sender-authentication-checklist))

### Message shows "Delivered" but recipient didn't get it

The email reached the recipient's mail server but isn't in their inbox.

**Possible causes:**

* **Spam folder.** The email was flagged by the recipient's email client. Ask the recipient to check their spam/junk folder.
* **Enterprise email security.** Organizations often run email security gateways (Proofpoint, Mimecast, Barracuda) that silently quarantine messages after the mail server accepts them. This is common with corporate email domains.
* **Inbox rules.** The recipient may have filters or rules that moved the message to a folder or deleted it automatically.

**What to do:**

1. Confirm the recipient checked their spam/junk folder
2. If all affected recipients share the same domain (e.g., `@company.com`), it's likely a domain-level email security filter. The recipient's IT team needs to check their email security quarantine and allowlist your sending domain.
3. Try sending a test email to a personal/non-corporate address as a control test

### Message shows "Filtered"

Courier filtered the message before it reached a provider.

**Possible causes:**

* **User preferences.** The recipient opted out of this notification type or channel via [Preferences](/platform/preferences/preferences-overview).
* **Send conditions.** The notification template has [send conditions](/platform/content/template-settings/send-conditions) that evaluated to false.
* **Routing rules.** No valid channel was found for the recipient (e.g., missing email address on their profile).

**What to do:**

1. Check the filter reason in the message timeline
2. Review the recipient's [user profile](/platform/users/users-overview) for missing contact info
3. Check the template's send conditions and the recipient's notification preferences

## Provider-Specific Troubleshooting

Each provider has its own dashboard and tools for investigating delivery issues. After identifying the problem in Courier's message logs, use these provider-specific resources to dig deeper:

* **SendGrid**: Check the [Activity Feed](https://app.sendgrid.com/email_activity) for per-message delivery events. Enable Email Activity Tracking in your [SendGrid integration](/external-integrations/email/sendgrid) for polling-based status updates.
* **Postmark**: Use the [Activity dashboard](https://account.postmarkapp.com/servers) to see delivery, bounce, and spam complaint details per message.
* **AWS SES**: Check the SES console under **Reputation Dashboard** for bounce and complaint rates. Make sure [SNS delivery tracking](/external-integrations/email/aws-ses#aws-ses-delivery-tracking) is configured; without it, Courier can't track delivery status.
* **Mailgun**: Use the [Logs dashboard](https://app.mailgun.com/app/logs) for per-message event history including delivery, bounce, and complaint events.
* **Mandrill**: Check the [Outbound Activity](https://mandrillapp.com/activity) for message status and bounce details.

For provider-specific setup and troubleshooting guides, see the [Email Integrations](/external-integrations/email/intro-to-email) section.

## Sender Authentication Checklist

Poor sender authentication is one of the most common causes of delivery issues. Verify the following for your sending domain:

| Record    | Purpose                                                                   | How to check                                                                        |
| --------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| **SPF**   | Authorizes which mail servers can send on behalf of your domain           | Look up your domain's TXT records for an `v=spf1` entry that includes your provider |
| **DKIM**  | Cryptographically signs emails to prove they haven't been tampered with   | Your provider's dashboard will show DKIM status; look for a CNAME or TXT record     |
| **DMARC** | Tells receiving servers how to handle emails that fail SPF or DKIM checks | Look up `_dmarc.yourdomain.com` for a TXT record; start with `p=none` to monitor    |

Most providers walk you through setting up these records during integration setup. If you're seeing delivery issues across multiple recipients, sender authentication is the first thing to check.

<Tip>
  If you're an Enterprise customer, consider setting up [Custom Domain Tracking](/platform/analytics/custom-domain-tracking) to use your own domain for link tracking instead of the default `ct0.app`. This can improve deliverability by avoiding spam filters that flag shared tracking domains.
</Tip>

## What's Next

<CardGroup cols={2}>
  <Card title="Message Logs" icon="chart-line" href="/platform/analytics/message-logs">
    Full reference for message statuses, filtering, and log detail views
  </Card>

  <Card title="Automated Failover" icon="shield" href="/platform/sending/failover">
    Configure provider and channel failover for reliable delivery
  </Card>

  <Card title="Custom Domain Tracking" icon="globe" href="/platform/analytics/custom-domain-tracking">
    Use your own domain for email link tracking
  </Card>

  <Card title="Email Integrations" icon="envelope" href="/external-integrations/email/intro-to-email">
    Provider-specific setup and troubleshooting guides
  </Card>
</CardGroup>
