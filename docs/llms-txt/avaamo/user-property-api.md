# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/user-property-api.md

# User Property API

## Create user property&#x20;

<mark style="color:green;">`POST`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties`

Adds a new user property for the specified agent. Note that the agent must be locked for edit when creating a new user property.

#### Path Parameters

<table><thead><tr><th width="169">Name</th><th width="97">Type</th><th>Description</th></tr></thead><tbody><tr><td>agent_id<mark style="color:red;">*</mark></td><td>integer</td><td>Agent identifier. You can get the agent identifier from the agent URL. </td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="170">Name</th><th width="93">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td><p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr></tbody></table>

#### Request Body

<table><thead><tr><th width="168">Name</th><th width="99">Type</th><th>Description</th></tr></thead><tbody><tr><td>user_property -> name<mark style="color:red;">*</mark></td><td>string</td><td>Name of the user property</td></tr><tr><td>user_property -> key<mark style="color:red;">*</mark></td><td>string</td><td>Key of the user property</td></tr></tbody></table>

{% tabs %}
{% tab title="200: OK Successful request" %}

```javascript
{
    "user_property": {
        "id": 92xx,
        "name": "region",
        "key": "region"
    }
}
```

{% endtab %}
{% endtabs %}

### Response attributes

In the response, the following attributes are returned:

```json
{
    "user_property": {
        "id": 92xx,
        "name": "region",
        "key": "region"
    }
}
```

<table><thead><tr><th width="167.41036354774155">Attribute</th><th width="381.06937919317096">Description</th><th>Type</th></tr></thead><tbody><tr><td>key</td><td>Indicates the key of the user property.</td><td>String</td></tr><tr><td>name</td><td>Indicates the name of the user property.</td><td>String</td></tr><tr><td>id</td><td>Indicates the unique identifier of the user property.</td><td>Integer</td></tr></tbody></table>

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location 'https://cx.avaamo.com/api/v1/agents/94xxx/user_properties' \
--header 'access-token: xxxxxxxxx61f48829a47ccdxxxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "user_property": {
    "name": "region",
    "key": "region"
  }
}'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://cx.avaamo.com/api/v1/agents/94xxx/user_properties',
  'headers': {
    'access-token': 'xxxxxxxxx61f48829a47ccdxxxxxxxxx',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "user_property": {
      "name": "region",
      "key": "region"
    }
  })

};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
log(response.body);
});
```

{% endtab %}
{% endtabs %}

### Example

**Request**: The following is a sample JSON request for adding a new "region" property to an agent:

```yaml
{
  "user_property": {
    "name": "region",
    "key": "region"
  }
}
```

