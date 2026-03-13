# Source: https://plivo.com/docs/number-masking/api/session.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Session API

> Create and manage anonymous calling sessions between two parties using virtual phone numbers

Number masking sessions establish anonymous connections between two phone numbers. When a session is created, Plivo assigns a virtual number that either party can call to connect to the other without revealing their actual phone numbers.

**API Endpoint**

```
https://api.plivo.com/v1/Account/{auth_id}/Masking/Session
```

***

## The Session Object

### Attributes

<ParamField body="session_uuid" type="string">
  Unique identifier for the session.
</ParamField>

<ParamField body="first_party" type="string">
  The actual phone number of the first participant.
</ParamField>

<ParamField body="second_party" type="string">
  The actual phone number of the second participant.
</ParamField>

<ParamField body="virtual_number" type="string">
  Plivo phone number to be dialed for connecting with the other participant.
</ParamField>

<ParamField body="status" type="string">
  Current session status. Values: `active`, `in-progress`, or `expired`.
</ParamField>

<ParamField body="session_expiry" type="integer">
  Time in seconds after which the session mapping will expire. Calls made after this will not be forwarded.
</ParamField>

<ParamField body="call_time_limit" type="integer">
  Time in seconds after which the call should be disconnected. Applies to all call legs.
</ParamField>

<ParamField body="ring_timeout" type="integer">
  Time in seconds after which the ring should be disconnected. Defaults to 120.
</ParamField>

<ParamField body="initiate_call_to_first_party" type="boolean">
  If `true`, Plivo calls the first party immediately and bridges if answered. Defaults to `false`.
</ParamField>

<ParamField body="record" type="boolean">
  Determines the recording status for a phone call. Defaults to `false`. If `true`, call recording starts only when both participants have answered.
</ParamField>

<ParamField body="record_file_format" type="string">
  Audio format for the recording. Values: `mp3`, `wav`. Defaults to `mp3`.
</ParamField>

<ParamField body="recording_callback_url" type="string">
  URL to which the call recording is sent.
</ParamField>

<ParamField body="recording_callback_method" type="string">
  HTTP verb for invoking `recording_callback_url`. Values: `GET`, `POST`. Defaults to `POST`.
</ParamField>

<ParamField body="callback_url" type="string">
  URL on which to receive important session events and status updates.
</ParamField>

<ParamField body="callback_method" type="string">
  HTTP verb for invoking `callback_url`. Values: `GET`, `POST`. Defaults to `POST`.
</ParamField>

<ParamField body="first_party_play_url" type="string">
  URL returning MP3/WAV file to play to first party before connecting.
</ParamField>

<ParamField body="second_party_play_url" type="string">
  URL returning MP3/WAV file to play to second party before connecting.
</ParamField>

<ParamField body="is_pin_authentication_required" type="boolean">
  Specifies whether PIN authentication is necessary when the call originates from an unidentified caller.
</ParamField>

<ParamField body="generate_pin" type="boolean">
  Indicates if Plivo generates the PIN for the session.
</ParamField>

<ParamField body="generate_pin_length" type="integer">
  Length of the PIN to be generated. Default: 4, Min: 4, Max: 15.
</ParamField>

<ParamField body="first_party_pin" type="string">
  The PIN for the first party when using a secondary number.
</ParamField>

<ParamField body="second_party_pin" type="string">
  The PIN for the second party when using a secondary number.
</ParamField>

<ParamField body="created_time" type="timestamp">
  UTC time when the session was created (yyyy-mm-dd, hh-mm-ss).
</ParamField>

<ParamField body="modified_time" type="timestamp">
  UTC time when the session was last modified (yyyy-mm-dd, hh-mm-ss).
</ParamField>

<ParamField body="expiry_time" type="timestamp">
  UTC time when the session will expire (yyyy-mm-dd, hh-mm-ss).
</ParamField>

<ParamField body="last_interaction_time" type="timestamp">
  UTC time when the latest interaction ended (yyyy-mm-dd, hh-mm-ss).
</ParamField>

<ParamField body="duration" type="integer">
  Duration of the session in seconds.
</ParamField>

<ParamField body="amount" type="string">
  Total charge incurred for creating the session.
</ParamField>

<ParamField body="total_call_count" type="integer">
  Total number of individual calls (call\_uuids) in the session.
</ParamField>

