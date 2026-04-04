# Source: https://plivo.com/docs/messaging/api/messages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Messages

> Send, retrieve, and manage SMS/MMS/WhatsApp messages programmatically

A Message Detail Record (MDR) is generated for every message sent or received by Plivo. Use the Message API to send outbound messages, retrieve message details, and monitor message delivery status.

## The Message Object

### Attributes

<ParamField body="message_uuid" type="string">
  A 36-character string that uniquely identifies a message detail record.
</ParamField>

<ParamField body="message_time" type="string">
  The exact timestamp at which an outbound message was initiated or an inbound message was received.
</ParamField>

<ParamField body="message_direction" type="string">
  Indicates the direction of the message. Values: `outbound`, `inbound`.
</ParamField>

<ParamField body="message_state" type="string">
  Current status of the message. Outbound: `queued`, `sent`, `failed`, `delivered`, `undelivered`, `read` (WhatsApp only). Inbound: `received`, `delivered`, `undelivered`.
</ParamField>

<ParamField body="message_type" type="string">
  Type of message. Values: `sms`, `mms`, `whatsapp`.
</ParamField>

<ParamField body="from_number" type="string">
  Source address of the message. For outbound: Plivo phone number, short code, alphanumeric sender ID, or WhatsApp Business number. For inbound: the sender's phone number.
</ParamField>

<ParamField body="to_number" type="string">
  Destination phone number. For inbound messages, this is the Plivo phone number that received the message.
</ParamField>

<ParamField body="units" type="integer">
  Number of units the message was split into.
</ParamField>

<ParamField body="total_rate" type="string">
  The charge applicable per unit of the message.
</ParamField>

<ParamField body="total_amount" type="string">
  The total amount charged for this message.
</ParamField>

<ParamField body="error_code" type="string">
  Plivo error code. `000` for successful delivery. See [error codes](/messaging/troubleshooting/error-codes/) for failure codes.
</ParamField>

<ParamField body="conversation_id" type="string">
  WhatsApp-only. ID of the conversation to which the message belongs.
</ParamField>

<ParamField body="conversation_origin" type="string">
  WhatsApp-only. How the conversation was initiated. Values: `utility`, `authentication`, `marketing`, `service`.
</ParamField>

### Example Message Object

```json  theme={null}
{
  "api_id": "85a704c8-e47a-11eb-9a69-0242ac110004",
  "carrier_fees": "0.00000",
  "carrier_fees_rate": "0.0000",
  "error_code": "000",
  "from_number": "17087654321",
  "message_direction": "outbound",
  "message_state": "delivered",
  "message_time": "2021-07-13 13:04:06.799021+05:30",
  "message_type": "sms",
  "message_uuid": "b48d95dc-e3ac-11eb-a9c2-0242ac110005",
  "to_number": "12401234567",
  "total_amount": "0.00140",
  "total_rate": "0.00140",
  "units": 1
}
```

***

## List All Messages

Retrieve a list of message records with optional filters.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Message/
```

### Arguments

<ParamField query="subaccount" type="string">
  Filter by subaccount auth\_id.
</ParamField>

<ParamField query="message_direction" type="string">
  Filter by direction. Values: `inbound`, `outbound`.
</ParamField>

<ParamField query="message_state" type="string">
  Filter by state. Values: `queued`, `sent`, `delivered`, `undelivered`, `failed`, `received`.
</ParamField>

<ParamField query="message_type" type="string">
  Filter by type. Values: `sms`, `mms`, `whatsapp`.
</ParamField>

<ParamField query="message_time__gt" type="string">
  Filter messages after this timestamp (format: `yyyy-MM-dd HH:mm:ss`).
</ParamField>

<ParamField query="message_time__lt" type="string">
  Filter messages before this timestamp.
</ParamField>

<ParamField query="error_code" type="integer">
  Filter by error code.
</ParamField>

<ParamField query="powerpack_id" type="string">
  Filter by Powerpack ID.
</ParamField>

<ParamField query="limit" type="integer">
  Results per page (max 20). Default: 20.
</ParamField>

<ParamField query="offset" type="integer">
  Number of records to skip. Default: 0.
</ParamField>

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      "https://api.plivo.com/v1/Account/{auth_id}/Message/?limit=5&message_direction=outbound"
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.messages.list(
      limit=5,
      offset=0,
      message_direction='outbound'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.messages.list({
      limit: 5,
      offset: 0,
      message_direction: 'outbound'
  }).then(console.log);
  ```
</CodeGroup>

***

## Retrieve a Message

Get details of a specific message by its UUID.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Message/{message_uuid}/
```

### Arguments

<ParamField path="message_uuid" type="string" required>
  The unique identifier of the message to retrieve.
</ParamField>

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Message/{message_uuid}/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.messages.get('message_uuid')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.messages.get('message_uuid').then(console.log);
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  response = api.messages.get('message_uuid')
  puts response
  ```
</CodeGroup>

***

## Send a Message

