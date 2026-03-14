# Source: https://plivo.com/docs/voice/xml/input.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Input Collection

> Collect DTMF digits and speech input from callers

This page covers the XML elements for collecting user input: DTMF digit presses and automatic speech recognition.

***

## GetDigits

The `<GetDigits>` element collects DTMF (touch-tone) digits entered by the caller. Use it for IVR menus, PIN entry, and numeric input.

<Note>
  **Recommendation:** Use [GetInput](#getinput) instead of GetDigits for new applications. GetInput supports both speech and digit input.
</Note>

### Basic Usage

```xml  theme={null}
<Response>
    <GetDigits action="https://example.com/handle-input/" numDigits="1">
        <Speak>Press 1 for sales, press 2 for support.</Speak>
    </GetDigits>
    <Speak>We didn't receive any input. Goodbye.</Speak>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  getdigits = plivoxml.GetDigitsElement(
      action='https://example.com/handle-input/',
      num_digits=1
  )
  getdigits.add(plivoxml.SpeakElement('Press 1 for sales, press 2 for support.'))
  response.add(getdigits)
  response.add(plivoxml.SpeakElement("We didn't receive any input. Goodbye."))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  const getDigits = response.addGetDigits({
      action: 'https://example.com/handle-input/',
      numDigits: 1
  });
  getDigits.addSpeak('Press 1 for sales, press 2 for support.');
  response.addSpeak("We didn't receive any input. Goodbye.");
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  getdigits = response.addGetDigits(
      action: 'https://example.com/handle-input/',
      numDigits: 1
  )
  getdigits.addSpeak('Press 1 for sales, press 2 for support.')
  response.addSpeak("We didn't receive any input. Goodbye.")
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $getdigits = $response->addGetDigits([
      'action' => 'https://example.com/handle-input/',
      'numDigits' => 1
  ]);
  $getdigits->addSpeak('Press 1 for sales, press 2 for support.');
  $response->addSpeak("We didn't receive any input. Goodbye.");
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;

  Response response = new Response()
      .children(
          new GetDigits()
              .action("https://example.com/handle-input/")
              .numDigits(1)
              .children(new Speak("Press 1 for sales, press 2 for support.")),
          new Speak("We didn't receive any input. Goodbye.")
      );
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  var getDigits = new GetDigits(new Dictionary<string, string>() {
      {"action", "https://example.com/handle-input/"},
      {"numDigits", "1"}
  });
  getDigits.AddSpeak("Press 1 for sales, press 2 for support.");
  response.Add(getDigits);
  response.AddSpeak("We didn't receive any input. Goodbye.");
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.GetDigitsElement).
                  Action("https://example.com/handle-input/").
                  NumDigits(1).
                  SetContents([]interface{}{
                      new(xml.SpeakElement).AddSpeak("Press 1 for sales."),
                  }),
              new(xml.SpeakElement).AddSpeak("No input received."),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### GetDigits Attributes

| Attribute            | Type    | Default        | Description                                   |
| -------------------- | ------- | -------------- | --------------------------------------------- |
| `action`             | URL     | -              | URL to receive the digits                     |
| `method`             | string  | `POST`         | HTTP method (`GET`, `POST`)                   |
| `numDigits`          | integer | `99`           | Maximum digits to collect                     |
| `timeout`            | integer | `5`            | Seconds to wait for first digit               |
| `digitTimeout`       | integer | `2`            | Seconds between consecutive digits            |
| `finishOnKey`        | string  | `#`            | Key to submit input (digit, `#`, `*`, `none`) |
| `retries`            | integer | `1`            | Retry attempts if no input                    |
| `redirect`           | boolean | `true`         | Redirect to action URL                        |
| `playBeep`           | boolean | `false`        | Play beep after nested elements               |
| `validDigits`        | string  | `1234567890*#` | Allowed digits                                |
| `invalidDigitsSound` | URL     | -              | Audio for invalid digit                       |
| `log`                | boolean | `true`         | Log digits (disable for sensitive input)      |

### Nested Elements

`<GetDigits>` can contain:

* `<Speak>` - Text-to-speech prompt
* `<Play>` - Audio file prompt

Prompts play while waiting for input. Input collection starts as soon as the first digit is pressed.

### Phone Tree (IVR)

```xml  theme={null}
<Response>
    <GetDigits action="https://example.com/ivr/" numDigits="1" timeout="10" retries="2">
        <Speak>
            Welcome to Acme Corp.
            Press 1 for sales.
            Press 2 for support.
            Press 3 for billing.
            Press 0 to speak with an operator.
        </Speak>
    </GetDigits>
    <Speak>Sorry, we didn't receive valid input. Goodbye.</Speak>
</Response>
```

Handle the input on your server:

```python  theme={null}
# Flask example
@app.route('/ivr/', methods=['POST'])
def handle_ivr():
    digits = request.form.get('Digits')
    response = plivoxml.ResponseElement()

    if digits == '1':
        response.add(plivoxml.SpeakElement('Connecting you to sales.'))
        dial = plivoxml.DialElement()
        dial.add(plivoxml.NumberElement('+14155551111'))
        response.add(dial)
    elif digits == '2':
        response.add(plivoxml.SpeakElement('Connecting you to support.'))
        dial = plivoxml.DialElement()
        dial.add(plivoxml.NumberElement('+14155552222'))
        response.add(dial)
    elif digits == '3':
        response.add(plivoxml.RedirectElement('https://example.com/billing-menu/'))
    elif digits == '0':
        response.add(plivoxml.SpeakElement('Please hold for an operator.'))
        dial = plivoxml.DialElement()
        dial.add(plivoxml.NumberElement('+14155550000'))
        response.add(dial)
    else:
        response.add(plivoxml.SpeakElement('Invalid option.'))
        response.add(plivoxml.RedirectElement('https://example.com/ivr-start/'))

    return Response(response.to_string(), mimetype='application/xml')
```

### PIN Entry

Collect a specific number of digits:

```xml  theme={null}
<Response>
    <GetDigits action="https://example.com/verify-pin/"
               numDigits="4"
               timeout="10"
               finishOnKey=""
               log="false">
        <Speak>Please enter your 4-digit PIN.</Speak>
    </GetDigits>
</Response>
```

**Note:** Set `log="false"` for sensitive input like PINs.

### Variable Length Input

Use `finishOnKey` for variable-length input:

```xml  theme={null}
<Response>
    <GetDigits action="https://example.com/handle-input/"
               finishOnKey="#"
               timeout="15">
        <Speak>
            Enter your account number followed by the pound key.
        </Speak>
    </GetDigits>
</Response>
```

### Restrict Valid Digits

Only accept specific digits:

```xml  theme={null}
<Response>
    <GetDigits action="https://example.com/handle-input/"
               numDigits="1"
               validDigits="123"
               invalidDigitsSound="https://example.com/invalid.mp3">
        <Speak>Press 1, 2, or 3.</Speak>
    </GetDigits>
</Response>
```

### No Redirect

Collect digits without redirecting (fire and forget):

```xml  theme={null}
<Response>
    <GetDigits action="https://example.com/log-input/"
               redirect="false"
               numDigits="1">
        <Speak>Press any key to confirm you're listening.</Speak>
    </GetDigits>
    <Speak>Thank you. Continuing with your call.</Speak>
</Response>
```

### GetDigits Action URL Parameters

When digits are collected, these parameters are sent:

| Parameter | Description                                  |
| --------- | -------------------------------------------- |
| `Digits`  | The digits entered (excluding `finishOnKey`) |

Plus all standard [request parameters](/voice/xml/overview/#request-parameters).

### GetDigits Flow Behavior

1. Nested `<Speak>` or `<Play>` elements execute
2. If `playBeep="true"`, a beep plays
3. Digit collection starts
4. Collection ends when:
   * `numDigits` reached
   * `finishOnKey` pressed
   * `timeout` or `digitTimeout` expires
5. Digits sent to `action` URL
6. Response XML from `action` URL executes

If no digits are received after `retries` attempts, execution continues to the next element.

***

## GetInput

The `<GetInput>` element collects user input through automatic speech recognition (ASR) or DTMF digit presses. It's the recommended replacement for `<GetDigits>`, supporting both speech and digit input.

### Basic Usage

```xml  theme={null}
<Response>
    <GetInput action="https://example.com/handle-input/" inputType="dtmf speech">
        <Speak>How can I help you today? You can say your request or press 1 for sales, 2 for support.</Speak>
    </GetInput>
    <Speak>We didn't receive any input. Please try again.</Speak>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  getinput = plivoxml.GetInputElement(
      action='https://example.com/handle-input/',
      input_type='dtmf speech'
  )
  getinput.add_speak('How can I help you today?')
  response.add(getinput)
  response.add(plivoxml.SpeakElement("We didn't receive any input."))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  const getInput = response.addGetInput({
      action: 'https://example.com/handle-input/',
      inputType: 'dtmf speech'
  });
  getInput.addSpeak('How can I help you today?');
  response.addSpeak("We didn't receive any input.");
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  response = Plivo::XML::Response.new
  get_input = response.addGetInput(
      action: 'https://example.com/handle-input/',
      inputType: 'dtmf speech'
  )
  get_input.addSpeak('How can I help you today?')
  response.addSpeak("We didn't receive any input.")
  puts Plivo::XML::PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $get_input = $response->addGetInput([
      'action' => 'https://example.com/handle-input/',
      'inputType' => 'dtmf speech'
  ]);
  $get_input->addSpeak('How can I help you today?');
  $response->addSpeak("We didn't receive any input.");
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;

  Response response = new Response()
      .children(
          new GetInput()
              .action("https://example.com/handle-input/")
              .inputType("dtmf speech")
              .children(new Speak("How can I help you today?")),
          new Speak("We didn't receive any input.")
      );
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  var getInput = new GetInput(new Dictionary<string, string>() {
      {"action", "https://example.com/handle-input/"},
      {"inputType", "dtmf speech"}
  });
  getInput.AddSpeak("How can I help you today?");
  response.Add(getInput);
  response.AddSpeak("We didn't receive any input.");
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.GetInputElement).
                  SetAction("https://example.com/handle-input/").
                  SetInputType("dtmf speech").
                  SetContents([]interface{}{
                      new(xml.SpeakElement).AddSpeak("How can I help you today?"),
                  }),
              new(xml.SpeakElement).AddSpeak("We didn't receive any input."),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### GetInput Attributes

#### Core Settings

| Attribute   | Type    | Default    | Description                                 |
| ----------- | ------- | ---------- | ------------------------------------------- |
| `action`    | URL     | *required* | URL to receive the input                    |
| `method`    | string  | `POST`     | HTTP method (`GET`, `POST`)                 |
| `inputType` | string  | -          | Input type: `dtmf`, `speech`, `dtmf speech` |
| `redirect`  | boolean | `true`     | Redirect to action URL after input          |
| `log`       | boolean | `true`     | Log input (disable for sensitive data)      |

#### Timing

| Attribute          | Type    | Default | Description                                        |
| ------------------ | ------- | ------- | -------------------------------------------------- |
| `executionTimeout` | integer | `15`    | Max seconds to wait for input (5-60)               |
| `digitEndTimeout`  | string  | `auto`  | Seconds between digits (2-10, or `auto`)           |
| `speechEndTimeout` | string  | `auto`  | Seconds of silence to end speech (2-10, or `auto`) |

#### DTMF Settings

| Attribute     | Type    | Default | Description                                   |
| ------------- | ------- | ------- | --------------------------------------------- |
| `numDigits`   | integer | `32`    | Maximum digits to collect (1-32)              |
| `finishOnKey` | string  | `#`     | Key to submit input (digit, `#`, `*`, `none`) |

#### Speech Settings

| Attribute         | Type    | Default   | Description                                              |
| ----------------- | ------- | --------- | -------------------------------------------------------- |
| `language`        | string  | `en-US`   | Speech recognition language                              |
| `speechModel`     | string  | `default` | ASR model: `default`, `command_and_search`, `phone_call` |
| `hints`           | string  | -         | Comma-separated phrases to boost recognition             |
| `profanityFilter` | boolean | `false`   | Filter profane words                                     |

#### Callbacks

| Attribute                            | Type   | Default | Description                      |
| ------------------------------------ | ------ | ------- | -------------------------------- |
| `interimSpeechResultsCallback`       | URL    | -       | URL for real-time speech results |
| `interimSpeechResultsCallbackMethod` | string | `POST`  | HTTP method for interim callback |

### Input Types

#### DTMF Only

Collect only digit presses:

```xml  theme={null}
<GetInput action="/handle-input/" inputType="dtmf" numDigits="4">
    <Speak>Enter your 4-digit PIN.</Speak>
</GetInput>
```

#### Speech Only

Collect only speech input:

```xml  theme={null}
<GetInput action="/handle-input/" inputType="speech" language="en-US">
    <Speak>What city would you like to search?</Speak>
</GetInput>
```

#### Both Speech and DTMF

Accept either input type (first detected wins):

```xml  theme={null}
<GetInput action="/handle-input/" inputType="dtmf speech">
    <Speak>Say your request or press 1 for help.</Speak>
</GetInput>
```

### Speech Recognition Models

| Model                | Best For                          |
| -------------------- | --------------------------------- |
| `default`            | General long-form audio           |
| `command_and_search` | Short commands and voice search   |
| `phone_call`         | Phone call audio (varied quality) |

```xml  theme={null}
<GetInput action="/handle-input/"
          inputType="speech"
          speechModel="command_and_search"
          language="en-US">
    <Speak>What would you like to do?</Speak>
</GetInput>
```

### Improve Speech Recognition

Use `hints` to boost recognition of specific words:

```xml  theme={null}
<GetInput action="/handle-input/"
          inputType="speech"
          hints="account balance, transfer money, pay bill, customer service">
    <Speak>How can I help you with your account today?</Speak>
</GetInput>
```

**Limits:**

* Max 500 phrases per request
* Max 10,000 characters total
* Max 100 characters per phrase

### Real-Time Speech Results

Get interim transcription results as the user speaks:

```xml  theme={null}
<GetInput action="/final-result/"
          inputType="speech"
          interimSpeechResultsCallback="https://example.com/interim/">
    <Speak>Please describe your issue.</Speak>
</GetInput>
```

#### Interim Callback Parameters

| Parameter        | Description                    |
| ---------------- | ------------------------------ |
| `StableSpeech`   | Confident transcription so far |
| `UnstableSpeech` | Current guess (may change)     |
| `Stability`      | Confidence score (0.0-1.0)     |
| `SequenceNumber` | Order of callbacks             |

### Supported Languages

Common languages include:

| Language            | Code    |
| ------------------- | ------- |
| English (US)        | `en-US` |
| English (UK)        | `en-GB` |
| English (Australia) | `en-AU` |
| Spanish (US)        | `es-US` |
| Spanish (Spain)     | `es-ES` |
| French              | `fr-FR` |
| German              | `de-DE` |
| Italian             | `it-IT` |
| Portuguese (Brazil) | `pt-BR` |
| Japanese            | `ja-JP` |
| Chinese (Mandarin)  | `zh-CN` |

### GetInput Action URL Parameters

When input is collected:

| Parameter               | Description                      |
| ----------------------- | -------------------------------- |
| `InputType`             | `dtmf` or `speech`               |
| `Digits`                | Digits entered (empty if speech) |
| `Speech`                | Transcribed text (empty if DTMF) |
| `SpeechConfidenceScore` | Confidence (0.0-1.0)             |
| `BilledAmount`          | Transcription cost               |

Plus all standard [request parameters](/voice/xml/overview/#request-parameters).

### Handling Input on Your Server

```python  theme={null}
# Flask example
@app.route('/handle-input/', methods=['POST'])
def handle_input():
    input_type = request.form.get('InputType')
    response = plivoxml.ResponseElement()

    if input_type == 'dtmf':
        digits = request.form.get('Digits')
        if digits == '1':
            response.add(plivoxml.SpeakElement('Connecting you to sales.'))
            # Add dial logic
        elif digits == '2':
            response.add(plivoxml.SpeakElement('Connecting you to support.'))
            # Add dial logic

    elif input_type == 'speech':
        speech = request.form.get('Speech', '').lower()
        confidence = float(request.form.get('SpeechConfidenceScore', 0))

        if confidence < 0.5:
            response.add(plivoxml.SpeakElement("I didn't catch that. Please try again."))
            response.add(plivoxml.RedirectElement('/start/'))
        elif 'balance' in speech:
            response.add(plivoxml.SpeakElement('Your current balance is $150.'))
        elif 'transfer' in speech:
            response.add(plivoxml.RedirectElement('/transfer-flow/'))
        else:
            response.add(plivoxml.SpeakElement("I'm not sure how to help with that."))

    return Response(response.to_string(), mimetype='application/xml')
```

### GetInput Nested Elements

`<GetInput>` can contain:

* `<Speak>` - Voice prompt
* `<Play>` - Audio prompt

### Speech Recognition Pricing

Speech recognition is billed per 15-second increment.

***

## Related

* [Audio Output](/voice/xml/audio-output/) - Speak, Play, DTMF
* [Call Routing](/voice/xml/routing/) - Dial, Redirect, Hangup, Wait
