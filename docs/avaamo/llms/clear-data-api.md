# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/clear-data-api.md

# Clear Data API

## Clear agent data

<mark style="color:green;">`POST`</mark> `https://cx.avaamo.com/dashboard/agents/{{agent_id}}/clear_data.json`

Clears the following agent data - storage, JS errors, and conversation states. Typically, this API is used when you have a huge amount of such data in an agent that is no longer required.

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-Token<mark style="color:red;">\*</mark> | string | <p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users and Roles page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

#### Request Body

| Name                                          | Type  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| data\_types<mark style="color:red;">\*</mark> | array | <p>Data types you wish to delete from the agent. Supported types: <br>- <strong>storage</strong>: Clears the storage data. You can view the agent storage data in Agent -> Debug -> Storage.<br>- <strong>js\_errors</strong>: Clears the JS errors. You can view the JS errors in Agent -> Debug -> JS Errors and use the Clear All option to clear JS errors from the UI.<br>- <strong>conversation\_sessions</strong>: Clears the conversation states of the agent and takes the conversation to the initial state. Note that this does not clear Conversation History.</p> |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "success": true
}
```

{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Key point**: The agent must be locked for edit.
{% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request POST 'https://cx.avaamo.com/dashboard/agents/20xxx/clear_data.json' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
  "data_types": [
    "storage_data",
    "js_errors",
    "conversation_sessions"
  ]
}'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://cx.avaamo.com/dashboard/agents/20xxx/clear_data.json',
  'headers': {
    'Content-Type': ['application/json', 'application/json'],
    'Access-Token': 'xxxxxx8d9952499ea466fc007dxxxxxx'
  },
  body: JSON.stringify({"data_types":["storage_data","js_errors","conversation_sessions"]})

};
request(options, function (error, response) { 
  if (error) throw new Error(error);
  console.log(response.body);
});

```

{% endtab %}
{% endtabs %}
