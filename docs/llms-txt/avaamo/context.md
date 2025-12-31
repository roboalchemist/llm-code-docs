# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context.md

# Context

Context object encapsulates various details of the user’s interaction with the agent at a particular instance in the agent's flow. **Example**: If a user’s intent is "I want to order cheese pan pizza", then broadly, a context object contains details of the user, agent, agent flow, and the intent applicable at that instance in the agent flow. In addition, it also contains details on the insights and history of agent conversation.

### Syntax

A context attribute can be accessed using **${context.<\<attributes>>}** in a text message or using **context.<\<attributes>>** in JavaScript.&#x20;

### Attributes

The following is a sample context JSON object:

{% hint style="info" %}
**Note:** In the JSON structure, ellipses (...) are used for brevity. Refer to individual sections for more information.
{% endhint %}

{% tabs %}
{% tab title="Structure" %}

```yaml
{
 "bot_id": 2154,
 "bot_layer_id": "fe8ee61c-f039-4cdc-8986-5bebec9edf08",
 "conversation_uuid": "1faa40c8253e65aa02bfd02fd8643d35",
 "user_uid": "dashboard_admin_test_user_696",
 "last_message": "i want to order cheese pan pizza",
 "visible_message": "i want to order cheese pan pizza",
 "last_message_timestamp": 1566205610480070,
 "last_message_custom_properties": {...},
 "message_uuid": "807dc584-1703-4b4e-b978-dce52a965e02",
 "device_uuid": "30809947-ec9a-4408-93ac-c7523d1f3058",
 "bot_name": "Mac Pizza",
 "bot_description": "order pizza and more",
 "is_validation_user": false,
 "phone": [...],
 "layer_id": "dashboard_admin_test_user_696",
 "last_name": "C",
 "first_name": "John",
 "custom_properties": {...},
 "<<env_variable>>": "https://cx.avaamo.com/v1/getdata.json",
 "email": [...],
 "location": [...],
 "organization": [...],
 "money": [...],
 "person": [...],
 "percent": [...],
 "url": [...],
 "credit_card": [...],
 "datetime": [...],
 "datetime_range": [...],
 "number": [...],
 "entities": {
 "<<slot_name_1>>": [...],
 "<<slot_name_2>>": [...]
},
 "stepmain": {
 "input": "reset"
 },
 "variables": {...},
 "user": {...},
 "constants": {...},
 "insights": {...},
 "intent_name": "order pizza",
 "history": [...],
 "is_agent_enabled": true
}
```

{% endtab %}

{% tab title="Example 1 " %}
&#x20;User query: I am very excited today I want to order pepper pan pizza. Where pepper and pan are both entity slots.

