# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/conversation-message-api.md

# Conversation API

## Get conversation summary&#x20;

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/v1/conversations/{{conversation_uuid}}.json`

Gets the summary of a conversation using Conversation API. In the conversation summary, you can learn about the participants involved in the conversation and the last message of the conversation.

#### Path Parameters

| Name                                                 | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| conversation\_uuid<mark style="color:red;">\*</mark> | integer | <p>Conversation identifier. </p><p></p><p>You can get the conversation identifier from the <a href="../../../how-to/build-agents/debug-agents#using-conversation-history">Conversation history URL</a> or from the <a href="../message-api#get-agent-messages">Get Messages API</a> or from the message object when you are using the <a href="../../how-to/build-agents/configure-agents/deploy/web-channel/web-channel-callback-functions">Avaamo.onBotMessage callback function</a> in the Web channel.</p> |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                          |
| ---------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Device-Id<mark style="color:red;">\*</mark>    | number | Currently, this can be any random number such as 12345678.                                                                                                                                                                                                           |
| access-token<mark style="color:red;">\*</mark> | string | The agent access token. You can get the agent access token from the Agent -> Settings page. See [Agent Authentication Keys](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#agent-authentication-keys), for more information |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "conversation": {
        "uuid": "9e2484a9be77d54ef1b0b668231cc065",
        "mode": false,
        "members_type": 2,
        "avatar": false,
        "name": null,
        "created_at": 1582707000.0,
        "user": null,
        "receivers": [
            {
                "first_name": "MacPizza",
                "last_name": "",
                "layer_id": "a1148a3e-58ce-4cc6-9ea6-2c2d7b092730",
                "phone": null,
                "email": null,
                "avaamo_id": 3344,
                "avatar": false,
                "avatar_updated_at": null,
                "custom_properties": {},
                "display_name": "MacPizza ",
                "bot_user_info": []
            },
            {
                "first_name": "David",
                "last_name": "Miller",
                "layer_id": "dashboard_admin_test_user_163",
                "phone": null,
                "email": null,
                "avaamo_id": 1380,
                "avatar": false,
                "avatar_updated_at": null,
                "custom_properties": {
                    "email": "david@avaamo.com"
                },
                "display_name": "David Miller",
                "bot_user_info": [
                    {
                        "key": "email",
                        "bot_id": null,
                        "value": "david@avaamo.com"
                    }
                ]
            }
        ],
        "avatar_updated_at": null,
        "description": null,
        "last_message": {
            "uuid": "923cd3d7-3ecb-4aab-939c-2877406cb17a",
            "content": "Currently, you can place only online orders. Visit, www.macpizza.com, for more information.",
            "content_type": "text",
            "created_at": 1586255204.153764,
            "user": {
                "first_name": "MacPizza",
                "last_name": "",
                "layer_id": "a1148a3e-58ce-4cc6-9ea6-2c2d7b092730",
                "email": null,
                "phone": null,
                "avatar": false,
                "avatar_updated_at": null,
                "avaamo_id": 3344
            },
            "timetoken": 1586255204140986,
            "external_source": null,
            "device_uuid": "3c163171-9bec-492f-8448-685e9bfeffbc",
            "request_message_uuid": "2ac5917f-16d1-431f-883d-0a1c9d255658",
            "sequence": "1/1",
            "custom_properties": {
            },
            "agent_message_uuid": null,
            "read_acks": [
                {
                    "read_at": 1586255204.0,
                    "user": {
                        "first_name": "David",
                        "last_name": "Miller",
                        "layer_id": "dashboard_admin_test_user_163",
                        "email": null,
                        "phone": null,
                        "avatar": false,
                        "avatar_updated_at": null,
                        "avaamo_id": 1380
                    }
                }
            ],
            "attachments": [],
            "conversation": {
                "uuid": "9e2484a9be77d54ef1b0b668231cc065",
                "mode": false,
                "display_name": "MacPizza,David",
                "locale": null
            }
        },
        "members_count": 2
    }
}
```

