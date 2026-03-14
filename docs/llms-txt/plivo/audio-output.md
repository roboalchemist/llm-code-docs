# Source: https://plivo.com/docs/voice/xml/audio-output.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Audio Output

> Play audio, text-to-speech, and DTMF tones during calls

This page covers the XML elements for audio output: converting text to speech, playing audio files, and sending DTMF tones.

***

## Speak

The `<Speak>` element converts text to speech and plays it to the caller. Use it for dynamic messages that can't be prerecorded.

### Basic Usage

```xml  theme={null}
<Response>
    <Speak>Hello! Welcome to our service.</Speak>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.SpeakElement('Hello! Welcome to our service.'))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addSpeak('Hello! Welcome to our service.');
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addSpeak('Hello! Welcome to our service.')
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addSpeak('Hello! Welcome to our service.');
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.Response;
  import com.plivo.api.xml.Speak;

  Response response = new Response()
      .children(new Speak("Hello! Welcome to our service."));
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  response.AddSpeak("Hello! Welcome to our service.");
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.SpeakElement).AddSpeak("Hello! Welcome to our service."),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### Speak Attributes

| Attribute  | Type    | Default | Description                                        |
| ---------- | ------- | ------- | -------------------------------------------------- |
| `voice`    | string  | `WOMAN` | Voice tone. Allowed: `WOMAN`, `MAN`                |
| `language` | string  | `en-US` | Language for speech. See supported languages below |
| `loop`     | integer | `1`     | Number of times to repeat. `0` = infinite          |

### Change Voice and Language

```xml  theme={null}
<Response>
    <Speak voice="MAN" language="en-GB">
        Good day! This message uses a British male voice.
    </Speak>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.SpeakElement(
      'Good day! This message uses a British male voice.',
      voice='MAN',
      language='en-GB'
  ))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addSpeak('Good day! This message uses a British male voice.', {
      voice: 'MAN',
      language: 'en-GB'
  });
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addSpeak('Good day!', voice: 'MAN', language: 'en-GB')
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addSpeak('Good day!', ['voice' => 'MAN', 'language' => 'en-GB']);
  echo $response->toXML();
  ```
</CodeGroup>

### Loop a Message

Play a message multiple times:

```xml  theme={null}
<Response>
    <Speak loop="3">Please hold. Your call is important to us.</Speak>
</Response>
```

Set `loop="0"` to repeat indefinitely until the call ends:

```xml  theme={null}
<Response>
    <Speak loop="0">Please wait while we connect you.</Speak>
