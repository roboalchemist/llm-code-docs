# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/user-storage-api.md

# User Storage API

## Get user storage data

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/dashboard/bots/{{agent_id}}/storages.json`

Get the data stored for a specific user session in your agent.

#### Path Parameters

<table><thead><tr><th width="152">Name</th><th width="100">Type</th><th>Description</th></tr></thead><tbody><tr><td>agent_id<mark style="color:red;">*</mark></td><td>integer</td><td>Agent identifier. You can get the agent identifier from the agent URL. </td></tr></tbody></table>

#### Query Parameters

<table><thead><tr><th width="155">Name</th><th width="98">Type</th><th>Description</th></tr></thead><tbody><tr><td>key</td><td>string</td><td>Key of the storage variable.</td></tr><tr><td>value</td><td>string</td><td>Value of the storage variable.</td></tr><tr><td>user_id</td><td>integer</td><td>User identifier for which the value is stored. <br>You can get the user_id from the API response itself. Use this to further filter the data, if required.</td></tr><tr><td>start_date</td><td>string</td><td>Date from which the storage data is retrieved. Specify date in dd/mm/yyyy format.</td></tr><tr><td>end_date</td><td>string</td><td>Date until which the storage data is retrieved. Specify in dd/mm/yyyy format.</td></tr><tr><td>page</td><td>integer</td><td>Page from which the entries must be fetched. <br>Default value: 1</td></tr><tr><td>per_page</td><td>integer</td><td>Number of entries fetched per page. <br>Default value: 25<br>Maximum value: 100</td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="157">Name</th><th width="100">Type</th><th>Description</th></tr></thead><tbody><tr><td>Access-Token<mark style="color:red;">*</mark></td><td>string</td><td><p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr></tbody></table>

{% tabs %}
{% tab title="200 Success" %}

```javascript
{
    "current_page": 1,
    "per_page": 1,
    "total_entries": 582068,
    "total_pages": 582068,
    "storage": [
        {
            "key": "current_plan",
            "value": "Lifetime Plan",
            "id": 15495246,
            "created_at": 1586750021.0,
            "updated_at": 1586750442.0,
            "user": {
                "display_name": "User 8880460",
                "id": 8880460
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

```javascript
curl --location --request GET 'https://cx.avaamo.com/dashboard/bots/20xxx/storages.json?per_page=1' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/dashboard/bots/20xxx/storages.json?per_page=1',
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

<table><thead><tr><th width="205.3137615449594">Attribute</th><th width="380.5888501742161">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td><a href="#storage">storage</a></td><td>Indicates an array of messages fetched from the agent. The number of entries in the array = Number specified in the per_page parameter.</td><td>JSON key-value pairs</td></tr></tbody></table>

#### storage

Indicates an array of storage data fetched from the agent. Each array contains the following attributes:

<table><thead><tr><th width="167.41036354774155">Attribute</th><th width="381.06937919317096">Description</th><th>Type</th></tr></thead><tbody><tr><td>key</td><td>Indicates the key of the storage variable.</td><td>String</td></tr><tr><td>value</td><td>Indicates the value of the storage variable.</td><td>String</td></tr><tr><td>id</td><td>Indicates the identifier of the storage variable.</td><td>String</td></tr><tr><td>created_at</td><td>Indicates the timestamp of when the storage variable was created in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>updated_at</td><td>Indicates the timestamp of when the storage variable was updated in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>user -> display_name</td><td>Indicates the display name of the user for which the value is stored. </td><td>String</td></tr><tr><td>user -> id</td><td>This is applicable only for user storage variables. Indicates the identifier of the user for which the value is stored. </td><td>Integer</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="190.01652591091437">Use-case</th><th width="409.2896125311376">Query Parameter</th></tr></thead><tbody><tr><td>Get the latest storage data from the agent</td><td><p><strong>per_page</strong>: Specify 1 to get the latest message. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/storages.json?per_page=1</code></p></td></tr><tr><td>Get storage data with a specified key and value</td><td><p><strong>key</strong>: Specify the key of the storage variable.</p><p><strong>value</strong>: Specify the value of the storage variable.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/storages.json?key=&#x3C;&#x3C;key>>&#x26;value=&#x3C;&#x3C;value>></code></p></td></tr><tr><td>Get storage data specific to a user</td><td><p><strong>user_id</strong>: Specify the user identifier.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/storages.json?user_id=&#x3C;&#x3C;user_id>></code></p></td></tr><tr><td>Get storage data within a specified period</td><td><p><strong>start_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/storages.json?start_date=12/04/2020&#x26;end_date=13/04/2020</code></p></td></tr><tr><td>Get storage data using pagination</td><td><p><strong>page</strong>: Specify the page from which you wish to fetch records. </p><p><strong>per_page</strong>: Specify the number of entries per page. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/storages.json?page=2&#x26;per_page=5</code></p></td></tr></tbody></table>

## Set user storage data

<mark style="color:green;">`POST`</mark> `https://cx.avaamo.com/bots_api/v1/users/{{user_layer_id}}/set_storage.json`

Sets the value in a user session at the agent level.

#### Path Parameters

<table><thead><tr><th width="163">Name</th><th width="97">Type</th><th>Description</th></tr></thead><tbody><tr><td>user_layer_id<mark style="color:red;">*</mark></td><td>string</td><td>Unique user identifier internally used by the Avaamo Platform. You can get the user layer identifier from the <a href="../conversation-message-api#get-conversation-messages">Conversation Message API</a> or from <a href="../message-api#get-agent-messages">Message API</a>.  <br> <br>Specify the user_layer_id of the user to set the storage value for a user.</td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="170">Name</th><th width="93">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td><p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr></tbody></table>

#### Request Body

<table><thead><tr><th width="168">Name</th><th width="99">Type</th><th>Description</th></tr></thead><tbody><tr><td>key<mark style="color:red;">*</mark></td><td>string</td><td>Key of the storage variable</td></tr><tr><td>value<mark style="color:red;">*</mark></td><td>string</td><td>Value of the storage variable.</td></tr><tr><td>bot_id<mark style="color:red;">*</mark></td><td>integer</td><td>Unique identifier of the agent. <br>You can get the agent identifier from the agent URL.</td></tr></tbody></table>

{% tabs %}
{% tab title="200: OK Successful request" %}

```javascript
{
    "status": 201
}
```

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request POST 'https://cx.avaamo.com/bots_api/v1/users/dashboard_admin_test_user_368/set_storage.json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
      "key": "role",
      "value": "guest",
      "bot_id": 8017
  }'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://cx.avaamo.com/bots_api/v1/users/dashboard_admin_test_user_368/set_storage.json',
  'headers': {
    'Access-Token': 'xxxxxx8d9952499ea466fc007dxxxxxx',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({"key":"role","value":"guest","bot_id":8017})

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

{% endtab %}
{% endtabs %}

### Examples

#### Set storage value for a user session

**Request**: The following is a sample JSON request for setting the storage value for a user session:

1. Get the user\_layer\_id from the Conversation Message API. See [Conversation Message API](https://docs.avaamo.com/user-guide/ref/conversation-message-api#get-conversation-messages), for more information.
2. Pass the user\_layer\_id of the user for which you wish to set the storage variable in the set\_storage API URL.
3. Specify the following payload in the Set Storage API:

```yaml
{
  "key": "role",
  "value": "guest",
  "bot_id": 8017
}
```

You can refer to the following example for more details.

{% file src="<https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MHtkO9fF4jepBJfXRlG%2F-MHtnPKBwPyHQTKLNCwx%2FSetStorageAPI_Example.html?alt=media&token=0e9d7b00-93f1-4ba5-9021-921278597bac>" %}
Use setstorage API of the user by conversation uuid
{% endfile %}

**Result**: You can view the storage variable set for the user in the **Debug -> Storage** page. See [Storage](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents#using-storage), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MHtH_8EgL9IGsEUOVr1%2F-MHtKozNE0r52HNcMBkj%2Fstorage-user-level.png?alt=media\&token=4df137f8-4363-4b71-a4bc-26864cc2cfbe)
