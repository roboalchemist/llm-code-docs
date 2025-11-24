# Source: https://docs.frigade.com/integrations/segment.md

# Segment

Frigade supports bidirectional reads and writes from Segment. This guide shows you how to get started in a few minutes.

## Sending Segment data to Frigade

You can set up Frigade as a destination for Segment identify, group, and track calls by using [Webhooks as a destination](https://segment.com/docs/connections/destinations/catalog/webhooks/).

<Steps>
  <Step title="Add webhook destination">
    Log in to your Segment account, open workspace, and select source. Click on **Add Destination** and search and select **Webhooks**.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/segment-1.png" className="rounded" />
  </Step>

  <Step title="Create mapping">
    Next after creating the destination, click the **Mappings** tab and add a new mapping:

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/segment-2.png" className="rounded" />
  </Step>

  <Step title="Select event types to send to Frigade">
    Select the event types you want to send to Frigade. In this example we select identify, group, and track, but you can select any event type you want to send to Frigade.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/segment-3.png" className="rounded" />
  </Step>

  <Step title="Add Frigade Webhook URL">
    Fill out the **Select mappings** as shown below using:

    * `https://api.frigade.com/v1/thirdParty/cdp/segment` as the URL
    * `POST` as **Method**
    * `100` as **Batch Size**. Note: if you send fewer than 500 events per day, it is recommended to set this to a lower value to avoid delays in sending events to Frigade.
    * Your secret Frigade API key (it will be the one prefixed with `api_private`). This key can be found in the dashboard under [API Keys](https://app.frigade.com/developer). Make sure to prefix it with `Bearer` as shown in the screenshot below.
    * `Authorization` as the key

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/segment-4.png" className="rounded" />

    Finally, set **Enable Batching?** to **Yes**. Optionally, you can send a test event to verify that the webhook is working. Click **Save** to save the webhook.
  </Step>

  <Step title="Turn on the webhook">
    Finally, turn on the webhook by turning on the mapping you just created. Then, open the **Settings** tab and enable the Destination.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/segment-5.png" className="rounded" />

    Congratulations! You have successfully set up Frigade as a destination for Segment. You can now use Frigade's [Targeting](/platform/targeting) with your Segment data to create personalized experiences for your users.
  </Step>
</Steps>

## Sending Frigade data to Segment

Frigade also supports sending user and organization events from Frigade Flows to Segment.

<Steps>
  <Step title="Add your Segment write key">
    To send events to your Segment instance, select **Add Source** and then **HTTP API**. Then, copy your Segment write key.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/segment-write.png" className="rounded" />
  </Step>

  <Step title="Add Segment in Frigade">
    Next, go to your Frigade dashboard and select **Integrations**. Click **Add Integration** and select **Segment**.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/segment.png" />

    You will be asked to enter your Segment write key. Click **Connect** to save the integration. Shortly after, events will start streaming from Frigade in real-time.
  </Step>
</Steps>
