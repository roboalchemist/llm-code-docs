# Source: https://plivo.com/docs/voice/xml/conferencing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Conferencing

> Create conference calls and multi-party calls with moderation and recording

This page covers the XML elements for conferencing: connecting multiple callers together with features like moderation, recording, and coaching.

***

## Conference

The `<Conference>` element connects a caller to a conference room. Multiple callers joining the same conference name are connected together. Maximum participants per conference: 20.

### Basic Usage

```xml  theme={null}
<Response>
    <Conference>my-conference-room</Conference>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.ConferenceElement('my-conference-room'))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addConference('my-conference-room');
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addConference('my-conference-room')
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addConference('my-conference-room');
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;

  Response response = new Response()
      .children(new Conference("my-conference-room"));
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  response.AddConference("my-conference-room");
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.ConferenceElement).SetContents("my-conference-room"),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### Conference Attributes

#### Basic Settings

| Attribute      | Type    | Default | Description                                |
| -------------- | ------- | ------- | ------------------------------------------ |
| `muted`        | boolean | `false` | Join muted (can still hear others)         |
| `enterSound`   | string  | `""`    | Sound on entry: `beep:1`, `beep:2`, or URL |
| `exitSound`    | string  | `""`    | Sound on exit: `beep:1`, `beep:2`, or URL  |
| `maxMembers`   | integer | `20`    | Maximum participants (1-20)                |
| `timeLimit`    | integer | `86400` | Max conference duration in seconds         |
| `hangupOnStar` | boolean | `false` | Let member exit by pressing \*             |
| `stayAlone`    | boolean | `true`  | End conference if only one member          |

#### Moderation

| Attribute                | Type    | Default | Description                                         |
| ------------------------ | ------- | ------- | --------------------------------------------------- |
| `startConferenceOnEnter` | boolean | `true`  | Start conference when this member joins             |
| `endConferenceOnExit`    | boolean | `false` | End conference when this member leaves              |
| `waitSound`              | URL     | -       | Audio to play while waiting for conference to start |

#### Recording

| Attribute           | Type    | Default | Description                     |
| ------------------- | ------- | ------- | ------------------------------- |
| `record`            | boolean | `false` | Record the conference           |
| `recordFileFormat`  | string  | `mp3`   | Recording format (`mp3`, `wav`) |
| `transcriptionType` | string  | -       | Set to `auto` for transcription |
| `transcriptionUrl`  | URL     | -       | URL to receive transcription    |

#### Callbacks

| Attribute        | Type    | Default | Description                   |
| ---------------- | ------- | ------- | ----------------------------- |
| `action`         | URL     | -       | URL called when member leaves |
| `method`         | string  | `POST`  | HTTP method for action        |
| `callbackUrl`    | URL     | -       | URL for conference events     |
| `callbackMethod` | string  | `POST`  | HTTP method for callback      |
| `redirect`       | boolean | `true`  | Redirect to action URL        |

#### DTMF

| Attribute     | Type    | Default | Description                             |
| ------------- | ------- | ------- | --------------------------------------- |
| `digitsMatch` | string  | -       | DTMF patterns to report                 |
| `floorEvent`  | boolean | `false` | Notify when member becomes floor-holder |
| `relayDTMF`   | boolean | `true`  | Transmit DTMF to all members            |

### Join Muted

Add participants who can listen but not speak:

```xml  theme={null}
<Response>
    <Conference muted="true">my-conference-room</Conference>
</Response>
```

### Entry/Exit Sounds

Play beeps when participants join or leave:

```xml  theme={null}
<Response>
    <Conference enterSound="beep:1" exitSound="beep:2">
        my-conference-room
    </Conference>
</Response>
```

Use a URL to play custom audio:

```xml  theme={null}
<Response>
    <Conference enterSound="https://example.com/join-sound.xml">
        my-conference-room
    </Conference>
</Response>
```

The URL must return XML with `Play`, `Speak`, or `Wait` elements.

### Moderated Conference

Create a "waiting room" where participants wait for the moderator:

**Participant XML:**

```xml  theme={null}
<Response>
    <Conference startConferenceOnEnter="false" waitSound="https://example.com/hold-music.xml">
        moderated-meeting
    </Conference>
</Response>
```

**Moderator XML:**

```xml  theme={null}
<Response>
    <Conference startConferenceOnEnter="true" endConferenceOnExit="true">
        moderated-meeting
    </Conference>
