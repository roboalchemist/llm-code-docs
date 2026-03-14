# Source: https://plivo.com/docs/voice/api/multiparty-calls.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Multiparty Calls

> Create and manage multiparty calls with role-based audio routing for contact center scenarios

Multiparty Calls (MPC) enable role-based conference calling with separate audio routing for agents, customers, and supervisors. Unlike standard conferences, MPCs support coach mode where supervisors can speak privately to agents without customers hearing.

## The Multiparty Call Object

| Attribute                | Type        | Description                                                                     |
| ------------------------ | ----------- | ------------------------------------------------------------------------------- |
| `mpc_uuid`               | `string`    | Unique identifier for the multiparty call.                                      |
| `friendly_name`          | `string`    | User-defined name for the MPC. Must be unique per account across all live MPCs. |
| `status`                 | `string`    | Current status. Values: `Initialized`, `Active`, `Ended`.                       |
| `creation_time`          | `timestamp` | When the MPC was created. Format: `YYYY-MM-DD HH:mm:ss±hh:mm`.                  |
| `start_time`             | `timestamp` | When the MPC started (first participant joined).                                |
| `end_time`               | `timestamp` | When the MPC ended. `null` if still active.                                     |
| `duration`               | `integer`   | Total duration in seconds. `null` if not ended.                                 |
| `billed_duration`        | `integer`   | Billable duration in seconds.                                                   |
| `billed_amount`          | `string`    | Total billed amount in USD.                                                     |
| `max_participants`       | `integer`   | Maximum participants allowed.                                                   |
| `max_duration`           | `integer`   | Maximum duration in seconds from initiation.                                    |
| `stay_alone`             | `boolean`   | Whether participants can remain alone in the MPC.                               |
| `recording`              | `string`    | Recording status. Values: `recording`, `not-recording`, `paused`.               |
| `participants`           | `string`    | URL to the participants list.                                                   |
| `termination_cause`      | `string`    | Reason the MPC ended.                                                           |
| `termination_cause_code` | `integer`   | Numeric code for termination cause.                                             |
| `sub_account`            | `string`    | Subaccount associated with the MPC.                                             |
| `resource_uri`           | `string`    | URI of the MPC resource.                                                        |

### Example MPC Object

```json  theme={null}
{
  "billed_amount": null,
  "billed_duration": null,
  "creation_time": "2020-12-24 09:20:03+00:00",
  "duration": null,
  "end_time": null,
  "friendly_name": "test_mpc",
  "mpc_uuid": "8742d531-292a-46aa-8754-836be1092885",
  "participants": "/v1/Account/MAOTE1OWE0MDK0MTLHYW/MultiPartyCall/name_test_mpc/Participant/",
  "recording": "not-recording",
  "resource_uri": "/v1/Account/MAOTE1OWE0MDK0MTLHYW/MultiPartyCall/name_test_mpc/",
  "start_time": "2020-12-24 09:20:03+00:00",
  "status": "Active",
  "stay_alone": false,
  "sub_account": null,
  "termination_cause": null,
  "termination_cause_code": null
}
```

***

## The Participant Object

| Attribute                | Type        | Description                                                                                                                                           |
| ------------------------ | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `member_id`              | `string`    | Unique ID for this participant in the MPC.                                                                                                            |
| `mpc_uuid`               | `string`    | UUID of the parent multiparty call.                                                                                                                   |
| `call_uuid`              | `string`    | UUID of the call resource.                                                                                                                            |
| `role`                   | `string`    | Participant role. Values: `Agent`, `Customer`, `Supervisor`. Cannot be changed after set.                                                             |
| `coach_mode`             | `boolean`   | For supervisors only. When `true`, supervisor audio is only heard by agents, not customers.                                                           |
| `join_time`              | `timestamp` | When the participant joined. Format: `YYYY-MM-DD HH:mm:ss±hh:mm`.                                                                                     |
| `exit_time`              | `timestamp` | When the participant left. `null` if still active.                                                                                                    |
| `duration`               | `integer`   | Duration in seconds the participant was in the MPC.                                                                                                   |
| `billed_duration`        | `integer`   | Billable duration in seconds.                                                                                                                         |
| `billed_amount`          | `string`    | Amount billed for this participant.                                                                                                                   |
| `mute`                   | `boolean`   | Whether the participant is muted.                                                                                                                     |
| `hold`                   | `boolean`   | Whether hold music is playing for this participant.                                                                                                   |
| `start_mpc_on_enter`     | `boolean`   | Whether MPC started when this participant entered.                                                                                                    |
| `end_mpc_on_exit`        | `boolean`   | Whether MPC ends when this participant leaves.                                                                                                        |
| `participant_exit_cause` | `string`    | Reason participant left. Values: `Participant Call Hangup`, `Kicked Out of Multiparty Call`, `Multiparty Call Ended`, `Participant Call Transferred`. |

