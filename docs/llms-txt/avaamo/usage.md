# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/usage.md

# Usage

## Get agent usage

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/bots/analytics/{{agent_id}}/usage.json`

Gets statistics on overall usage of the agent such as count of messages, successful responses, ambiguous responses, and success rate percentage.

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name        | Type   | Description                                                                                                                                                                                     |
| ----------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| utc\_offset | number | The difference in seconds from Coordinated Universal Time (UTC) for a particular place and date. The default value is 0 implying that there is no offset from Coordinated Universal Time (UTC). |
| from\_date  | string | <p>Date from which the required details are retrieved. </p><p></p><p>Default value is the last three days from the to\_date. Specify date in dd/mm/yyyy format.</p>                             |
| to\_date    | string | <p>Date to which the required details are retrieved. </p><p></p><p>The default value is the current date. Specify date in dd/mm/yyyy format.</p>                                                |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-Token<mark style="color:red;">\*</mark> | string | <p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200 Successful request" %}

```javascript
{
  "aggregate_stats": {
    "start_time": 1586502000,
    "end_time": 1586847599,
    "session_count": 8123,
    "messages_count": 50138,
    "unhandled_messages_count": 2297,
    "successful_responses_count": 45736,
    "ambiguous_messages_count": 2105,
    "interventions_count": 0,
    "success_rate_count": 47633,
    "success_rate": 91.22
  },
  "previous_interval_stats": {
    "start_time": 1586156401,
    "end_time": 1586502000,
    "session_count": 15094,
    "messages_count": 82686,
    "unhandled_messages_count": 4745,
    "successful_responses_count": 74013,
    "ambiguous_messages_count": 3928,
    "interventions_count": 0,
    "success_rate_count": 77615,
    "success_rate": 89.51
  },
  "stats": [
    {
      "start_time": 1586502000,
      "end_time": 1586540399.8888888,
      "session_count": 2209,
      "messages_count": 11852,
      "unhandled_messages_count": 525,
      "successful_responses_count": 10731,
      "ambiguous_messages_count": 596,
      "interventions_count": 0,
      "success_rate_count": 11255,
      "success_rate": 90.54
    },
    {
      "start_time": 1586540399.8888888,
      "end_time": 1586578799.7777777,
      "session_count": 490,
      "messages_count": 1927,
      "unhandled_messages_count": 168,
      "successful_responses_count": 1689,
      "ambiguous_messages_count": 70,
      "interventions_count": 0,
      "success_rate_count": 1752,
      "success_rate": 87.65
    },
    {
      "start_time": 1586578799.7777777,
      "end_time": 1586617199.6666667,
      "session_count": 1821,
      "messages_count": 11481,
      "unhandled_messages_count": 414,
      "successful_responses_count": 10579,
      "ambiguous_messages_count": 488,
      "interventions_count": 0,
      "success_rate_count": 11031,
      "success_rate": 92.14
    },
    {
      "start_time": 1586617199.6666667,
      "end_time": 1586655599.5555556,
      "session_count": 592,
      "messages_count": 3956,
      "unhandled_messages_count": 153,
      "successful_responses_count": 3703,
      "ambiguous_messages_count": 100,
      "interventions_count": 0,
      "success_rate_count": 3794,
      "success_rate": 93.6
    },
    {
      "start_time": 1586655599.5555556,
      "end_time": 1586693999.4444444,
      "session_count": 1491,
      "messages_count": 8339,
      "unhandled_messages_count": 433,
      "successful_responses_count": 7575,
      "ambiguous_messages_count": 331,
      "interventions_count": 0,
      "success_rate_count": 7870,
      "success_rate": 90.84
    },
    {
      "start_time": 1586693999.4444444,
      "end_time": 1586732399.3333333,
      "session_count": 1064,
      "messages_count": 4568,
      "unhandled_messages_count": 240,
      "successful_responses_count": 4128,
      "ambiguous_messages_count": 200,
      "interventions_count": 0,
      "success_rate_count": 4316,
      "success_rate": 90.37
    },
    {
      "start_time": 1586732399.3333333,
      "end_time": 1586770799.2222223,
      "session_count": 1429,
      "messages_count": 7031,
      "unhandled_messages_count": 330,
      "successful_responses_count": 6421,
      "ambiguous_messages_count": 280,
      "interventions_count": 0,
      "success_rate_count": 6667,
      "success_rate": 91.32
    },
    {
      "start_time": 1586770799.2222223,
      "end_time": 1586809199.1111112,
      "session_count": 225,
      "messages_count": 985,
      "unhandled_messages_count": 34,
      "successful_responses_count": 911,
      "ambiguous_messages_count": 40,
      "interventions_count": 0,
      "success_rate_count": 949,
      "success_rate": 92.49
    },
    {
      "start_time": 1586809199.1111112,
      "end_time": 1586847599,
      "session_count": 0,
      "messages_count": 0,
      "unhandled_messages_count": 0,
      "successful_responses_count": 0,
      "ambiguous_messages_count": 0,
      "interventions_count": 0,
      "success_rate_count": 0,
      "success_rate": null
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
curl --location --request GET 'https://cx.avaamo.com/bots/analytics/20xxx/usage.json?utc_offset=19800' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/bots/analytics/20xxx/usage.json?utc_offset=19800',
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

In response JSON, the following statistics can be viewed:

* **aggregate\_stats**: Indicates agent usage statistics for the time period (to\_date - from\_date) specified in the query parameters. Example: from\_date -> 15th November, to\_date -> 30th November. Here, aggregate\_stats is displayed for a period of 15 days from 15th November to 30th November.
* **previous\_interval\_stats**: Indicates agent usage statistics for the same number of days prior to the from\_date. Example: Here, previous\_interval\_stats is displayed for a period of 15 days prior to from\_date (1st November to 15th November).
* **stats**: This is an array of 9 elements. Each array element provides statistics for a specific duration interval. Duration Interval = \[(end\_time - start\_time) in aggregate\_stats] / 9.

Each of these statistics contains the following details:

| Attribute                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Type                 |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| start\_time, end\_time       | Indicates the time frame for which statistics are applicable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Unix epoch timestamp |
| session\_count               | Indicates the number of sessions in the specified time frame. Here, a session indicates a user agent interaction.                                                                                                                                                                                                                                                                                                                                                                                                                              | Integer              |
| messages\_count              | Indicates the number of messages received by the agent in the specified time frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer              |
| unhandled\_messages\_count   | Indicates the number of messages that led to unhandled responses in the specified time frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Integer              |
| successful\_responses\_count | <p>Indicates the number of successful responses in the specified time frame. </p><p><code>successful\_responses\_count =</code> </p><p><code>(messages\_count - unhandled\_messages\_count - ambiguous\_messages\_count)</code></p>                                                                                                                                                                                                                                                                                                            | Integer              |
| ambiguous\_messages\_count   | Indicates the number of messages that led to ambiguous responses in the specified time frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Integer              |
| interventions\_count         | Indicates the number of agent interventions in the specified time frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer              |
| success\_rate                | Indicates the success rate of the agent in percentage. `success_rate = (successful_responses_count / messages_count) * 100`                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer              |
| success\_rate\_count         | <p>Indicates the number of successful responses including only those ambiguous messages that are not mismatched. </p><p></p><p>Note that during disambiguation, </p><ul><li>If you select none of the above options, then that is considered mismatched. </li><li>If the user did not choose any of the options from the list, then the query is counted in ambiguous\_messages\_count.</li></ul><p><code>success\_rate\_count = successful\_responses\_count + ambiguous\_messages\_count - mismatched\_ambiguous\_messages\_count</code></p> | Integer              |

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="150">Use-case</th><th width="600.4285714285713">Query Parameter</th></tr></thead><tbody><tr><td>Get an overall list of agent usage </td><td><code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/usage.json?utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></td></tr><tr><td>Get agent usage  within a specified period</td><td><p><strong>from_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/usage.json?from_date=01/04/2020&#x26;to_date=06/04/2020&#x26;utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></p></td></tr></tbody></table>
