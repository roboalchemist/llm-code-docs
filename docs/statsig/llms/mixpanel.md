# Source: https://docs.statsig.com/integrations/data-connectors/mixpanel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Mixpanel

## Overview

The [Mixpanel](https://mixpanel.com/) integration has two functions.

* Incoming: Statsig can sync your Mixpanel user cohorts with a Statsig ID list segment.
* Outgoing: Statsig can forward Statsig events to Mixpanel.

## Cohort Syncing

Statsig can ingest user information via a [Mixpanel Cohort Syncing](https://developer.mixpanel.com/docs/cohort-webhooks)

1. On Statsig, navigate to [Segments](https://console.statsig.com/segments) on the left navigation menu and create a segment.

* **Name**: Must match the name of your Mixpanel cohort.
* **Type of segment**: Should be ID List.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/RMs0i7ONYpBtCIa5/images/integrations/data-connectors/mixpanel/id_list_segments.png?fit=max&auto=format&n=RMs0i7ONYpBtCIa5&q=85&s=a4770bbd455eb33b73201738fb055a91" alt="statsig-segment-config" width="914" height="438" data-path="images/integrations/data-connectors/mixpanel/id_list_segments.png" />
</Frame>

2. On Mixpanel, click on the Data Management navbar item and choose Integrations from
   the dropdown.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/mixpanel/195173611-170f02df-543f-4198-8589-7db313f4dd9f.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=5cd69797da3e810eb1ad0b4b07a94d58" alt="mixpanel-integration-menu" width="521" height="601" data-path="images/integrations/data-connectors/mixpanel/195173611-170f02df-543f-4198-8589-7db313f4dd9f.png" />
</Frame>

3. In the list of integrations, scroll until you find Custom Webhook and then
   select it.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/mixpanel/195173845-73ac1d5b-94b4-4daf-bf36-102eabd5d1fe.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=8fe1ba3626050818fd0d195ac2a00aa0" alt="mixpanel-custom-webhook" width="1132" height="269" data-path="images/integrations/data-connectors/mixpanel/195173845-73ac1d5b-94b4-4daf-bf36-102eabd5d1fe.png" />
</Frame>

4. In the dialog that appears, paste the url below, substituting the
   SERVER\_SECRET\_KEY with a "Server Secret Key" found in [Project Settings](https://console.statsig.com/api_keys), then click Continue.

```
https://api.statsig.com/v1/webhooks/mixpanel?statsig-api-key=SERVER_SECRET_KEY
```

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/mixpanel/195174446-d3e8078c-ebaf-4ed4-bb5b-f8195694bade.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=d52ca87ed5d50c4b0399c2555c481ad1" alt="custom-webhook-dialog" width="582" height="535" data-path="images/integrations/data-connectors/mixpanel/195174446-d3e8078c-ebaf-4ed4-bb5b-f8195694bade.png" />
</Frame>

5. Click "Enable" (or "Confirm" if you are updating the integration).

6. You can now kick off a cohort sync job on Mixpanel from the Cohorts page.

## Configuring Outbound Events

To export your Statsig events to Mixpanel:

1. Get a copy of your "Project Token" from Mixpanel by following this [guide](https://help.mixpanel.com/hc/en-us/articles/115004502806-Find-Project-Token-).

2. Paste your project token into the Outgoing configuration on the Statsig integration panel.

3. Select your **Data Residency Region** based on your Mixpanel project's data residency configuration:
   * **US** (default): Events are sent to the global `api.mixpanel.com` endpoint
   * **EU**: For projects using [EU data residency](https://docs.mixpanel.com/docs/privacy/eu-residency)
   * **India**: For projects using [India data residency](https://docs.mixpanel.com/docs/privacy/in-residency)

4. Hit "Enable" (or "Confirm" if you are updating the integration).

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/jyjU3itJM18ouNls/images/integrations/data-connectors/mixpanel/mixpanel-outgoing-data-residency.png?fit=max&auto=format&n=jyjU3itJM18ouNls&q=85&s=9e30af9acc918edd0d84c087a28d2283" alt="mixpanel-outgoing-configuration" width="1591" height="919" data-path="images/integrations/data-connectors/mixpanel/mixpanel-outgoing-data-residency.png" />
   </Frame>

5. Verify your events are being forwarded by visiting the Events tab on Mixpanel.

   <Frame>
     <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/mixpanel/195172678-8ff14bfe-6400-4660-b1dd-fef1780ddcd5.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=002fe7679a0c4b54902a2bb2842fe5a8" alt="mixpanel-event-tab" width="1122" height="518" data-path="images/integrations/data-connectors/mixpanel/195172678-8ff14bfe-6400-4660-b1dd-fef1780ddcd5.png" />
   </Frame>

### Filtering Events

You can customize which events should be sent to Mixpanel using [Event Filtering](/integrations/event_filtering#outgoing-event-filtering)


Built with [Mintlify](https://mintlify.com).