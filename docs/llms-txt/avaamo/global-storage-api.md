# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/global-storage-api.md

# Global Storage API

## Get global storage data

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/bots_api/v1/storages/{{key}}.json?bot_id={{bot_id}}`

Get the value of the specified key from the agent's global storage.

#### Path Parameters

| Name                                  | Type   | Description                  |
| ------------------------------------- | ------ | ---------------------------- |
| key<mark style="color:red;">\*</mark> | String | Key of the storage variable. |

#### Query Parameters

| Name                                      | Type    | Description                                                            |
| ----------------------------------------- | ------- | ---------------------------------------------------------------------- |
| bot\_id<mark style="color:red;">\*</mark> | Integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Headers

| Name                                            | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token <mark style="color:red;">\*</mark> | String | <p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "key": "bearer_token",
    "value": "jfqbu23Zi2"
}
```

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/bots_api/v1/storages/<<key>>.json?bot_id=30xxx' \
--header 'access-token: xxxxxxe6e3aa45349dad98axxxxxxxxx'
```

{% endtab %}

{% tab title="node.js " %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/bots_api/v1/storages/<<key>>.json?bot_id=30xxx',
  'headers': {
    'access-token': 'xxxxxxe6e3aa45349dad98axxxxxxxxx'
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

<table><thead><tr><th>Attribute</th><th width="352.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>key</td><td>Indicates the key of the storage variable.</td><td>String</td></tr><tr><td>value</td><td>Indicates the value of the storage variable.</td><td>String</td></tr></tbody></table>

### Example

The following table lists a sample use case with query parameters:

| Use-case                               | Description                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Get global storage data value of a key | <p><strong>key</strong>: Specify the key of the storage variable in the request.</p><p></p><p><strong>Example</strong>: [https://cx.avaamo.com/bots\_api/v1/storages/\&#x3C;\&#x3C;key>>.json?bot\_id=\&#x3C;\&#x3C;bot\_id>>](https://cx.avaamo.com/bots_api/v1/storages/\&#x3C;\&#x3C;key>>.json?bot_id=\&#x3C;\&#x3C;bot_id>>)</p> |

## Set global storage data

<mark style="color:orange;">`PUT`</mark> `https://cx.avaamo.com/bots_api/v1/storages/{{key}}.json?bot_id={{bot_id}}`

Stores key and the value in agent's global storage. This is applicable to all the users interacting with agents.

#### Path Parameters

| Name                                  | Type   | Description                  |
| ------------------------------------- | ------ | ---------------------------- |
| key<mark style="color:red;">\*</mark> | String | Key of the storage variable. |

#### Query Parameters

| Name    | Type    | Description                                                            |
| ------- | ------- | ---------------------------------------------------------------------- |
| bot\_id | Integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Headers

| Name                                            | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ----------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access\_token<mark style="color:red;">\*</mark> | String | <p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

#### Request Body

| Name                                    | Type   | Description                    |
| --------------------------------------- | ------ | ------------------------------ |
| value<mark style="color:red;">\*</mark> | String | Value of the storage variable. |

{% tabs %}
{% tab title="201: Created " %}

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
curl --location --request PUT 'https://cx.avaamo.com/bots_api/v1/storages/<<key>>.json?bot_id=30xxx' \
--header 'access-token: xxxxxxe6e3aa45349dad98axxxxxxxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
    "value": "jfqbu23Zi2"
}'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'PUT',
  'url': 'https://cx.avaamo.com/bots_api/v1/storages/<<key>>.json?bot_id=30xxx',
  'headers': {
    'access-token': 'xxxxxxe6e3aa45349dad98axxxxxxxxx',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "value": "jfqbu23Zi2"
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});

```

{% endtab %}
{% endtabs %}

### Example

**Request**: The following is a sample JSON request for setting the storage variable "bearer\_token" in a global session:

1. Send a PUT request with storage key and agent identifier - <https://cx.avaamo.com/bots\\_api/v1/storages/bearer\\_token.json?bot\\_id=30011>
2. Pass the user access token in the Header parameter.
3. Send the payload in the request body with the storage variable value you wish to set.

```json
{
   "value": "jfqbu23Zi2"
}
```

**Result**: You can view the storage variable set for the user in the **Debug -> Storage** page. See [Storage](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents#using-storage), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FYdAW4qNUsY1KThIUNSwu%2Fimage.png?alt=media\&token=dd627ca4-f891-48be-ba35-4af89831a51f)

## Delete global storage data

<mark style="color:red;">`DELETE`</mark> `https://cx.avaamo.com/bots_api/v1/storages/{{key}}.json?bot_id={{bot_id}}`

Delete the storage data of the specified key from the agent's global storage.

#### Path Parameters

| Name                                  | Type   | Description                  |
| ------------------------------------- | ------ | ---------------------------- |
| key<mark style="color:red;">\*</mark> | String | Key of the storage variable. |

#### Query Parameters

| Name                                      | Type    | Description                                                            |
| ----------------------------------------- | ------- | ---------------------------------------------------------------------- |
| bot\_id<mark style="color:red;">\*</mark> | Integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | String | <p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200: OK " %}

```
{
    "status": 200
}
```

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request DELETE 'https://cx.avaamo.com/bots_api/v1/storages/<<key>>.json?bot_id=30xxx' \
--header 'access-token: xxxxxxe6e3aa45349dad98axxxxxxxxx'
```

{% endtab %}
{% endtabs %}