<ParamField body="total_call_amount" type="string">
  Total billed amount for all calls within the session.
</ParamField>

<ParamField body="total_call_billed_duration" type="integer">
  Total rounded bill duration (seconds) for all calls.
</ParamField>

<ParamField body="total_session_amount" type="string">
  Total charges for hosting the session, including call and session creation fees.
</ParamField>

<ParamField body="interaction" type="object">
  Interaction object containing session interactions.
</ParamField>

### Example Object

```json  theme={null}
{
  "first_party": "919003459051",
  "second_party": "918197241073",
  "virtual_number": "912269947011",
  "status": "active",
  "initiate_call_to_first_party": false,
  "first_party_pin": "1234",
  "second_party_pin": "4321",
  "is_pin_authentication_required": true,
  "generate_pin": false,
  "generate_pin_length": 4,
  "session_uuid": "c28b77d4-21e7-43bd-9447-04bfee92e651",
  "callback_url": "",
  "callback_method": "POST",
  "created_time": "2024-02-01 06:28:15 +0000 UTC",
  "modified_time": "2024-02-01 06:28:37 +0000 UTC",
  "expiry_time": "2024-02-01 06:58:15 +0000 UTC",
  "duration": 1800,
  "amount": 0,
  "call_time_limit": 14400,
  "ring_timeout": 45,
  "record": true,
  "record_file_format": "mp3",
  "recording_callback_url": "",
  "recording_callback_method": "POST",
  "interaction": null,
  "total_call_amount": 0,
  "total_call_count": 0,
  "total_call_billed_duration": 0,
  "total_session_amount": 0,
  "last_interaction_time": ""
}
```

***

## The Interaction Object

The Interaction object is nested within a session. A masking session can contain multiple interactions. Each interaction within a session has a maximum of two communication legs, regardless of the direction of the call.

### Attributes

<ParamField body="first_party_resource_url" type="string">
  URL of the call-leg resource created for the first party. This field is null if a call is exchanged between the Plivo virtual number and the second party but has not yet been initiated for the first party.
</ParamField>

<ParamField body="second_party_resource_url" type="string">
  URL of the call-leg resource created for the second party. This field is null if a call is exchanged between the Plivo virtual number and the first party but has not yet been initiated for the second party.
</ParamField>

<ParamField body="recording_resource_url" type="string">
  URL of the recording resource for the interaction. This field will be null when one of the participants didn't pick up the call.
</ParamField>

***

## Create a Session

