# Source: https://docs.statsig.com/integrations/event_webhook.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Event Webhook

## Incoming

The Statsig Event Webhook allows you to log event data to Statsig from third party apps or other external sources to provide additional insights to your Statsig experiments and metrics.

Before using the Webhook, you will need to obtain your Projects' server secret key. An example call to the Statsig Event Webhook should look like the following:

```bash title="HTTP" theme={null}
POST https://api.statsig.com/v1/webhooks/event_webhook
```

```bash title="Headers" theme={null}
Content-Type: application/json
Accept: */*
STATSIG-API-KEY: {STATSIG_SERVER_SECRET}
```

```bash title="JSON Body" theme={null}
{
  "user": {
    "userID": {USER_ID},
    ...
  },
  "event": {EVENT_NAME},
  "value": {VALUE},
  "metadata": {
    "example_field_1": {EXAMPLE_VALUE_1},
    "example_field_2": {EXAMPLE_VALUE_2},
    ...
  },
  timestamp: {TIMESTAMP}
}
```

<div style={{ paddingBottom: "32px" }} />

***

## Outgoing

<div style={{ display: "flex", justifyContent: "center", marginBottom: "16px" }}>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/event_webhook/162286552-c257a736-4050-4d0a-8223-67097c731c0b.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=321cc06ce94954dce5b7565b88b22d56" alt="Statsig Webhook integration card with Enable button" width="444" height="305" data-path="images/integrations/event_webhook/162286552-c257a736-4050-4d0a-8223-67097c731c0b.png" />
</div>

If you are using a service that we don't have an official integration for, you can always use our Generic Webhook integration.

This integration just sends raw events to the provided webhook url.

### Setup

In your Project Settings, under the Integrations tab. Enable the Generic Webhook integration.

In the dialog that appears, enter the url of you destination webhook and then hit Enable to save the url and enable this integration.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/event_webhook/162327234-c9a683af-3c36-4da9-a66d-d16bf0ad09bc.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=a8a9a6fbb2dc77bba7275e956228830b" alt="integration-dialog" width="819" height="425" data-path="images/integrations/event_webhook/162327234-c9a683af-3c36-4da9-a66d-d16bf0ad09bc.png" />
</Frame>

You can then set which events you want forwarded to your webhook using the [Event Filtering](#filtering-events) dialog.

### Runtime event webhooks

These webhooks are triggered at runtime as users are being assigned to gates, experiments and are triggering events.

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

<a name="event-filtering-dialog" />

### Config Change webhooks

These webhooks are triggered by configuration changes taking place within Console. Each webhook request body will contain a batch of change events in the following format: `{"data": [<config-change>, <config-change>]}`. Batches may contain 1 or more config change events.

Below are a few examples of some of the config change payloads. To best capture the exhaustive types of config webhooks and their payloads, it's recommended to run a service such as ngrok or some other service that will help you log incoming webhooks.

#### Gate Change

```json  theme={null}
{
  "user": {
      "name": "Test User",
      "email": "testuser@email.com"
  },
  "timestamp": 1709660061095,
  "eventName": "statsig::config_change",
  "metadata": {
      "type": "Gate",
      "name": "layout_v2",
      "description": "Description: Change default page layout",
      "action": "created"
  }
}
```

#### Experiment Change

```json  theme={null}
{
  "user": {
      "name": "Test User",
      "email": "testuser@email.com"
  },
  "timestamp": 1709658507446,
  "eventName": "statsig::config_change",
  "metadata": {
      "type": "Experiment",
      "name": "heading_test",
      "description": "- Updated experiment settings\n    - Groups updated: control, test\n    - Parameters added: heading\n    - Parameters updated: directives",
      "action": "updated"
  }
}
```

### Filtering Events

Once you've enabled outbound events to your webhook, you can select which categories of Statsig events you want to export by clicking on the **Event Filtering** button and checking the appropriate boxes as shown below.
There are 2 main types of events: *Exposures* (e.g. events logged via the SDK) and *Config Changes* (changelogs for Statsig Console)

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/event_webhook/162329973-6f229186-1126-4824-9e29-1ff029f6553e.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=31bce36ef422f0b24d569339bfd1afb5" alt="event-filter-button" width="831" height="553" data-path="images/integrations/event_webhook/162329973-6f229186-1126-4824-9e29-1ff029f6553e.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/event_webhook/162329983-169703fc-c838-40a2-81dc-dd3c83886d00.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=52c02835d6b2c8f6270f21ed46911f7e" alt="event-filter-dialog" width="659" height="829" data-path="images/integrations/event_webhook/162329983-169703fc-c838-40a2-81dc-dd3c83886d00.png" />
</Frame>

### Webhook Signature

You can verify that a webhook request is coming from Statsig via our Webhook Signature.

Follow the following steps to verify the signature:

1. Grab your webhook signing secret from your Webhook integration card

<img width="738" alt="Webhook integration card showing signing secret" src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/event_webhook/209035738-bbbc0944-b428-4454-bf19-8845892c2044.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=a4b8d28949ed0d2179ee5695cbce1792" data-path="images/integrations/event_webhook/209035738-bbbc0944-b428-4454-bf19-8845892c2044.png" />

2. Extract the request time header 'X-Statsig-Request-Timestamp' from the webhook request.
3. Concatenate the version number ("v0"), the timestamp, and the request body together, using a colon (:) as a delimiter to create a signature basestring. Here's an example of a possible base string:

```
v0:1671672194836:{"data":[{"user":{"name":"Joe Zeng","email":"joe@statsig.com"},"timestamp":1671672134833,"eventName":"statsig::config_change","metadata":{"type":"Gate","name":"test","description":"- Updated Rule test rollout from 100.00% to 10.00%","environment":"production"}}]}
```

4. Hash the signature basestring, using the signing secret as a key, and take the hex digest of the hash. Create the full signature by prefixing the hex digest with the version number ("v0") and an equals sign. See sample pseudo code below.

```
statsig_signature = 'v0=' + hmac.compute_hash_sha256(
webhook_signing_secret,
signature_basestring
).hexdigest()
>>> 'v0=05c50d1513d49f884df8b0469befbbd432bd30364e81f16a606dec69f29e8f18'
```

5. Compare the resulting signature to the 'X-Statsig-Signature' header on the request

### Developing and Testing Webhooks

<Info>
  The actual event payload may look different than the examples above. <br />
  To test webhook configuration and see payloads before starting development, you can use a local HTTP tunnel (e.g. ngrok).
</Info>

You can also use the **Debug** tool to

1. See requests made to the webhook, including diagnostic information such as number of events forwarded/filtered, request header & body, and more.
2. Send example requests to the webhook using any recently logged event or exposure

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/hdTkQo7iTJfd4sfn/images/integrations/event_webhook/5e14e128-1fd4-46f9-8543-364f9b9819bb.png?fit=max&auto=format&n=hdTkQo7iTJfd4sfn&q=85&s=312ca1696bb7ef395f2d65555d5c7b90" alt="Debug Tool" width="780" height="910" data-path="images/integrations/event_webhook/5e14e128-1fd4-46f9-8543-364f9b9819bb.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).