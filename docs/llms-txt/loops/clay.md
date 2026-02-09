# Source: https://loops.so/docs/integrations/clay.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Clay

> Learn how to sync data between Clay and Loops.

Clay is a platform for managing and enriching your customer and user data. You can sync contact data between Clay and Loops using webhooks and API requests, as well as trigger emails from Clay.

## Send Loops contacts to Clay

You can send Loops contact data to Clay using Loops [webhooks](/webhooks).

### Create a webhook in Clay

In Clay, add a Webhook source by clicking **More sources...** in the sidebar and selecting **Webhook**.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-create-webhook.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b00c8ce52a010fb7df4ceb5e9a76b1fa" alt="Add a webhook in Clay" data-og-width="2280" width="2280" data-og-height="1290" height="1290" data-path="images/clay-create-webhook.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-create-webhook.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=85c67ab283cb9eaaeda0292f0ce53967 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-create-webhook.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=a760e68a126f7da440fc57e4cec957af 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-create-webhook.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=252738a2d587fc00e53b979fbe4a2bb4 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-create-webhook.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=a1c3c5faeaa50d5b3e0c150a236a2fa9 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-create-webhook.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=53c377f5e48acae47d052465aeedb0b5 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-create-webhook.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e1cb75e446a4e7c970470ea68048220e 2500w" />

This generates a new webhook URL.

Make sure to change the **Send response as** option just below the URL to "JSON" to match the data format sent by Loops.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-webhook-details.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6b924f5206bff4bc7634626838f76ac8" alt="Webhook setup in Clay" data-og-width="2280" width="2280" data-og-height="1665" height="1665" data-path="images/clay-webhook-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-webhook-details.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e8c244c1241518c818568e7fab8cde8c 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-webhook-details.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0398894df23b55aa3d19d8d50acc4154 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-webhook-details.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=3406701f6a549685cec52074d40d459e 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-webhook-details.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=623129335e82dcf4fab0c6b767505a93 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-webhook-details.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=a7ab9c755826a764f9cdcaf2e0d08f68 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-webhook-details.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=5c1b472bc912d5337a2d4c4c02c3b53d 2500w" />

### Set up the webhook in Loops

