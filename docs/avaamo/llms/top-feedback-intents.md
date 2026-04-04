# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/top-feedback-intents.md

# Top feedback intents

## Get top feedback intents&#x20;

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/bots/analytics/{{agent_id}}/top_feedback_intents.json`

Gets a list of top intents for which feedback is received by the agent. In the response, for each of the intents, you can learn about the intent name, the number of positive feedback responses, and the number of negative feedback responses. You can further use **Feedback API**, to get detailed feedback responses.&#x20;

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name        | Type   | Description                                                                                                                                                                                                  |
| ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| utc\_offset | number | <p>Difference in seconds from Coordinated Universal Time (UTC) for a particular place and date. </p><p></p><p>Default value is 0 implying that there is no offset from Coordinated Universal Time (UTC).</p> |
| from\_date  | string | <p>Date from which the required details are retrieved. </p><p></p><p>Default value is the last three days from the to\_date. </p><p></p><p>Specify date in dd/mm/yyyy format.</p>                            |
| to\_date    | string | <p>Date to which the required details are retrieved. </p><p></p><p>Default value is the current date. </p><p></p><p>Specify date in dd/mm/yyyy format.</p>                                                   |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-Token<mark style="color:red;">\*</mark> | string | <p>User access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200 Successful request" %}

```javascript
{
  "aggregate_intent_count": {
    "positive": 874,
    "negative": 615
  },
  "top_intents": [
    {
      "positive": 135,
      "negative": 18,
      "intent_name": "Thanks"
    },
    {
      "negative": 7,
      "positive": 3,
      "intent_name": "Bye"
    },
    {
      "negative": 3,
      "positive": 3,
      "intent_name": "Policy Information"
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
curl --location --request GET 'https://cx.avaamo.com/bots/analytics/20xxx/top_feedback_intents.json?utc_offset=19800' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/bots/analytics/20xxx/top_feedback_intents.json?utc_offset=19800',
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

In the response, **top\_intents** array is returned with a list of top intents for which feedback is received by the agent:

{% hint style="info" %}
**Note**: A maximum of 10 records is returned in the response.
{% endhint %}

| Attribute                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                       | Type                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| aggregate\_intent\_count | Indicates the total count of positive and negative feedback received by the agent.                                                                                                                                                                                                                                                                                                                                                                | Integer                       |
| top\_intents             | <p>Indicates an array of top intents for which feedback is received by the agent. Each array contains the following details about the intents: </p><ul><li>negative: Indicates the number of negative feedback responses received for this intent.</li><li>positive: Indicates the number of positive feedback responses received for this intent.</li><li>intent\_name: Indicates the name of intent for which the feedback was given.</li></ul> | Array of JSON key-value pairs |

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="150">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get list of top intents for which feedback is received by the agent. </td><td><code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/top_feedback_intents.json?utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></td></tr><tr><td>Get top intents for which feedback is received by the agent within a specified period. </td><td><p><strong>from_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/top_feedback_intents.json?from_date=01/04/2020&#x26;to_date=06/04/2020</code></p><p><code>&#x26;utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code> </p></td></tr></tbody></table>
