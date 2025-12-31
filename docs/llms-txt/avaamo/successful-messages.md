# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/successful-messages.md

# Successful messages

## Get successful messages

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/bots/analytics/{{agent_id}}/successful_responses.json`

Gets a list of successful message responses that are triggered in the conversation flow. In the response, for each of the successful message responses, you can learn about the user query, created time, message identifier, and the details of the user who posted the query.  Note that disambiguations are also available in the response

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name            | Type    | Description                                                                                                                                                                                                                                     |
| --------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page            | integer | <p>Page from which the entries must be fetched. <br>Default: 1</p>                                                                                                                                                                              |
| per\_page       | integer | <p>The number of entries fetched per page. <br>Default: 25<br>Maximum value: 100</p>                                                                                                                                                            |
| from\_timetoken | Number  | <p>Timestamp from which the records are fetched.</p><p>If you specify from\_timetoken and not to\_timetoken, then the latest 5 entries upto the specified timetoken are fetched.</p><p></p><p>Specify UNIX Epoch Timestamp in microseconds.</p> |
| to\_timetoken   | Number  | <p>Timestamp until which the records are fetched. Default is the current timestamp. </p><p></p><p>Specify UNIX Epoch Timestamp in microseconds.</p>                                                                                             |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-Token<mark style="color:red;">\*</mark> | string | <p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200 Successful request" %}

```javascript
{
  "current_page": 1,
  "per_page": 1,
  "total_entries": 42,
  "total_pages": 42,
  "time_token": 1589536852.4691367,
  "entries": [
    {
      "message_uuid": "ebd118af-025e-4a07-b2df-2a883d53ee31",
      "score": 1,
      "content": "where is your store?",
      "intent_type": "KNOWLEDGEPACK::INTENT",
      "channel_name": "web",
      "created_at": 1589451824,
      "user": {
        "first_name": 30572
      },
      "intent_name": "store"
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
curl --location --request GET 'https://cx.avaamo.coms/bots/analytics/20xxx/successful_responses.json?page=2&per_page=55' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/bots/analytics/20xxx/successful_responses.json?page=2&per_page=55',
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

<table><thead><tr><th width="155.855986119144" align="center">Attribute</th><th width="339.134458809146">Description</th><th>Type</th></tr></thead><tbody><tr><td align="center">current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td align="center">per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td align="center">total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td align="center">total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td align="center">time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td align="center">entries</td><td><p>Indicates an array of successful messages fetched from the agent. Number of entries in the array = Number specified in per_page parameter. In each successful message, the following details are returned: </p><ul><li>message_uuid: Unique identifier of the message.</li><li>content: User query for which agent gave a successful response.</li><li>channel_name: Channel used by the user to communicate with the agent.</li><li>created_at: Timestamp of message creation.</li><li>user: User who interacted with the agent.</li><li>intent_name: Name of intent that gave a response to the user.</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="252.51415323672637">Use-case</th><th width="436.0499197717953">Query Parameter</th></tr></thead><tbody><tr><td>Get successful messages from agent using pagination</td><td><p><strong>page</strong>: Specify the page from which you wish to fetch records. </p><p><strong>per_page</strong>: Specify the number of entries per page. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/successful_responses.json?page=&#x3C;&#x3C;no_of_pages>>&#x26;per_page=&#x3C;&#x3C;per_page_messages>></code> </p></td></tr><tr><td>Get successful messages from agent within a specified period.</td><td><p><strong>from_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/successful_responses.json?from_date=01/04/2020&#x26;to_date=06/04/2020&#x26;utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></p></td></tr></tbody></table>
