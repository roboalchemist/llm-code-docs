# Source: https://loops.so/docs/deliverability/improving-inbox-placement.md

# Improve your inbox placement

> If your emails are not landing in the inbox folder you expect, here are some tips to improve your inbox placement.

Your email deliverability is an ever-evolving metric that can be influenced by a variety of factors.

It's composed of, but not limited to, a combination of the following:

* sending IP
* your domain
* your content
* email clients' history of those
* the content of your current message
* blocklists
* sending frequency
* TLD (Top Level Domain)

Follow these steps to resolve any issues you may be experiencing with your email deliverability. When these steps are followed, we typically see a significant improvement in inbox placement.

## 1. Confirm Domain Record Setup

Ensure your domain records are properly set up is a huge piece of the puzzle. Utilize [Bounce Doctor](https://bounce.doctor) to verify your domain settings if you are not a Loops user. If you already use Loops, you can just visit the [Domain Records](https://app.loops.so/sending-domain) page to see if your records are set up correctly.

## 2. Recent Domain Record Changes

Following on the previous point, if you've added or updated domain records within the last 24 hours, wait for changes to propagate. This is especially important if you've just set up your domain for email sending.

## 3. Don't Send Cold Emails

Avoid sending cold emails from your primary domain or a subdomain linked to it. Use a separate domain dedicated to sales efforts. Any cold emails at all can have a negative impact on your deliverabilty. Talk to your sales team. Please do not send cold emails with Loops.

## 4. Historical Use of Primary Domain for Cold Email

If you have previously used your primary domain for cold emailing, you may need a new domain for sending emails, especially if your domain reputation has had issues in the past. It's not impossible to fix your domain reputation, but it can be a long process. If you're a startup, a fresh domain might be the right choice.

## 5. Send a Welcome Email

[Implement a welcome email with a Loop](/loop-builder) to welcome new users as soon as they join. When a user signs up, they expect a welcome email, so intent is clear and engagement is high. Keeping a steady cadence of emails to all new users will help balance out larger email sends to your entire user base. This is especially important if you're a new sender.

## 6. Content of Emails

Review the content of your emails and refrain from sending emails about crypto, giveaways, financial products or a regulated industry which are typically flagged by email clients. If you need to send these types of emails, review the content and ensure it's compliant with email client policies.

## 7. Use of Popular Top-Level Domains (TLDs)

Consider sending email from a domain with a popular top-level domain (TLD) such as .com or .org. These TLDs are less likely to be flagged as spam by email clients. A few less common TLD's like .io, .ai and .so seem to be fine as well. However brand new TLD's as well as specificially .xyz and .info are often flagged as spam.

## 8. Send Content Your Users Want

Ensure your email content is desirable and relevant to your audience. Focus on valuable updates such as product information rather than unsolicited giveaways or promotions. Would you want to read the email if it came from a service you use? If not, consider changing the content.

## 9. User Consent

Only send emails to users who have explicitly opted in to receive communication from you. Do not email without explicit consent.

## 10. Google Postmaster Tools

Set up [Google Postmaster Tools](/deliverability/gaining-insights) to gain insights into your email performance and identify potential issues.

## 11. Incorrectly Flagged

Occasionally, when setting up emails from a new domain that matches your workspace domain, you may run into issues where Gmail or another email client incorrectly flags the message as spam or phishing.

You can usually confirm this is the case by sending the same email to a different address—for example, a personal account or one on another domain. If the email is delivered normally there, the issue is with how the client is classifying messages from the new domain.

If this happens, simply mark the message as “Not spam” or “Not phishing” in Gmail. The issue should resolve itself shortly.

This behavior is not caused by Loops, it’s a built-in protection mechanism that email clients use when learning to trust a new domain.

## Additional Checks: Blocklists and IP Reputation

If you've checked all the above and are still having issues, you may want to check if your IP address is on a blocklist. You can use [MXToolbox](https://mxtoolbox.com/blacklists.aspx) to check if your IP address is on a blocklist. Please note that blocklists change frequently and usually resolve themselves within a few days.

## Read more

<CardGroup cols={2}>
  <Card title="Understand email open rates" icon="envelope-open-text" href="/deliverability/understanding-email-open-rates" />

  <Card title="Delivery optimization" icon="chart-line" href="/deliverability/optimization" />

  <Card title="Build your sender reputation" icon="shield" href="/deliverability/sending-reputation" />
</CardGroup>