</Response>
```

### Supported Languages

| Language               | Code    | Woman | Man |
| ---------------------- | ------- | ----- | --- |
| Danish                 | `da-DK` | Yes   | No  |
| Dutch                  | `nl-NL` | Yes   | Yes |
| English (Australian)   | `en-AU` | Yes   | Yes |
| English (British)      | `en-GB` | Yes   | Yes |
| English (USA)          | `en-US` | Yes   | Yes |
| French                 | `fr-FR` | Yes   | Yes |
| French (Canadian)      | `fr-CA` | Yes   | No  |
| German                 | `de-DE` | Yes   | Yes |
| Italian                | `it-IT` | Yes   | Yes |
| Polish                 | `pl-PL` | Yes   | Yes |
| Portuguese             | `pt-PT` | No    | Yes |
| Portuguese (Brazilian) | `pt-BR` | Yes   | Yes |
| Russian                | `ru-RU` | Yes   | No  |
| Spanish                | `es-ES` | Yes   | Yes |
| Spanish (USA)          | `es-US` | Yes   | Yes |
| Swedish                | `sv-SE` | Yes   | No  |

### SSML Support

Speech Synthesis Markup Language (SSML) provides fine-grained control over pronunciation, pitch, rate, and pauses. Use Polly voices for SSML support.

```xml  theme={null}
<Response>
    <Speak voice="Polly.Joey" language="en-US">
        <prosody rate="medium">
            Hello and welcome to Plivo.
            <break time="500ms"/>
            The word <say-as interpret-as="spell-out">SSML</say-as>
            stands for Speech Synthesis Markup Language.
        </prosody>
    </Speak>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  speak = plivoxml.SpeakElement(
      content="The word",
      voice="Polly.Joey",
      language="en-US"
  )
  speak.add_say_as("read", interpret_as="characters")
  speak.add_s("may be interpreted as either the present simple form")
  speak.add_w("read", role="amazon:VB")
  speak.add_s("or the past participle form")
  speak.add_w("read", role="amazon:VBD")
  response.add(speak)
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  const speakElem = response.addSpeak('The word', {
      voice: 'Polly.Joey',
      language: 'en-US'
  });
  speakElem.addSayAs('read', { 'interpret-as': 'characters' });
  speakElem.addS('may be interpreted differently');
  speakElem.addW('read', { role: 'amazon:VB' });
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  response = Plivo::XML::Response.new
  speak_elem = response.addSpeak('The word', voice: 'Polly.Joey', language: 'en-US')
  speak_elem.addSayAs('read', 'interpret-as' => 'characters')
  speak_elem.addS('may be interpreted differently')
  speak_elem.addW('read', 'role' => 'amazon:VB')
  puts Plivo::XML::PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $speak_elem = $response->addSpeak('The word', [
      'language' => 'en-US',
      'voice' => 'Polly.Joey'
  ]);
  $speak_elem->addSayAs('read', ['interpret-as' => 'characters']);
  $speak_elem->addS('may be interpreted differently');
  echo $response->toXML();
  ```
</CodeGroup>

#### Common SSML Tags

| Tag          | Description                | Example                                         |
| ------------ | -------------------------- | ----------------------------------------------- |
| `<break>`    | Add a pause                | `<break time="500ms"/>`                         |
| `<say-as>`   | Control pronunciation      | `<say-as interpret-as="spell-out">ABC</say-as>` |
| `<prosody>`  | Modify pitch, rate, volume | `<prosody rate="slow">Slowly</prosody>`         |
| `<emphasis>` | Add emphasis               | `<emphasis level="strong">Important</emphasis>` |
| `<p>`        | Paragraph pause            | `<p>First paragraph.</p>`                       |
| `<s>`        | Sentence pause             | `<s>First sentence.</s>`                        |

### Speak Nesting

`<Speak>` can be nested inside:

* `<GetDigits>` - Play message while collecting input
* `<GetInput>` - Play message while collecting speech/digits
* `<PreAnswer>` - Play message before answering

```xml  theme={null}
<Response>
    <GetDigits action="/handle-input/" numDigits="1">
        <Speak>Press 1 for sales, press 2 for support.</Speak>
    </GetDigits>
</Response>
```

***

## Play

The `<Play>` element plays an audio file to the caller. Use it for pre-recorded messages, music, or sound effects.

### Basic Usage

```xml  theme={null}
<Response>
    <Play>https://example.com/audio/welcome.mp3</Play>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.PlayElement('https://example.com/audio/welcome.mp3'))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addPlay('https://example.com/audio/welcome.mp3');
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addPlay('https://example.com/audio/welcome.mp3')
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addPlay('https://example.com/audio/welcome.mp3');
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.Response;
  import com.plivo.api.xml.Play;

  Response response = new Response()
      .children(new Play("https://example.com/audio/welcome.mp3"));
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  response.AddPlay("https://example.com/audio/welcome.mp3");
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.PlayElement).SetContents("https://example.com/audio/welcome.mp3"),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### Play Attributes

| Attribute | Type    | Default | Description                                            |
| --------- | ------- | ------- | ------------------------------------------------------ |
| `loop`    | integer | `1`     | Number of times to play the audio. `0` = infinite loop |

### Loop Audio

Play hold music on repeat:

```xml  theme={null}
<Response>
    <Play loop="0">https://example.com/audio/hold-music.mp3</Play>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.PlayElement(
      'https://example.com/audio/hold-music.mp3',
      loop=0
  ))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addPlay('https://example.com/audio/hold-music.mp3', { loop: 0 });
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addPlay('https://example.com/audio/hold-music.mp3', loop: 0)
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addPlay('https://example.com/audio/hold-music.mp3', ['loop' => 0]);
  echo $response->toXML();
  ```
</CodeGroup>

### Supported Formats

| Format | Extension | Notes                              |
| ------ | --------- | ---------------------------------- |
| MP3    | `.mp3`    | Recommended for smaller file sizes |
| WAV    | `.wav`    | Highest quality, larger files      |

**Requirements:**

* Audio must be served over HTTPS
* Maximum file size: 10 MB
* Recommended: 8kHz or 16kHz sample rate, mono

