# Source: https://plivo.com/docs/programmable-api/verify/sessions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Session API

> Create, validate, retrieve, and list verification sessions

The Session API lets you send and validate one-time passwords (OTP) for two-factor authentication (2FA) using SMS and voice channels.

**API Endpoint**

```
https://api.plivo.com/v1/Account/{auth_id}/Verify/Session/
```

***

## The Session Object

The API creates a Session object once for each recipient within the code expiry time. A session can have multiple attempts to deliver the OTP.

### Attributes

<ParamField body="session_uuid" type="string">
  A 36-character string that uniquely identifies a session.
</ParamField>

<ParamField body="app_uuid" type="string">
  ID of the application used to trigger the session.
</ParamField>

<ParamField body="recipient" type="string">
  The destination phone number (in E.164 format).
</ParamField>

<ParamField body="status" type="string">
  Current status. Values: `in-progress`, `verified`, `expired`.
</ParamField>

<ParamField body="channel" type="string">
  The last channel used for the session.
</ParamField>

<ParamField body="locale" type="string">
  Language translation used for the session.
</ParamField>

<ParamField body="otp_attempts" type="object">
  Details of all attempts made during a session.
</ParamField>

<ParamField body="charge" type="object">
  Details of all charges incurred during a session.
</ParamField>

<ParamField body="created_at" type="string">
  UTC time when the session was created.
</ParamField>

<ParamField body="updated_at" type="string">
  UTC time when the session was last updated.
</ParamField>

***

## Create a Session

Send an OTP via SMS or voice.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Verify/Session/
```

### Arguments

<ParamField body="recipient" type="string" required>
  The phone number to send the OTP to.
</ParamField>

<ParamField body="app_uuid" type="string">
  UUID of the Verify application. Defaults to default application.
</ParamField>

<ParamField body="channel" type="string">
  Delivery channel. Values: `sms`, `voice`. Default: `sms`.
</ParamField>

<ParamField body="url" type="string">
  URL for status callbacks.
</ParamField>

<ParamField body="method" type="string">
  HTTP method for callbacks. Values: `GET`, `POST`. Default: `POST`.
</ParamField>

<ParamField body="locale" type="string">
  Language code (e.g., `en_US`, `es`, `fr_FR`). Default: `en`.
</ParamField>

<ParamField body="brand_name" type="string">
  Brand name to replace `${brand_name}` in templates.
</ParamField>

<ParamField body="app_hash" type="string">
  Android app hash for SMS Retriever API integration.
</ParamField>

<ParamField body="code_length" type="integer">
  OTP length (4-8). Overrides application default.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.verify_session.create(
      recipient='<destination_number>',
      app_uuid='<verify_app_uuid>',
      channel='sms',
      url='https://your-domain.com/callback',
      method='POST'
  )

  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.verify_session.create({
      recipient: '<destination_number>',
      app_uuid: '<verify_app_uuid>',
      channel: 'sms',
      url: 'https://your-domain.com/callback',
      method: 'POST'
  }).then(response => {
      console.log(response);
  });
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.verify_session.create(
      recipient: '<destination_number>',
      app_uuid: '<verify_app_uuid>',
      channel: 'sms',
      url: 'https://your-domain.com/callback',
      method: 'POST'
  )

  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->verifySessions->create(
      '<destination_number>',
      [
          'app_uuid' => '<verify_app_uuid>',
          'channel' => 'sms',
          'url' => 'https://your-domain.com/callback',
          'method' => 'POST'
      ]
  );

  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.verify_session.VerifySession;
  import com.plivo.api.models.verify_session.SessionCreateResponse;

  Plivo.init("<auth_id>", "<auth_token>");

  SessionCreateResponse response = VerifySession.creator(
      "<verify_app_uuid>",
      "<destination_number>",
      "sms",
      "https://your-domain.com/callback",
      "POST"
  ).create();

  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.VerifySession.Create(
      recipient: "<destination_number>",
      app_uuid: "<verify_app_uuid>",
      channel: "sms",
      url: "https://your-domain.com/callback",
      method: "POST"
  );

  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import (
      "fmt"
      "github.com/plivo/plivo-go/v7"
  )

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})

      response, _ := client.VerifySession.Create(plivo.SessionCreateParams{
          Recipient: "<destination_number>",
          AppUUID:   "<verify_app_uuid>",
          Channel:   "sms",
          URL:       "https://your-domain.com/callback",
          Method:    "POST",
      })

      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Verify/Session/" \
    -u "{auth_id}:{auth_token}" \
    -H "Content-Type: application/json" \
    -d '{
      "recipient": "<destination_number>",
      "app_uuid": "<verify_app_uuid>",
      "channel": "sms",
      "url": "https://your-domain.com/callback",
      "method": "POST"
    }'
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "3335cb16-d297-4e00-a5e6-66d2bb03b323",
    "message": "Session initiated",
    "session_uuid": "8e712097-8090-4644-81e7-8f4265d8354e"
}
```

