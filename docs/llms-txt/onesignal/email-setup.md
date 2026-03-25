# Source: https://documentation.onesignal.com/docs/en/email-setup.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Email setup

> Set up OneSignal Email by selecting a provider, creating a sender, configuring DNS authentication, and verifying your account.

Complete these four steps to start sending authenticated emails with OneSignal. The process takes about 10 minutes, plus up to 24 business hours for account verification.

<Frame caption="Email channel setup overview">
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/0686d2ebaaf882ae3391eacfdfd8afe308e9b4fd5f9978b24983950e238dbdd2-channel-setup-email.jpg?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=9e45d24ac76c56e5f60123bd1565843c" alt="Diagram showing the email setup steps: provider, sender, DNS, and verification" width="1280" height="720" data-path="images/docs/0686d2ebaaf882ae3391eacfdfd8afe308e9b4fd5f9978b24983950e238dbdd2-channel-setup-email.jpg" />
</Frame>

***

## 1. Select a provider

In your OneSignal dashboard, navigate to **Settings > Email > Set up Email** and click **Continue Setup** to use OneSignal Email.

<Frame caption="Provider selection during email setup.">
  <img src="https://mintcdn.com/onesignal/2-gyvU4UfJHiycCa/images/dashboard/email-configuration.png?fit=max&auto=format&n=2-gyvU4UfJHiycCa&q=85&s=060895e85c6452778c8dfd736c3ee1e1" alt="Email configuration page showing provider options" width="1912" height="1056" data-path="images/dashboard/email-configuration.png" />
</Frame>

<Note>
  OneSignal also supports external providers: [SendGrid](./sendgrid-setup), [Mailgun](./mailgun-setup), and [Mailchimp](./mandrill-setup).
</Note>

***

## 2. Create a sender

Configure the default sender identity that OneSignal uses to send authenticated email from your domain:

* **Default sender email** — The email address used when no other sender is specified.
* **Default sender name** — The display name shown in the recipient's inbox (e.g., `Acme Team`).
* **Default reply-to** — The email address users reply to. You can override this per email.
* **Sending domain** — OneSignal auto-generates a subdomain based on your sender email. You can customize it.

<Frame caption="Default sender configuration.">
  <img src="https://mintcdn.com/onesignal/2-gyvU4UfJHiycCa/images/dashboard/create-a-sender.png?fit=max&auto=format&n=2-gyvU4UfJHiycCa&q=85&s=c765f939bfb2faa0e3282a041ddfb19b" alt="Form fields for default sender email, name, reply-to, and sending domain" width="1912" height="1056" data-path="images/dashboard/create-a-sender.png" />
</Frame>

