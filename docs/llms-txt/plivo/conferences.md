# Source: https://plivo.com/docs/voice/api/conferences.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Conferences

> Create and manage audio conferences with multiple participants

Conferences let you connect multiple participants in a single call. Using the Conference API, you can manage ongoing conferences, control individual members, and record conversations.

Conferences are suited for traditional "meeting" use cases. For advanced contact center or sales dialer scenarios requiring more control, consider [Multiparty Calls](/voice/api/multiparty-calls/).

## The Conference Object

<ParamField body="conference_name" type="string">
  Name used to identify the conference.
</ParamField>

<ParamField body="conference_run_time" type="string">
  Time in seconds since the conference was initiated.
</ParamField>

<ParamField body="conference_member_count" type="string">
  Number of members currently active in the conference.
</ParamField>

<ParamField body="members" type="array">
  Array of member objects in the conference.
</ParamField>

### Member Attributes

Each member in the `members` array has the following attributes:

<ParamField body="member_id" type="string">
  Unique ID of the member within the conference.
</ParamField>

<ParamField body="muted" type="boolean">
  `true` if the member is currently muted.
</ParamField>

<ParamField body="deaf" type="boolean">
  `true` if the member cannot hear conference audio.
</ParamField>

<ParamField body="from" type="string">
  Source of the call — PSTN number or SIP endpoint.
</ParamField>

<ParamField body="to" type="string">
  Conference bridge number — Plivo number or application URL.
</ParamField>

<ParamField body="caller_name" type="string">
  Name of the caller (SIP calls only).
</ParamField>

<ParamField body="direction" type="string">
  Direction of the call — `inbound` or `outbound`.
</ParamField>

<ParamField body="call_uuid" type="string">
  Unique identifier of the call.
</ParamField>

<ParamField body="join_time" type="string">
  Time in seconds since the member joined.
</ParamField>

### Example Conference Object

```json  theme={null}
{
  "conference_name": "My Conf Room",
  "conference_run_time": "590",
  "conference_member_count": "1",
  "members": [
    {
      "muted": false,
      "member_id": "17",
      "deaf": false,
      "from": "1456789903",
      "to": "1677889900",
      "caller_name": "John",
      "direction": "inbound",
      "call_uuid": "acfbf0b5-12e0-4d74-85f7-fce15f8f07ec",
      "join_time": "590"
    }
  ]
}
```

***

## Retrieve a Conference

Get details of a specific conference by name.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/
```

### Arguments

No arguments required.

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.conferences.get(conference_name='My Conf Room')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.conferences.get('My Conf Room')
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.conferences.get("My Conf Room").then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->conferences->get('My Conf Room');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.conference.Conference;

  Plivo.init("<auth_id>","<auth_token>");
  Conference response = Conference.getter("My Conf Room").get();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Conference.Get(conferenceName: "My Conf Room");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.Conferences.Get("My Conf Room")
  }
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "conference_name": "My Conf Room",
  "conference_run_time": "590",
  "conference_member_count": "1",
  "members": [
    {
      "muted": false,
      "member_id": "17",
      "deaf": false,
      "from": "1456789903",
      "to": "1677889900",
      "caller_name": "John",
      "direction": "inbound",
      "call_uuid": "acfbf0b5-12e0-4d74-85f7-fce15f8f07ec",
      "join_time": "590"
    }
  ],
  "api_id": "816e903e-58c4-11e1-86da-adf28403fe48"
}
```

***

## List All Conferences

Retrieve names of all ongoing conferences in your account.

```
GET https://api.plivo.com/v1/Account/{auth_id}/Conference/
```

### Arguments

