# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/unhandled-messages.md

# Unhandled messages

## Get unhandled messages

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/bots/analytics/{{agent_id}}/unhandled_messages.json`

Gets a list of unhandled responses that are triggered in the conversation flow. In the response, for each of the unhandled message responses, you can learn about the user query, created time, message identifier, and the details of the user who posted the query.&#x20;

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name            | Type    | Description                                                                                                                                                                            |
| --------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page            | integer | <p>Page from which the entries must be fetched. <br>Default: 1</p>                                                                                                                     |
| per\_page       | integer | <p>Number of entries fetched per page. <br>Default: 25<br>Maximum value: 100</p>                                                                                                       |
| from\_timetoken | number  | <p>Timestamp from which the records are fetched.</p><p></p><p>Default value is last three days from the specified to\_timetoken value. </p><p></p><p>Specify UNIX Epoch Timestamp.</p> |
| to\_timetoken   | number  | <p>Timestamp until which the records are fetched. Default is the current timestamp. </p><p></p><p>Specify UNIX Epoch Timestamp.</p>                                                    |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | string | <p>User access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200 Successful request" %}

```javascript
{
  "current_page": 1,
  "per_page": 1,
  "total_entries": 3038,
  "total_pages": 3038,
  "time_token": 1588842292.4734528,
  "entries": [
    {
      "message_uuid": "f80145f9-6a1f-4494-92a0-1f13f188d469",
      "score": 0,
      "content": "Tel me about your product ",
      "intent_type": "UNHANDLED::INTENT",
      "channel_name": "web",
      "created_at": 1588575626,
      "user": {
        "first_name": 9374364
      },
      "intent_name": "Unhandled"
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
curl --location --request GET 'https://cx.avaamo.com/bots/analytics/20xxx/unhandled_messages.json?page=2&per_page=55' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/bots/analytics/20xxx/unhandled_messages.json?page=2&per_page=55',
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

### Response attributes

In the response, the following attributes are returned:

<table><thead><tr><th width="172.34399183981196">Attribute</th><th width="315.3812709365702">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td>entries</td><td><p>Indicates an array of unhandled messages fetched from the agent. Number of entries in the array = Number specified in per_page parameter. In each unhandled message, the following details are returned: </p><ul><li>message_uuid: Unique identifier of the message.</li><li>content: User query for which agent gave the unhandled response.</li><li>channel_name: Channel used by the user to communicate with the agent.</li><li>created_at: Timestamp of message creation.</li><li>user: User who interacted with the agent.</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="221.7208277434376">Use-case</th><th width="456.36715000561543">Query Parameter</th></tr></thead><tbody><tr><td>Get unhandled messages from agent using pagination</td><td><p><strong>page</strong>: Specify the page from which you wish to fetch records. </p><p><strong>per_page</strong>: Specify the number of entries per page. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/unhandled_messages.json?page=5&#x26;per_page=2</code> </p></td></tr><tr><td>Get unhandled messages from agent within a specified period.</td><td><p><strong>from_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/unhandled_messages.json?from_date=01/04/2020&#x26;to_date=06/04/2020&#x26;utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></p></td></tr></tbody></table>
