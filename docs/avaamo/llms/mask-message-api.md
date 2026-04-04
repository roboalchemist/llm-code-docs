# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/mask-message-api.md

# Mask message API

### Mask user messages and agent responses

<mark style="color:orange;">`PUT`</mark> `https://cx.avaamo.com/dashboard/conversations/{{conversation_uuid}}/mask_messages.json`

Masks the user messages in the specified user conversation (for new conversation) from the beginning till the date as per the agent masking configuration details. To mask Personally Identifiable Information (PII) within a specific time range, you can include the `since_timetoken` and `timetoken` parameters in the API request.

Masks the agent's response in the specified user conversation from the date masking is enabled for the response node.

#### Path Parameters

<table><thead><tr><th width="217.05950927734375">Name</th><th width="90.57354736328125">Type</th><th>Description</th></tr></thead><tbody><tr><td>conversation_uuid<mark style="color:red;">*</mark></td><td>String</td><td>User conversation identifier. You can get the conversation uuid from the Conversation History URL. You can get the conversation identifier from the <a href="../../how-to/build-agents/debug-agents/conversation-history">Conversation history URL</a> or from the <a href="../message-api#get-agent-messages">Get Messages API. </a> </td></tr></tbody></table>

#### Query Parameters

<table><thead><tr><th width="210.43829345703125">Name</th><th width="103.60498046875">Type</th><th>Description</th></tr></thead><tbody><tr><td>since_timetoken</td><td>number</td><td>Timestamp from which the messages should be masked.<br><br>Specify in UNIX Epoch Timestamp in seconds.</td></tr><tr><td>timetoken</td><td>number</td><td>Timestamp until which the messages should be masked. <br><br>Specify in UNIX Epoch Timestamp in seconds.</td></tr></tbody></table>

{% hint style="info" %}
**Note**:&#x20;

Users can also pass either or both parameters (`since_timetoken` or `timetoken`).

* If only `since_timetoken` is specified, the system uses the latest message's timestamp as the `timetoken`.
* If only `timetoken` is provided, the system uses the agent creation timestamp as the `since_timetoken`.
  {% endhint %}

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Access-Token<mark style="color:red;">\*</mark> | string | <p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p><p></p><p>Users must have at least edit permission on the agent. See <a href="applewebdata://CD31BA2E-218E-4FE5-B2EB-2CAE29868D4B/@avaamo/s/avaamo/~/drafts/-MYxGNUFf68iUPzf71u7/how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

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
**The key points**:&#x20;

* See [Mask response in Advanced settings](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings), for more information on how to enable masking for a response node.
* When you enable masking for a node with file masking, all the uploaded files are physically deleted from the Platform and cannot be accessed.
* You can check the Conversation history to view the masked messages. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents#using-conversation-history), for more information.
* See [Information masking](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/information-masking), for more details.
  {% endhint %}

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request PUT 'https://cx.avaamo.com/dashboard/conversations/xxxxxxae172c539696ff6f4f67xxxxxx/mask_messages.json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx' \
--header 'Content-Type: application/json'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'PUT',
  'url': 'https://cx.avaamo.com/dashboard/conversations/xxxxxxae172c539696ff6f4f67xxxxxx/mask_messages.json',
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

#### Examples&#x20;

The following table lists a sample use case with query parameters:

<table><thead><tr><th width="363"> Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Mask messages within a specified period</td><td><p><strong>since_timetoken:</strong> Specify the starting timestamp in seconds in UNIX Epoch format.</p><p><strong>timetoken</strong>: Specify the ending timestamp in seconds in UNIX Epoch format.</p><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/conversations/{{conversation_uuid}}/mask_messages.json?since_timetoken=1720604526&#x26;timetoken=1736502126</code></p></td></tr></tbody></table>
