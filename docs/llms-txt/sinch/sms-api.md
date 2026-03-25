# Source: https://docs.sinch.com/technical-documentation/api-and-integrations/sms-api.md

# SMS API

Technical Documentation: SMS API.

## Important Terms

### **Important Terms**

| ​             | ​                              | ​                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MT**        | Mobile Terminated              | Term used for messages that have the user (device) as destination. I.e., **messages originating from your company**, destined for the user (device)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **MO**        | Mobile Originated              | Term used for messages that have your company as destination. I.e., **messages originating from the user** (device). It is used, for instance, in question and answer flows via SMS, when confirmation is required from the user.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Response**  | Synchronous response from Wavy | The immediate response to a request made in our API, where we inform whether the message has been accepted by our platform.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Callback**  | Sent status                    | The first sent status we return, where we inform whether the message has been delivered **to the carrier**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **LA**        | Short Code                     | A short 5- or 6-digit number, used for sending and receiving SMS messages. They are appointed by carriers to approved integrators (Wavy) and have antifraud and antispam rules                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **DR or DLR** | Delivery Receipt               | <p>The second sent status we return, where we inform whether the message was delivered <strong>to the device</strong>. The carriers send this information to Wavy, and we relay it to the customer. Delivery time varies: for example, if the device was turned off at the time the message was sent and the user turned it back on 2 hours later, this DLR status will be delivered to the customer with a 2-hour delay.</p><p><strong>•</strong> This receipt of delivery to the device will only exist in cases where the message has been successfully delivered to the carrier, i.e., the first status (callback) was successful.</p><p><strong>•</strong> It is very important to highlight that unfortunately carriers Oi and Sercomtel do not have this functionality, that is, they do not give us information on delivery to the device. Messages sent to numbers from those carriers will only have information on delivery to the carrier (callback)</p> |

## Message Flow

Simplified Flow: MT, Callback, DLR, MO

!\[Diagram

Description automatically generated]\(<https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2Fsinch-documentation-global%2F-MlGhsmOlT1CwS5Md1dR%2F-MlGj-fPMNPcZsbwy1u5%2F0.png?generation=1633458858387845\\&alt=media>)

## HTTPS API

This API allows you to automatize both single and bulk message requests and the retrieval of sent statuses through queries. It uses HTTP protocol with TLS and accepts the GET method with query string parameters and the POST method with [JSON](http://json.org/) parameters.

### Authentication

To send messages and run queries in our API, you need to authenticate using a combination of either username or email and a token.

| Field                   | Details                                                                                                                                                                                                                                                                                                                         | Data Type |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| **UserName**            | Your username or email                                                                                                                                                                                                                                                                                                          | String    |
| **AuthenticationToken** | Your authentication token. Check [here](https://messaging.movile.com/messaging/user/api_configuration) and read username descriptions below.                                                                                                                                                                                    | String    |
| Type                    | Details                                                                                                                                                                                                                                                                                                                         | ​         |
| **Administrator**       | Admin user for your company; it is used for creating/editing/deactivating subaccounts and other users, and it can view reports of the entire company. This user does not send messages, whether through the portal or via API integration.                                                                                      | ​         |
| **User**                | User used for sending messages via API and portal; it can view reports specific to its subaccount. A user is always related to a single subaccount. A subaccount can have multiple users. Each subaccount is a cost center in our platform; messages are broken down in reports and financially by subaccount, and not by user. | ​         |
| **templateID**          | SMS template identifier. The text of the message will be retrieved and it should first be created through the Messaging Portal.                                                                                                                                                                                                 | Long      |
| **templateName**        | SMS template name. It may not be exclusive, resulting in an error if more than one template is found for the user’s access level. The text of the message will be retrieved and it should first be created through the Messaging Portal                                                                                         | String    |

### Connection Details

| ​                  | ​                                                            |
| ------------------ | ------------------------------------------------------------ |
| **Hostname**       | api-messaging.wavy.global                                    |
| **APIs**           | Single messages /v1/send-sms Bulk messages /v1/send-bulk-sms |
| **Port**           | 443 (https)                                                  |
| **Protocol**       | HTTPS (TLS encryption)                                       |
| **Authentication** | username + token                                             |
| **Portal**         | messaging.wavy.global                                        |

### Encoding

The encoding standard used is UTF-8, all message contents must follow this standard.

You can escape characters if you wish or encode using HTTP format.

You can see some encoding examples to the side

***“messageText”:“A combinação foi perfeita :)”***

Or you can escape characters if you so wish:

***“messageText”:“A combina\u00e7\u00e3o foi perfeita :)”***

***​***

## Sending Messages (MT)

### Sending with GET Method - Individual

curl -X POST \\

&#x20;<https://api-messaging.wavy.global/v1/send-sms> \\

&#x20;-H 'authenticationtoken: \<authenticationtoken>' \\

&#x20;-H 'username: \<username>' \\

&#x20;-H 'content-type: application/json' \\

&#x20;-d '{"destination": "5511900000000" , "messageText": "linha\nquebrada"}'

​

After sending a message, you will receive a JSON informing the id that was generated for that message (Synchronous response from Wavy):

\[

&#x20;{

&#x20;"id":"9cb87d36-79af-11e5-89f3-1b0591cdf807",

&#x20;"correlationId":"myId"

&#x20;}

]

Via GET method, you can send a message by relaying all parameters as a query string.

### URL for Single Messages with GET Method

GET <https://api-messaging.wavy.global/v1/send-sms?destination=>..

Via POST method, you can send a message by relaying all parameters in the body.

### URL for Single Messages with POST Method

POST <https://api-messaging.wavy.global/v1/send-sms> - Content-Type: application/json

### Request Parameters

**\* Required field**

