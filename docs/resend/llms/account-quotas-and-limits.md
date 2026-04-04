# Source: https://resend.com/docs/knowledge-base/account-quotas-and-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What are Resend account quotas and limits?

> Learn what quotas and limits apply to accounts.

Resend regulates email volume in three ways:

1. email volume (quota) - for [Transactional Email](/knowledge-base/what-sending-feature-to-use#what-is-a-transactional-email)
2. number of contacts - for [Marketing Email](/knowledge-base/what-sending-feature-to-use#what-is-a-marketing-email)
3. sending rate

These limits help improve your deliverability and likelihood of reaching your recipient's inbox.

<Info>
  Both **sent emails** and **received emails** (inbound) count towards your
  account's email quota. Each received email counts as 1 email against your
  daily and monthly limits, just like sent emails.
</Info>

## Free Account Quotas and Limits

Free accounts have the following:

* Transactional emails: daily email quota of 100 emails/day and 3,000 emails/month. This quota includes both sent and received emails. Multiple `To`, `CC`, or `BCC` recipients in sent emails count as separate emails towards this quota.

* Marketing emails: unlimited emails to up to 1,000 contacts per month.

## Paid Plan Quota

* Transactional Pro, Scale and Enterprise plans have no daily quota limits, though the plan tier will dictate the monthly email quota. Both sent and received emails count towards this monthly quota. To see your current month usage, view the [**Usage page**](https://resend.com/settings/usage). Multiple `To`, `CC`, or `BCC` recipients in sent emails count as separate emails towards the monthly quota.
* Marketing Pro, Enterprise plans have unlimited emails, though the plan tier will dictate the monthly contacts.

## Overage Limits

Paid plans include pay-as-you-go overages, which allow you to continue sending emails after you've reached your monthly quota. To prevent extreme overages and unexpected costs, we impose a hard limit of 5x your monthly quota.

<Note>
  By default, overage usage is capped at **5x your plan's monthly quota**. Once you reach this limit, sending will be paused until the next billing cycle.

  If you need to adjust this limit, please [contact support](https://resend.com/help).
</Note>

<Tip>
  While overages provide flexibility for occasional spikes in email volume, they
  can be more expensive per email than upgrading your plan. If you consistently
  exceed your quota, consider [upgrading to a higher
  tier](https://resend.com/settings/billing) for better value and more
  predictable costs.
</Tip>

## Rate Limits

All accounts start with a rate limit of 2 requests per second. The [rate limits](/api-reference/introduction#rate-limit) follow the [IETF standard](https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-ratelimit-headers) for stating the rate limit in the response header. If you have specific requirements, [contact support](https://resend.com/help) to request a rate increase.

## Bounce Rate

All accounts must maintain a bounce rate of under **4%**. The [**Metrics page**](https://resend.com/metrics) within an account and/or [webhooks](https://resend.com/docs/webhooks/event-types#email-bounced) allow you to monitor your account bounce rates.

Maintaining a bounce rate above 4% may result in a temporary pause in sending until the bounce rate is reduced.

Tips to keep a bounce rate low:

* Remove inactive user email addresses from email lists.
* Only send to recipients who have given consent to receive email.
* When testing, avoid sending to fake email addresses. Use Resend's [test email addresses](/dashboard/emails/send-test-emails) instead.
* If you are using open/click tracking, periodically remove recipients who are not engaging with your emails from your email lists.

## Spam Rate

All accounts must have a spam rate of under **0.08%**. The [**Metrics page**](https://resend.com/metrics) within an account and/or [webhooks](https://resend.com/docs/webhooks/event-types#email-complained) allow you to monitor your account spam rates.

Maintaining a spam rate over 0.08% may result in a temporary pause in sending until the spam rate is reduced.

Tips to keep a spam rate low:

* Give recipients an easy way to opt-out of emails.
* Send relevant and timely emails.
* Only send to recipients who have given consent to receive email.