### Example Participant Object

```json  theme={null}
{
  "billed_amount": null,
  "billed_duration": null,
  "call_uuid": "dd473c48-34a6-4d67-a033-af590b41c23f",
  "coach_mode": false,
  "duration": null,
  "end_mpc_on_exit": false,
  "exit_cause": null,
  "exit_time": null,
  "hold": false,
  "join_time": "2020-12-24 10:01:56+00:00",
  "member_id": "355",
  "mpc_uuid": "4e9ae3f1-a29c-4524-a1b4-4758922e589b",
  "mute": false,
  "resource_uri": "/v1/Account/MAOTE1OWE0MDK0MTLHYW/MultiPartyCall/name_test_mpc_1/Participant/355/",
  "role": "agent",
  "start_mpc_on_enter": true
}
```

***

## Retrieve a Multiparty Call

Get details of a specific multiparty call.

```
GET https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/
GET https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/uuid_{mpc_uuid}/
```

<Note>
  You can fetch details using the MPC name only for ongoing calls. For ended calls, use the UUID.
</Note>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.multi_party_calls.get(friendly_name='mpc_name')
  # Or by UUID
  response = client.multi_party_calls.get(uuid='8742d531-292a-46aa-8754-836be1092885')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  response = api.multipartycalls.get(friendly_name: 'mpc_name')
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.multiPartyCalls.get('mpc_name').then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');
  $response = $client->multiPartyCalls->get(['friendly_name' => 'mpc_name']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.multipartycall.MultiPartyCall;
  import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

  Plivo.init('<auth_id>', '<auth_token>');
  MultiPartyCall mpc = MultiPartyCall.getter(MultiPartyCallUtils.friendlyName('mpc_name')).get();
  System.out.println(mpc);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi('<auth_id>', '<auth_token>');
  var response = api.MultiPartyCall.Get(friendlyName: "mpc_name");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.MultiPartyCall.Get(plivo.MultiPartyCallBasicParams{
          FriendlyName: "mpc_name",
      })
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/
  ```
</CodeGroup>

***

## List All Multiparty Calls

Retrieve all multiparty calls with optional filters.

```
GET https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/
```

### Arguments

| Parameter                | Description                                                                                                                                                   |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `friendly_name`          | Filter by MPC name.                                                                                                                                           |
| `status`                 | Filter by status. Values: `initialized`, `active`, `ended`.                                                                                                   |
| `termination_cause_code` | Filter by termination code: `1000` (No Active Participants), `1010` (Stay Alone Not Permitted), `2000` (Max Duration Reached), `3000` (Hangup API Triggered). |
| `end_time`               | Filter by end time. Supports `__gt`, `__gte`, `__lt`, `__lte`. Format: `YYYY-MM-DD HH:MM[:ss]`.                                                               |
| `creation_time`          | Filter by creation time. Same format and suffixes as `end_time`.                                                                                              |
| `limit`                  | Results per page. Max: 20. Default: 20.                                                                                                                       |
| `offset`                 | Number of records to skip for pagination.                                                                                                                     |

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.multi_party_calls.list()
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  response = api.multipartycalls.list
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.multiPartyCalls.list().then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');
  $response = $client->multiPartyCalls->getList();
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.multipartycall.MultiPartyCall;

  Plivo.init('<auth_id>', '<auth_token>');
  ListResponse<MultiPartyCall> response = MultiPartyCall.lister().list();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi('<auth_id>', '<auth_token>');
  var response = api.MultiPartyCall.List();
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.MultiPartyCall.List(plivo.MultiPartyCallListParams{})
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "ed93aea0-45cd-11eb-8530-0242ac110006",
  "meta": {
    "count": 2,
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null
  },
  "objects": [
    {
      "billed_amount": "0.05000",
      "billed_duration": 60,
      "creation_time": "2020-12-24 15:23:38+05:30",
      "duration": 2,
      "end_time": "2020-12-24 15:23:40+05:30",
      "friendly_name": "test_mpc_1",
      "mpc_uuid": "4ed623a5-9f3e-45e0-9e7e-3d19a94b3bd3",
      "status": "Ended",
      "termination_cause": "No Active Participants",
      "termination_cause_code": 1000
    }
  ]
}
```

***

## Activate a Multiparty Call

Activate an MPC that was initialized with `start_mpc_on_enter` set to `false`.

```
POST https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/
```

### Arguments

| Parameter | Description                                 |
| --------- | ------------------------------------------- |
| `status`  | Required. Set to `Active` to start the MPC. |

<Note>
  This API only activates an MPC in the initialized state. To start a new MPC, use the [Add Participant API](#add-a-participant) or [MultiPartyCall XML](/voice/xml/multipartycall/).
</Note>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.multi_party_calls.start(friendly_name='mpc_name')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  response = api.multipartycalls.start(friendly_name: 'mpc_name')
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.multiPartyCalls.start('mpc_name').then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');
  $response = $client->multiPartyCalls->start(['friendly_name' => 'mpc_name']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.multipartycall.MultiPartyCall;
  import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

  Plivo.init('<auth_id>', '<auth_token>');
  MultiPartyCall.starter(MultiPartyCallUtils.friendlyName('mpc_name')).update();
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi('<auth_id>', '<auth_token>');
  var response = api.MultiPartyCall.Start(friendlyName: "mpc_name");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      client.MultiPartyCall.Start(plivo.MultiPartyCallBasicParams{FriendlyName: "mpc_name"})
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN -X POST \
      -d '{"status": "active"}' \
      https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/
  ```
</CodeGroup>

### Response

```
HTTP Status Code: 204
```

***

## End a Multiparty Call

Terminate an ongoing MPC.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/
```

When the MPC ends:

* Participants added via XML proceed to the next element or `onExitActionUrl`
* Participants added via API are disconnected with hangup cause code `4020` or proceed to `on_exit_action_url`

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.multi_party_calls.stop(friendly_name='mpc_name')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  response = api.multipartycalls.stop(friendly_name: 'mpc_name')
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.multiPartyCalls.stop('mpc_name').then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');
  $response = $client->multiPartyCalls->stop(['friendly_name' => 'mpc_name']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.multipartycall.MultiPartyCall;
  import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

  Plivo.init('<auth_id>', '<auth_token>');
  MultiPartyCall.stopper(MultiPartyCallUtils.friendlyName('mpc_name')).delete();
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi('<auth_id>', '<auth_token>');
  var response = api.MultiPartyCall.Stop(friendlyName: "mpc_name");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      client.MultiPartyCall.Stop(plivo.MultiPartyCallBasicParams{FriendlyName: "mpc_name"})
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN -X DELETE \
      https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/
  ```
</CodeGroup>

### Response

```
HTTP Status Code: 204
```

***

## Add a Participant

Add a participant to an existing MPC or start a new MPC. Plivo creates a new MPC if no ongoing call with the given name exists.

```
POST https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/
```

### Required Arguments

| Parameter | Description                                                     |
| --------- | --------------------------------------------------------------- |
| `role`    | Participant role. Values: `agent`, `supervisor`, `customer`.    |
| `from`    | Caller ID for the outbound call (E.164 format or SIP endpoint). |
| `to`      | Destination number or SIP endpoint.                             |

### Optional Arguments

| Parameter                     | Default  | Description                                                      |
| ----------------------------- | -------- | ---------------------------------------------------------------- |
| `caller_name`                 |          | Caller name for SIP endpoints.                                   |
| `call_uuid`                   |          | Add an existing call to the MPC.                                 |
| `call_status_callback_url`    |          | URL for call status events.                                      |
| `call_status_callback_method` | `POST`   | HTTP method for status callbacks.                                |
| `confirm_key`                 |          | DTMF key participant must press to join.                         |
| `confirm_key_sound_url`       |          | Audio to play before confirm key.                                |
| `dial_music`                  | `Real`   | Music/ringtone while connecting. Use `real` for ringback or URL. |
| `ring_timeout`                | 45       | Seconds to ring before timeout.                                  |
| `max_duration`                | 14400    | Max call duration in seconds.                                    |
| `max_participants`            | 10       | Max participants allowed (2-10).                                 |
| `record_min_member_count`     | 1        | Min members before recording starts.                             |
| `wait_music_url`              |          | Music URL while waiting for MPC to start.                        |
| `agent_hold_music_url`        |          | Hold music URL for agents.                                       |
| `customer_hold_music_url`     |          | Hold music URL for customers.                                    |
| `recording_callback_url`      |          | URL for recording events.                                        |
| `status_callback_url`         |          | URL for participant status events.                               |
| `on_exit_action_url`          |          | URL to fetch XML when participant exits.                         |
| `stay_alone`                  | `false`  | Allow participant to stay alone.                                 |
| `coach_mode`                  | `true`   | For supervisors: whether to whisper to agents only.              |
| `mute`                        | `false`  | Join muted.                                                      |
| `hold`                        | `false`  | Join on hold.                                                    |
| `start_mpc_on_enter`          | `true`   | Start MPC when participant joins.                                |
| `end_mpc_on_exit`             | `false`  | End MPC when participant leaves.                                 |
| `enter_sound`                 | `beep:1` | Sound when joining. Values: `beep:1`, `beep:2`, `none`, or URL.  |
| `enter_sound_method`          | `GET`    | HTTP method for enter\_sound URL.                                |
| `exit_sound`                  | `beep:2` | Sound when leaving. Same values as enter\_sound.                 |

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.multi_party_calls.add_participant(
      friendly_name='mpc_name',
      role='agent',
      from_='+14151234567',
      to_='+14157654321',
      start_mpc_on_enter=True,
      enter_sound='beep:1'
  )
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  response = api.multipartycalls.add_participant(
    friendly_name: 'mpc_name',
    role: 'agent',
    from: '+14151234567',
    to: '+14157654321'
  )
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.multiPartyCalls.addParticipant({
      friendlyName: 'mpc_name',
      role: 'agent',
      from: '+14151234567',
      to: '+14157654321'
  }).then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');
  $response = $client->multiPartyCalls->addParticipant([
      'friendly_name' => 'mpc_name',
      'role' => 'agent',
      'from' => '+14151234567',
      'to' => '+14157654321'
  ]);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.multipartycall.MultiPartyCall;
  import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

  Plivo.init('<auth_id>', '<auth_token>');
  MultiPartyCall.adder(MultiPartyCallUtils.friendlyName('mpc_name'), 'agent')
      .from('+14151234567')
      .to('+14157654321')
      .create();
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi('<auth_id>', '<auth_token>');
  var response = api.MultiPartyCall.AddParticipant(
      friendlyName: "mpc_name",
      role: "agent",
      from: "+14151234567",
      to: "+14157654321"
  );
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      client.MultiPartyCall.AddParticipant(plivo.MultiPartyCallBasicParams{
          FriendlyName: "mpc_name",
      }, plivo.MultiPartyCallAddParticipantParams{
          Role: "agent",
          From: "+14151234567",
          To:   "+14157654321",
      })
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"role": "agent", "from": "+14151234567", "to": "+14157654321"}' \
      https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/
  ```
</CodeGroup>

***

## Retrieve a Participant

Get details of a specific participant.

```
GET https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/{member_id}/
```

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.multi_party_calls.get_participant(
      participant_id='355',
      friendly_name='mpc_name'
  )
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  response = api.multipartycalls.get_participant(
    friendly_name: 'mpc_name',
    member_id: '355'
  )
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.multiPartyCalls.getParticipant('355', null, 'mpc_name').then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');
  $response = $client->multiPartyCalls->getParticipant('355', ['friendly_name' => 'mpc_name']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.multipartycall.MultiPartyCall;
  import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

  Plivo.init('<auth_id>', '<auth_token>');
  MultiPartyCall.participantGetter(MultiPartyCallUtils.friendlyName('mpc_name'), '355').get();
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi('<auth_id>', '<auth_token>');
  var response = api.MultiPartyCall.GetParticipant(
      friendlyName: "mpc_name",
      participantId: "355"
  );
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.MultiPartyCall.GetParticipant(plivo.MultiPartyCallParticipantParams{
          FriendlyName:  "mpc_name",
          ParticipantId: "355",
      })
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/{member_id}/
  ```
</CodeGroup>

***

## List All Participants

Retrieve all participants in a multiparty call.

```
GET https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/
```

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.multi_party_calls.list_participants(friendly_name='mpc_name')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  response = api.multipartycalls.list_participants(friendly_name: 'mpc_name')
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.multiPartyCalls.listParticipants(null, 'mpc_name').then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');
  $response = $client->multiPartyCalls->listParticipants(['friendly_name' => 'mpc_name']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.multipartycall.MultiPartyCall;
  import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

  Plivo.init('<auth_id>', '<auth_token>');
  MultiPartyCall.participantList(MultiPartyCallUtils.friendlyName('mpc_name')).list();
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi('<auth_id>', '<auth_token>');
  var response = api.MultiPartyCall.ListParticipants(friendlyName: "mpc_name");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.MultiPartyCall.ListParticipants(
          plivo.MultiPartyCallBasicParams{FriendlyName: "mpc_name"},
          plivo.MultiPartyCallListParticipantParams{},
      )
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "2de9cf75-9606-11eb-8ca5-0242ac110006",
  "meta": {
    "count": 3,
    "limit": 20,
    "offset": 0
  },
  "objects": [
    {
      "call_uuid": "58e76e86-54b8-402e-9d83-a16e29b6582c",
      "coach_mode": true,
      "hold": false,
      "member_id": "229",
      "mpc_uuid": "d5c8be43-87d0-4ba6-90a1-011bb6ab0a00",
      "mute": false,
      "role": "supervisor"
    },
    {
      "call_uuid": "9def1955-870f-4052-84ca-02063d24105d",
      "coach_mode": false,
      "hold": false,
      "member_id": "228",
      "mpc_uuid": "d5c8be43-87d0-4ba6-90a1-011bb6ab0a00",
      "mute": false,
      "role": "customer"
    },
    {
      "call_uuid": "b4e8210e-9cd5-4d92-b989-2ff889ee0e1f",
      "coach_mode": false,
      "hold": false,
      "member_id": "226",
      "mpc_uuid": "d5c8be43-87d0-4ba6-90a1-011bb6ab0a00",
      "mute": false,
      "role": "agent"
    }
  ]
}
```

***

## Update a Participant

Mute, unmute, hold, or unhold a participant. Can also toggle coach mode for supervisors.

```
POST https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/{member_id}/
```

The `{member_id}` can be a specific ID, comma-separated list, or `all` to affect all participants.

### Arguments

| Parameter    | Description                                                                      |
| ------------ | -------------------------------------------------------------------------------- |
| `mute`       | `true` to mute, `false` to unmute.                                               |
| `hold`       | `true` to hold (plays hold music), `false` to unhold.                            |
| `coach_mode` | For supervisors only. `true` = whisper to agents only, `false` = audible to all. |

<Note>
  `coach_mode` can only be updated for individual participants, not with `all`.
</Note>

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.multi_party_calls.update_participant(
      participant_id='355',
      friendly_name='mpc_name',
      mute=True,
      hold=False
  )
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  response = api.multipartycalls.update_participant(
    friendly_name: 'mpc_name',
    member_id: '355',
    mute: true
  )
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.multiPartyCalls.updateParticipant('355', null, 'mpc_name', {
      mute: true,
      hold: false
  }).then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');
  $response = $client->multiPartyCalls->updateParticipant('355', [
      'friendly_name' => 'mpc_name',
      'mute' => true
  ]);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.multipartycall.MultiPartyCall;
  import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

  Plivo.init('<auth_id>', '<auth_token>');
  MultiPartyCall.participantUpdater(MultiPartyCallUtils.friendlyName('mpc_name'), '355')
      .mute(true)
      .update();
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi('<auth_id>', '<auth_token>');
  var response = api.MultiPartyCall.UpdateParticipant(
      participantId: "355",
      friendlyName: "mpc_name",
      mute: true
  );
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      mute := true
      client.MultiPartyCall.UpdateParticipant(
          plivo.MultiPartyCallParticipantParams{FriendlyName: "mpc_name", ParticipantId: "355"},
          plivo.MultiPartyCallUpdateParticipantParams{Mute: &mute},
      )
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{"mute": true, "hold": false}' \
      https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/{member_id}/
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "03042285-45d9-11eb-9014-0242ac110003",
  "mute": "MPC: test_mpc_1 mute/unmute member(s) succeeded",
  "hold": "MPC: test_mpc_1 hold/unhold member(s) succeeded"
}
```

***

## Kick a Participant

Remove a participant from the MPC.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/{member_id}/
```

The `{member_id}` can be a specific ID, comma-separated list, or `all` to kick all participants.

<CodeGroup>
  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>', '<auth_token>')
  response = client.multi_party_calls.kick_participant(
      participant_id='355',
      friendly_name='mpc_name'
  )
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
  response = api.multipartycalls.kick_participant(
    friendly_name: 'mpc_name',
    member_id: '355'
  )
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client('<auth_id>', '<auth_token>');
  client.multiPartyCalls.kickParticipant('355', {friendlyName: 'mpc_name'}).then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient('<auth_id>', '<auth_token>');
  $response = $client->multiPartyCalls->kickParticipant('355', ['friendly_name' => 'mpc_name']);
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.multipartycall.MultiPartyCall;
  import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

  Plivo.init('<auth_id>', '<auth_token>');
  MultiPartyCall.participantGetter(MultiPartyCallUtils.friendlyName('mpc_name'), '355').get().kick();
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi('<auth_id>', '<auth_token>');
  var response = api.MultiPartyCall.KickParticipant(
      participantId: "355",
      friendlyName: "mpc_name"
  );
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      client.MultiPartyCall.KickParticipant(plivo.MultiPartyCallParticipantParams{
          FriendlyName:  "mpc_name",
          ParticipantId: "355",
      })
  }
  ```

  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN -X DELETE \
      https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/{member_id}/
  ```
</CodeGroup>

### Response

```
HTTP Status Code: 204
```

***

## Record a Multiparty Call

<Tabs>
  <Tab title="Start Recording">
    Start recording the entire MPC.

    ```
    POST https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Record/
    ```

    ### Arguments

    | Parameter                   | Default | Description                             |
    | --------------------------- | ------- | --------------------------------------- |
    | `file_format`               | `mp3`   | Recording format. Values: `mp3`, `wav`. |
    | `recording_callback_url`    |         | URL for recording status events.        |
    | `recording_callback_method` | `POST`  | HTTP method for callbacks.              |

    <Note>
      A supervisor's voice is recorded regardless of `coach_mode` setting.
    </Note>

    <CodeGroup>
      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>', '<auth_token>')
      response = client.multi_party_calls.start_recording(
          friendly_name='mpc_name',
          file_format='mp3',
          recording_callback_url='https://example.com/recording-status'
      )
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
      response = api.multipartycalls.start_recording(friendly_name: 'mpc_name')
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client('<auth_id>', '<auth_token>');
      client.multiPartyCalls.startRecording({
          file_format: 'mp3',
          recordingCallbackUrl: 'https://example.com/recording-status'
      }, 'mpc_name').then(console.log);
      ```

      ```php PHP theme={null}
      <?php
      require 'vendor/autoload.php';
      use Plivo\RestClient;

      $client = new RestClient('<auth_id>', '<auth_token>');
      $response = $client->multiPartyCalls->startRecording(['friendly_name' => 'mpc_name']);
      print_r($response);
      ```

      ```java Java theme={null}
      import com.plivo.api.Plivo;
      import com.plivo.api.models.multipartycall.MultiPartyCall;
      import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

      Plivo.init('<auth_id>', '<auth_token>');
      MultiPartyCall.recordStarter(MultiPartyCallUtils.friendlyName('mpc_name'))
          .fileFormat("mp3")
          .update();
      ```

      ```csharp .NET theme={null}
      using Plivo;

      var api = new PlivoApi('<auth_id>', '<auth_token>');
      var response = api.MultiPartyCall.StartRecording(friendlyName: "mpc_name");
      Console.WriteLine(response);
      ```

      ```go Go theme={null}
      package main

      import "github.com/plivo/plivo-go/v7"

      func main() {
          client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
          response, _ := client.MultiPartyCall.StartRecording(
              plivo.MultiPartyCallBasicParams{FriendlyName: "mpc_name"},
              plivo.MultiPartyCallStartRecordingParams{FileFormat: "mp3"},
          )
      }
      ```

      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN \
          -H "Content-Type: application/json" \
          -d '{"file_format": "mp3"}' \
          https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Record/
      ```
    </CodeGroup>

    #### Response

    ```json  theme={null}
    {
      "api_id": "e05b5263-45dc-11eb-9014-0242ac110003",
      "message": "MPC: test_mpc_1 record started",
      "recording_id": "e06ac332-45dc-11eb-94fe-06dd7f581a50",
      "recording_url": "https://media.plivo.com/v1/Account/MAOTE1OWE0MDK0MTLHYW/Recording/e06ac332-45dc-11eb-94fe-06dd7f581a50.mp3"
    }
    ```
  </Tab>

  <Tab title="Stop Recording">
    Stop MPC recording.

    ```
    DELETE https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Record/
    ```

    <CodeGroup>
      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>', '<auth_token>')
      response = client.multi_party_calls.stop_recording(friendly_name='mpc_name')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
      response = api.multipartycalls.stop_recording(friendly_name: 'mpc_name')
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client('<auth_id>', '<auth_token>');
      client.multiPartyCalls.stopRecording('mpc_name').then(console.log);
      ```

      ```php PHP theme={null}
      <?php
      require 'vendor/autoload.php';
      use Plivo\RestClient;

      $client = new RestClient('<auth_id>', '<auth_token>');
      $response = $client->multiPartyCalls->stopRecording(['friendly_name' => 'mpc_name']);
      print_r($response);
      ```

      ```java Java theme={null}
      import com.plivo.api.Plivo;
      import com.plivo.api.models.multipartycall.MultiPartyCall;
      import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

      Plivo.init('<auth_id>', '<auth_token>');
      MultiPartyCall.recordStopper(MultiPartyCallUtils.friendlyName('mpc_name')).delete();
      ```

      ```csharp .NET theme={null}
      using Plivo;

      var api = new PlivoApi('<auth_id>', '<auth_token>');
      var response = api.MultiPartyCall.StopRecording(friendlyName: "mpc_name");
      Console.WriteLine(response);
      ```

      ```go Go theme={null}
      package main

      import "github.com/plivo/plivo-go/v7"

      func main() {
          client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
          client.MultiPartyCall.StopRecording(plivo.MultiPartyCallBasicParams{FriendlyName: "mpc_name"})
      }
      ```

      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN -X DELETE \
          https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Record/
      ```
    </CodeGroup>

    #### Response

    ```
    HTTP Status Code: 204
    ```
  </Tab>

  <Tab title="Pause Recording">
    Pause ongoing MPC recording.

    ```
    POST https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Record/Pause/
    ```

    <CodeGroup>
      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>', '<auth_token>')
      response = client.multi_party_calls.pause_recording(friendly_name='mpc_name')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
      response = api.multipartycalls.pause_recording(friendly_name: 'mpc_name')
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client('<auth_id>', '<auth_token>');
      client.multiPartyCalls.pauseRecording('mpc_name').then(console.log);
      ```

      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN -X POST \
          https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Record/Pause/
      ```
    </CodeGroup>

    #### Response

    ```
    HTTP Status Code: 204
    ```
  </Tab>

  <Tab title="Resume Recording">
    Resume paused MPC recording.

    ```
    POST https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Record/Resume/
    ```

    <CodeGroup>
      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>', '<auth_token>')
      response = client.multi_party_calls.resume_recording(friendly_name='mpc_name')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
      response = api.multipartycalls.resume_recording(friendly_name: 'mpc_name')
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client('<auth_id>', '<auth_token>');
      client.multiPartyCalls.resumeRecording('mpc_name').then(console.log);
      ```

      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN -X POST \
          https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Record/Resume/
      ```
    </CodeGroup>

    #### Response

    ```
    HTTP Status Code: 204
    ```
  </Tab>
</Tabs>

### Recording Callback Events

Events sent to `recording_callback_url`:

* `MPCRecordingInitiated`
* `MPCRecordingPaused`
* `MPCRecordingResumed`
* `MPCRecordingCompleted`
* `MPCRecordingFailed`

<Accordion title="Callback Parameters">
  | Parameter            | Description                    |
  | -------------------- | ------------------------------ |
  | `EventName`          | The recording event type.      |
  | `EventTimestamp`     | When the event occurred.       |
  | `MPCName`            | Name of the MPC.               |
  | `MPCUUID`            | UUID of the MPC.               |
  | `RecordingDuration`  | Duration in seconds.           |
  | `RecordingFormat`    | File format (mp3/wav).         |
  | `RecordingURL`       | URL to download the recording. |
  | `RecordingUUID`      | Unique recording identifier.   |
  | `RecordingStartTime` | When recording started.        |
  | `RecordingEndTime`   | When recording ended.          |
  | `SequenceNumber`     | Event sequence number.         |
</Accordion>

***

## Record a Participant

Record a specific participant's audio.

<Tabs>
  <Tab title="Start Recording">
    ```
    POST https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/{mpc_name}/Participant/{member_id}/Record/
    ```

    ### Arguments

    | Parameter                   | Default | Description                                                                      |
    | --------------------------- | ------- | -------------------------------------------------------------------------------- |
    | `file_format`               | `mp3`   | Recording format. Values: `mp3`, `wav`.                                          |
    | `recording_callback_url`    |         | URL for recording status events.                                                 |
    | `recording_callback_method` | `POST`  | HTTP method for callbacks.                                                       |
    | `record_track_type`         | `all`   | Track type. Values: `participant` (single-track), `all` (multi-channel), `both`. |

    <CodeGroup>
      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>', '<auth_token>')
      response = client.multi_party_calls.start_participant_recording(
          participant_id='355',
          friendly_name='mpc_name',
          file_format='mp3'
      )
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
      response = api.multipartycalls.start_participant_recording(
        friendly_name: 'mpc_name',
        member_id: '355'
      )
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client('<auth_id>', '<auth_token>');
      client.multiPartyCalls.startParticipantRecording('355', null, 'mpc_name', {
          file_format: 'mp3'
      }).then(console.log);
      ```

      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN \
          -H "Content-Type: application/json" \
          -d '{"file_format": "mp3"}' \
          https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/{member_id}/Record/
      ```
    </CodeGroup>
  </Tab>

  <Tab title="Stop Recording">
    ```
    DELETE https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/{mpc_name}/Participant/{member_id}/Record/
    ```

    | Parameter           | Default | Description                                                    |
    | ------------------- | ------- | -------------------------------------------------------------- |
    | `record_track_type` | `all`   | Which recording to stop. Values: `participant`, `all`, `both`. |

    <CodeGroup>
      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>', '<auth_token>')
      response = client.multi_party_calls.stop_participant_recording(
          participant_id='355',
          friendly_name='mpc_name'
      )
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
      response = api.multipartycalls.stop_participant_recording(
        friendly_name: 'mpc_name',
        member_id: '355'
      )
      puts response
      ```

      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN -X DELETE \
          https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Participant/{member_id}/Record/
      ```
    </CodeGroup>
  </Tab>
</Tabs>

***

## Play Audio to Participant

<Tabs>
  <Tab title="Start Playing">
    Play an audio file to specific participants.

    ```
    POST https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Member/{member_id}/Play/
    ```

    The `{member_id}` can be a specific ID, comma-separated list, or `all`.

    ### Arguments

    | Parameter | Description                                     |
    | --------- | ----------------------------------------------- |
    | `urls`    | Required. URL of the audio file (.mp3 or .wav). |

    <CodeGroup>
      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>', '<auth_token>')
      response = client.multi_party_calls.start_play_audio(
          participant_id='355',
          friendly_name='mpc_name',
          url='https://example.com/audio.mp3'
      )
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
      response = api.multipartycalls.start_play_audio(
        friendly_name: 'mpc_name',
        member_id: '355',
        url: 'https://example.com/audio.mp3'
      )
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client('<auth_id>', '<auth_token>');
      client.multiPartyCalls.startPlayAudio('355', {
          friendlyName: 'mpc_name',
          url: 'https://example.com/audio.mp3'
      }).then(console.log);
      ```

      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN \
          -H "Content-Type: application/json" \
          -d '{"urls": "https://example.com/audio.mp3"}' \
          https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Member/{member_id}/Play/
      ```
    </CodeGroup>

    #### Response

    ```json  theme={null}
    {
      "api_id": "e05b5263-45dc-11eb-9014-0242ac110003",
      "message": "play queued into MPC",
      "mpcMemberId": ["355"],
      "mpcName": "test_mpc_1"
    }
    ```
  </Tab>

  <Tab title="Stop Playing">
    Stop playing audio to participants.

    ```
    DELETE https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Member/{member_id}/Play/
    ```

    <Note>
      Use the same `member_id` format you used to start playing. If you started with a specific ID, stopping with `all` won't work.
    </Note>

    <CodeGroup>
      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>', '<auth_token>')
      response = client.multi_party_calls.stop_play_audio(
          participant_id='355',
          friendly_name='mpc_name'
      )
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new('<auth_id>', '<auth_token>')
      response = api.multipartycalls.stop_play_audio(
        friendly_name: 'mpc_name',
        member_id: '355'
      )
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client('<auth_id>', '<auth_token>');
      client.multiPartyCalls.stopPlayAudio('355', {friendlyName: 'mpc_name'}).then(console.log);
      ```

      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN -X DELETE \
          https://api.plivo.com/v1/Account/{auth_id}/MultiPartyCall/name_{mpc_name}/Member/{member_id}/Play/
      ```
    </CodeGroup>

    #### Response

    ```
    HTTP Status Code: 204
    ```
  </Tab>
</Tabs>

***

## Related

* [MultiPartyCall XML Element](/voice/xml/multipartycall/) - Add participants using XML
* [Conference API](/voice/api/conferences/) - Standard conference calls
* [Recordings API](/voice/api/recordings/) - Manage call recordings
* [Hangup Causes](/voice/troubleshooting/hangup-causes/) - Termination cause codes