Create a number masking session using the real phone numbers of two parties. Plivo returns a virtual number from your account that either party can call to connect anonymously.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Masking/Session
```

### Arguments

<ParamField body="first_party" type="string" required>
  The actual phone number of the first party.
</ParamField>

<ParamField body="second_party" type="string" required>
  The actual phone number of the second party.
</ParamField>

<ParamField body="geomatch" type="boolean">
  Specifies if the country of the virtual number must match the first\_party number. Default: `true`.
</ParamField>

<ParamField body="subaccount" type="string">
  Specifies the sub-account auth ID for which the session is created.
</ParamField>

<ParamField body="session_expiry" type="integer">
  Time in seconds after which session mapping ends. Default: 3600.
</ParamField>

<ParamField body="call_time_limit" type="integer">
  Time in seconds after which the call disconnects. Default: 3600.
</ParamField>

<ParamField body="ring_timeout" type="integer">
  Time in seconds after which ringing stops. Default: 120.
</ParamField>

<ParamField body="initiate_call_to_first_party" type="boolean">
  If `true`, Plivo calls first party immediately and bridges to second party. Default: `false`.
</ParamField>

<ParamField body="callback_url" type="string">
  URL to receive session events and status updates.
</ParamField>

<ParamField body="callback_method" type="string">
  HTTP method to invoke callback\_url. Values: `GET`, `POST`. Default: `POST`.
</ParamField>

<ParamField body="record" type="boolean">
  Call recording status. Default: `false`. If `true`, recording starts after both parties answer.
</ParamField>

<ParamField body="recording_callback_url" type="string">
  URL where call recordings are sent.
</ParamField>

<ParamField body="record_file_format" type="string">
  Audio format for recording. Values: `mp3`, `wav`. Default: `mp3`.
</ParamField>

<ParamField body="recording_callback_method" type="string">
  HTTP method to invoke recording\_callback\_url. Values: `GET`, `POST`. Default: `POST`.
</ParamField>

<ParamField body="first_party_play_url" type="string">
  URL to .mp3 or .wav file played to first party before connecting.
</ParamField>

<ParamField body="second_party_play_url" type="string">
  URL to .mp3 or .wav file played to second party before connecting.
</ParamField>

<ParamField body="is_pin_authentication_required" type="boolean">
  Specifies whether PIN authentication is necessary for unidentified callers. Default: `false`.
</ParamField>

<ParamField body="generate_pin" type="boolean">
  Indicates if Plivo generates the PIN. Only when is\_pin\_authentication\_required is `true`. Default: `false`.
</ParamField>

<ParamField body="generate_pin_length" type="integer">
  Length of the PIN to be generated. Applicable when generate\_pin is `true`. Default: 4, Min: 4, Max: 15.
</ParamField>

<ParamField body="first_party_pin" type="string">
  The PIN for the first party. Must differ from second\_party\_pin. Length: 4-15 digits.
</ParamField>

<ParamField body="second_party_pin" type="string">
  The PIN for the second party. Must differ from first\_party\_pin. Length: 4-15 digits.
</ParamField>

<ParamField body="pin_prompt_play" type="string">
  URL for playback prompting PIN entry. Required when PIN is activated. Must be .mp3 or .wav.
</ParamField>

<ParamField body="pin_retry" type="integer">
  Number of PIN retries allowed. Values: 0-5. Default: 1.
</ParamField>

<ParamField body="pin_retry_wait" type="integer">
  Wait time in seconds before retrying PIN. Default: 5, Min: 5, Max: 10.
</ParamField>

<ParamField body="incorrect_pin_play" type="string">
  URL for playback when incorrect PIN entered. Must be .mp3 or .wav.
</ParamField>

<ParamField body="unknown_caller_play" type="string">
  URL for playback when unknown caller calls the virtual number. Must be .mp3 or .wav.
</ParamField>

<ParamField body="force_pin_authentication" type="boolean">
  Requires PIN even for registered numbers. Only applies if PIN authentication is required. Default: `false`.
</ParamField>

<ParamField body="create_session_with_single_party" type="boolean">
  Allows session creation with only one party. Default: `false`.
</ParamField>

<ParamField body="virtual_number_cooloff_period" type="integer">
  Cool-off period in seconds before the virtual number can be reused. Default: 0, Max: 3600.
</ParamField>

<Note>
  The following parameters cannot be updated during an active session:

  * first\_party, second\_party
  * initiate\_call\_to\_first\_party
  * is\_pin\_authentication\_required
  * pin\_prompt\_play, pin\_retry, pin\_retry\_wait
  * incorrect\_pin\_play, unknown\_caller\_play
  * geomatch, subaccount
</Note>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.masking_sessions.create_masking_session(
      first_party="+12025550000",
      second_party="+12025551111"
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.maskingSession.createMaskingSession(
      '+12025550000', '+12025551111',
      { callTimeLimit: 600 }
  ).then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.maskingsession.create(
      first_party: '+12025550000',
      second_party: '+12025551111'
  )
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->maskingSessions->createMaskingSession(
      '+12025550000',
      '+12025551111'
  );
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.maskingsession.MaskingSession;
  import com.plivo.api.models.maskingsession.MaskingSessionCreateResponse;

  Plivo.init("<auth_id>", "<auth_token>");

  MaskingSessionCreateResponse response = MaskingSession
      .creator("+12025550000", "+12025551111")
      .create();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.MaskingSession.Create(
      firstParty: "+12025550000",
      secondParty: "+12025551111"
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

      response, _ := client.MaskingSession.CreateMaskingSession(
          plivo.CreateMaskingSessionParams{
              FirstParty:  "+12025550000",
              SecondParty: "+12025551111",
          },
      )
      fmt.Printf("Response: %#v\n", response)
  }
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Masking/Session" \
      -H "Content-Type: application/json" \
      -u "{auth_id}:{auth_token}" \
      -d '{
          "first_party": "+12025550000",
          "second_party": "+12025551111"
      }'
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "ae245217-f78e-4939-bc48-d4b8ef05cf66",
  "session_uuid": "4189591e-d004-4801-abdf-8893c15e5dcd",
  "virtual_number": "+912269947011",
  "message": "Session created",
  "session": {
    "first_party": "12025550000",
    "second_party": "12025551111",
    "virtual_number": "912269947011",
    "status": "active",
    "initiate_call_to_first_party": false,
    "session_uuid": "4189591e-d004-4801-abdf-8893c15e5dcd",
    "callback_url": "",
    "callback_method": "POST",
    "created_time": "2024-01-03 13:35:51 +0000 UTC",
    "modified_time": "2024-01-03 13:35:51 +0000 UTC",
    "expiry_time": "2024-01-03 14:05:51 +0000 UTC",
    "duration": 1800,
    "amount": 0,
    "call_time_limit": 14400,
    "ring_timeout": 45,
    "record": false,
    "record_file_format": "mp3",
    "recording_callback_url": "",
    "recording_callback_method": "POST",
    "interaction": null,
    "total_call_amount": 0,
    "total_call_count": 0,
    "total_call_billed_duration": 0,
    "total_session_amount": 0,
    "last_interaction_time": ""
  }
}
```

