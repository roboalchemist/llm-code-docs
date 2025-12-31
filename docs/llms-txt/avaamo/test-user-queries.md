# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/test-user-queries.md

# Test user queries

## Post and test user queries

<mark style="color:green;">`POST`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}/test.json`

Posts the user queries to the agent and gets the insights on how the user’s intent is analyzed and matched in the agent flow for each query.

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| access-token<mark style="color:red;">\*</mark> | string | <p>User access token. You can get the user access token from the Settings -> Users page. Users must have at least view permission on the agent.</p><p></p><p>See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information on how to get the user access token.</p><p></p><p>See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information on agent permissions.</p> |

#### Request Body

| Name             | Type    | Description                                                                                                                                                                                                                                                                                           |
| ---------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| data             | array   | An array of queries to be executed. Each query contains a unique identifier that helps to identify the query.                                                                                                                                                                                         |
| batch            | integer | The number of queries to be executed per batch. This is used when you wish to execute queries parallelly in batches.                                                                                                                                                                                  |
| total\_batches   | integer | Total number of batches that you wish to execute queries in. This is used when you wish to execute queries parallelly in batches.                                                                                                                                                                     |
| skip\_javascript | boolean | If custom code and pre-unhandled Javascript blocks must be considered during intent execution or not.                                                                                                                                                                                                 |
| locale           | String  | <p>Language or locale of the user query. See <a href="../../../how-to/build-agents/configure-agents/deploy/web-supported-languages">Web - Supported languages</a>, for more detailed on supported languages.</p><p></p><p>Default: en-US. If language is not specified, then en-US is considered.</p> |

{% tabs %}
{% tab title="201: Created Successful request" %}

```javascript
{
  "result": [
    {
      "query": "I want to order veg cheese pizza",
      "uuid": "10",
      "insight": {
        "id": 944003,
        "intent_name": "MacPizza Order",
        "intent_type": "INLINE::INTENT",
        "node_key": "7.3",
        "score": 1,
        "query_insights": {
          "entities": [
            {
              "entity": "pizza_type_1",
              "entity_type": "pizza_type",
              "entity_value": "veg",
              "domain_key": "bot_inline_domain_5236cd12-b47e-4609-9e02-f883f038ca19",
              "value": "veg",
              "current_value": [
                "cheese",
                "veg"
              ],
              "index": 20,
              "derived_parent": true,
              "parent_entity_key": null,
              "custom_entity_type": true
            },
            {
              "entity": "pizza_toppings_1",
              "entity_type": "pizza_toppings",
              "entity_value": "cheese",
              "domain_key": "bot_inline_domain_5236cd12-b47e-4609-9e02-f883f038ca19",
              "value": "cheese",
              "current_value": "cheese",
              "index": 20,
              "parent_entity_key": "pizza_type",
              "custom_entity_type": true
            }
          ],
          "normalized_document": "want order veg pizzatoppings pizza",
          "intent": "node_intent_node_1",
          "intent_name": "MacPizza Order",
          "training_datum_id": 1165747,
          "matching_document": "I want to order veg cheese pizza",
          "detected_language": "en"
        },
        "skill": {
          "id": 17828,
          "name": "MacPizza Order",
          "type": "bot",
          "source_id": 20459,
          "created_at": 1590390904,
          "updated_at": 1590391698,
          "status": "complete"
        }
      }
    },
    {
      "query": "I want coke",
      "uuid": "11",
      "insight": {
        "id": 944004,
        "intent_name": "Unhandled",
        "intent_type": "UNHANDLED::INTENT",
        "node_key": "1",
        "score": 0,
        "query_insights": {
          "entities": [],
          "normalized_document": "want coke",
          "intent": "",
          "detected_language": "en"
        },
        "skill": {}
      }
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
curl --location --request POST 'https://cx.avaamo.com/api/v1/agents/20xxx/test.json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
	"data": [{"query": "I want to order veg cheese pizza", "uuid": "10"}, {"query": "I want coke", "uuid": "11"}],
	"batch": 1,
	"total_batches": 1,
	"skip_javascript": true
}'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://cx.avaamo.com/api/v1/agents/20xxx/test.json',
  'headers': {
    'Access-Token': 'xxxxxx8d9952499ea466fc007dxxxxxx',
    'Content-Type': ['application/json', 'application/json']
  },
  body: JSON.stringify({"data":[{"query":"I want to order veg cheese pizza","uuid":"10"},{"query":"I want coke","uuid":"11"}],"batch":1,"total_batches":1,"skip_javascript":true})

};
request(options, function (error, response) { 
  if (error) throw new Error(error);
  console.log(response.body);
});

```

{% endtab %}
{% endtabs %}

### Response attributes

For each query, the query and the insights indicating how the user’s intent was analyzed and matched in the agent flow. See [insights](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/insights), for more information.

{% hint style="success" %}
**Key point**: Skill status in the insights objects can have the following values:

* complete: Skill is ready to be used.
* importing: Skill is being imported.
* publishing: Skill is being published.
* failed: Skill failed to import or copy.
* publish\_failed: Skill failed to publish.
* copying: Skill is being copied.
  {% endhint %}

### Example

The following is a sample POST request to test user queries:

```yaml
{
  "data": [
    {
      "query": "I want to order veg cheese pizza",
      "uuid": "10"
    },
    {
      "query": "I want coke",
      "uuid": "11"
    }
  ],
  "batch": 1,
  "total_batches": 1,
  "skip_javascript": true
}
```
