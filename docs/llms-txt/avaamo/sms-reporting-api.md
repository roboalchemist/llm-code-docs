# Source: https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/sms-reporting-api.md

# SMS Reporting API

## Get report on SMS sent to users

<mark style="color:blue;">`GET`</mark> `https://cx.avaamo.com/api/v1/agents/{{agent_id}}/sms/report.json`

SMS report of the messages sent through the SMS Gateway of an agent. See [SMS Send API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/sms-send-api), for more information.

#### Path Parameters

| Name                                        | Type    | Description                                                            |
| ------------------------------------------- | ------- | ---------------------------------------------------------------------- |
| agent\_id<mark style="color:red;">\*</mark> | integer | Agent identifier. You can get the agent identifier from the agent URL. |

#### Query Parameters

| Name            | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| --------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from\_timetoken | number | <p>Timestamp from which the records are fetched. If you specify to\_timetoken and not from\_timetoken, then the latest 3 entries up to the specified timetoken are fetched. </p><p></p><p>Specify in UNIX Epoch Timestamp.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| to\_timetoken   | number | <p>Timestamp until which the records are fetched. The default value is the current timestamp. </p><p></p><p>Specify in UNIX Epoch Timestamp.</p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| from\_phone     | string | The phone number from which the SMS was sent to the recipients. Ensure that the value is URL encoded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| to\_phone       | string | The recipient's phone number to which the SMS was sent. Ensure that the value is URL encoded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| status          | string | <p>Indicates the delivery status of the SMS to the recipient.</p><p>Possible values: sent, failed, delivered, undelivered</p><p></p><p><strong>sent</strong>: The SMS send request was successfully received by the carrier.</p><p></p><p><strong>failed</strong>: The carrier failed to receive the SMS send request.</p><p></p><p><strong>delivered</strong>: The SMS send request was successfully received by the carrier and the SMS was successfully delivered to the desired recipient.</p><p></p><p><strong>undelivered</strong>: The SMS send request was successfully received by the carrier but the SMS was not delivered successfully to the desired recipient.</p><p></p><p>Note that "carrier" here, indicates the service responsible for delivering the SMS to the desired recipient.</p> |

#### Headers

| Name                                           | Type   | Description                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| access-token<mark style="color:red;">\*</mark> | string | <p>The user access token. </p><p></p><p>You can get the user access token from the Settings -> Users page. See <a href="../../../how-to/manage-platform-settings/users-and-permissions/users#get-user-access-token">Users</a> or <a href="../../../how-to/manage-platform-settings/users-and-permissions/groups#access-token-for-users-in-groups">Groups</a>, for more information.</p> |

{% tabs %}
{% tab title="200: OK Successful request" %}
{% code overflow="wrap" %}

