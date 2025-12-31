# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/user-sessions.md

# User sessions

## Get user sessions

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/bots/analytics/{{agent_id}}/sessions.json`

Gets a list of unique user sessions with the agent within a specified period of time. Here, a user session indicates user interaction with the agent.&#x20;

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name            | Type   | Description                                                                                                                                                                            |
| --------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| per\_page       | number | <p>The number of entries fetched per page. <br>Default value: 25<br>Maximum value: 100 </p>                                                                                            |
| page            | number | <p>Page from which the entries must be fetched. <br>Default value: 1</p>                                                                                                               |
| from\_timetoken | number | <p>Timestamp from which the records are fetched.</p><p></p><p>Default value is last three days from the specified to\_timetoken value. </p><p></p><p>Specify UNIX Epoch Timestamp.</p> |
| to\_timetoken   | number | <p>Timestamp until which the records are fetched. </p><p></p><p>Default is the current timestamp. </p><p></p><p>Specify UNIX Epoch Timestamp.</p>                                      |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | string | <p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information. </p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200 Successful request" %}

```javascript
{
  "current_page": 1,
  "per_page": 1,
  "total_entries": 6,
  "total_pages": 6,
  "time_token": 1600752248.3784475,
  "entries": [
    {
      "first_name": "John",
      "last_name": "Miller",
      "layer_id": "dashboard_admin_test_user_368",
      "created_at": 1576153636
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
curl --location --request GET 'https://cx.avaamo.com/bots/analytics/20xxx/sessions.json' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/bots/analytics/20xxx/sessions.json',
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

| Attribute      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Type                 |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| current\_page  | Indicates the page from which the entries are fetched.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer              |
| per\_page      | Indicates the number of entries fetched per page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integer              |
| total\_entries | Indicates the total number of entries in the agent messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Integer              |
| total\_pages   | Indicates the total number of pages calculated using per\_page. Note that total\_entries = per\_page \* total\_pages                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer              |
| time\_token    | Indicates the timestamp at which the API response is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | UNIX epoch timestamp |
| entries        | <p>Indicates an array of user sessions fetched from the agent. The number of entries in the array = Number specified in the per\_page parameter. Each array contains the following details of each user session: </p><ul><li>first\_name: First name of the user. Currently, for non-dashboard users, the name is displayed as "You".</li><li>last\_name: Last name of the user, if any.</li><li>layer\_id: Unique user identifier used internally by the Avaamo Platform.</li><li>created\_at: Indicates the timestamp in UNIX epoch timestamp format of when the session was created in seconds. </li></ul> | JSON key-value pairs |

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="150">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get unique user sessions in a specified period of time</td><td><p><strong>from_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/bots/analytics/&#x3C;&#x3C;agent_id>>/sessions.json?from_date=01/04/2020&#x26;to_date=06/04/2020&#x26;utc_offset=&#x3C;&#x3C;utc-offset-second</code></p></td></tr></tbody></table>
