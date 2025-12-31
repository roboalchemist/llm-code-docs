# Source: https://docs.avaamo.com/user-guide/outreach/outreach-rest-apis/outreach-insights-api.md

# Outreach insights API

## Get campaign insights

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v2/campaigns/insights`

Get a closer look at the user conversations with the campaign. You can use this API for debugging and reporting purposes. See [Campaigns](https://docs.avaamo.com/user-guide/outreach/campaigns), for more information.

#### Query Parameters

<table><thead><tr><th width="192">Name</th><th width="105">Type</th><th>Description</th></tr></thead><tbody><tr><td>conversation_uuid</td><td>String</td><td><p>Conversation identifier of the communication between campaign and the recipient. Valid when the campaign is linked to an agent for two-way communication. See <a href="../../campaigns/create-new-campaign#link-to-avaamo-agent-two-way-communication">Link to Avaamo agent</a>, for more information.</p><p></p><p>You can get the conversation identifier from the <a href="../../../how-to/build-agents/debug-agents#using-conversation-history">Conversation history URL</a> or from the <a href="../../../ref/avaamo-platform-api-documentation/message-api#get-agent-messages">Get Messages API</a> of the agent that is linked to the campaign. </p><p></p><p><code>Example: conversation_uuid=17xxxxxxxx</code></p><p></p></td></tr><tr><td>delivery_channel</td><td>array</td><td><p>Channel in which the campaign message was delivered. Possible values: sms, voice, ms_teams</p><p></p><p><code>Example:</code> </p><p><code>delivery_channel=sms</code></p><p></p></td></tr><tr><td>start_time</td><td>number</td><td><p>Timestamp from which the records are fetched. </p><p></p><p>The default value is the last three days from the specified <code>end_time</code> value. </p><p></p><p>Specify in UNIX Epoch Timestamp.</p><p></p><p>The Outreach Insights API allows you to retrieve data for the last 6 months. If the <code>start_time</code> specified in the data request exceeds this 6-month limit, the system automatically adjusts <code>start_time</code> to the maximum allowable range of the past 6 months.</p></td></tr><tr><td>end_time</td><td>number</td><td><p>Timestamp until which the records are fetched. The default value is the current timestamp.</p><p></p><p>Specify in UNIX Epoch Timestamp in milliseconds.</p></td></tr><tr><td>page</td><td>integer</td><td>Page from which the entries must be fetched. <br>Default: 1.</td></tr><tr><td>per_page</td><td>integer</td><td>Number of entries fetched per page. <br>Default: 25<br>Maximum value: 100</td></tr><tr><td>language</td><td>String</td><td><p>Language of the campaign message.  See <a href="../../campaigns/create-new-campaign#language-specific-messages">Language-specific messages</a>, for more information.</p><p><br><code>Example 1:</code></p><p><code>language[]=en-US</code></p><p><br><code>Example 2:</code></p><p><code>language[]=en-US&#x26;language[]=hi-IN</code></p></td></tr><tr><td>message_uuid</td><td>String</td><td><p>Message identifier in the campaign conversation. Valid when the campaign is linked to an agent for two-way communication. See <a href="../../campaigns/create-new-campaign#link-to-avaamo-agent-two-way-communication">Link to Avaamo agent</a>, for more information.</p><p></p><p>You can get the message identifier from the API response itself or from the <a href="../../../ref/avaamo-platform-api-documentation/message-api#get-agent-messages">Get Messages API</a> of the agent that is linked to the campaign. </p><p></p><p><code>Example: message_uuid=bc12xxxxxxxx</code></p></td></tr><tr><td>execution_id</td><td>integer</td><td><p>Identifier of a campaign run. You can get the <code>execution_id</code> from the API response itself. </p><p></p><p><code>Example: execution_id=2x</code></p></td></tr><tr><td>campaign_id</td><td>integer</td><td><p>Campaign identifier. You can get the campaign identifier from the campaign URL.  </p><p></p><p><code>Example 1: campaign_id=17x</code></p><p><code>Example 2: campaign_id=13x, 45x</code></p></td></tr><tr><td>to_phone</td><td>String</td><td><p>The recipient's phone number to which the campaign message was sent. </p><p></p><p>Valid for SMS and Voice campaigns. Ensure that the value is URL encoded. </p><p></p><p><code>Example: to_phone=222xxx5678</code></p></td></tr><tr><td>from_phone</td><td>String</td><td><p>The phone number from which the campaign message was sent to the recipients. </p><p></p><p>Valid for SMS and Voice campaigns. Ensure that the value is URL encoded. </p><p></p><p><code>Example: from_phone=444666xxxx</code></p></td></tr><tr><td>filter_id</td><td>integer</td><td><p>Filter identifier that was applied for delivering the campaign message. You can specify multiple filters using a comma-separated list.</p><p></p><p>You can get the filter identifier from the campaign filter URL. See <a href="../filters">Filters</a>, for more information. </p><p></p><p><code>Example 1: filter_id=5x</code></p><p><code>Example 2: filter_id=5x,2x</code></p></td></tr><tr><td>agent_id</td><td>integer</td><td><p>Agent identifier. Valid when the campaign is linked to an agent for two-way communication. See <a href="../../campaigns/create-new-campaign#link-to-avaamo-agent-two-way-communication">Link to Avaamo agent</a>, for more information. </p><p></p><p>You can get the agent identifier from the agent URL. </p><p></p><p><code>Example: agent_id=17x</code></p></td></tr><tr><td>response_set_id</td><td>integer</td><td><p>Response set identifier that was picked for delivering the campaign message. You can get the response set identifier from the API response itself. See <a href="../../campaigns/create-new-campaign#response-sets">Response sets</a>, for more information. </p><p></p><p><code>Example: response_set_id=17x</code></p></td></tr><tr><td>delivery_status</td><td>String</td><td><p>Delivery status of the campaign message. Possible values: sent, failed, skipped, delivered, undelivered.</p><p></p><p>See <a href="#campaign-delivery-status">Campaign delivery status</a>, for more information.</p><p></p><p><code>delivery_status[]=failed</code></p></td></tr><tr><td>channel_id</td><td>integer</td><td><p>Channel identifier. You must specify </p><p><code>delivery_channel</code> query parameter to use <code>channel_id</code> in the query parameter.</p><p></p><p>You can get the response set identifier from the API response itself. Valid when the campaign is linked to an agent for two-way communication. See <a href="../../campaigns/create-new-campaign#link-to-avaamo-agent-two-way-communication">Link to Avaamo agent</a>, for more information. </p><p></p><p><code>Example: channel_id=5xx</code></p></td></tr><tr><td>to_email</td><td>String</td><td><p>The recipient's email to which the campaign message was sent. </p><p></p><p>Valid for MS Teams campaign. Ensure that the value is URL encoded. </p><p></p><p><code>Example: to_email=john%40avaamo.com%0A</code></p></td></tr><tr><td>recipient_uuid</td><td>String</td><td><p>Unique identifier for each recipient. For multi-message campaign, the recipient_uuid remains the same for each message in the multi-message list when sent to the same recipient. You can get the <code>recipient_uuid</code> from the API response itself. </p><p></p><p><code>Example: recipient_uuid=bc12xxxxxxx</code></p></td></tr><tr><td>user[&#x3C;&#x3C;user_properties>>]</td><td>Array</td><td><p><a href="../../how-to/build-agents/configure-agents/add-user-properties">User properties</a> such as first name, last name<br><br><code>Example 1: user[first_name]=Mike</code></p><p><code>Example 2: user[last_name]=Bob</code> </p><p><code>Example 3: user[first_name]=Mike&#x26;user[last_name]=Bob</code></p></td></tr><tr><td>error_code</td><td>String</td><td>Indicates the code for the error that occurred when delivering the campaign message to the corresponding recipient. You can get the <code>error_code</code> from the API <a href="#entries">response</a> itself. <br><br><code>Example: error_code=AVM01, AVM02</code></td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="183">Name</th><th width="115">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>String</td><td><p>The user access token. This API gets  the insights of all the campaigns from the account the user is associated with.</p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p></td></tr></tbody></table>

{% tabs %}
{% tab title="200 Successful request" %}
{% code overflow="wrap" %}

```json
{
    "current_page": 1,
    "per_page": 25,
    "total_entries": 2,
    "total_pages": 1,
    "time_token": 1689593442.8405523,
    "entries": [
        {
            "id": 1382620,
            "recipient_uuid": "8eb0dxxx-xxxx-xxxx-xxxx-xxx0db5b6fb5",
            "delivery_status": "failed",
            "message_uuid": null,
            "created_at": 1751450792,
            "content": "If you are having any references, feel free to forward this message.",
            "conversation_uuid": null,
            "language": "en-US",
            "user": {
                "id": "1373",
                "last_name": "Smith",
                "first_name": "Jake",
                "phone": "72) 913-6939",
                "acct_bal": "$0.00",
                "age": "72",
                "job_id": "Z1479217",
                "dob": "03/16/1967"
            },
            "error": "Could not place call due to technical error.",
            "error_code": "AVM1015",
            "execution": {
                "id": 2980,
                "created_at": 1751450376
            },
            "delivery_channel": "voice",
            "from_phone": "+18507905180",
            "filters": [],
            "response_set": {
                "id": 1384,
                "name": null
            },
            "campaign": {
                "id": 780,
                "name": "CIVR7"
            },
            "to_phone": "729136939"
        },
            "user": {
                "phone": "+918971115555",
                "email": "john@avaamo.com",
                "first_name": "John",
                "last_name": "Miller"
            },
            "campaign": {
                "id": 511,
                "name": "Sparsh Healthcare Multi Message Campaign"
            },
            "to_phone": "+918971115555"
        },
        {
            "id": 8685,
            "recipient_uuid": "f8adcxxx-xxxx-xxxx-xxxx-xxx734ac348e",
            "delivery_status": "delivered",
            "message_uuid": null,
            "created_at": 1689592018,
            "content": "The Sparsh care center is organizing a free Flu vaccination drive on October 1st and October 2nd from 10 AM to 6 PM. Visit your nearest Sparsh Care Center to get vaccinated. \n",
            "conversation_uuid": null,
            "language": "en-US",
            "execution": {
                "id": 1708,
                "created_at": 1689592016
            },
            "delivery_channel": "sms",
            "from_phone": "+18507905180",
            "filters": [],
            "response_set": {
                "id": 997,
                "name": null
            },
            "user": {
                "phone": "+918971115555",
                "email": "John@avaamo.com",
                "first_name": "John",
                "last_name": "Miller"
            },
            "campaign": {
                "id": 511,
                "name": "Sparsh Healthcare Multi Message Campaign"
            },
            "to_phone": "+918971115555"
        }
    ]
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Notes**:&#x20;

