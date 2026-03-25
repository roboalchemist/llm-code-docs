# Source: https://www.courier.com/docs/external-integrations/email/gmail.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Gmail

> Send Gmail messages via Courier by authorizing your Gmail account through OAuth, providing the recipient's email in their profile, and optionally switching accounts via the integration settings—ideal for testing and small-scale sending due to Gmail's API rate limits.

## Setup

When you set up Gmail as a provider and connect your gmail account, Courier will request permission to send emails on your behalf. Courier will not send any emails unless you explicitly make a send request using the provider.

<Note>
  Gmail's API has [limitations](https://developers.google.com/gmail/api/reference/quota) based on per-method quota usage (250 per second) thus Gmail is really intended for getting started fast, testing, or small-scale sending.
  Courier has a variety of [email provider integrations](/external-integrations/integrations-overview) that won't rate limit you.
</Note>

### OAuth Authorization

Google APIs use the OAuth protocol for authentication and authorization. Once given permission, Courier will request an access token from the Google Authorization Server, and send the token to the Google Gmail API on your behalf.

To give Courier access to your Gmail credentials, you will need to consent to Courier's requested Gmail scopes by signing into your desired Gmail inbox and allowing Courier permission.

### Updating Authorized Account

On the [Gmail Integration](https://app.courier.com/integrations/gmail) page, you can click on "Authorize a different Gmail inbox" to send messages from a different account. This will require you to give permissions for the new email account every time you change the account.

## Profile Requirements

To deliver a message to a recipient over Gmail, Courier must be provided the recipient's email address. This value should be included in the recipient profile as `email`.

```json  theme={null}
{
  "message": {
    // Recipient Profile
    "to": {
      "email": "alice@acme.com"
    }

    // ... rest of message definition
  }
}
```

## Overrides

Gmail does not support provider-level body overrides. OAuth authorization and token refresh are handled automatically by Courier.
