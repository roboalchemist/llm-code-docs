# Source: https://docs.sinch.com/technical-documentation/api-and-integrations/email-api.md

# Email API

Technical Documentation: Email API.

## Email API

This API allows you to automatize both single and bulk message requests and the retrieval of sent status through its endpoints. It uses HTTP protocol with TLS and accepts GET requests with query string parameters and POST requests with [JSON](http://json.org/%22%20/t%20%22_blank) parameters.

## User Authentication

In order to successfully use our API, you are required to present a valid username - or email - and the associated token authentication. While creating the request, you have to provide the following parameters on the headers:

| Field               | Details                                                                                                                         | Data Type |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- | --------- |
| UserName            | Your username or email                                                                                                          | String    |
| AuthenticationToken | Your authentication token. Get yours [here](https://messaging.movile.com/messaging/user/api_configuration%22%20/t%20%22_blank)​ | String    |

## Connection Details

| ​                  | ​                                                                                            |
| ------------------ | -------------------------------------------------------------------------------------------- |
| **Hostname**       | api-messaging.wavy.global                                                                    |
| **APIs**           | SendEmail /v1/email/send SearchEmail /v1/email/status/search ListEmail /v1/email/status/list |
| **Port**           | 443 (https)                                                                                  |
| **Protocol**       | HTTPS (TLS encryption)                                                                       |
| **Authentication** | username + token                                                                             |

## SendEmail

## SendEmail request

​

curl --request POST \\

&#x20;\--url <https://api-messaging.wavy.global/v1/email/send> \\

&#x20;\--header 'authenticationtoken: \<authenticationtoken>' \\

&#x20;\--header 'content-type: application/json' \\

&#x20;\--header 'username: \<username>' \\

&#x20;\--data '{

&#x20;"fromEmail": "<notification@movile.com>",

&#x20;"fromName": "Notifications",

&#x20;"replyTo": "<replyTo@movile.com>",

&#x20;"subject": "Marketing e-mail",

&#x20;"campaignAlias": "MyCampaign",

&#x20;"recipients": \[{

&#x20;"correlationId": "1234",

&#x20;"emailAddress": "<recipient-1@wavy.global>",

&#x20;"emailName": "Recipient-1",

&#x20;"extraInfo": "Extra e-mail info1",

&#x20;"substitutionData": {

&#x20;"name": "Recipient-1"

&#x20;}

&#x20;},

&#x20;{

&#x20;"correlationId": "567",

&#x20;"emailAddress": "<recipient-2@wavy.global>",

&#x20;"emailName": "Recipient-2",

&#x20;"extraInfo": "Extra e-mail info2"

&#x20;}

&#x20;],

&#x20;"emailHtml": "\<html> Hi, {{name}}, this is the email HTML body \</html>",

&#x20;"emailText": "Email text body",

&#x20;"substitutionData": {

&#x20;"name": "Recipient-1"

&#x20;},

&#x20;"attachments": \[{

&#x20;"data": "Q29uZ3JhdHVsYX2FuIGJhc2U2NCBkZWNvZGUh",

&#x20;"name": "billing.pdf",

&#x20;"type": "application/pdf"

&#x20;}]

}'

​

POST <https://api-messaging.wavy.global/v1/email/send> Content-Type: application/json

The request body must contain a JSON object in which information are enveloped with the following fields. Fields with a \* are required.

| Field            | Details                                                                                                                                                                                                                                                                                                          | Type   |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| fromEmail\*      | Email sender’s address. E.g. <notification@domain.com>                                                                                                                                                                                                                                                           | String |
| fromName\*       | Email sender’s name. E.g. Notification.                                                                                                                                                                                                                                                                          | String |
| replyTo          | Email address used to compose the email’s “Reply-To” header.                                                                                                                                                                                                                                                     | String |
| subject          | Email subject line.                                                                                                                                                                                                                                                                                              | String |
| campaignAlias    | Campaign name.                                                                                                                                                                                                                                                                                                   | String |
| recipients\*     | Array of recipients.                                                                                                                                                                                                                                                                                             | ​      |
| correlationId    | Identifier generated by the customer.                                                                                                                                                                                                                                                                            | String |
| emailAddress\*   | Valid email address of a recipient.                                                                                                                                                                                                                                                                              | String |
| emailName        | Name of the recipient, associated with the emailAddress                                                                                                                                                                                                                                                          | String |
| extraInfo        | Any extra info set by the user when the email was sent.                                                                                                                                                                                                                                                          | String |
| emailHTML        | HTML content for the email’s text/html MIME part.                                                                                                                                                                                                                                                                | String |
| emailText        | Text content for the email’s text/plain MIME part.                                                                                                                                                                                                                                                               | String |
| substitutionData | Mapping of tags, within {{}} marks, that should be replaced on html body.                                                                                                                                                                                                                                        | ​      |
| attachments      | Array of attachment files.                                                                                                                                                                                                                                                                                       | ​      |
| data             | The content of the attachment as a Base64 encoded string. The string should not contain \r\n line breaks.                                                                                                                                                                                                        | String |
| name             | The filename of the attachment (for example, document.pdf).                                                                                                                                                                                                                                                      | String |
| type             | The MIME type of the attachment; e.g., text/plain, image/jpeg, audio/mp3, video/mp4, application/msword, application/pdf, etc., including the charset parameter (ex: text/html; charset=“UTF-8”) if needed. The value will apply as-is to the Content-Type header of the generated MIME part for the attachment. | String |

## SendEmail response

{

&#x20;"id": "abcd-1234-efgh-5678-ijkl-9999",

&#x20;"recipients": \[

&#x20;{

&#x20;"correlationId": "5678",

&#x20;"id": "9i9j9k9l-5e6f7g8h-0i0j0k0l-1a2b3c4d"

&#x20;},

&#x20;{

&#x20;"correlationId": "5678",

&#x20;"id": "9i9j9k9l-5e6f7g8h-0i0j0k0l-1a2b3c4d"

&#x20;}

&#x20;]

}

The response body will contain a JSON object with tracking information related to the email request:

| Field         | Details                                                                   | Type   |
| ------------- | ------------------------------------------------------------------------- | ------ |
| id            | UUID generated for this email request.                                    | String |
| correlationId | The same correlationId from the request.                                  | String |
| recipients    | Tag corresponding to an id and correlationId for every request recipient. | ​      |

## SearchEmailStatus request

Example:

{

&#x20;"correlationIds": \["1234", "5678", "7890"],

&#x20;"ids": \["1234-5678-9asd-fghj", "qwer-1234-asdf-0987",

&#x20;"zxcv-4567-ghjk-6789"],

&#x20;"startDate": "2017-04-27T10:00:00Z",

&#x20;"endDate": "2017-04-28T10:00:00Z"

}

POST <https://api-messaging.wavy.global/v1/email/status/search> Content-Type: application/json

Retrieves information on a previously sente mail, given its IDs, correlationIds, and a date interval.

| Field          | Details                                                                                                                                                               | Type   |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| ids\*          | UUID generated for this email. Must correspond to the respective correlationId.                                                                                       | String |
| correlationIds | The same correlationId from the request. Must correspond to the respective id.                                                                                        | String |
| startDate      | Start date for search interval. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601%22%20/t%20%22_blank)​ | String |
| endDate        | End date to search interval. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601%22%20/t%20%22_blank)​    | String |

