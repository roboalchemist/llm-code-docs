# Source: https://docs.sinch.com/technical-documentation/api-and-integrations/whatsapp-api.md

# WhatsApp API

## WhatsApp API

Technical Documentation: WhatsApp API

### WhatsApp API

This documentation provides information on how your application can send WhatsApp messages via API using the Wavy Messaging platform.

Here you will also find information on **Webhooks,** which are HTTP call returns set by the user that are triggered by specific events. Whenever a trigger event occurs, Wavy’s API will collect the data and immediately send a notification (HTTP request) to the URL chosen by our customer, updating the status of messages sent or letting you know when you receive a message.

Wavy Messaging’s API allows you to send single or bulk messages.

The API has REST integration, using HTTP protocol with TLS, supporting the POST method with parameters sent in JSON format.

### **Prerequisites**

1. To use Wavy Messaging’s API, first you need to have an active account on the Wavy Messaging platform. Refer to our documentation on [Account & Settings](https://docs.wavy.global/getting-started/wavy-messaging-platform/conta-e-configuracoes) for more information on how to follow this procedure.
2. You must also have a valid username and token associated with this account. Learn how to create your username in our [Adding Users](https://docs.wavy.global/permissoes/subcontas-e-usuarios#adicionar-usuarios) guide.
3. With the above credentials, you can already start using Wavy Messaging’s API.

​

### **Connection Details**

| ​                  | ​                         |
| ------------------ | ------------------------- |
| **Hostname**       | api-messaging.wavy.global |
| **Port**           | 443 (https)               |
| **Protocol**       | HTTPS (TLS encryption)    |
| **Authentication** | username + token          |
| **Encoding**       | UTF-8                     |

## **Making Calls to Wavy Messaging’s API**

To make your first calls, we recommend using the “[Postman](https://www.postman.com/downloads/)” application with requests in JSON format instead of starting out already writing code in other languages.

**Note: In order to send test messages, you need to have an approved message template in your WhatsApp Business account. Refer to our documentation on** [**Creating WhatsApp Message Templates**](https://docs.wavy.global/whatsapp/cadastro-de-template) **to create your first templates.**

If you do not yet have any approved message templates, you can still send test messages as long as the recipient interacts with the source number. This way, a customer service window will be activated. It allows you to send any type of message within a 24-hour window. If your message arrives, it means your request to Wavy Messaging’s API was successful. If not, check your Webhook for notifications that could indicate any issues.

**Messages:**

Calls to Wavy Messaging’s API are sent to <https://api-messaging.wavy.global/v1/whatsapp/send> in POST format regardless of message type, but the content of the JSON message’s body varies for each type of message.

The authentication fields in the header will also follow the same format regardless of message type:

POST /v1/whatsapp/send HTTP/1.1 Host: api-messaging.movile.com UserName: user\_name AuthenticationToken: aaaaaa-bbbbbbbbbbbbbXXXXX12 Content-Type: application/json

### **Sending a Template**

### **Destinations**

| **Name**         | Required | Description                                     |
| ---------------- | -------- | ----------------------------------------------- |
| **destinations** | Yes      | Details on sent and destination identifiers     |
| **message**      | Yes      | Details on the MESSAGE object that will be sent |

### **Destination**

| Name              | Required | ​ | Description                                                                                                                                                       |
| ----------------- | -------- | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **correlationId** | No       | ​ | Id set by the customer that will be returned in the message status (callback). You can use this id to track sent messages in a customized manner.                 |
| **destination**   | Yes      | ​ | Phone number that will receive the message (country code (55 for Brazil) and area code are required). Examples: 5519900001111, +5519900001111, +55(19) 900001111. |

### **Message**

| Name         | ​ | Required | ​ | Description                                                                                                                                           |
| ------------ | - | -------- | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ttl**      | ​ | No       | ​ | Time to live in days. It sets the maximum number of days in which the message should be delivered. Valid from 1 to 30. Default value is 7 if not set. |
| **template** | ​ | Yes      | ​ | Details on the TEMPLATE object that will be sent                                                                                                      |

### **Template**

| **Name**         | ​ | Required                                            | ​ | Description                                                                                                                                                                                                           |
| ---------------- | - | --------------------------------------------------- | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **namespace**    | ​ | Yes                                                 | ​ | ID of the namespace that will be used. **NOTE:** The namespace and element\_name parameters must match the Business Manager with which the source number is associated, otherwise the message will fail when sending. |
| **elementName**  | ​ | Yes                                                 | ​ | Name of the registered and approved template.                                                                                                                                                                         |
| **header**       | ​ | Yes, when the Template has parameters in the header | ​ | Header objects with their parameters                                                                                                                                                                                  |
| **languageCode** | ​ | Yes                                                 | ​ | Name of the registered and approved template.                                                                                                                                                                         |

### **Header**

| **Name**    | Required | Description                                                                                             |
| ----------- | -------- | ------------------------------------------------------------------------------------------------------- |
| **title**   | Optional | Title must have no more than 60 characters                                                              |
| **element** | Yes      | <p>Options:</p><p>text (default),</p><p>image,</p><p>audio,</p><p>document,</p><p>hsm,</p><p>video.</p> |

### **Element**

| **Name**    | ​ | Required | ​ | Description                               |
| ----------- | - | -------- | - | ----------------------------------------- |
| **url**     | ​ | Yes      | ​ | Media URL. Use only with HTTP/HTTPS URLs. |
| **type**    | ​ | Yes      | ​ | Type of media (JPEG, MP3, PDF, etc.)      |
| **caption** | ​ | Yes      | ​ | Name of media                             |

​

## **Webhooks**

Webhooks (or callbacks) are HTTP call returns set by the user that are triggered by specific events. Whenever a trigger event occurs, Wavy’s API will collect the data and immediately send a notification (HTTP request) to the URL chosen by the customer updating the status of messages sent or letting you know when you receive a message.

When your customer sends you a message, Wavy Messaging’s API will send a POST HTTP request notification to the **Webhook**’s URL with the details.

It is important that your **Webhook** returns a 200 OK HTTPS response to notifications (within 200 ms or asynchronously). Otherwise, Wavy Messaging’s API will consider this notification to have failed and will try again after some delay.

**Important: The URL where you will receive Webhooks must be set up by our support team.**

### **General Format of a Webhook**

| **Name**     | Object Content                 |
| ------------ | ------------------------------ |
| **messages** | Incoming message notifications |
| **statuses** | Message status updates         |

### Status

| Status                 | Description                           | WhatsApp Equivalent for Mobile Devices |
| ---------------------- | ------------------------------------- | -------------------------------------- |
| **SENT\_SUCCESS**      | Message received by WhatsApp’s server | One check mark                         |
| **DELIVERED\_SUCCESS** | Message delivered to the recipient    | Two check marks                        |
| **READ\_SUCCESS**      | Message read by the recipient         | Two blue check marks                   |

### Errors

| **HTTP Code** | **Description**                              |
| ------------- | -------------------------------------------- |
| **2xx**       | **Success**                                  |
| **200**       | **Success (OK)**                             |
| **201**       | **Successfully Created (For POST requests)** |
| **302**       | **Found**                                    |
| **4xx**       | **Client Errors**                            |
| **400**       | **Bad Request**                              |
| **401**       | **Unauthorized**                             |
| **403**       | **Forbidden**                                |
| **404**       | **Not Found**                                |
| **405**       | **Method Not Allowed**                       |
| **412**       | **Precondition Failed**                      |
| **420**       | **Message is Rate Limited**                  |
| **429**       | **Too Many Requests**                        |
| **5xx**       | **Server Errors**                            |
| **500**       | **Internal Server Error**                    |
| **504**       | **Timeout**                                  |

### Other Statuses

| Sent Code | Delivery Code | Status                           | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------- | ------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 102       | ​             | CARRIER COMMUNICATION ERROR      | Error in uploading media to WhatsApp                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 103       | ​             | REJECTED\_BY\_CARRIER            | A databank error has occurred                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2         | 101           | EXPIRED                          | Message expired                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 2         | 104           | NOT\_DELIVERED                   | <p>Potential Causes:</p><p>Limit reached -too many attempts to send messages, or failure to send message because the destination phone number is part of an experiment, or the template structure does not exist, or failure to send message because the destination number is outside the 24h service window to receive messages freely, or an error occurred when uploading media (unknown error),</p><p>or failure to send message because your account is ineligible on Facebook Business Manager,</p><p>or there was a temporary upload failure. Please try again later.</p> |
| 202       | ​             | INVALID\_DESTINATION\_NUMBER     | Invalid WhatsApp contact                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 204       | ​             | DESTINATION\_BLOCKED\_BY\_OPTOUT | Destination blocked by Opt-Out                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 206       | ​             | INVALID\_MESSAGE\_LENGTH         | Message is too long                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 207       | ​             | INVALID\_MESSAGE\_TEXT           | Invalid parameter value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 209       | ​             | INVALID\_CONTENT                 | Invalid type of UNKNOWN message                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 210       | ​             | INVALID\_SESSION                 | Session or service window is not open and no fallback Template is set up                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 311       | ​             | INTERNAL\_ERROR                  | Unable to verify WhatsApp API contacts                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

### **Messages (MO)**

When a customer sends you a message, Wavy Messaging’s API will send a POST HTTP request to the **Webhook’s URL with the details**.

It is important that your **Webhook** returns a 200 OK HTTPS response to notifications (within 200 ms or asynchronously). Otherwise, Wavy Messaging’s API will consider this notification to have failed and will try again after some delay.

**Important: The URL where you will receive Webhooks must be set up by our support team.**

## Common HTTP Status Code Responses

### Successful Request Response (200)

{

&#x20;"Id": "5efc3581-b8e8-11e7-9895-a6aabe61edb5",

&#x20;"destination": \[{

&#x20;"id": "5efc3581-b8e8-11e7-9895-a6aabe61edb5",

&#x20;"correlationId": "MyCorrelationId",

&#x20;"destination": "5519900001111."

}]

}

If your request is successfully run, a list of destinations with the generated uuids will be returned:

### Authentication Error Response (401)

{

&#x20;"errorCode": 401,

&#x20;"errorMessage": "Authentication Error: No user was found with this combination of username and Authentication token."

}

If a problem occurs with authentication, the following message will be returned:

### Status Update Callback

Example

{

&#x20;"total": 1,

&#x20;"data": \[

&#x20;{

&#x20;"id": "8995c40f-1c3a-48d0-98ee-bbc603622a91",

&#x20;"correlationId": "...",

&#x20;"destination": "5519900000000",

&#x20;"origin": "5519900000000",

&#x20;"campaignId": 100,

&#x20;"campaignAlias": "...",

&#x20;"flowId": "...",

&#x20;"extraInfo": "...",

&#x20;"sent": true,

&#x20;"sentStatusCode": 1,

&#x20;"sentStatus": "sent status",

&#x20;"sentDate": "2017-12-18T17:09:31.891Z",

&#x20;"sentAt": 1513616971891,

&#x20;"delivered": true,

&#x20;"deliveredStatusCode": 1,

&#x20;"deliveredStatus": "delivered status",

&#x20;"deliveredDate": "2017-12-18T17:09:31.891Z",

&#x20;"deliveredAt": 1513616971891,

&#x20;"read": true,

&#x20;"readDate": "2017-12-18T17:09:31.891Z",

&#x20;"readAt": 1513616971891,

&#x20;"updatedDate": "2017-12-18T17:09:31.891Z",

&#x20;"updatedAt": 1513616971891

&#x20;}

&#x20;],

&#x20;"clientInfo": {

&#x20;"customerId": 42,

&#x20;"subAccountId": 1291,

&#x20;"userId": 1

&#x20;}

}

For every status update of sent messages (receipt of delivery to the end user, message read, etc.), a callback/webhook is sent. Callbacks are sent in bulk.

Important: The endpoint that the webhook will use to send statuses must be set up by our support and operations team.

The return format will have the following description:

| Field          | Details                          | Type       |
| -------------- | -------------------------------- | ---------- |
| **total**      | Number of callbacks in the call. | String     |
| **data**       | List of Callbacks.               | Data\[]    |
| **clientInfo** | Client information.              | ClientInfo |

### Data:

| Field                   | Details                                                                                                                                                              | Type    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **id**                  | Last message id.                                                                                                                                                     | String  |
| **correlationId**       | Unique ID set by you to compare to the message status (Callback and DLR). This parameter is optional, and you can use the ID generated by Wavy Messaging to compare. | String  |
| **destination**         | Phone number to which your message was sent (including country code). E.g.: 5511900000000.                                                                           | String  |
| **origin**              | Phone number that identifies the WhatsApp Account (including country code). E.g.: 5511900000000.                                                                     | String  |
| **campaignId**          | Previously set campaignID.                                                                                                                                           | String  |
| **campaignAlias**       | Previously set campaign alias.                                                                                                                                       | String  |
| **extraInfo**           | Extra information sent with the original message.                                                                                                                    | String  |
| **sent**                | Indicates whether the message has been sent.                                                                                                                         | Boolean |
| **sentStatusCode**      | Status Code generated by Wavy Messaging for the message indicating its sent status.                                                                                  | Number  |
| **sentStatus**          | Sent status description.                                                                                                                                             | Boolean |
| **sentDate**            | Date the message was sent. Format: yyyy-MM-dd’T'HH:mm:ssZ.                                                                                                           | String  |
| **sentAt**              | Time the message was sent, using Unix\_time format                                                                                                                   | Number  |
| **delivered**           | Indicates whether the message has been delivered to its destination.                                                                                                 | Boolean |
| **deliveredStatusCode** | Status Code generated by Wavy Messaging indicating whether the message has been delivered.                                                                           | Number  |
| **deliveredStatus**     | Delivered status description.                                                                                                                                        | String  |
| **deliveredDate**       | Date the message was delivered. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                                                       | String  |
| **deliveredAt**         | Time the message was delivered, using Unix\_time format                                                                                                              | Number  |
| **read**                | Indicates whether the message has been read by the recipient.                                                                                                        | Boolean |
| **readDate**            | Date the message was read. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                                                            | String  |
| **readAt**              | Time the message was read, using Unix\_time format                                                                                                                   | String  |
| **updatedDate**         | Date the message status was updated. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                                                  | String  |
| **updatedAt**           | Time the message status was updated, using Unix\_time format                                                                                                         | String  |

### ClientInfo

| Field            | Details                    | Type   |
| ---------------- | -------------------------- | ------ |
| **customerId**   | Customer identification.   | Number |
| **subAccountId** | Subaccount identification. | Number |
| **userId**       | User identification.       | Number |

### Status

Statuses that can be sent in the callback:

| Status                                  | Sent Code | Delivery Code | Meaning                                                                                                                                               |
| --------------------------------------- | --------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CARRIER\_COMMUNICATION\_ERROR**       | 102       | ​             | Error in uploading media to WhatsApp.                                                                                                                 |
| **REJECTED\_BY\_CARRIER**               | 103       | ​             | A databank error has occurred.                                                                                                                        |
| **SENT\_SUCCESS**                       | 2         | ​             | ​                                                                                                                                                     |
| **EXPIRED**                             | 2         | 101           | Message expired.                                                                                                                                      |
| ​                                       | ​         | ​             | Failure to send message because it is too old.                                                                                                        |
| **NOT\_DELIVERED**                      | 2         | 104           | Limit reached - too many attempts to send messages.                                                                                                   |
| ​                                       | ​         | ​             | Failure to send message because this user’s phone number is part of an experiment.                                                                    |
| ​                                       | ​         | ​             | Structure unavailable: Customer unable to display HSM.                                                                                                |
| ​                                       | ​         | ​             | Failure to send message because you are outside the support window for freely messaging this user. Please use a valid HSM notification or reconsider. |
| ​                                       | ​         | ​             | Error uploading media (unknown error).                                                                                                                |
| ​                                       | ​         | ​             | Failure to send message because your account is ineligible. Please verify your WhatsApp Business account.                                             |
| ​                                       | ​         | ​             | Temporary upload failure. Please try again later.                                                                                                     |
| **DELIVERED\_SUCCESS**                  | 2         | 4             | ​                                                                                                                                                     |
| **READ\_SUCCESS**                       | 2         | 5             | ​                                                                                                                                                     |
| **INVALID\_DESTINATION\_NUMBER**        | 202       | ​             | Invalid WhatsApp contact.                                                                                                                             |
| **DESTINATION\_BLOCKED\_BY\_OPTOUT**    | 204       | ​             | Destination blocked by Opt-Out.                                                                                                                       |
| **INVALID\_MESSAGE\_LENGTH**            | 206       | ​             | Message is too long.                                                                                                                                  |
| **INVALID\_MESSAGE\_TEXT**              | 207       | ​             | Invalid parameter value.                                                                                                                              |
| **INVALID\_CONTENT**                    | 209       | ​             | Invalid type of UNKNOWN message.                                                                                                                      |
| **INVALID\_SESSION**                    | 210       | ​             | Session is not open and no fallback HSM is set up.                                                                                                    |
| **DESTINATION\_BLOCKED\_BY\_OPTIN**     | 211       | ​             | ​                                                                                                                                                     |
| **DESTINATION\_BLOCKED\_BY\_WHITELIST** | 212       | ​             | ​                                                                                                                                                     |
| **INTERNAL\_ERROR**                     | 311       | ​             | Unable to verify WhatsApp API contacts.                                                                                                               |

### MO (Messages Sent by the End User to the WhatsApp Account)

Text message example:

{

&#x20;"total": 1,

&#x20;"data": \[

&#x20;{

&#x20;"id": "ce425ffe-bc62-421f-9261-e6819a5eab43",

&#x20;"source": "5519900000000",

&#x20;"origin": "5519900000000",

&#x20;"userProfile": {

&#x20;"name": "username"

&#x20;},

&#x20;"campaignId": 100,

&#x20;"correlationId": "...",

&#x20;"campaignAlias": "...",

&#x20;"flowId": "....",

&#x20;"extraInfo": "...",

&#x20;"message": {

&#x20;"type": "TEXT",

"messageText": "Hello, this is a user message."

&#x20;},

&#x20;"receivedAt": 1513616971473,

&#x20;"receivedDate": "2017-12-18T17:09:31.473Z"

&#x20;}

&#x20;]

}

Extra Info example:

{

&#x20;"segmentation\_list":\[

&#x20;{

&#x20;"id":26,

&#x20;"customerId":42,

&#x20;"subAccountId":0,

&#x20;"name":"Movile WhatsApp Segmentation List",

&#x20;"active":true

&#x20;},

&#x20;{

&#x20;"id":27,

&#x20;"customerId":43,

&#x20;"subAccountId":0,

&#x20;"name":"Movile WhatsApp Segmentation List 2",

&#x20;"active":true

&#x20;}

&#x20;]

}

Media message example

{

&#x20;"total": 1,

&#x20;"data": \[

&#x20;{

&#x20;"id": "ce425ffe-bc62-421f-9261-e6819a5eab43",

&#x20;"source": "5519900000000",

&#x20;"origin": "5519900000000",

&#x20;"userProfile": {

&#x20;"name": "username"

&#x20;},

&#x20;"campaignId": 100,

&#x20;"correlationId": "...",

&#x20;"campaignAlias": "...",

&#x20;"flowId": "....",

&#x20;"extraInfo": "...",

&#x20;"message": {

&#x20;"type": "IMAGE",

&#x20;"mediaUrl": "https\://...",

&#x20;"mimeType": "image/jpg",

&#x20;"caption": "..."

&#x20;},

&#x20;"receivedAt": 1513616971473,

&#x20;"receivedDate": "2017-12-18T17:09:31.473Z"

&#x20;}

&#x20;]

}

Location message example:

{

&#x20;"total": 1,

&#x20;"data": \[

&#x20;{

&#x20;"id": "ce425ffe-bc62-421f-9261-e6819a5eab43",

&#x20;"source": "5519900000000",

&#x20;"origin": "5519900000000",

&#x20;"userProfile": {

&#x20;"name": "username"

&#x20;},

&#x20;"campaignId": 100,

&#x20;"correlationId": "...",

&#x20;"campaignAlias": "...",

&#x20;"flowId": "....",

&#x20;"extraInfo": "...",

&#x20;"message": {

&#x20;"location": {

&#x20;"geoPoint": "-22.894180,-47.047960",

&#x20;"name": "Wavy",

&#x20;"address": "Av. Cel. Silva Telles"

&#x20;}

&#x20;},

&#x20;"receivedAt": 1513616971473,

&#x20;"receivedDate": "2017-12-18T17:09:31.473Z"

&#x20;}

&#x20;]

}

Contact message example:

{

&#x20;"total": 1,

&#x20;"data": \[

&#x20;{

&#x20;"id": "ce425ffe-bc62-421f-9261-e6819a5eab43",

&#x20;"source": "5519900000000",

&#x20;"origin": "5519900000000",

&#x20;"userProfile": {

&#x20;"name": "username"

&#x20;},

&#x20;"campaignId": 100,

&#x20;"correlationId": "...",

&#x20;"campaignAlias": "...",

&#x20;"flowId": "....",

&#x20;"extraInfo": "...",

&#x20;"message": {

&#x20;"contacts":\[

&#x20;{

&#x20;"addresses":\[

&#x20;{

&#x20;"city":"Menlo Park",

&#x20;"country":"United States",

&#x20;"country\_code":"us",

&#x20;"state":"CA",

&#x20;"street":"1 Hacker Way",

&#x20;"type":"HOME",

&#x20;"zip":"94025"

&#x20;},

&#x20;{

&#x20;"city":"Menlo Park",

&#x20;"country":"United States",

&#x20;"country\_code":"us",

&#x20;"state":"CA",

&#x20;"street":"200 Jefferson Dr",

&#x20;"type":"WORK",

&#x20;"zip":"94025"

&#x20;}

&#x20;],

&#x20;"birthday":"2012-08-18",

&#x20;"emails":\[

&#x20;{

&#x20;"email":"<test@fb.com>",

&#x20;"type":"WORK"

&#x20;},

&#x20;{

&#x20;"email":"<test@whatsapp.com>",

&#x20;"type":"WORK"

&#x20;}

&#x20;],

&#x20;"name":{

&#x20;"first\_name":"John",

&#x20;"formatted\_name":"John Smith",

&#x20;"last\_name":"Smith"

&#x20;},

&#x20;"org":{

&#x20;"company":"WhatsApp",

&#x20;"department":"Design",

&#x20;"title":"Manager"

&#x20;},

&#x20;"phones":\[

&#x20;{

&#x20;"phone":"+1 (940) 555-1234",

&#x20;"type":"HOME"

&#x20;},

&#x20;{

&#x20;"phone":"+1 (650) 555-1234",

&#x20;"type":"WORK",

&#x20;"wa\_id":"16505551234"

&#x20;}

&#x20;],

&#x20;"urls":\[

&#x20;{

&#x20;"url":"<https://www.fb.com>",

&#x20;"type":"WORK"

&#x20;}

&#x20;]

&#x20;}

&#x20;]

&#x20;},

&#x20;"receivedAt": 1513616971473,

&#x20;"receivedDate": "2017-12-18T17:09:31.473Z"

&#x20;}

&#x20;]

}

For each reply from the end user (MO or Mobile Originated), a callback/webhook is sent. These MOs are sent in bulk.

Important: The endpoint that the webhook will use to send statuses must be set up by our support and operations team.

The return format will have the following description:

| Field             | Details                                                                                                                                                              | Type        |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| **total**         | Number of callbacks for the call.                                                                                                                                    | String      |
| **data**          | List of Mobile Originated (MO) messages.                                                                                                                             | Data\[]     |
| Field             | Details                                                                                                                                                              | Type        |
| **id**            | Last message identification                                                                                                                                          | String      |
| **source**        | Sender’s phone number                                                                                                                                                | String      |
| **origin**        | Phone number that identifies the WhatsApp Account (including country code). E.g.: 5511900000000.                                                                     | String      |
| **userProfile**   | Profile of the user who sent the message                                                                                                                             | UserProfile |
| **correlationId** | Unique ID set by you to compare to the message status (Callback and DLR). This parameter is optional, and you can use the ID generated by Wavy Messaging to compare. | String      |
| **campaignId**    | Previously set campaignID.                                                                                                                                           | String      |
| **campaignAlias** | Previously set campaign alias.                                                                                                                                       | String      |
| **message**       | MO message.                                                                                                                                                          | message     |
| **receivedAt**    | Date the message was received. Format: yyyy-MM-dd’T'HH:mm:ssZ                                                                                                        | String      |
| **receivedDate**  | Date the message was received, using Unix\_time format                                                                                                               | String      |
| **extraInfo**     | Extra information related to the message. Format: **Json**                                                                                                           | String      |

### **MO Flow Control - Segmentation Lists**

The message will have a list of segmentation lists in the extraInfo field. Our partners use it to direct messages to certain flows. The key name is **segmentation\_lists** and it contains a list of **SegmentationList**.

| Field            | Details                      | Type    |
| ---------------- | ---------------------------- | ------- |
| **id**           | Segmentation list identifier | Integer |
| **customerId**   | Customer identifier          | Integer |
| **subAccountId** | Subaccount identifier        | Integer |
| **name**         | Name of segmentation list    | String  |
| **active**       | Status of segmentation list  | Boolean |

### Message:

| Field           | Details                                                               | Type       |
| --------------- | --------------------------------------------------------------------- | ---------- |
| **type**        | Type of message sent to the end user: TEXT - IMAGE - AUDIO - DOCUMENT | String     |
| **messageText** | Text message (MO) sent by the end user.                               | String     |
| **waGroupId**   | Group to which the message was sent.                                  | String     |
| **mediaUrl**    | Url to download media sent by the end user.                           | String     |
| **mimeType**    | Mime type of the file sent by the end user.                           | String     |
| **caption**     | Media label sent by the end user.                                     | String     |
| **location**    | Location sent by the end user.                                        | Location   |
| **contacts**    | Contacts sent by the end user.                                        | Contact\[] |

### UserProfile:

| Field    | Required | Details           | Type   |
| -------- | -------- | ----------------- | ------ |
| **name** | No       | User profile name | String |

### Location:

| Field        | Details                                                     | Type   |
| ------------ | ----------------------------------------------------------- | ------ |
| **name**     | Location name.                                              | String |
| **address**  | Location address.                                           | String |
| **geoPoint** | Geopoint sent by the end user. Format: “latitude,longitude” | String |

### Contact:

| Field         | Required | Details                                    | Type       |
| ------------- | -------- | ------------------------------------------ | ---------- |
| **addresses** | No       | Full address(es) of the contact.           | Address\[] |
| **birthday**  | No       | Birthday in YYYY-MM-DD format.             | String     |
| **emails**    | No       | Email address(es) of the contact.          | Email\[]   |
| **name**      | No       | Full name of the contact.                  | Name       |
| **org**       | No       | Information of the contact’s organization. | Org        |
| **phones**    | No       | Phone number(s) of the contact.            | Phone\[]   |
| **urls**      | No       | URL(s) of the contact.                     | Url\[]     |

### Address:

| Field             | Required | Details                             | Type   |
| ----------------- | -------- | ----------------------------------- | ------ |
| **street**        | No       | Street name and number.             | String |
| **city**          | No       | City name.                          | String |
| **state**         | No       | State abbreviation.                 | String |
| **zip**           | No       | Zip code.                           | String |
| **country**       | No       | Full country name.                  | String |
| **country\_code** | No       | Country abbreviation (Two letters). | String |
| **type**          | No       | Default Values: HOME, WORK.         | String |

### Email:

| Field     | Required | Details                     | Type   |
| --------- | -------- | --------------------------- | ------ |
| **email** | No       | Email address.              | String |
| **type**  | No       | Default Values: HOME, WORK. | String |

### Name:

| Field               | Required | Details                           | Type   |
| ------------------- | -------- | --------------------------------- | ------ |
| **first\_name**     | No       | First name.                       | String |
| **last\_name**      | No       | Last name.                        | String |
| **middle\_name**    | No       | Middle name.                      | String |
| **name\_suffix**    | No       | Name suffix.                      | String |
| **name\_prefix**    | No       | Name prefix.                      | String |
| **formatted\_name** | No       | Full name as it normally appears. | String |

### Org:

| Field          | Required | Details                             | Type   |
| -------------- | -------- | ----------------------------------- | ------ |
| **company**    | No       | Name of the contact’s organization. | String |
| **department** | No       | Name of the contact’s department.   | String |
| **title**      | No       | Contact’s corporate title.          | String |

### Phone:

| Field      | Required | Details                                         | Type   |
| ---------- | -------- | ----------------------------------------------- | ------ |
| **phone**  | No       | Formatted phone number.                         | String |
| **type**   | No       | Default values: CELL, MAIN, IPHONE, HOME, WORK. | String |
| **wa\_id** | No       | WhatsApp identifier.                            | String |

### Url:

| Field     | Required | Details                     | Type   |
| --------- | -------- | --------------------------- | ------ |
| **phone** | No       | URL of the contact.         | String |
| **type**  | No       | Default values: HOME, WORK. | String |

For objects containing a type field, the listed values are simply considered default values that can be seen; however, you can set the field to any descriptive value you choose.

## WhatsApp SFTP API

#### Connection Details

| ​                  | ​                                                            |
| ------------------ | ------------------------------------------------------------ |
| **Hostname**       | ftp-messaging.wavy.global                                    |
| **Port**           | 2222                                                         |
| **Protocol**       | SFTP (transfer over ssh, providing client-server encryption) |
| **Authentication** | username + password (provided by support)                    |

Your IPs must be allowed in Movile’s firewalls. If you need to allow outgoing traffic in the firewall for port 2222, you must allow the DNS, or IPs 200.219.220.54, 200.189.169.53 and 45.236.179.22

### Sending Messages via SFTP

To trigger messages via FTP, you need to generate a file with formatting following the example below: HSM Message:

**2018-10-16;10:00;20:00;HSM;chatclub\_welcome;pt\_BR;DETERMINISTIC;name|company** **phone;name;company** **551999999999;Name1;Wavy** **551999999999;Name2;Movile**

| 1st Line                                                |
| ------------------------------------------------------- |
| Send date (for scheduling cases)                        |
| Start send time (for scheduling cases)                  |
| End send time (for scheduling cases)                    |
| Message type must be: **HSM**                           |
| HSM name (elementName)                                  |
| HSM language (languageLocale)                           |
| HSM language Deterministic or Fallback (languagePolicy) |
| name of HSM parameters                                  |

### **Notes for the First Line:**

1 - Parameter names must match the column names

2 - Information that will not be used may be left blank, however you should keep the semicolon as separation. Example of a case where we did not use scheduling (the first fields are between semicolons and have no information within): ; ; ; HSM;chatclub\_welcome;pt\_BR;DETERMINISTIC;name|company

3 - By default, the languagePolicy will be Deterministic.

4 - The names of HSM parameters should be separated by “ | ” and not by “ ; ”

| 2nd Line                               |
| -------------------------------------- |
| Column names                           |
| 3rd and Remaining Lines:               |
| Recipient and values of HSM parameters |

### Consulting Lists via API

### Request

Using GET, you can make a request by sending all parameters in the query string

<http://api-messaging.wavy.global/v1/list/{listType}?customerId={customerId}\\&subAccountId={subAccountId}>

| List Type                       | Value relayed in {listType} |
| ------------------------------- | --------------------------- |
| **Whatsapp OPT-OUT List**       | OPTOUT                      |
| **Whatsapp OPT-IN List**        | OPTIN                       |
| **Whatsapp Blacklist**          | BLACKLIST                   |
| **Whatsapp Whitelist (for MT)** | WHITELIST                   |

The ***customerId*** parameter is required, while ***subAccountId*** is optional.

Attention: the ’{‘ and ’}‘ curly brackets must also be replaced. For example, “{listType}” becomes “OPTIN”.

You should also relay the following headers:

| Header                  | Value               |
| ----------------------- | ------------------- |
| **Content-Type**        | application/json    |
| **authenticationToken** | Messaging1 token    |
| **userName**            | Messaging1 username |

### Response

If successful, if there is any data related to the customerId and subAccountId, the request will return a JSON with 3 attributes:

| Attribute   | Value                                                                                                |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| **success** | true                                                                                                 |
| **status**  | 200                                                                                                  |
| **data**    | Link to download a csv file containing the “source” and “createdAt” fields of all destinations found |

The “createdAt” column is in the **America/Sao\_Paulo time zone**, UTC-3 or UTC-2 in Daylight Saving Time

If there is no associated data, only a similar JSON will be returned, but without the data field, which means no issues occurred with the request, but there weren’t any data related to the parameters relayed.

Response example:

{

&#x20;"success": true,

&#x20;"status": 200,

&#x20;"data": "<https://chatclub-cdn.wavy.global/2019/02/12/f2b8effb-d0bc-4327-86c2-48fedcb01b1b/list-42-4330544192402746957.csv>"

}

### Consulting Open Sessions via API

### Request

To consult open sessions through our API, you need to make a GET request to the following URL:

GET <http://api-messaging.wavy.global/v1/session?customerId={customerId}\\&subAccountId={subAccountId}>

The ***customerId*** parameter is required, while ***subAccountId*** is optional.

Attention: The ’{‘ and ’}‘ curly brackets must also be replaced. For example, “={customerId}” becomes “=42”.

You should also relay the following headers:

| Header                  | Value            |
| ----------------------- | ---------------- |
| **Content-Type**        | application/json |
| **authenticationToken** | Token            |
| **userName**            | Username         |

Username and token can be obtained through our platform: <https://messaging.wavy.global>

### Response

If successful, if there are any open sessions for the customerId and subAccountId, the request will return a JSON with the following attribute:

| Attribute     | Value                                                                                                           |
| ------------- | --------------------------------------------------------------------------------------------------------------- |
| **file\_url** | Link to download a csv file containing the “source” and “session\_created\_at” fields of all destinations found |

If there are no data associated with the ***customerId*** and ***subAccountId***, the returned file will be empty, containing only the header.

Response example:

{

&#x20;"file\_url": "<https://chatclub-cdn.wavy.global/2019/02/13/633e33fc-3a3f-4ca5-a8b0-4b747fb67137/5bd46e2b-5990-4681-9b29-98ab6598960e>"

}
