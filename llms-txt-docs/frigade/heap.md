# Source: https://docs.frigade.com/integrations/heap.md

# Heap

Frigade supports bidirectional reads and writes from Heap. This guide shows you how to get started in a few minutes.

## Sending Frigade data to Heap

The following steps will help you send data from Frigade to Heap. For instance, when a user completes a Survey or a step in a Checklist, Frigade can send this data to Heap.

<Steps>
  <Step title="Get your Heap Environment ID">
    From the Heap dashboard, navigate to **Settings** and open **Projects**.
    Click the appropriate project and environment and copy the numeric **Environment ID**.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/heap/1.png" className="rounded" />
  </Step>

  <Step title="Add Heap in Frigade">
    Next, go to your Frigade dashboard and select **Integrations**. Click **Add Integration** and select **Heap**.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/heap/2.png" className="rounded" />

    You will be asked to enter your Heap Environment ID. Click **Connect** to save and activate the integration. Shortly after, events will start streaming from Frigade in real-time.
  </Step>

  <Step title="See Frigade events in Heap">
    You should now see events from Frigade in your Heap dashboard. You can test the integration by completing a Flow and checking the **Live data feed** page in Heap:

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/heap/3.png" className="rounded" />
  </Step>
</Steps>

## Sending Heap segments to Frigade

<Note>This feature is in early preview. <a href="mailto:support@frigade.com">Reach out</a> to get early access.</Note>