<Note>
  For optimal deliverability, use a [subdomain](#what-is-a-subdomain-and-why-should-i-use-one) (e.g., `mail.yourdomain.com`) rather than your root domain.
</Note>

<Card title="Senders" icon="at" href="./senders">
  Add and manage multiple senders, from addresses, reply-to addresses, and sending domains.
</Card>

***

## 3. Configure DNS

Configure DNS records to authenticate your sending domain. You can auto-configure using your domain registrar login if your registrar is supported, or add the records manually.

In the DNS configuration view, a warning icon means the record does not match and a check icon means it matches.

<Frame caption="DNS configuration in the OneSignal dashboard.">
  <img src="https://mintcdn.com/onesignal/2-gyvU4UfJHiycCa/images/dashboard/dns-manual-configure.png?fit=max&auto=format&n=2-gyvU4UfJHiycCa&q=85&s=f9d2428369c011d44bfe9a3c8ef3a003" alt="OneSignal dashboard showing required DNS records and their verification status" width="1912" height="1056" data-path="images/dashboard/dns-manual-configure.png" />
</Frame>

<Card title="Email DNS configuration" icon="globe" href="./email-dns-configuration">
  Step-by-step guide for auto-configuring or manually adding SPF, DKIM, and DMARC records.
</Card>

***

## 4. Verify your account

Once DNS is configured, click **Verify** to open a support ticket. You'll be asked about your company and intended use cases.

<Frame caption="Account verification prompt.">
  <img src="https://mintcdn.com/onesignal/2-gyvU4UfJHiycCa/images/dashboard/account-verification.png?fit=max&auto=format&n=2-gyvU4UfJHiycCa&q=85&s=11e65071e8e9daa276eeeececff15134" alt="OneSignal account verification dialog with form fields" width="1940" height="1056" data-path="images/dashboard/account-verification.png" />
</Frame>

* Provide complete answers to speed up approval.
* The support team typically responds within 24 business hours.
* You'll receive an email when verification is complete.
* You can send test emails while waiting for approval.

***

## After setup

Once your account is verified, you're ready to send emails.

<Columns cols={3}>
  <Card title="Email overview" icon="envelope" href="./email-messaging">
    Full guide to sending, scheduling, tracking, and optimizing emails.
  </Card>

  <Card title="Email deliverability" icon="inbox" href="./email-deliverability">
    Understand how inbox providers evaluate your reputation and how to protect it.
  </Card>

  <Card title="Auto warm-up" icon="temperature-arrow-up" href="./email-warm-up">
    Gradually ramp sending volume on new or cold domains.
  </Card>

  <Card title="Users and subscriptions" icon="users" href="./users">
    Manage email subscriptions created via CSV, API, web prompt, or SDK.
  </Card>

  <Card title="Design emails" icon="palette" href="./design-emails-with-drag-and-drop">
    Build emails visually with the block editor or use the HTML editor.
  </Card>

  <Card title="Unsubscribe links" icon="link-slash" href="./unsubscribe-links-email-subscriptions">
    Configure unsubscribe behavior and compliance settings.
  </Card>
</Columns>

***

## FAQ

### How long does account verification take?

The OneSignal support team typically responds within 24 business hours. You can send test emails while waiting for verification to complete.

### What is a subdomain and why should I use one?

A subdomain is a prefix added to your domain name — for example, `mail.yourdomain.com` is a subdomain of `yourdomain.com`. While your "From Address" can still appear as `anything@yourdomain.com`, the subdomain is used for email authentication and delivery.

<Frame caption="From domain vs. from address.">
  <img src="https://mintcdn.com/onesignal/6v_cVPknFpo5qSVB/images/docs/098ef181651314b6e6cca670268ead697aa84bcdd728f967e46429bbcc80d283-from_domain_vs_from_address_5.png?fit=max&auto=format&n=6v_cVPknFpo5qSVB&q=85&s=8634e226cf67b094af55bbddd066f2c0" alt="Diagram showing the difference between the from domain and from address" width="2074" height="1374" data-path="images/docs/098ef181651314b6e6cca670268ead697aa84bcdd728f967e46429bbcc80d283-from_domain_vs_from_address_5.png" />
</Frame>

Using a subdomain isolates your email [sending reputation](./email-deliverability#reputation) from your root domain. If your marketing emails generate complaints, it won't affect your root domain's reputation for other services like corporate email. You can also maintain separate reputations for different mail streams:

* `mail.yourdomain.com` for marketing
* `receipts.yourdomain.com` for transactional

### What DNS records are required?

OneSignal requires SPF, DKIM, and DMARC records to authenticate your sending domain. The exact values are shown in the OneSignal dashboard during setup. See [Email DNS configuration](./email-dns-configuration) for details.

### Can I use an external email provider instead of OneSignal Email?

Yes. OneSignal supports [SendGrid](./sendgrid-setup), [Mailgun](./mailgun-setup), and [Mailchimp/Mandrill](./mandrill-setup) as external providers. Select your provider during the initial setup step.

### What happens if my DNS records don't match?

Emails sent from an unauthenticated domain are more likely to be rejected or filtered to spam by inbox providers. Verify your DNS records in the OneSignal dashboard — a warning icon indicates a mismatch that needs to be resolved.

Built with [Mintlify](https://mintlify.com).