Send an SMS, MMS, or WhatsApp message to one or more recipients.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Message/
```

### Arguments

<ParamField body="src" type="string" required>
  Sender ID: phone number, short code, or alphanumeric string. For WhatsApp, use your WhatsApp Business number. Either `src` or `powerpack_uuid` is required.
</ParamField>

<ParamField body="powerpack_uuid" type="string">
  UUID of the Powerpack to use for this message. Either `src` or `powerpack_uuid` is required.
</ParamField>

<ParamField body="dst" type="string" required>
  Destination phone number in E.164 format. For multiple recipients, separate with `<` (e.g., `14156667777<14157778888`).
</ParamField>

<ParamField body="text" type="string">
  Message content. For SMS: max 1,600 GSM characters or 737 Unicode characters. For WhatsApp freeform: max 4,096 characters.
</ParamField>

<ParamField body="type" type="string">
  Message type. Values: `sms` (default), `mms`, `whatsapp`.
</ParamField>

<ParamField body="media_urls" type="array">
  For MMS: comma-separated URLs (max 10, total size \< 5MB). For WhatsApp: single media URL.
</ParamField>

<ParamField body="template" type="object">
  WhatsApp template object for templated messages. Required for initiating conversations.
</ParamField>

<ParamField body="interactive" type="object">
  WhatsApp interactive message object for list buttons, reply buttons, or CTA buttons.
</ParamField>

<ParamField body="location" type="object">
  WhatsApp location object with `latitude`, `longitude`, `name`, and `address`.
</ParamField>

<ParamField body="url" type="string">
  Callback URL for delivery status updates.
</ParamField>

<ParamField body="method" type="string">
  HTTP method for callback URL. Values: `GET`, `POST` (default).
</ParamField>

<ParamField body="message_expiry" type="integer">
  Queue expiry time in seconds (5-10,799). Default: 10,800 (3 hours).
</ParamField>

<ParamField body="log" type="string">
  Data logging preference. Values: `true` (default), `false`, `content_only`, `number_only`.
</ParamField>

<ParamField body="trackable" type="boolean">
  Set `true` for messages with trackable actions (e.g., 2FA). Default: `false`.
</ParamField>

<ParamField body="dlt_entity_id" type="string">
  DLT entity ID for India DLT compliance.
</ParamField>

<ParamField body="dlt_template_id" type="string">
  DLT template ID for India DLT compliance.
</ParamField>

<ParamField body="dlt_template_category" type="string">
  DLT template category. Values: `transactional`, `promotional`, `service_implicit`, `service_explicit`.
</ParamField>

### Response

Returns the message UUID(s) and API request ID.

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{
          "src": "+14151234567",
          "dst": "+14157654321",
          "text": "Hello from Plivo!"
      }' \
      https://api.plivo.com/v1/Account/{auth_id}/Message/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.messages.create(
      src='+14151234567',
      dst='+14157654321',
      text='Hello from Plivo!'
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.messages.create({
      src: '+14151234567',
      dst: '+14157654321',
      text: 'Hello from Plivo!'
  }).then(console.log);
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = api.messages.create(
    '+14151234567',
    ['+14157654321'],
    'Hello from Plivo!'
  )
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->messages->create([
      'src' => '+14151234567',
      'dst' => '+14157654321',
      'text' => 'Hello from Plivo!'
  ]);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.message.Message;

  public class SendMessage {
      public static void main(String[] args) {
          Plivo.init("<auth_id>", "<auth_token>");

          Message.creator("+14151234567", "+14157654321", "Hello from Plivo!")
              .create();
      }
  }
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.Message.Create(
      src: "+14151234567",
      dst: new[] { "+14157654321" },
      text: "Hello from Plivo!"
  );
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})

      client.Messages.Create(plivo.MessageCreateParams{
          Src:  "+14151234567",
          Dst:  "+14157654321",
          Text: "Hello from Plivo!",
      })
  }
  ```
</CodeGroup>

```json Response theme={null}
{
  "message": "message(s) queued",
  "message_uuid": ["db3ce55a-7f1d-11e1-8ea7-1231380bc196"],
  "api_id": "db342550-7f1d-11e1-8ea7-1231380bc196"
}
```

***

## List MMS Media

Retrieve media files associated with an MMS message.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Message/{message_uuid}/Media/
```

### Arguments

<ParamField path="message_uuid" type="string" required>
  The unique identifier of the MMS message.
</ParamField>

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Message/{message_uuid}/Media/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.messages.list_media('message_uuid')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.messages.listMedia('message_uuid').then(console.log);
  ```
</CodeGroup>

***

## Message Status Callbacks

Configure a callback URL to receive delivery status updates for your messages.

### Callback Parameters

<Accordion title="Status callback parameters">
  | Parameter     | Type    | Description                                                                     |
  | ------------- | ------- | ------------------------------------------------------------------------------- |
  | `From`        | string  | The sender ID of the message.                                                   |
  | `To`          | string  | The destination number.                                                         |
  | `MessageUUID` | string  | Unique identifier for the message.                                              |
  | `Status`      | string  | Current status: `queued`, `sent`, `delivered`, `undelivered`, `failed`, `read`. |
  | `Units`       | integer | Number of message units.                                                        |
  | `TotalRate`   | string  | Per-unit charge.                                                                |
  | `TotalAmount` | string  | Total charge for the message.                                                   |
  | `ErrorCode`   | string  | Error code if delivery failed.                                                  |
  | `MCC`         | string  | Mobile Country Code of the destination.                                         |
  | `MNC`         | string  | Mobile Network Code of the destination.                                         |
</Accordion>

***

## Handling Incoming Messages

When a message is received on your Plivo number, Plivo sends a request to your configured Message URL.

### Incoming Message Parameters

| Parameter           | Type   | Description                              |
| ------------------- | ------ | ---------------------------------------- |
| `From`              | string | Sender's phone number.                   |
| `To`                | string | Your Plivo phone number.                 |
| `Text`              | string | Message content.                         |
| `Type`              | string | Message type (`sms`, `mms`, `whatsapp`). |
| `MessageUUID`       | string | Unique message identifier.               |
| `Media0`...`MediaN` | string | MMS media URLs (for MMS messages).       |

### Configuration

1. Create a [Messaging Application](https://cx.plivo.com/xml-applications)
2. Set your Message URL endpoint
3. Assign the application to your Plivo number

Your endpoint should return a `200 OK` response. Optionally, return [Message XML](/messaging/xml/message/) to send a reply.
