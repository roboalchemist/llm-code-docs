# Source: https://docs.sinch.com/technical-documentation/api-and-integrations/fallback-api.md

# Fallback API

This API allows you to automatize messaging using many different channels (SMS, email and voice) in the fallback system (messaging is structured in steps and, if one of those steps fails, the following specified step will be executed).

It uses HTTP protocol with TLS and accepts the POST method with parameters via [JSON](http://json.org/).

## Authentication

To send messages and run queries in our API, it is necessary to authenticate using a combination of either username or email and a token.

| Field               | Details                                                                                                                                      | Data Type |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| UserName            | Your username or email                                                                                                                       | String    |
| AuthenticationToken | Your authentication token. Check [here](https://messaging.movile.com/messaging/user/api_configuration) and read username descriptions below. | String    |

## Connection Details

| ​                  | ​                                 |
| ------------------ | --------------------------------- |
| **Hostname**       | api-messaging.wavy.global         |
| **APIs**           | Individual messages /v1/omni/send |
| **Port**           | 443 (https)                       |
| **Protocol**       | HTTPS (TLS encryption)            |
| **Authentication** | username + token                  |
| **Portal**         | messaging.wavy.global             |

## Encoding

The encoding standard used is UTF-8, all message contents must follow this standard.

You can escape characters if you wish or encode using HTTP format

You can see some encoding examples to the side

***“messageText”:“A combinação foi perfeita :)”***

Or you can escape characters if you wish:

***“messageText”:“A combina\u00e7\u00e3o foi perfeita :)”***

## Messaging via POST Method

```
curl --request POST \
 --url 'http://{{channel-api-base-url}}/v1/omni/send' \
 --header 'authenticationtoken: 56xdJ3zs_ses51KyGM1b8py1CxCsba2sTT334hrs' \
 --header 'content-type: application/json' \
 --header 'username: bruno.azenha@movile.com' \
 --data '{
 "contacts":
 [
 {
 "contactInfo": {
 "phone1": "5516981562829",
 "phone2": "5516981562829",
 "email": "azenha.bruno@gmail.com",
 "recipientName": "Bruno Azenha"
 }
 },
 {
 "contactInfo": {
 "phone1": "0",
 "phone2": "5511982994265",
 "email": "bruno.farias@movile.com",
 "recipientName": "Bruno Farias"
 }
 }
 ],
 "template":
 {
 "campaignAlias": "Campaign Alias",
 "steps":
 [
 {
 "type": "MT",
 "destinationField": "phone1",
 "messageText": "First message.",
 "flashSms": false
 },
 {
 "type": "VOICE",
 "destinationField": "phone2",
 "ttsMessage": "This is the third message",
 "timeout": 3
 },
 {
 "type": "MT",
 "destinationField": "phone1",
 "messageText": "Second Message as Flash",
 "flashSms": true
 },
 {
 "type": "EMAIL",
 "destinationField": "email",
 "recipientName": "recipientName",
 "subject": "Third message",
 "replyTo": "reply.to@domain.com",
 "fromEmail": "email@domain.com",
 "fromName": "Your name",
 "emailText": "Email content as simple plain text",
 "emailHtml": "Email content as HTML"
 }
 ]
 }
}'
```

POST <https://api-messaging.wavy.global/v1/omni/send> Content-Type: application/json

The request body must contain the JSON object with information according to the fields below:

\* Required field

| Field                | Details                                                                                      | Type     |
| -------------------- | -------------------------------------------------------------------------------------------- | -------- |
| **contacts\***       | Array of contacts to which delivery attempts will be made                                    | Array\[] |
| **contactInfo\***    | Text of the message that will be sent                                                        | String   |
| **phone**            | Phone number to which the message will be sent (including country code). E.g.: 5511900000000 | Long     |
| **email**            | Email of the recipient                                                                       | String   |
| **emailName**        | ​                                                                                            | ​        |
| **template\***       | Template with information on the flow that will be executed                                  | Array\[] |
| **campaignAlias**    | Fallback identification                                                                      | String   |
| **Steps\***          | Steps to be executed when sending                                                            | Array\[] |
| **type\***           | Type of message (Email, MT, Voice)                                                           | String   |
| **destinationField** | Information created in the contactInfo field should be relayed                               | String   |
| **subject\***        | Used when sending emails, subject of the email to be sent                                    | String   |
| **fromEmail\***      | Source email                                                                                 | String   |
| **emailHTML\***      | HTML content to be relayed in the body of the email                                          | String   |
| **messageText**      | Content of the message for sending SMS                                                       | String   |
| **ttsMessage**       | Check phone\*\*\*\*\*\*                                                                      | ​        |

**IMPORTANT!**

**For each username, there is a unique authentication token**

## Request responses

The response to bulk messaging will contain a JSON file with the information required for tracking, an id will be created for the entire batch and an individual id and correlationId will be created for each message:

| Field | Details                     | Type   |
| ----- | --------------------------- | ------ |
| id    | UUID generated for messages | String |
