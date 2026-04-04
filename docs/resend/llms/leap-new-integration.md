# Source: https://resend.com/docs/knowledge-base/leap-new-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://resend.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Send emails with Leap and Resend

> Learn how to add the Resend integration to your Leap.new project.

[Leap](https://leap.new) is a platform for building full-stack web and mobile apps via chat.

## 1. Ask Leap to add Resend

You can add Resend in a Leap project by asking the chat to add email sending with Resend.

**Example prompt**

```
When someone fills out the contact form, send an email using Resend.
```

## 2. Add your Resend API key

To use Resend with Leap, you'll need to add a Resend API key, which you can create in the [Resend Dashboard](https://resend.com/api-keys). Do not share your API key with others or expose it in the browser or other client-side code.

Leap will prompt you to set a secret value on the Infrastructure page. Paste your key value and click **Update secret**.

<img src="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/leap-new-integration.png?fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=d1c68aa7b6144ffcd8ee2793cdebe67d" alt="adding the Resend integration to a leap.new chat" data-og-width="3360" width="3360" data-og-height="2100" height="2100" data-path="images/leap-new-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/leap-new-integration.png?w=280&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=85fa70d109462c9f5f63fc548825564d 280w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/leap-new-integration.png?w=560&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=75d801baa69988a8ffc8f99cdb8ffdb9 560w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/leap-new-integration.png?w=840&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=cf8de66906546502c08e22fcd00a6329 840w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/leap-new-integration.png?w=1100&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=f412e543f5e54d01a8158df825281609 1100w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/leap-new-integration.png?w=1650&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=bfc0165713fd70500260705a81d53e06 1650w, https://mintcdn.com/resend/OWNnQaVDyqcGyhhN/images/leap-new-integration.png?w=2500&fit=max&auto=format&n=OWNnQaVDyqcGyhhN&q=85&s=99d2aac664e970d8f765ab5f9f1fd06e 2500w" />

<Info>
  Learn more about the Resend integration in the [Leap
  documentation](https://docs.leap.new/integrations/resend).
</Info>

## 3. Add a custom domain to your Resend account

By default, you can only send emails to your own email address.

To send emails to other email addresses:

1. Add a [custom domain to your Resend account](https://resend.com/domains).
2. Add the custom domain to the `from` field in the `resend` function in Leap (or ask the chat to update these fields).

Get more help adding a custom domain in [Resend's documentation](/dashboard/domains/introduction).
