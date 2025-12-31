# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/unhandled-queries.md

# Unhandled queries

## Get unhandled queries

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}/unhandled_queries.json`

Get a list of all the unhandled queries from the agent. This does also includes queries that led to disambiguation responses.

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name        | Type    | Description                                                                                                       |
| ----------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| start\_time | number  | Timestamp from which the records are fetched. Default is from the beginning. Specify in UNIX Epoch Timestamp.     |
| end\_time   | number  | Timestamp until which the records are fetched. Default is the current timestamp. Specify in UNIX Epoch Timestamp. |
| page        | integer | <p>Page from which the entries must be fetched. <br>Default: 1</p>                                                |
| per\_page   | integer | <p>Number of entries fetched per page. <br>Default: 25<br>Maximum value: 100</p>                                  |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | string | <p>User access token. You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "current_page": 1,
    "per_page": 25,
    "total_entries": 2,
    "total_pages": 1,
    "time_token": 1590580099.9726138,
    "queries": [
        {
            "id": 943994,
            "user_query": "I want to order coke",
            "corrected_query": "I want to order coke",
            "node_key": "1",
            "intent_type": "Unhandled",
            "detected_language": "en",
            "created_at": 1590569762.0
        },
        {
            "id": 943989,
            "user_query": "I want to order pizza",
            "corrected_query": "I want to order pizza",
            "node_key": "1",
            "intent_type": "Unhandled",
            "detected_language": "en",
            "created_at": 1590569723.0
        }
    ]
}
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Note**: For optimal API performance, the recommended time duration for fetching data from any of the REST APIs that support a date range or time period is 7 days.&#x20;
{% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/api/v1/agents/20xxx/unhandled_queries.json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v1/agents/20xxx/unhandled_queries.json',
  'headers': {
    'Access-Token': 'xxxxxx8d9952499ea466fc007dxxxxxx',
    'Content-Type': 'application/json'
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

<table><thead><tr><th width="181.30798479087454">Attribute</th><th width="301.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of intent entries in the response.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td>queries</td><td><p>Indicates an array of queries that led to unhandled or disambiguation response. Each entry contains the following details: </p><ul><li>id: Internal identifier used by the Platform.</li><li>user_query: Actual user query</li><li>corrected_query: Query corrected by the Platform</li><li>node_key: Node in the conversational flow at which the query led to unhandled or disambiguation response.</li><li>intent_type: Type of intent, Unhandled, or Disambiguation</li><li>detected_language: Language detected while analyzing the user’s query.</li><li>created_at: Indicates the timestamp of when this entry was created in seconds. (UNIX Epoch Timestamp)</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="243.04859028194363">Use-case</th><th width="564.4285714285713">Query Parameter</th></tr></thead><tbody><tr><td>Get unhandled queries from the agent using pagination</td><td><p><strong>page</strong>: Specify the page from which you wish to fetch records. </p><p><strong>per_page</strong>: Specify the number of entries per page. </p><p></p><p><strong>Example</strong>: </p><p><code>https://cx.avaamo.com/api/v1/agents/&#x3C;&#x3C;agent_id>></code></p><p><code>/unhandled_queries.json?per_page=2&#x26;page=5</code> </p></td></tr><tr><td>Get unhandled queries from agent within specified period</td><td><p><strong>start_time</strong>: Specify the <strong>from</strong> timestamp in epoch format such as 1569229247677821</p><p><strong>end_time</strong>: Specify the <strong>to</strong> timestamp in epoch format such as 1569229251418739. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/api/v1/agents/&#x3C;&#x3C;agent_id>></code></p><p><code>/unhandled_queries.json?start_time=1569229247677821&#x26;end_time=1569229251418739</code></p></td></tr></tbody></table>