## ListEmailStatus request

POST <https://api-messaging.wavy.global/v1/email/status/list> Content-Type: application/json

Retrieves information on a previously sente mail, considering its user and token. This method returns all emails that haven’t yet been checked.

## List and Search EmailStatus response

\[{

&#x20;"recipient": {

&#x20;"id": "1234-5678-9asd-fghj",

&#x20;"correlationId": "1234",

&#x20;"emailAddress": "<recipient-1@movile.com>",

&#x20;"emailName": "Recipient-1",

&#x20;"extraInfo": "Extra e-mail info1"

&#x20;},

&#x20;"fromEmail": "<notificaction@movile.com>",

&#x20;"fromName": "Notifications",

&#x20;"createdAt": 12345678910,

&#x20;"createdDate": "2017-04-28T13:10:10.336Z",

&#x20;"sent": true,

&#x20;"sentStatusCode": 2,

&#x20;"sentStatus": "SENT\_SUCCESS",

&#x20;"sentAt": 9638527410,

&#x20;"sentDate": "2017-04-28T13:10:10.336Z",

&#x20;"delivered": true,

&#x20;"deliveredStatusCode": 2,

&#x20;"deliveredStatus": "SENT\_SUCCESS",

&#x20;"deliveredAt": 9876543210,

&#x20;"deliveredDate": "2017-04-28T13:10:10.336Z",

&#x20;"opened": true,

&#x20;"openedAt": 9638527410,

&#x20;"openedDate": "2017-04-28T13:10:10.336Z",

&#x20;"clicked": true,

&#x20;"clickedAt": 741258963,

&#x20;"clickedDate": "2017-04-28T13:10:10.336Z",

&#x20;"campaignId": 1,

&#x20;"campaignAlias": "demo1"

}, {

&#x20;"recipient": {

&#x20;"id": "qwer-1234-asdf-0987",

&#x20;"correlationId": "5678",

&#x20;"emailAddress": "<recipient-1@movile.com>",

&#x20;"emailName": "Recipient-1",

&#x20;"extraInfo": "Extra e-mail info1"

&#x20;},

&#x20;"fromEmail": "<notificaction@movile.com>",

&#x20;"fromName": "Notifications",

&#x20;"createdAt": 12345678910,

&#x20;"createdDate": "2017-04-28T13:10:10.336Z",

&#x20;"sent": true,

&#x20;"sentStatusCode": 2,

&#x20;"sentStatus": "SENT\_SUCCESS",

&#x20;"sentAt": 9876543210,

&#x20;"sentDate": "2017-04-28T13:10:10.336Z",

&#x20;"delivered": true,

&#x20;"deliveredStatusCode": 2,

&#x20;"deliveredStatus": "SENT\_SUCCESS",

&#x20;"deliveredAt": 9876543210,

&#x20;"deliveredDate": "2017-04-28T13:10:10.336Z",

&#x20;"opened": true,

&#x20;"openedAt": 9638527410,

&#x20;"openedDate": "2017-04-28T13:10:10.336Z",

&#x20;"clicked": true,

&#x20;"clickedAt": 741258963,

&#x20;"clickedDate": "2017-04-28T13:10:10.336Z",

&#x20;"campaignId": 1,

&#x20;"campaignAlias": "demo1"

}, {

&#x20;"recipient": {

&#x20;"id": "zxcv-4567-ghjk-6789",

&#x20;"correlationId": "0987",

&#x20;"emailAddress": "<recipient-1@movile.com>",

&#x20;"emailName": "Recipient-1",

&#x20;"extraInfo": "Extra e-mail info1"

&#x20;},

&#x20;"fromEmail": "<notificaction@movile.com>",

&#x20;"fromName": "Notifications",

&#x20;"createdAt": 12345678910,

&#x20;"createdDate": "2017-04-28T13:10:10.336Z",

&#x20;"sent": true,

&#x20;"sentStatusCode": 2,

&#x20;"sentStatus": "SENT\_SUCCESS",

&#x20;"sentAt": 9876543210,

&#x20;"sentDate": "2017-04-28T13:10:10.336Z",

&#x20;"delivered": true,

&#x20;"deliveredStatusCode": 2,

&#x20;"deliveredStatus": "SENT\_SUCCESS",

&#x20;"deliveredAt": 9876543210,

&#x20;"deliveredDate": "2017-04-28T13:10:10.336Z",

&#x20;"opened": true,

&#x20;"openedAt": 9638527410,

&#x20;"openedDate": "2017-04-28T13:10:10.336Z",

&#x20;"clicked": true,

&#x20;"clickedAt": 741258963,

&#x20;"clickedDate": "2017-04-28T13:10:10.336Z",

&#x20;"campaignId": 1,

&#x20;"campaignAlias": "demo1"

}]