***

## Validate a Session

Validate the OTP entered by the user.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Verify/Session/{session_uuid}/
```

### Arguments

<ParamField body="otp" type="string" required>
  The OTP to validate.
</ParamField>

<Note>
  You can attempt no more than 10 validations per session to prevent brute-force attacks.
</Note>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.verify_session.validate(
      session_uuid='<session_uuid>',
      otp='<otp_value>'
  )

  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.verify_session.validate({
      id: '<session_uuid>',
      otp: '<otp_value>'
  }).then(response => {
      console.log(response);
  });
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.verify_session.validate('<session_uuid>', '<otp_value>')

  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->verifySessions->validate('<session_uuid>', '<otp_value>');

  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.verify_session.VerifySession;

  Plivo.init("<auth_id>", "<auth_token>");

  SessionCreateResponse response = VerifySession.validation(
      "<session_uuid>",
      "<otp_value>"
  ).create();

  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.VerifySession.Validate(
      session_uuid: "<session_uuid>",
      otp: "<otp_value>"
  );

  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import (
      "fmt"
      "github.com/plivo/plivo-go/v7"
  )

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})

      response, _ := client.VerifySession.Validate(
          plivo.SessionValidationParams{OTP: "<otp_value>"},
          "<session_uuid>",
      )

      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Verify/Session/{session_uuid}/" \
    -u "{auth_id}:{auth_token}" \
    -H "Content-Type: application/json" \
    -d '{"otp": "<otp_value>"}'
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "e7af31b5-a7cb-40d6-a3ab-122fdcc9f0fe",
    "message": "session validated successfully."
}
```

***

## Retrieve a Session

Get details of a specific session.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Verify/Session/{session_uuid}/
```

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.verify_session.get('<session_uuid>')

  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.verify_session.get('<session_uuid>').then(response => {
      console.log(response);
  });
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.verify_session.get('<session_uuid>')

  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->verifySessions->get('<session_uuid>');

  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.verify_session.VerifySession;

  Plivo.init("<auth_id>", "<auth_token>");

  VerifySession response = VerifySession.getter("<session_uuid>").get();

  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.VerifySession.Get("<session_uuid>");

  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import (
      "fmt"
      "github.com/plivo/plivo-go/v7"
  )

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})

      response, _ := client.VerifySession.Get("<session_uuid>")

      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl "https://api.plivo.com/v1/Account/{auth_id}/Verify/Session/{session_uuid}/" \
    -u "{auth_id}:{auth_token}"
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "abf7fc2b-fac5-471c-9592-74ed6834b5e6",
    "session_uuid": "60ea68db-b123-46d9-9eb2-1201d516dbbd",
    "app_uuid": "ec66515e-86f6-4507-8620-31c039538d7a",
    "recipient": "919380013443",
    "channel": "voice",
    "status": "Expired",
    "count": 3,
    "attempt_details": [
        {
            "channel": "voice",
            "attempt_uuid": "90cc6cde-db80-4d14-9716-3aaa2b403377",
            "status": "answer",
            "time": "2023-06-01T08:52:39.363253Z"
        },
        {
            "channel": "sms",
            "attempt_uuid": "acbffc94-283b-42b3-8a96-65cbc18a9624",
            "status": "delivered",
            "time": "2023-06-01T08:52:59.484375Z"
        }
    ],
    "charges": {
        "total_charge": "0.113",
        "validation_charge": "0.0000",
        "attempt_charges": [
            {
                "attempt_uuid": "90cc6cde-db80-4d14-9716-3aaa2b403377",
                "channel": "voice",
                "charge": "0.03300"
            },
            {
                "attempt_uuid": "acbffc94-283b-42b3-8a96-65cbc18a9624",
                "channel": "sms",
                "charge": "0.08000"
            }
        ]
    },
    "created_at": "2023-06-01T08:52:39.363253Z",
    "updated_at": "2023-06-01T08:53:25.577153Z"
}
```

***

## List All Sessions

