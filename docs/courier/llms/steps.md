# Source: https://www.courier.com/docs/platform/automations/steps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Ad hoc Automation Steps

> Courier’s ad hoc automation steps let you define workflows via API in a single request—supporting batching, delays, fetches, notifications, profile updates, cancellations, and invokes—without a saved template.

Ad hoc automations let you define workflows in a single API request without a saved template. Each step has an `action` field that specifies its type.

<Note>
  For visual designer documentation, see [Batching](/platform/automations/batching), [Digests](/platform/automations/digest), [Throttle](/platform/automations/throttle), and [Control Flow](/platform/automations/control-flow).
</Note>

## Add to Batch

Add the data object to a batch. Steps after "add-to-batch" are not executed until the batch conditions are met and released. Subsequent steps are invoked only once per batch run.

### Fields

| Field             | Type   | Required | Description                                                                                                                                                                                                                                                    |
| ----------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| action            | string | required | The type of element. For the add to batch Automation Step, this value should be `"add-to-batch"`.                                                                                                                                                              |
| batch\_key        | string | required | A unique id for the batch. This value must be the same for each event expected to be added to the batch                                                                                                                                                        |
| wait\_period      | string | required | Defines the period of inactivity before the batch is released. Specified as an ISO 8601 duration, [https://en.wikipedia.org/wiki/ISO\_8601#Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations)                                                        |
| max\_wait\_period | string | required | Defines the maximum wait time before the batch should be released. Must be less than wait period. Maximum of 60 days. Specified as an ISO 8601 duration, [https://en.wikipedia.org/wiki/ISO\_8601#Durations](https://en.wikipedia.org/wiki/ISO_8601#Durations) |
| max\_items        | number |          | If specified, the batch will release as soon as this number is reached                                                                                                                                                                                         |
| retain            | object | required | Defines what items should be retained and passed along to the next steps when the batch is released                                                                                                                                                            |
| retain.type       | string | required | One of `first`, `last`, `highest`, `lowest`.                                                                                                                                                                                                                   |
| retain.count      | number | required | Currently, only 10 is supported                                                                                                                                                                                                                                |
| retain.sort\_key  | string |          | Defines the data value `data[sort_key]` that is used to sort the stored items. Required when type is set to `highest` or `lowest`.                                                                                                                             |
| category\_key     | string |          | Defines the field of the data object the batch is set to when complete. Defaults to `batch`                                                                                                                                                                    |

### Schema

```json  theme={null}
{
  "action": "add-to-batch",
  "wait_period": "",
  "max_wait_period": "",
  "max_items": 10,
  "retain": {
    "type": "first" | "last" | "highest" | "lowest",
    "count": 10,
    "sort_key": ""
  },
  "category_key": ""
}
```

### Overriding Batches In Flight

When making a batch call, you can make changes to the batching settings to a batching automation mid-flight.

**Retain Settings**

Users can initially set the `retain` parameters when invoking a batch for the first time and make changes to the `retain.count` on subsequent calls. The automation batch will be overwritten with the new retention policy. For example, if you send a batch to retain the first 10 items, and then edit the automation to retain the first 20, the batch will not release until the first 20 are retained while it's less than the `max_items` parameter.

**Send Step**

Send steps cannot be overwritten mid-flight in a batch. The first send step method introduced in the batch will run before the overwritten one takes place.

## Cancel

Cancel an Automation Run that is In Progress.

### Fields

| Field              | Type   | Required | Description                                                                                                                                                |
| ------------------ | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| action             | string | required | The type of element. For the Cancel Automation Step, this value should be `"cancel"`.                                                                      |
| cancelation\_token | string |          | The string that is associated with the cancelable automation run. An Automation Run is cancelable if it has a `cancelation_token` value at execution time. |
| if                 | string |          | A boolean expression whose value is used to determine the execution of the step. Can optionally consume step reference data.                               |
| ref                | string |          | A pointer to step and its data.                                                                                                                            |

### Schema

```json  theme={null}
{
  "action": "cancel",
  "cancelation_token": "",
  "if": "",
  "ref": ""
}
```

## Delay

Wait a duration of time, before proceeding to the next Automation Step.

### Fields

| Field    | Type   | Required | Description                                                                                                                  |
| -------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| action   | string | required | The type of element. For the Delay Automation Step, this value should be `"delay"`.                                          |
| duration | string |          | The human readable time duration. A duration value and unit is required, e.g. 5 minutes, 1 hour, 3 days                      |
| if       | string |          | A boolean expression whose value is used to determine the execution of the step. Can optionally consume step reference data. |
| ref      | string |          | A pointer to step and its data.                                                                                              |
| until    | string |          | The ISO 8601 timestamp that describes the length of the delay.                                                               |

Either `until` or `duration` is required.

### Schema

```json  theme={null}
{
  "action": "delay",
  "if": "",
  "ref": "",
  "until": "",
  "duration": ""
}
```

## Fetch Data

Fetch data via https and write the response to the `data` property of the Automation Run Cache.

### Fields

| Field               | Type   | Required | Description                                                                                                                                                                                               |
| ------------------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| action              | string | required | The type of element. For the Fetch Data Automation Step, this value should be `"fetch-data"`.                                                                                                             |
| idempotency\_expiry | string |          | A unix epoch timestamp (seconds) or an ISO\_8601 date string that describes how long the idempotency\_key is valid.                                                                                       |
| idempotency\_key    | string |          | A unique value generated by the client which the server uses to recognize subsequent retries of the same request.                                                                                         |
| if                  | string |          | A boolean expression whose value is used to determine the execution of the step. Can optionally consume step reference data.                                                                              |
| merge\_strategy     | enum   |          | `replace`, `soft-merge`, `overwrite`, or `none`. If nothing is specified then the default strategy is `replace`. The strategy to merge the webhook response into the Automation Run Cache. Details below. |
| ref                 | string |          | A pointer to step and its data.                                                                                                                                                                           |
| webhook             | object |          | The webhook configuration of the resource that is accessible via http. See the `webhook` schema bellow.                                                                                                   |

The `merge_strategy` property can be any of the following values:

* `replace`
  * overwrite all properties in the Automation Cache with the http response. Removes all properties in the Automation Cache that do not exist in the http response.
* `soft-merge`
  * only overwrite properties in the Automation Cache with the http response properties that do not yet exist in the Automation Cache.
* `overwrite`
  * overwrite all properties in the Automation Cache with the properties from the http response.
* `none`
  * do not make any changes to the Automation Cache if the Automation Cache already exists and has data. Otherwise initialize the Automation Cache.

The `webhook` can be configured with any of the following properties:

```json  theme={null}
{
  "webhook": {
    "body": {}, // optional
    "headers": {}, // optional
    "params": {}, // optional
    "method": "GET" | "POST", // optional, default GET
    "url": "<API_RESOURCE>"
  }
}
```

### Schema

```json  theme={null}
{
  "action": "fetch-data",
  "idempotency_expiry": "",
  "idempotency_key": "",
  "if": "",
  "merge_strategy": "replace" | "none" | "overwrite" | "soft-merge",
  "ref": "",
  "webhook": {
    "body": {}, // optional
    "headers": {}, // optional
    "params": {}, // optional
    "method": "GET" | "POST", // optional, default GET
    "url": "<API_RESOURCE>"
  }
}
```

## GET Profile

Bring a profile stored with Courier into scope. See [GET Profile](/platform/automations/get-profile) for usage details.

### Fields

| Field           | Type   | Required | Description                                                                                                                  |
| --------------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| action          | string | required | The type of element. For the GET Profile step, this value should be `"get-profile"`.                                         |
| user\_id        | string | required | The user id of the profile to load                                                                                           |
| path            | string |          | Where the profile should be attached. Can be `profile` or `data.<field-name>`. Defaults to `profile`.                        |
| merge\_strategy | string |          | How to merge the profile with existing context data. `"replace"`, `"none"`, `"overwrite"`, or `"soft-merge"` (default).      |
| tenant\_id      | string |          | Load profile with tenant-specific data                                                                                       |
| if              | string |          | A boolean expression whose value is used to determine the execution of the step. Can optionally consume step reference data. |
| ref             | string |          | A pointer to step and its data.                                                                                              |

### Schema

```json  theme={null}
{
  "action": "get-profile",
  "user_id": "",
  "path": "profile",
  "merge_strategy": "soft-merge",
  "if": "",
  "ref": ""
}
```

## Invoke

Invoke another Automation Template

### Fields

| Field    | Type   | Required | Description                                                                                                                                         |
| -------- | ------ | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| action   | string | required | The type of element. For the Invoke Automation Step, this value should be `"invoke"`.                                                               |
| context  | string |          | The initial values of the Automation Run Cache to invoke the Automation Template with.                                                              |
| if       | string |          | A boolean expression whose value is used to determine the execution of the step. Can optionally consume step reference data.                        |
| ref      | string |          | A pointer to step and its data.                                                                                                                     |
| template | string | required | A unique identifier that can be mapped to an Automation Template. This could be the Template ID or the Alias from the Automation Template Designer. |

### Schema

```json  theme={null}
{
  "action": "invoke",
  "context": {
    "brand": "",
    "data": {},
    "profile": {},
    "template": "",
    "recipient": ""
  },
  "if": "",
  "ref": "",
  "template": ""
}
```

## Send (Legacy)

Send a Notification Template

### Fields

| Field               | Type   | Required | Description                                                                                                                                                                                                                                                                                                             |
| ------------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| action              | string | required | The type of element. For the Send Automation Step, this value should be `"send"`.                                                                                                                                                                                                                                       |
| recipient           | string | required | A unique identifier associated with the recipient of the delivered message.                                                                                                                                                                                                                                             |
| template            | string | required | A unique identifier that can be mapped to an individual Notification. This could be the "Notification ID” on Notification detail pages (see the Notifications page in the Courier app) or a custom string mapped to the event in settings.                                                                              |
| brand               | string |          | The brand id to be used in the notification.                                                                                                                                                                                                                                                                            |
| data                | string |          | An object that includes any data you want to pass to a message template. The data will populate the corresponding template variables.                                                                                                                                                                                   |
| if                  | string |          | A boolean expression whose value is used to determine the execution of the step. Can optionally consume step reference data.                                                                                                                                                                                            |
| idempotency\_expiry | string |          | A unix epoch timestamp (seconds) or an ISO\_8601 date string that describes how long the idempotency\_key is valid.                                                                                                                                                                                                     |
| idempotency\_key    | string |          | A unique value generated by the client which the server uses to recognize subsequent retries of the same request.                                                                                                                                                                                                       |
| override            | string |          | An object that is merged into the request sent by Courier to the provider to override properties or to gain access to features in the provider API that are not natively supported by Courier.                                                                                                                          |
| profile             | string |          | An object that includes any key-value pairs required by your chosen Integrations (see our Provider Documentation for the requirements for each Integration.) If profile information is included in the request and that information already exists in the profile for the recipientId, that information will be merged. |
| ref                 | string |          | A pointer to step and its data.                                                                                                                                                                                                                                                                                         |

### Schema

```json  theme={null}
{
  "action": "send",
  "brand": "",
  "data": {},
  "if": "",
  "idempotency_expiry": "",
  "idempotency_key": "",
  "override": {},
  "profile": {},
  "recipient": "",
  "ref": ""
}
```

## Send

Send a Notification Template

### Fields

| Field   | Type   | Required | Description                                                                                                                         |
| ------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| action  | string | required | The type of element. For the Send Automation Step, this value should be `"send"`.                                                   |
| message | object | required | The Courier Message. For more information see [The Courier Message](/api-reference/send/send-a-message) in the /send API reference. |

### Schema

```json  theme={null}
{
  "action": "send",
  "message": {
    "to": {
      // profile
    },
    // either template or content is required but not both
    "template": "",
    "content": {}
  }
}
```

## Send List

Send a message to each recipient in the list. Optionally fetch data for each recipient via http and merge the response into the `data` property of the Automation Run Cache.

### Fields

| Field               | Type   | Required | Description                                                                                                                                                                                                                                |
| ------------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| action              | string | required | The type of element. For the Send List Automation Step, this value should be `"send-list"`.                                                                                                                                                |
| brand               | string |          | The brand id to be used in the notification.                                                                                                                                                                                               |
| data                | string |          | An object that includes any data you want to pass to a message template. The data will populate the corresponding template variables.                                                                                                      |
| data\_source        | object |          | The webhook configuration of the resource that is accessible via http. See the `data_source` schema bellow.                                                                                                                                |
| idempotency\_expiry | string |          | A unix epoch timestamp (seconds) or an ISO\_8601 date string that describes how long the idempotency\_key is valid.                                                                                                                        |
| idempotency\_key    | string |          | A unique value generated by the client which the server uses to recognize subsequent retries of the same request.                                                                                                                          |
| if                  | string |          | A boolean expression whose value is used to determine the execution of the step. Can optionally consume step reference data.                                                                                                               |
| list                | string | required | The Courier List Id.                                                                                                                                                                                                                       |
| override            | string |          | An object sent by Courier to the provider to leverage features of the provider API or to simply override properties of the provider api call.                                                                                              |
| template            | string | required | A unique identifier that can be mapped to an individual Notification. This could be the "Notification ID” on Notification detail pages (see the Notifications page in the Courier app) or a custom string mapped to the event in settings. |
| ref                 | string |          | A pointer to step and its data.                                                                                                                                                                                                            |

The `merge_strategy` property of the steps `data_source` object, can be any of the following values:

* `replace`
  * overwrite all properties in the Automation Cache with the http response. Removes all properties in the Automation Cache that do not exist in the http response.
* `soft-merge`
  * only overwrite properties in the Automation Cache with the http response properties that do not yet exist in the Automation Cache.
* `overwrite`
  * overwrite all properties in the Automation Cache with the properties from the http response.
* `none`
  * do not make any changes to the Automation Cache if the Automation Cache already exists and has data. Otherwise initialize the Automation Cache.

The `webhook` property of the steps `data_source` object, can be configured with any of the following properties:

```json  theme={null}
{
  "webhook": {
    "body": {}, // optional
    "headers": {}, // optional
    "params": {}, // optional
    "method": "GET" | "POST", // optional, default GET
    "url": "<API_RESOURCE>"
  }
}
```

### Schema

```json  theme={null}
{
  "action": "send-list",
  "brand": "",
  "data": {},
  "data_source": {
    "webhook": {
      "url": "WEBHOOK_URL",
      "method": "GET",
      "headers": {}
    },
    "merge_strategy": "replace"
  },
  "idempotency_expiry": "",
  "idempotency_key": "",
  "if": "",
  "list": "",
  "override": {},
  "ref": "",
  "template": ""
}
```

## Update Profile

Update the Courier Profile given a recipientId.

### Fields

| Field         | Type   | Required | Description                                                                                                                                                                                |
| ------------- | ------ | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| action        | string | required | The type of element. For the Update Profile Automation Step, this value should be `"update-profile"`.                                                                                      |
| if            | string |          | A boolean expression whose value is used to determine the execution of the step. Can optionally consume step reference data.                                                               |
| merge         | enum   |          | `replace`, `soft-merge`, `overwrite`, or `none`. If nothing is specified then the default strategy is `replace`. The strategy to merge new data into the recipient profile. Details below. |
| profile       | string |          | An object that includes any key-value pairs associated with the recipient profile                                                                                                          |
| recipient\_id | string |          | A unique identifier associated with the recipient profile you intend to update.                                                                                                            |
| ref           | string |          | A pointer to step and its data.                                                                                                                                                            |

The `merge` property can be any of the following values:

* `replace`
  * overwrite all properties in the recipient profile with the http response. Removes all properties in the recipient profile that do not exist in the http response.
* `soft-merge`
  * only overwrite properties in the recipient profile with the http response properties that do not yet exist in the recipient profile.
* `overwrite`
  * overwrite all properties in the recipient profile with the properties from the http response.
* `none`
  * do not make any changes to the recipient profile if the recipient profile already exists and has data. Otherwise initialize the recipient profile

<Warning>
  **Profile Merging**: When using update-profile steps, be mindful with the aforementioned merge strategies that can update an existing profile that was [created with a Segment Identify event](/external-integrations/cdp/segment#identify-calls).
</Warning>

### Schema

```json  theme={null}
{
  "action": "update-profile",
  "if": "",
  "merge": "replace",
  "profile": {},
  "recipient_id": "",
  "ref": ""
}
```

## Subscribe

Subscribe a user to a Courier List.

### Fields

| Field         | Type   | Required | Description                                                                                                                  |
| ------------- | ------ | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| action        | string | required | The type of element. For the Subscribe Automation Step, this value should be `"subscribe"`.                                  |
| list\_id      | string | required | The ID of the Courier List to subscribe the user to.                                                                         |
| recipient\_id | string | required | The user ID of the recipient to subscribe.                                                                                   |
| subscription  | object |          | Optional subscription options including preferences.                                                                         |
| if            | string |          | A boolean expression whose value is used to determine the execution of the step. Can optionally consume step reference data. |
| ref           | string |          | A pointer to step and its data.                                                                                              |

### Schema

```json  theme={null}
{
  "action": "subscribe",
  "list_id": "my-list-id",
  "recipient_id": "user-123",
  "subscription": {
    "preferences": {}
  },
  "if": "",
  "ref": ""
}
```
