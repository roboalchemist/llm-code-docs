# Source: https://docs.sinch.com/technical-documentation/api-and-integrations/whatsapp-interactive-api.md

# WhatsApp Interactive API

## Interactive Messages

To send interactive messages we will follow the standard of other types of messages that can be seen [here](https://docs.wavy.global/documentacao-tecnica/todas-as-integracoes/whatsapp-api#whatsapp-api).

#### Message

| Field       | Required | Details                                 | Type                |
| ----------- | -------- | --------------------------------------- | ------------------- |
| interactive | Yes      | Field used to send interactive messages | Interactive Message |

#### Interactive Message

| Field                  | Required                                         | Details                                                                                 | Type              |
| ---------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------- | ----------------- |
| messageInteractiveType | Yes                                              | Type of interactive message. Available options: LIST and REPLY\_BUTTON                  | String            |
| header                 | No                                               | Header content                                                                          | Header            |
| body                   | Yes                                              | Main text                                                                               | Body              |
| footer                 | No                                               | Footer content                                                                          | Footer            |
| listAction             | When the messageInteractiveType is LIST          | Contains parameters of a list message                                                   | ListAction        |
| replyButtonAction      | When the messageInteractiveType is REPLY\_BUTTON | Contains parameters of a reply button message                                           | ReplyButtonAction |
| alternativeText        | No                                               | Text that will be sent if the user’s mobile phone does not support interactive messages | String            |

#### Header

If the message has a header, **exactly one of the fields below must be filled**.

If the message type is LIST only the text field is accepted.

| Field    | Details                                                                    | Type     |
| -------- | -------------------------------------------------------------------------- | -------- |
| text     | Header text. Maximum 60 characters. Allows the use of emojis and markdown. | String   |
| document | Complex Document object.                                                   | Document |
| video    | Complex Video object.                                                      | Video    |
| image    | Complex Image object.                                                      | Image    |
| location | Complex Location object.                                                   | Location |

**Image**

| Field | Required | Details                                                                                          | Type   |
| ----- | -------- | ------------------------------------------------------------------------------------------------ | ------ |
| type  | Yes      | Type/extension of the image that will be sent in the message. Available options: JPG, JPEG, PNG. | String |
| url   | Yes      | URL of the content (image) that will be sent.                                                    | String |

**Video**

| Field | Required | Details                                                                               | Type   |
| ----- | -------- | ------------------------------------------------------------------------------------- | ------ |
| type  | Yes      | Type/extension of the video that will be sent in the message. Available options: MP4. | String |
| url   | Yes      | URL of the content (video) that will be sent.                                         | String |

**Document**

| Field | Required | Details                                                                                  | Type   |
| ----- | -------- | ---------------------------------------------------------------------------------------- | ------ |
| type  | Yes      | Type/extension of the document that will be sent in the message. Available options: PDF. | String |
| url   | Yes      | URL of the content (document) that will be sent.                                         | String |

**Location**

| Field    | Required | Details                                       | Type   |
| -------- | -------- | --------------------------------------------- | ------ |
| name     | No       | Location name.                                | String |
| address  | No       | Location address.                             | String |
| geoPoint | Yes      | Coordinates in the format: latitude,longitude | String |

#### Body/Footer

| Field | Required | Details                                                                                                                  | Type   |
| ----- | -------- | ------------------------------------------------------------------------------------------------------------------------ | ------ |
| text  | Yes      | Cannot be an empty string. Allows for emojis and markdown. Body: Maximum 1024 characters. Footer: Maximum 60 characters. | String |

#### ListAction

| Field    | Required | Details                                           | Type       |
| -------- | -------- | ------------------------------------------------- | ---------- |
| button   | Yes      | Content to be written inside the button.          | String     |
| sections | Yes      | List of sections. Must have at least one section. | Section\[] |

**Section**

| Field | Required | Details                                                                   | Type   |
| ----- | -------- | ------------------------------------------------------------------------- | ------ |
| rows  | Yes      | List rows. Must have at least one row and at most 10 adding all sections. | Row\[] |

**Row**

| Field       | Required | Details         | Type   |
| ----------- | -------- | --------------- | ------ |
| identifier  | Yes      | Row identifier  | String |
| title       | Yes      | Row title       | String |
| description | No       | Row description | String |

#### ReplyButtonAction

| Field   | Required | Details                      | Type      |
| ------- | -------- | ---------------------------- | --------- |
| buttons | Yes      | List with 1, 2, or 3 Buttons | Button\[] |

**Button**

| Field | Required | Details          | Type  |
| ----- | -------- | ---------------- | ----- |
| reply | Yes      | Button structure | Reply |

**Reply**

| Field   | Required | Details                                                             | Type   |
| ------- | -------- | ------------------------------------------------------------------- | ------ |
| title   | Yes      | Text to be written inside the button. Maximum 20 characters.        | String |
| payload | Yes      | Information to be returned in the callback. Maximum 256 characters. | String |

### Request Examples

**LIST**

```
{
 "destinations": [
 {
 "correlationId": "MyCorrelationId",
 "destination": "5519900001111"
 }
 ],
 "message": {
 "interactive": {
 "messageInteractiveType": "LIST",
 "header": {
 "text": "Sample text"
 },
 "body": {
 "text": "Main message text"
 },
 "footer": {
 "text": "Footer text"
 },
 "listAction": {
 "button": "button text",
 "sections": [
 {
 "rows": [
 {
 "identifier": "9ab8d65e-d389-4123-b97b-702e658cc9e4",
 "title": "August 7, 11:00",
 "description": "Saturday, August 7, 2021. 11:00AM"
 },
 {
 "identifier": "2051afef-e000-47d0-99a5-7d96c17968b2",
 "title": "August 7, 15:00",
 "description": "Saturday, August 7, 2021. 3:00PM"
 },
 {
 "identifier": "55baac93-a513-45d0-ad9e-2e2271861fc8",
 "title": "August 9, 11:00",
 "description": "Monday, August 9, 2021. 11:00AM"
 },
 {
 "identifier": "e2703f03-689c-4d1e-b0e9-4045d6687605",
 "title": "August 9, 15:00",
 "description": "Monday, August 9, 2021. 4:00PM"
 }
 ]
 }
 ]
 },
 "alternativeText": "Simple message text"
 }
 }
}
```

**REPLY\_BUTTON**

```
{
 "destinations": [
 {
 "correlationId": "MyCorrelationId",
 "destination": "5519900001111"
 }
 ],
 "message": {
 "interactive": {
 "messageInteractiveType": "REPLY_BUTTON",
 "header": {
 "text": "Sample text",
 "image": {
 "type": "JPG",
 "url": "http://...jpg"
 },
 "video": {
 "type": "MP4",
 "url": "http://...mp4"
 },
 "document": {
 "type": "PDF",
 "url": "http://...pdf"
 },
 "location": {
 "geoPoint": "-22.894180,-47.047960",
 "name": "Wavy",
 "address": "Av. Cel. Silva Telles"
 }
 },
 "body": {
 "text": "Main message text"
 },
 "footer": {
 "text": "Footer text"
 },
 "replyButtonAction": {
 "buttons": [
 {
 "reply": {
 "title": "Display Text 1",
 "payload": "callback_payload_1"
 }
 },
 {
 "reply": {
 "title": "Display Text 2",
 "payload": "callback_payload_2"
 }
 }
 ],
 },
 "alternativeText": "Simple message text"
 }
 }
}
```

## Interactive Message Callback

#### Callback

| Field      | Details                                                  | Type       |
| ---------- | -------------------------------------------------------- | ---------- |
| total      | Number of callbacks in this request                      | Long       |
| data       | List of messages sent by the user                        | Data\[]    |
| clientInfo | Information of the client that is receiving the messages | ClientInfo |

#### Data

| Field         | Details                                                                                           | Type        |
| ------------- | ------------------------------------------------------------------------------------------------- | ----------- |
| id            | Message identifier                                                                                | String      |
| source        | Phone number of who sent the message                                                              | String      |
| origin        | Phone number of the WhatsApp Account that received the message                                    | String      |
| userProfile   | User profile who sent the message                                                                 | UserProfile |
| correlationId | Unique ID sent by the customer when sending the message to be returned in the callback. Optional. | String      |
| campaignId    | Campaign related to the message                                                                   | String      |
| campaignAlias | Alias of the campaign related to the message                                                      | String      |
| message       | Message received                                                                                  | Message     |
| receivedDate  | Date the message was received. Format: yyyy-MM-dd’T'HH:mm:ssZ                                     | String      |
| receivedAt    | Date the message was received, using Unix\_time format                                            | Long        |
| extraInfo     | Extra information related to the message. Format: Json                                            | String      |
| session       | Session information                                                                               | Session     |

#### UserProfile

| Field      | Details           | Type   |
| ---------- | ----------------- | ------ |
| name       | WhatsApp username | String |
| whatsAppId | User phone number | String |

#### Session

| Field     | Details                            | Type   |
| --------- | ---------------------------------- | ------ |
| sessionId | Id of this user’s session          | String |
| createdAt | Creation timestamp of this session | Long   |

#### Message

| Field           | Details                                                                                                 | Type                |
| --------------- | ------------------------------------------------------------------------------------------------------- | ------------------- |
| type            | Type of message sent by the user: TEXT - IMAGE - AUDIO - DOCUMENT - STICKER - BUTTON - ORDER            | String              |
| **messageText** | Text of the message sent by the user. For list replies, it is the same as the rowTitle the user clicked | String              |
| mediaUrl        | Url to download media sent by the user                                                                  | String              |
| mimeType        | Mime type of the file sent by the user                                                                  | String              |
| caption         | Label of media sent by the user                                                                         | String              |
| location        | Location sent by the user                                                                               | Location            |
| contacts        | List of contacts sent by the user                                                                       | Contact\[]          |
| interactive     | Fields related to interactive messages                                                                  | ReceivedInteractive |

#### ReceivedInteractive

| Field       | Details                                                           | Type        |
| ----------- | ----------------------------------------------------------------- | ----------- |
| type        | Type of interactive message. Can be: LIST\_REPLY or BUTTON\_REPLY | String      |
| listReply   | List reply (LIST)                                                 | ListReply   |
| buttonReply | Button reply (REPLY\_BUTTON)                                      | ButtonReply |

**ListReply**

| Field         | Details                                 | Type   |
| ------------- | --------------------------------------- | ------ |
| rowIdentifier | Identifier of the row the user selected | String |
| rowTitle      | Title of the row the user selected      | String |

**ButtonReply**

| Field   | Details                                     | Type   |
| ------- | ------------------------------------------- | ------ |
| payload | Text set at the time of sending the message | String |
| title   | Title of the button the user clicked        | String |

#### ClientInfo

| Field        | Details                                               | Type |
| ------------ | ----------------------------------------------------- | ---- |
| customerId   | customerId of the customer who receives the message   | Long |
| subAccountId | subAccountId of the customer who receives the message | Long |
| userId       | userId of the customer who receives the message       | Long |