***

## Retrieve a Session

Fetch details of an existing masking session.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Masking/Session/{session_uuid}
```

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.masking_sessions.get_masking_session('<session_uuid>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.maskingSession.getMaskingSession('<session_uuid>')
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.maskingsession.get('<session_uuid>')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->maskingSessions->getMaskingSession('<session_uuid>');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.maskingsession.MaskingSession;

  Plivo.init("<auth_id>", "<auth_token>");

  MaskingSession response = MaskingSession.getter("<session_uuid>").get();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.MaskingSession.Get(sessionUuid: "<session_uuid>");
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

      response, _ := client.MaskingSession.GetMaskingSession("<session_uuid>")
      fmt.Printf("Response: %#v\n", response)
  }
  ```

  ```bash cURL theme={null}
  curl "https://api.plivo.com/v1/Account/{auth_id}/Masking/Session/{session_uuid}" \
      -u "{auth_id}:{auth_token}"
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "678c8b24-b703-43aa-8690-d28e7f163d18",
  "response": {
    "first_party": "919003459051",
    "second_party": "918197241073",
    "virtual_number": "912269947011",
    "status": "expired",
    "initiate_call_to_first_party": false,
    "session_uuid": "c28b77d4-21e7-43bd-9447-04bfee92e651",
    "callback_url": "",
    "callback_method": "POST",
    "created_time": "2024-02-01 06:28:15 +0000 UTC",
    "modified_time": "2024-02-01 06:28:37 +0000 UTC",
    "expiry_time": "2024-02-01 06:58:15 +0000 UTC",
    "duration": 1800,
    "amount": 0,
    "call_time_limit": 14400,
    "ring_timeout": 45,
    "record": true,
    "record_file_format": "mp3",
    "recording_callback_url": "",
    "recording_callback_method": "POST",
    "interaction": null,
    "total_call_amount": 0,
    "total_call_count": 0,
    "total_call_billed_duration": 0,
    "total_session_amount": 0,
    "last_interaction_time": ""
  }
}
```

***

## List All Sessions

