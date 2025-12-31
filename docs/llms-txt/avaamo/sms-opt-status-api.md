# Source: https://docs.avaamo.com/user-guide/outreach/outreach-rest-apis/sms-opt-status-api.md

# SMS Opt status API

## Gets a list of Opt SMS status of the recipient numbers that have explicitly opted-in or opted-out across all the campaigns of an account

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v2/sms/opt-status.json`

By default, all the recipients are considered as opted-in to receive campaign messages, unless the recipients have explicitly opted out of the campaign. See [Opting out of campaign](https://docs.avaamo.com/user-guide/outreach/campaigns/opting-out-of-campaign), for more information. To optimize the cost and to respect the user's privacy of opting out, it is useful to get a list of all such opted-out recipients before sending any campaign message.

#### Query Parameters

<table><thead><tr><th width="163">Name</th><th width="104">Type</th><th>Description</th></tr></thead><tbody><tr><td>to_phone</td><td>String</td><td>The recipient's phone number to which the SMS was sent. Ensure that the value is URL encoded.</td></tr><tr><td>from_phone</td><td>String</td><td><p>The phone number from which the SMS was sent to the recipients. </p><p>Ensure that the value is URL encoded. </p></td></tr><tr><td>start_time</td><td>Number</td><td><p>Timestamp from which the records are fetched. If you specify <code>start_time</code> and not <code>end_time</code>, then the latest 3 entries up to the specified timetoken are fetched.</p><p></p><p>Specify in UNIX Epoch Timestamp in milliseconds.</p></td></tr><tr><td>status</td><td>String</td><td><p>The opt-status of the recipient's phone number at the time the record was created. </p><p></p><p>Note that this is useful when the same recipient's phone number has opted-out and opted-in multiple times. In such cases, the same recipient phone number can have multiple entries in the response for each such opt-status and the latest current opt-status. </p><p></p><p>Supported values: opt-in, opt-out</p></td></tr><tr><td>current_status</td><td>String</td><td><p>Latest opt-status of the recipient's phone number. </p><p></p><p>Supported values: opt-in, opt-out</p></td></tr><tr><td>end_time</td><td>Number</td><td><p>Timestamp until which the records are fetched. The default value is the current timestamp.</p><p></p><p>Specify in UNIX Epoch Timestamp in milliseconds.</p></td></tr><tr><td>page</td><td>integer</td><td><p>Page from which the entries must be fetched. </p><p>Default: 1</p></td></tr><tr><td>per_page</td><td>integer</td><td><p>Number of entries fetched per page. </p><p>Default: 25 </p><p>Maximum value: 100</p></td></tr></tbody></table>

#### Headers

<table><thead><tr><th width="179">Name</th><th width="98">Type</th><th>Description</th></tr></thead><tbody><tr><td>access-token<mark style="color:red;">*</mark></td><td>String</td><td><p>The user access token. This API gets  the opt-status of all the recipient phone number's that have explicitly opted-in or opted-out from the account the user is associated with.</p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p></td></tr></tbody></table>

{% tabs %}
{% tab title="200: OK Successful request" %}

```json
{
    "current_page": 1,
    "per_page": 1,
    "total_entries": 9,
    "total_pages": 5,
    "time_token": 1675410047.186922,
    "entries": [
        {
            "to_phone": "+12929929902",
            "from_phone": "+19090909090",
            "created_at": "<<timestamp>>",
            "status": "opt-out",
            "current_status": "opt-out"
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
{% code overflow="wrap" %}

```bash
curl --location --request GET 'https://cx.avaamo.com/api/v2/sms/opt-status' \
--header 'access-token: xxxxxxxx9952499ea466fcxxxxxxxxxx'
```

{% endcode %}
{% endtab %}

{% tab title="node.JS" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v2/sms/opt-status',
  'headers': {
    'access-token': 'xxxxxxxx9952499ea466fcxxxxxxxxxx'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
}
```

{% endtab %}
{% endtabs %}

### Response attributes

The following is a sample response of a successful SMS Opt Status API request:

```json
{
    "current_page": 1,
    "per_page": 1,
    "total_entries": 9,
    "total_pages": 5,
    "time_token": 1675410047.186922,
    "entries": [
        {
            "to_phone": "+12929929902",
            "from_phone": "+19090909090",
            "created_at": "<<timestamp>>",
            "status": "opt-out",
            "current_status": "opt-out"
        }
    ]
}
```

In the response, you can get the following details about the SMS messages:

<table><thead><tr><th width="198.97643515043268">Attribute</th><th width="321.2689031392294">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td><a href="#entries">entries</a></td><td><p>Indicates an array of SMS message details fetched across all the campaigns of an account.</p><p></p><p>Number of entries in the array = Number specified in per_page parameter.</p></td><td>JSON key-value pairs</td></tr></tbody></table>

#### entries

Indicates an array of SMS message details fetched across all the campaigns of an account. Each array contains the following attributes:

<table><thead><tr><th>Attribute</th><th width="297.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>from_phone</td><td>Indicates the number from which the SMS was sent.</td><td>String</td></tr><tr><td>to_phone</td><td>Indicates the number to which the SMS was sent.</td><td>String</td></tr><tr><td>created_at</td><td><p>Indicates the timestamp of when the request was received by the carrier. </p><p></p><p>Note that "carrier" here, indicates the service responsible for delivering the SMS to the desired recipient.</p></td><td>UNIX epoch timestamp</td></tr><tr><td>status</td><td><p>Indicates the opt-status of the  <code>to_phone</code> number at the time the record was created. </p><p></p><p>Note that this is useful when the same recipient's phone number has opted-out and opted-in multiple times. In such cases, the same recipient phone number can have multiple entries in the response for each such opt-status and the latest current opt-status. </p><p></p><p>Possible values: opt-in, opt-out. </p><ul><li><strong>opt-in</strong>: The <code>to_number</code> has subscribed to receive SMS from the  <code>from_number</code>.</li><li><strong>opt-out</strong>: The <code>to_number</code> has unsubscribed to receive SMS from the  <code>from_number</code>.</li></ul></td><td>String</td></tr><tr><td>current_status</td><td><p>Indicates the latest opt-status of the  <code>to_phone</code> number. </p><p></p><p>Possible values: opt-in, opt-out. </p><ul><li><strong>opt-out</strong>: The <code>to_number</code> has unsubscribed to receive SMS from the  <code>from_number</code>.</li><li><strong>opt-in</strong>: The <code>to_number</code> has subscribed to receive SMS from the  <code>from_number</code>.</li></ul></td><td>String</td></tr></tbody></table>

## Examples

The following table lists a few sample use cases with query parameters:

| Use case                                          | Query parameter                                                      |
| ------------------------------------------------- | -------------------------------------------------------------------- |
| Get all the opted-out recipient numbers           | `https://cx.avaamo.com/api/v2/sms/opt-status?current_status=opt-out` |
| Get the opt status of a specific recipient number | `https://cx.avaamo.com/api/v2/sms/opt-status?to_phone=%2B1909090909` |