```javascript
{
    "current_page": 1,
    "per_page": 25,
    "total_entries": 2,
    "total_pages": 1,
    "time_token": 1670940238.4926484,
    "entries": [
        {
            "uuid": "xxxxxx36-bbff-4b13-963f-40c733xxxxxx",
            "from_phone": "+11231231234",
            "to_phone": "+1(123) 456-xxxx",
            "message": "New Message - Appt Reminder - John Doe has an appointment on 05-12-2022 at 11:30",
            "created_at": 1670923358.0,
            "sms_status": "sent"
        },
        {
            "uuid": "xxxxxx06-7cbd-4a1f-9798-594a01xxxxxx",
            "from_phone": "+11231231234",
            "to_phone": "+1(123) 456-xxxx",
            "message": "New Message - Appt Reminder - John Doe has an appointment on 05-12-2022 at 11:30",
            "created_at": 1670923397.0,
            "sms_status": "failed",
            "sms_status_response": "Unable to create record: The 'To' number +11234567890 is not a valid phone number."
        }
    ]
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Note**: For optimal API performance, the recommended time duration for fetching data from any of the REST APIs that support a date range or time period is 7 days.
{% endhint %}

## Code request snippets

{% tabs %}
{% tab title="cURL" %}

```javascript
curl --location --request GET 'https://cx.avaamo.com/api/v1/agents/51xxx/sms/report.json' \
--header 'access-token: xxxxxxxxxxae468491fbd0xxxxxxxxxx'
```

{% endtab %}

{% tab title="node.JS" %}

```javascript
var request = require('request');
var options = {
  'method': 'GET',
  'url': 'https://cx.avaamo.com/api/v1/agents/51xxx/sms/report.json',
  'headers': {
    'Content-Type': 'application/json',
    'access-token': 'xxxxxxxxxxae468491fbd0xxxxxxxxxx'
  }
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```

{% endtab %}
{% endtabs %}

## Response attributes

The following is a sample response of a successful response:

{% code overflow="wrap" %}

```json
{
    "current_page": 1,
    "per_page": 25,
    "total_entries": 2,
    "total_pages": 1,
    "time_token": 1670940238.4926484,
    "entries": [
        {
            "uuid": "xxxxxx36-bbff-4b13-963f-40c733xxxxxx",
            "from_phone": "+11231231234",
            "to_phone": "+1(123) 456-xxxx",
            "message": "New Message - Appt Reminder - John Doe has an appointment on 05-12-2022 at 11:30",
            "created_at": 1670923358.0,
            "sms_status": "sent"
        },
        {
            "uuid": "xxxxxx06-7cbd-4a1f-9798-594a01xxxxxx",
            "from_phone": "+11231231234",
            "to_phone": "+1(123) 456-xxxx",
            "message": "New Message - Appt Reminder - John Doe has an appointment on 05-12-2022 at 11:30",
            "created_at": 1670923397.0,
            "sms_status": "failed",
            "sms_status_response": "Unable to create record: The 'To' number +11234567890 is not a valid phone number."
        }
    ]
}
```

{% endcode %}

In the response, you can get the following details about the SMS messages:

<table><thead><tr><th width="198.97643515043268">Attribute</th><th width="321.2689031392294">Description</th><th>Type</th></tr></thead><tbody><tr><td>current_page</td><td>Indicates the page from which the entries are fetched.</td><td>Integer</td></tr><tr><td>per_page</td><td>Indicates the number of entries fetched per page.</td><td>Integer</td></tr><tr><td>total_entries</td><td>Indicates the total number of entries in the agent messages.</td><td>Integer</td></tr><tr><td>total_pages</td><td>Indicates the total number of pages calculated using per_page. Note that total_entries = per_page * total_pages</td><td>Integer</td></tr><tr><td>time_token</td><td>Indicates the timestamp at which the API response is returned in seconds.</td><td>UNIX epoch timestamp</td></tr><tr><td><a href="#entries">entries</a></td><td><p>Indicates an array of SMS message details fetched from the agent. </p><p></p><p>Number of entries in the array = Number specified in per_page parameter.</p></td><td>JSON key-value pairs</td></tr></tbody></table>

#### entries

Indicates an array of SMS message details fetched from the agent. Each array contains the following attributes:

<table><thead><tr><th>Attribute</th><th width="297.3333333333333">Description</th><th>Type</th></tr></thead><tbody><tr><td>uuid</td><td>Indicates a unique identifier of the message.</td><td>Integer</td></tr><tr><td>from_phone</td><td>Indicates the number from which the SMS was sent.</td><td>String</td></tr><tr><td>to_phone</td><td>Indicates the number to which the SMS was sent.</td><td>String</td></tr><tr><td>message</td><td>Indicates the actual message sent in SMS.</td><td>String </td></tr><tr><td>created_at</td><td>Indicates the timestamp of when the request was received by the carrier. Note that "carrier" here, indicates the service responsible for delivering the SMS to the desired recipient.</td><td>UNIX epoch timestamp</td></tr><tr><td>sms_status</td><td><p>Indicates the status of SMS delivery. Possible values: sent, failed, delivered, undelivered. </p><ul><li><strong>sent</strong>: The SMS send request was successfully received by the carrier.</li><li><strong>failed</strong>: The carrier failed to receive the SMS send request.</li><li><strong>delivered</strong>: The SMS send request was successfully received by the carrier and the SMS was successfully delivered to the desired recipient.</li><li><strong>undelivered</strong>: The SMS send request was successfully received by the carrier but the SMS was not delivered successfully to the desired recipient.</li></ul><p>Note that "carrier" here, indicates the service responsible for delivering the SMS to the desired recipient.</p></td><td>String</td></tr><tr><td>sms_status_response</td><td>Indicates the error status of the failed SMS delivery. See <a href="#error-status">Error status</a>, for more information.</td><td>String</td></tr></tbody></table>

## Examples

The following table lists a few sample use cases with query parameters:

| Use case                                                         | Query parameter                                                                                                            |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Get the SMS message report within a specified period             | `https://cx.avaamo.com/api/v1/agents/57xx/sms/report.json?from_timetoken=1672123097&to_timetoken=1672134095`               |
| Get the SMS message report that failed within a specified period | `https://cx.avaamo.com/api/v1/agents/57xx/sms/report.json?from_timetoken=1672123097&to_timetoken=1672134095&status=failed` |
| Get the SMS message report triggered to a specific "to\_number"  | `https://cx.avaamo.com/api/v1/agents/57xx/sms/report.json?to_phone=%2B17778889999`                                         |

## Error status

When there is a failure, the SMS status response is returned that explains the reason for the failure and recommended ways to resolve the error. The following error can be returned when the SMS was not successfully sent to the recipient:&#x20;

1. [SMS send rate limit exceeded](#1.-sms-send-rate-limit-exceeded)
2. [Permission to send an SMS has not been enabled for the region indicated by the 'To' number](#2.-permission-to-send-an-sms-has-not-been-enabled-for-the-region-indicated-by-the-to-number)
3. [Attempt to send to unsubscribed recipient](#3.-attempt-to-send-to-an-unsubscribed-recipient)
4. [This 'From' number has exceeded the maximum number of queued messages](#4.-this-from-number-has-exceeded-the-maximum-number-of-queued-messages)
5. ['To' number is not a valid mobile number](#5.-to-number-is-not-a-valid-mobile-number)
6. [Queue overflow](#6.-queue-overflow)
7. [Account suspended](#7.-account-suspended)
8. [Unreachable destination handset](#8.-unreachable-destination-handset)
9. [Message blocked](#9.-message-blocked)
10. [Message Delivery - Unknown destination handset](#10.-message-delivery-unknown-destination-handset)
11. [Landline or unreachable carrier](#11.-landline-or-unreachable-carrier)
12. [Message filtered](#12.-message-filtered)
13. [Message Delivery - Unknown error](#13.-message-delivery-unknown-error)
14. [Carrier network congestion](#14.-carrier-network-congestion)
15. [Content size exceeds carrier limit](#15.-content-size-exceeds-carrier-limit)
16. [Invalid message recipient](#16.-invalid-message-recipient)
17. [Channels message cannot have same From and To](#17.-channels-message-cannot-have-same-from-and-to)

### 1. SMS send rate limit exceeded

**Possible Causes**

Repeated rapid responses by the end user (15 replies in less than 30 seconds).

**Recommended Solution**

* Ensure that you are not inadvertently sending a large number of messages to the same phone number, e.g. a script caught in a loop.
* Contact Avaamo Support for further assistance.

### 2. Permission to send an SMS has not been enabled for the region indicated by the 'To' number

**Possible Causes**

You have attempted to send an SMS to a region outside the allowed range.

**Recommended Solution**

If you wish to send messages to this region, contact Avaamo Support with details for further assistance.

### 3. Attempt to send to an unsubscribed recipient

#### Possible Causes

The person you are trying to message has opted out of receiving messages from your phone number.

#### Possible Solution

* Consider removing this phone number from your list of recipients.
* Request the recipient to resubscribe to your messages by texting "START".
* Before sending messages to a recipient, ensure they have consented to receive messages from you.

### 4. This 'From' number has exceeded the maximum number of queued messages

#### Possible Causes

You have attempted to enqueue too many messages for a given 'From' number.

#### Possible Solutions

Slow down your sending rate to avoid queuing on your "from" number

### 5. 'To' number is not a valid mobile number

#### Possible Causes

You have attempted to send an SMS with a 'To' number that is not a valid mobile number. It is likely that the number that you have specified is a landline number or is an invalid number.

#### Possible Solutions

* The number you provided may be a landline number.
* The number you provided may be invalid or formatted incorrectly. It must be in the correct E.164 format: `[+] [country code] [subscriber number including area code]`

### 6. Queue overflow

#### Possible Causes

The messages are queued based on the sending rate of a sender or an account. Messages can only be queued for 4 hours and then they automatically fail.

#### Possible Solutions

* Try sending your message again after waiting for some time.
* If you are messaging in the US or Canada, talk to Avaamo Support about getting a Toll Free or Short Code number that allows you to send more messages per second.

### 7. Account suspended

#### Possible Causes

Your account was suspended between the time of the message send and delivery.

#### Possible Solutions

Contact Avaamo Support for further assistance.

### 8. Unreachable destination handset

#### Possible Causes

The destination handset you are trying to reach is switched off or otherwise unavailable.

#### Possible Solutions

* Is the destination device powered on?
* Does the device have a sufficient signal? If not power the device off, wait 30 seconds, and then power it back up.
* Is the device connected to the home carrier's network? We cannot guarantee message delivery on devices roaming off-network.
* Can other devices using the same mobile carrier receive your messages?

### 9. Message blocked

#### Possible Causes

* The destination number you are trying to reach is blocked from receiving this message.
* The device you are trying to reach does not have a sufficient signal.
* The device cannot receive SMS (for example, the phone number belongs to a landline).
* There is an issue with the mobile carrier.

#### Possible Solutions

* Verify you are attempting to send messages to the correct phone number in the correct E.164 format: `[+] [country code] [subscriber number including area code]`
* Is the destination device powered on?
* Does the device have a sufficient signal? If not power the device off, wait 30 seconds, and then power it back up.
* Is the device connected to the home carrier's network? We cannot guarantee message delivery on devices roaming off-network.
* Can other devices using the same mobile carrier receive your messages?

### 10. Message Delivery - Unknown destination handset

#### Possible Causes

* The destination number you are trying to reach is unknown and may no longer exist.
* The device you are trying to reach is not on or does not have sufficient signal.
* The device cannot receive SMS (for example, the phone number belongs to a landline)
* There is an issue with the mobile carrier

#### Possible Solutions

* Verify you are attempting to send messages to the correct phone number in the correct E.164 format: `[+] [country code] [subscriber number including area code]`
* Is the destination device powered on?
* Does the device have sufficient signal? If not power the device off, wait 30 seconds, and then power it back up.
* Is the device connected to the home carrier's network? We cannot guarantee message delivery on devices roaming off-network.
* Can other devices using the same mobile carrier receive your messages?

### 11. Landline or unreachable carrier

#### Possible Causes

The destination number is unable to receive this message. Potential reasons could include trying to reach a landline or, in the case of shortcodes, an unreachable carrier.

#### Possible Solutions

Contact Avaamo Support with the details of your message for further assistance. Include a minimum of 3 or more messages where this error was thrown. Per our carriers' requirements, these can be no older than 48 hours at most.

### 12. Message filtered

#### Possible Causes

Your message content was flagged as going against carrier guidelines. Examples of messaging that would be blocked are spam, phishing, and fraud.

#### Possible Solutions

Contact Avaamo Support with the details of your message for further assistance. Include a minimum of 3 or more messages where this error was thrown. Per our carriers' requirements, these can be no older than 48 hours at most.

### 13. Message Delivery - Unknown error

#### Possible Causes

Delivery of your message failed for unknown reasons.

#### Possible Solutions

* Check that the phone you were sending to is turned on and can receive SMS
* Ensure that the phone is not roaming off the network. We cannot guarantee message delivery on roaming phones.
* Try sending it to other phones who have the same mobile carrier
* Try sending a shorter message to the phone, with simple content that does not include any special characters. This gives our support team an idea as to whether the failure is related to concatenation or character encoding.
* Contact Avaamo Support with a minimum of 3 or more messages where this error was thrown. Per our carriers' requirements, these can be no older than 48 hours at most.

### 14. Carrier network congestion

#### Possible Causes

Carrier is experiencing congestion in traffic

#### Possible Solutions

Send your message over a longer period of time, rather than sending it in bursts

### 15. Content size exceeds carrier limit

#### Possible Causes

The message failed because the size of the content associated with the message exceeded the carrier limit

#### Possible Solutions

Content size should be within carrier limits.

### 16. Invalid message recipient

#### Possible Causes

Message recipient could not be verified

#### Possible Solutions

Content size should be within carrier limits.

### 17. Channels message cannot have same From and To

#### Possible Causes

Incorrect To and From number in channels message

#### Possible Solutions

Correct the channels To the destination number