### Combine with Speak

```xml  theme={null}
<Response>
    <Play>https://example.com/audio/intro-jingle.mp3</Play>
    <Speak>Welcome to Acme Corporation. How can we help you today?</Speak>
</Response>
```

### Play During IVR

Nest `<Play>` inside `<GetDigits>` to play audio while collecting input:

```xml  theme={null}
<Response>
    <GetDigits action="/handle-input/" numDigits="1" timeout="10">
        <Play>https://example.com/audio/menu-options.mp3</Play>
    </GetDigits>
    <Speak>We didn't receive any input. Goodbye.</Speak>
</Response>
```

### Play Nesting

`<Play>` can be nested inside:

* `<GetDigits>` - Play while collecting digits
* `<GetInput>` - Play while collecting speech/digits
* `<PreAnswer>` - Play before answering the call

### Play Best Practices

1. **Use HTTPS** - Audio URLs must use HTTPS
2. **Optimize file size** - Compress audio for faster loading
3. **Host reliably** - Use a CDN for audio file hosting
4. **Test audio quality** - Ensure audio is clear at phone quality (8kHz)
5. **Provide fallback** - Use `<Speak>` as backup if audio fails to load

***

## DTMF

The `<DTMF>` element sends DTMF (Dual-Tone Multi-Frequency) tones on the current call. Use it to navigate IVR systems, enter PINs, or interact with telephony systems.

### Basic Usage

```xml  theme={null}
<Response>
    <DTMF>1234</DTMF>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.DTMFElement('1234'))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addDTMF('1234');
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addDTMF('1234')
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addDTMF('1234');
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;

  Response response = new Response()
      .children(new DTMF("1234"));
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  response.AddDTMF("1234");
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.DTMFElement).SetContents("1234"),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### DTMF Attributes

| Attribute | Type    | Default | Description                                      |
| --------- | ------- | ------- | ------------------------------------------------ |
| `async`   | boolean | `true`  | Send asynchronously and continue to next element |

### Allowed Characters

| Character | Description      |
| --------- | ---------------- |
| `0-9`     | Digit tones      |
| `*`       | Star key         |
| `#`       | Pound/hash key   |
| `w`       | Wait 0.5 seconds |
| `W`       | Wait 1 second    |

### With Pauses

Use `w` (0.5s) or `W` (1s) to add delays between tones:

```xml  theme={null}
<Response>
    <DTMF>1ww2ww3ww4</DTMF>
</Response>
```

This sends 1, waits 1 second, sends 2, waits 1 second, etc.

### Navigate External IVR

When dialing an external number with an IVR:

```xml  theme={null}
<Response>
    <Dial>
        <Number sendDigits="wwww1234#">+14155559999</Number>
    </Dial>
</Response>
```

This is typically done using the `sendDigits` attribute on `<Number>` rather than the `<DTMF>` element.

### Send During Call

Send tones during an active call:

```xml  theme={null}
<Response>
    <Speak>Sending your confirmation code now.</Speak>
    <DTMF>5678</DTMF>
    <Speak>Code sent.</Speak>
</Response>
```

### Synchronous vs Asynchronous

**Async (default):** DTMF sends while next element starts

```xml  theme={null}
<DTMF async="true">123</DTMF>
<Speak>Processing...</Speak>
```

**Sync:** Wait for DTMF to complete before continuing

```xml  theme={null}
<DTMF async="false">123</DTMF>
<Speak>DTMF complete.</Speak>
```

### DTMF Use Cases

| Scenario          | Example                 |
| ----------------- | ----------------------- |
| Enter PIN         | `<DTMF>1234#</DTMF>`    |
| Navigate IVR menu | `<DTMF>1</DTMF>`        |
| Enter extension   | `<DTMF>wwww5678</DTMF>` |
| Star code         | `<DTMF>*67</DTMF>`      |

### Combined with Dial

When using with `<Dial>`, prefer `sendDigits` on the `<Number>` element:

```xml  theme={null}
<Response>
    <Dial>
        <Number sendDigits="wwww123#">+14155551234</Number>
    </Dial>
</Response>
```

***

## Related

* [Input Collection](/voice/xml/input/) - GetDigits, GetInput
* [Call Routing](/voice/xml/routing/) - Dial, Redirect, Hangup, Wait
* [SSML Concepts](/voice/concepts/ssml/) - Advanced speech control