Retrieves information on a previously sent email, considering its user and token. This method returns all emails not previously queried.

| Field               | Details                                                                                                                                                        | Type    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| emailStatus         | Block for each email information.                                                                                                                              | ​       |
| recipient           | Block for recipient email information.                                                                                                                         | ​       |
| id                  | The same id from the request.                                                                                                                                  | ​       |
| correlationId       | The same correlationId from the request.                                                                                                                       | ​       |
| emailAddress        | Email address of the recipient.                                                                                                                                | ​       |
| emailName           | Name of the recipient, associated with the emailAddress.                                                                                                       | ​       |
| extraInfo           | Any extra information.                                                                                                                                         | ​       |
| fromEmail           | Email sender’s address. E.g. <notification@domain.com>                                                                                                         | ​       |
| fromName            | Email sender’s name. E.g. Notification, Not reply, etc.                                                                                                        | ​       |
| createdAt           | When the email was created. It is an Epoch Date.                                                                                                               | Long    |
| createdDate         | When the message was created. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601)​                | ​       |
| sent                | Flag indicating if the email was sent.                                                                                                                         | Boolean |
| sentStatusCode      | Sent status code. Check Sent Status Codes for more information.                                                                                                | Long    |
| sentStatus          | Sent status.                                                                                                                                                   | String  |
| sentAt              | When the email was sent. It is an Epoch Date.                                                                                                                  | Long    |
| sentDate            | When the email was sent. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601)​                     | ​       |
| delivered           | Flag indicating if the email was delivered to the recipient.                                                                                                   | Boolean |
| deliveredStatusCode | Delivered status code. Check Delivered Status Codes for more information.                                                                                      | Long    |
| deliveredStatus     | Delivered status.                                                                                                                                              | String  |
| deliveredAt         | When the email was delivered. It is an Epoch Date.                                                                                                             | Long    |
| deliveredDate       | When the email was delivered. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601)​                | ​       |
| open                | Flag indicating if the email was opened by the recipient.                                                                                                      | Boolean |
| openedAt            | When the email was opened. It is an Epoch Date.                                                                                                                | Long    |
| openedDate          | When the email was opened. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601)​                   | ​       |
| clicked             | Flag indicating if the email was clicked by the recipient.                                                                                                     | Boolean |
| clickedAt           | When the email was clicked. It is an Epoch Date.                                                                                                               | Long    |
| clickedDate         | When the email was clicked by the recipient. Format yyyy-MM-dd’T'HH:mm:ssZ. Date format with time and time zone [ISO](https://en.wikipedia.org/wiki/ISO_8601)​ | ​       |
| campaignId          | Campaign identifier.                                                                                                                                           | Long    |
| campaignAlias       | Campaign name.                                                                                                                                                 | String  |