</Response>
```

When the moderator joins, the conference starts. When they leave, everyone is disconnected.

### Record Conference

```xml  theme={null}
<Response>
    <Conference record="true" recordFileFormat="mp3"
                callbackUrl="https://example.com/recording-ready/">
        recorded-meeting
    </Conference>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.ConferenceElement(
      'recorded-meeting',
      record=True,
      record_file_format='mp3',
      callback_url='https://example.com/recording-ready/'
  ))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addConference('recorded-meeting', {
      record: true,
      recordFileFormat: 'mp3',
      callbackUrl: 'https://example.com/recording-ready/'
  });
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  response = Plivo::XML::Response.new
  response.addConference('recorded-meeting',
      record: true,
      recordFileFormat: 'mp3',
      callbackUrl: 'https://example.com/recording-ready/'
  )
  puts Plivo::XML::PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addConference('recorded-meeting', [
      'record' => true,
      'recordFileFormat' => 'mp3',
      'callbackUrl' => 'https://example.com/recording-ready/'
  ]);
  echo $response->toXML();
  ```
</CodeGroup>

### With Transcription

```xml  theme={null}
<Response>
    <Conference record="true"
                transcriptionType="auto"
                transcriptionUrl="https://example.com/transcription/">
        transcribed-meeting
    </Conference>
</Response>
```

### Exit with Action URL

```xml  theme={null}
<Response>
    <Conference action="https://example.com/conference-ended/"
                hangupOnStar="true">
        my-conference
    </Conference>
</Response>
```

### Conference Action URL Parameters

Sent when a member leaves the conference:

| Parameter            | Description                   |
| -------------------- | ----------------------------- |
| `ConferenceName`     | Name of the conference        |
| `ConferenceUUID`     | Unique conference identifier  |
| `ConferenceMemberID` | Member's ID in the conference |
| `RecordUrl`          | Recording URL (if recorded)   |
| `RecordingID`        | Recording identifier          |

### Conference Callback URL Parameters

Sent for conference events:

| Parameter               | Description                                     |
| ----------------------- | ----------------------------------------------- |
| `ConferenceAction`      | `enter`, `exit`, `digits`, `floor`, `record`    |
| `ConferenceName`        | Conference name                                 |
| `ConferenceUUID`        | Conference identifier                           |
| `ConferenceMemberID`    | Member ID                                       |
| `CallUUID`              | Call identifier                                 |
| `ConferenceDigitsMatch` | Matched digits (when `ConferenceAction=digits`) |
| `RecordUrl`             | Recording URL (when `ConferenceAction=record`)  |
| `RecordingID`           | Recording ID                                    |
| `RecordingDuration`     | Duration in seconds                             |
| `RecordingDurationMs`   | Duration in milliseconds                        |
| `RecordingStartMs`      | Start time (epoch ms)                           |
| `RecordingEndMs`        | End time (epoch ms)                             |

### Transcription URL Parameters

| Parameter              | Description            |
| ---------------------- | ---------------------- |
| `transcription`        | Transcribed text       |
| `transcription_charge` | Cost of transcription  |
| `transcription_rate`   | Rate per minute        |
| `duration`             | Recording duration     |
| `call_uuid`            | Call identifier        |
| `recording_id`         | Recording identifier   |
| `error`                | Error message (if any) |

### Bridge Two Callers

Use conferences to connect two incoming callers:

**First Caller:**

```xml  theme={null}
<Response>
    <Conference waitSound="https://example.com/hold.xml">
        private-bridge-123
    </Conference>
</Response>
```

**Second Caller:**

```xml  theme={null}
<Response>
    <Conference>private-bridge-123</Conference>
</Response>
```

***

## MultiPartyCall

The `<MultiPartyCall>` element creates or joins a multi-party call (MPC) with advanced features like participant roles, coach mode for supervisors, and individual hold/mute controls.

### Basic Usage

```xml  theme={null}
<Response>
    <MultiPartyCall role="customer" maxDuration="10000">
        my-mpc-name
    </MultiPartyCall>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.MultiPartyCallElement(
      content='my-mpc-name',
      role='customer',
      max_duration=10000
  ))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addMultiPartyCall('my-mpc-name', {
      role: 'customer',
      maxDuration: 10000
  });
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  response = Plivo::XML::Response.new
  response.addMultiPartyCall('my-mpc-name',
      role: 'Agent',
      maxDuration: 10000)
  puts Plivo::XML::PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addMultiPartyCall('my-mpc-name', [
      'role' => 'Customer',
      'maxDuration' => 10000
  ]);
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;
  import com.plivo.api.models.multipartycall.MultiPartyCallUtils;

  Response response = new Response();
  response.children(new MultiPartyCall("my-mpc-name", MultiPartyCallUtils.customer)
      .maxDuration(10000));
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  response.AddMultiPartyCall("my-mpc-name", new Dictionary<string, string>() {
      {"role", "customer"},
      {"maxDuration", "10000"}
  });
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.MultiPartyCallElement).
                  SetRole("customer").
                  SetMaxDuration(10000).
                  SetContents("my-mpc-name"),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### Participant Roles

