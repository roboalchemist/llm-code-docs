# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/q-and-a-intents.md

# Q\&A intents

## Get Q\&A intents

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}/intents/qna.json`

Get a list of all the Q\&A intents from the agent.&#x20;

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

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| access-token<mark style="color:red;">\*</mark> | string | <p>User access token. You can get the user access token from the Settings -> Users and Roles page. See <a href="../../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least view permission on the agent. See <a href="../../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "current_page": 1,
    "per_page": 1,
    "total_entries": 3,
    "total_pages": 3,
    "time_token": 1590483068.2610612,
    "intents": [
        {
            "id": 185260,
            "name": "store",
            "created_at": 1590390904.0,
            "updated_at": 1590390904.0,
            "skill": {
                "id": 17826,
                "name": "MacPizza FAQs",
                "type": "knowledge",
                "source_id": 5493,
                "created_at": 1590390904.0,
                "updated_at": 1590390909.0,
                "status": "complete"
            },
            "training_data": [
                {
                    "id": 1161932,
                    "created_at": 1590390904.0,
                    "value": "where is your store?",
                    "slots": []
                },
                {
                    "id": 1161933,
                    "created_at": 1590390904.0,
                    "value": "do you have any branches?",
                    "slots": []
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
curl --location --request GET 'https://cx.avaamo.com/api/v1/agents/20xxx/intents/qna.json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v1/agents/20xxx/intents/qna.json',
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

<table><thead><tr><th>Attribute</th><th width="386.4039641340255">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the response.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td>intents</td><td><p>Indicates an array of Q&#x26;A intents from the agent. Number of entries in the array = Number specified in per_page parameter. </p><p></p><p>Each intent entry contains the following details: </p><ul><li>id: Unique intent identifier</li><li>name: Name of the intent</li><li>created_at: Indicates the timestamp of when the intent was created in seconds. (UNIX Epoch Timestamp)</li><li>updated_at: Indicates the timestamp of when the intent was updated in seconds. (UNIX Epoch Timestamp)</li><li><p>skill: Indicates the following skill details:</p><ul><li>id: Internal identifier used by the Platform</li><li>name: Name of the skill</li><li><p>type: Type of the skill. </p><ul><li>knowledge: <a href="../../../how-to/build-skills/create-skill/using-q-and-a-designer">Q&#x26;A skill</a></li><li>knowledge-v2: <a href="../../../how-to/build-skills/create-skill/dynamic-q-and-a">Dynamic Q&#x26;A skill</a></li></ul></li><li>source_id: Unique identifier for the skill</li><li>created_at: Timestamp of when the skill was created in seconds (UNIX epoch timestamp).</li><li>updated_at: Timestamp of when the skill was updated in seconds (UNIX epoch timestamp).</li><li><p>status: Skill status can have the following values:</p><ul><li>complete: Skill is ready to be used.</li><li>importing: Skill is being imported.</li><li>publishing: Skill is being published.</li><li>failed: Skill failed to import or copy.</li><li>publish_failed: Skill failed to publish.</li><li>copying: Skill is being copied.</li></ul></li></ul></li><li><p>training_data: Indicates an array of training data as applicable to the intent. Each training data contains the following details:</p><ul><li>id: Internal identifier used by the Platform.</li><li>created_at: Timestamp of when training data was created in seconds (UNIX epoch timestamp).</li><li>value: Actual training data value specified for the intent,</li></ul></li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="150">Use-case</th><th width="478.65664056339597">Query Parameter</th></tr></thead><tbody><tr><td>Get Q&#x26;A intents from agent using pagination</td><td><p><strong>page</strong>: Specify the page from which you wish to fetch records. </p><p><strong>per_page</strong>: Specify the number of entries per page. </p><p></p><p><strong>Example</strong>:  <code>https://cx.avaamo.com/api/v1/agents/&#x3C;&#x3C;agent_id>>/intents/qna.json per_page=2&#x26;page=5</code></p></td></tr></tbody></table>
