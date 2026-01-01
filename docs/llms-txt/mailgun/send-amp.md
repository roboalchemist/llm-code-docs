# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/sending-messages/send-amp.md

# Sending an AMP Message

Google's Accelerated Mobile Pages (AMP) for email is a web component framework that you can use to easily create user-first websites, stories, emails, and ads. The AMP email format provides a subset of AMPHTML components for use in email messages, that allows recipients of AMP emails to interact dynamically with content directly in the message. Mailgun allows senders to include AMP components within their email message(s) using the `amp-html` parameter.
This allows recipients to interact within the email message.

Some examples include:

- Answering surveys
- Replying to documents
- Viewing inventory in real-time
- Submitting updates


### AMP Requirements

While AMP is a really exciting email tool, it takes a bit of setup before you can successfully send an AMP email message to your recipients.

#### Registration

Here's what you'll need to know to register:

- In order to send AMP emails to mailboxes that support it (Gmail for now), youâll need to register your sending domain with Google.[Click here](https://support.google.com/mail/answer/81126) to register.


#### Content

- Your AMP email content must comply with Google's requirements. Be sure to look at Google's [Bulk Senders Guidelines](https://support.google.com/mail/answer/81126) before composing your email.
- AMP messages must follow the [AMP for Email Specifications](https://amp.dev/documentation/guides-and-tutorials/learn/email-spec/amp-email-format). Specifically, the required markup, AMP components, and CSS requirements.
- To ensure your content will pass the validation process, use Gmail's [AMP for Email Playground](https://amp.gmail.dev/playground/)


Note:
If you follow the AMP requirements set by Google, you should be well on your way to sending AMP messages.

#### HTTPS URLs

All URLs must use HTTPS, including tracking and unsubscribe URLs. If you're using Mailgun for your open/click tracking and unsubscribe UR:s, you'll need to [Follow these steps](https://help.mailgun.com/hc/en-us/articles/360011566033-How-to-Enable-HTTPS-Tracking-Links) to enable HTTPS on your Mailgun tracking URLs.

### Sending AMP emails

Mailgun has made it easy to send an AMP email using our API by providing the optional `amp-html` parameter along with your AMP content. Mailgun will take care of building the proper `text/x-amp-html` MIME portion. As long as youâre following the AMP requirements set by Google, you should be well on your way to sending your AMP messages.

### Testing your AMP email messages

Note:
You can build and test your AMP email messages even while you're waiting for Google to register your domain.

### AMP Best Practices

1. Visit your Gmail settings page (*GSuite users will need their admins to enable the Dynamic Email Option*)
2. Click the **Dynamic Email** section, check the box to **Enable Dynamic Email**.
3. Click **Developer Settings**
4. Enter your sending address in the field â This will whitelist your sending address.
5. Click **OK**


Following the proper requirements and these steps for sending AMP messages will allow you to be able to receive an AMP email from your sending address to your Gmail account.