{% endtab %}
{% endtabs %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/v1/conversations/xxxxxxae172c539696ff6f4f67xxxxxx.json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Device-Id: 12345667' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/v1/conversations/xxxxxxae172c539696ff6f4f67xxxxxx.json',
  'headers': {
    'Access-Token': 'xxxxxx8d9952499ea466fc007dxxxxxx',
    'Device-Id': '12345667',
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

<table><thead><tr><th width="155.33333333333331">Attribute</th><th width="360">Description</th><th>Type</th></tr></thead><tbody><tr><td>uuid</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>created_at</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td><a href="#receivers">receivers</a></td><td><p>Indicates the details of the participants in the conversation. </p><p>This is an array of two -</p><p>One with the details of the user and another the details of the agent in the conversation.</p></td><td>JSON key-value pairs</td></tr><tr><td><a href="#last_message">last_message</a></td><td>Indicates the details of the last message in the specified conversation.</td><td>JSON key-value pairs</td></tr></tbody></table>

#### receivers

Indicates the details of the participants in the conversation. This is an array of two - one with the details of the user and another with the details of the agent in the conversation.

<table><thead><tr><th width="198.33333333333331">Attribute</th><th width="455">Description</th><th>Type</th></tr></thead><tbody><tr><td><p></p><p>first_name</p></td><td>Indicates the first name of the user or agent participating in the conversation. </td><td>String</td></tr><tr><td>last_name</td><td>Indicates the last name of the user participating in the conversation. For agents, this field is null.</td><td>String</td></tr><tr><td>layer_id</td><td>Indicates a unique user or agent identifier internally used by the Avaamo Platform.</td><td>String</td></tr><tr><td>phone</td><td>Indicates an array of phone numbers of the user interacting with the agent.</td><td>Array</td></tr><tr><td>email</td><td>Indicates the email of the user interacting with the agent.</td><td>String</td></tr><tr><td>custom_properties</td><td><p>Indicates any additional custom properties of the user interacting with the agent.</p><p><strong>Example</strong>:</p><p>"custom_properties": {</p><p>"employee_id":12345,</p><p>"dept": "quality"</p><p>},</p></td><td>JSON key-value pairs</td></tr><tr><td>display_name</td><td>Indicates the display name of the user participating in the conversation. </td><td>String</td></tr></tbody></table>

#### **last\_message**

Indicates the last message of the specified conversation:

<table><thead><tr><th width="157.33333333333331">Attribute</th><th width="399">Description</th><th>Type</th></tr></thead><tbody><tr><td>uuid</td><td>Indicates a unique identifier of the message.</td><td>String</td></tr><tr><td>content</td><td>Indicates the content of the message.</td><td>String</td></tr><tr><td>content_type</td><td>Indicates the type of content such as text, ListView, card</td><td>String</td></tr><tr><td>created_at</td><td>Indicates the timestamp of when the message was created in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>user</td><td><p>Indicates the details of the user interacting with the agent.</p><ul><li><strong>phone</strong>: Indicates an array of phone numbers of the user interacting with the agent.</li><li><strong>layer_id</strong>: Indicates a unique user identifier internally used by the Avaamo Platform.</li><li><strong>last_name</strong>: Indicates the last name of the user interacting with the agent.</li><li><strong>first_name</strong>: Indicates the first name of the user interacting with the agent.</li><li><strong>email</strong>: Indicates the email of the user interacting with the agent.</li></ul></td><td>JSON key-value pairs</td></tr><tr><td>timetoken</td><td>Indicates the created timestamp of the message in milliseconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>device_uuid</td><td>Indicates a unique identifier of the device from which the agent is being used.</td><td>String</td></tr><tr><td>request_message_uuid</td><td>Indicates the message identifier from the agent to which this conversation is linked to.</td><td>String</td></tr><tr><td>sequence</td><td>Indicates the sequence of the agent response message. There can be multiple responses for a user query, each identified with the <strong>request_message_uuid</strong> and sequence. Note that the request_message_uuid is the same for each agent response.</td><td>&#x3C;&#x3C;message_sequence>>/&#x3C;&#x3C;total message></td></tr><tr><td>custom_properties</td><td><p>Indicates any additional user properties in the fetched message.</p><p><strong>Example</strong>:</p><p>"custom_properties": {</p><p>“employee_id”:12345,</p><p>“dept”: “quality”</p><p>},</p></td><td>JSON key-value pairs</td></tr><tr><td>read_acks</td><td><p>Indicates the details of when the message was read and acknowledged.</p><ul><li><strong>read_at</strong>: Indicates the read timestamp of the message in UNIX epoch format.</li><li><strong>user</strong>: Indicates the details of the user who acknowledged the message.</li></ul></td><td>An array of JSON key-value pairs</td></tr><tr><td>attachments</td><td>Indicates an array of attachments that is fetched from the agent message.</td><td>JSON key-value pairs</td></tr><tr><td>conversation</td><td><p>Indicates the conversation details of the message:</p><ul><li><strong>uuid</strong>: Indicates a unique identifier of the conversation.</li><li><strong>display_name</strong>: Indicates display name of the conversation in the following format: &#x3C;&#x3C;Agent Display Name>>, &#x3C;&#x3C;User First Name>>.</li><li><strong>locale</strong>: Indicates the locale used in the agent conversation.</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

## Get conversation messages&#x20;

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/v1/conversations/{{conversation_uuid}}/messages.json`

Gets the complete message details of a specific user conversation using Conversation Message API. \
All the conversation with an Avaamo agent has a conversation uuid associated with the conversation. In the message details, you can learn about the actual message content, type, identifier, and details of when the message was read and acknowledged.<br>

#### Path Parameters

| Name                                                 | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| conversation\_uuid<mark style="color:red;">\*</mark> | integer | <p>You can get the conversation identifier from the <a href="../../../how-to/build-agents/debug-agents#using-conversation-history">Conversation history URL </a>or from the <a href="../message-api#get-agent-messages">Get Messages API</a> or from the message object when you are using the <a href="../../how-to/build-agents/configure-agents/deploy/web-channel/web-channel-callback-functions">Avaamo.onBotMessage callback function</a> in the Web channel.<br></p> |

#### Query Parameters

| Name             | Type    | Description                                                                                                                                                                                                                    |
| ---------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| since\_timetoken | number  | <p>Timestamp from which the records are fetched. <br>If you specify timetoken and not since\_timetoken, then the latest 5 entries up to the specified timetoken are fetched. Specify UNIX Epoch Timestamp in microseconds.</p> |
| timetoken        | number  | Timestamp until which the records are fetched. The default value is the current timestamp. Specify UNIX Epoch Timestamp in microseconds.                                                                                       |
| page             | integer | Page from which the entries must be fetched. The default value is 1.                                                                                                                                                           |
| per\_page        | integer | <p>The number of entries fetched per page. <br>Default value: 25</p><p>Maximum: 100</p>                                                                                                                                        |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                           |
| ---------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Device-Id<mark style="color:red;">\*</mark>    | string | Currently, this can be any random identifier such as 12345678.                                                                                                                                                                                                        |
| access-token<mark style="color:red;">\*</mark> | string | The agent access token. You can get the agent access token from the Agent -> Settings page. See [Agent Authentication Keys](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/define-settings#agent-authentication-keys), for more information. |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "current_page": 1,
    "per_page": 1,
    "total_entries": 66,
    "total_pages": 66,
    "time_token": 1586147024.9868526,
    "entries": [
        {
            "uuid": "251c8106-2e06-422c-9495-11c9878b9289",
            "content": "Chez MacPizza, nous avons utilisé des ingrédients biologiques fraîchement préparés dans toutes nos recettes.",
            "content_type": "text",
            "created_at": 1582737781.470828,
            "user": {
                "first_name": "MacPizza",
                "last_name": "",
                "layer_id": "a1148a3e-58ce-4cc6-9ea6-2c2d7b092730",
                "email": null,
                "phone": null,
                "avatar": false,
                "avatar_updated_at": null,
                "avaamo_id": 3344
            },
            "timetoken": 1582737781457202,
            "external_source": null,
            "device_uuid": "3c163171-9bec-492f-8448-685e9bfeffbc",
            "request_message_uuid": "f6850f78-a869-403c-b765-20b546343ea6",
            "sequence": "1/1",
            "custom_properties": {},
            "agent_message_uuid": null,
            "read_acks": [
                {
                    "read_at": 1582737781.0,
                    "user": {
                        "first_name": "David",
                        "last_name": "Miller",
                        "layer_id": "dashboard_admin_test_user_163",
                        "email": null,
                        "phone": null,
                        "avatar": false,
                        "avatar_updated_at": null,
                        "avaamo_id": 1380
                    }
                }
            ],
            "attachments": [],
            "conversation": {
                "uuid": "9e2484a9be77d54ef1b0b668231cc065",
                "mode": false,
                "display_name": "MacPizza,David",
                "locale": null
            }
        }
    ]
}
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Note**: For optimal API performance, the recommended time duration for fetching data from any of the REST APIs that support a date range or time period is 7 days.
{% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/v1/conversations/7db4d0ae172c539696ff6f4f676f2222/messages.json?page=2&per_page=55' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Device-Id: 12345667' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/v1/conversations/xxxxxxae172c539696ff6f4f67xxxxxx/messages.json?page=2&per_page=55',
  'headers': {
    'Access-Token': 'xxxxxx8d9952499ea466fc007dxxxxxx',
    'Device-Id': '12345667',
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

<table><thead><tr><th width="159.33333333333331">Attribute</th><th>Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td><a href="../message-api#entries">entries</a></td><td><p>Indicates an array of messages fetched from the agent. </p><p>The number of entries in the array = Number specified in the per_page parameter.</p></td><td>JSON key-value pairs</td></tr></tbody></table>

#### **entries**

Indicates an array of messages fetched from the agent. Each array contains the following attributes:

<table><thead><tr><th width="160.33333333333331">Attribute</th><th>Description</th><th>Type</th></tr></thead><tbody><tr><td>uuid</td><td>Indicates a unique identifier of the message.</td><td>String</td></tr><tr><td>content</td><td>Indicates the content of the message.</td><td>String</td></tr><tr><td>content_type</td><td>Indicates the type of content such as text, ListView, card</td><td>String</td></tr><tr><td>created_at</td><td>Indicates the timestamp of when the message was created in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>user</td><td><p>Indicates the details of the user interacting with the agent.</p><ul><li><strong>phone</strong>: Indicates an array of phone numbers of the user interacting with the agent.</li><li><strong>layer_id</strong>: Indicates a unique user identifier internally used by the Avaamo Platform.</li><li><strong>last_name</strong>: Indicates the last name of the user interacting with the agent.</li><li><strong>first_name</strong>: Indicates the first name of the user interacting with the agent.</li><li><strong>email</strong>: Indicates the email of the user interacting with the agent.</li></ul></td><td>JSON key-value pairs</td></tr><tr><td>timetoken</td><td>Indicates the created timestamp of the message in milliseconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>device_uuid</td><td>Indicates a unique identifier of the device from which the agent is being used.</td><td>String</td></tr><tr><td>request_message_uuid</td><td>Indicates the message identifier from the agent for which this conversation is linked to. For a live agent conversation message, request_message_uuid is null.</td><td>String</td></tr><tr><td>sequence</td><td>Indicates the sequence of the agent response message. There can be multiple responses for a user query, each identified with the <strong>request_message_uuid</strong> and sequence. Note that the request_message_uuid is the same for each agent response.</td><td>&#x3C;&#x3C;message_sequence>>/&#x3C;&#x3C;total message></td></tr><tr><td>custom_properties</td><td><p>Indicates any additional user properties in the fetched message.</p><p><strong>Example</strong>:</p><p>"custom_properties": {</p><p>“employee_id”:12345,</p><p>“dept”: “quality”</p><p>},</p></td><td>JSON key-value pairs</td></tr><tr><td>agent_message_uuid</td><td>Indicates the unique identifier for a live agent conversation. </td><td>String</td></tr><tr><td>read_acks</td><td><p>Indicates the details of when the message was read and acknowledged.</p><ul><li><strong>read_at</strong>: Indicates the read timestamp of the message in UNIX epoch format.</li><li><strong>user</strong>: Indicates the details of the user who acknowledged the message.</li></ul></td><td>An array of JSON key-value pairs</td></tr><tr><td>attachments</td><td>Indicates an array of attachments that is fetched from the agent message.</td><td>JSON key-value pairs</td></tr><tr><td>conversation</td><td><p>Indicates the conversation details of the message:</p><ul><li><strong>uuid</strong>: Indicates a unique identifier of the conversation.</li><li><strong>display_name</strong>: Indicates display name of the conversation in the following format: &#x3C;&#x3C;Agent Display Name>>, &#x3C;&#x3C;User First Name>>.</li><li><strong>locale</strong>: Indicates the locale used in the agent conversation.</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="244.57142857142856">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get the latest message of a  user conversation </td><td><p><strong>per_page</strong>: Specify 1 to get the latest message. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/v1/conversations/</code></p><p><code>&#x3C;&#x3C;conversation_uuid>>/messages.json?per_page=1</code></p></td></tr><tr><td>Get messages of a user conversation within a specified period</td><td><p><strong>since_timetoken</strong>: Specify the <strong>from</strong> timestamp in epoch format such as 1569229247677821</p><p><strong>timetoken</strong>: Specify the <strong>to</strong> timestamp in epoch format such as 1569229251418739. </p><p></p><p><strong>Example</strong>: </p><p><code>https://cx.avaamo.com/v1/conversations/</code></p><p><code>&#x3C;&#x3C;conversation_uuid>>/messages.json?since_timetoken=1569229247677821&#x26;timetoken=1569229251418739</code></p></td></tr><tr><td>Get messages of a user conversation using pagination</td><td><p><strong>page</strong>: Specify the page from which you wish to fetch records. </p><p><strong>per_page</strong>: Specify the number of entries per page. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/v1/conversations/</code></p><p><code>&#x3C;&#x3C;conversation_uuid>>/messages.json?page=5&#x26;per_page=2</code></p></td></tr></tbody></table>
