# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/feedback-api.md

# Feedback API

## Get feedback summary&#x20;

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/dashboard/bots/{{agent_id}}/feedbacks/user_feedbacks.json`

Get a summary of the total positive and negative user feedback given to an agent. If you wish to get details of each feedback, then refer to **Get feedback details**.

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name        | Type   | Description                                                                                                                                                                                                  |
| ----------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| utc\_offset | number | <p>Difference in seconds from Coordinated Universal Time (UTC) for a particular place and date. </p><p></p><p>Default value is 0 implying that there is no offset from Coordinated Universal Time (UTC).</p> |
| from\_date  | string | Date from which the required details are retrieved. Default value is the last four days from the to\_date. Specify date in dd/mm/yyyy format.                                                                |
| to\_date    | string | Date to which the required details are retrieved. Default value is the current date. Specify date in dd/mm/yyyy format.                                                                                      |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | string | <p>User access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information. </p><p></p><p>Users must have at least view permission on the agent. See <a href="../../how-to/build-agents/configure-agents/permissions">Permissions</a>, for more information.</p> |

{% tabs %}
{% tab title="200 " %}

```javascript
{
    "user_feedbacks": [
        {
            "feedback_type": "Positive Feedback",
            "count": 3,
            "positive": true
        },
        {
            "feedback_type": "Negative Feedback",
            "count": 2,
            "positive": false
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
curl --location --request GET 'https://cx.avaamo.com/dashboard/bots/20xxx/feedbacks/user_feedbacks.json?utc_offset=19800' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/dashboard/bots/20xxx/feedbacks/user_feedbacks.json?utc_offset=19800',
  'headers': {
    'Content-Type': 'application/json',
    'Access-Token': 'xxxxxx8d9952499ea466fc007dxxxxxx'
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

In the response, user\_feedbacks array is returned with a count of positive and negative feedback:

<table><thead><tr><th width="164.33333333333331">Attribute</th><th width="440">Description</th><th>Type</th></tr></thead><tbody><tr><td>feedback_type</td><td>Indicates if the feedback is positive or negative.</td><td>String</td></tr><tr><td>count</td><td>Indicates the count of positive or negative feedback.</td><td>Integer</td></tr><tr><td>positive</td><td>Indicates if the user feedback is positive or negative.</td><td>Boolean</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="186.68455977675723">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get overall feedback summary</td><td><p><code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/feedbacks</code></p><p><code>/user_feedbacks.json?utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></p></td></tr><tr><td>Get feedback summary within a specified period</td><td><p><strong>from_date</strong>: Specify the <strong>from</strong> date in dd/mm/yyyy format.</p><p><strong>to_date</strong>: Specify the <strong>to</strong> date in dd/mm/yyyy format.</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/</code></p><p><code>feedbacks/user_feedbacks.json?from_date=01/04/2020&#x26;to_date=06/04/2020&#x26;utc_offset=&#x3C;&#x3C;utc-offset-seconds>></code></p></td></tr></tbody></table>

## Get feedback details

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/dashboard/bots/{{agent_id}}/feedbacks.json`

Gets details of each user feedback given to the agent. In the response, you can learn about the intent, user query, and the skill for which the feedback was given.&#x20;

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name             | Type    | Description                                                                                                                                                                                                                                         |
| ---------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| response\_type   | string  | Indicates if you wish to get a detailed response for each feedback. In the detailed response, you can view the user query and the user details for which the feedback is given. Specify **detailed** to view a detailed response for each feedback. |
| since\_timetoken | number  | <p>Timestamp from which the records are fetched. </p><p><br>If you specify timetoken and not since\_timetoken, then the latest 5 entries up to the specified timetoken are fetched. </p><p></p><p>Specify UNIX Epoch Timestamp in microseconds.</p> |
| timetoken        | number  | <p>Timestamp until which the records are fetched. </p><p></p><p>Default is the current timestamp. </p><p></p><p>Specify UNIX Epoch Timestamp in microseconds.</p>                                                                                   |
| page             | integer | <p>Page from which the entries must be fetched. </p><p>Default is 1.</p>                                                                                                                                                                            |
| per\_page        | integer | <p>Number of entries fetched per page. </p><p>Default: 25.</p><p>Maximum: 100</p>                                                                                                                                                                   |
| from\_date       | String  | <p>Date from which the required details are retrieved. </p><p></p><p>Default value is the last four days from the to\_date. </p><p></p><p>Specify date in dd/mm/yyyy format.</p>                                                                    |
| to\_date         | String  | <p>Date to which the required details are retrieved. </p><p></p><p>Default value is the current date. </p><p></p><p>Specify date in dd/mm/yyyy format.</p>                                                                                          |
| message\_uuid    | String  | <p>Unique identifier of the message. Refer <a href="../message-api#get-agent-messages">Message API</a></p><p>to get the details of message uuid.</p>                                                                                                |

#### Headers

| Name                                           | Type   | Description                                                                                                                                            |
| ---------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Access-Token<mark style="color:red;">\*</mark> | string | User access token. You can get the user access token from the Settings -> Users and Roles page. Users must have at least view permission on the agent. |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
   "current_page": 1,
   "per_page": 25,
   "total_entries": 8,
   "total_pages": 1,
   "feedbacks": [
       {
           "id": 115986,
           "comment": "\n      Oh! Can you tell me what went wrong?:\n      Others\n",
           "positive": false,
           "node_key": "1",
           "intent_type": "Q&A Intent",
           "intent_name": "Price of RAM",
           "created_at": 1670420497.0,
           "message_uuid": "u-2xxxxxxx9-7xxe-4xx9-8xx5-7xxxxxxxxxx9",
           "conversation_uuid": "exxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
           "skill_name": "Price FAQs",
           "bot_replies": null,
           "user_query": "I need a RAM price",
           "user": {
               "display_name": "David Miller",
               "id": 1997722,
               "first_name": "David",
               "last_name": "Miller",
               "avatar": false,
               "uid": "dashboard_admin_ua_test_user_xx4"
           }
       },

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
curl --location --request GET 'https://cx.avaamo.com/dashboard/bots/20xxx/feedbacks.json?page=2&per_page=55' \
--header 'Content-Type: application/json' \
--header 'Access-Token: xxxxxx8d9952499ea466fc007dxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/dashboard/bots/20xxx/feedbacks.json?page=2&per_page=55',
  'headers': {
    'Content-Type': 'application/json',
    'Access-Token': 'xxxxxx8d9952499ea466fc007dxxxxxx'
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

<table><thead><tr><th>Attribute</th><th width="376.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td><a href="#feedbacks">feedbacks</a></td><td>Indicates an array of feedback entries fetched from the agent. Number of entries in the array = Number specified in per_page parameter.</td><td>JSON key-value pairs</td></tr></tbody></table>

#### **feedbacks**

Indicates an array of messages fetched from the agent. Each array contains the following attributes:

<table><thead><tr><th>Attribute</th><th width="384.16396568160155">Description</th><th>Type</th></tr></thead><tbody><tr><td>id</td><td>Indicates a unique identifier of the feedback message.</td><td>Integer</td></tr><tr><td>comment</td><td>Indicates the comments given by the user for negative feedback.</td><td>String</td></tr><tr><td>positive/negative</td><td>Indicates if the user feedback is positive or negative</td><td>Boolean</td></tr><tr><td>node_key</td><td><p>Indicates the node number for which the feedback is given. </p><ul><li>For Q&#x26;A skill the node_key is 1. </li><li>For Dialog skill node_key is &#x3C;&#x3C;skill_number>>.&#x3C;&#x3C;node_number>></li></ul></td><td>String</td></tr><tr><td>intent_type</td><td><p>Indicates the type of intent. For Q&#x26;A skill, intent_type is "Q&#x26;A Intent". </p><p></p><p>For Dialog skill, intent_type can be entity, training phrase, custom code, or system entity. See <a href="../../how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent">Add user intent</a>, for more information.</p></td><td>String</td></tr><tr><td>intent_name</td><td>Indicates the name of the intent for which the feedback is given.</td><td>String</td></tr><tr><td>created_at</td><td>Indicates the timestamp of when the feedback was created in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>skill_name</td><td>Indicates the name of the skill.</td><td>String</td></tr><tr><td>bot_replies -> message</td><td>Indicates the message agent responded with. By default, this field always shows a "null" value.<br><br>See <a href="../message-api#get-agent-messages">Messege API</a>, for more details on the parameters displayed in this section.</td><td>JSON key-value pairs </td></tr><tr><td>user_query</td><td>Indicates the user query for which the feedback is given. This is returned only for a detailed response.</td><td>String</td></tr><tr><td>user</td><td><p>Indicates the details of the user interacting with the agent.</p><ul><li><strong>phone</strong>: Indicates an array of phone numbers of the user interacting with the agent.</li><li><strong>layer_id</strong>: Indicates a unique user identifier internally used by the Avaamo Platform.</li><li><strong>last_name</strong>: Indicates the last name of the user interacting with the agent.</li><li><strong>first_name</strong>: Indicates the first name of the user interacting with the agent.</li><li><strong>email</strong>: Indicates the email of the user interacting with the agent.</li></ul><p>This is returned only for a detailed response.</p></td><td>JSON key-value pairs</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="215">Use-case</th><th>Query Parameter</th></tr></thead><tbody><tr><td>Get feedback entries from agent using pagination</td><td><p><strong>page</strong>: Specify the page from which you wish to fetch records. By default, the value is 1.</p><p><strong>per_page</strong>: Specify the number of entries per page. By default, the value is 5. </p><p></p><p><strong>Example</strong>:  <code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/feedbacks.json&#x26;per_page=2&#x26;page=1</code></p><p>Here, per_page * total_pages = total_entries</p></td></tr><tr><td>Get feedback entries from agent within a specified period</td><td><p><strong>since_timetoken</strong>: Specify the <strong>from</strong> timestamp in epoch format such as 1569229247677821</p><p><strong>timetoken</strong>: Specify the <strong>to</strong> timestamp in epoch format such as 1569229251418739. </p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/feedbacks.json?since_timetoken=&#x3C;&#x3C;from_timetoken>>&#x26;timetoken=&#x3C;&#x3C;to_timetoken></code></p></td></tr><tr><td>Get detailed feedback response </td><td><p><strong>response_type</strong>: detailed</p><p></p><p><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/feedbacks.json?response_type=detailed</code></p></td></tr><tr><td>Get feedback entries from agent using message UUID</td><td><strong>message_uuid:</strong> Specify the Unique identifier of the message such as u-2xxxxxxx9-7xxe-4xx9-8xx5-7xxxxxxxxxx9<br><br><strong>Example</strong>: <code>https://cx.avaamo.com/dashboard/bots/&#x3C;&#x3C;agent_id>>/feedbacks.json?&#x26;message_uuid=&#x3C;&#x3C;message_uuid>></code></td></tr></tbody></table>
