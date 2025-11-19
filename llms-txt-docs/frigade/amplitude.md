# Source: https://docs.frigade.com/integrations/amplitude.md

# Amplitude

Frigade supports sending events to Amplitude. The following guide will help you set up this integration in just a few steps.

## Sending Frigade events to Amplitude

You can set up Frigade to send events to Amplitude when your users take actions in your Flows.
The event types and data schema is identical to the events sent in [Frigade Webhooks](/api-reference/webhooks).

<Steps>
  <Step title="Copy your Amplitude API Key">
    Log in to your Amplitude account, open the settings menu, and select **Organization settings**. Select the **Projects** tab and copy the API Key for the project you want to send events to. Do not copy the secret API key as only the public API key is required.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/amplitude-1.png" className="rounded" />
  </Step>

  <Step title="Add Amplitude as an integration in Frigade">
    Open the **Integrations** page in Frigade and select **Amplitude**. Paste the API key you copied in step 1 and click **Save**. If the integration is enabled, events will start streaming to Amplitude immediately.

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/integrations/amplitude.png" className="rounded" />
  </Step>

  <Step title="See data in Amplitude">
    Open the dashboard for the project you selected in step 1 and take some action in any given Frigade Flow such as completing a step. You should see events starting to stream from Frigade in the **Realtime event stream** widget:

    <img src="https://mintlify.s3.us-west-1.amazonaws.com/frigade-docs/images/amplitude-2.png" className="rounded" />
  </Step>
</Steps>

## Sending Amplitude data to Frigade

Bidirectional read/write to Amplitude is not yet available on all Frigade plans. If you're interested in this feature, please [get in touch](mailto:support@frigade.com).