Fetch details of all existing masking sessions.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Masking/Session
```

### Arguments

<ParamField query="first_party" type="string">
  Filter by first party phone number.
</ParamField>

<ParamField query="second_party" type="string">
  Filter by second party phone number.
</ParamField>

<ParamField query="virtual_number" type="string">
  Filter by virtual number assigned for the session.
</ParamField>

<ParamField query="status" type="string">
  Filter by status. Values: `active`, `expired`, `all`. Default: `all`.
</ParamField>

<ParamField query="created_time" type="string">
  Filter sessions by creation time. Format: `YYYY-MM-DD HH:MM[:ss[.uuuuuu]]`. Supports variants: `created_time__gt`, `created_time__gte`, `created_time__lt`, `created_time__lte`. Default window: 7 days. Max: 30 days.
</ParamField>

<ParamField query="expiry_time" type="string">
  Filter sessions by expiry time. Format: `YYYY-MM-DD HH:MM[:ss[.uuuuuu]]`. Supports variants: `expiry_time__gt`, `expiry_time__gte`, `expiry_time__lt`, `expiry_time__lte`. Default window: 7 days. Max: 30 days.
</ParamField>

<ParamField query="duration" type="string">
  Filter sessions by duration in seconds. Supports variants: `duration__gt`, `duration__gte`, `duration__lt`, `duration__lte`.
</ParamField>

<ParamField query="limit" type="integer">
  Number of results per page. Min: 1, Max: 20. Default: 20.
</ParamField>

<ParamField query="offset" type="integer">
  Number of results to skip. Used for pagination.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.masking_sessions.list_masking_session(status='active')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.maskingSession.listMaskingSession({ limit: 10 })
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.maskingsession.list()
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->maskingSessions->listMaskingSession(['status' => 'active']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.base.ListResponse;
  import com.plivo.api.models.maskingsession.MaskingSession;

  Plivo.init("<auth_id>", "<auth_token>");

  ListResponse<MaskingSession> response = MaskingSession.lister().list();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.MaskingSession.List();
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

      response, _ := client.MaskingSession.ListMaskingSession(
          plivo.ListSessionFilterParams{Limit: 10},
      )
      fmt.Printf("Response: %#v\n", response)
  }
  ```

  ```bash cURL theme={null}
  curl "https://api.plivo.com/v1/Account/{auth_id}/Masking/Session/?status=active" \
      -u "{auth_id}:{auth_token}"
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "7d962130-8eb6-49f1-920b-ae4609bf6dfe",
  "response": {
    "meta": {
      "limit": 20,
      "next": null,
      "offset": 0,
      "previous": null,
      "total_count": 1
    },
    "objects": [
      {
        "amount": 0,
        "call_time_limit": 14400,
        "callback_method": "POST",
        "callback_url": "",
        "created_time": "2024-02-01 06:28:15 +0000 UTC",
        "duration": 1800,
        "expiry_time": "2024-02-01 06:58:15 +0000 UTC",
        "first_party": "919003459051",
        "initiate_call_to_first_party": false,
        "interaction": null,
        "last_interaction_time": "",
        "modified_time": "2024-02-01 06:28:37 +0000 UTC",
        "record": true,
        "record_file_format": "mp3",
        "recording_callback_method": "POST",
        "recording_callback_url": "",
        "resource_uri": "/v1/Account/MAOTQ3NGFLNZRMZME1MT/Masking/Session/c28b77d4-21e7-43bd-9447-04bfee92e651/",
        "ring_timeout": 45,
        "second_party": "918197241073",
        "session_uuid": "c28b77d4-21e7-43bd-9447-04bfee92e651",
        "status": "expired",
        "total_call_amount": 0,
        "total_call_billed_duration": 0,
        "total_call_count": 0,
        "total_session_amount": 0,
        "virtual_number": "912269947011"
      }
    ]
  }
}
```

***

## Update a Session

