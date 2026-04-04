# Source: https://docs.sinch.com/technical-documentation/api-and-integrations/whatsapp-lists-via-api.md

# WhatsApp Lists via API

### **Consulting Lists via API**

**OPT IN/OUT & BLACK/WHITE LIST**

**API - Possible list request types:**

* OPT IN
* OPT OUT
* BLACK LIST
* WHITE LIST
* OPEN SESSIONS

**Request**

You need to make a GET request to the URL ***<http://api-messaging.wavy.global/v1/list/{listType}?customerId={customerId}\\&subAccountId={subAccountId}>***.

| List Type                       | Value relayed in listType |
| ------------------------------- | ------------------------- |
| **WhatsApp OPT-OUT List**       | OPTOUT                    |
| **WhatsApp OPT-IN List**        | OPTIN                     |
| **WhatsApp Blacklist**          | BLACKLIST                 |
| **WhatsApp Whitelist (for MT)** | WHITELIST                 |

The ***customerId*** parameter is required, while ***subAccountId*** is optional. You should also relay the following headers:

| ​                       | ​                   |
| ----------------------- | ------------------- |
| **Content-Type**        | application/json    |
| **authenticationToken** | Messaging1 token    |
| **userName**            | Messaging1 username |

**Response**

If successful, if there is any data related to the customerId and subAccountId (if specified), the request will return a JSON with 3 attributes:

| ​           | ​                                                                                                    |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| **success** | true                                                                                                 |
| **status**  | 200                                                                                                  |
| **data**    | Link to download a csv file containing the “source” and “createdAt” fields of all destinations found |

**If there is no associated data, only a similar JSON will be returned, but without the data field, which means no issues occurred with the request, but there weren’t any data related to the parameters relayed.**

**​**
