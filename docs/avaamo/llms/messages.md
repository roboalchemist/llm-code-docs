# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/messages.md

# Messages

## Get agent messages

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/bots/analytics/{{agent_id}}/messages.json`

Gets a list of messages from the agent within a specified period of time.&#x20;

#### Path Parameters

<table><thead><tr><th width="203">Name</th><th width="112">Type</th><th>Description</th></tr></thead><tbody><tr><td>agent_id<mark style="color:red;">*</mark></td><td>integer</td><td>Agent identifier. You can get the agent identifier from the agent URL. </td></tr></tbody></table>

#### Query Parameters

<table><thead><tr><th width="209">Name</th><th width="108">Type</th><th>Description</th></tr></thead><tbody><tr><td>per_page</td><td>number</td><td>The number of entries fetched per page. <br>Default value: 25<br>Maximum value: 100</td></tr><tr><td>page</td><td>number</td><td>Page from which the entries must be fetched. <br>Default value: 1</td></tr><tr><td>from_timetoken</td><td>number</td><td><p>Timestamp from which the records are fetched.</p><p></p><p>Default value is last three days from the specified to_timetoken value. </p><p></p><p>Specify UNIX Epoch Timestamp.</p></td></tr><tr><td>to_timetoken</td><td>number</td><td><p>Timestamp until which the records are fetched. </p><p></p><p>Default is the current timestamp. </p><p></p><p>Specify UNIX Epoch Timestamp.</p></td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="208">Name</th><th width="111">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td><p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr></tbody></table>

{% tabs %}
{% tab title="200 Successful request" %}

```json
{
    "current_page": 1,
    "per_page": 1,
    "total_entries": 8,
    "total_pages": 8,
    "time_token": 1716811116.983583,
    "entries": [
        {
            "message_uuid": "e00a9d28-xxxx-4350-xxxx-389c395afec5",
            "score": 1.0,
            "content": "",
            "intent_type": "JS::INTENT",
            "channel_name": "web",
            "created_at": 1716811065.0,
            "user": {
                "first_name": "David",
                "layer_id": "06c7beb3-9bf8-xxxx-xxxx-745e5431053d"
            },
            "intent_name": "custom code"
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
curl --location --request GET 'https://cx.avaamo.com/bots/analytics/20xxx/messages.json' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/bots/analytics/20xxx/messages.json',
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

<table><thead><tr><th width="147.8396361895644">Attribute</th><th width="485.7423460867629">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td>entries</td><td><p>Indicates an array of user sessions fetched from the agent. The number of entries in the array = Number specified in the per_page parameter. Each array contains the following details of each user session: </p><ul><li>message_uuid: Unique message identifier.</li><li>content: Content of the message.</li><li>intent_type: Type of intent such as system, inline, KnowledgePack</li><li>channel_name: Channel of communication</li><li>created_at: Timestamp at which the message was created in seconds. This is in Unix epoch timestamp format. </li><li>first_name: If the user information is collected, then <code>first_name</code> indicates the first name of the user corresponding to the message, or else it is displayed as "You". See <a href="../../../../how-to/build-agents/configure-agents/deploy/web-channel/widget-configuration#collect-user-information">Collect user information</a>, for more details.</li><li>layer_id: Unique identifier for each user.</li><li>intent_name: Name of the intent corresponding to the message.</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="150">Use-case</th><th width="610.4285714285713">Query Parameter</th></tr></thead><tbody><tr><td>Get agent messages in a specified period of time</td><td><p><strong>from_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/messages.json?from_date=01/04/2020&#x26;to_date=06/04/2020&#x26;utc_offset=&#x3C;&#x3C;utc-offset-sec</code></p></td></tr></tbody></table>