| Role         | Description                           |
| ------------ | ------------------------------------- |
| `Customer`   | The customer being served             |
| `Agent`      | Customer service representative       |
| `Supervisor` | Can monitor/coach agents (coach mode) |

### MPC-Level Attributes

These settings apply to the entire multi-party call:

| Attribute              | Type    | Default | Description                             |
| ---------------------- | ------- | ------- | --------------------------------------- |
| `maxDuration`          | integer | `14400` | Max MPC duration in seconds (300-28800) |
| `maxParticipants`      | integer | `10`    | Maximum participants (2-10)             |
| `record`               | boolean | `false` | Record the MPC                          |
| `recordFileFormat`     | string  | `mp3`   | Recording format (`mp3`, `wav`)         |
| `recordMinMemberCount` | integer | `1`     | Min members to start recording (1 or 2) |

#### Hold Music

| Attribute                 | Type   | Description                                     |
| ------------------------- | ------ | ----------------------------------------------- |
| `waitMusicUrl`            | URL    | Music for participants waiting for MPC to start |
| `waitMusicMethod`         | string | HTTP method for waitMusicUrl                    |
| `agentHoldMusicUrl`       | URL    | Music for agents on hold                        |
| `agentHoldMusicMethod`    | string | HTTP method for agent hold music                |
| `customerHoldMusicUrl`    | URL    | Music for customers on hold                     |
| `customerHoldMusicMethod` | string | HTTP method for customer hold music             |

#### Callbacks

| Attribute                 | Type   | Description                        |
| ------------------------- | ------ | ---------------------------------- |
| `statusCallbackUrl`       | URL    | URL for MPC events                 |
| `statusCallbackMethod`    | string | HTTP method (`GET`, `POST`)        |
| `statusCallbackEvents`    | string | Events to receive (see below)      |
| `recordingCallbackUrl`    | URL    | URL for recording events           |
| `recordingCallbackMethod` | string | HTTP method for recording callback |

### Participant-Level Attributes

These settings apply to individual participants:

| Attribute         | Type    | Default    | Description                              |
| ----------------- | ------- | ---------- | ---------------------------------------- |
| `role`            | string  | *required* | `Agent`, `Supervisor`, or `Customer`     |
| `mute`            | boolean | `false`    | Join muted                               |
| `hold`            | boolean | `false`    | Join on hold                             |
| `coachMode`       | boolean | `true`     | Supervisor coach mode (supervisors only) |
| `stayAlone`       | boolean | `false`    | Stay if only participant                 |
| `startMpcOnEnter` | boolean | `true`     | Start MPC when joining                   |
| `endMpcOnExit`    | boolean | `false`    | End MPC when leaving                     |

#### Entry/Exit Sounds

| Attribute          | Type   | Default  | Description                                        |
| ------------------ | ------ | -------- | -------------------------------------------------- |
| `enterSound`       | string | `beep:1` | Sound on entry: `none`, `beep:1`, `beep:2`, or URL |
| `enterSoundMethod` | string | `GET`    | HTTP method for enterSound URL                     |
| `exitSound`        | string | `beep:2` | Sound on exit: `none`, `beep:1`, `beep:2`, or URL  |
| `exitSoundMethod`  | string | `GET`    | HTTP method for exitSound URL                      |

#### Actions

| Attribute            | Type    | Description                         |
| -------------------- | ------- | ----------------------------------- |
| `onExitActionUrl`    | URL     | URL called when participant exits   |
| `onExitActionMethod` | string  | HTTP method (`GET`, `POST`)         |
| `relayDTMFInputs`    | boolean | Transmit DTMF to other participants |

### Supervisor Coach Mode

Supervisors with `coachMode="true"` can hear everyone but only agents hear them (customers cannot):

**Supervisor joining:**

```xml  theme={null}
<Response>
    <MultiPartyCall role="Supervisor" coachMode="true">
        support-call-123
    </MultiPartyCall>
</Response>
```

**Agent joining:**