| Field                | Details                                                                                                                                                                                                                                                                                                                                                                                                                                        | Type       |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **destination\***    | Phone number to which the message will be sent (**including country code**). E.g.: 5511900000000                                                                                                                                                                                                                                                                                                                                               | String     |
| **messageText\***    | Text of the message to be sent (max 1280 chars).                                                                                                                                                                                                                                                                                                                                                                                               | String     |
| **correlationId**    | A unique ID set by you to match the sent statuses (callback and DLR). This parameter is optional, and you can use the ID generated by Wavy for this purpose (max 64 chars).                                                                                                                                                                                                                                                                    | String     |
| **extraInfo**        | Any extra information you wish to add to your message (max 255 chars).                                                                                                                                                                                                                                                                                                                                                                         | String     |
| **timeWindow**       | Messages will only be sent during the specified time. For example, if you set a \[11, 12, 18] window, messages will be sent between 11:00 and 11:59 A.M., 12:00 and 12:59 P.M., and 6:00 and 6:59 PM. This parameter must be set in the root of the JSON object                                                                                                                                                                                | Integer\[] |
| **expiresAt**        | Your message will not be sent after this date. The format used is [Unix time](https://en.wikipedia.org/wiki/Unix_time) . Note: The expiresAt, expiresInMinutes and expiresDate field are mutually exclusive (use one of them only)                                                                                                                                                                                                             | Long       |
| **expiresInMinutes** | Your message will expire after the time set in this field. The time starts counting as soon as your message is received by Wavy. Note: The expiresAt, expiresInMinutes and expiresDate fields are mutually exclusive (use one of them only)                                                                                                                                                                                                    | Long       |
| **expiresDate**      | Your message will not be sent after this date. This field accepts the following format yyyy-MM-dd’T'HH:mm:ss. Note: The expiresAt, expiresInMinutes and expiresDate fields are mutually exclusive (use one of them only)                                                                                                                                                                                                                       | String     |
| **scheduledAt**      | Your message will not be sent after this date. IMPORTANT! You can only schedule a period longer than 30 minutes, as it is processed by a differentiated flow from non-scheduled messages. The format used is [Unix time](https://en.wikipedia.org/wiki/Unix_time). The expiresAt, expiresInMinutes and expiresDate fields are mutually exclusive (use one of them only)                                                                        | Long       |
| **delayedInMinutes** | How many minutes after the request is made your message will be sent. The expiresAt, expiresInMinutes and expiresDate fields are mutually exclusive (use one of them only)                                                                                                                                                                                                                                                                     | Long       |
| **scheduledDate**    | Your message will not be sent before this date. This field supports the format yyyy-MM-dd’T'HH:mm:ss. Note: The expiresAt, expiresInMinutes and expiresDate fields are mutually exclusive (use one of them only)                                                                                                                                                                                                                               | String     |
| **timeZone**         | Specifies the time zone into be used directly in the fields: expiresDate, scheduledDate and timeWindow (which will be modified in case dynamic time zones are used, such as daylight saving time). If the time zone is not included in your request, the system will check the user’s time zone - if included - or the time zone of the user’s country as a last resort. If neither of these options are present, the system will use UTC time | String     |
| **campaignAlias**    | Identification for a previously created campaign. [Click here](https://messaging.movile.com/messaging/master) to register a new campaign; this parameter must be set in the root of the JSON object                                                                                                                                                                                                                                            | String     |
| **flashSMS**         | Flash SMS; use this option to send a pop-up message to a user’s phone. To send a Flash message, set parameter to true.                                                                                                                                                                                                                                                                                                                         | Boolean    |
| **flowId**           | Bot flow identifier. The text of your message will come from the selected flow                                                                                                                                                                                                                                                                                                                                                                 | String     |
| **subAccount**       | Subaccount reference. It can only be used by Admin users                                                                                                                                                                                                                                                                                                                                                                                       | String     |
| **params**           | Map of placeholders that will be replaced in the text of your message. If one or more parameters are incorrect, your message will be flagged as invalid, but delivery will not be cancelled. You must send the flowId to use parameters                                                                                                                                                                                                        | Map        |

**For every user, there is a unique authentication token**

### Messaging via POST Method - Single or Bulk

curl --request POST \\

&#x20;\--url <https://api-messaging.wavy.global/v1/send-bulk-sms> \\

&#x20;\--header 'authenticationtoken: \<Authentication Token>' \\

&#x20;\--header 'username:\<Movile Messaging User>' \\

&#x20;\--header 'content-type: application/json' \\

&#x20;\--data "{ "messages":\[{ "destination":"5519999999999", "messageText":"First message" }, { "destination":"5519999999999" }, { "destination":"5519999999999" }], "defaultValues":{"messageText":"Default message" }}"

​

**There is a 1000-message limit per request**

After sending a message, a JSON object will be returned with the UUID for the batch and individual messages:

​

&#x20;{

&#x20;"id": "ce528d70-013b-11e7-98f2-e27c463c8809",

&#x20;"messages": \[

&#x20;{

&#x20;"id": "ce528d71-013b-11e7-98f2-e27c463c8809"

&#x20;},

&#x20;{

&#x20;"id": "ce528d72-013b-11e7-98f2-e27c463c8809"

&#x20;}

&#x20;]

}

Allows you to send bulk or individual messages by relaying parameters in a JSON object. There is a 1000-message limit per request

### HTTP Request via POST Method

Example of JSON for Bulk messaging:

Example 1:

{

&#x20;"messages":\[

&#x20;{

&#x20;"destination":"5519900001111",

&#x20;"messageText":"First message"

&#x20;},

&#x20;{

&#x20;"destination":"5519900002222"

&#x20;},

&#x20;{

&#x20;"destination":"5519900003333"

&#x20;}

&#x20;],

&#x20;"defaultValues":{

&#x20;"messageText":"Default message"

&#x20;}

}

Example 2:

{

&#x20;"messages":\[

&#x20;{

&#x20;"destination":"5519900001111",

&#x20;"messageText":"First message"

&#x20;},

&#x20;{

&#x20;"destination":"5519900002222"

&#x20;}

&#x20;],

&#x20;"timeZone":"America/Sao\_Paulo",

&#x20;"scheduledDate": "2017-01-28T02:30:43",

&#x20;"timeWindow": \[12, 15, 20],

&#x20;"defaultValues":{

&#x20;"messageText":"Default message"

&#x20;}

}

Example 3:

{

&#x20;"messages":\[

&#x20;{

&#x20;"destination":"5519900001111"

&#x20;},

&#x20;{

&#x20;"destination":"5519900002222"

&#x20;}

&#x20;],

&#x20;"defaultValues":{

&#x20;"messageText":"Default message",

&#x20;"flashSMS":"true"

&#x20;}

}

Example 4, with flowId and params:

{

&#x20;"messages":\[

&#x20;{

&#x20;"destination":"5519900001111",

&#x20;"params": {

&#x20;"param1": "other\_value1",

&#x20;"param2": "other\_value2"

&#x20;}

&#x20;},

&#x20;{

&#x20;"destination":"5519900002222"

&#x20;}

&#x20;],

&#x20;"defaultValues":{

&#x20;"params": {

&#x20;"param1": "value1",

&#x20;"param2": "value2"

&#x20;}

&#x20;},

&#x20;"flowId": "14f8142d-e731-4971-8220-5a76a12c413f"

}

Example 5, with templateId/templateName (possible with either or both) and parameters:

{

&#x20;"messages":\[

&#x20;{

&#x20;"destination":"5519900001111",

&#x20;"params": {

&#x20;"param1": "other\_value1",

&#x20;"param2": "other\_value2"

&#x20;}

&#x20;},

&#x20;{

&#x20;"destination":"5519900002222"

&#x20;}

&#x20;],

&#x20;"defaultValues":{

&#x20;"params": {

&#x20;"param1": "value1",

&#x20;"param2": "value2"

&#x20;}

&#x20;},

&#x20;"templateId": 0,

&#x20;"templateName": 'name'

}

​

## HTTP Status Code Response

Most common HTTP status codes:

| Group   | Description           |
| ------- | --------------------- |
| **2xx** | Success               |
| **4xx** | Client Error          |
| **5xx** | Server Error          |
| Code    | Description           |
| **200** | Success               |
| **400** | Bad Request           |
| **401** | Unauthorized          |
| **403** | Forbidden             |
| **404** | Not Found             |
| **429** | Too Many Requests     |
| **500** | Internal Server Error |
| **503** | Service Unavailable   |
| **504** | Gateway Timeout       |

Maximum limit is 700 requests per second per IP.

## Sent Status (Callback and DLR)

There are two ways of obtaining message sent statuses, namely:

* Webhook - Receive statuses in a webserver of your company (recommended)

As soon as we deliver your message to the carrier, or as soon as the carrier informs us whether it has delivered your message to the device, this information is relayed to you instantaneously.

* Query API - Make query requests in our sms-status API.

Statuses are available for 3 days and can be retrieved using the UUID that Wavy returned upon receiving the message from your company or the ID that your company received after delivering your message to Wavy.

The downside to this option Note in the examples above, some “destination” fields do not have a “messageText” directly attributed to them; in these cases, the text of your message will be the “messageText” within “defaultValues.” This function is useful when you need to send the same message to several different numbers of running queries instead of webhooks is that you will make query requests for an ID that might not have been delivered to the carrier or the device yet; in this case, a series of unnecessary requests will be made. For example, if a user had their device turned off when you sent them a message and they turned it back on 2 hours later, you will be requesting this ID countless times during two hours. And if you use a webhook, this information would be sent to you as soon as it was delivered to the device, without any empty requests.

Status queries have a rate-limit of 1 request per second per IP address. Requests beyond this limit are responded to with HTTP status code 429.

### Statuses via Webhook (Delivery to Your Webservice)

In order to set the delivery of Callbacks and DRs (if you have questions about these terms, check the [Important Terms](http://doc-messaging.movile.com/pt.html#termos-importantes) tab), first you need to log in to [Wavy Messaging](https://www.messaging.wavy.global/) in API settings; in the settings form, you can provide the URLs to which sent statuses (Callbacks) and device confirmation statuses (DRs) will be sent

After including your webhook in the portal above, your settings will be replicated to our platform within 10 minutes, and we will call your URL when the following actions occur:

| Action                                                      | Return status sent         |
| ----------------------------------------------------------- | -------------------------- |
| After a message is delivered or not to the carrier          | Sent status API (callback) |
| When a message is delivered or not to the customer’s device | Delivery Report API (DRs)  |

Example of JSON sent status (callback - delivery to the carrier)

POST <https://example.com/callback/>

Content-Type: application/json

​

{

&#x20;"id":"f9c100ff-aed0-4456-898c-e57d754c439c",

&#x20;"correlationId":"client-id",

&#x20;"carrierId":1,

&#x20;"carrierName":"VIVO",

&#x20;"destination":"5511900009999",

&#x20;"sentStatusCode":2,

&#x20;"sentStatus":"SENT\_SUCCESS",

&#x20;"sentAt":1266660300000,

&#x20;"sentDate":"2010-02-20T10:05:00Z",

&#x20;"campaignId":"64",

&#x20;"extraInfo":"",

}

### JSON response fields in Callbacks (sent status)

| Field              | Description                                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------- |
| **id**             | Message UUID generated                                                                                                |
| **correlationId**  | Your identification for this message                                                                                  |
| **carrierId**      | Carrier identifier                                                                                                    |
| **carrierName**    | Carrier name                                                                                                          |
| **destination**    | Phone number to which your message was sent                                                                           |
| **sentStatusCode** | Status code generated by Wavy for your message indicating its sent status. Refer to status codes for more information |
| **sentStatus**     | Sent status description. Refer to status codes for more information                                                   |
| **sentAt**         | Time the message was sent, the format used is Unix\_time                                                              |
| **sentDate**       | Date the message was sent. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                             |
| **campaignId**     | Campaign identifier, if any                                                                                           |
| **extraInfo**      | Any extra information added by the customer when sending the message                                                  |

### JSON response fields in Delivery Reports (DRs)

| Field                   | Description                                                                                                                |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **id**                  | Message UUID generated                                                                                                     |
| **correlationId**       | Your identification for this message                                                                                       |
| **carrierId**           | Carrier identifier                                                                                                         |
| **carrierName**         | Carrier name                                                                                                               |
| **destination**         | Phone number to which your message was sent                                                                                |
| **sentStatusCode**      | Status code generated by Wavy for your message indicating its sent status. Refer to status codes for more information      |
| **sentStatus**          | Sent status description. Refer to status codes for more information                                                        |
| **sentAt**              | Time the message was sent, the format used is Unix\_time                                                                   |
| **sentDate**            | Date the message was sent. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                  |
| **deliveredStatusCode** | Status code generated by Wavy for your message indicating its delivered status. Refer to status codes for more information |
| **deliveredStatus**     | Delivered status description. Refer to status codes for more information                                                   |
| **deliveredAt**         | Time of delivery, the format used is Unix\_time                                                                            |
| **deliveredDate**       | Date the message was sent. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                  |
| **campaignId**          | Campaign identifier, if any                                                                                                |
| **extraInfo**           | Any extra information added by the customer when sending the message                                                       |

### Status Query via HTTP Request

To check the status of the your last sent messages, you need to make a POST request to the URL below by sending the UUID(s) and/or correlationId(s) obtained in the sent response:

POST <https://api-messaging.wavy.global/v1/sms/status/search>

{ "ids": \["918F3591-9AD6-11E7-9C9B-E255B01A8B1A","234F3591-6AD6-11E7-9C9B-E255B01A8B1A"], "correlationIds": \["2468"] }

You can also obtain only the statuses that have not yet been requested:

GET <https://api-messaging.wavy.global/v1/sms/status/list>

Note that this endpoint only returns statuses that haven’t yet been returned by this endpoint.

### Response

JSON response fields:

| Field                   | Details                                                                                                       | Type   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------- | ------ |
| **id**                  | UUID generated in the request for the message                                                                 | String |
| **correlationId**       | Same correlationId as in the request                                                                          | String |
| **carrierId**           | Carrier ID; for more information, refer to error codes                                                        | Long   |
| **carrierName**         | Carrier name                                                                                                  | String |
| **destination**         | Phone number to which your message was sent                                                                   | String |
| **sentStatusCode**      | Sent status code. Refer to Sent Status Codes for more information                                             | Long   |
| **sentStatus**          | Sent status. Refer to Sent Status Codes for more information                                                  | String |
| **sentStatusAt**        | When the message was sent. It is an Epoch Date                                                                | Long   |
| **sentStatusDate**      | When the message was sent. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone (ISO 8601)      | String |
| **deliveredStatusCode** | Delivered status code. Refer to Delivered Status Codes for more information                                   | Long   |
| **deliveredStatus**     | Delivered status. Refer to Delivered Status Codes for more information                                        | String |
| **deliveredAt**         | When the message was delivered. It is an Epoch Date                                                           | Long   |
| **deliveredDate**       | When the message was delivered. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone (ISO 8601) | String |
| **campaignId**          | Campaign Identifier                                                                                           | Long   |
| **extraInfo**           | Any extra information set by the user when the message was sent                                               | String |

Example of JSON Delivery Report (DR or DLR - Delivery to the user’s device)

{

&#x20;"id":"8f5af680-973e-11e4-ad43-4ee58e9a13a6",

&#x20;"correlationId":"myId",

&#x20;"carrierId":5,

&#x20;"carrierName":"TIM",

&#x20;"destination":"5519900001111",

&#x20;"sentStatusCode":2,

&#x20;"sentStatus":"SENT\_SUCCESS",

&#x20;"sentStatusAt":1420732929252,

&#x20;"sentStatusDate":"2015-01-08T16:02:09Z",

&#x20;"deliveredStatusCode":4,

&#x20;"deliveredStatus":"DELIVERED\_SUCCESS",

&#x20;"deliveredAt":1420732954000,

&#x20;"deliveredDate":"2015-01-08T16:02:34Z",

&#x20;"campaignId":1234

}

## User Response (MO)

The MO API allows you to automatize the process of retrieving messages sent by customers in response to the messages you have sent them. All requests use the GET method, and responses are sent in JSON format. IMPORTANT! MO receipt is enabled by default only for LAs 27182 and 28149; if you need to receive messages through other Las, you need to contact support for evaluation.

You can also set it so that MOs are forwarded as they arrive to an API of the customer; this is the most efficient manner, as you don’t have to make any calls, just handle messages as they arrive. For this setting to be made, you need to open a ticket with our support team at <customer.service@wavy.global> relaying the url that will receive MOs. We are able to send MOs via both GET method (query string) and POST method (JSON)

Example of JSON sent to your API (POST method)

{

&#x20;"id": "25950050-7362-11e6-be62-001b7843e7d4",

&#x20;"subAccount": "iFoodMarketing",

&#x20;"campaignAlias": "iFoodPromo",

&#x20;"carrierId": 1,

&#x20;"carrierName": "VIVO",

&#x20;"source": "5516981562820",

&#x20;"shortCode": "28128",

&#x20;"messageText": "I want pizza",

&#x20;"receivedAt": 1473088405588,

&#x20;"receivedDate": "2016-09-05T12:13:25Z",

&#x20;"mt": {

&#x20;"id": "8be584fd-2554-439b-9ba9-aab507278992",

&#x20;"correlationId": "1876",

&#x20;"username": "iFoodCS",

&#x20;"email": "<customer.support@ifood.com>"

&#x20;}

&#x20;}

​

Each request made will return MOs received during the last 3 days, up to a limit of 1,000 MOs. For previous dates or larger amounts, please contact our support team at <customer.service@wavy.global>

The behavior of the MO query list will be different for each authenticated user due to each user’s permission level.

We recommend the method of sending MOs to an API; every MO sent will automatically be sent to an API, thus all responses can be handled immediately after receipt

| Profile           | Permission                                                                                                                                                                                                                                                       |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Regular**       | each request made in the MO API will only return MOs that correspond to the subaccount the user belongs to. A regular user is not able to retrieve MOs from other subaccounts.                                                                                   |
| **Administrator** | the default behavior for the administrator user is to retrieve all MOs from all subaccounts. If an admin wishes to retrieve MOs from only one subaccount, they need to specify the subaccount in the subAccount parameter with the id of the desired subaccount. |

### Default MO Response Format

Example of JSON response to a Wavy API call:

{

&#x20;"total": 1,

&#x20;"start": "2016-09-04T11:12:41Z",

&#x20;"end": "2016-09-08T11:17:39.113Z",

&#x20;"messages": \[

&#x20;{

&#x20;"id": "25950050-7362-11e6-be62-001b7843e7d4",

&#x20;"subAccount": "iFoodMarketing",

&#x20;"campaignAlias": "iFoodPromo",

&#x20;"carrierId": 1,

&#x20;"carrierName": "VIVO",

&#x20;"source": "5516981562820",

&#x20;"shortCode": "28128",

&#x20;"messageText": "I want pizza",

&#x20;"receivedAt": 1473088405588,

&#x20;"receivedDate": "2016-09-05T12:13:25Z",

&#x20;"mt": {

&#x20;"id": "8be584fd-2554-439b-9ba9-aab507278992",

&#x20;"correlationId": "1876",

&#x20;"username": "iFoodCS",

&#x20;"email": "<customer.support@ifood.com>"

&#x20;}

&#x20;},

&#x20;{

&#x20;"id": "d3afc42a-1fd9-49ff-8b8b-34299c070ef3",

&#x20;"subAccount": "iFoodMarketing",

&#x20;"campaignAlias": "iFoodPromo",

&#x20;"carrierId": 5,

&#x20;"carrierName": "TIM",

&#x20;"source": "5519987565020",

&#x20;"shortCode": "28128",

&#x20;"messageText": "Is my burger arriving?",

&#x20;"receivedAt": 1473088405588,

&#x20;"receivedDate": "2016-09-05T12:13:25Z",

&#x20;"mt": {

&#x20;"id": "302db832-3527-4e3c-b57b-6a481644d88b",

&#x20;"correlationId": "1893",

&#x20;"username": "iFoodCS",

&#x20;"email": "<customer.support@ifood.com>"

&#x20;}

&#x20;}

&#x20;]

}

Both list and search requests return a JSON object with the following fields:

| Field        | Details                                     | Type    |
| ------------ | ------------------------------------------- | ------- |
| **total**    | Total number of MOs returned by the request | Integer |
| **start**    | Minimum query limit                         | String  |
| **end**      | Maximum query limit                         | String  |
| **messages** | List of objects                             | List    |

### **Each message in the messages field has the following structure:**

| Field             | Details                                                                                       | Type    |
| ----------------- | --------------------------------------------------------------------------------------------- | ------- |
| **id**            | Message ID                                                                                    | String  |
| **subAccount**    | subaccount responsible for sending the message that generated the response                    | String  |
| **carrierId**     | Carrier ID                                                                                    | Integer |
| **carrierName**   | Carrier name                                                                                  | String  |
| **source**        | Phone number that sent the response message                                                   | String  |
| **shortCode**     | Shortcode of the message that originated the response and through which the response was sent | String  |
| **messageText**   | Text of the response message                                                                  | String  |
| **receivedAt**    | Time of receipt                                                                               | Long    |
| **receivedDate**  | Date and time of receipt in UTC format                                                        | String  |
| **campaignAlias** | Alias of the campaign that originated the response                                            | String  |
| **mt**            | Original MT that generated the response                                                       | MT      |

### **MTs have the following structure:**

| Field             | Details                                             | Type   |
| ----------------- | --------------------------------------------------- | ------ |
| **id**            | MT ID                                               | String |
| **correlationId** | CorrelationID sent in the MT                        | String |
| **username**      | Username of the user responsible for sending the MT | String |
| **email**         | Email of the user responsible for sending the MT    | String |

### List MO Request

The List will return all MOs received since the last call according to the default response described above. Once this call is made, it will be consumed and will not return following calls.

As a regular user, to retrieve all MOs from a subaccount, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/list>

As an administrator user, to retrieve ALL MOs from ALL subaccounts, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/list>

As an administrator user, to retrieve MOs from a subaccount with the reference “referencia\_subconta”, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/list?subAccount=referencia\\_subconta>

### Search MO Request

The search request will return each MO received within a given period of time. You must set the start and end parameters to specify a time period, using the ISO-8601 format. START by default is set for 5 days prior to the current date, and END by default is set for the current date. You cannot retrieve MOs prior to 5 days.

As a regular user, to retrieve all MOs from a subaccount, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/search>

As an administrator user, to retrieve ALL MOs from ALL subaccounts, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/search>

As an administrator user, to retrieve MOs from a subaccount with the reference “referencia\_subconta”, use:

GET <https://api-messaging.wavy.global/v1/sms/receive/search?subAccount=referencia\\_subconta>

Search with set START and END parameters:

GET <https://api-messaging.wavy.global/v1/sms/receive/search?start=2016-09-12T00:00:00\\&end=2016-09-15T00:00:00>

Only with START specified (using default END, current date)

GET <https://api-messaging.wavy.globalv1/sms/receive/search?start=2016-09-12T00:00:00>

Only with END specified (using default START, 5 days prior to the current date)

GET <https://api-messaging.wavy.global/v1/sms/receive/search?end=2016-09-15T00:00:00>

Using default values for START and END and specifying the subaccount

GET <https://api-messaging.wavy.global/v1/sms/receive/search?subAccount=iFoodMarketing>

## Sent Status Codes

There are **two status levels** that are sent independently.

**1 - First Status (sent\_status - Sent Status = Callback)**

Status of delivery **to the carrier**, this is the first status we return, and all carriers have it.

| Code    | Message                                  | Meaning                                                                                                                                                                                                                         |
| ------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**   | **SENT\_SUCCESS**                        | Successfully delivered to the carrier (This is the status to be considered for billing purposes.)                                                                                                                               |
| **101** | **EXPIRED**                              | Expired before being delivered to the device                                                                                                                                                                                    |
| **102** | **CARRIER\_COMMUNICATION\_ERROR**        | Communication error with the carrier                                                                                                                                                                                            |
| **103** | **REJECTED\_BY\_CARRIER**                | The carrier has rejected the message                                                                                                                                                                                            |
| **201** | **NO\_CREDIT**                           | The message limit set by your company’s administrator, for your account or subaccount, has been exceeded. Or, if your company uses the pre-paid credit model, it has run out.                                                   |
| **202** | **INVALID\_DESTINATION\_NUMBER**         | The destination number is invalid (Not a valid mobile number).                                                                                                                                                                  |
| **203** | **BLACKLISTED**                          | The destination number is blacklisted and has been manually entered by your company.                                                                                                                                            |
| **204** | **DESTINATION\_BLOCKED\_BY\_OPTOUT**     | The destination number has opted out and no longer wishes to receive messages from this subaccount. (This status is specifically for mobile marketing accounts).                                                                |
| **205** | **DESTINATION\_MESSAGE\_LIMIT\_REACHED** | The destination number has already received the maximum number of messages that one company can send, within a period of time. (This status is specifically for Mobile Marketing accounts, and this is a rule set by carriers). |
| **207** | **INVALID\_MESSAGE\_TEXT**               | The text of your message contains words that are not accepted by the carrier. These words can be profanity, or, if yours is a Mobile Marketing account, they can be major brands.                                               |
| **301** | **INTERNAL\_ERROR**                      | An error occurred in Wavy’s platform.                                                                                                                                                                                           |

**2 - Second Status (delivered\_status - Delivery Report Callback)**

Status of delivery to **the device**, this is the second status we return and it only exists for cases where the first status above was successful, i.e., the message was successfully delivered to the carrier. In this status, we inform whether the message has been delivered to the device. Carriers Oi and Sercomtel do not have this second status level; for those carriers, the first status, i.e., whether the carrier has accepted your message, is the maximum information there is.

| Code    | Message                | Meaning                                                                                                                                                                                                                                                                                                                                                        |
| ------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **4**   | **DELIVERED\_SUCCESS** | Successfully delivered to the device.                                                                                                                                                                                                                                                                                                                          |
| **104** | **NOT\_DELIVERED**     | The carrier has accepted the message, but was unable to deliver it to the device. Potential causes: Device is off or has no signal for a given period of time (usually 24 hours, but for some carriers, such as Vivo, this retry period is 8 hours). Number is valid, but inactive (some carriers only return this kind of error in this second status level). |

## SMPP API

All services provided by Wavy must necessarily be encrypted, and the [SMPP](http://doc-messaging.movile.com/pt.html#termos-importantes) protocol does not have native encryption. In this case, we provide two options for integration:

### Option 1 - SMPP over TLS + IP whitelist (**Recommended option**)

This is the option we recommend. If your system does not have this functionality, click [HERE](http://doc-messaging.movile.com/pt.html#proxy-tls) to get help in setting up a TLS proxy.

In addition to the encryption to be done by TLS, access will only be authorized for the public IP of your server. (We accept multiple IPs and ranges) This information must be sent to the email address <customer.service@wavy.global>

If you need to allow outgoing traffic in your firewall, we recommend allowing any destination IP on port 2444; if not possible, you must include rules with the following allowances: 200.219.220.8:2444 200.219.220.193:2444 200.189.169.8:2444 189.36.59.86:2444 45.236.179.18:2444 45.236.179.19:2444

​

### Option 2 - SMPP over VPN

Encryption and access granting will be done through VPN.

If you choose this option, set up VPNs using the peers and hosts below, already including the phase 1 and 2 proposals you wish. Please send the completed VPN form for your company to <customer.service@wavy.global>

peer 200.155.0.250 hosts 200.219.220.8 and 200.219.220.193 port 2443

peer 200.143.57.150 hosts 200.189.169.8 and 189.36.59.86 port 2443

peer 45.236.178.12 hosts 45.236.179.18 and 45.236.179.19 port 2443

For high availability and load balancing reasons, you are required to set the **2** **VPNs**, as well as use the smpp-messaging.wavy.global.com domain as your SMPP client’s destination, instead of IPs.

​

## Connection Details

| Information                     | Details                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hostname**                    | smpp-messaging.wavy.global When setting your SMPP system, you must use the domain as destination, instead of IPs. This domain has 4 entry proxies with round robin DNS and health check, and multiple backend servers. Based on the volume of messages your company will transmit, we will increase the number of binds (connections) allowed simultaneously. |
| **Port**                        | 2444 (SMPP over TLS) or 2443 (VPN)                                                                                                                                                                                                                                                                                                                            |
| **SMPP Version**                | 3.4                                                                                                                                                                                                                                                                                                                                                           |
| **Bind Count**                  | Minimum of 4. Setting at least 4 binds is required to obtain high availability and load balancing.                                                                                                                                                                                                                                                            |
| **Character Encoding**          | GSM7 - Default (data\_coding = 0) (GSM3.38 extended table is not supported by carriers.) LATIN1 (data\_coding = 1) UCS2 (data\_coding=8). **Attention:** Check character and billing details [HERE](http://doc-messaging.movile.com/pt.html#characters).                                                                                                      |
| **Flash SMS**                   | Supported data\_coding=0x10 for GSM7 and data\_coding 0x18 for UCS2 When we receive flashSMS messages from our customers, they are sent to carriers as flashSMS; if the carrier does not support flashSMS, it is delivered as a normal SMS message.                                                                                                           |
| **Enquire-link**                | Minimum: 30 seconds / Maximum: 59 seconds.                                                                                                                                                                                                                                                                                                                    |
| **Concatenation**               | UDH 8-bit and 16-bit are supported / [UDH Headers](https://en.wikipedia.org/wiki/Concatenated_SMS).                                                                                                                                                                                                                                                           |
| **Default addr\_ton**           | 1                                                                                                                                                                                                                                                                                                                                                             |
| **Default addr\_npi**           | 1                                                                                                                                                                                                                                                                                                                                                             |
| **window size**                 | 10                                                                                                                                                                                                                                                                                                                                                            |
| **2way**                        | Supported                                                                                                                                                                                                                                                                                                                                                     |
| **SMPP bind type**              | Transceiver (Recommended). Separate transmit/receiver binds are also accepted.                                                                                                                                                                                                                                                                                |
| **SMPP system\_type**           | MovileSMSC                                                                                                                                                                                                                                                                                                                                                    |
| **SMPP source addr (senderID)** | When your service requires user responses (MO), the source address **must** match the system\_id, i.e., username. When your service does not require MOs, you can use anything in this field.                                                                                                                                                                 |
| **Max MO throughput**           | 80 per bind                                                                                                                                                                                                                                                                                                                                                   |
| **Max MT throughput**           | 80 per bind                                                                                                                                                                                                                                                                                                                                                   |
| **Server Timezone**             | UTC                                                                                                                                                                                                                                                                                                                                                           |
| **ID Format**                   | UUID                                                                                                                                                                                                                                                                                                                                                          |
| **Default validity\_period**    | 24 hours                                                                                                                                                                                                                                                                                                                                                      |

​

## Sent Status (Callback and DLR)

**1 - First Status (sent\_status - Sent Status = Callback)**

Status of delivery **to the carrier**, this is the first status we return, and all carriers have it.

| stat        | err | TLV (0x1403) | TLV (0x1404)                         | Meaning                                                                                                                                                                                                                         |
| ----------- | --- | ------------ | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ACCEPTD** | 000 | 2            | SENT\_SUCCESS                        | Successfully delivered to the carrier **(This is the status to be considered for billing purposes.)**                                                                                                                           |
| **EXPIRED** | 101 | 101          | EXPIRED                              | Expired before being delivered to the device.                                                                                                                                                                                   |
| **REJECTD** | 102 | 102          | CARRIER\_COMMUNICATION\_ERROR        | Communication error with the carrier.                                                                                                                                                                                           |
| **REJECTD** | 103 | 103          | REJECTED\_BY\_CARRIER                | The carrier has rejected the message.                                                                                                                                                                                           |
| **REJECTD** | 201 | 201          | NO\_CREDIT                           | The message limit set by your company’s administrator, for your account or subaccount, has been exceeded. Or, if your company uses the pre-paid credit model, it has run out.                                                   |
| **REJECTD** | 202 | 202          | INVALID\_DESTINATION\_NUMBER         | The destination number is invalid (Not a valid mobile number).                                                                                                                                                                  |
| **REJECTD** | 203 | 203          | BLACKLISTED                          | The destination number is blacklisted and has been manually entered by your company.                                                                                                                                            |
| **REJECTD** | 204 | 204          | DESTINATION\_BLOCKED\_BY\_OPTOUT     | The destination number has opted out and no longer wishes to receive messages from this subaccount. (This status is specifically for mobile marketing accounts).                                                                |
| **REJECTD** | 205 | 205          | DESTINATION\_MESSAGE\_LIMIT\_REACHED | The destination number has already received the maximum number of messages that one company can send, within a period of time. (This status is specifically for Mobile Marketing accounts, and this is a rule set by carriers). |
| **REJECTD** | 207 | 207          | INVALID\_MESSAGE\_TEXT               | The text of your message contains words that are not accepted by the carrier. These words can be profanity, or, if yours is a Mobile Marketing account, they can be major brands.                                               |
| **REJECTD** | 301 | 301          | INTERNAL\_ERROR                      | An error occurred in Wavy’s platform.                                                                                                                                                                                           |
| **UNKNOWN** | 301 | 301          | INTERNAL\_ERROR                      | An error occurred in Wavy’s platform.                                                                                                                                                                                           |

**2 - Second Status (delivered\_status - Delivery Report Callback)**

Status of delivery to **the device**, this is the second status we return and it only exists for cases where the first status above was successful, i.e., the message was successfully delivered to the carrier. In this status, we inform whether the message has been delivered to the device. Carriers Oi and Sercomtel do not have this second status level; for those carriers, the first status, i.e., whether the carrier has accepted your message, is the maximum information there is.

| stat        | err | TLV (0x1403) | TLV (0x1404)  | TLV (0x1405) | TLV (0x1406)       | Meaning                                                                                                                                                                                                                                                                                                                                                        |
| ----------- | --- | ------------ | ------------- | ------------ | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DELIVRD** | 000 | 2            | SENT\_SUCCESS | 4            | DELIVERED\_SUCCESS | Successfully delivered to the device.                                                                                                                                                                                                                                                                                                                          |
| **UNDELIV** | 104 | 2            | SENT\_SUCCESS | 104          | NOT\_DELIVERED     | The carrier has accepted the message, but was unable to deliver it to the device. Potential causes: Device is off or has no signal for a given period of time (usually 24 hours, but for some carriers, such as Vivo, this retry period is 8 hours). Number is valid, but inactive (some carriers only return this kind of error in this second status level). |

Statuses of delivery to the device, carrier, and MOs are queued if a connectivity problem occurs, but the time period is 8h; after this, you will no longer be able to obtain statuses through SMPP.

## TLS Proxy - Linux

The proxy is required if your connection is not made via VPN. As previously explained, the SMPP protocol does not have native TLS encryption; in this case we suggest the proxy below:

### HAProxy

### Installing the HAProxy

**Debian-Like**

In Debian-like distributions through the repository: sudo apt-get install haproxy

**RedHat-Like**

As there is currently no HAProxy package with TLS support already in the repository, you can download it from the official website: <http://www.haproxy.org/>

To the side, you will find a script for installation

sudo yum install wget gcc pcre-static pcre-devel -y

​

wget <http://www.haproxy.org/download/1.6/src/haproxy-1.6.3.tar.gz> -O \~/haproxy.tar.gz

tar xzvf \~/haproxy.tar.gz -C \~/

​

cd \~/haproxy-1.6.3

make TARGET=linux2628 USE\_LINUX\_TPROXY=1 USE\_ZLIB=1 USE\_REGPARM=1 USE\_OPENSSL=1 USE\_PCRE=1

sudo make install

sudo cp /usr/local/sbin/haproxy /usr/sbin/

sudo cp \~/haproxy-1.6.3/examples/haproxy.init /etc/init.d/haproxy

sudo chmod 755 /etc/init.d/haproxy

sudo mkdir -p /etc/haproxy

sudo mkdir -p /run/haproxy

sudo mkdir -p /var/lib/haproxy

sudo touch /var/lib/haproxy/stats

​

sudo useradd -r haproxy

sudo haproxy -vv

Setting up haproxy

global

&#x20;\# local2.\* /var/log/haproxy.log

&#x20;log 127.0.0.1 local2

​

&#x20;chroot /var/lib/haproxy

&#x20;pidfile /var/run/haproxy.pid

&#x20;ssl-server-verify none

&#x20;maxconn 4000

&#x20;user haproxy

&#x20;group haproxy

&#x20;daemon

&#x20;\# turn on stats unix socket

&#x20;stats socket /var/lib/haproxy/stats

​

resolvers dns

&#x20;nameserver google 8.8.8.8:53

&#x20;hold valid 1s

​

defaults

&#x20;log global

&#x20;option redispatch

&#x20;retries 3

&#x20;timeout http-request 10s

&#x20;timeout queue 1m

&#x20;timeout connect 10s

&#x20;timeout client 1m

&#x20;timeout server 1m

&#x20;timeout http-keep-alive 10s

&#x20;timeout check 10s

&#x20;maxconn 3000

​

frontend movile

&#x20;bind \*:2444

&#x20;mode tcp

&#x20;option tcplog

&#x20;use\_backend movile

​

backend movile

&#x20;mode tcp

&#x20;server smpp-messaging.movile.com smpp-messaging.wavy.global.com:2444 ssl resolvers dns check inter 15000

* Installing haproxy servers (red-hat / centos):

$sudo yum install -y openssl-devel haproxy

* Installing haproxy servers (debian / ubuntu)

$sudo apt-get install -y openssl-devel haproxy

* After installing, replace the entire content of the /etc/haproxy/haproxy.cfg file with the content to the side ->

**IMPORTANT:** Set your system (SMPP client) to use 127.0.0.1:2444 as destination address

## TLS Proxy - Windows

Setting up nginx

worker\_processes 2;

​

events {

&#x20;worker\_connections 1024;

}

​

stream {

&#x20;resolver 8.8.8.8 valid=1s;

&#x20;map $remote\_addr $backend {

&#x20;default smpp-messaging.wavy.global.com;

&#x20;}

&#x20;server {

&#x20;listen 2444;

&#x20;proxy\_pass $backend:2444;

&#x20;proxy\_ssl on;

&#x20;}

}

You can use nginx as a TLS proxy in Windows servers to encrypt the data

Download the version below (it is important to use this version, as older versions only resolve the name in the first request)

​<http://nginx.org/download/nginx-1.12.1.zip>​

Extract the .zip file to the desired location and replace the content of the conf/nginx.conf file with the data to the side

## SFTP API

### Connection Details

| ​                  | ​                                                            |
| ------------------ | ------------------------------------------------------------ |
| **Hostname**       | ftp-messaging.wavy.global                                    |
| **Port**           | 2222                                                         |
| **Protocol**       | SFTP (transfer over ssh, providing client-server encryption) |
| **Authentication** | username + password (provided by support)                    |
| **Portal**         | messaging.wavy.global                                        |

Your IPs must be allowed in Wavy’s firewalls. If you need to allow outgoing traffic in the firewall for port 2222, you must allow the DNS, or IPs 200.219.220.54, 200.189.169.53 and 45.236.179.22

## Sending Messages via SFTP

To trigger messages via SFTP, you need to generate a TXT file, with formatting following the example below:

**number;text;correlationId(optional);** **5511900000000;message 1;;** **5519900000000;message 2;;** **5521900000000;message 3;;** **EOF**

The name of the file to be sent must have the following format:

\<SUBACCOUNT\_ID>.\<DATE(YYYYMMDD)>.\<SEQUENCE> or \<SUBACCOUNT\_REFERENCE\_NAME>.\<DATE(YYYYMMDD)>.\<SEQUENCE>

Subaccounts (projects) can be created by the customer themself in the portal. If the nomenclature above is not followed, the messages will be sent by the customer’s default subaccount.

**Example:**

3486.20170101.01.txt or PROJECT1.20170101.01.txt

It is important to follow the set nomenclature so the messages can be discounted from the correct subaccount.

Afterwards, the file must be sent to the sftp server in the upload directory. The file will be moved to the success directory after it is done; if any error occurs, the file will be moved to the error directory.

## Number Validation API

API for validating phone numbers, where we return the current carrier of queried numbers (including ported numbers), or whether the number is invalid, i.e., it is not a mobile number.

IMPORTANT: Number lookup queries have a differentiated fee from SMS deliveries; before running a query, check with the head of the commercial team

### Authentication

To send messages and run queries in our API, you need to authenticate using a combination of username or email and a token.

| Field               | Details                                                                     | Data Type |
| ------------------- | --------------------------------------------------------------------------- | --------- |
| UserName            | Your username or email                                                      | String    |
| AuthenticationToken | Your authentication token. Check here and read username descriptions below. | String    |

### Connection Details

| ​                  | ​                         |
| ------------------ | ------------------------- |
| **Hostname**       | api-messaging.wavy.global |
| **APIs**           | /v1/carrier/lookup        |
| **Port**           | 443 (https)               |
| **Protocol**       | HTTPS (TLS encryption)    |
| **Authentication** | username + token          |
| **Portal**         | messaging.wavy.global     |

​

## HTTP Request via POST Method

curl --request POST \\

&#x20;\--url <https://api-messaging.wavy.global/v1/carrier/lookup> \\

&#x20;\--header 'authenticationtoken: \<authenticationtoken>' \\

&#x20;\--header 'username: \<username>' \\

&#x20;\--header 'Content-Type: application/json' \\

&#x20;\--data '{

&#x20;"destinations": \["+55(19)997712322", "5519997712322", "2312312"]

}'

POST <https://api-messaging.wavy.global/v1/carrier/lookup> Content-Type: application/json

To run a query, just add a json to the request body with the number array. You can run a query using the +55(19)999999999 and 5519999999999 formats

### Query Response

Call response in JSON format

{

&#x20;"id": "aadb5130-7dd7-11e7-baac-a6aabe61edb5",

&#x20;"destinations": \[

&#x20;{

&#x20;"destination": "5519997712322",

&#x20;"active": true,

&#x20;"carrier": {

&#x20;"name": "VIVO",

&#x20;"countryCode": "BR"

&#x20;}

&#x20;},

&#x20;{

&#x20;"destination": "5519997712322",

&#x20;"active": true,

&#x20;"carrier": {

&#x20;"name": "VIVO",

&#x20;"countryCode": "BR"

&#x20;}

&#x20;},

&#x20;{

&#x20;"destination": "2312312",

&#x20;"active": false,

&#x20;"carrier": {

&#x20;"name": "UNKNOWN"

&#x20;}

&#x20;}

&#x20;]

}

The last number in the example is an invalid number to shown now the query returns the JSON in such cases.

The batch query response will contain a JSON file with individual information on each queried number:

| Field            | Details                                                                                                                                | Type                  |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **id**           | UUID generated for this batch                                                                                                          | String                |
| **destinations** | This field is an array with the responses of the individual batch queries, it contains the id and correlationId of each queried number | IndividualResponse\[] |
| **destination**  | Queried phone number                                                                                                                   | Long                  |
| **active**       | number's status with the carrier (currently only checks whether the number belongs to the carrier, not active / in use)                | Boolean               |
| **carrier**      | Carrier and country to which the queried number belongs                                                                                | array\[]              |
| **name**         | Carrier name                                                                                                                           | String                |
| **countryCode**  | Country Code                                                                                                                           | String                |

## Accents & Special Characters

Messages containing **only** characters in the table below are charged for every 160 characters. If your message has **one or more** characters that are not in the table below, you will be charged for every 70 characters, as specified in the protocol of the carriers’ network.

| ​     | ​  | ​ | ​ | ​ | ​ | ​ | ​  | ​  | ​ | ​ | ​  |
| ----- | -- | - | - | - | - | - | -- | -- | - | - | -- |
| Space | (  | 0 | 8 | @ | H | P | X  | \` | h | p | x  |
| !     | )  | 1 | 9 | A | I | Q | Y  | a  | i | q | y  |
| “     | \* | 2 | : | B | J | R | Z  | b  | j | r | z  |
| #     | +  | 3 | ; | C | K | S | {  | c  | k | s | \~ |
| $     | ,  | 4 | < | D | L | T | \\ | d  | l | t | ​  |
| %     | -  | 5 | = | E | M | U | }  | e  | m | u | ​  |
| &     | .  | 6 | > | F | N | V | ^  | f  | n | v | ​  |
| ‘     | /  | 7 | ? | G | O | W | \_ | g  | o | w | ​  |

Notes:

• Please request our support team to enable the use of accents and special characters.

• If the destination carrier does not accept accents and characters (Sercomtel), our platform automatically replaces them for our customers, such as: á to a, é to e, etc.

## Long Texts (Concatenation)

The protocol used in the carriers’ network has 70- or 160-character limits for messages with or without **special characters**, respectively. But you can send longer messages using concatenation, where the device regroups messages upon receipt.

For customers integrated via HTTPS, SFTP, or MQ, there are no additional indicators in order to activate concatenation, just send the long message text in a single request.

For customers integrated via SMPP, you must use the concatenation feature with indicators in the header (UDH), [LINK](https://en.wikipedia.org/wiki/Concatenated_SMS).

It is worth noting that, despite appearing on the device as a single long message, messages still travel through carriers’ networks individually, and, in this case, we continue being charged and charging individually for every 63 or 160 characters (depending on the **characters** used). Reminding that, when you use concatenation, part of the characters (70 or 160) are used by the header header.

Note: In cases of carriers that do not support the concatenation feature (e.g.: Sercomtel), Wavy sends the messages separately, without concatenating, and includes order indicators automatically for our customers. E.g.:

​
