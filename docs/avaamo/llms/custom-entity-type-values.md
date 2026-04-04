# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/custom-entity-type-values.md

# Custom entity type API

## Get entity values&#x20;

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v1/custom_entity_types/{{entity_type_id}}/values.json`

Get a list of all entity values from a custom entity type.&#x20;

#### Path Parameters

| Name                                               | Type    | Description                                                                              |
| -------------------------------------------------- | ------- | ---------------------------------------------------------------------------------------- |
| entity\_type\_id<mark style="color:red;">\*</mark> | integer | Entity type identifier. You can get the entity type identifier from the entity type URL. |

#### Query Parameters

| Name      | Type    | Description                                                                      |
| --------- | ------- | -------------------------------------------------------------------------------- |
| page      | integer | <p>Page from which the entries must be fetched. <br>Default: 1</p>               |
| per\_page | integer | <p>Number of entries fetched per page. <br>Default: 25<br>Maximum value: 100</p> |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-Token<mark style="color:red;">\*</mark> | string | <p>User access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information</p> |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "current_page": 1, 
  "per_page": 5,
  "total_entries": 3,
  "total_pages": 1,
  "time_token": 1590674605.172428,
  "values": [
    {
      "id": 14926171,
      "value": "Bread Sticks",
      "alternate_values": []
    },
    {
      "id": 14926168,
      "value": "French Fries",
      "alternate_values": [
        {
          "id": 14926169,
          "value": "French fingers",
          "alternate_values": []
        }
      ]
    },
    {
      "id": 14926167,
      "value": "Onion rings",
      "alternate_values": []
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/api/v1/custom_entity_types/20xxx/values.json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v1/custom_entity_types/20xxx/values.json',
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

<table><thead><tr><th>Attribute</th><th width="384.1463414634146">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td>values</td><td><p>Indicates an array of entity values fetched from the custom entity type. Number of entries in the array = Number specified in per_page parameter. </p><p></p><p>Each array entry contains the following details:</p><ul><li>id: Unique value identifier</li><li>value: Entity value</li><li>alternate_values: Array of alternate values specified for the entity value, if any.</li><li>parent_value: Parent entity value, if any.</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

| Use-case                                                   | Query Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Get entity values from custom entity type using pagination | <p><strong>page</strong>: Specify the page from which you wish to fetch records. </p><p><strong>per\_page</strong>: Specify the number of entries per page. </p><p></p><p><strong>Example</strong>: <code>[https://cx.avaamo.com/api/v1/custom\_entity\_types/\&#x3C;\&#x3C;entity\_type\_id>>/values.json?page=2\&#x26;per\_page=5](https://cx.avaamo.com/api/v1/custom_entity_types/\&#x3C;\&#x3C;entity_type_id>>/values.json?page=2\&#x26;per_page=5)</code> </p><p></p> |
