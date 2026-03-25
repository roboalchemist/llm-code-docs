# Source: https://www.courier.com/docs/external-integrations/sms/twilio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Twilio

> Step-by-step guide for integrating Twilio with Courier to send SMS notifications, covering setup, recipient profile requirements, overrides, and troubleshooting for common Twilio errors.

## Setup

You will need a [Twilio](https://www.twilio.com/try-twilio) account with a phone number that has SMS capabilities and a Messaging Service configured. If you don't have these yet, follow Twilio's guides:

1. [Purchase a phone number](https://www.twilio.com/docs/phone-numbers) with SMS capability.
2. [Create a Messaging Service](https://www.twilio.com/docs/sms/send-messages#messaging-services) and add your phone number to it.

In Courier, navigate to the [Twilio Integration](https://app.courier.com/integrations/twilio) page and enter your:

* **Account SID** and **Auth Token** from the [Twilio Console Dashboard](https://www.twilio.com/console/project/settings)
* **Messaging Service SID** from your Messaging Service configuration page

Click "Save" to complete the integration.

<Note>
  Twilio trial accounts may limit sending to verified numbers only. See the [Twilio trial account guide](https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account) for details.
</Note>

## Profile Requirements

To deliver a message to a recipient over Twilio, Courier must be provided the recipient's SMS-compatible phone number. This value should be included in the recipient profile as `phone_number`.

```json  theme={null}
{
  "message": {
    "to": {
      "phone_number": "+12025550156"
    }
  }
}
```

## Overrides

Overrides can be used to change the request body that Courier uses to send an SMS message. You can override any of the fields supported by Twilio's `Messages.json` endpoint ([see all request body fields here](https://www.twilio.com/docs/sms/api/message-resource#create-a-message-resource)).

<Warning>
  Courier relies on configured credentials for status polling. Using config overrides to swap credentials will prevent Courier from polling Twilio's API for delivery status events.
</Warning>

```json  theme={null}
{
  "message": {
    "template": "NOTIFICATION_TEMPLATE_ID",
    "to": {
      "phone_number": "+12345678901"
    },
    "data": {
      "name": "Katherine Pryde"
    },
    "providers": {
      "twilio": {
        "override": {
          "body": {
            "To": "+10987654321"
          },
          "config": {
            "accountSid": "<your Account SID>",
            "authToken": "<your Auth Token>",
            "messagingServiceSid": "<your Messaging Service SID>"
          }
        }
      }
    }
  }
}
```

<Note>
  The Twilio API uses PascalCase field names (`Body`, `To`, `From`). Courier auto-capitalizes override body keys for backwards compatibility, so both `"to"` and `"To"` work in the `body` override.
</Note>

## Troubleshooting

<AccordionGroup>
  <Accordion title="Error 30003: Destination Unavailable">
    Message failed to deliver due to unreachable destination.

    * Send another test message via the Twilio API Explorer
    * Check device status, signal strength, and carrier network
    * Use the "Fallback to Long Code" feature if needed
    * Open a Twilio support request if the issue persists
  </Accordion>

  <Accordion title="Error 30005: Unknown or Inactive Destination">
    Carrier issue, signal loss, or inactive number.

    * Verify the number is active and formatted correctly (E.164)
    * Check device status and signal
    * Test with other devices on the same carrier
  </Accordion>

  <Accordion title="Error 30006: Landline or Unreachable Carrier">
    Message sent to a landline or unreachable carrier.

    * Use the [Lookup API](https://www.twilio.com/docs/lookup/v2-api) to check if the number is a landline
    * Try an alternative phone number
  </Accordion>

  <Accordion title="Error 30007: Message Filtered">
    Messages filtered by Twilio or carrier due to policy violations.

    * Ensure compliance with Twilio's Messaging and Acceptable Use Policies
    * Secure account credentials
    * Open a support request if you suspect a mistake
  </Accordion>

  <Accordion title="Error 30008: Unknown Delivery Failure">
    Message failed for unknown reasons.

    * Test with a simpler message and a different sender ID
    * Check device roaming status
    * Contact Twilio support with recent message SIDs if the issue persists
  </Accordion>

  <Accordion title="Error 20003: Permission Denied">
    Lack of permission to access the requested resource.

    * Verify the correct Auth Token and Account SID combination
    * Check account type (sub-account vs master, test vs live)
    * Confirm API Key and Auth Token are valid
  </Accordion>

  <Accordion title="Error 20404: Resource Not Found">
    Requested resource doesn't exist or is unavailable.

    * Check that the resource exists and verify API case-sensitivity
    * Verify Account SID and base URL
  </Accordion>

  <Accordion title="Error 21211: Invalid To Phone Number">
    Incorrectly formatted or invalid recipient number.

    * Ensure E.164 format with the correct country code
    * Avoid calling or messaging a Twilio number from itself
  </Accordion>

  <Accordion title="Error 21408: Permission Not Enabled for Region">
    Permission not enabled for the recipient's region.

    * Enable permission in [Geo-Permissions settings](https://www.twilio.com/console/sms/settings/geo-permissions)
  </Accordion>

  <Accordion title="Error 21610: SMS STOP Filter">
    Recipient previously unsubscribed using the "STOP" keyword.

    * Request the recipient text "START" to resubscribe
    * Ensure you have consent for messaging
  </Accordion>

  <Accordion title="Error 11200: HTTP Retrieval Failure">
    Failed to retrieve content from the given URL.

    * Verify web server status and accessibility
    * Check for network issues
    * Ensure proper server configuration for static resources
  </Accordion>

  <Accordion title="Error 12300: Invalid Content-Type">
    Twilio unable to process the URL's Content-Type.

    * Verify the correct Content-Type is returned by the server
    * Ensure the URL refers to a valid, acceptable resource
  </Accordion>
</AccordionGroup>
