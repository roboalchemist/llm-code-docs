# Source: https://docs.statsig.com/integrations/data-connectors/stitch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Stitch

## Overview

Enabling the Stitch integration for Statsig will allow Statsig to push events to your Stitch account through a webhook. This allows you to forward Statsig data to any connectors available from Stitch.

## Configuring Outbound Events

1. Follow the steps in the [Stitch Webhook Setup Guide](https://www.stitchdata.com/docs/integrations/webhooks/stitch-incoming-webhooks#setup) to create a new Webhook URL.
2. On the Statsig [Integrations](https://console.statsig.com/integrations) page, enable the Stitch integration by pasting in the Stitch Webhook URL and click **Confirm**.

### Event Format

Events will be sent in batches in a JSON format. The structure of a Statsig Event sent will look like the following:

| Field     | Type   | Description                                                                                      |
| --------- | ------ | ------------------------------------------------------------------------------------------------ |
| event     | String | Name of the event provided                                                                       |
| user      | JSON   | [Statsig User Object](/concepts/user)                                                            |
| userId    | String | User ID provided                                                                                 |
| stableId  | String | Stable ID                                                                                        |
| timestamp | Number | Timestamp in MS of the event                                                                     |
| value     | String | Value of the event provided                                                                      |
| metadata  | JSON   | Both custom metadata provided and metadata related to the logging of this event added by Statsig |

#### Custom Event Formatting - logEvent

>

```json  theme={null}
{
  "userId": "a_user",
  "stableId": "123",
  "timestamp": 1655231253265,
  "event": "my_custom_event",
  "context": {
    "user": {
      "userID": "a_user",
      "email": "a.user@email.com"
    },
    "value": "a_custom_value",
    "metadata": {

    },
    "library": {
      "name": "statsig",
      "version": "1.0"
    }
  }
}
```

#### Feature Gate Exposure Formatting - checkGate

>

```json  theme={null}
{
  "userId": "a_user",
  "stableId": "123",
  "timestamp": 1655231253265,
  "event": "statsig::gate_exposure",
  "context": {
    "user": {
      "userID": "a_user",
      "email": "a.user@email.com"
    },
    "value": "",
    "metadata": {
      "gate": "a_gate",
      "gateValue": "false",
      "ruleID": "default",
      "reason": "Network",
      "time": "1655231249644"
    },
    "library": {
      "name": "statsig",
      "version": "1.0"
    }
  }
}
```

#### Dynamic Config Exposure Formatting - getConfig

>

```json  theme={null}
{
  "userId": "a_user",
  "stableId": "123",
  "timestamp": 1655231253265,
  "event": "statsig::config_exposure",
  "context": {
    "user": {
      "userID": "a_user",
      "email": "a.user@email.com"
    },
    "value": "",
    "metadata": {
      "config": "a_config",
      "ruleID": "default",
      "reason": "Network",
      "time": "1655231249644"
    },
    "library": {
      "name": "statsig",
      "version": "1.0"
    }
  }
}
```

#### Experiment Exposure Formatting - getExperiment

>

```json  theme={null}
{
  "userId": "a_user",
  "stableId": "123",
  "timestamp": 1655231253265,
  "event": "statsig::experiment_exposure",
  "context": {
    "user": {
      "userID": "a_user",
      "email": "a.user@email.com"
    },
    "value": "",
    "metadata": {
      "config": "an_experiment",
      "ruleID": "4SauZJcM1T7zNvh1igBjwE",
      "reason": "Network",
      "time": "1655231249644",
      "experimentGroupName": "Control"
    },
    "library": {
      "name": "statsig",
      "version": "1.0"
    }
  }
}
```

## Filtering Events

Once you've enabled outbound events to Stitch, you can select which categories of Statsig events you want to export by click on the **Event Filtering** button and checking the appropriate boxes as shown below.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/data-connectors/stitch/183725742-b58c87a7-fbb4-4f30-be9a-9d20c08cd7d0.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=d7568be946d05d268479aaf81e27b575" alt="Initial Setup Dialog" width="910" height="462" data-path="images/integrations/data-connectors/stitch/183725742-b58c87a7-fbb4-4f30-be9a-9d20c08cd7d0.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/data-connectors/stitch/183725752-b79b5c3f-d275-4dec-80ba-04fa9a73da0d.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=689e078a8c8c98890e5031ee9f73c453" alt="Event Filtering" width="683" height="870" data-path="images/integrations/data-connectors/stitch/183725752-b79b5c3f-d275-4dec-80ba-04fa9a73da0d.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).