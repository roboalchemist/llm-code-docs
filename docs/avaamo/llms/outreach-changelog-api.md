# Source: https://docs.avaamo.com/user-guide/outreach/outreach-rest-apis/outreach-changelog-api.md

# Outreach Changelog API

## Get outreach changelog

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v2/outreach/change_logs.json`

Outreach campaigns go through several changes by different users in their life cycles. You can use the Outreach Changelog API to get a list of changes made to all the campaigns of an account.

#### Query Parameters

<table><thead><tr><th width="151">Name</th><th width="103">Type</th><th>Description</th></tr></thead><tbody><tr><td>start_time</td><td>number</td><td><p>Timestamp from which the records are fetched. <br></p><p>If you specify timetoken and not end_time, then the latest 5 entries up to the specified timetoken are fetched. </p><p></p><p>Specify UNIX Epoch Timestamp in milliseconds.</p></td></tr><tr><td>end_time</td><td>number</td><td><p>Timestamp until which the records are fetched. Default is the current timestamp. </p><p></p><p>Specify UNIX Epoch Timestamp in milliseconds.</p></td></tr><tr><td>page</td><td>integer</td><td>Page from which the entries must be fetched. <br>Default: 1</td></tr><tr><td>per_page</td><td>integer</td><td>Number of entries fetched per page. <br>Default: 25<br>Maximum value: 100</td></tr><tr><td>actions</td><td>String</td><td><p>Actions in an campaign for which you wish to get changelog. </p><p></p><p>Supported values are: update, create, destroy</p><p></p><p>By default, all actions are considered. You can also specify multiple resources in a comma-separated list. </p><p></p><p>Example: actions=update,create</p></td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="155">Name</th><th width="84">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td><p>User access token. This API gets  the changelog of all the campaigns from the account the user is associated with.</p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the campaign. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr></tbody></table>

{% tabs %}
{% tab title="200 Consider that you wish to get the latest change log from the agent. Use GET method and specify the URL <https://cx.avaamo.com/dashboard/change_logs?agent_id=> <\<agent\_id>>\&per\_page=1. The following is a sample JSON response returned:" %}

```javascript
{
    "current_page": 1,
    "per_page": 1,
    "total_entries": 1916,
    "total_pages": 1916,
    "time_token": 1676971459.482645,
    "entries": [
        {
            "id": 1707596,
            "resource": {
                "id": 30,
                "type": "Outreach::Template"
            },
            "action": "create",
            "changelog": "John Miller created template 'Vaccination test template'",
            "timestamp": 1676967911,
            "dashboard_user": {
                "id": 368,
                "display_name": "John Miller",
                "email": "john@mycompany.com"
            }
        }
    ]
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
{% code overflow="wrap" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/api/v2/outreach/change_logs?per_page=1' \
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
    "total_entries": 1916,
    "total_pages": 1916,
    "time_token": 1676971459.482645,
    "entries": [
        {
            "id": 1707596,
            "resource": {
                "id": 30,
                "type": "Outreach::Template"
            },
            "action": "create",
            "changelog": "John Miller created template 'Vaccination test template'",
            "timestamp": 1676967911,
            "dashboard_user": {
                "id": 368,
                "display_name": "John Miller",
                "email": "john@mycompany.com"
            }
        }
    ]
}
```

In the response, the following attributes are returned:

<table><thead><tr><th width="173.97643515043268">Attribute</th><th width="321.2689031392294">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the campaign changelog.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td><a href="#entries">entries</a></td><td>Indicates an array of change logs fetched from the campaign. Number of entries in the array = Number specified in per_page parameter.</td><td>JSON key-value pairs</td></tr></tbody></table>

#### entries

Indicates an array of change logs fetched from the campaign. Each array contains the following attributes:

<table><thead><tr><th>Attribute</th><th width="297.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>id</td><td>Indicates a unique identifier for the changelog entry.</td><td>Integer</td></tr><tr><td>resource -> id</td><td>Indicates a unique identifier of the resource for which the changelog is listed such as the campaign identifier,  recipient list identifier, filter identifier, or template identifier.</td><td>Integer</td></tr><tr><td>resource -> type</td><td>Indicates the type of resource for which the changelog is applicable.</td><td>String</td></tr><tr><td>action</td><td>Indicates the action such as create, update, destroy for which the changelogs are retrieved.</td><td>String</td></tr><tr><td>changelog</td><td><p>Indicates the actual change that occurred for this entry. </p><p></p><p>This is a user-friendly description to help you identify the type of change..</p></td><td>String </td></tr><tr><td>timestamp</td><td><p>Indicates the timestamp of when the changelog was created in seconds. </p><p></p><p>This is the timestamp when the changes for the campaign are persistent in the database.</p></td><td>UNIX epoch timestamp</td></tr><tr><td>dashboard_user -> id</td><td>Indicates the identifier of the user who is the modifier of the resource.</td><td>Integer</td></tr><tr><td>dashboard_user -> display_name</td><td>Indicates the display name of the user who is the modifier of the resource.</td><td>String</td></tr><tr><td>dashboard_user -> email</td><td>Indicates the email of the user who is the modifier of the resource.</td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="239.22619600434115">Use-case</th><th width="502.61793372319687">Query Parameter</th></tr></thead><tbody><tr><td>Get changelogs within a specified period</td><td><ul><li>start_time: Specify the <strong>from</strong> timestamp in epoch format such as 1579149424</li><li>end_time: Specify the <strong>to</strong> timestamp in epoch format such as 1579149436</li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/api/v2/outreach/change_logs.json?start_time=1579149424&#x26;end_time=1579149436</code> </p></td></tr><tr><td>Get changelogs using pagination</td><td><ul><li>page: Specify the page from which you wish to fetch records. By default, the value is 1.</li><li>per_page: Specify the number of entries per page. By default, the value is 5. </li></ul><p><strong>Example</strong>: </p><p><code>https://cx.avaamo.com/api/v2/outreach/change_logs.json?page=5&#x26;per_page=2</code></p><p>Here, per_page * total_pages = total_entries</p></td></tr><tr><td>Get changelogs of all updated campaign records within a specified period</td><td><ul><li>start_time: Specify the <strong>from</strong> timestamp in epoch format such as 1579149424</li><li>end_time: Specify the <strong>to</strong> timestamp in epoch format such as 1579149436</li><li>action: Specify <strong>update</strong></li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/api/v2/outreach/change_logs.json?start_time=1579149424&#x26;end_time=1579149436&#x26;actions=update</code> </p></td></tr><tr><td></td><td></td></tr></tbody></table>
