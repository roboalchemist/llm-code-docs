# Source: https://resend.com/docs/knowledge-base/v0-integration.md

# Send emails with v0 and Resend

> Learn how to add the Resend integration to your v0 project.

[v0](https://v0.dev) by Vercel is a platform for building web sites, tools, apps, and projects via chat. You can add Resend in a v0 project by asking the chat to add email sending with Resend.

## 1. Add your Resend API key

To use Resend with v0, you'll need to add a Resend API key, which you can create in the [Resend Dashboard](https://resend.com/api-keys).

<Note>
  Do not share your API key with others or expose it in the browser or other
  client-side code.
</Note>

<img src="https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/v0-integration.png?fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=cb85c63c4d0bca95571920a08324432f" alt="adding the Resend integration to a v0 chat" data-og-width="3808" width="3808" data-og-height="2128" height="2128" data-path="images/v0-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/v0-integration.png?w=280&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=50b38b9adb1c3bb7ca723541c769c330 280w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/v0-integration.png?w=560&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=2a4b6eb558568a8fff286a1f304ad317 560w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/v0-integration.png?w=840&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=4d17778498f6f98968ecf7091859f85a 840w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/v0-integration.png?w=1100&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=5410e161b281a7347ae4e5f2d66eb215 1100w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/v0-integration.png?w=1650&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=accd2fd395d3105181ac036c532dda7a 1650w, https://mintcdn.com/resend/lyl6PQTYhtWhUjuS/images/v0-integration.png?w=2500&fit=max&auto=format&n=lyl6PQTYhtWhUjuS&q=85&s=7a4727d618641d1316bdc9e4bd526832 2500w" />

## 2. Add a custom domain to your Resend account

By default, you can only send emails to your own email address.

To send emails to other email addresses:

1. Add a [custom domain to your Resend account](https://resend.com/domains).
2. Add the custom domain to the `from` field in the `resend` function in v0 (or ask the chat to update these fields).

Get more help adding a custom domain in [Resend's documentation](/dashboard/domains/introduction).
