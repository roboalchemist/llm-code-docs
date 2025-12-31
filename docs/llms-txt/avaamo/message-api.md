# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/message-api.md

# Message API

## Post agent messages&#x20;

<mark style="color:green;">`POST`</mark> `https://cx.avaamo.com/bots_api/v1/messages.json`

Post messages to the agent. Typically, this API is used when you wish to post agent responses for notifications, summary, and important product or service announcements.

#### Headers

<table><thead><tr><th width="207">Name</th><th width="118">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td><p>The user access token. <br>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information </p><p></p><p>User must have at least edit permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information<br></p></td></tr></tbody></table>

#### Request Body

<table><thead><tr><th width="207">Name</th><th width="122">Type</th><th>Description</th></tr></thead><tbody><tr><td>message<mark style="color:red;">*</mark></td><td>string</td><td>The message you wish to post to the agent. <br>This can be any message as supported by the channel. </td></tr><tr><td>conversation -> uuid<mark style="color:red;">*</mark></td><td>string</td><td>Unique identifier of the conversation for which the message is posted. You can get the conversation uuid from the Conversation History URL</td></tr><tr><td>bot_id<mark style="color:red;">*</mark></td><td>integer</td><td>Unique identifier of the agent. <br>You can get the agent identifier from the agent URL.</td></tr><tr><td>force_locale</td><td>string</td><td>The locale used to override the locale of the agent. </td></tr></tbody></table>

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "success": true
}
```

{% endtab %}
{% endtabs %}

{% hint style="success" %}
**Key point**: See [Supported agent responses](applewebdata://E3416F10-9D83-4DB7-B173-CC5D7BD95AFE/@avaamo/s/avaamo/~/drafts/-M8iZKLHjv_ONgUq4a3a/v/dev/how-to/build-agents/configure-agents/deploy/custom-channel#supported-agent-responses) in the Custom channel, for more information on WhatsApp-compatible responses.
{% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request POST 'https://cx.avaamo.com/bots_api/v1/messages.json' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: text/plain' \
--data-raw '{
  "message": "Sample message",
  "conversation": {
    "uuid": "xxxxxx8253e65aa02bfd02fd86xxxxxx"
  },
  "bot_id": 2xxx,
  "force_locale": "en"
}'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://cx.avaamo.com/bots_api/v1/messages.json',
  'headers': {
    'Content-Type': ['application/json', 'text/plain'],
    'Access-Token': 'xxxxxx8d9952499ea466fc007dxxxxxx'
  },
  body: "{\n  \"message\": \"Sample message\",\n  \"conversation\": {\n    \"uuid\": \"xxxxxx8253e65aa02bfd02fd86xxxxxx\"\n  },\n  \"bot_id\": 2xxx,\n  \"force_locale\": \"en\"\n}"

};
request(options, function (error, response) { 
  if (error) throw new Error(error);
  console.log(response.body);
});

```

{% endtab %}
{% endtabs %}

### Examples

#### **Scenario 1**: Post a **simple message**

**Request**: The following is a sample JSON request for posting a simple message to the agent:

```yaml
{
  "message": "Sample message",
  "conversation": {
    "uuid": "xxxxxx8253e65aa02bfd02fd86xxxxxx"
  },
  "bot_id": 2xxx,
  "force_locale": "en"
}
```

The message as sent in the request is posted to the agent. You can also view the same message in the conversation for which the message is posted:

#### ![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FZUHbxqJGMSdvwaNPsBoJ%2Fimage.png?alt=media\&token=ee68de2f-d9a9-401f-9b9b-53fa0a85ceec)

#### **Scenario 2**: Post a list of promotional items

**Request**: The following is a sample JSON request for posting a list of promotional items to the agent:

```yaml
{
  "message": {
    "list_view": {
      "top_element_style": "compact",
      "items": [
        {
          "title": "Coke",
          "subtitle": "All Chilled",
          "links": [
            {
              "type": "post_message",
              "title": "Get a pack of 5",
              "value": "coke"
            }
          ]
        },
        {
          "title": "Coffee",
          "subtitle": "Cold",
          "links": [
            {
              "type": "post_message",
              "title": "Buy one get one",
              "content": "coffee"
            }
          ]
        }
      ]
    }
  },
  "conversation": {
    "uuid": "1faa40c8253e65aa02bfd02fd8643d35"
  },
  "bot_id": 2154,
  "force_locale": "en"
}
```

The following response is displayed in the agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fsxzfwa7zriGuDQKZOgIG%2Fimage.png?alt=media\&token=877e07ff-04ed-4bd2-8193-735f31711809)

**Scenario 3**: Post a feedback message

**Request**: The following is a sample JSON request for posting a feedback message to the agent:

```yaml
{
  "message": {
    "card": {
      "inputs": [
        {
          "title": "How was our service?",
          "type": "data_capture",
          "uuid": "comments"
        }
      ]
    }
  },
  "conversation": {
    "uuid": "xxxxxx8253e65aa02bfd02fd86xxxxxx"
  },
  "bot_id": 2xxx,
  "force_locale": "en"
}
```

