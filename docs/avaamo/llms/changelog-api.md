# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/change-log-apis/changelog-api.md

# Changelog API (v1)

## Get agent changelog

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/dashboard/change_logs`

An agent goes through several changes by different users in its life cycle. You can use Changelog API to get a list of changes made to an agent.

#### Query Parameters

| Name                                        | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| agent\_id<mark style="color:red;">\*</mark> | integer | Identifier of the agent for which the changelog is retrieved.                                                                                                                                                                                                                                                                                                                                                                  |
| dashboard\_user\_id                         | integer | <p>Identifier of the user that is the modifier of the resource in the agent for which the changelog is retrieved.  </p><p></p><p>You can get the dashboard\_user\_id from the API response itself.</p>                                                                                                                                                                                                                         |
| resources                                   | string  | <p>Resources in an agent for which you wish to get the changelogs. </p><p></p><p>Supported values are: </p><p>agent</p><p>skills</p><p>entity\_types</p><p>persistent\_menu</p><p>language</p><p>channels</p><p>live\_agent</p><p>conversation\_node</p><p>permissions</p><p>agent\_life\_cycle</p><p></p><p>By default, all resources are considered. You can also specify multiple resources in a comma-separated list. </p> |
| since\_timetoken                            | number  | <p>Timestamp from which the records are fetched. <br></p><p>If you specify timetoken and not since\_timetoken, then the latest 5 entries up to the specified timetoken are fetched. </p><p></p><p>Specify UNIX Epoch Timestamp in microseconds.</p>                                                                                                                                                                            |
| timetoken                                   | number  | Timestamp until which the records are fetched. Default is the current timestamp. Specify UNIX Epoch Timestamp in microseconds.                                                                                                                                                                                                                                                                                                 |
| page                                        | integer | <p>Page from which the entries must be fetched. <br>Default: 1</p>                                                                                                                                                                                                                                                                                                                                                             |
| per\_page                                   | integer | <p>Number of entries fetched per page. <br>Default: 25<br>Maximum value: 100</p>                                                                                                                                                                                                                                                                                                                                               |
| events                                      | String  | <p>Events in an agent for which you wish to get changelog. </p><p></p><p>Supported values are: update, create, destroy</p><p></p><p>By default, all events are considered. You can also specify multiple resources in a comma-separated list. </p>                                                                                                                                                                             |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-Token<mark style="color:red;">\*</mark> | string | <p>User access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information</p> |

{% tabs %}
{% tab title="200 Consider that you wish to get the latest change log from the agent. Use GET method and specify the URL <https://cx.avaamo.com/dashboard/change_logs?agent_id=> <\<agent\_id>>\&per\_page=1. The following is a sample JSON response returned:" %}

```javascript
{
    "current_page": 1,
    "per_page": 1,
    "total_entries": 26,
    "total_pages": 26,
    "time_token": 1576488895.6128085,
    "entries": {
        "change_logs": [
            {
                "resource": {
                    "id": 6043,
                    "type": "Agent's Conversation data"
                },
                "event": "update",
                "changeset": [
                    "John updated Agent's Conversation data"
                ],
                "timestamp": 1576478653,
                "dashboard_user": {
                    "id": 368,
                    "display_name": "John Miller",
                    "email": "sindhu+john@avaamo.com"
                }
            }
        ]
    }
}
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Note**: For optimal API performance, the recommended time duration for fetching data from any of the REST APIs that support a date range or time period is 7 days. &#x20;
{% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/dashboard/change_logs?agent_id=20xxx&resources=skills&events=update' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/dashboard/change_logs?agent_id=20xxx&resources=skills&events=update',
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

<table><thead><tr><th width="219.33333333333331">Attribute</th><th width="375">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>entries -> <a href="#change_logs">change_logs</a></td><td>Indicates an array of change logs fetched from the agent. Number of entries in the array = Number specified in per_page parameter.</td><td>JSON key-value pairs</td></tr></tbody></table>

#### change\_logs

Indicates an array of change logs fetched from the agent. Each array contains the following attributes:

<table><thead><tr><th width="213.33333333333331">Attribute</th><th width="413">Description</th><th>Type</th></tr></thead><tbody><tr><td>resource -> id</td><td>Indicates a unique identifier of the changelog.</td><td>Integer</td></tr><tr><td>resource -> type</td><td>Indicates the type of resource for which the changelog is applicable.</td><td>String</td></tr><tr><td>event</td><td>Indicates the event such as create, update, destroy for which the changelogs are retrieved.</td><td>String</td></tr><tr><td>changeset</td><td>Indicates a comma-separated list of changesets applicable at that timestamp when the changelog was created. </td><td>String array</td></tr><tr><td>timestamp</td><td>Indicates the timestamp of when the changelog was created in seconds. This is the timestamp when the changes for the agent is persistent in the database.</td><td>UNIX epoch timestamp</td></tr><tr><td>dashboard_user -> id</td><td>Indicates the identifier of the user who is the modifier of the resource.</td><td>Integer</td></tr><tr><td>dashboard_user -> display_name</td><td>Indicates the display name of the user who is the modifier of the resource.</td><td>String</td></tr><tr><td>dashboard_user -> email</td><td>Indicates the email of the user who is the modifier of the resource.</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="219.57142857142856">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get the latest changelog of an agent</td><td><ul><li>agent_id: Specify agent identifier.</li><li>per_page: Specify 1 to get the latest changelog. </li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/change_logs?agent_id=1234&#x26;per_page=1</code></p></td></tr><tr><td>Get changelogs of an agent within a specified period</td><td><ul><li>agent_id: Specify agent identifier.</li><li>since_timetoken: Specify the <strong>from</strong> timestamp in epoch format such as 1579149424</li><li>timetoken: Specify the <strong>to</strong> timestamp in epoch format such as 1579149436</li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/change_logs?agent_id=1234&#x26;since_timetoken=1579149424&#x26;timetoken=1579149436</code> </p></td></tr><tr><td>Get changelogs of an agent using pagination</td><td><ul><li>agent_id: Specify agent identifier.</li><li>page: Specify the page from which you wish to fetch records. </li><li>per_page: Specify the number of entries per page. </li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/change_logs?agent_id=1234&#x26;page=5&#x26;per_page=2</code></p><p></p></td></tr><tr><td>Get logs of skill updates in an agent </td><td><ul><li>agent_id: Specify agent identifier.</li><li>resources: Specify <strong>skills</strong> as resources.</li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/change_logs?agent_id=1234&#x26;resources=skills&#x26;events=update</code></p></td></tr><tr><td>Get logs of all updated events in an agent</td><td><ul><li>agent_id: Specify agent identifier.</li><li>events: Specify <strong>update</strong> event.</li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/change_logs?agent_id=1234&#x26;events=update</code></p></td></tr><tr><td>Get all changelogs of a user in an agent</td><td><ul><li>agent_id: Specify agent identifier.</li><li><p>dashboard_user_id: Specify user identifier. You can get the </p><p>dashboard_user_id in the response received from the changelog API.</p></li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/change_logs?agent_id=1234&#x26;dashboard_user_id=5678</code></p></td></tr></tbody></table>
