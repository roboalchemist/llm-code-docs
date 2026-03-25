# Source: https://www.courier.com/docs/external-integrations/email/onesignal-email.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# OneSignal Email

> Integrate OneSignal Email with Courier by configuring your App ID and REST API Key, and sending email messages using the recipient's email address.

## Setup

You will need a [OneSignal](https://onesignal.com/) account. Get your `App ID` and `REST API Key` by following [these instructions](https://documentation.onesignal.com/docs/accounts-and-keys). In Courier, navigate to the [OneSignal Email Integration](https://app.courier.com/integrations/catalog/onesignal-email) page, enter both values, then click "Save."

## Profile Requirements

To deliver a message to a recipient over OneSignal Email, Courier must be provided the recipient's email address. This value should be included in the recipient profile as `email`.

```json  theme={null}
{
  "message": {
    "to": {
      "email": "alice@acme.com"
    }
  }
}
```

<Note>
  The `oneSignalPlayerID` and `oneSignalExternalUserId` profile fields are used by the [OneSignal push provider](/external-integrations/push/onesignal), not the OneSignal Email provider.
</Note>

## Overrides

OneSignal Email does not support provider-level overrides or attachments.
