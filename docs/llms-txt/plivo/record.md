# Source: https://plivo.com/docs/voice/xml/record.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Record

> Record calls, voicemails, and conversations

The `<Record>` element records audio from the call and returns the URL of the recording file. Use it for voicemail, call logging, or quality monitoring.

## Basic Usage

```xml  theme={null}
<Response>
    <Speak>Please leave a message after the beep.</Speak>
    <Record action="https://example.com/handle-recording/" />
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.SpeakElement('Please leave a message after the beep.'))
  response.add(plivoxml.RecordElement(action='https://example.com/handle-recording/'))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addSpeak('Please leave a message after the beep.');
  response.addRecord({ action: 'https://example.com/handle-recording/' });
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addSpeak('Please leave a message after the beep.')
  response.addRecord(action: 'https://example.com/handle-recording/')
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addSpeak('Please leave a message after the beep.');
  $response->addRecord(['action' => 'https://example.com/handle-recording/']);
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;

  Response response = new Response()
      .children(
          new Speak("Please leave a message after the beep."),
          new Record().action("https://example.com/handle-recording/")
      );
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  response.AddSpeak("Please leave a message after the beep.");
  response.AddRecord(new Dictionary<string, string>() {
      {"action", "https://example.com/handle-recording/"}
  });
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.SpeakElement).AddSpeak("Please leave a message after the beep."),
              new(xml.RecordElement).Action("https://example.com/handle-recording/"),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

***

## Attributes

### Basic Settings

| Attribute    | Type    | Default | Description                            |
| ------------ | ------- | ------- | -------------------------------------- |
| `action`     | URL     | -       | URL to receive recording data          |
| `method`     | string  | `POST`  | HTTP method for action (`GET`, `POST`) |
| `fileFormat` | string  | `mp3`   | Recording format (`mp3`, `wav`)        |
| `redirect`   | boolean | `true`  | Redirect to action URL when complete   |

### Timing

| Attribute     | Type    | Default | Description                                        |
| ------------- | ------- | ------- | -------------------------------------------------- |
| `timeout`     | integer | `15`    | Seconds of silence before stopping                 |
| `maxLength`   | integer | `60`    | Maximum recording duration in seconds              |
| `finishOnKey` | string  | `#`     | Key to stop recording (digit, `#`, `*`, or `none`) |
| `playBeep`    | boolean | `true`  | Play beep before recording                         |

### Session Recording

| Attribute           | Type    | Default  | Description                        |
| ------------------- | ------- | -------- | ---------------------------------- |
| `recordSession`     | boolean | `false`  | Record entire call in background   |
| `startOnDialAnswer` | boolean | `false`  | Start recording when B-leg answers |
| `recordChannelType` | string  | `stereo` | Channel type (`mono`, `stereo`)    |

### Transcription

| Attribute           | Type   | Default | Description                     |
| ------------------- | ------ | ------- | ------------------------------- |
| `transcriptionType` | string | -       | Set to `auto` for transcription |
| `transcriptionUrl`  | URL    | -       | URL to receive transcription    |

### Callbacks

| Attribute        | Type   | Default | Description                          |
| ---------------- | ------ | ------- | ------------------------------------ |
| `callbackUrl`    | URL    | -       | URL notified when recording is ready |
| `callbackMethod` | string | `POST`  | HTTP method for callback             |

***

## Voicemail

```xml  theme={null}
<Response>
    <Speak>
        You've reached John's voicemail.
        Leave a message after the beep, press pound when finished.
    </Speak>
    <Record
        action="https://example.com/save-voicemail/"
        maxLength="120"
        finishOnKey="#"
        playBeep="true"
    />
    <Speak>Thank you for your message. Goodbye.</Speak>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.SpeakElement(
      "You've reached John's voicemail. Leave a message after the beep."
  ))
  response.add(plivoxml.RecordElement(
      action='https://example.com/save-voicemail/',
      max_length=120,
      finish_on_key='#',
      play_beep=True
  ))
  response.add(plivoxml.SpeakElement('Thank you for your message. Goodbye.'))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addSpeak("You've reached John's voicemail. Leave a message after the beep.");
  response.addRecord({
      action: 'https://example.com/save-voicemail/',
      maxLength: 120,
      finishOnKey: '#',
      playBeep: true
  });
  response.addSpeak('Thank you for your message. Goodbye.');
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  response = Plivo::XML::Response.new
  response.addSpeak("You've reached John's voicemail.")
  response.addRecord(
      action: 'https://example.com/save-voicemail/',
      maxLength: 120,
      finishOnKey: '#',
      playBeep: true
  )
  response.addSpeak('Thank you for your message.')
  puts Plivo::XML::PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addSpeak("You've reached John's voicemail.");
  $response->addRecord([
      'action' => 'https://example.com/save-voicemail/',
      'maxLength' => 120,
      'finishOnKey' => '#',
      'playBeep' => true
  ]);
  $response->addSpeak('Thank you for your message.');
  echo $response->toXML();
  ```
