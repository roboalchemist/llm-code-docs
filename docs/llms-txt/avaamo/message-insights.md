# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/message-insights.md

# Message insights

## Get query insights by message ID

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}/query_insights/{{message_id}}.json`

Get a closer look at the insights of the message.

#### Path Parameters

<table><thead><tr><th width="169">Name</th><th width="138">Type</th><th>Description</th></tr></thead><tbody><tr><td>agent_id<mark style="color:red;">*</mark></td><td>integer</td><td>Agent identifier. You can get the agent identifier from the agent URL. </td></tr><tr><td>message_id<mark style="color:red;">*</mark></td><td>alphanumeric</td><td>Message identifier. You can get the message identifier from any other API response. For example, Message UUID in the custom channel response.</td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="174">Name</th><th width="109">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td><p>User access token. </p><p></p><p>You can get the user access token from the <strong>Settings -> Users</strong> page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information </p></td></tr></tbody></table>

{% tabs %}
{% tab title="200 " %}
{% code overflow="wrap" %}

```json
{
  "insight": {
    "intent_type": "INLINE::INTENT",
    "skill_name": "Macpizza Order",
    "skill_key": "macpizza_order",
    "intent_name": "Macpizza Order",
    "intent_key": "pizza_toppings",
    "node_key": "macpizza_order.pizza_toppings",
    "original_text": "I want to order veg cheese pizza",
    "document": "I want to order veg cheese pizza",
    "entities": [
      {
        "entity": "pizza_toppings",
        "entity_type": "pizza_toppings",
        "entity_value": "cheese",
        "domain_key": "bot_inline_domain_bee25dca-3b9f-46eb-a456",
        "value": "cheese",
        "current_value": "cheese",
        "index": 20,
        "parent_entity_key": "pizza_types",
        "custom_entity_type": true
      }
    ],
    "negation": false,
    "sentiment": "neutral",
    "tone": "",
    "detected_language": "English(en-US)",
    "second_best_result": null,
    "matching_document": "I want to order veg cheese pizza"
  }
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```javascript
curl --location 'https://cx.avaamo.com/api/v1/agents/30xxx/query_insights/77851a10-xxxx-xxxx-xxxx-a1c16f4904ad.json' \
--header 'access-token: 8cexxxxxxxxxxxxxxx47ccd9e60f3bd5'
```

{% endcode %}
{% endtab %}

{% tab title="node.js" %}
{% code overflow="wrap" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v1/agents/30xxx/query_insights/777851a10-xxxx-xxxx-xxxx-a1c16f4904ad.json',
  'headers': {
    'access-token': '8cexxxxxxxxxxxxxxx47ccd9e60f3bd5'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});


```

{% endcode %}
{% endtab %}
{% endtabs %}

### Response attributes

In the response, the following attributes are returned:

```json
{
  "insight": {
    "intent_type": "INLINE::INTENT",
    "skill_name": "Macpizza Order",
    "skill_key": "macpizza_order",
    "intent_name": "Macpizza Order",
    "intent_key": "pizza_toppings",
    "node_key": "macpizza_order.pizza_toppings",
    "original_text": "I want to order veg cheese pizza",
    "document": "I want to order veg cheese pizza",
    "entities": [
      {
        "entity": "pizza_toppings",
        "entity_type": "pizza_toppings",
        "entity_value": "cheese",
        "domain_key": "bot_inline_domain_bee25dca-3b9f-46eb-a456",
        "value": "cheese",
        "current_value": "cheese",
        "index": 20,
        "parent_entity_key": "pizza_types",
        "custom_entity_type": true
      }
    ],
    "negation": false,
    "sentiment": "neutral",
    "tone": "",
    "detected_language": "English(en-US)",
    "second_best_result": null,
    "matching_document": "I want to order veg cheese pizza"
  }
}
```

<table><thead><tr><th width="123.91519923365865">Attribute</th><th width="480.74249584282035">Description</th><th>Type</th></tr></thead><tbody><tr><td>insight</td><td>See <a href="../../../how-to/build-skills/create-skill/customize-your-skill/reference-library/context/insights">insights</a>, for more information on each attribute.</td><td>Integer</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="264">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get message insights for an agent</td><td><p><strong>agent_id</strong>: Specify the agent identifier</p><p><strong>message_id</strong>: Specify the message identifier for which you wish to view the insights.</p></td></tr></tbody></table>