## Get agent messages&#x20;

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/v1/messages.json`

Gets all messages from the agent. This API just gets the latest messages from the agent and not specific to any user conversation.&#x20;

#### Query Parameters

<table><thead><tr><th width="185">Name</th><th width="117">Type</th><th>Description</th></tr></thead><tbody><tr><td>device_info</td><td>boolean</td><td>Indicates if the device details must be returned in the response or not. The default value is false.</td></tr><tr><td>since_timetoken</td><td>number</td><td>Timestamp from which the records are fetched. <br>If you specify timetoken and not since_timetoken, then the latest 5 entries up to the specified timetoken are fetched. Specify in UNIX Epoch Timestamp in microseconds.</td></tr><tr><td>timetoken</td><td>number</td><td>Timestamp until which the records are fetched. The default value is the current timestamp. Specify in UNIX Epoch Timestamp in microseconds.</td></tr><tr><td>page</td><td>integer</td><td><p>Page from which the entries must be fetched. </p><p></p><p>The default value is 1.</p></td></tr><tr><td>per_page</td><td>integer</td><td><p>The number of entries fetched per page. <br></p><p>The default value is 25.</p><p>Maximum value: 100</p></td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="192">Name</th><th width="112">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>string</td><td>The agent access token. You can get the agent access token from the Agent -> Settings page. See <a href="../../../how-to/build-agents/configure-agents/define-settings#agent-authentication-keys">Agent Authentication Keys</a>, for more information</td></tr></tbody></table>

{% tabs %}
{% tab title="200 Consider that you wish to get the latest message from the agent. Use GET method and specify the URL <https://cx.avaamo.com/v1/messages.json?per_page=1>. The following is a sample JSON response returned:" %}

```javascript
{
  "current_page": 1,
  "per_page": 1,
  "total_entries": 4371,
  "total_pages": 4371,
  "time_token": 1569219802.3621287,
  "entries": [
    {
      "uuid": "dc3c4ebd-e0b0-4bd9-a79d-09114e286358",
      "content": "Hi, your order number is V5678.",
      "content_type": "text",
      "created_at": 1569216722.51246,
      "user": {
        "first_name": "Mac Pizza Agent",
        "last_name": "",
        "layer_id": "fe8ee61c-f039-4cdc-8986-5bebec9edf08",
        "email": null,
        "phone": null,
        "avatar": false,
        "avatar_updated_at": null,
        "avaamo_id": 5713616
      },
      "timetoken": 1569216722502878,
      "external_source": null,
      "device_uuid": "b05fde04-2242-419b-bf12-49f79e5f9d74",
      "request_message_uuid": "14b92488-a3b4-4a10-9384-dd80f425f4f3",
      "sequence": "1/1",
      "custom_properties": {},
      "agent_message_uuid": null,
      "read_acks": [
        {
          "read_at": 1569216722,
          "user": {
            "first_name": "John",
            "last_name": "C",
            "layer_id": "dashboard_admin_test_user_696",
            "email": null,
            "phone": null,
            "avatar": false,
            "avatar_updated_at": null,
            "avaamo_id": 5713625
          }
        }
      ],
      "attachments": [],
      "conversation": {
        "uuid": "1faa40c8253e65aa02bfd02fd8643d35",
        "mode": false,
        "display_name": "Mac Pizza Agent,John",
        "locale": "en-GB"
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Note**: For optimal API performance, the recommended time duration for fetching data from any of the REST APIs that support a date range or time period is 7 days.&#x20;
{% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/v1/messages.json?per_page=1' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/v1/messages.json?per_page=1',
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

<table><thead><tr><th width="170.33333333333331">Attribute</th><th width="384.30274693161897">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages.</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td><a href="#entries">entries</a></td><td>Indicates an array of messages fetched from the agent. The number of entries in the array = Number specified in the per_page parameter.</td><td>JSON key-value pairs</td></tr></tbody></table>

#### **entries**

Indicates an array of messages fetched from the agent. Each array contains the following attributes:

<table><thead><tr><th width="195.2560899076883">Attribute</th><th width="335.87372218881546">Description</th><th>Type</th></tr></thead><tbody><tr><td>uuid</td><td>Indicates a unique identifier of the message.</td><td>String</td></tr><tr><td>content</td><td>Indicates the content of the message.</td><td>String</td></tr><tr><td>content_type</td><td>Indicates the type of content such as text, ListView, card, quick_reply.</td><td>String</td></tr><tr><td>created_at</td><td>Indicates the timestamp of when the message was created in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>user</td><td>Indicates the details of the user interacting with the agent. See <a href="#user-details">User details</a>, for more information.</td><td>JSON key-value pairs</td></tr><tr><td>timetoken</td><td>Indicates the created timestamp of the message in milliseconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>device_uuid</td><td>Indicates a unique identifier of the device from which the agent is being used.</td><td>String</td></tr><tr><td>request_message_uuid</td><td>Indicates a unique identifier of the request message.</td><td>String</td></tr><tr><td>sequence</td><td>Indicates the sequence of the agent response message. There can be multiple responses for a user query, each identified with the <strong>request_message_uuid</strong> and sequence. Note that the request_message_uuid is the same for each agent response.</td><td>&#x3C;&#x3C;message_sequence>>/&#x3C;&#x3C;total message></td></tr><tr><td>custom_properties</td><td><p>Indicates any additional user properties in the fetched message.</p><p><strong>Example</strong>:</p><p>"custom_properties": {</p><p>"employee_id":12345,</p><p>"dept": "quality"</p><p>},</p></td><td>JSON key-value pairs</td></tr><tr><td>read_acks</td><td><p>Indicates the details of when the message was read and acknowledged.</p><ul><li><strong>read_at</strong>: Indicates the read timestamp of the message in UNIX epoch format.</li><li><strong>user</strong>: Indicates the details of the user who acknowledged the message. </li></ul></td><td>An array of JSON key-value pairs</td></tr><tr><td>attachments</td><td>Indicates an array of attachments that is fetched from the agent message.</td><td>JSON key-value pairs</td></tr><tr><td>conversation</td><td><p>Indicates the conversation details of the message:</p><ul><li><strong>uuid</strong>: Indicates a unique identifier of the conversation.</li><li><strong>display_name</strong>: Indicates display name of the conversation in the following format: <code>&#x3C;&#x3C;Agent Display Name>>, &#x3C;&#x3C;User First Name>>.</code></li><li><strong>locale</strong>: Indicates the locale used in the agent conversation.</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

#### User details

The following user details are available in each message response of the Get Message API:

<table><thead><tr><th width="166.33333333333331">Attribute</th><th width="364.1553855208947">Description</th><th>Type</th></tr></thead><tbody><tr><td>phone</td><td>Indicates an array of phone numbers of the user interacting with the agent.</td><td>An array of JSON key-value pairs</td></tr><tr><td>last_name</td><td>Indicates the last name of the user interacting with the agent.</td><td>String</td></tr><tr><td>first_name</td><td>Indicates the first name of the user interacting with the agent.</td><td>String</td></tr><tr><td>email</td><td>Indicates the email of the user interacting with the agent.</td><td>String</td></tr><tr><td>layer_id</td><td>Indicates an internal unique user identifier used by the Avaamo Platform.</td><td>String</td></tr><tr><td>avaamo_id</td><td>Indicates the unique identifier of the user interacting with the agent. You can use this user identifier to further get custom properties, if any, from the agent. See <a href="custom-properties-api">Custom properties API</a>, for more information.</td><td>Integer</td></tr><tr><td><p>user_agent, os_name, zone_offset, </p><p>utc_offset, time_zone</p></td><td><p>Indicates the device details from where the agent is accessed. </p><p>Note that the device details are tracked at the user level and not at the message level. So, if the same user is accessing the agent from different devices, then the latest device details is returned in the messages. </p><p>The device details are returned only when the device_info = true in the GET message request. </p><ul><li><strong>user_agent</strong>: Indicates the browser’s user agent, applicable only for the web channel.</li><li><strong>os_name</strong>: Indicates the operating system of the device with which the user interacted with the agent.</li><li><strong>zone_offset</strong>: Indicates the time zone offset from GMT for the user.</li><li><strong>utc_offset</strong>: Indicates the time zone offset from UTC for the user.</li><li><strong>time_zone</strong>: Indicates the time zone of the user who accessed the agent.</li></ul></td><td>JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="211.02964405363724">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get the latest message from the agent</td><td><p><strong>per_page</strong>: Specify 1 to get the latest message. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/v1/messages.json?per_page=1</code></p></td></tr><tr><td>Get messages from the agent within a specified period</td><td><p><strong>since_timetoken</strong>: Specify the "from" timestamp in epoch format such as 1569229247677821</p><p><strong>timetoken</strong>: Specify the "to" timestamp in epoch format such as 1569229251418739. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/v1/messages.json?since_timetoken=1569229247677821&#x26;timetoken=1569229251418739</code></p></td></tr><tr><td>Get messages from the agent using pagination</td><td><p><strong>page</strong>: Specify the page from which you wish to fetch records. </p><p><strong>per_page</strong>: Specify the number of entries per page. y default, the value is 5. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/v1/messages.json?page=5&#x26;per_page=2</code></p></td></tr><tr><td>Get the latest message with device details from agent</td><td><p><strong>per_page</strong>: Specify 1 to get the latest message. </p><p><strong>device_info</strong>: Set to true</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/v1/messages.json?per_page=1&#x26;device_info=true</code></p></td></tr></tbody></table>
