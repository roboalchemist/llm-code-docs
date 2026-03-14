# Source: https://docs.statsig.com/integrations/data-connectors/google-analytics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Analytics

Enabling the Google Analytics 4 integration allows Statsig to send logged events and exposures to GA4. This enhances your existing Google Analytics tracking with additional data collected by Statsig's logging SDKs.

Once enabled, Statsig will forward exposures and logged events to a configured Data Stream. These events can be filtered with [event filtering.](/integrations/data-connectors/google-analytics#filtering-events)

### Benefits of using the Google Analytics 4 integration

Using the GA4 Integration allows you to log additional events without having the orchestrate two libraries, thus simplifying your code. Furthermore by implementing this integration, you'll be able to join data about experiments you create in Statsig to existing analytics events you care about in Google Analytics, giving you greater insights into different experiments' impact on your user interactions.

## Configuring outbound events to Google Analytics 4

To send events collected by Statsig's SDKs to GA4, you must configure a Data Stream and provide a few pieces of information.

1. Navigate to the GA4 admin settings. Under your app's property click Data Streams and select the stream you'd like to use. If you don't have a stream you'll need to create one.

2. Statsig requires an API secret to send the data to your stream, navigate to your stream and create a new secret:
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/google-analytics/263364181-a672aec0-15c1-4030-a4c8-2e2a58083d7e.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=1cacc740f893c71039975322792faa5c" alt="GA4 Data Stream details with Measurement Protocol API secrets section" width="2734" height="1096" data-path="images/integrations/data-connectors/google-analytics/263364181-a672aec0-15c1-4030-a4c8-2e2a58083d7e.png" />
   </Frame>
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/google-analytics/263364616-65a054d6-c0b7-48ba-84ee-cbdb7f5eaa9a.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=9a8ebd25d160922a551d7f321fcee6ca" alt="Create API secret dialog in GA4" width="2038" height="886" data-path="images/integrations/data-connectors/google-analytics/263364616-65a054d6-c0b7-48ba-84ee-cbdb7f5eaa9a.png" />
   </Frame>
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/google-analytics/263364730-b419ac78-01cb-453c-8cd3-c0b5f7a3cb6a.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=b9a4efe7b2ddc14fbe0041d2372d3fb5" alt="List of API secrets showing newly generated key" width="1272" height="338" data-path="images/integrations/data-connectors/google-analytics/263364730-b419ac78-01cb-453c-8cd3-c0b5f7a3cb6a.png" />
   </Frame>
   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/google-analytics/263364942-1fb5da05-dbfc-4362-86f8-8d77bdd23cd4.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=99504022883800aa30d5c8ca9568eb06" alt="Measurement ID highlighted on GA4 stream setup" width="1770" height="428" data-path="images/integrations/data-connectors/google-analytics/263364942-1fb5da05-dbfc-4362-86f8-8d77bdd23cd4.png" />
   </Frame>

3. Once created, copy the API secret and the measurement ID (optional). Navigate to your Statsig Project -> Project Settings -> Integrations -> Google Analytics (click enable) -> Google Analytics 4.

   Provide your API Secret and measurement ID from the previous step and click *confirm*:

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/google-analytics/263366565-c9f97636-8bd3-428f-b2ee-e542776b50ab.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=158ab06aef5616c610eeddc4e0b4d520" alt="Statsig integration configuration form for GA4 API secret and measurement ID" width="1494" height="854" data-path="images/integrations/data-connectors/google-analytics/263366565-c9f97636-8bd3-428f-b2ee-e542776b50ab.png" />
   </Frame>

4. Verify that you are receiving events now by checking the Realtime overview report for the event with name `statsig`. Account for a couple days of delay for events to be available in other reports.

5. You can also add the following custom event dimensions. Other custom IDs and custom user attributes are available as user dimensions

<ul>
  <li>`config` - Name of the experiment/gate/dynamic config</li>
  <li>`group` - Name of the exposed group (e.g. Control)</li>
  <li>`value` - Value for custom events</li>
  <li>`statsig_session_id` - Session ID</li>
  <li>`category` - Type of exposure or name of the custom event (e.g. `statsig_gate_exposure`)</li>
  <li>`unit_id` - Value of the unit ID (e.g. '123')</li>
  <li>`unit_id_type` - Type of the unit ID (e.g. 'stableID')</li>
</ul>

## Filtering Events

Once the outgoing integration has been enabled, you can optionally configure event filtering to control whch events are populating the GA4 Data Stream:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/google-analytics/264458718-69f0d248-7df3-4360-bdb4-dcffb1503e3c.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=4870b5d4ffe82dd47525d08392623287" alt="Event filtering UI specifying which Statsig events flow to GA4" width="661" height="901" data-path="images/integrations/data-connectors/google-analytics/264458718-69f0d248-7df3-4360-bdb4-dcffb1503e3c.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).