No arguments required.

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Conference/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.conferences.list()
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.conferences.list
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.conferences.list().then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->conferences->list();
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.conference.Conference;

  Plivo.init("<auth_id>","<auth_token>");
  ListResponse<Conference> response = Conference.lister().list();
  System.out.println(response);
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Conference.List();
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      response, _ := client.Conferences.List(plivo.ConferenceListParams{})
  }
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48",
  "conferences": [
    "My Conf Room",
    "Sales Meeting",
    "Support Call"
  ]
}
```

***

## Hang Up a Conference

Terminate a conference and disconnect all members.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/
```

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.conferences.delete(conference_name='My Conf Room')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.conferences.delete('My Conf Room')
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.conferences.hangup("My Conf Room").then(console.log);
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\RestClient;

  $client = new RestClient("<auth_id>","<auth_token>");
  $response = $client->conferences->delete('My Conf Room');
  print_r($response);
  ```

  ```java Java theme={null}
  import com.plivo.api.Plivo;
  import com.plivo.api.models.conference.Conference;

  Plivo.init("<auth_id>","<auth_token>");
  Conference.deleter("My Conf Room").delete();
  ```

  ```csharp .NET theme={null}
  using Plivo;

  var api = new PlivoApi("<auth_id>","<auth_token>");
  var response = api.Conference.Delete(conferenceName: "My Conf Room");
  Console.WriteLine(response);
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7"

  func main() {
      client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
      client.Conferences.Delete("My Conf Room")
  }
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "message": "conference hung up",
  "api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48"
}
```

***

## Hang Up All Conferences

Terminate all ongoing conferences in your account.

```
DELETE https://api.plivo.com/v1/Account/{auth_id}/Conference/
```

<CodeGroup>
  ```bash cURL theme={null}
  curl -X DELETE --user AUTH_ID:AUTH_TOKEN \
      https://api.plivo.com/v1/Account/{auth_id}/Conference/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.conferences.delete_all()
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.conferences.delete_all
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.conferences.hangupAll().then(console.log);
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "message": "all conferences hung up",
  "api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48"
}
```

***

## Member Operations

Control individual members within a conference. The `member_id` parameter can be:

* A specific member ID (e.g., `10`)
* A comma-separated list (e.g., `10,11,12`)
* The string `all` to affect all members

### Kick a Member

Disconnect a member from the conference.

```
POST https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Kick/
```

<CodeGroup>
  ```bash cURL theme={null}
  curl -i --user AUTH_ID:AUTH_TOKEN \
      -H "Content-Type: application/json" \
      -d '{}' \
      https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Kick/
  ```

  ```python Python theme={null}
  import plivo

  client = plivo.RestClient('<auth_id>','<auth_token>')
  response = client.conferences.member_kick(conference_name='My Conf Room', member_id='10')
  print(response)
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  api = Plivo::RestClient.new("<auth_id>","<auth_token>")
  response = api.conferences.kick_member('My Conf Room', [10])
  puts response
  ```

  ```javascript Node theme={null}
  const plivo = require('plivo');

  const client = new plivo.Client("<auth_id>","<auth_token>");
  client.conferences.kickMember("My Conf Room", 10).then(console.log);
  ```
</CodeGroup>

### Response

```json  theme={null}
{
  "message": "kicked",
  "member_id": "10",
  "api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48"
}
```

### Mute / Unmute a Member

<Tabs>
  <Tab title="Mute">
    Mute a member so other participants cannot hear them.

    ```
    POST https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Mute/
    ```

    <CodeGroup>
      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN \
          -H "Content-Type: application/json" \
          -d '{}' \
          https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Mute/
      ```

      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.conferences.member_mute(conference_name='My Conf Room', member_id='10')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new("<auth_id>","<auth_token>")
      response = api.conferences.mute_member('My Conf Room', [10])
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client("<auth_id>","<auth_token>");
      client.conferences.muteMember("My Conf Room", 10).then(console.log);
      ```
    </CodeGroup>

    #### Response

    ```json  theme={null}
    {
      "message": "muted",
      "member_id": "10",
      "api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48"
    }
    ```
  </Tab>

  <Tab title="Unmute">
    Unmute a previously muted member.

    ```
    DELETE https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Mute/
    ```

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X DELETE --user AUTH_ID:AUTH_TOKEN \
          https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Mute/
      ```

      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.conferences.member_unmute(conference_name='My Conf Room', member_id='10')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new("<auth_id>","<auth_token>")
      response = api.conferences.unmute_member('My Conf Room', [10])
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client("<auth_id>","<auth_token>");
      client.conferences.unmuteMember("My Conf Room", 10).then(console.log);
      ```
    </CodeGroup>

    #### Response

    ```json  theme={null}
    {
      "message": "unmuted",
      "member_id": "10",
      "api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48"
    }
    ```
  </Tab>
</Tabs>

### Deaf / Undeaf a Member

<Tabs>
  <Tab title="Deaf">
    Make a member deaf so they cannot hear conference audio.

    ```
    POST https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Deaf/
    ```

    <CodeGroup>
      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN \
          -H "Content-Type: application/json" \
          -d '{}' \
          https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Deaf/
      ```

      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.conferences.member_deaf(conference_name='My Conf Room', member_id='10')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new("<auth_id>","<auth_token>")
      response = api.conferences.deaf_member('My Conf Room', [10])
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client("<auth_id>","<auth_token>");
      client.conferences.deafMember("My Conf Room", 10).then(console.log);
      ```
    </CodeGroup>

    #### Response

    ```json  theme={null}
    {
      "message": "deaf",
      "member_id": "10",
      "api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48"
    }
    ```
  </Tab>

  <Tab title="Undeaf">
    Restore hearing to a deaf member.

    ```
    DELETE https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Deaf/
    ```

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X DELETE --user AUTH_ID:AUTH_TOKEN \
          https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Deaf/
      ```

      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.conferences.member_undeaf(conference_name='My Conf Room', member_id='10')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new("<auth_id>","<auth_token>")
      response = api.conferences.enable_hearing_member('My Conf Room', [10])
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client("<auth_id>","<auth_token>");
      client.conferences.undeafMember("My Conf Room", 10).then(console.log);
      ```
    </CodeGroup>

    #### Response

    ```json  theme={null}
    {
      "message": "undeaf",
      "member_id": "10",
      "api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48"
    }
    ```
  </Tab>
</Tabs>

### Play Audio to a Member

<Tabs>
  <Tab title="Start Playing">
    Play an audio file to specific members.

    ```
    POST https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Play/
    ```

    | Parameter | Required | Description                               |
    | --------- | -------- | ----------------------------------------- |
    | `url`     | Yes      | URL of the `.mp3` or `.wav` file to play. |

    <CodeGroup>
      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN \
          -H "Content-Type: application/json" \
          -d '{"url":"https://s3.amazonaws.com/plivocloud/music.mp3"}' \
          https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Play/
      ```

      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.conferences.member_play(
          conference_name='My Conf Room',
          member_id='10',
          url='https://s3.amazonaws.com/plivocloud/music.mp3')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new("<auth_id>","<auth_token>")
      response = api.conferences.play_member(
          'My Conf Room',
          [10],
          'https://s3.amazonaws.com/plivocloud/music.mp3')
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client("<auth_id>","<auth_token>");
      client.conferences.playAudioToMember(
          "My Conf Room",
          10,
          "https://s3.amazonaws.com/plivocloud/music.mp3"
      ).then(console.log);
      ```
    </CodeGroup>

    #### Response

    ```json  theme={null}
    {
      "message": "play queued into conference",
      "api_id": "4e44bd4e-f830-11e6-b886-067c5485c240",
      "member_id": "10"
    }
    ```
  </Tab>

  <Tab title="Stop Playing">
    Stop playing audio to members.

    ```
    DELETE https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Play/
    ```

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X DELETE --user AUTH_ID:AUTH_TOKEN \
          https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Play/
      ```

      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.conferences.member_play_stop(conference_name='My Conf Room', member_id='10')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new("<auth_id>","<auth_token>")
      response = api.conferences.stop_play_member('My Conf Room', [10])
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client("<auth_id>","<auth_token>");
      client.conferences.stopPlayingAudioToMember("My Conf Room", 10).then(console.log);
      ```
    </CodeGroup>
  </Tab>
</Tabs>

### Speak Text to a Member

<Tabs>
  <Tab title="Start Speaking">
    Speak text to specific members using text-to-speech.

    ```
    POST https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Speak/
    ```

    | Parameter  | Required | Description                                           |
    | ---------- | -------- | ----------------------------------------------------- |
    | `text`     | Yes      | Text to speak.                                        |
    | `voice`    | No       | Voice type. Values: `MAN`, `WOMAN`. Default: `WOMAN`. |
    | `language` | No       | Language code. Default: `en-US`.                      |

    <CodeGroup>
      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN \
          -H "Content-Type: application/json" \
          -d '{"text":"Hello, welcome to the conference"}' \
          https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Speak/
      ```

      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.conferences.member_speak(
          conference_name='My Conf Room',
          member_id='10',
          text='Hello, welcome to the conference')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new("<auth_id>","<auth_token>")
      response = api.conferences.speak_member(
          'My Conf Room',
          [10],
          'Hello, welcome to the conference')
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client("<auth_id>","<auth_token>");
      client.conferences.speakTextToMember(
          "My Conf Room",
          10,
          "Hello, welcome to the conference"
      ).then(console.log);
      ```
    </CodeGroup>

    #### Response

    ```json  theme={null}
    {
      "message": "speak queued into conference",
      "api_id": "4e44bd4e-f830-11e6-b886-067c5485c240",
      "member_id": "10"
    }
    ```
  </Tab>

  <Tab title="Stop Speaking">
    Stop speaking text to members.

    ```
    DELETE https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Speak/
    ```

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X DELETE --user AUTH_ID:AUTH_TOKEN \
          https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Member/{member_id}/Speak/
      ```

      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.conferences.member_speak_stop(conference_name='My Conf Room', member_id='10')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new("<auth_id>","<auth_token>")
      response = api.conferences.stop_speak_member('My Conf Room', [10])
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client("<auth_id>","<auth_token>");
      client.conferences.stopSpeakingTextToMember("My Conf Room", 10).then(console.log);
      ```
    </CodeGroup>
  </Tab>
</Tabs>

***

## Record a Conference

<Tabs>
  <Tab title="Start Recording">
    Start recording an ongoing conference.

    ```
    POST https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Record/
    ```

    ### Arguments

    | Parameter            | Description                                             |
    | -------------------- | ------------------------------------------------------- |
    | `file_format`        | Recording format. Values: `mp3`, `wav`. Default: `mp3`. |
    | `transcription_type` | Set to `auto` for automated transcription.              |
    | `transcription_url`  | URL to receive transcription results.                   |
    | `callback_url`       | URL invoked when recording ends.                        |
    | `callback_method`    | HTTP verb for `callback_url`. Default: `POST`.          |

    <Accordion title="Callback URL parameters">
      | Parameter               | Description                                  |
      | ----------------------- | -------------------------------------------- |
      | `api_id`                | API ID returned by the record API.           |
      | `record_url`            | URL where the recorded file can be accessed. |
      | `recording_id`          | Recording ID associated with the file.       |
      | `conference_name`       | Name of the recorded conference.             |
      | `recording_duration`    | Duration in seconds.                         |
      | `recording_duration_ms` | Duration in milliseconds.                    |
      | `recording_start_ms`    | Start time (epoch ms).                       |
      | `recording_end_ms`      | End time (epoch ms).                         |
    </Accordion>

    <CodeGroup>
      ```bash cURL theme={null}
      curl -i --user AUTH_ID:AUTH_TOKEN \
          -H "Content-Type: application/json" \
          -d '{"file_format":"mp3"}' \
          https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Record/
      ```

      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.conferences.record(conference_name='My Conf Room')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new("<auth_id>","<auth_token>")
      response = api.conferences.record('My Conf Room')
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client("<auth_id>","<auth_token>");
      client.conferences.record("My Conf Room").then(console.log);
      ```

      ```php PHP theme={null}
      <?php
      require 'vendor/autoload.php';
      use Plivo\RestClient;

      $client = new RestClient("<auth_id>","<auth_token>");
      $response = $client->conferences->startRecording('My Conf Room');
      print_r($response);
      ```

      ```java Java theme={null}
      import com.plivo.api.Plivo;
      import com.plivo.api.models.conference.Conference;

      Plivo.init("<auth_id>","<auth_token>");
      ConferenceRecordCreateResponse response = Conference.recorder("My Conf Room").record();
      System.out.println(response);
      ```

      ```csharp .NET theme={null}
      using Plivo;

      var api = new PlivoApi("<auth_id>","<auth_token>");
      var response = api.Conference.StartRecording("My Conf Room");
      Console.WriteLine(response);
      ```

      ```go Go theme={null}
      package main

      import "github.com/plivo/plivo-go/v7"

      func main() {
          client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
          response, _ := client.Conferences.Record("My Conf Room", plivo.ConferenceRecordParams{})
      }
      ```
    </CodeGroup>

    #### Response

    ```json  theme={null}
    {
      "api_id": "2867b6e2-58c3-11e1-86da-adf28403fe48",
      "message": "conference recording started",
      "recording_id": "93bc7c6a-3b2b-11e3",
      "url": "https://media.plivo.com/v1/Account/<Auth_ID>/Recording/93bc7c6a-3b2b-11e3.mp3"
    }
    ```
  </Tab>

  <Tab title="Stop Recording">
    Stop recording a conference.

    ```
    DELETE https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Record/
    ```

    <CodeGroup>
      ```bash cURL theme={null}
      curl -X DELETE --user AUTH_ID:AUTH_TOKEN \
          https://api.plivo.com/v1/Account/{auth_id}/Conference/{conference_name}/Record/
      ```

      ```python Python theme={null}
      import plivo

      client = plivo.RestClient('<auth_id>','<auth_token>')
      response = client.conferences.record_stop(conference_name='My Conf Room')
      print(response)
      ```

      ```ruby Ruby theme={null}
      require 'plivo'

      api = Plivo::RestClient.new("<auth_id>","<auth_token>")
      response = api.conferences.stop_record('My Conf Room')
      puts response
      ```

      ```javascript Node theme={null}
      const plivo = require('plivo');

      const client = new plivo.Client("<auth_id>","<auth_token>");
      client.conferences.stopRecording("My Conf Room").then(console.log);
      ```

      ```php PHP theme={null}
      <?php
      require 'vendor/autoload.php';
      use Plivo\RestClient;

      $client = new RestClient("<auth_id>","<auth_token>");
      $response = $client->conferences->stopRecording('My Conf Room');
      print_r($response);
      ```

      ```java Java theme={null}
      import com.plivo.api.Plivo;
      import com.plivo.api.models.conference.Conference;

      Plivo.init("<auth_id>","<auth_token>");
      Conference.recordStopper("My Conf Room").stop();
      ```

      ```csharp .NET theme={null}
      using Plivo;

      var api = new PlivoApi("<auth_id>","<auth_token>");
      var response = api.Conference.StopRecording("My Conf Room");
      Console.WriteLine(response);
      ```

      ```go Go theme={null}
      package main

      import "github.com/plivo/plivo-go/v7"

      func main() {
          client, _ := plivo.NewClient("<auth_id>", "<auth_token>", &plivo.ClientOptions{})
          client.Conferences.RecordStop("My Conf Room")
      }
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

* [Conference XML Element](/voice/xml/conferencing) - Create conferences using XML
* [Multiparty Calls](/voice/api/multiparty-calls/) - Advanced call control for contact centers
* [Recordings](/voice/api/recordings/) - Manage conference recordings
