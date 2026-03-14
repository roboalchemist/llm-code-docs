# Source: https://docs.statsig.com/integrations/data-connectors/amplitude.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Amplitude

## Overview

Statsig supports both incoming and outgoing events for Amplitude. As well as adding Amplitude Cohorts to Statsig ID Lists.

## Incoming - Receiving Events From Amplitude

The following steps outline how to forward events from Amplitude into Statsig.

1. Get a Statsig "Server Secret Key" from the API keys page in [Project Settings](https://console.statsig.com/api_keys).

2. Go to Amplitude and navigate to the Data Destinations page. Click the
   "Add Destination" button in the top right.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/amplitude/step_1.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=663f43c9f91cc8ab4432dcb853f94dc9" alt="Amplitude Data Destinations page showing Add Destination button" width="1822" height="1384" data-path="images/integrations/data-connectors/amplitude/step_1.png" />
   </Frame>

3. From the Destinations Catalog, search for and select the Statsig Event
   Streaming destination.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/amplitude/step_2.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=b0e94cfbf14330d69e085d5370d867bb" alt="Destinations catalog highlighting Statsig event streaming option" width="1698" height="1424" data-path="images/integrations/data-connectors/amplitude/step_2.png" />
   </Frame>

4. Give this destination a name and click "Create Sync".

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/amplitude/step_3.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=ce6fe766a4b4c044cf96adef7f088ec6" alt="Create Sync form for Statsig destination" width="2454" height="1414" data-path="images/integrations/data-connectors/amplitude/step_3.png" />
   </Frame>

5. Enter the "Server Secret Key" you copied in Step 1 into the provided
   field. Select the events you wish to send to Statsig. Ensure that the
   Status is set to "Enabled" and then click "Save".

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/amplitude/step_4.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=74673574479e414a328da4d4cc5de933" alt="Statsig destination settings entering server secret key and event selection" width="2296" height="1580" data-path="images/integrations/data-connectors/amplitude/step_4.png" />
   </Frame>

6. *Enable the integration* - On the Integrations page for your Statsig project, enable the Amplitude Incoming integration.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/data-connectors/amplitude/09de394e-dcc7-4a80-81fb-ae4cc58b25a1.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=063da1bb6667cc0534e1a3d8fe6e66c5" alt="Statsig integration panel confirming Amplitude connection" width="805" height="450" data-path="images/integrations/data-connectors/amplitude/09de394e-dcc7-4a80-81fb-ae4cc58b25a1.png" />
   </Frame>

## Outgoing - Sending Statsig Events to Amplitude

1. Navigate to Amplitude and click on the Settings button in the
   bottom-left corner.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/amplitude/settings.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=ff40a41bcb6b4d72c7c1a710cf6a87a7" alt="Amplitude settings menu accessed from bottom-left" width="2256" height="1122" data-path="images/integrations/data-connectors/amplitude/settings.png" />
   </Frame>

2. Click on the Projects tab and choose the Project you wish to send data
   to.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/amplitude/project.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=eb28a5861506d74855fa4646def9168d" alt="Amplitude Projects tab listing available workspaces" width="587" height="296" data-path="images/integrations/data-connectors/amplitude/project.png" />
   </Frame>

3. Copy the API Key and paste it in the Statsig integration panel.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/data-connectors/amplitude/api_key.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=14a3767d90c84d7cb4012328d7d3f271" alt="Amplitude project API key display" width="519" height="482" data-path="images/integrations/data-connectors/amplitude/api_key.png" />
   </Frame>

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/data-connectors/amplitude/197276579-b3884a8f-ed47-4cd9-8852-c37f40958554.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=01f8e321718957dec5796039c951a4d9" alt="Statsig integration panel fields for Amplitude API key" width="549" height="350" data-path="images/integrations/data-connectors/amplitude/197276579-b3884a8f-ed47-4cd9-8852-c37f40958554.png" />
   </Frame>

4. Hit Enable on the integration panel and any data logged to Statsig will show up in your
   Amplitude Project account.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/data-connectors/amplitude/amplitude_data.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=b7e0afa701d096026e818f4eebd474dc" alt="Amplitude event stream showing Statsig exposure events" width="778" height="84" data-path="images/integrations/data-connectors/amplitude/amplitude_data.png" />
   </Frame>

## First Exposures

[First exposures](/pulse/export#first-exposures-file-description) are an enterprise-tier feature that simplifies your project insights.

<Info>
  This is available for Enterprise contracts. Please reach out to our support team, your sales contact, or via our [Slack community](https://statsig.com/slack) if you want this enabled.
</Info>

### What is it?

Our Amplitude Integration offers the flexibility to forward first exposures instead of every exposure, reducing the overall number of events being forwarded. First exposures are calculated daily and forwarded to integrations at around 7pm UTC.

### How to enable

First ensure that the "first exposure" feature has been enabled for your company by reaching out to support team, your sales contact, or via our [Slack community](https://statsig.com/slack).
Once this is done you will be able to go into the event filtering tab of the integration and enabled "First Exposure" setting.

### Example Events In Amplitude

Example of a get\_experiment First Exposure in Amplitude.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/CdxKvlj2hGtAFimZ/images/integrations/data-connectors/amplitude/5e945a95-8c7b-4181-8440-8e60502455e2.png?fit=max&auto=format&n=CdxKvlj2hGtAFimZ&q=85&s=345dc90dcdd3910b6c41c2b78da64c09" alt="Example first exposure event in Amplitude log" width="632" height="942" data-path="images/integrations/data-connectors/amplitude/5e945a95-8c7b-4181-8440-8e60502455e2.png" />
</Frame>

### Accessing Raw Data

For a comprehensive view, you can obtain the raw first exposure data in CSV format. Simply make a request to the [console/v1/reports](/console-api/daily-reports#get-/reports) endpoint to receive a download link.

## Cohort Sync - Syncing Amplitude Cohorts to Statsig Segments

For up to date configuration information on syncing Cohorts (aka Segments) from Amplitude to Statsig, please take a look at Amplitude's documentation [here](https://www.docs.developers.amplitude.com/data/destinations/statsig-cohort/).

<Warning>
  Ensure you create and use a console API key from your [Statsig project settings](https://console.statsig.com/api_keys)
</Warning>

## Filtering Events

You can customize which events should be sent and received via Amplitude using [Event Filtering](/integrations/event_filtering)


Built with [Mintlify](https://mintlify.com).