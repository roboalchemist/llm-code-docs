# Source: https://loops.so/docs/webhooks.md

# Webhooks

> Receive event notifications with webhooks.

Webhooks send data to your website or application when certain events happen in your Loops account.

## Set up webhooks

Go to [Settings -> Webhooks](https://app.loops.so/settings?page=webhooks) and input the URL of your endpoint that will receive events.

You will be provided with a signing secret. You should save this in your project (for example in an environment variable) so you can verify requests when you receive them.

Currently you can only set up one webhook endpoint per Loops account.

Subscribe to the events you want to receive using the toggles. Click the group names to view all events in each.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=a7897e5e44e8ce6065a485d93b129002" alt="Webhooks settings" data-og-width="2280" width="2280" data-og-height="1854" height="1854" data-path="images/webhooks-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=e9822c133796329f92aca93f50d3b669 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=12d491bf879a4d9858749a7b5c4f6ca9 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=41dc9af209e6d8ccd8491bc8d28af6d0 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=8fbe9ca24d771110f13e679f51126fe1 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=feeaa261e99f547d03d48ea128c9b05c 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=6989624d615ec1cf641072746c827a93 2500w" />

<Tip>
  When toggling your endpoint on and off there may be a small delay before this
  setting is reflected on the server. For example, it may take a few seconds
  after toggling on your endpoint for requests to be dispatched.
</Tip>

## Rate limiting

Webhook events will be sent at a maximum rate of 10 per second. Any further events will be queued.

## Verify requests

Every event is signed so you can check that data sent to your endpoint is sent from Loops.

To verify webhooks, you need to create a signature of the received request and match that to the provided signature in the request's headers.

Here's an example verification function you could use in Next.js:

<CodeGroup>
  ```javascript utils.ts theme={"dark"}
  import { NextRequest } from 'next/server';
  import crypto from 'crypto';

  interface WebhookVerificationError extends Error {
  code: 'MISSING_HEADERS' | 'MISSING_SECRET' | 'INVALID_SIGNATURE' | 'VERIFICATION_FAILED';
  }

  /\*\*

  - Verifies a webhook request from Loops
  - @param req The incoming Next.js request
  - @throws {WebhookVerificationError} If verification fails
  - @returns {Promise<boolean>} True if verification succeeds
    \*/
    async function verifyWebhook(req: NextRequest): Promise<boolean> {
    try {

        // Get the webhook-related headers directly from req.headers
        // Next.js automatically lowercases header names
        const eventId = req.headers.get('webhook-id');
        const timestamp = req.headers.get('webhook-timestamp');
        const webhookSignature = req.headers.get('webhook-signature');

        // Verify required headers are present
        if (!eventId || !timestamp || !webhookSignature) {
          const error = new Error('Missing required webhook header') as WebhookVerificationError;
          error.code = 'MISSING_HEADERS';
          throw error;
        }

        // Read raw body as buffer
        const readable = req.read();
        const buffer = Buffer.from(readable);
        const rawBodyText = buffer.toString();

        const signedContent = `${eventId}.${timestamp}.${rawBodyText}`;

        // Verify secret exists
        const secret = process.env.LOOPS_SIGNING_SECRET;
        if (!secret) {
          const error = new Error(
            'Missing LOOPS_SIGNING_SECRET environment variable'
          ) as WebhookVerificationError;
          error.code = 'MISSING_SECRET';
          throw error;
        }
        // Create a signature from the request data
        const secretBytes = Buffer.from(secret.split('_')[1], 'base64');
        const signature = crypto
          .createHmac('sha256', secretBytes)
          .update(signedContent)
          .digest('base64');

        // Check if the signature matches
        const signatureFound = webhookSignature
          .split(' ')
          .some((sig) => sig.includes(`,${signature}`));

        if (!signatureFound) {
          const error = new Error('Invalid signature') as WebhookVerificationError;
          error.code = 'INVALID_SIGNATURE';
          throw error;
        }

        return true;

    } catch (error) {
    if ((error as WebhookVerificationError).code) {
    throw error;
    }
    const wrappedError = new Error(
    `Webhook verification failed: ${(error as Error).message}`
    ) as WebhookVerificationError;
    wrappedError.code = 'VERIFICATION_FAILED';
    throw wrappedError;
    }
    }

  ```

  ```javascript webhook.ts theme={"dark"}
  import { NextApiRequest, NextApiResponse } from 'next';

  export const config = {
    api: {
      bodyParser: false,
    },
  };

  export default async function handler(req: NextApiRequest, res: NextApiResponse) {
    if (req.method !== 'POST') {
      return res.status(405).json({ message: 'Method not allowed' });
    }

    try {
      await verifyWebhook(req);
      // Webhook is verified, process the event...
      res.status(200).json({ message: 'Webhook processed successfully' });
    } catch (error) {
      console.error('Webhook error:', error);
      const status = {
        MISSING_HEADERS: 400,
        MISSING_SECRET: 500,
        INVALID_SIGNATURE: 401,
        VERIFICATION_FAILED: 400
      }[(error as WebhookVerificationError).code] || 500;

      return NextResponse.json(
        { message: error.message },
        { status }
      );
    }
  }
  ```
</CodeGroup>

## Testing webhooks

From the Webhooks settings page you can send a test request to your endpoint. This allows you to test that your endpoint is working, and that your verification code is OK.

The event name sent during testing is `testing.testEvent`. You can [see the payload below](#testing-testevent).

## Viewing webhook history

Once Loops has started sending webhook events to your endpoint you will be able to see event history in the **Messages** section at the bottom of the Webhooks settings page.

Clicking on an event in the table will reveal the response from your endpoint, which is helpful if there have been any errors.

We retain 30 days of event history.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-history.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=9cc28ff8f2e3dfaf2fb548f90e67070e" alt="Viewing webhook event history" data-og-width="2280" width="2280" data-og-height="1368" height="1368" data-path="images/webhooks-history.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-history.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=27bed898297a3d11632b8775110f7405 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-history.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=331ed62d5f182ba5bebc55e811b12b24 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-history.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=441ae6982f74999303574c96f2894329 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-history.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=00aa7e6e69a9ae98e6d82b1f4293242e 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-history.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=0ffd1054d26f569df9358419ee236b82 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-history.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=57e7c6ee0a564b791ff954743d854c30 2500w" />

## Event data

Every webhook will contain the following data in the request body:

### `eventName`

The event type. See a [full list of events below](#event-types).

### `webhookSchemaVersion`

Will be `1.0.0` for all events.

### `eventTime`

Unix timestamp of the time the event occurred in Loops.

***

Depending on the context of the event, more data will also be included. Full examples are shown in the [Event types](#event-types) section below.

### `contact`

A full contact object containing a contact's properties.

Contains:

* `id`
* `email`
* `firstName` (nullable string)
* `lastName` (nullable string)
* `source`
* `subscribed` (boolean)
* `userGroup`
* `userId` (nullable string)
* `mailingLists` (object with mailing list IDs as keys and `true` as the value; these are the mailing lists the contact is subscribed to)
* `optInStatus` (nullable string, `"accepted"` or `null`)
  {" "}
  <Note>
    This will be `null` for contacts unless they are created via a form and
    [double opt-in](/contacts/double-opt-in) is enabled. `contact.created`
    events are only sent once contacts have confirmed their subscription, so
    this value will never be `"pending"` or `"rejected"`.
  </Note>
* plus any custom contact properties

This object is the same as the data returned in the [Find a contact](/api-reference/find-contact#response) API endpoint.

### `contactIdentity`

A contact's identifiers. To retrieve the full contact, use the [Find a contact](/api-reference/find-contact) API endpoint.

Contains:

* `id`
* `email`
* `userId` (nullable string)

### `email`

Details about an individual email send to a recipient:

* `id` - The unqiue ID of the email.
* `emailMessageId` - The ID of the sent version of the campaign/loop/transactional email.
* `subject` - The subject of the sent version of the campaign/loop/transactional email.

<Info>
  To get the ID of the campaign, loop or transactional email that relates to the
  Loops dashboard or API, look for a `campaignId`, `loopId`, or
  `transactionalId` in the payload.
</Info>

### `mailingList`

Details about a mailing list:

* `id`
* `name`
* `description` (nullable string)
* `isPublic` (boolean)

This object is the same as the data returned in the [List mailing lists](/api-reference/list-mailing-lists#response) API endpoint.

### `mailingLists`

A list of `mailingList` objects (see above), when an event relates to multiple mailing lists.

### `sourceType`

For `email.*` events, this specifies the type of email.

One of `campaign`, `loop` or `transactional`.

***

### Headers

Headers will include:

* `Webhook-Signature` - A list of request signatures, which can be used to [verify the request](#verify-requests).
* `Webhook-Id` - The unique ID of the event. You can use this to check if you have already saved or processed this specific event.
* `Webhook-Timestamp` - The timestamp of the request (seconds since epoch).

## Event types

### Contacts

#### contact.created

Sent when a new contact is created in your audience.

Contains a `contactIdentity` object plus a full `contact` object, which includes all of the new contact's properties.

<Tip>
  When [double opt-in](/contacts/double-opt-in) is enabled, contact webhooks
  don't fire until the contact is confirmed. The `contact.created` event will
  only be sent for contacts created via forms once the contact has confirmed
  their subscription. Other contact-related webhooks (such as
  `contact.mailingList.subscribed`) will also only fire after confirmation.
</Tip>

```json  theme={"dark"}
{
  "eventName": "contact.created",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "contactIdentity": {
    "id": "cm4itta800003ow9hhekzk94o",
    "email": "test+5@loops.so",
    "userId": null
  },
  "contact": {
    "id": "cm4itta800003ow9hhekzk94o",
    "email": "test+5@loops.so",
    "firstName": null,
    "lastName": null,
    "source": "API",
    "subscribed": true,
    "userGroup": "",
    "userId": null,
    "mailingLists": {
      "cm4ittp2k000l12j3lgrzvlxt": true
    },
    "optInStatus": "accepted",
    "favoriteColor": "blue",
    "favoriteNumber": 42
  }
}
```

#### contact.unsubscribed

Sent when

* a contact is unsubscribed from your audience.
* a contact is deleted from your audience (alongside [contact.deleted](#contact-deleted)).

<Info>
  This is not the same as a contact unsubscribing from a mailing list. See
  [contact.mailingList.unsubscribed](#contact-mailingList-unsubscribed)).
</Info>

Contains a `contactIdentity` object.

```json  theme={"dark"}
{
  "eventName": "contact.unsubscribed",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  }
}
```

#### contact.deleted

Sent when a contact is deleted from your audience.

Contains a `contactIdentity` object.

```json  theme={"dark"}
{
  "eventName": "contact.deleted",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  }
}
```

#### contact.mailingList.subscribed

Sent when a contact is subscribed to a mailing list.

Contains `contactIdentity` and `mailingList` objects.

```json  theme={"dark"}
{
  "eventName": "contact.mailingList.subscribed",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  },
  "mailingList": {
    "id": "cm4ittp2k000l12j3lgrzvlxt",
    "name": "test mailing list",
    "description": null,
    "isPublic": true
  }
}
```

#### contact.mailingList.unsubscribed

Sent when a contact is unsubscribed from a mailing list.

<Info>
  This is not the same as a contact unsubscribing from your audience. See
  [contact.unsubscribed](#contact-unsubscribed).
</Info>

Contains `contactIdentity` and `mailingList` objects.

```json  theme={"dark"}
{
  "eventName": "contact.mailingList.unsubscribed",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  },
  "mailingList": {
    "id": "cm4ittp2k000l12j3lgrzvlxt",
    "name": "test mailing list",
    "description": null,
    "isPublic": true
  }
}
```

### Email sending

#### campaign.email.sent

Sent when a campaign is sent to a contact.

<Info>
  This event will fire for every campaign send. If you send a campaign to 1,000
  contacts, you will receive 1,000 events.
</Info>

Contains a `campaignId` value plus `contactIdentity` and `email` objects.

If the campaign was sent to one or more mailing lists, a `mailingLists` list will also be included.

```json  theme={"dark"}
{
  "eventName": "campaign.email.sent",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  },
  "campaignId": "cm4t1suns001uw6atri87v54s",
  "email": {
    "id": "cm4t1sv84004yje79hawr1fi1",
    "emailMessageId": "cm4t1suns001ww6atotin3bn1",
    "subject": "Test Subject"
  },
  "mailingLists": [
    {
      "id": "cm4ittp2k000l12j3lgrzvlxt",
      "name": "test mailing list",
      "description": null,
      "isPublic": true
    }
  ]
}
```

#### loop.email.sent

Sent when a loop email is sent to a contact.

<Info>
  This event will fire for every contact in a loop. If 1,000 contacts get sent
  emails from your loop, you will receive 1,000 events.
</Info>

Contains a `loopId` value plus `contactIdentity` and `email` objects.

If the loop was sent to one or more mailing lists, a `mailingLists` list will also be included.

```json  theme={"dark"}
{
  "eventName": "loop.email.sent",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  },
  "loopId": "cm4t1snfj0052icemfshgqfcw",
  "email": {
    "id": "cm4t1socj004mje79e61mgh7d",
    "emailMessageId": "cm4ittv1v001oow9hruou8na8",
    "subject": "Subject of the email"
  },
  "mailingLists": [
    {
      "id": "cm4ittp2k000l12j3lgrzvlxt",
      "name": "test mailing list",
      "description": null,
      "isPublic": true
    }
  ]
}
```

#### transactional.email.sent

Sent when a transactional email is sent.

Contains a `transactionalId` value plus `contactIdentity` and `email` objects.

```json  theme={"dark"}
{
  "eventName": "transactional.email.sent",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  },
  "transactionalId": "cm4t1suns001uw6atri87v54s",
  "email": {
    "id": "cm4t1sseg004tje7982991nan",
    "emailMessageId": "cm4ittv1v001oow9hruou8na8",
    "subject": "Subject of the email"
  }
}
```

### Email events

#### email.delivered

Sent when an email is delivered to its recipient.

Contains a `sourceType` and a related `campaignId` / `transactionalId` / `loopId` value, plus `contactIdentity` and `email` objects.

```json  theme={"dark"}
{
  "eventName": "email.delivered",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "sourceType": "campaign",
  "campaignId": "cm4t1suns001uw6atri87v54s",
  "email": {
    "id": "cm4t1sseg004tje7982991nan",
    "emailMessageId": "cm4ittv1v001oow9hruou8na8",
    "subject": "Subject of the email"
  },
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  }
}
```

#### email.softBounced

Sent when an email soft bounces.

<Tip>
  Soft bounces are temporary email delivery failures, for example a connection
  timing out. Soft bounces are retried multiple times and some times the email
  is delivered.
</Tip>

Contains a `sourceType` and a related `campaignId` / `transactionalId` / `loopId` value, plus `contactIdentity` and `email` objects.

```json  theme={"dark"}
{
  "eventName": "email.softBounced",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "sourceType": "campaign",
  "campaignId": "cm4t1suns001uw6atri87v54s",
  "email": {
    "id": "cm4t1sseg004tje7982991nan",
    "emailMessageId": "cm4ittv1v001oow9hruou8na8",
    "subject": "Subject of the email"
  },
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  }
}
```

#### email.hardBounced

Sent when an email hard bounces.

<Tip>
  Hard bounces are persistent email delivery failures, for example a mailbox
  that doesn't exist. The email will not be delivered.
</Tip>

In Loops, a hard bounce results in a contact being unsubscribed from your audience so a `contact.unsubscribed` event will also be sent.

Contains a `sourceType` and a related `campaignId` / `transactionalId` / `loopId` value, plus `contactIdentity` and `email` objects.

```json  theme={"dark"}
{
  "eventName": "email.hardBounced",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "sourceType": "campaign",
  "campaignId": "cm4t1suns001uw6atri87v54s",
  "email": {
    "id": "9874cm4t1sseg004tje7982991nan8732843",
    "emailMessageId": "cm4ittv1v001oow9hruou8na8",
    "subject": "Subject of the email"
  },
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  }
}
```

#### email.opened

Sent when a campaign or loop email is opened.

Contains a `sourceType` and a related `campaignId` or `loopId` value, plus `contactIdentity` and `email` objects.

<Info>
  This event is not available for transactional emails because email opens are
  [not tracked](/transactional#tracking) for transactional emails.
</Info>

```json  theme={"dark"}
{
  "eventName": "email.opened",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "sourceType": "campaign",
  "campaignId": "cm4t1suns001uw6atri87v54s",
  "email": {
    "id": "cm4t1sseg004tje7982991nan",
    "emailMessageId": "cm4ittv1v001oow9hruou8na8",
    "subject": "Subject of the email"
  },
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  }
}
```

#### email.clicked

Sent when a link in a campaign or loop email is clicked.

Contains a `sourceType` and a related `campaignId` or `loopId` value, plus `contactIdentity` and `email` objects.

<Info>
  This event is not available for transactional emails because link clicks are
  [not tracked](/transactional#tracking) in transactional emails.
</Info>

```json  theme={"dark"}
{
  "eventName": "email.clicked",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "sourceType": "campaign",
  "campaignId": "cm4t1suns001uw6atri87v54s",
  "email": {
    "id": "cm4t1sseg004tje7982991nan",
    "emailMessageId": "cm4ittv1v001oow9hruou8na8",
    "subject": "Subject of the email"
  },
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  }
}
```

#### email.unsubscribed

Sent when a recipient unsubscribes from marketing email or a mailing list using an email's "Unsubscribe" link.

A `contact.unsubscribed` or `contact.mailingList.unsubscribed` event will also be sent depending on whether the email was sent to a mailing list or not.

Contains a `sourceType` and a related `campaignId` or `loopId` value, plus `contactIdentity` and `email` objects.

<Info>
  This event is not available for transactional emails because unsubscribe links
  are [not included or required](/types-of-emails#transactional) for
  transactional emails.
</Info>

```json  theme={"dark"}
{
  "eventName": "email.unsubscribed",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "sourceType": "campaign",
  "campaignId": "cm4t1suns001uw6atri87v54s",
  "email": {
    "id": "cm4t1sseg004tje7982991nan",
    "emailMessageId": "cm4ittv1v001oow9hruou8na8",
    "subject": "Subject of the email"
  },
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  }
}
```

#### email.resubscribed

Sent when a recipient resubscribes to marketing email from an email's preference center ("Unsubscribe" link).

Contains a `sourceType` and a related `campaignId` or `loopId` value, plus `contactIdentity` and `email` objects.

<Info>
  This event is not available for transactional emails because unsubscribe links
  are [not included or required](/types-of-emails#transactional) for
  transactional emails.
</Info>

```json  theme={"dark"}
{
  "eventName": "email.resubscribed",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "sourceType": "campaign",
  "campaignId": "cm4t1suns001uw6atri87v54s",
  "email": {
    "id": "cm4t1sseg004tje7982991nan",
    "emailMessageId": "cm4ittv1v001oow9hruou8na8",
    "subject": "Subject of the email"
  },
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  }
}
```

#### email.spamReported

Sent when a recipient reports your email as spam.

Contains a `sourceType` and a related `campaignId` / `transactionalId` / `loopId` value, plus `contactIdentity` and `email` objects.

```json  theme={"dark"}
{
  "eventName": "email.spamReported",
  "eventTime": 1734425918,
  "webhookSchemaVersion": "1.0.0",
  "sourceType": "campaign",
  "campaignId": "cm4t1suns001uw6atri87v54s",
  "email": {
    "id": "cm4t1sseg004tje7982991nan",
    "emailMessageId": "cm4ittv1v001oow9hruou8na8",
    "subject": "Subject of the email"
  },
  "contactIdentity": {
    "id": "cm4ittmhq0011ow9h6fb460yw",
    "email": "test+1@loops.so",
    "userId": null
  }
}
```

### Testing

#### testing.testEvent

This is a test event that can be triggered at any time from the [Webhooks settings page](https://app.loops.so/settings?page=webhooks) in Loops.

```json  theme={"dark"}
{
  "eventName": "testing.testEvent",
  "eventTime": 1734425918,
  "message": "test",
  "webhookSchemaVersion": "1.0.0"
}
```
