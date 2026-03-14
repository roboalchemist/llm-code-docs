# Source: https://docs.statsig.com/integrations/data-connectors/fivetran.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fivetran

## Overview

Enabling the Fivetran integration for Statsig will allow Statsig to push events to your Fivetran account through a webhook. This allows you to forward Statsig data to any connectors available from Fivetran.

## Configuring Outbound Events

1. Follow the steps in the [Fivetran Webhook Setup Guide](https://fivetran.com/docs/events/webhooks/setup-guide) to create a new Webhook URL.
2. On the Statsig [Integrations](https://console.statsig.com/integrations) page, enable the Fivetran integration by pasting in the Fivetran Webhook URL and click **Confirm**.

### Event Format

Events will be sent in batches in a JSON format. The structure of a Statsig Event sent will look like the following:

| Field           | Type   | Description                                                      |
| --------------- | ------ | ---------------------------------------------------------------- |
| eventName       | String | Name of the event provided                                       |
| user            | JSON   | [Statsig User Object](/concepts/user)                            |
| userID          | String | User ID provided                                                 |
| timestamp       | Number | Timestamp in MS of the event                                     |
| value           | String | Value of the event provided                                      |
| metadata        | JSON   | Custom Metadata provided                                         |
| statsigMetadata | JSON   | Metadata related to the logging of this event added by Statsig   |
| timeUUID        | String | UUID for the event                                               |
| unitID          | String | Unit ID of the exposure (e.g. userID, stableID, or the customID) |

#### Custom Event Formatting - logEvent

>

```json  theme={null}
{
  "eventName": "my_custom_event",
  "user": {
    "userID": "a_user",
    "email": "a.user@email.com"
  },
  "userID": "a_user",
  "timestamp": "1655231253265",
  "statsigMetadata": {
    ...
  },
  "value": "a_custom_value",
  "metadata": {
    "key_a": "value_a",
    "key_b": "123"
  },
  "timeUUID": "abd2a983-ec0f-11ec-917a-fb8cdaeda578"
}
```

#### Feature Gate Exposure Formatting - checkGate

>

```json  theme={null}
{
  "eventName": "statsig::gate_exposure",
  "user": { ... },
  "userID": "a_user",
  "timestamp": "1655231253265",
  "statsigMetadata": { ... },
  "value": "",
  "metadata": {
    "gate": "a_gate",
    "gateValue": "false",
    "ruleID": "default",
    "reason": "Network",
    "time": "1655231249644"
  },
  "timeUUID": "8d7c1040-ec11-11ec-g123-abe2c32fcf46",
  "unitID": "userID"
}
```

#### Dynamic Config Exposure Formatting - getConfig

>

```json  theme={null}
{
  "eventName": "statsig::config_exposure",
  "user": { ... },
  "userID": "a_user",
  "timestamp": "1655231253265",
  "statsigMetadata": { ... },
  "value": "",
  "metadata": {
    "config": "a_config",
    "ruleID": "default",
    "reason": "Network",
    "time": "1655231249644"
  },
  "timeUUID": "af379f60-ec11-22ad-8e0a-05c3ee70bd0c",
  "unitID": "userID"
}
```

#### Experiment Exposure Formatting - getExperiment

>

```json  theme={null}
{
  "eventName": "statsig::experiment_exposure",
  "user": { ... },
  "userID": "a_user",
  "timestamp": "1655232119734",
  "statsigMetadata": { ... },
  "value": "",
  "metadata": {
    "config": "an_experiment",
    "ruleID": "4SauZJcM1T7zNvh1igBjwE",
    "reason": "Network",
    "time": "1655231249644",
    "experimentGroupName": "Control"
  },
  "timeUUID": "af379f61-ab22-11ec-8e0a-05c3ee70bd0c",
  "unitID": "userID"
}
```

#### Example Batch

>

```json  theme={null}
[
  {
    "eventName": "page_view",
    "user": {"userID": "user_1", "country": "US"},
    "userID": "user_1",
    "timestamp": 1644520566967,
    "value": "example_value",
    "metadata": {"page": "home_page"},
    "statsigMetadata": {},
    "timeUUID": "f4c414a0-8ab5-11ec-a8a3-0242ac120002"
  },
  {
    "eventName": "statsig::gate_exposure",
    "user": {"userID": "user_1", "country": "US"},
    "userID": "user_1",
    "timestamp": 1644520566968,
    "value": "",
    "metadata": {"gate": "test_gate", "gateValue": "true", "ruleID": "default"},
    "statsigMetadata": {},
    "timeUUID": "f4c414a0-8ab5-11ec-a8a3-0242ac120003",
    "unitID": "userID"
  },
  {
    "eventName": "statsig::experiment_exposure"
    "user": {"userID": "user_1", "country": "US"},
    "userID": "user_1",
    "timestamp": 1644520566969,
    "value": "",
    "metadata": {
       "config": "an_experiment", "ruleID": "4SauZJcM1T7zNvh1igBjwE", "reason": "Network", "time": "1655231249644", "experimentGroupName": "Control"
    },
    "statsigMetadata": {},
    "timeUUID": "f4c414a0-8ab5-11ec-a8a3-0242ac120004",
    "unitID": "userID"
  }
]
```

## Filtering Events

Once you've enabled outbound events to Fivetran, you can select which categories of Statsig events you want to export by click on the **Event Filtering** button and checking the appropriate boxes as shown below.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/fivetran/150854805-c70a1e01-5d3e-407f-9f2b-2eccafbe04a3.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=a4b90cd1220bdea69d7234bff017fa1a" alt="Event filtering configuration interface" width="538" height="369" data-path="images/integrations/data-connectors/fivetran/150854805-c70a1e01-5d3e-407f-9f2b-2eccafbe04a3.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/aXbnJ_Igoga8-0MX/images/integrations/data-connectors/fivetran/150855038-fc6add6c-48ed-4063-8fdf-b210b43a3308.png?fit=max&auto=format&n=aXbnJ_Igoga8-0MX&q=85&s=8c5b9751093d891803821fe59153e772" alt="Event category selection checkboxes" width="404" height="609" data-path="images/integrations/data-connectors/fivetran/150855038-fc6add6c-48ed-4063-8fdf-b210b43a3308.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).