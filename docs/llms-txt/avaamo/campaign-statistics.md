# Source: https://docs.avaamo.com/user-guide/outreach/campaign-statistics.md

# Campaign statistics

The **Campaign statistics** page provides a data summary of the campaign sent out to the recipients. You can use this data for further analysis, debugging, and reporting purposes.

## Overall Campaign details

By default, the data for the most recent campaign sent out is displayed. For the past campaigns, select a specific date and time from the **Execution** dropdown.

{% hint style="info" %}
**Note**: Up to 6 months of campaign runs are displayed in the `Execution` dropdown.
{% endhint %}

Click **View current campaign** at the top right corner to see the current campaign details. Click this link to view the latest campaign settings such as its name, intended target audience, scheduling, communication channels, filters, and configured recipient list.&#x20;

For the selected campaign run date in the **Execution** dropdown, you can view the following details related to the campaign execution:&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FmElA47YzI2Toq6IZR9Xl%2Fimage.png?alt=media&#x26;token=03c9978c-f145-453e-9e03-dec4ae6b4567" alt=""><figcaption></figcaption></figure>

* **Total recipients**: The total number of recipients to whom the campaign message is sent.&#x20;
* **Undelivered messages**: Displays the number of undelivered messages for the whole campaign in the following format: `<<Number of undelivered messages>>/<<Total number of messages>>`.&#x20;
  * Number of undelivered messages: Sum of undelivered messages across all the recipients of the campaign.&#x20;
  * Total number of messages: Sum of all the messages in the message count column.
