# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/top-tags.md

# Top tags

## Get top tags&#x20;

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/bots/analytics/{{agent_id}}/top_tags.json`

Gets a list of tags that are frequently triggered in the conversation flow. In the response, for each of the top tags, you can learn about the tag name and the number of times the tag is used.

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name        | Type   | Description                                                                                                                                                                                                  |
| ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| utc\_offset | number | <p>Difference in seconds from Coordinated Universal Time (UTC) for a particular place and date. </p><p></p><p>Default value is 0 implying that there is no offset from Coordinated Universal Time (UTC).</p> |
| from\_date  | string | <p>Date from which the required details are retrieved. </p><p></p><p>Default value is the last three days from the to\_date. Specify date in dd/mm/yyyy format.</p>                                          |
| to\_date    | string | Date to which the required details are retrieved. Default value is current date. Specify date in dd/mm/yyyy format.                                                                                          |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-Token<mark style="color:red;">\*</mark> | string | <p>User access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200 Successful request" %}

```javascript
{
    "aggregate_tag_count": 12,
    "top_tags": [
        {
            "tag_name": "status",
            "count": 9,
            "tag_id": 829,
            "deleted": false
        },
        {
            "tag_name": "order",
            "count": 3,
            "tag_id": 827,
            "deleted": false
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

{% hint style="success" %}
**Key points**:&#x20;

* Only custom tags are included in the Top tags API. See [Tags](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-tags), for more information.
* For optimal API performance, the recommended time duration for fetching data from any of the REST APIs that support a date range or time period is 7 days.
  {% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/bots/analytics/20xxx/top_tags.json?utc_offset=19800' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/bots/analytics/20xxx/top_tags.json?utc_offset=19800',
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

In the response, a **top\_tags** array is returned with a list of tags that are frequently triggered in the conversation flow:

{% hint style="info" %}
**Note**: A maximum of 10 records is returned in the response.
{% endhint %}

<table><thead><tr><th width="219">Attribute</th><th width="425.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>aggregate_tag_count</td><td>Indicates the total count of all the top intents frequently used in the conversation flow.</td><td>Integer</td></tr><tr><td>top_tags</td><td><p>Indicates an array of top tags that are frequently used in the conversation flow. Each array contains the following details about the tags: </p><ul><li>tag_id: Indicates the identifier of the tag.</li><li>tag_name: Indicates the name of the tag.</li><li>count: Indicates the number of times the tag was used in the conversation flow.</li><li><p>deleted: Indicates if the top tags are present or deleted in the agent. Possible values: true, false.</p><ul><li>true: A top tag that matched earlier has been deleted. As the API is based on historical data, the deleted top tag is also included in the API response.</li><li>false: A tag that still is a top tag and has not been deleted.</li></ul></li></ul><p></p></td><td>Array of JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="173.1290322580645">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get list of top tags</td><td><p><code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/</code></p><p><code>top_tags.json?utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></p></td></tr><tr><td>Get top tags within a specified period</td><td><p><strong>from_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/top_tags.json?from_date=01/04/2020&#x26;to_date=06/04/2020&#x26;utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></p></td></tr></tbody></table>
