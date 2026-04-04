# Source: https://docs.avaamo.com/user-guide/live-agent-console/live-agent-console-rest-apis/live-agent-changelog-api.md

# Live Agent Changelog API

## Get live agent changelog

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v1/cap/change_logs.json`

Captures all the configuration changes performed by the live agent (such as live agent status updates) and the supervisors (such as configuration changes in Teams, Routing rules, or Quick responses).&#x20;

Note that the live agent change log API captures only configuration changes in the Live agent console. See [Live Sessions ](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/live-sessions)and [Reports](https://docs.avaamo.com/user-guide/live-agent-console/supervisor/reports) page to view transactional changes in the Live agent console such as incoming chat requests, wait time, and conversation duration.

#### Query Parameters

| Name        | Type    | Description                                                                                                                                                                                                                                                                                           |
| ----------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start\_time | number  | <p>Timestamp from which the records are fetched. <br></p><p>If you specify timetoken and not end\_time, then the latest 5 entries up to the specified timetoken are fetched. </p><p></p><p>Specify UNIX Epoch Timestamp in milliseconds.</p>                                                          |
| end\_time   | number  | <p>Timestamp until which the records are fetched. Default is the current timestamp. </p><p></p><p>Specify UNIX Epoch Timestamp in milliseconds.</p>                                                                                                                                                   |
| page        | integer | <p>Page from which the entries must be fetched. <br>Default: 1</p>                                                                                                                                                                                                                                    |
| per\_page   | integer | <p>Number of entries fetched per page. <br>Default: 25<br>Maximum value: 100</p>                                                                                                                                                                                                                      |
| actions     | String  | <p>Actions in an live agent for which you wish to get changelog. </p><p></p><p>Supported values are: update, create, destroy</p><p></p><p>By default, all actions are considered. You can also specify multiple resources in a comma-separated list. </p><p></p><p>Example: actions=update,create</p> |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | string | <p>User access token. Both live agents and supervisors can access the changelogs.</p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p> |

{% tabs %}
{% tab title="200 Sample Reponse" %}
{% code overflow="wrap" %}

```json
{
  "current_page": 1,
  "per_page": 1,
  "total_entries": 3,
  "total_pages": 3,
  "time_token": 1699347493.7744794,
  "entries": [
    {
      "id": 2202442,
      "resource": {
        "id": 739,
        "type": "User"
      },
      "action": "update",
      "changelog": "Donna Miller updated User Donna Miller status from 'offline' to 'active",
      "timestamp": 1699264790,
      "dashboard_user": {
        "id": 739,
        "display_name": "Donna Miller",
        "email": "donna@avaamo.com"
      }
    }
  ]
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Note**: For optimal API performance, the recommended time duration for fetching data from any of the REST APIs that support a date range or time period is 7 days.
{% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/api/v1/cap/change_logs.json?per_page=1' \
--header 'Content-Type: application/json' \
--header 'access-token: xxxxxxxxx9a34a44a838af10fxxxxxxx'
```

{% endcode %}
{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v2/outreach/change_logs?per_page=1',
  'headers': {
    'Content-Type': 'application/json',
    'access-token': 'xxxxxxxxx9a34a44a838af10fxxxxxxx'
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

The following is a sample response of a successful API request:

```json
{
  "current_page": 1,
  "per_page": 1,
  "total_entries": 3,
  "total_pages": 3,
  "time_token": 1699347493.7744794,
  "entries": [
    {
      "id": 2202442,
      "resource": {
        "id": 739,
        "type": "User"
      },
      "action": "update",
      "changelog": "Donna Miller updated User Donna Miller status from 'offline' to 'active",
      "timestamp": 1699264790,
      "dashboard_user": {
        "id": 739,
        "display_name": "Donna Miller",
        "email": "donna@avaamo.com"
      }
    }
  ]
}
```

In the response, the following attributes are returned:

<table><thead><tr><th width="173.97643515043268">Attribute</th><th width="321.2689031392294">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the live agent changelog.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td><a href="#entries">entries</a></td><td>Indicates an array of change logs fetched from the live agent. Number of entries in the array = Number specified in per_page parameter.</td><td>JSON key-value pairs</td></tr></tbody></table>

#### entries

Indicates an array of change logs fetched from the campaign. Each array contains the following attributes:

<table><thead><tr><th>Attribute</th><th width="297.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>id</td><td>Indicates a unique identifier for the changelog entry.</td><td>Integer</td></tr><tr><td>resource -> id</td><td>Indicates a unique identifier of the resource for which the changelog is listed such as the live agent identifier,  Teams identifier, Routing rule identifier, or Quick response identifier.</td><td>Integer</td></tr><tr><td>resource -> type</td><td>Indicates the type of resource for which the changelog is applicable.</td><td>String</td></tr><tr><td>action</td><td>Indicates the action such as create, update, destroy for which the changelogs are retrieved.</td><td>String</td></tr><tr><td>changelog</td><td><p>Indicates the actual change that occurred for this entry. </p><p></p><p>This is a user-friendly description to help you identify the type of change..</p></td><td>String </td></tr><tr><td>timestamp</td><td><p>Indicates the timestamp of when the changelog was created in seconds. </p><p></p><p>This is the timestamp when the changes for the campaign are persistent in the database.</p></td><td>UNIX epoch timestamp</td></tr><tr><td>dashboard_user -> id</td><td>Indicates the identifier of the user who is the modifier of the resource.</td><td>Integer</td></tr><tr><td>dashboard_user -> display_name</td><td>Indicates the display name of the user who is the modifier of the resource.</td><td>String</td></tr><tr><td>dashboard_user -> email</td><td>Indicates the email of the user who is the modifier of the resource.</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="239.22619600434115">Use-case</th><th width="502.61793372319687">Query Parameter</th></tr></thead><tbody><tr><td>Get changelogs within a specified period</td><td><ul><li>start_time: Specify the <strong>from</strong> timestamp in epoch format such as 1579149424</li><li>end_time: Specify the <strong>to</strong> timestamp in epoch format such as 1579149436</li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/api/v1/cap/change_logs.json?start_time=1579149424&#x26;end_time=1579149436</code> </p></td></tr><tr><td>Get changelogs using pagination</td><td><ul><li>page: Specify the page from which you wish to fetch records. By default, the value is 1.</li><li>per_page: Specify the number of entries per page. By default, the value is 25. </li></ul><p><strong>Example</strong>: </p><p><code>https://cx.avaamo.com/api/v1/cap/change_logs.json?page=5&#x26;per_page=2</code></p><p>Here, per_page * total_pages = total_entries</p></td></tr><tr><td>Get changelogs of all updated campaign records within a specified period</td><td><ul><li>start_time: Specify the <strong>from</strong> timestamp in epoch format such as 1579149424</li><li>end_time: Specify the <strong>to</strong> timestamp in epoch format such as 1579149436</li><li>action: Specify <strong>update</strong></li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/api/v1/cap/change_logs.json?start_time=1579149424&#x26;end_time=1579149436&#x26;actions=update</code> </p></td></tr><tr><td></td><td></td></tr></tbody></table>
