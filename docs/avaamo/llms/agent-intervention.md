# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/agent-intervention.md

# Live agent intervention

## Get live agent interventions

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/bots/analytics/{{agent_id}}/agent_intervention.json`

Gets the statistics on the live agent transfers by the users.&#x20;

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name        | Type   | Description                                                                                                                                                                             |
| ----------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| utc\_offset | number | Difference in seconds from Coordinated Universal Time (UTC) for a particular place and date. Default value is 0 implying that there is no offset from Coordinated Universal Time (UTC). |
| from\_date  | string | <p>Date from which the required details are retrieved. </p><p></p><p>Default value is the last three days from the to\_date. Specify date in dd/mm/yyyy format.</p>                     |
| to\_date    | string | <p>Date to which the required details are retrieved. </p><p></p><p>Default value is the current date. Specify date in dd/mm/yyyy format.</p>                                            |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-Token<mark style="color:red;">\*</mark> | string | <p>User access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information</p> |

{% tabs %}
{% tab title="200 Successful request" %}

```javascript
{
  "aggregate_stats": {
    "start_time": 1586502000,
    "end_time": 1586847599,
    "session_count": 7858,
    "interventions_count": 5,
    "users_count": 7858
  },
  "previous_interval_stats": {
    "start_time": 1586156401,
    "end_time": 1586502000,
    "session_count": 15094,
    "interventions_count": 0,
    "users_count": 15094
  },
  "stats": [
    {
      "start_time": 1586502000,
      "end_time": 1586540399.8888888,
      "session_count": 2209,
      "interventions_count": 2,
      "users_count": 2209
    },
    {
      "start_time": 1586540399.8888888,
      "end_time": 1586578799.7777777,
      "session_count": 490,
      "interventions_count": 2,
      "users_count": 490
    },
    {
      "start_time": 1586578799.7777777,
      "end_time": 1586617199.6666667,
      "session_count": 1821,
      "interventions_count": 1,
      "users_count": 1821
    },
    {
      "start_time": 1586617199.6666667,
      "end_time": 1586655599.5555556,
      "session_count": 592,
      "interventions_count": 0,
      "users_count": 592
    },
    {
      "start_time": 1586655599.5555556,
      "end_time": 1586693999.4444444,
      "session_count": 1491,
      "interventions_count": 0,
      "users_count": 1491
    },
    {
      "start_time": 1586693999.4444444,
      "end_time": 1586732399.3333333,
      "session_count": 1064,
      "interventions_count": 0,
      "users_count": 1064
    },
    {
      "start_time": 1586732399.3333333,
      "end_time": 1586770799.2222223,
      "session_count": 1291,
      "interventions_count": 0,
      "users_count": 1291
    },
    {
      "start_time": 1586770799.2222223,
      "end_time": 1586809199.1111112,
      "session_count": 0,
      "interventions_count": 0,
      "users_count": 0
    },
    {
      "start_time": 1586809199.1111112,
      "end_time": 1586847599,
      "session_count": 0,
      "interventions_count": 0,
      "users_count": 0
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
curl --location --request GET 'https://cx.avaamo.com/bots/analytics/20xxx/agent_intervention.json?from_date=25/01/2020&to_date=25/05/2020&utc_offset=19800' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/bots/analytics/20xxx/agent_intervention.json?from_date=25/01/2020&to_date=25/05/2020&utc_offset=19800',
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

In response JSON, the following statistics can be viewed:

* **aggregate\_stats**: Indicates agent usage statistics for the time period (to\_date - from\_date) specified in the query parameters. Example: from\_date -> 15th November, 2020, to\_date -> 30th November, 2020. Here, aggregate\_stats is displayed for a period of 15 days from 15th November to 30th November.
* **previous\_interval\_stats**: Indicates agent usage statistics for the same number of days prior to from\_date. Example: Here, previous\_interval\_stats is displayed for a period of 15 days prior to from\_date (1st November to 15th November).
* **stats**: This is an array of 9 elements. Each array element provides statistics for a specific duration interval. Duration Interval = \[(end\_time - start\_time) in aggregate\_stats] / 9.

Each of these statistics contains the following details:

| Attribute               | Description                                                                               | Type                 |
| ----------------------- | ----------------------------------------------------------------------------------------- | -------------------- |
| start\_time,  end\_time | Indicates the time frame for which session\_count, interventions\_count, and users\_count | Unix epoch timestamp |
| session\_count          | Indicates the number of sessions in the specified time frame.                             | Integer              |
| interventions\_count    | Indicates the number of agent interventions in the specified time frame.                  | Integer              |
| users\_count            | Indicates the number of users in the session for the specified time frame.                | Integer              |

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="173">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get overall list of agent interventions </td><td><code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/agent_intervention.json?utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></td></tr><tr><td>Get agent interventions within a specified period</td><td><p><strong>from_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/agent_intervention.json?from_date=01/04/2020&#x26;to_date=06/04/2020&#x26;utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></p></td></tr></tbody></table>
