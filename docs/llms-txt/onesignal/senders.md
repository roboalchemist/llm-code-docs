# Source: https://documentation.onesignal.com/docs/en/senders.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Senders

> Learn how to manage sender identities and domains to improve email deliverability and maintain a strong sender reputation.

**Senders** identify where emails are being sent *from*. Managing your senders is critical to ensuring your emails reach the inbox and reflect your brand. Each sender is made up of two key parts:

1. **From Address** – The sender name and email address your recipients see in their inbox.
2. **Sending Domain** – The authenticated domain used to send your emails and build your sending reputation.

Sender identities must be verified (via DNS records) to ensure deliverability and prevent bad actors from sending emails on your behalf. Every email sent through OneSignal must come from a verified sender identity that you control.

<Warning>
  If you're using an integration with SendGrid, Mailchimp, or Mailgun, you must manage senders directly through your ESP’s platform.
</Warning>

***

## Create a sender

When you first [set up email](./email-setup), you’ll be prompted to create a **default sender**.

### Default sender email

This is the email address used to send messages when no other sender is specified. You must have one default sender at all times.

To change the default, click the action menu next to a sender and select **Set as Default**.

<Frame caption="Action menu to set a sender as default">
  <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/821a26d5974877b48fb61c9ccee42a205c8e299ce4c32fe004fde1ea5d60b653-Screenshot_2025-01-22_at_8.58.56_AM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=e0f910c6d4064d389cc60d28848f512e" width="2148" height="1016" data-path="images/docs/821a26d5974877b48fb61c9ccee42a205c8e299ce4c32fe004fde1ea5d60b653-Screenshot_2025-01-22_at_8.58.56_AM.png" />
</Frame>

### Default sender name

This is the display name that appears in the recipient's inbox (e.g. `Acme Team`, `Maggie’s Newsletter`).

### Default reply-to address

The email address users will reply to. You can override this per email if needed.

### Sending domain

This is the domain used to send and authenticate your emails. You must [configure your DNS records](./email-dns-configuration) to verify ownership and improve deliverability.

We strongly recommend using a subdomain (e.g. `mail.yourdomain.com`) to keep email reputation isolated from your main domain.

***

## Add additional senders

You can register up to 100 senders to support different teams, brands, or message types. Each sender is tied to one domain but a single domain can support multiple senders (e.g. `rewards@yourdomain.com`, `support@yourdomain.com`, `marketing@yourdomain.com`, etc.).

<Frame caption="Add sender button in settings">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/4338e0e0691c803c5b67cb0613740b4b5a3ce4c6f4b59b4f2ef806459eb93e8d-Frame_17279.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=f5211651db914023f40ed83459325e55" width="912" height="372" data-path="images/docs/4338e0e0691c803c5b67cb0613740b4b5a3ce4c6f4b59b4f2ef806459eb93e8d-Frame_17279.png" />
</Frame>

To create a new sender:

1. Go to **Settings** > **Email** > **Senders**
2. Click **Add Sender**
3. Enter the sender name and sender email
4. Enter your sending domain and configure DNS. It may take a few minutes to auto-detect and verify DNS records.
5. Once verified, use this sender in **Messages** > **New Email** by selecting it from the **Sender** dropdown

***

## From addresses vs. senders

<Frame caption="From addresses versus senders comparison interface">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d18940496a844f3487531974f98c6966685147adbf4aca6947931c98e44dbbca-Screenshot_2025-01-27_at_1.01.38_PM.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=14e6955e860d027dfff693b6409f069e" width="1016" height="508" data-path="images/docs/d18940496a844f3487531974f98c6966685147adbf4aca6947931c98e44dbbca-Screenshot_2025-01-27_at_1.01.38_PM.png" />
</Frame>

* **From addresses**: These are the sender name and email shown in the recipient’s inbox. You can create multiple from addresses under the same sender, as long as they share the same domain.

  **Example** under `mail.yourdomain.com`:

  * `news@yourdomain.com` (Newsletter)
  * `promos@yourdomain.com` (Promotions)

* **Senders**: Each sender has its own unique sending domain. This is helpful when you want to isolate deliverability between message types.

  **Example**:

  * `mail.yourdomain.com` (Marketing)
  * `notify.yourdomain.com` (Transactional)

***

## Deactivate a sender or delete from address

You may deactivate senders or delete individual from addresses, as long as they are not your defaults. This prevents that from address or sender from being selected or used in emails going forward.

<Tabs>
  <Tab title="Deactivate secondary sender or from address">
    <p>When a sender and its from addresses are not set as the default, both can be removed.</p>

    <Frame caption="Secondary sender and from address">
            <img src="https://mintcdn.com/onesignal/5Rk7jeEkIGBDy1IV/images/email/Secondary-sender.jpg?fit=max&auto=format&n=5Rk7jeEkIGBDy1IV&q=85&s=35fb2f0ee7d335e140c8eb10d748726e" alt="" width="1672" height="764" data-path="images/email/Secondary-sender.jpg" />
    </Frame>
  </Tab>

  <Tab title="Default from address">
    <p>The default from address cannot be deleted, nor can its parent sender be deactivated.</p>

    <Frame caption="Default sender and from address">
            <img src="https://mintcdn.com/onesignal/5Rk7jeEkIGBDy1IV/images/email/Default-sender-no-deactivate.jpg?fit=max&auto=format&n=5Rk7jeEkIGBDy1IV&q=85&s=3457eb77ff9838c53ecf0551224a8e4b" alt="" width="1672" height="563" data-path="images/email/Default-sender-no-deactivate.jpg" />
    </Frame>
  </Tab>

  <Tab title="Delete secondary from address">
    <p>A secondary from address for your default sender can be deleted.</p>

    <Frame caption="Secondary from address">
            <img src="https://mintcdn.com/onesignal/5Rk7jeEkIGBDy1IV/images/email/Secondary-from-default-sender.jpg?fit=max&auto=format&n=5Rk7jeEkIGBDy1IV&q=85&s=76afe94fa6d7c40d4dfd381a24b0494c" alt="" width="1640" height="714" data-path="images/email/Secondary-from-default-sender.jpg" />
    </Frame>
  </Tab>
</Tabs>

For best results, you should ensure a sender is not in use before deactivating it. However, if it is:

* **Email templates**: All email templates using that sender be updated to use your default sender and from address. In some cases, if you have a very large number of templates, this may take a few minutes to complete.

* **Scheduled sends**: Any emails scheduled to be sent in the future, including warm-ups, will be updated to use your default sender and from address.

* **In-progress sends**: Any emails currently mid-send, including regular, intelligent delivery, and timezone delivery sends, must either be allowed to complete or canceled. You will be shown a list of these sends and can choose to wait or cancel them according to your preferences.

***

## Best practices

To protect your sender reputation and ensure high deliverability:

* Use separate senders and subdomains for different message types:
  * `mail.yourdomain.com` for transactional emails
  * `info.yourdomain.com` for marketing emails

* Avoid using your root domain (e.g. `yourdomain.com`) to send email. Always use a subdomain.

* Monitor domain reputation and avoid mixing high-risk marketing sends with critical transactional messages.

***

## Next steps

* [Email setup](./email-setup)
* [Email DNS configuration](./email-dns-configuration)
* [Email deliverability](./email-deliverability)

***

Built with [Mintlify](https://mintlify.com).
