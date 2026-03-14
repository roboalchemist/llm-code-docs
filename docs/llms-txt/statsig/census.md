# Source: https://docs.statsig.com/integrations/data-connectors/census.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Census

## Overview

Enabling the [Census](https://getcensus.com/) integration for Statsig allows Statsig to receive events from Census. This enables you to ingest data into Statsig from any sources that Census supports.

You can find all events that Statsig receives from Census in the [Metrics](/metrics) tab in the Statsig console. Statsig will automatically include these events in [Pulse](/pulse/read-pulse) and [Experiment](/experiments-plus/monitor) results for your feature gates and experiments respectively.

## Configuring Incoming Events

1. From the [API Keys](https://console.statsig.com/api_keys) tab in the Statsig console, copy the Statsig "Server Secret Key”.
2. From census, create a new [destination](https://docs.getcensus.com/destinations/overview) and select Statsig from the list of options.
3. Paste the Statsig secret into the field and click save.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/census/b3134399-288d-4a0f-b4d2-4b88980f0718.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=4567dac0d9decfd27c30dede01618ff0" alt="Census destination setup form with Statsig secret key input" width="966" height="406" data-path="images/integrations/data-connectors/census/b3134399-288d-4a0f-b4d2-4b88980f0718.png" />
</Frame>

4. Create a Sync to the new Statsig destination (see [Sync Configuration](#sync-configuration) section below)
5. On the Statsig [Integrations](https://console.statsig.com/integrations) page, enable the Census integration.

### Sync Configuration

A sync key is required to uniquely identify each event.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/census/e5d1154d-bd55-48d8-a300-13d96a89a0c8.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=8dc18908d9a4fc4c7d36ebd9aed2b57c" alt="Census sync configuration showing sync key selection" width="936" height="179" data-path="images/integrations/data-connectors/census/e5d1154d-bd55-48d8-a300-13d96a89a0c8.png" />
</Frame>

The following fields are required when mapping to Statsig events.

* `User ID` -> `userID`
* `Event Name` -> `eventName`
* `Timestamp` -> `timestamp`
* `Value` -> `value`

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/census/7fce9183-312c-4b47-90c4-b48b0479ecca.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=d8749f1b7a0ed7dcdc1e3c8c80d40ec1" alt="Field mapping table aligning Census columns to Statsig event fields" width="946" height="286" data-path="images/integrations/data-connectors/census/7fce9183-312c-4b47-90c4-b48b0479ecca.png" />
</Frame>

All other fields will be included in the `metadata` section of the mapped Statsig event.

### Custom ID Mapping

The Census integration allows the mapping of arbitrary fields to Statsig Custom IDs. To do this, visit the Census panel on the Statsig [Integrations](https://console.statsig.com/integrations) page and look for the "Map Identifier" section. Here you can choose fields you would like mapped to a Custom ID.

<Note>
  The input Event Field must match the exact spelling as in the original Census event.
</Note>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/census/213269548-e6457527-c938-44fd-9360-1f3fd7af2fac.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=116606358974652e6e18490eae58ec3c" alt="Statsig integration panel for Census custom ID mapping" width="841" height="609" data-path="images/integrations/data-connectors/census/213269548-e6457527-c938-44fd-9360-1f3fd7af2fac.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).