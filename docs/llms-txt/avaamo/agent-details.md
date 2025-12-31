# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/agent-details.md

# Agent details

### Get agent details

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}.json`

Get the agent details such as agent identifier, agent description, skills, entities used across all the skills, dictionaries, and list of entity types available in the agent.

#### Path Parameters

<table><thead><tr><th width="131.7637939453125">Name</th><th width="133.8895263671875">Type</th><th>Description</th></tr></thead><tbody><tr><td>agent_id<mark style="color:red;">*</mark></td><td>integer</td><td><p>Agent identifier. </p><p></p><p>You can get the agent identifier from the agent URL. </p></td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="144.37615966796875">Name</th><th width="115.10113525390625">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td><p>User access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. Users must have at least view permission on the agent. </p><p></p><p>See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p></td></tr></tbody></table>

{% tabs %}
{% tab title="200 Success" %}

```javascript
{
  "agent": {
    "id": 20457,
    "description": "For ordering pizzas and more",
    "display_name": "Mac Pizza - New",
    "created_at": 1590390902,
    "updated_at": 1590666408,
    "entities": [
      {
        "id": 102350,
        "name": "phonenumber",
        "entity_type": "phone_number",
        "entity_type_id": 21664,
        "skill_ids": [
          17825,
          17826,
          17830
        ]
      },
      {
        "id": 102357,
        "name": "ordernumber",
        "entity_type": "order_number",
        "entity_type_id": 21665,
        "skill_ids": [
          17825,
          17826,
          17830
        ]
      },
      {
        "id": 103095,
        "name": "starters",
        "entity_type": "starters",
        "entity_type_id": 21810,
        "skill_ids": [
          17825,
          17826,
          17830
        ]
      },
      {
        "id": 103647,
        "name": "pizza_type_1",
        "entity_type": "pizza_type",
        "entity_type_id": 21661,
        "skill_ids": [
          17828,
          17825,
          17826,
          17830
        ]
      },
      {
        "id": 103648,
        "name": "pizza_toppings_1",
        "entity_type": "pizza_toppings",
        "entity_type_id": 21662,
        "skill_ids": [
          17828,
          17825,
          17826,
          17830
        ]
      }
    ],
    "entity_types": [
      {
        "id": 21661,
        "key": "pizza_type",
        "name": "pizzatype",
        "description": "Types of pizza",
        "regex": false
      },
      {
        "id": 21662,
        "key": "pizza_toppings",
        "name": "pizza toppings",
        "description": "Toppings for veg and non-veg pizza",
        "regex": false
      },
      {
        "id": 21664,
        "key": "phone_number",
        "name": "phone number",
        "description": "phone number",
        "regex": true
      },
      {
        "id": 21665,
        "key": "order_number",
        "name": "Order number",
        "description": "Order number",
        "regex": true
      },
      {
        "id": 21810,
        "key": "starters",
        "name": "Starters",
        "description": "Starters",
        "regex": false
      }
    ],
    "dictionaries": [
      {
        "id": 755,
        "name": "Business words",
        "description": "Business words",
        "updated_at": 1590396449,
        "created_at": 1590396449
      }
    ],
    "skills": [
      {
        "id": 17825,
        "name": "MacPizza Policy",
        "type": "document-knowledge",
        "source_id": 5492,
        "created_at": 1590390903,
        "updated_at": 1590390909,
        "status": "complete"
      },
      {
        "id": 17826,
        "name": "MacPizza FAQs",
        "type": "knowledge",
        "source_id": 5493,
        "created_at": 1590390904,
        "updated_at": 1590390909,
        "status": "complete"
      },
      {
        "id": 17828,
        "name": "MacPizza Order",
        "type": "dialog",
        "source_id": 20459,
        "created_at": 1590390904,
        "updated_at": 1590391698,
        "status": "complete"
      },
      {
        "id": 17830,
        "name": "custom",
        "type": "smalltalk-knowledge",
        "source_id": 5494,
        "created_at": 1590390905,
        "updated_at": 1590390909,
        "status": "complete"
      }
    ],
    "information_masking": {
            "realtime_masking_enabled": true,
            "api_masking_enabled": false,
            "retention_period": 2,
            "mask_files": true,
            "mask_responses_from_all_nodes": true,
            "system_entity_types": [
                "date",
                "email",
                "person",
                "phone",
                "ssn",
                "location"
            ],
            "custom_entity_types": [],
            "masking_patterns": "",
            "response_masking_patterns": "",
            "user_properties": [
                "first_name",
                "last_name",
                "phone",
                "ssn"
            ],
            "updated_at": 1744640124.0
        },
        "language_packs": [
            {
                "id": 402579,
                "language": "kn-IN",
                "default": false
            },
            {
                "id": 402580,
                "language": "fr-FR",
                "default": false
            }
        ]
      }
}
```

{% endtab %}
{% endtabs %}

#### Path Parameters

#### Headers

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/api/v1/agents/20xxx.json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v1/agents/204xxx.json',
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

In the response, you can get the following details about the agent:

<table><thead><tr><th width="189.56974552121983">Attribute</th><th width="338.3433835663669">Description</th><th>Type</th></tr></thead><tbody><tr><td>id</td><td>Indicates the unique agent identifier.</td><td>Integer</td></tr><tr><td>description</td><td>Indicates the description given for the agent.</td><td>String</td></tr><tr><td>display_name</td><td>Indicates the display name of the agent.</td><td>String</td></tr><tr><td>created_at</td><td>Indicates the timestamp of when the agent was created in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>updated_at</td><td>Indicates the timestamp of when the agent was updated in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>entities</td><td><p>Indicates a list of entities used in intents across all the agent skills. Each entry contains the following details: </p><ul><li>id: Internal identifier used by the Platform.</li><li>name: Entity name given in the dialog skill,</li><li>entity_type: Name of the entity type this entity is linked to.</li><li>entity_type_id: Unique identifier of the entity type this entity is linked to.</li><li>skill_ids: Array of skills where the entity is used.</li></ul></td><td>JSON key-value pairs</td></tr><tr><td>dictionaries</td><td><p>Indicates an array of all the dictionaries in the agent. Each entry contains the following details: </p><ul><li>id: Unique dictionary identifier</li><li>name: Name of the dictionary.</li><li>description: Description given for the dictionary.</li><li>created_at: Timestamp of when the dictionary was created in seconds (UNIX epoch timestamp).</li><li>updated_at: Timestamp of when the dictionary was updated in seconds (UNIX epoch timestamp).</li></ul></td><td>JSON key-value pairs</td></tr><tr><td>skills</td><td><p>Indicates an array of all the skills (enabled or disabled) in the agent. Each entry contains the following details: </p><ul><li>id: Internal identifier used by the Platform.</li><li>name: Name of the skill</li><li><p>type: Type of skill. The following are the types:</p><ul><li>dialog: <a href="../../../how-to/build-skills/create-skill/using-dialog-designer">Dialog skill</a></li><li>knowledge: <a href="../../../how-to/build-skills/create-skill/using-q-and-a-designer">Q&#x26;A skill</a></li><li>knowledge-v2: <a href="../../../how-to/build-skills/create-skill/dynamic-q-and-a">Dynamic Q&#x26;A skill</a></li><li>answers_pluggable_skill: <a href="../../../how-to/build-skills/create-skill/using-avaamo-answers-1">Answers skill</a></li><li>smalltalk-knowledge: <a href="../../../how-to/build-skills/create-skill/using-smalltalk">Smalltalk skill</a></li><li>llamb_content_skill: <a href="../../../llamb/get-started">LLaMB Content skill</a></li></ul></li><li>source_id: Unique skill identifier.</li><li>created_at: Timestamp of when the skill was created in seconds (UNIX epoch timestamp).</li><li>updated_at: Timestamp of when the skill was updated in seconds (UNIX epoch timestamp).</li><li><p>status: Current state of the skill.</p><ul><li>complete: Skill is ready to be used.</li><li>importing: Skill is being imported.</li><li>publishing: Skill is being published.</li><li>failed: Skill failed to import or copy</li><li>publish_failed: Skill failed to publish.</li><li>copying: Skill is being copied.</li></ul></li></ul><p>  </p></td><td>JSON key-value pairs</td></tr><tr><td>entity_types</td><td><p>Indicates an array of all the custom entity types in the agent. </p><p>Each entry contains the following details: </p><ul><li>id: Unique identifier for the entity type.</li><li>key: Key given for the entity type at the time of creation.</li><li>name: Name of the entity type.</li><li>description: Description of the entity type.</li><li>regex: Indicates if this is a regular expression entity or not.</li></ul></td><td>JSON key-value pairs</td></tr><tr><td>information_masking</td><td><p>Indicates the masking configuration details, if information masking is enabled for the agent: </p><ul><li>realtime_masking_enabled: Indicates if masking in real-time is enabled or not for the agent.</li><li>api_masking_enabled: Indicates if masking via API is enabled or not for the agent.</li><li>retention_period: Indicates the set retention period for the agent in minutes.</li><li>mask_files: Indicates if file masking is enabled or not.</li><li>mask_responses_from_all_nodes: Indicates if masking responses from all nodes is enabled or not for the agent.</li><li>system_entity_types: Array of system entity types that are masked. </li><li>custom_entity_types: Array of custom entity types that are masked.</li><li>masking_patterns: Array of regular expression patterns that are masked in a user query.</li><li>response_masking_patterns: Array of regular expression patterns that must be masked in the agent response.</li><li>user_properties: An Array of user attributes that are masked</li><li>updated_at: Indicates the timestamp of when the masking details were updated in seconds. (UNIX epoch timestamp).</li></ul><p>See <a href="../../../overview-and-concepts/advanced-concepts/information-masking">Information masking</a>, for more information.</p></td><td>JSON key-value pairs</td></tr><tr><td>language_packs</td><td><ul><li>id: Internal identifier used by the Platform.</li><li>language: Name of the language </li><li>default: Indicates whether it is the default language.</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>
