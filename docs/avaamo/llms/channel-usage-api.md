# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/channel-usage-api.md

# Channel usage

## Get channel usage

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/bots/analytics/{{agent_id}}/channel_usage.json`

Gets the count of user interactions from the different channels the agent is deployed on.

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name        | Type   | Description                                                                                                                                                                                                          |
| ----------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| utc\_offset | number | <p>The difference in seconds from Coordinated Universal Time (UTC) for a particular place and date. </p><p></p><p>The default value is 0 implying that there is no offset from Coordinated Universal Time (UTC).</p> |
| from\_date  | string | <p>Date from which the required details are retrieved. </p><p></p><p>Default value is the last three days from the to\_date. Specify date in dd/mm/yyyy format.</p>                                                  |
| to\_date    | string | <p>Date to which the required details are retrieved. </p><p></p><p>The default value is the current date. Specify date in dd/mm/yyyy format.</p>                                                                     |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | string | <p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200 Successful request" %}

```javascript
{
  "channel_usage": [
    {
      "type": "web",
      "channel": "web",
      "count": 35565
    },
    {
      "type": "whatsapp"
      "channel": "whatsApp_Disha_3",
      "count": 27058
    }
  ]
}
```

{% endtab %}

{% tab title="422: Unprocessable Entity Unprocessable entity -> to\_date is before from\_date" %}

```javascript
{
    "error": "To Date cannot be before From Date"
}
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Note**: For optimal API performance, the recommended time duration for fetching data from any of the REST APIs that support a date range or time period is 7 days.
{% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/bots/analytics/20xxx/channel_usage.json?utc_offset=19800' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/bots/analytics/20xxx/channel_usage.json?utc_offset=19800',
  'headers': {
    'Content-Type': 'application/json',
    'Access-Token': 'xxxxxx8d9952499ea466fc007dxxxxxx'
  }
};
request(options, function (error, response) { 
  if (error) throw new Error(error);
  console.log(response.body);
});

```

{% endtab %}
{% endtabs %}

### Response attributes:

In the response, the user\_feedbacks array is returned with a count of positive and negative feedback:

<table><thead><tr><th>Attribute</th><th width="308.3333333333333">Description</th><th width="247.20000000000002">Type</th></tr></thead><tbody><tr><td>channel_usage</td><td><p>Indicates an array of channels and channel usage. Each array contains the following details about the intents: </p><ul><li>type: Indicates the channel type.</li><li>channel: Indicates the channel name.</li><li>count: Indicates the count of user interactions from the channels.</li></ul></td><td><p>An array of </p><p>JSON key-value pairs</p></td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="150">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get overall list of channel usage </td><td><code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/channel_usage.json?utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></td></tr><tr><td>Get channel usage within a specified period</td><td><p><strong>from_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/channel_usage.json?from_date=01/04/2020&#x26;to_date=06/04/2020&#x26;utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></p></td></tr></tbody></table>