```xml  theme={null}
<Response>
    <MultiPartyCall role="Agent" startMpcOnEnter="true">
        support-call-123
    </MultiPartyCall>
</Response>
```

**Customer joining:**

```xml  theme={null}
<Response>
    <MultiPartyCall role="Customer">
        support-call-123
    </MultiPartyCall>
</Response>
```

### MPC Recording

```xml  theme={null}
<Response>
    <MultiPartyCall
        role="Agent"
        record="true"
        recordFileFormat="mp3"
        recordingCallbackUrl="https://example.com/recording-ready/">
        recorded-call
    </MultiPartyCall>
</Response>
```

#### Recording Events

* `MPCRecordingInitiated`
* `MPCRecordingPaused`
* `MPCRecordingResumed`
* `MPCRecordingCompleted`
* `MPCRecordingFailed`

### Status Callback Events

Configure which events to receive with `statusCallbackEvents`:

| Value                            | Events Included                                                                                                                                               |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mpc-state-changes`              | MPCInitialized, MPCStart, MPCEnd                                                                                                                              |
| `participant-state-changes`      | ParticipantJoin, ParticipantExit, ParticipantMute, ParticipantUnmute, ParticipantHold, ParticipantUnhold, ParticipantCoachModeStart, ParticipantCoachModeStop |
| `participant-speak-events`       | ParticipantSpeakStart, ParticipantSpeakStop                                                                                                                   |
| `participant-digit-input-events` | ParticipantDigitInput                                                                                                                                         |
| `add-participant-api-events`     | AddParticipantByAPIActionInitiated, AddParticipantByAPIActionCompleted                                                                                        |

```xml  theme={null}
<MultiPartyCall
    statusCallbackUrl="https://example.com/mpc-events/"
    statusCallbackEvents="mpc-state-changes,participant-state-changes,participant-speak-events">
    my-mpc
</MultiPartyCall>
```

### Status Callback Parameters

| Parameter              | Description                    |
| ---------------------- | ------------------------------ |
| `EventName`            | Event that triggered callback  |
| `EventTimestamp`       | When the event occurred        |
| `MPCUUID`              | Unique MPC identifier          |
| `MPCName`              | Friendly MPC name              |
| `MemberID`             | Participant identifier         |
| `ParticipantRole`      | Agent, Supervisor, or Customer |
| `ParticipantCallUUID`  | Participant's call UUID        |
| `ParticipantCoachMode` | Whether in coach mode          |
| `MPCDuration`          | Total MPC duration (on end)    |
| `MPCBilledDuration`    | Billed duration                |
| `MPCBilledAmount`      | Cost in USD                    |

### On Exit Action

Continue call flow after leaving MPC:

```xml  theme={null}
<Response>
    <MultiPartyCall
        role="Customer"
        onExitActionUrl="https://example.com/post-call-survey/"
        onExitActionMethod="POST">
        support-call
    </MultiPartyCall>
</Response>
```

#### On Exit Parameters

| Parameter             | Description             |
| --------------------- | ----------------------- |
| `MPCUUID`             | MPC identifier          |
| `MPCFriendlyName`     | MPC name                |
| `MemberID`            | Participant ID          |
| `ParticipantCallUUID` | Call UUID               |
| `ParticipantJoinTime` | When participant joined |
| `ParticipantEndTime`  | When participant left   |
| `ParticipantRole`     | Participant's role      |

### Custom Hold Music

```xml  theme={null}
<Response>
    <MultiPartyCall
        role="Agent"
        agentHoldMusicUrl="https://example.com/agent-hold.xml"
        customerHoldMusicUrl="https://example.com/customer-hold.xml"
        waitMusicUrl="https://example.com/wait-music.xml">
        call-center-mpc
    </MultiPartyCall>
</Response>
```

Hold music URLs must return XML with `Play`, `Speak`, or `Wait` elements.

***

## Conference vs MultiPartyCall

| Feature              | Conference      | MultiPartyCall                    |
| -------------------- | --------------- | --------------------------------- |
| Max participants     | 20              | 10                                |
| Participant roles    | No              | Yes (Agent, Customer, Supervisor) |
| Coach mode           | No              | Yes                               |
| Individual hold/mute | No              | Yes                               |
| API control          | Limited         | Full                              |
| Use case             | Simple meetings | Call centers, support             |

***

## Related

* [Recording](/voice/xml/record/) - Record calls
* [Call Routing](/voice/xml/routing/) - Dial, Redirect, Hangup
* [MultiPartyCall API](/voice/api/multiparty-calls/) - Control MPCs via API