Copy the URL and paste it into the **Endpoint URL** field on the [Webhooks](https://app.loops.so/settings?page=webhooks) settings page in Loops.

Activate `contact.created` events. This is the only event that makes sense to sync to Clay because it's only [event type](/webhooks#event-types) that contains a full contact record.

<img src="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=a7897e5e44e8ce6065a485d93b129002" alt="Webhook in Loops" data-og-width="2280" width="2280" data-og-height="1854" height="1854" data-path="images/webhooks-setup.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=280&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=e9822c133796329f92aca93f50d3b669 280w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=560&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=12d491bf879a4d9858749a7b5c4f6ca9 560w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=840&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=41dc9af209e6d8ccd8491bc8d28af6d0 840w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=1100&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=8fbe9ca24d771110f13e679f51126fe1 1100w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=1650&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=feeaa261e99f547d03d48ea128c9b05c 1650w, https://mintcdn.com/loops/1DdZd7QTRR4Srm-l/images/webhooks-setup.png?w=2500&fit=max&auto=format&n=1DdZd7QTRR4Srm-l&q=85&s=6989624d615ec1cf641072746c827a93 2500w" />

### Create a data mapping in Clay

Now, in order to create data mappings in Clay, you need to send some data from Loops. To do this we need to create a contact, which will trigger a webhook to be sent to Clay.

In your Loops [Audience page](https://app.loops.so/audience) you can create a new contact from the `+` button in the top right, or use the [API](/api-reference/create-contact) or an [integration](/integrations).

Once the contact is created, go back to Clay. You should see a webhook record in your table, and there should now be data shown in the **Setup mapping** section on the right.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-received.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=88280293428a0211087b17171fcf09aa" alt="Event received in Clay" data-og-width="2280" width="2280" data-og-height="1290" height="1290" data-path="images/clay-event-received.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-received.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d470197851246639172ef35b855ff43d 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-received.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=7b402ed413c3a2dd5a712dce0ba28145 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-received.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=5eb448052d19b5a20d58a9defc241c40 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-received.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=df74a707979f4cd783e94fb3d5bc7f32 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-received.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b8f5a0260322a34b32fd951627bdb3bb 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-received.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f8ae1e0925fc4a89d0e8c4eca00f70c6 2500w" />

Now you can map data from Loops to columns in Clay. Click on the cell in the **Webhook** column. On the right you can click on attributes and map them to columns. Expand the **Contact** object to view the full record from Loops.

Click on an attribute you want to sync and then **Add as column**. You have the option to map the data to a new or existing column.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-mapping-data.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=5cd7c2f2ed8612d506570bfe2b32ebe9" alt="Mapping data in Clay" data-og-width="2280" width="2280" data-og-height="1449" height="1449" data-path="images/clay-mapping-data.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-mapping-data.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=79ebdcf06e3f3bed536add6df7b7a4d1 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-mapping-data.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=ead806e255f257e5ed7e92b3d2687fdf 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-mapping-data.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=05009d140f76593c52625aeca806a8a3 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-mapping-data.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=9a7e187bb872fc6fb49fe2aa8edc94c9 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-mapping-data.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=72c9c51a3c104ed5c001956cdc32720f 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-mapping-data.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=21df66bd5ebc7e47502c668d61ab28a3 2500w" />

Once you've mapped your desired data to Clay, future webhooks will automatically sync the same Loops data to your Clay table. You can test this by adding another contact to your Loops audience.

If you ever want to check or view the data coming into Clay, clicking on cells in the **Webhook** column will show the full request body for each request.

## Send Clay contacts to Loops

You can sync data to your Loops audience from Clay using a custom enrichment in your tables. This sends contact data to Loops whenever a row is created or updated (or on a manual schedule).

### Create a connection to the Loops API

Add an API connection to your table in Clay by selecting **Add enrichment** and searching for **HTTP API** as the data source.

In the **Account** section of the sidebar, click **+ Add account** or select an existing connection.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-add-connection.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=84bf6cb0cf929ab387c302f7822b80f3" alt="Add a connection" data-og-width="2280" width="2280" data-og-height="1442" height="1442" data-path="images/clay-add-connection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-add-connection.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=ae4b0a4391ac56e94bdc249adcb47681 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-add-connection.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=65d21d4c56bba77d70b62c2ca74922d3 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-add-connection.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=c6949e9edabefb64867ed4d1549d993d 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-add-connection.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b348eeb4716bcc46d5d2c2deeeb16f8b 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-add-connection.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=26a932f4c19f2d87a57626a1773398b2 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-add-connection.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e1b93067d382c16e01e240fbbb891371 2500w" />

If you're adding a new connection, give the connection a name (e.g. "Loops") and then add the two API Request Headers listed below.

You'll need to generate or copy an API key from [Settings -> API](https://app.loops.so/settings?page=api) in Loops and replace `<api_key>` with the key.

| Key           | Value              |
| :------------ | :----------------- |
| Authorization | `Bearer <api_key>` |
| Content-Type  | `application/json` |

Click **Save** to create the connection.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-api-connection.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b3515f094f932673c3a09663f104037c" alt="Connection details" data-og-width="2280" width="2280" data-og-height="1770" height="1770" data-path="images/clay-api-connection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-api-connection.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f727537ed834d33c99eba46b47876171 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-api-connection.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d364dd600da0e66be661793a88e0dff3 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-api-connection.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=eac3cc961e64a10693ff67a646b58b08 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-api-connection.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=7a3317c04e3265c6cfc605319395bf61 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-api-connection.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=e6cc94f10c73bdc4ab4c8269c1ff1c48 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-api-connection.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=acd6799cdf83936872fac2927844ef05 2500w" />

<Tip>
  If you want to edit the connection in the future, you can do so from **Settings -> Connections** in Clay.
</Tip>

### Create an API request

We're going to set up an "update contact" API request, which will *create or update* contacts in Loops.

In the **Configure** section, select "PUT" from **Method** dropdown and enter the following URL into the **Endpoint** field:

```
https://app.loops.so/api/v1/contacts/update
```

In the **Body** field, you can build up the request, using data from your table. Type `/` to add columns, and make sure to wrap values in quotes to create valid JSON data for the API.

<Warning>
  You must include an `email` in the request body.
</Warning>

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-contact-api-request.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f90f63ef59a67498cf661ff89611f365" alt="API request body" data-og-width="2280" width="2280" data-og-height="1736" height="1736" data-path="images/clay-contact-api-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-contact-api-request.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=274633846816f1211566f90a3eee5a3c 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-contact-api-request.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=d14ac3c08076037a754180e99ae9b21c 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-contact-api-request.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=f05163d4aa91c9259a7dd36981235f9c 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-contact-api-request.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=43c875e18738edcce50f476383b96e7c 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-contact-api-request.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=269c2c075d134e7418d7eacbd80a0324 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-contact-api-request.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=dc15c88879a5c0b25b8fedaad6e91c14 2500w" />

Data will be sent to Loops automatically when a row is created or updated when the **Auto-update** option is enabled. Toggle this off to only sync data manually.

<Tip>
  To edit the request in the future, click on the **HTTP API** column header and select **Edit column**.
</Tip>

<CardGroup>
  <Card title="Update contacts" href="/api-reference/update-contact" icon="user-pen">
    Read the API documentation for updating contacts
  </Card>
</CardGroup>

### Test the setup

To test the connection and request you created, click **Save** and then **Save and run (x) rows in this view**.

If the sync succeeds, you'll see the cell populate with "200", which means a successful API request was made.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-successful-request.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=288d35fc837631b72776cbec2bded881" alt="200 means success" data-og-width="2280" width="2280" data-og-height="656" height="656" data-path="images/clay-successful-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-successful-request.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6ede67453d714913f9b8c453e0567070 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-successful-request.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=6d598a73f1c98f4b0a56c3d5b1fb1d05 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-successful-request.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=bc37dcd97c8aab78ccdcd4f232f47b87 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-successful-request.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=699d4ba127d63d8411f2f6f26b4dad83 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-successful-request.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=b5fb3be8307e1ecfdd8d65bec3dc33e7 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-successful-request.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0d4d6ed1b89aa3533bd7e1b9b405bd7b 2500w" />

If there is an error sending data to Loops, you can click on the cell in the **HTTP API** column to see the error message returned by the API, including the reason for the failure.

## Send events from Clay

You can trigger [loops](/loop-builder) from inside Clay by [sending events](/events) with the Loops API.

### Create an event and a loop

An [event](/events) allows you to start a loop when something happens in an external platform (like Clay). Loops can contain emails, timers, and filters.

<CardGroup>
  <Card title="Events" href="/events" icon="bolt">
    Learn more about events
  </Card>

  <Card title="Loops" href="/loop-builder" icon="arrows-rotate">
    Learn more about loops
  </Card>
</CardGroup>

To define your event, go to [Settings -> Events](https://app.loops.so/settings?page=events) and click **Create**. You can specify [event properties](/events/properties) for the event, which are data about specific events that you can add into your emails to personalize them for each recipient.

<img src="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/edit-event.png?fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=f33969bee2b8d531d23a8808ec7a99a3" alt="Create an event" data-og-width="2280" width="2280" data-og-height="1476" height="1476" data-path="images/edit-event.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/edit-event.png?w=280&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=b56ee39e1ed626c98663e4969cd6fa68 280w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/edit-event.png?w=560&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=ae5a6f4b4e174e4d872183d937a87832 560w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/edit-event.png?w=840&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=42080bb6e1c8d29b0e4f4b1d2cdbb45a 840w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/edit-event.png?w=1100&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=7cec9ba050ed6d9acc5d6a48f3353252 1100w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/edit-event.png?w=1650&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=77f2fbae5a92bdb52d974f34a9c7b0db 1650w, https://mintcdn.com/loops/I7MiNuGd9K5dwTEQ/images/edit-event.png?w=2500&fit=max&auto=format&n=I7MiNuGd9K5dwTEQ&q=85&s=33a30fd8d8a58a3a517dc93e42d2a154 2500w" />

When you're done, go to the [Loops page](https://app.loops.so/loops) to create a new loop. Use the "Event received" trigger and select your event from the previous step.

In this loop, add as many emails as you want plus timers to space them out. You can personalize emails by [adding event properties](/events/properties#using-event-properties-in-emails) into your emails body, subject and other sending settings fields.

<img src="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-email.png?fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=d07521dcddc09d27873e6989f4fa401a" alt="Loop email" data-og-width="2280" width="2280" data-og-height="1434" height="1434" data-path="images/loop-email.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-email.png?w=280&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=6072619c6abe36533c0adfb00f226daf 280w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-email.png?w=560&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b5512836d5a3db7eab8acdb0330ba636 560w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-email.png?w=840&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=620701d107b3046d5ecc5206c44cdc7d 840w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-email.png?w=1100&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=c5520a47aed0759ffdf1621e2fb38cef 1100w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-email.png?w=1650&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=1b38c387aacccdd760caf73043dbdf0d 1650w, https://mintcdn.com/loops/OG31ikb--92jQDlq/images/loop-email.png?w=2500&fit=max&auto=format&n=OG31ikb--92jQDlq&q=85&s=b8258313fb3fc653c98346481effa93d 2500w" />

### Create an API request

To send an event with the API from Clay, we need to make a request containing our event data. If you've added event properties to your emails, we need to include those in the request.

Add a new enrichment to your table in Clay by selecting **Add enrichment** and searching for **HTTP API** as the data source. Then create or select an existing connection to the Loops API. Follow the [steps outlined above](#create-a-connection-to-the-loops-api).

In the **Configure** section of your HTTP API enrichment, select "POST" from **Method** dropdown and enter the following URL into the **Endpoint** field:

```
https://app.loops.so/api/v1/events/send
```

In the **Body** field, you can build up the request, using data from your table. Type `/` to add columns, and make sure to wrap values in quotes to create valid JSON data for the API.

<Warning>
  You must include an `eventName` and an `email`/`userId` in the request body. [Read more](/api-reference/send-event#body)
</Warning>

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-api-request.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=c3b3f108ffa7f3fff9eac48389274ee4" alt="API request body" data-og-width="2280" width="2280" data-og-height="1736" height="1736" data-path="images/clay-event-api-request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-api-request.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=bf0dc103a43659faef3475f0ded12bc1 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-api-request.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=9060c3d109d37b99bf68c751d00a7a3b 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-api-request.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=dd494d5aaf7bf305d0088c52bb4595ce 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-api-request.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=1842e0b13567cbe92dc1d9f2c730ab9f 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-api-request.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=8cc47d12ee3224c2d14549069658bcc2 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-event-api-request.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=781259e7bcb98ce9785c88f3344478fa 2500w" />

<Tip>
  You can also update contact information in Loops in the same request by including contact properties alongside `email` in the root of the request body. [More info](/api-reference/send-event#contact-properties)
</Tip>

Events will be sent to Loops automatically when a row is created or updated with the **Auto-update** option enabled. Toggle this off to only sync data manually.

You can use the **Only run if** option to only send events when a certain condition is met.

<img src="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-conditional-sending.png?fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=fd0c353c20024d3f94797f1712bbeaef" alt="Conditional sending" data-og-width="2280" width="2280" data-og-height="1208" height="1208" data-path="images/clay-conditional-sending.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-conditional-sending.png?w=280&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=cf8b8f27e64b913205fb151a33b47220 280w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-conditional-sending.png?w=560&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=ec4abfc5a899183f13110466bc776db6 560w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-conditional-sending.png?w=840&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=0e929fbc771a4ce1af45e086ecd30b42 840w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-conditional-sending.png?w=1100&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=09f3331d3a3f072899e8322b00554da2 1100w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-conditional-sending.png?w=1650&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=bf53dce20eeeba36e1619f8126887c75 1650w, https://mintcdn.com/loops/K9TRANbphBauR0pJ/images/clay-conditional-sending.png?w=2500&fit=max&auto=format&n=K9TRANbphBauR0pJ&q=85&s=1de3e1979bc9dc5818fcccefd431a837 2500w" />

<Tip>
  To edit the request in the future, click on the **HTTP API** column header and select **Edit column**.
</Tip>

<CardGroup>
  <Card title="Send event" href="/api-reference/send-event" icon="bolt">
    Read the API documentation for sending events
  </Card>
</CardGroup>

### Test the setup

Review the [information in the previous section](#test-the-setup) to see how to test your setup