Update an existing masking session.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Masking/Session/{session_uuid}
```

### Arguments

<ParamField body="session_expiry" type="integer">
  Time in seconds after which the session mapping will end. Default: 3600.
</ParamField>

<ParamField body="call_time_limit" type="integer">
  Time in seconds after which the call will be disconnected. Default: 3600.
</ParamField>

<ParamField body="ring_timeout" type="integer">
  Time in seconds after which the ring will be disconnected. Default: 120.
</ParamField>

<ParamField body="callback_url" type="string">
  URL to receive session events and status updates.
</ParamField>

<ParamField body="callback_method" type="string">
  HTTP verb to invoke callback\_url. Values: `GET`, `POST`. Default: `POST`.
</ParamField>

<ParamField body="record" type="boolean">
  Recording status for phone calls. Default: `false`.
</ParamField>

<ParamField body="recording_callback_url" type="string">
  URL to which the call recording is sent.
</ParamField>

<ParamField body="record_file_format" type="string">
  Audio format for the recording. Values: `mp3`, `wav`. Default: `mp3`.
</ParamField>

<ParamField body="recording_callback_method" type="string">
  HTTP verb to invoke recording\_callback\_url. Values: `GET`, `POST`. Default: `POST`.
</ParamField>

<ParamField body="first_party_play_url" type="string">
  URL that returns an .mp3 or .wav file to be played to the first party.
</ParamField>

<ParamField body="second_party_play_url" type="string">
  URL that returns an .mp3 or .wav file to be played to the second party.
</ParamField>

<ParamField body="first_party" type="string">
  The phone number of the first participant. Only applicable when session was created with `create_session_with_single_party` set to `true`.
</ParamField>

<ParamField body="second_party" type="string">
  The phone number of the second participant. Only applicable when session was created with `create_session_with_single_party` set to `true`.
</ParamField>

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.masking_sessions.update_masking_session(
      session_uuid='<session_uuid>',
      call_time_limit=3600,
      record=True
  )
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.maskingSession.updateMaskingSession('<session_uuid>', {
      sessionExpiry: 120
  }).then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.maskingsession.update(
      '<session_uuid>',
      { call_time_limit: 1440, record: true }
  )
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->maskingSessions->updateMaskingSession(
      '<session_uuid>',
      ['call_time_limit' => 3600]
  );
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.maskingsession.MaskingSession;
  import com.plivo.api.models.maskingsession.MaskingSessionUpdateResponse;

  Plivo.init("<auth_id>", "<auth_token>");

  MaskingSessionUpdateResponse response = MaskingSession.updater("<session_uuid>")
      .callTimeLimit(14400)
      .record(true)
      .update();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.MaskingSession.Update(
      sessionUuid: "<session_uuid>",
      sessionExpiry: 6000
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

      response, _ := client.MaskingSession.UpdateMaskingSession(
          plivo.UpdateMaskingSessionParams{SessionExpiry: 120},
          "<session_uuid>",
      )
      fmt.Printf("Response: %#v\n", response)
  }
  ```

  ```bash cURL theme={null}
  curl -X POST "https://api.plivo.com/v1/Account/{auth_id}/Masking/Session/{session_uuid}" \
      -H "Content-Type: application/json" \
      -u "{auth_id}:{auth_token}" \
      -d '{"record": true}'
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "32d333cb-3709-4b9b-b27b-3296aca6e1cc",
  "message": "Session updated",
  "session": {
    "first_party": "919003459051",
    "second_party": "918197241073",
    "virtual_number": "912269947011",
    "status": "active",
    "initiate_call_to_first_party": false,
    "session_uuid": "c28b77d4-21e7-43bd-9447-04bfee92e651",
    "callback_url": "",
    "callback_method": "POST",
    "created_time": "2024-02-01 06:28:15 +0000 UTC",
    "modified_time": "2024-02-01 06:28:37 +0000 UTC",
    "expiry_time": "2024-02-01 06:58:15 +0000 UTC",
    "duration": 1800,
    "amount": 0,
    "call_time_limit": 14400,
    "ring_timeout": 45,
    "record": true,
    "record_file_format": "mp3",
    "recording_callback_url": "",
    "recording_callback_method": "POST",
    "interaction": null,
    "total_call_amount": 0,
    "total_call_count": 0,
    "total_call_billed_duration": 0,
    "total_session_amount": 0,
    "last_interaction_time": ""
  }
}
```

***

## Expire a Session

Terminate an ongoing session and mark it as expired.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Masking/Session/{session_uuid}
```

### Example

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')

  response = client.masking_sessions.delete_masking_session('<session_uuid>')
  print(response)
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');

  client.maskingSession.deleteMaskingSession('<session_uuid>')
      .then(response => console.log(response));
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  client = Plivo::RestClient.new('<auth_id>', '<auth_token>')

  response = client.maskingsession.delete('<session_uuid>')
  puts response
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');

  $response = $client->maskingSessions->deleteMaskingSession('<session_uuid>');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.maskingsession.MaskingSession;

  Plivo.init("<auth_id>", "<auth_token>");

  MaskingSession.deleter("<session_uuid>").delete();
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>", "<auth_token>");

  var response = api.MaskingSession.Delete(sessionUuid: "<session_uuid>");
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

      response, _ := client.MaskingSession.DeleteMaskingSession("<session_uuid>")
      fmt.Printf("Response: %#v\n", response)
  }
  ```

  ```bash cURL theme={null}
  curl -X DELETE "https://api.plivo.com/v1/Account/{auth_id}/Masking/Session/{session_uuid}" \
      -u "{auth_id}:{auth_token}"
  ```
</CodeGroup>

***

## Session Callbacks

### Session Status Callback

Configure the `callback_url` to receive important session events and status updates.

#### Events

<ParamField body="SessionFirstPartyAnswer" type="event">
  Triggered when the first party answers the call.
</ParamField>

<ParamField body="SessionSecondPartyRing" type="event">
  Triggered when the second party's phone starts ringing.
</ParamField>

