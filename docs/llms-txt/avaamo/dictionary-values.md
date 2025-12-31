# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/dictionary-values.md

# Dictionary values

## Get dictionary values

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}/dictionary_values.json`

Get a list of all the dictionary values from an agent.&#x20;

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name      | Type    | Description                                                                      |
| --------- | ------- | -------------------------------------------------------------------------------- |
| page      | integer | <p>Page from which the entries must be fetched. <br>Default: 1</p>               |
| per\_page | integer | <p>Number of entries fetched per page. <br>Default: 25<br>Maximum value: 100</p> |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-Token<mark style="color:red;">\*</mark> | string | <p>User access token. You can get the user access token from the Settings -> Users page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information </p> |

{% tabs %}
{% tab title="200 " %}

```javascript
{
  "current_page": 1,
  "per_page": 5,
  "total_entries": 2,
  "total_pages": 1,
  "time_token": 1590675292.2248158,
  "dictionary_values": [
    {
      "id": 19376,
      "value": "POS",
      "dictionary_id": 755,
      "created_at": 1590399522,
      "updated_at": 1590491408,
      "synonyms": [
        {
          "id": 19377,
          "value": "Pizza Order Status",
          "parent_id": 19376,
          "created_at": 1590399522,
          "updated_at": 1590491408
        }
      ]
    },
    {
      "id": 19632,
      "value": "SSN",
      "dictionary_id": 755,
      "created_at": 1590467160,
      "updated_at": 1590491408,
      "synonyms": [
        {
          "id": 19633,
          "value": "Social Security Number",
          "parent_id": 19632,
          "created_at": 1590467160,
          "updated_at": 1590491408
        }
      ]
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
curl --location --request GET 'https://cx.avaamo.com/api/v1/agents/20xxx/dictionary_values.json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v1/agents/20xxx/dictionary_values.json',
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

### **Response attributes**

In the response, the following attributes are returned:

<table><thead><tr><th width="196.9442896935933">Attribute</th><th width="330.6096508215004">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the response.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td>dictionary_values</td><td><p>Indicates an array of dictionary values fetched from the agent. Number of entries in the array = Number specified in per_page parameter. </p><p></p><p>Each array entry contains the following details:</p><ul><li>id: Unique value identifier</li><li>value: Dictionary value</li><li>dicitonary_id:  Indicates the dictionary the value belongs to</li><li>created_at: Created timestamp of dictionary value </li><li>updated_at: Updated timestamp of dictionary value</li><li>synonyms: Array of synonyms specified for the dictionary value. Each synonym contains an identifier, value, created_at, and updated_at details.</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

| Use-case                                          | Query Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Get dictionary values from agent using pagination | <p><strong>page</strong>: Specify the page from which you wish to fetch records. </p><p><strong>per\_page</strong>: Specify the number of entries per page. </p><p></p><p><strong>Example</strong>: <code>[https://cx.avaamo.com/api/v1/agents/\&#x3C;\&#x3C;agent\_id>>/dictionary\_values.json?page=2\&#x26;per\_page=5](https://cx.avaamo.com/api/v1/agents/\&#x3C;\&#x3C;agent_id>>/dictionary_values.json?page=2\&#x26;per_page=5)</code> </p> |