* **Link to agent**: Displays the agent details the campaign is linked to in case of a two-way campaign. In the one-way campaign, since no agent is linked to the campaign, N/A is displayed in the `Link to agent` block.
* **Channel**: Channel used for delivering the campaign message.
* **Campaign message history**: Displays the campaign sent status for each recipient for the selected date run of the campaign. See [Campaign messaging history](#campaign-messaging-history), for more information.

The following is a sample campaign statistics displayed for one-way campaigns. Since no agent is linked in the one-way campaign, N/A is displayed in the `Link to agent` block:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FmElA47YzI2Toq6IZR9Xl%2Fimage.png?alt=media&#x26;token=03c9978c-f145-453e-9e03-dec4ae6b4567" alt=""><figcaption></figcaption></figure>

The following is a sample campaign statistics displayed for two-way campaigns - the agent the campaign is linked to and the lifecycle stage of the agent are also displayed in this page.&#x20;

* Click the agent, if you wish to navigate and view the agent details.&#x20;
* If the campaign is linked to an agent and a conversation is established with the recipient, you can click the arrow icon against the recipient and navigate to the [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/conversation-history) page to check the conversation in more detail.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLUU2SvRBCTJoSyOSIiH7%2Fimage.png?alt=media&#x26;token=8e9292b8-e6e5-4742-994f-a52c20b28346" alt=""><figcaption></figcaption></figure>

## Campaign messaging history

{% hint style="info" %}
**Note**: Upon encountering any recipient CSV parsing error during campaign execution, the system displays a detailed error message in the `Campaign statistics` UI page, specifying the line or row where the error occurred. Furthermore, if users have configured campaign failure notifications, an email containing the error details is notified to all the users. See [Campaign failures](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#campaign-failures), for more information.
{% endhint %}

In the message history, you can view the following details:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FblOApIUIYIp4P3g0GXt9%2Fimage.png?alt=media&#x26;token=fd183feb-dbe4-421f-96a8-c662cc14d098" alt=""><figcaption></figcaption></figure>

* The first column header is based on the campaign channel:
  * For C-IVR or SMS channels, it is the recipient's phone number.
  * For the MS Teams channel, the recipient's email is displayed.
  * For the Custom channel, it is the primary field selected during campaign configuration.
  * Click the arrow icon against the recipient and navigate to the [Conversation history](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/conversation-history) page to check the conversation in more detail.&#x20;
* **Message count**: Number of messages that must be delivered to the recipient.&#x20;
* **Time**: Indicates the date and time when the campaign to the recipient was triggered.&#x20;
* **Text sent / Voice sent**: Click the help icon to view more details. In the`View message` pop-up, you can view detailed information on each message delivery status.&#x20;

The following illustration is a `View message` a pop-up window of a [multi-message SMS campaign](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#multiple-campaign-messages). You can view the phone number of the recipient, the language of the SMS messages, the number of failures, and the response set and provided in the Campaign configuration. Further, for each message in the multi-message campaign, you can view detailed information on the delivery status along with the reason for failure, if any, the time when the status was updated, and a message preview.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FCLwn0CrNtPRAmgDX87sJ%2Fimage.png?alt=media&#x26;token=43da45d9-62f8-40ef-882f-49e050bf96cc" alt=""><figcaption></figcaption></figure>

## Download reports

Click `Download` in the `Campaign message history` section to download the report. A pop-up message is displayed. Click `Ok` to download the report in a new tab.&#x20;

{% hint style="success" %}
**Key point**: The `Download` option now initiates an asynchronous job, facilitating the seamless download of larger campaign reports.
{% endhint %}

You can use this to get more details on the failed or undelivered messages and the reason for failure for further analysis.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FLDDcvkvb0t8A97dia2TA%2Fimage.png?alt=media&#x26;token=85281a57-bf16-491e-88a0-f6e6e70e2ebb" alt=""><figcaption></figcaption></figure>

In the downloaded report, apart from all the columns of the recipient list, the following details are available for each recipient:

* `Campaign :: Recipient Uuid`: Unique identifier for each recipient in the campaign to whom the message is intended. If this is a multi-message campaign, then each message sent to the campaign is a separate row in the downloaded CSV report, however, in such cases, the `Campaign :: Recipient Uuid` remains the same for each message.
* `Campaign :: To Phone`: The recipient's phone number. Applicable for SMS, C-IVR, and Custom Channel.
* `Campaign :: To Email`: The recipient's email. Applicable for MS Teams and Custom Channel.
* `Campaign :: Channel`: The campaign channel used for delivering the campaign message.
* `Campaign :: Delivery Status`: Delivery status of the campaign message. See [Delivery status](#delivery-status), for more information.
* `Campaign :: Failed Reason`: Reason for failed delivery of campaign message to the recipient, if any. See [Error status](#error-status), for more information.
* `Campaign :: Sent At (UTC)`: UTC time when the campaign to the recipient was triggered.&#x20;
* `Campaign :: Response`: Name of the response set if configured for the campaign message. See [Create new campaign](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#response-sets), for more information.

## Delivery status

Note the following campaign delivery status mapping for each channel:

<table><thead><tr><th width="144">Status</th><th width="418">Description</th><th>Applicable channels</th></tr></thead><tbody><tr><td>Sent</td><td>Request has been initiated successfully.</td><td><p>SMS </p><p>C-IVR </p><p>MS Teams </p><p>Custom channel</p></td></tr><tr><td>Failed</td><td><p>The recipient is filtered out or failed to send the request to the recipient since the email or phone number was not available.</p><p> </p><p>For C-IVR, failed status is returned even when the user declines the call. </p><p></p><p>Check the <a href="#error-status">Error status</a> of the corresponding record for more information.   </p></td><td><p>SMS </p><p>C-IVR </p><p>MS Teams </p><p>Custom channel</p></td></tr><tr><td>Pending</td><td>Status is pending when the recipient was engaged in another call at the same time when the campaign was triggered. The campaign message is later updated to Delivered, Undelivered, Failed when the recipient line is again available for usage.</td><td><p></p><p>C-IVR </p><p></p></td></tr><tr><td>Delivered</td><td>The message is successfully delivered to the recipient</td><td><p>SMS </p><p>C-IVR  </p><p>Custom channel</p></td></tr><tr><td>Undelivered</td><td><p>Unable to deliver the message to the recipient.  </p><p></p><p>Check the <a href="#error-status">Error status</a> of the corresponding record for more information.   </p></td><td><p>SMS </p><p>C-IVR </p><p>Custom channel</p></td></tr><tr><td>Queued</td><td>Received the request, but the recipient is waiting in queue to process it.</td><td>MS Teams </td></tr><tr><td>Installed</td><td>Triggered the installation of the MS teams app to the recipient, waiting to send the campaign message.</td><td>MS Teams </td></tr></tbody></table>

## Error status

When there is a message failure and you have used SMS as the delivery channel for your campaign, then the following error can be returned when the SMS was not successfully sent to the recipient. You can refer to the specific error to check the possible causes and recommended ways to resolve the error:

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