* For optimal API performance, the recommended time duration for fetching data from any of the REST APIs that support a date range or time period is 7 days.
* You can retrieve data from the Outreach Insights API for up to the past 6 months from the current date of access.
* If the same user appears in multiple campaigns with the same primary header, the insights override the attributes from different CSV files, showing the most recent attributes in the latest insights.
  {% endhint %}

### Campaign delivery status

Note the following campaign delivery status mapping for each channel:

<table><thead><tr><th width="144">Status</th><th width="389">Description</th><th>Applicable channels</th></tr></thead><tbody><tr><td>Sent</td><td>Request has been initiated successfully.</td><td><p>SMS </p><p>C-IVR </p><p>MS Teams </p><p>Custom channel</p></td></tr><tr><td>Failed</td><td><p>The recipient is filtered out or failed to send the request to the recipient since the email or phone number was not available.</p><p> </p><p>For C-IVR, failed status is returned even when the user declines the call. </p><p></p><p>Check the <a href="../../../ref/avaamo-platform-api-documentation/sms-reporting-api#error-status">Error status</a> of the corresponding record for more information.   </p></td><td><p>SMS </p><p>C-IVR </p><p>MS Teams </p><p>Custom channel</p></td></tr><tr><td>Pending</td><td>Status is pending when the recipient was engaged in another call at the same time when the campaign was triggered. The campaign message is later updated to Delivered, Undelivered, Failed when the recipient line is again available for usage.</td><td><p></p><p>C-IVR </p><p></p></td></tr><tr><td>Delivered</td><td>The message is successfully delivered to the recipient</td><td><p>SMS </p><p>C-IVR  </p><p>Custom channel</p></td></tr><tr><td>Undelivered</td><td><p>Unable to deliver the message to the recipient.  </p><p></p><p>Check the <a href="../../../ref/avaamo-platform-api-documentation/sms-reporting-api#error-status">Error status</a> of the corresponding record for more information.</p></td><td><p>SMS </p><p>C-IVR </p><p>Custom channel</p></td></tr><tr><td>Queued</td><td>Received the request, but the recipient is waiting in queue to process it.</td><td>MS Teams </td></tr><tr><td>Installed</td><td>Triggered the installation of the MS teams app to the recipient, waiting to send the campaign message.</td><td>MS Teams </td></tr></tbody></table>

### Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location 'https://cx.avaamo.com/api/v2/campaigns/insights' \
--header 'Content-Type: application/json' \
--header 'access-token: xxxxxxxxx4d14acba2fb2ccxxxxxxxxx'
```

{% endtab %}

{% tab title="node.js" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v2/campaigns/insights',
  'headers': {
    'Content-Type': 'application/json',
    'access-token': 'xxxxxxxxx4d14acba2fb2ccxxxxxxxxx'
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

The following is a sample response of a successful Outreach insights API request:

{% code overflow="wrap" %}

```json
{
    "current_page": 1,
    "per_page": 25,
    "total_entries": 2,
    "total_pages": 1,
    "time_token": 1751971354.0004876,
    "entries": [
        {
            "id": 1382614,
            "recipient_uuid": "917c7xxx-xxxx-xxxx-xxxx-xxx21754d1b7",
            "delivery_status": "failed",
            "message_uuid": null,
            "created_at": 1750851657,
            "content": "Hi nobody here, I'm your point of contact.\n",
            "conversation_uuid": null,
            "language": "en-US",
            "user": {
                "phone": "1234567890",
                "email": "someone@somewhere.com",
                "first_name": "nobody",
                "last_name": "here"
            },
            "error": "'To' number +91123456XXXX cannot be a landline",
            "error_code": null,
            "execution": {
                "id": 2978,
                "created_at": 1750851339
            },
            "delivery_channel": "sms",
            "from_phone": "+18507905180",
            "filters": [],
            "response_set": {
                "id": 1394,
                "name": null
            },
            "campaign": {
                "id": 832,
                "name": "multi message test 2"
            },
            "to_phone": "+911234567890"
        },
        {
            "id": 1382615,
            "recipient_uuid": "917c79d0-5a0a-41fb-b1ad-1a021754d1b7",
            "delivery_status": "failed",
            "message_uuid": null,
            "created_at": 1750851657,
            "content": "\nReach out to me for any queries.",
            "conversation_uuid": null,
            "language": "en-US",
            "user": {
                "phone": "1234567890",
                "email": "someone@somewhere.com",
                "first_name": "nobody",
                "last_name": "here"
            },
            "error": "'To' number +91123456XXXX cannot be a landline",
            "error_code": null,
            "execution": {
                "id": 2978,
                "created_at": 1750851339
            },
            "delivery_channel": "sms",
            "from_phone": "+18507905180",
            "filters": [],
            "response_set": {
                "id": 1394,
                "name": null
            },
            "campaign": {
                "id": 832,
                "name": "multi message test 2"
            },
            "to_phone": "+911234567890"
        }
    ]
}
```

{% endcode %}

In the response, the following attributes are returned:

<table><thead><tr><th width="189.96747765510364">Attribute</th><th width="283.74249584282035">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of intent entries in the response.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned.</td><td>UNIX epoch timestamp</td></tr><tr><td><a href="#entries">entries</a></td><td><p>Indicates an array of insights fetched across all the campaigns of an account.</p><p></p><p>Number of entries in the array = Number specified in per_page parameter.</p></td><td>JSON key-value pairs</td></tr></tbody></table>

#### entries

Indicates an array of insights fetched across all the campaigns of an account. Each array contains the following attributes:

<table><thead><tr><th width="188">Attribute</th><th width="423.93690248565963">Description</th><th>Type</th></tr></thead><tbody><tr><td>id</td><td>Indicates an identifier of each insight entry. This is for internal purposes only.</td><td>Integer</td></tr><tr><td>recipient_uuid</td><td>Unique identifier for each recipient. For multi-message campaign, the recipient_uuid remains the same for each message in the multi-message list when sent to the same recipient.</td><td>String</td></tr><tr><td>delivery_status</td><td><p>Indicates the delivery status of the campaign message. Possible values: sent, failed, skipped, delivered, undelivered.</p><p></p><p>See <a href="#campaign-delivery-status">Campaign delivery status</a>, for more information.</p></td><td>String</td></tr><tr><td>to_phone</td><td><p>Indicates the recipient's phone number to which the campaign message was sent. </p><p></p><p>Valid and returned only for SMS and Voice campaigns. </p></td><td>String</td></tr><tr><td>to_email</td><td><p>Indicates the recipient's email to which the campaign message was sent. </p><p></p><p>Valid and returned only for MS Teams campaign.</p></td><td>String </td></tr><tr><td>language</td><td>Indicates the language of the campaign message. See <a href="../../campaigns/create-new-campaign#language-specific-messages">Language-specific messages</a>, for more information.</td><td>String</td></tr><tr><td>execution</td><td>Indicates the identifier of a campaign run.</td><td>Integer</td></tr><tr><td>delivery_channel</td><td>Indicates the channel in which the campaign message was delivered. Possible values: sms, voice, ms_teams</td><td>String</td></tr><tr><td>from_phone</td><td><p>Indicates the phone number from which the campaign message was sent to the recipients. </p><p></p><p>Valid for SMS and Voice campaigns. from_phone is null for MS Teams campaigns.</p></td><td>String</td></tr><tr><td>filters</td><td><p>Indicates an array of filters that were applied for delivering the campaign message. Each filter array contains the identifier, the name of the filter, and if the filter was matched or not.</p><p></p><p>See <a href="../filters">Filters</a>, for more information. </p></td><td>Array of JSON key-value pairs</td></tr><tr><td>response_set</td><td><p>Indicates the response set that was picked for delivering the campaign message. The response set contains the identifier and name of the response set.</p><p></p><p>See <a href="../../campaigns/create-new-campaign#response-sets">Response sets</a>, for more information. </p></td><td>JSON key-value pairs</td></tr><tr><td>created_at</td><td>Indicates the timestamp of when the insight was created in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td>user</td><td><p>Indicates any additional user properties fetched in the campaign insights. </p><p><strong>Example</strong>: </p><p>"user": { </p><p>"phone": " 1 972 913 xxx", </p><p>"email": "john.miller@avaamo.com", "first_name": "John", </p><p>"last_name": "Miller"</p><p>}</p></td><td>JSON key-value pairs</td></tr><tr><td>content</td><td>Indicates the content of the campaign message.</td><td>String</td></tr><tr><td>conversation_uuid</td><td><p>Indicates the conversation identifier of the communication between the campaign and the recipient. </p><p></p><p>Valid when the campaign is linked to an agent for two-way communication. See <a href="../../campaigns/create-new-campaign#link-to-avaamo-agent-two-way-communication">Link to Avaamo agent</a>, for more information.</p></td><td>String</td></tr><tr><td>message_uuid</td><td><p>Indicates the message identifier in the campaign conversation. A conversation can have multiple messages and each message has an identifier to uniquely identify the message in the conversation.</p><p></p><p>Valid when the campaign is linked to an agent for two-way communication. See <a href="../../campaigns/create-new-campaign#link-to-avaamo-agent-two-way-communication">Link to Avaamo agent</a>, for more information.</p></td><td>String</td></tr><tr><td>campaign</td><td>Indicates the campaign details such as the identifier and name of the campaign.</td><td>JSON key-value pairs</td></tr><tr><td>agent</td><td><p>Indicates the agent details such as the identifier, name, and channel details of the agent. </p><p></p><p>Valid when the campaign is linked to an agent for two-way communication. See <a href="../../campaigns/create-new-campaign#link-to-avaamo-agent-two-way-communication">Link to Avaamo agent</a>, for more information.</p></td><td>JSON key-value pairs</td></tr><tr><td>error</td><td>Indicates the error that occurred when delivering the campaign message to the corresponding recipient. This is available only when the <code>delivery_status</code> is either failed or skipped.</td><td>String</td></tr><tr><td>error_code</td><td>Indicates the code for the error that occurred when delivering the campaign message to the corresponding recipient. </td><td>String</td></tr></tbody></table>

### Examples

The following table lists a few sample use cases with query parameters:

<table><thead><tr><th width="269">Use case</th><th>Query parameter</th></tr></thead><tbody><tr><td>Get insights of campaigns using multiple campaign IDs</td><td><code>https://cx.avaamo.com/api/v2/campaigns/insights?campaign_id=12xx,56xx</code></td></tr><tr><td>Get insights specific to a channel and delivery status</td><td><code>https://cx.avaamo.com/api/v2/campaigns/insights?delivery_channel=ms_teams&#x26;delivery_status=failed</code></td></tr><tr><td>Get insights using user properties</td><td><code>https://cx.avaamo.com/api/v2/campaigns/insights?campaign_id=6xx, 6xx&#x26;user[first_name]=Mike&#x26;user[last_name]=Bob</code></td></tr><tr><td>Get insights using error codes</td><td><code>https://cx.avaamo.com/api/v2/campaigns/insights?error_code=AVM1015, AVM1010, AVM1001</code></td></tr></tbody></table>