```javascript
{
  "bot_id": 4426,
  "bot_layer_id": "a5da2d81-9603-4316-beda-a7bb3ee9ebc1",
  "conversation_uuid": "e08b4ed471a08fb4e1afae4ced99b4f9",
  "user_uid": "dashboard_admin_test_user_12",
  "last_message": "I am very excited today I want to order pepper pan pizza",
  "visible_message": "I am very excited today I want to order pepper pan pizza",
  "last_message_timestamp": 1624871080666740,
  "last_message_custom_properties": {},
  "text": "I am very excited today I want to order pepper pan pizza",
  "message_uuid": "028ee78a-4193-44d0-9e07-c5344e304e7e",
  "device_uuid": "907847bf-8f49-4c29-b5ae-0c55cf490347",
  "bot_name": "MacPizza",
  "bot_description": "order pizza and more",
  "is_validation_user": false,
  "first_name": "John",
  "last_name": null,
  "layer_id": "dashboard_admin_test_user_12",
  "avatar": false,
  "avaamo_id": 22,
  "phone": [],
  "avatar_updated_at": null,
  "custom_properties": {},
  "email": [],
  "bot_inline_domain_5a3c0eb1-cbae-4167-9b9c-9fb255fe331d": {
    "pizza_types": [
      "veg"
    ],
    "pizza_toppings": [
      "pepper"
    ],
    "pizza_crust": [
      "pan"
    ]
  },
  "location": [],
  "organization": [],
  "money": [],
  "person": [],
  "percent": [],
  "url": [],
  "credit_card": [],
  "datetime": [
    1624881600000
  ],
  "datetime_range": [],
  "number": [],
  "entities": {
    "pizza_types": [
      "veg"
    ],
    "pizza_toppings": [
      "pepper"
    ],
    "pizza_crust": [
      "pan"
    ],
    "location": [],
    "organization": [],
    "money": [],
    "person": [],
    "percent": [],
    "email": [],
    "url": [],
    "credit_card": [],
    "phone": [],
    "datetime": [
      1624881600000
    ],
    "datetime_range": [],
    "number": []
  },
  "bot_inline_domain_d5fc76f2-03d8-4b06-8df0-3e53a7e28a89": {
    "pizza_types": [
      "veg"
    ],
    "pizza_toppings": [
      "pepper"
    ],
    "pizza_crust": [
      "pan"
    ]
  },
  "stepmain": {
    "input": "reset"
  },
  "step1": {
    "input": "I am very excited today I want to order pepper pan pizza"
  },
  "variables": {},
  "user": {
    "first_name": "John",
    "last_name": null,
    "layer_id": "dashboard_admin_test_user_12",
    "avatar": false,
    "avaamo_id": 22,
    "phone": null,
    "avatar_updated_at": null,
    "custom_properties": {}
  },
  "constants": {},
  "insights": {
    "analyzed_document": "I am very excited today I want to order pepper pan pizza",
    "document": "I am very excited today I want to order pepper pan pizza",
    "domain_ids": [
      13751
    ],
    "entities": [
      {
        "entity": "pizza_types",
        "entity_type": "pizza_types",
        "entity_value": "veg",
        "domain_key": "bot_inline_domain_5a3c0eb1-cbae-4167-9b9c-9fb255fe331d",
        "value": "veg",
        "current_value": "pepper",
        "index": 39,
        "derived_parent": true,
        "parent_entity_key": null,
        "custom_entity_type": true
      },
      {
        "entity": "pizza_toppings",
        "entity_type": "pizza_toppings",
        "entity_value": "pepper",
        "domain_key": "bot_inline_domain_5a3c0eb1-cbae-4167-9b9c-9fb255fe331d",
        "value": "pepper",
        "current_value": "pepper",
        "index": 39,
        "parent_entity_key": "pizza_types",
        "custom_entity_type": true
      },
      {
        "entity": "pizza_crust",
        "entity_type": "pizza_crust",
        "entity_value": "pan",
        "domain_key": "bot_inline_domain_5a3c0eb1-cbae-4167-9b9c-9fb255fe331d",
        "value": "pan",
        "current_value": "pan",
        "index": 47,
        "custom_entity_type": true
      }
    ],
    "featured_tokens": [
      "i",
      "am",
      "very",
      "excite",
      "today",
      "i",
      "want",
      "to",
      "order",
      "pepper",
      "pan",
      "pizza"
    ],
    "featured_tokens_lemma_map": {
      "am": "am",
      "excited": "excite",
      "i": "i",
      "order": "order",
      "pan": "pan",
      "pepper": "pepper",
      "pizza": "pizza",
      "to": "to",
      "today": "today",
      "very": "very",
      "want": "want"
    },
    "id": null,
    "lemma": "i am very excite today i want to order pepper pan pizza",
    "negation": false,
    "original_document": "I am very excited today I want to order pepper pan pizza",
    "pos": [
      [
        "i",
        "NN"
      ],
      [
        "am",
        "VBP"
      ],
      [
        "very",
        "RB"
      ],
      [
        "excited",
        "JJ"
      ],
      [
        "today",
        "NN"
      ],
      [
        "i",
        "VBP"
      ],
      [
        "want",
        "VBP"
      ],
      [
        "to",
        "TO"
      ],
      [
        "order",
        "NN"
      ],
      [
        "pepper",
        "NN"
      ],
      [
        "pan",
        "NN"
      ],
      [
        "pizza",
        "NN"
      ]
    ],
    "sentiment": "neutral",
    "tone": "Surprise",
    "raw_document": "I am very excited today I want to order pepper pan pizza",
    "bow_normalized_document_with_stopwords": "i very excite datetime want order randomA randomB pizza",
    "bow_normalized_document": "excite datetime want order randomA randomB pizza",
    "bow_words": [
      "want",
      "randomb",
      "randoma",
      "pizza",
      "order",
      "excite",
      "datetime"
    ],
    "normalized_document": "excite datetime want order randomA randomB pizza",
    "featured_normalized_tokens": "excite datetime want order randomA randomB pizza",
    "normalized_tokens": "excite datetime want order randomA randomB pizza",
    "multiIntentEligible": false,
    "bow_score": 1,
    "entities_already_processed": true,
    "intent": "node_intent_node_1",
    "intent_name": "MacPizza Order",
    "skill_name": "MacPizza Order",
    "score": 1,
    "es_score": 33.98229,
    "confidence_score": 0,
    "training_datum_id": 2130273,
    "intent_id": 81879,
    "intent_type": "INLINE::INTENT",
    "bot_key": "macpizza_order",
    "skill_key": "macpizza_order",
    "intent_key": "1",
    "matching_document": "I want to order pepper pan pizza",
    "second_best_result": null,
    "detected_language": "en-US",
    "original_text": "I am very excited today I want to order pepper pan pizza",
    "is_transaction": false
  },
  "response_filters": [],
  "intent_name": "MacPizza Order",
  "history": [],
  "is_agent_enabled": true
}
```