A successful request adds a new property "region" to the agent. You can view the same user property in the `Agent Configuration -> User Property` page. See [User properties](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FTvoU2eQxtB7mvsIINmxY%2Fimage.png?alt=media&#x26;token=1627b525-f58c-4376-b260-7b2c4271f036" alt=""><figcaption></figcaption></figure>

## Get user properties&#x20;

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties/{{property_id}}`

Get a list of all the user properties from the agent. See [User property](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties), for more information.

#### Path Parameters

<table><thead><tr><th width="153">Name</th><th width="106">Type</th><th>Description</th></tr></thead><tbody><tr><td>agent_id<mark style="color:red;">*</mark></td><td>integer</td><td>Agent identifier. You can get the agent identifier from the agent URL. </td></tr><tr><td>property_id</td><td>integer</td><td><p>Property identifier. You can get the property identifier from the API response itself. </p><ul><li>First, get the list of all the user properties from the agent using the User property API.</li><li>From the API response, you can get the property identifier for further use.</li></ul></td></tr></tbody></table>

#### Query Parameters

<table><thead><tr><th width="154">Name</th><th width="111">Type</th><th>Description</th></tr></thead><tbody><tr><td>page</td><td>integer</td><td>Page from which the entries must be fetched. <br>Default value: 1</td></tr><tr><td>per_page</td><td>integer</td><td>Number of entries fetched per page. <br>Default value: 25<br>Maximum value: 100</td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="160">Name</th><th width="109">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td><p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr></tbody></table>

{% tabs %}
{% tab title="200 Success" %}

```json
{
    "current_page": 1,
    "per_page": 25,
    "total_entries": 1,
    "total_pages": 1,
    "time_token": 1717055987.929187,
    "entries": [
        {
            "id": 92xx,
            "name": "region",
            "key": "region"
        }
    ]
}
```

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location 'https://cx.avaamo.com/api/v1/agents/54xxx/user_properties' \
--header 'access-token: xxxxxxxxe61f48829a47ccd9xxxxxxxx'
```

{% endcode %}
{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v1/agents/54xxx/user_properties',
  'headers': {
    'access-token': 'xxxxxxxxe61f48829a47ccd9xxxxxxxx'
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

```json
{
    "current_page": 1,
    "per_page": 25,
    "total_entries": 1,
    "total_pages": 1,
    "time_token": 1717055987.929187,
    "entries": [
        {
            "id": 92xx,
            "name": "region",
            "key": "region"
        }
    ]
}
```

<table><thead><tr><th width="167.3137615449594">Attribute</th><th width="380.5888501742161">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td><a href="#entries">entries</a></td><td>Indicates an array of user properties fetched from the agent. The number of entries in the array = Number specified in the per_page parameter.</td><td><p>JSON </p><p>key-value pairs</p></td></tr></tbody></table>

#### entries

Indicates an array of user properties fetched from the agent. Each array contains the following attributes:

<table><thead><tr><th width="167.41036354774155">Attribute</th><th width="381.06937919317096">Description</th><th>Type</th></tr></thead><tbody><tr><td>key</td><td>Indicates the key of the user property.</td><td>String</td></tr><tr><td>name</td><td>Indicates the name of the user property.</td><td>String</td></tr><tr><td>id</td><td>Indicates the unique identifier of the user property.</td><td>Integer</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases for getting the user properties from agent:

<table><thead><tr><th width="314.1615310846795">Use-case</th><th width="409.2896125311376">Query/Path Parameter</th></tr></thead><tbody><tr><td>Get the latest user property from the agent</td><td><p><strong>Query parameter</strong> -> <strong>per_page</strong>: Specify 1 to get the latest user property. </p><p><strong>Path parameter</strong> -> <strong>agent_id</strong>: Specify the agent identifier</p><p><strong>Path parameter</strong> -> <strong>property_id</strong>: Specify the property identifier</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties?per_page=1</code></p></td></tr><tr><td>Get user property using  property identifier</td><td><p><strong>Path parameter</strong> -> <strong>agent_id</strong>: Specify the agent identifier</p><p><strong>Path parameter</strong> -> <strong>property_id</strong>: Specify the property identifier</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties/{{property_id}}</code></p></td></tr></tbody></table>

## Update user property&#x20;

<mark style="color:green;">`PUT`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties/{{property_id}}`

Update the name of the specified user property. Note that the agent must be locked for edit when updating user property.

#### Path Parameters

<table><thead><tr><th width="160">Name</th><th width="97">Type</th><th>Description</th></tr></thead><tbody><tr><td>agent_id<mark style="color:red;">*</mark></td><td>integer</td><td>Agent identifier. You can get the agent identifier from the agent URL. </td></tr><tr><td>property_id<mark style="color:red;">*</mark></td><td>integer</td><td>Property identifier. Use <a href="#get-user-properties">Get user properties API </a>to get the property identifier.</td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="170">Name</th><th width="93">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td><p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr></tbody></table>

#### Request Body

<table><thead><tr><th width="168">Name</th><th width="99">Type</th><th>Description</th></tr></thead><tbody><tr><td>user_property -> name<mark style="color:red;">*</mark></td><td>string</td><td>Name of the user property</td></tr></tbody></table>

{% tabs %}
{% tab title="200: OK Successful request" %}

<pre class="language-javascript"><code class="lang-javascript"><strong>{
</strong>    "user_property": {
        "id": 92xx,
        "name": "location",
        "key": "region"
    }
}
</code></pre>

{% endtab %}
{% endtabs %}

### Response attributes

In the response, the following attributes are returned:

```json
{
    "user_property": {
        "id": 92xx,
        "name": "location",
        "key": "region"
    }
}
```

<table><thead><tr><th width="145.41036354774155">Attribute</th><th width="420.06937919317096">Description</th><th>Type</th></tr></thead><tbody><tr><td>key</td><td>Indicates the key of the user property.</td><td>String</td></tr><tr><td>name</td><td>Indicates the name of the user property.</td><td>String</td></tr><tr><td>id</td><td>Indicates the unique identifier of the user property.</td><td>Integer</td></tr></tbody></table>

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location --request PUT 'https://cx.avaamo.com/api/v1/agents/942xx/user_properties/92xx' \
--header 'access-token: xxxxxxxxx61f48829a47ccdxxxxxxxxx' \
--header 'Content-Type: application/json' \
--data '{
  "user_property": {
    "name": "location"
  }
}'
```

{% endcode %}
{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'PUT',
  'url': 'https://cx.avaamo.com/api/v1/agents/94xxx/user_properties/92xx',
  'headers': {
    'access-token': 'xxxxxxxxx61f48829a47ccdxxxxxxxxx',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    "user_property": {
      "name": "location"
    }
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

**Request**: The following is a sample JSON request for adding a new "region" property to an agent:

```yaml
{
  "user_property": {
    "name": "location"  
  }
}
```

A successful request updates the name of the specified user property as mentioned in the request. You can view the same user property in the `Agent Configuration -> User Property` page. See [User properties](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-user-properties), for more information.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FU45CryxSNXcnLesMsvKe%2Fimage.png?alt=media&#x26;token=c64bfd7c-7866-4c4b-8073-361c8ee5e916" alt=""><figcaption></figcaption></figure>

## Delete user property&#x20;

<mark style="color:green;">`DELETE`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties/{{property_id}}`

Deletes the specified user property from the agent. Note that the agent must be locked for edit when deleting user property.

#### Path Parameters

<table><thead><tr><th width="160">Name</th><th width="97">Type</th><th>Description</th></tr></thead><tbody><tr><td>agent_id<mark style="color:red;">*</mark></td><td>integer</td><td>Agent identifier. You can get the agent identifier from the agent URL. </td></tr><tr><td>property_id<mark style="color:red;">*</mark></td><td>integer</td><td>Property identifier. Use <a href="#get-user-properties">Get user properties API </a>to get the property identifier.</td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="170">Name</th><th width="93">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td><p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr></tbody></table>

{% tabs %}
{% tab title="200: OK Successful request" %}

<pre class="language-javascript"><code class="lang-javascript"><strong>{}
</strong></code></pre>

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location --request DELETE 'https://cx.avaamo.com/api/v1/agents/94xxx/user_properties/92xx' \
--header 'access-token: xxxxxxxxx61f48829a47ccdxxxxxxxxx' \
--data ''
```

{% endcode %}
{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'DELETE',
  'url': 'https://cx.avaamo.com/api/v1/agents/942xxx/user_properties/92xx',
  'headers': {
    'access-token': 'xxxxxxxxx61f48829a47ccdxxxxxxxxx'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});


```

{% endtab %}
{% endtabs %}

### Example

The following table lists sample use cases for deleting user property from the agent:

<table><thead><tr><th width="276.1615310846795">Use-case</th><th width="409.2896125311376">Path Parameters</th></tr></thead><tbody><tr><td>Delete the user property using property identifier</td><td><ul><li><strong>agent_id</strong>: Specify the agent identifier</li><li><strong>property_id</strong>: Specify the property identifier</li></ul><p><strong>Example</strong>: <code>https://cx.avaamo.com/api/v1/agents/{{agent_id}}/user_properties/{{property_id}}</code></p></td></tr></tbody></table>