<ParamField body="SessionSecondPartyAnswer" type="event">
  Triggered when the second party answers the call.
</ParamField>

<ParamField body="SessionSecondPartyHangup" type="event">
  Triggered when the second party disconnects the call.
</ParamField>

<ParamField body="SessionFirstPartyHangup" type="event">
  Triggered when the first party disconnects the call.
</ParamField>

<ParamField body="SessionPinAuthenticationStatus" type="event">
  Triggered when the PIN authentication status is success, failed, or if the call is from an authorized caller.
</ParamField>

<ParamField body="SessionTimeout" type="event">
  Triggered when the session expires.
</ParamField>

<ParamField body="SessionPartiesHangup" type="event">
  Triggered when the session call is done.
</ParamField>

#### Callback Attributes

<ParamField body="EventName" type="string">
  Event that triggered this callback.
</ParamField>

<ParamField body="EventTimestamp" type="string">
  Timestamp in UTC at which the event occurred.
</ParamField>

<ParamField body="SessionUUID" type="string">
  Unique ID of the masking session.
</ParamField>

<ParamField body="From" type="string">
  Actual from number used to interact with the virtual number.
</ParamField>

<ParamField body="To" type="string">
  Actual to number dialing out from the virtual number.
</ParamField>

<ParamField body="VirtualNumber" type="string">
  The virtual number used in the session.
</ParamField>

<ParamField body="PinAuthenticationStatus" type="string">
  Status of the PIN authentication. Values: `success`, `failed`, `AuthorizedCaller`.
</ParamField>

<ParamField body="PinRetryCounter" type="integer">
  Indicates the PIN retry counter due to incorrect PIN input.
</ParamField>

<ParamField body="Amount" type="string">
  Total amount incurred for the call.
</ParamField>

<ParamField body="BilledDuration" type="string">
  Duration in seconds for which the call was billed.
</ParamField>

<ParamField body="Duration" type="string">
  Actual duration of the call in seconds.
</ParamField>

<ParamField body="PlivoHangupCause" type="string">
  Reason for the call termination.
</ParamField>

<ParamField body="PlivoHangupCauseCode" type="integer">
  A unique integer code for the termination cause.
</ParamField>

<ParamField body="SequenceNumber" type="string">
  Indicates the sequence of the callback. Helpful for sorting events.
</ParamField>

***

### Session Recording Callback

Configure the `recording_callback_url` to receive recording-related callback events.

#### Events

<ParamField body="SessionRecordingInitiated" type="event">
  Triggered when the first party and the second party are connected via the virtual phone number and the recording begins.
</ParamField>

<ParamField body="SessionRecordingCompleted" type="event">
  Triggered when one of the parties disconnects the call.
</ParamField>

<ParamField body="SessionRecordingFailed" type="event">
  Triggered when the record attribute is set to true but the recording could not be started.
</ParamField>

#### Recording Callback Attributes

<ParamField body="EventName" type="string">
  Event that triggered this callback.
</ParamField>

<ParamField body="EventTimestamp" type="string">
  Timestamp at which the event occurred.
</ParamField>

<ParamField body="SessionUUID" type="string">
  Unique ID of the masking session.
</ParamField>

<ParamField body="From" type="string">
  Actual from number used to interact with the virtual number.
</ParamField>

<ParamField body="To" type="string">
  Actual to number dialing out from the virtual number.
</ParamField>

<ParamField body="VirtualNumber" type="string">
  The virtual number used in the session.
</ParamField>

<ParamField body="RecordingUUID" type="string">
  Unique identifier of the recording file.
</ParamField>

<ParamField body="RecordingURL" type="string">
  Actual media URL path of the recording.
</ParamField>

<ParamField body="RecordingResourceURL" type="string">
  Complete URL path to the recording resource URL.
</ParamField>

<ParamField body="RecordingDuration" type="string">
  Duration of recording in seconds.
</ParamField>

<ParamField body="RecordingStartTime" type="string">
  UTC Timestamp at which the recording started.
</ParamField>

<ParamField body="RecordingEndTime" type="string">
  UTC Timestamp at which the recording ended.
</ParamField>

<ParamField body="RecordingFormat" type="string">
  Format of the recording. Values: `.mp3`, `.wav`.
</ParamField>

<ParamField body="SequenceNumber" type="string">
  Indicates the sequence of the callback.
</ParamField>