{% endtab %}

{% tab title="Example 2 " %}
User query: I want to travel by air and sea. Where air and sea are both entity slots.

```javascript
{
  "bot_id": 32745,
  "bot_layer_id": "039db95b-f27b-4ae3-8c89-fc529e32d772",
  "conversation_uuid": "bbf0d8d9491049750e87423a0dcb8063",
  "user_uid": "dashboard_admin_test_user_368",
  "last_message": "I want to travel via both air and sea",
  "visible_message": "I want to travel via both air and sea",
  "last_message_timestamp": 1624866162245929,
  "last_message_custom_properties": {},
  "text": "I want to travel via both air and sea",
  "message_uuid": "1ff21e25-a452-4739-8e41-94dac2a38e26",
  "device_uuid": "83133fee-79b0-497f-bc3d-10e568e05b89",
  "bot_name": "Travel assistant",
  "bot_description": "Travel assistant",
  "is_validation_user": false,
  "first_name": "John",
  "last_name": "Miller",
  "layer_id": "dashboard_admin_test_user_368",
  "avatar": false,
  "avaamo_id": 30572,
  "phone": [],
  "avatar_updated_at": null,
  "custom_properties": {},
  "email": [],
  "bot_inline_domain_7447fd52-19d1-493c-b1d1-c4552d5ad7e4": {
    "travel_modes_1": [
      "air"
    ],
    "travel_modes_2": [
      "sea"
    ]
  },
  "location": [],
  "organization": [],
  "money": [],
  "person": [],
  "percent": [],
  "url": [],
  "credit_card": [],
  "datetime": [],
  "datetime_range": [],
  "number": [],
  "entities": {
    "travel_modes_1": [
      "air"
    ],
    "travel_modes_2": [
      "sea"
    ],
    "location": [],
    "organization": [],
    "money": [],
    "person": [],
    "percent": [],
    "email": [],
    "url": [],
    "credit_card": [],
    "phone": [],
    "datetime": [],
    "datetime_range": [],
    "number": []
  },
  "bot_inline_domain_35ff647c-2031-4a4b-a78b-d850e99ee074": {
    "travel_modes_1": [
      "air"
    ],
    "travel_modes_2": [
      "sea"
    ]
  },
  "bot_inline_domain_71e3373f-b5f2-4de8-8ef6-d10dcdaf3618": {
    "travel_modes_1": [
      "air"
    ],
    "travel_modes_2": [
      "sea"
    ]
  },
  "bot_inline_domain_c60eeee0-4810-41b8-a9ac-bce503abd117": {
    "travel_modes_1": [
      "air"
    ],
    "travel_modes_2": [
      "sea"
    ]
  },
  "stepmain": {
    "input": "reset"
  },
  "step3": {
    "input": "I want to travel via both air and sea"
  },
  "variables": {},
  "user": {
    "first_name": "John",
    "last_name": "Miller",
    "layer_id": "dashboard_admin_test_user_368",
    "avatar": false,
    "avaamo_id": 30572,
    "phone": null,
    "avatar_updated_at": null,
    "custom_properties": {}
  },
  "constants": {},
  "insights": {
    "analyzed_document": "I want to travel via both air and sea",
    "document": "I want to travel via both air and sea",
    "domain_ids": [
      53292
    ],
    "entities": [
      {
        "entity_type": "travel_modes",
        "entity": "travel_modes_1",
        "entity_value": "air",
        "current_value": "air",
        "domain_key": "bot_inline_domain_7447fd52-19d1-493c-b1d1-c4552d5ad7e4",
        "value": "air"
      },
      {
        "entity_type": "travel_modes",
        "entity": "travel_modes_2",
        "entity_value": "sea",
        "current_value": "sea",
        "domain_key": "bot_inline_domain_7447fd52-19d1-493c-b1d1-c4552d5ad7e4",
        "value": "sea"
      }
    ],
    "featured_tokens": [
      "i",
      "want",
      "to",
      "travel",
      "via",
      "both",
      "air",
      "and",
      "sea"
    ],
    "featured_tokens_lemma_map": {
      "air": "air",
      "and": "and",
      "both": "both",
      "i": "i",
      "sea": "sea",
      "to": "to",
      "travel": "travel",
      "via": "via",
      "want": "want"
    },
    "id": null,
    "lemma": "i want to travel via both air and sea",
    "negation": false,
    "original_document": "I want to travel via both air and sea",
    "pos": [
      [
        "i",
        "NN"
      ],
      [
        "want",
        "VBP"
      ],
      [
        "to",
        "TO"
      ],
      [
        "travel",
        "VB"
      ],
      [
        "via",
        "IN"
      ],
      [
        "both",
        "DT"
      ],
      [
        "air",
        "NN"
      ],
      [
        "and",
        "CC"
      ],
      [
        "sea",
        "NN"
      ]
    ],
    "sentiment": "neutral",
    "tone": "",
    "raw_document": "I want to travel via both air and sea",
    "bow_normalized_document_with_stopwords": "want travel via both randomB and randomA",
    "bow_normalized_document": "want travel randomB randomA",
    "bow_words": [
      "want",
      "travel",
      "randomb",
      "randoma"
    ],
    "normalized_document": "want travel randomB randomA",
    "featured_normalized_tokens": "want travel randomB randomA",
    "normalized_tokens": "want travel randomB randomA",
    "multiIntentEligible": true,
    "bow_score": 1,
    "entities_already_processed": true,
    "intent": "node_intent_node_1",
    "intent_name": "Book Travel",
    "skill_name": "Book Travel",
    "score": 1,
    "es_score": 44.024994,
    "confidence_score": 0,
    "training_datum_id": 2187561,
    "intent_id": 272933,
    "intent_type": "INLINE::INTENT",
    "bot_key": "book_travel",
    "skill_key": "book_travel",
    "intent_key": "1",
    "matching_document": "I want to travel via both air and sea",
    "detected_language": "en-US",
    "original_text": "I want to travel via both air and sea",
    "is_transaction": false
  },
  "response_filters": [],
  "intent_name": "Book Travel",
  "history": [],
  "is_agent_enabled": true
}
```

