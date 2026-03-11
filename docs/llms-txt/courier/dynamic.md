# Source: https://www.courier.com/docs/platform/automations/dynamic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Accessing Dynamic Data

> Courier Automations support dynamic data access using the refs object (e.g., refs.data.userId). You can remap nested values for cleaner templates and personalize notifications using mapped variables.

The `refs` object has access to the following properties:

* `brand`
  * type: string
  * description: A unique identifier that represents the brand that should be used for rendering the notification.
* `data`
  * type: object
  * description: An object that includes any data you want to pass to a message template or accessor type. The data will populate the corresponding template variables.
* `profile`
  * type: object
  * description: an object that includes any key-value pairs required by your chosen Integrations (see our Provider Documentation for the requirements for each Integration.) If profile information is included in the request and that information already exists in the profile for the recipientId, that information will be merged.
* `template`
  * type: string
  * description: A unique identifier that can be mapped to an individual Notification. This could be the "Notification ID” on Notification detail pages (see the Notifications page in the Courier app) or a custom string mapped to the event in settings.
* `recipient`
  * type: string
  * description: A unique identifier associated with the recipient of the delivered message, which can optionally map to a Courier managed profile.

These properties can all be set using the `invoke` api. Additionally, the data property can be initialized by triggers
such as Segment, or modified by actions such as `Fetch Data`.

For example, you can access the `userId` supplied by segment in a send node using `refs.data.userId`

<Frame caption="Accessing userId dynamically using refs.data.userId within the send node">
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/new-refs-example.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=e54f8f9a03a68ffe251bd6fe5ea512ae" alt="Accessing userId dynamically using refs.data.userId within the send node" width="2522" height="1246" data-path="assets/platform/automations/new-refs-example.png" />
</Frame>

## Mapping Dynamic Data to Variables

By default, all `data` passed into an automation is passed through to the notification template in a send call. However, there are cases where you want to map specific data attributes to different variables.

1. Open a send node, click on the advanced section, and then click edit next to the `Data` field

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/new-send_data.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=4839a7627131b4f9b8f8f9c91d786032" alt="Editing Send Node Data" width="2492" height="1272" data-path="assets/platform/automations/new-send_data.png" />
</Frame>

2. You can either use the interactive JSON editor, or just modify the JSON in the text editor directly. The syntax to map the attribute is as follows:

```json  theme={null}
  "<new_attribute>": {
    "$ref": "data.<some_attribute>"
  }
```

### Example: Mapping Dynamic Data to a Variable

Let's say we have a segment event as a trigger for our automation. The event has a `vendor_name` attribute in the segment `properties` object and we want to map that to a `vendor` attribute in our send call.

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/segment_sample_data.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=02deee15896ea3aac7893d5eadd618b2" alt="Segment Sample Data" width="768" height="660" data-path="assets/platform/automations/segment_sample_data.png" />
</Frame>

We would use the following syntax:

```json  theme={null}
  "vendor": {
    "$ref": "data.properties.vendor_name"
  }
```

<Frame>
  <img src="https://mintcdn.com/courier-4f1f25dc/WNdu5qn7yJu4418-/assets/platform/automations/new-send_dynamic_data_map.png?fit=max&auto=format&n=WNdu5qn7yJu4418-&q=85&s=583e205a4ba4fb3c57f763f7bd8b02bc" alt="Dynamic Data Mapping" width="2520" height="1292" data-path="assets/platform/automations/new-send_dynamic_data_map.png" />
</Frame>

In the notification template, you are now able to access the `vendor` property directly in a template variable `{vendor}` rather than destructing the data object `{data.properties.vendor_name}`

## URL Interpolation

You can use dynamic data to construct URLs by interpolating values directly into the URL string. This is particularly useful for Fetch Data steps where you need to make API calls with dynamic parameters.

Wrap the entire URL with template literal syntax using `${`...`}` and use `${refs.data.variableName}` to substitute values within the URL string.

### Basic URL Interpolation

```json  theme={null}
{
  "type": "fetch",
  "url": "${`https://api.courier.com/profiles/${refs.data.userID}`}",
  "method": "get"
}
```

### Advanced URL Interpolation Examples

**User-specific API calls:**

```json  theme={null}
{
  "type": "fetch",
  "url": "${`https://api.example.com/users/${refs.data.userId}/orders/${refs.data.orderId}`}",
  "method": "get"
}
```

**Profile-based endpoints:**

```json  theme={null}
{
  "type": "fetch",
  "url": "${`https://api.example.com/accounts/${refs.profile.accountId}/settings`}",
  "method": "get"
}
```

**Query parameters with interpolation:**

```json  theme={null}
{
  "type": "fetch",
  "url": "${`https://api.example.com/search?q=${refs.data.searchTerm}&limit=${refs.data.limit}`}",
  "method": "get"
}
```

**Nested data access:**

```json  theme={null}
{
  "type": "fetch",
  "url": "${`https://api.example.com/events/${refs.data.event.id}/attendees`}",
  "method": "get"
}
```

### URL Interpolation with Authentication

Combine URL interpolation with authentication headers:

```json  theme={null}
{
  "type": "fetch",
  "url": "${`https://api.example.com/users/${refs.data.userId}/profile`}",
  "method": "get",
  "headers": {
    "Authorization": "Bearer ${refs.data.accessToken}",
    "X-User-ID": "${refs.data.userId}"
  }
}
```

<Note>
  **URL Encoding**: Courier automatically handles URL encoding for interpolated values. Special characters in your data will be properly encoded in the final URL.
</Note>

## Reserved Field values

The following field values are reserved for current and future interpolation features. They can
not be used literally in an input field.

* `refs`
* `data`
* `profile`