</CodeGroup>

***

## Record Entire Session

Record the complete call in the background:

```xml  theme={null}
<Response>
    <Record recordSession="true"
            callbackUrl="https://example.com/recording-ready/" />
    <Speak>This call is being recorded for quality purposes.</Speak>
    <Dial>
        <Number>+14155551234</Number>
    </Dial>
</Response>
```

**Notes:**

* Recording starts immediately and continues until the call ends
* `timeout`, `finishOnKey`, and `playBeep` are ignored
* Recording is sent to `callbackUrl` when complete

***

## Record Dial Conversation

Record both parties after the dial connects:

```xml  theme={null}
<Response>
    <Record startOnDialAnswer="true"
            callbackUrl="https://example.com/recording-ready/" />
    <Dial>
        <Number>+14155551234</Number>
    </Dial>
</Response>
```

***

## Stereo vs Mono Recording

**Stereo** (default): Each party on separate audio channels - useful for call analytics.

**Mono**: Both parties on single channel - smaller file size.

```xml  theme={null}
<Record recordSession="true" recordChannelType="mono" />
```

***

## With Transcription

Get automatic speech-to-text:

```xml  theme={null}
<Response>
    <Speak>Please leave your message.</Speak>
    <Record
        action="https://example.com/handle-recording/"
        transcriptionType="auto"
        transcriptionUrl="https://example.com/transcription/"
    />
</Response>
```

**Transcription limits:**

* English only
* Duration: 500ms to 4 hours
* File size: under 2GB

***

## Action URL Parameters

Sent when recording completes:

| Parameter             | Description                  |
| --------------------- | ---------------------------- |
| `RecordUrl`           | URL of the recording file    |
| `RecordingID`         | Unique recording identifier  |
| `RecordingDuration`   | Duration in seconds          |
| `RecordingDurationMs` | Duration in milliseconds     |
| `RecordingStartMs`    | Start time (epoch ms)        |
| `RecordingEndMs`      | End time (epoch ms)          |
| `Digits`              | Key pressed to stop (if any) |

**Note:** When `recordSession` or `startOnDialAnswer` is `true`, duration values are `-1` in the initial request. Final values are sent to `callbackUrl`.

***

## Callback URL Parameters

Sent when recording file is ready:

| Parameter             | Description               |
| --------------------- | ------------------------- |
| `RecordUrl`           | URL of the recording file |
| `RecordingID`         | Recording identifier      |
| `RecordingDuration`   | Duration in seconds       |
| `RecordingDurationMs` | Duration in milliseconds  |
| `RecordingStartMs`    | Start time (epoch ms)     |
| `RecordingEndMs`      | End time (epoch ms)       |

***

## Transcription URL Parameters

| Parameter              | Description               |
| ---------------------- | ------------------------- |
| `transcription`        | Transcribed text          |
| `transcription_charge` | Cost of transcription     |
| `transcription_rate`   | Rate per minute           |
| `duration`             | Recording duration        |
| `call_uuid`            | Call identifier           |
| `recording_id`         | Recording identifier      |
| `error`                | Error message (if failed) |

***

## Best Practices

1. **Inform callers** - Always notify that the call is being recorded (legal requirement in many jurisdictions)
2. **Set appropriate limits** - Use `maxLength` to prevent very long recordings
3. **Use callbacks** - Use `callbackUrl` for reliable notification when recording is ready
4. **Choose format wisely** - MP3 for smaller files, WAV for highest quality
5. **Handle storage** - Download recordings from Plivo; they're deleted after 30 days

***

## Related

* [Conference](/voice/xml/conferencing) - Record conference calls
* [Recordings API](/voice/api/recordings/) - Manage recordings
* [Play](/voice/xml/audio-output#play) - Play recorded audio