{% endtab %}
{% endtabs %}

The following attributes are supported in the context object:

<table><thead><tr><th width="190.33333333333331">Attribute</th><th width="387">Description</th><th>Type</th></tr></thead><tbody><tr><td>bot_id</td><td>Indicates a unique identifier of the agent.</td><td>Integer</td></tr><tr><td>bot_layer_id</td><td>Indicates a unique agent identifier internally used by the Avaamo platform.</td><td>String</td></tr><tr><td>conversation_uuid</td><td>Indicates a unique identifier of conversation per user. Note that conversation/uuid is different for each user.</td><td>String</td></tr><tr><td>user_uid</td><td>Indicates a unique identifier of the user interacting with the agent.</td><td>String</td></tr><tr><td>last_message</td><td><p>Indicates the last message sent to the agent. For form fields, you can access last_message in one of the following ways:</p><ul><li>context.last_message.ID</li><li>context.last_message["ID"]</li><li>context.last_message[expression]</li></ul><p>Note that <strong>context.last_message</strong> can store any valid Javascript object.</p><p></p><p><strong>Examples</strong>:</p><p>// context.last_message.ID</p><p>context.last_message.da83d;</p><p></p><p>// context.last_message["ID"]</p><p>context.last_message["3a62c2"];</p><p></p><p>// context.last_message[expression]</p><p>var control = "3a62c2";</p><p>context.last_message[control];</p><p></p><p>See <a href="../how-to/build-dynamic-skill-response/card">Card</a>, for more details.</p></td><td>String</td></tr><tr><td>visible_message</td><td>Indicates the last visible message sent to the agent. Note that in case of hidden messages, visible and last messages can be different.</td><td>String</td></tr><tr><td>last_message_timestamp</td><td>Indicates timestamp of the last message sent by the user to the agent in milliseconds.</td><td>UTC Timestamp</td></tr><tr><td>last_message_custom_properties</td><td><p>Indicates any additional user properties specified in the last message. </p><p></p><p><strong>Example</strong>:</p><p>"custom_properties": {</p><p>"employee_id":12345,</p><p>"dept":"quality"</p><p>},</p></td><td>JSON key-value pairs</td></tr><tr><td>message_uuid</td><td>Indicates a unique identifier of the message.</td><td>String</td></tr><tr><td>device_uuid</td><td>Indicates a unique identifier of the device from which the agent is being used.</td><td>String</td></tr><tr><td>bot_name</td><td>Indicates the name of the agent specified during creation.</td><td>String</td></tr><tr><td>bot_description</td><td>Indicates the description of the agent specified during creation.</td><td>String</td></tr><tr><td>is_validation_user</td><td>Indicates if queries posted to the agent are from an actual user or from regression tests. Returns true, if the queries posted to the agent are from regression tests.</td><td>Boolean</td></tr><tr><td>phone</td><td><p>Indicates an array of phone numbers of the user interacting with the agent. </p><p></p><p><strong>Example</strong>: phone["+16503835663", "+919999988888"].</p></td><td>Array</td></tr><tr><td>layer_id</td><td>Indicates a unique user identifier internally used by the Avaamo platform.</td><td>String</td></tr><tr><td>last_name</td><td>Indicates the last name of the user interacting with the agent.</td><td>String</td></tr><tr><td>first_name</td><td>Indicates the first name of the user interacting with the agent.</td><td>String</td></tr><tr><td>custom_properties</td><td><p>Indicates any additional user properties specified when sending requests to the agent.</p><p></p><p><strong>Example</strong>:</p><p>"custom_properties": {</p><p>"employee_id":12345,</p><p>"dept":"quality"</p><p>},<br></p><p><strong>NOTE:</strong> If you have set custom user properties, then you can use <code>context.user.custom_properties.&#x3C;></code> to get the value of the set property.<br></p></td><td>JSON key-value pairs</td></tr><tr><td>environment variables</td><td>Indicates the environment variables configured in your agent.</td><td>JSON key-value pairs</td></tr><tr><td>email</td><td><p>Indicates an array of email Ids of the user interacting with the agent. </p><p></p><p><strong>Example</strong>: email["john@gmail.com", "john@hotmail.com"]</p></td><td>Array</td></tr><tr><td>location, organization, money, person, percent, URL, credit_card, DateTime, datetime_range, number</td><td>Indicates all the system entities that are predefined and available for all the agents. Note that values for these are populated as applicable during the execution of a user’s intent in the agent flow.</td><td>Array</td></tr><tr><td>entities -> &#x3C;&#x3C;slot_name>></td><td>Indicates slot names extracted and applicable during the execution of a user’s intent in the agent flow.</td><td>JSON with an array of slot_name as key-value pairs</td></tr><tr><td>step&#x3C;&#x3C;node>></td><td><p>Indicates the steps in the agent flow for which the user’s intent is executed. There can be multiple steps and each is specified as individual JSON key-value pairs.</p><p>&#x3C;&#x3C;node>> here refers to <strong>main</strong> for starting step or a specific node number. Example:</p><p>"step14": {</p><p> "input": "i want to order cheese pan pizza"</p><p> },</p></td><td>JSON key-value pairs</td></tr><tr><td><a href="context/variables">variables</a></td><td>Indicates the temporary variables that are defined to store information required for the agent flow at a particular node.</td><td>JSON key-value pairs</td></tr><tr><td><a href="context/user">user</a></td><td>Indicates the details of the user interacting with the agent.</td><td>JSON key-value pairs</td></tr><tr><td>constants</td><td><p>Indicates environment variables constants defined for the agent. These environment variables are global for all users of the agent. </p><p></p><p><strong>Examples</strong>: External service access credentials like web service login credentials, webservice_username, webservice_password.</p></td><td>JSON key-value pairs</td></tr><tr><td><a href="context/insights">insights</a></td><td>Indicates insights into how the user’s intent was analyzed and matched in the agent flow.</td><td>JSON key-value pairs</td></tr><tr><td><a href="context/history">history</a></td><td>Indicates the history of the message such as created date and time, actual message, and the sender of the message generated during the execution of the user’s intent in the agent flow.</td><td>JSON with an array of entity_name as key-value pairs</td></tr><tr><td>intent_name</td><td>Indicates the name of the intent that mapped to the user query.</td><td>String </td></tr><tr><td>is_agent_enabled</td><td>Indicates if the live agent is enabled or not for the agent.</td><td>Boolean</td></tr></tbody></table>

### When is the context reset?

* By default, the context is reset at the leaf node of the Dialog skill. However, if you wish to retain certain values, then you can consider using other storage options depending on the use case. See [Use storage](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/using-storage), for more information.
* If you wish to reset context in a non-leaf node, then you can use the **Reset Context** slider in the Skill Response -> Advanced Settings. See [Reset Context in Advanced Settings](https://docs.avaamo.com/user-guide/how-to/build-skills/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings#reset-context), for more information.
* Note that when you use `execute intent, goto node, or goto output`from the leaf node, then the context is not reset as the agent is still in the same transactional flow and context. Example: Consider that in the last post-processing node of the Pizza order flow, you have specified `return execute_intent('main','I want to check my order status')`. When the specified intent is executed at the transferred node, the previous context is still available.