## Status Codes

## Sent Status Codes

A sent status code represents the status of a message that goes through our system and is sent to the carrier.

### Success codes

| ​ | ​             | ​                         |
| - | ------------- | ------------------------- |
| 2 | SENT\_SUCCESS | Sent to Wavy successfully |

### Wavy error codes

| ​   | ​               | ​                   |
| --- | --------------- | ------------------- |
| 301 | INTERNAL\_ERROR | Wavy internal error |

## Delivered Status Codes

A delivered status code represents the status report we receive from the server about the email.

### Success codes

| ​ | ​                  | ​                                |
| - | ------------------ | -------------------------------- |
| 3 | DELIVERED\_SUCCESS | Delivered to server successfully |

### Carrier error codes

| ​   | ​              | ​                                                |
| --- | -------------- | ------------------------------------------------ |
| 103 | NOT\_DELIVERED | Email accepted but has not delivered the e-mail. |

## Opened Status Codes

An opened status code represents the email opened by the customer.

### Success codes

| ​ | ​               | ​                                |
| - | --------------- | -------------------------------- |
| 4 | OPENED\_SUCCESS | Delivered to server successfully |

### Carrier error codes

| ​   | ​           | ​                                                 |
| --- | ----------- | ------------------------------------------------- |
| 104 | NOT\_OPENED | Email accepted but has not opened by the customer |

## Clicked Status Codes

A clicked status code represents the status report when the customer clicked over the email. |||| |–|–|–| |5|CLICKED\_SUCCESS|Clicked by the customer successfully|

### Carrier error codes

| ​   | ​            | ​                                                  |
| --- | ------------ | -------------------------------------------------- |
| 104 | NOT\_CLICKED | Email accepted but has not clicked by the customer |