Retrieve a list of sessions based on filter criteria over the last 90 days.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Verify/Session/
```

<Note>
  The default rate limit is 20 requests per minute. Exceeding this limit returns "too many requests" error.
</Note>

### Query Parameters

<ParamField query="app_uuid" type="string">
  Filter by application UUID.
</ParamField>

<ParamField query="status" type="string">
  Filter by status. Values: `in-progress`, `verified`, `expired`.
</ParamField>

<ParamField query="recipient" type="string">
  Filter by destination number (E.164 format).
</ParamField>

<ParamField query="subaccount" type="string">
  Filter by subaccount.
</ParamField>

<ParamField query="limit" type="integer">
  Results per page. Max: 20. Default: 20.
</ParamField>

<ParamField query="offset" type="integer">
  Number of results to skip. Default: 0.
</ParamField>

<ParamField query="session_time" type="string">
  Filter by session initiation time. Format: `YYYY-MM-DD HH:MM`. Supports variants: `session_time__gt`, `session_time__gte`, `session_time__lt`, `session_time__lte`.
</ParamField>

<ParamField query="brand_name" type="string">
  Filter by brand name.
</ParamField>

<ParamField query="app_hash" type="string">
  Filter by app hash.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.verify_session.list(limit=10, offset=0)

  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.verify_session.list().then(response => {
      console.log(response);
  });
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.verify_session.list(limit: 10, offset: 0)

  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->verifySessions->list(['limit' => 10, 'offset' => 0]);

  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.verify_session.VerifySession;

  Plivo.init("<auth_id>", "<auth_token>");

  ListResponse<VerifySessionList> response = VerifySession.lister()
      .limit(10)
      .offset(0)
      .list();

  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.VerifySession.List(limit: 10, offset: 0);

  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import (
      "fmt"
      "github.com/plivo/plivo-go/v7"
  )

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})

      response, _ := client.VerifySession.List(plivo.SessionListParams{
          Limit:  10,
          Offset: 0,
      })

      fmt.Println(response)
  }
  ```

  ```bash cURL theme={null}
  curl "https://api.plivo.com/v1/Account/{auth_id}/Verify/Session/?limit=10&offset=0" \
    -u "{auth_id}:{auth_token}"
  ```
</CodeGroup>

### Response

```json  theme={null}
{
    "api_id": "3a7a0d6d-1b85-4593-921c-373e673a5799",
    "meta": {
        "limit": 20,
        "offset": 0,
        "next": null,
        "previous": null
    },
    "sessions": [
        {
            "session_uuid": "51e965f3-65a5-4ca0-9542-57154118a991",
            "app_uuid": "59728519-d145-45d6-8d46-60c06f7e8bbb",
            "recipient": "918681951370",
            "channel": "sms",
            "status": "expired",
            "count": 1,
            "attempt_details": [...],
            "charges": {...},
            "created_at": "2023-06-01T10:40:05.804031Z",
            "updated_at": "2023-06-01T10:40:05.804031Z"
        }
    ]
}
```

***

## Status Callbacks

Set up a server endpoint to receive real-time status updates for your verification sessions. Specify the callback URL when creating a session.

### Callback Attributes

<ParamField body="SessionUUID" type="string">
  Unique session identifier.
</ParamField>

<ParamField body="SessionStatus" type="string">
  Session status. Values: `in-progress`, `expired`.
</ParamField>

<ParamField body="AttemptUUID" type="string">
  Unique identifier for the SMS/call attempt.
</ParamField>

<ParamField body="AttemptSequence" type="string">
  Sequence number of the attempt.
</ParamField>

<ParamField body="Channel" type="string">
  Channel used. Values: `sms`, `voice`.
</ParamField>

<ParamField body="ChannelStatus" type="string">
  Attempt status. SMS: `queued`, `sent`, `delivered`, `failed`, `undelivered`. Voice: `in-progress`, `completed`, `ringing`.
</ParamField>

<ParamField body="ChannelErrorCode" type="string">
  Error code from the channel.
</ParamField>

<ParamField body="Recipient" type="string">
  Destination phone number.
</ParamField>

<ParamField body="RequestTime" type="string">
  UTC time when the attempt was created.
</ParamField>

### Callback Behavior

<Note>
  Plivo automatically retries webhooks three times if HTTP 200 is not returned:

  * First retry: 60 seconds after original attempt
  * Second retry: 120 seconds after first retry
  * Third retry: 240 seconds after second retry
</Note>

***

## Related

* [Overview](/programmable-api/verify/overview) - Quick start guide and concepts
