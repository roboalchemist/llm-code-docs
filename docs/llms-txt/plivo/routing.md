# Source: https://plivo.com/docs/voice/xml/routing.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Call Routing

> Connect calls, transfer flow, end calls, and pause execution

This page covers the XML elements for call routing: connecting to other parties, transferring call flow, ending calls, and pausing execution.

***

## Dial

The `<Dial>` element connects the current call to another phone number, SIP endpoint, or Plivo user. When the dialed party answers, both parties are connected. When either party hangs up, the connection ends.

### Basic Usage

```xml  theme={null}
<Response>
    <Dial>
        <Number>+14155551234</Number>
    </Dial>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  dial = plivoxml.DialElement()
  dial.add(plivoxml.NumberElement('+14155551234'))
  response.add(dial)
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  const dial = response.addDial();
  dial.addNumber('+14155551234');
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  dial = response.addDial()
  dial.addNumber('+14155551234')
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $dial = $response->addDial();
  $dial->addNumber('+14155551234');
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;

  Response response = new Response()
      .children(
          new Dial().children(new Number("+14155551234"))
      );
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  var dial = new Dial();
  dial.AddNumber("+14155551234");
  response.Add(dial);
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.DialElement).SetContents([]interface{}{
                  new(xml.NumberElement).SetContents("+14155551234"),
              }),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### Dial Attributes

| Attribute      | Type    | Default       | Description                                |
| -------------- | ------- | ------------- | ------------------------------------------ |
| `action`       | URL     | -             | URL to receive dial completion status      |
| `method`       | string  | `POST`        | HTTP method for action URL (`GET`, `POST`) |
| `timeout`      | integer | -             | Seconds to wait for answer                 |
| `timeLimit`    | integer | `14400`       | Maximum call duration in seconds           |
| `callerId`     | string  | caller's ID   | Caller ID to display                       |
| `callerName`   | string  | caller's name | Caller name (max 50 chars)                 |
| `hangupOnStar` | boolean | `false`       | Let caller hang up B-leg by pressing \*    |
| `redirect`     | boolean | `true`        | Redirect to action URL when complete       |

#### Callback Attributes

| Attribute         | Type    | Description                                  |
| ----------------- | ------- | -------------------------------------------- |
| `callbackUrl`     | URL     | URL for real-time dial events                |
| `callbackMethod`  | string  | HTTP method for callback (`GET`, `POST`)     |
| `confirmSound`    | URL     | URL returning XML to play when B-leg answers |
| `confirmKey`      | string  | Key B-leg must press to accept call          |
| `confirmTimeout`  | integer | Seconds to wait for confirm key              |
| `dialMusic`       | URL     | URL returning XML for ringback, or `real`    |
| `digitsMatch`     | string  | DTMF patterns to report (A-leg)              |
| `digitsMatchBLeg` | string  | DTMF patterns to report (B-leg)              |
| `sipHeaders`      | string  | Custom SIP headers (key=value,key2=value2)   |

### Nested Elements

`<Dial>` must contain at least one nested element:

#### Number Element

Dial a phone number:

```xml  theme={null}
<Dial>
    <Number>+14155551234</Number>
</Dial>
```

**Number Attributes:**

| Attribute         | Type    | Default | Description                                              |
| ----------------- | ------- | ------- | -------------------------------------------------------- |
| `sendDigits`      | string  | -       | DTMF digits to send after answer. Use `w` for 0.5s pause |
| `sendOnPreanswer` | boolean | `false` | Send digits during early media                           |

#### User Element

Dial a SIP endpoint:

```xml  theme={null}
<Dial>
    <User>sip:alice@example.com</User>
</Dial>
```

### Simultaneous Dialing

Ring multiple numbers at once. First to answer is connected:

```xml  theme={null}
<Response>
    <Dial>
        <Number>+14155551111</Number>
        <Number>+14155552222</Number>
        <Number>+14155553333</Number>
    </Dial>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  dial = plivoxml.DialElement()
  dial.add(plivoxml.NumberElement('+14155551111'))
  dial.add(plivoxml.NumberElement('+14155552222'))
  dial.add(plivoxml.NumberElement('+14155553333'))
  response.add(dial)
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  const dial = response.addDial();
  dial.addNumber('+14155551111');
  dial.addNumber('+14155552222');
  dial.addNumber('+14155553333');
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  response = Plivo::XML::Response.new
  dial = response.addDial()
  dial.addNumber('+14155551111')
  dial.addNumber('+14155552222')
  dial.addNumber('+14155553333')
  puts Plivo::XML::PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $dial = $response->addDial();
  $dial->addNumber('+14155551111');
  $dial->addNumber('+14155552222');
  $dial->addNumber('+14155553333');
  echo $response->toXML();
  ```
</CodeGroup>

### Sequential Dialing

Try numbers one at a time with timeouts:

```xml  theme={null}
<Response>
    <Dial timeout="15" action="/dial-status/">
        <Number>+14155551111</Number>
    </Dial>
    <Dial timeout="15" action="/dial-status/">
        <Number>+14155552222</Number>
    </Dial>
    <Speak>Sorry, no one is available. Please try again later.</Speak>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()

  # First attempt
  dial1 = plivoxml.DialElement(timeout=15, action='/dial-status/')
  dial1.add(plivoxml.NumberElement('+14155551111'))
  response.add(dial1)

  # Second attempt
  dial2 = plivoxml.DialElement(timeout=15, action='/dial-status/')
  dial2.add(plivoxml.NumberElement('+14155552222'))
  response.add(dial2)

  response.add(plivoxml.SpeakElement('Sorry, no one is available.'))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();

  const dial1 = response.addDial({ timeout: 15, action: '/dial-status/' });
  dial1.addNumber('+14155551111');

  const dial2 = response.addDial({ timeout: 15, action: '/dial-status/' });
  dial2.addNumber('+14155552222');

  response.addSpeak('Sorry, no one is available.');
  console.log(response.toXML());
  ```
</CodeGroup>

### Dial with Confirmation

Require the called party to press a key to accept:

```xml  theme={null}
<Response>
    <Dial confirmSound="https://example.com/confirm.xml" confirmKey="1">
        <Number>+14155551234</Number>
    </Dial>
</Response>
```

The `confirmSound` URL should return XML like:

```xml  theme={null}
<Response>
    <Speak>Press 1 to accept this call.</Speak>
</Response>
```

### Custom Caller ID

```xml  theme={null}
<Response>
    <Dial callerId="+14155559999" callerName="Support Team">
        <Number>+14155551234</Number>
    </Dial>
</Response>
```

### Custom Ringback

Play custom audio instead of the standard ring:

```xml  theme={null}
<Response>
    <Dial dialMusic="https://example.com/ringback.xml">
        <Number>+14155551234</Number>
    </Dial>
</Response>
```

Use `dialMusic="real"` to play the actual ringtone from the carrier.

### Dial Extensions

Send DTMF tones after the call connects (useful for extensions):

```xml  theme={null}
<Response>
    <Dial>
        <Number sendDigits="wwww1234">+14155551234</Number>
    </Dial>
</Response>
```

Each `w` adds a 0.5-second pause. This example waits 2 seconds, then dials extension 1234.

### Dial Action URL Parameters

When the dial completes, these parameters are sent to the `action` URL:

| Parameter         | Description                                                     |
| ----------------- | --------------------------------------------------------------- |
| `DialStatus`      | `completed`, `busy`, `failed`, `cancel`, `timeout`, `no-answer` |
| `DialRingStatus`  | `true` or `false` - whether the call rang                       |
| `DialHangupCause` | Standard telephony hangup cause                                 |
| `DialALegUUID`    | Call UUID of the A-leg (original caller)                        |
| `DialBLegUUID`    | Call UUID of the B-leg (empty if not answered)                  |

### Dial Callback URL Parameters

Real-time events sent to `callbackUrl`:

| Parameter                 | Description                               |
| ------------------------- | ----------------------------------------- |
| `DialAction`              | `answer`, `connected`, `hangup`, `digits` |
| `DialBLegStatus`          | B-leg status                              |
| `DialALegUUID`            | A-leg call UUID                           |
| `DialBLegUUID`            | B-leg call UUID                           |
| `DialBLegDuration`        | Call duration (on hangup)                 |
| `DialBLegBillDuration`    | Billed duration (on hangup)               |
| `DialBLegFrom`            | B-leg caller number                       |
| `DialBLegTo`              | B-leg destination                         |
| `DialDigitsMatch`         | Matched DTMF digits                       |
| `DialDigitsPressedBy`     | `ALeg` or `BLeg`                          |
| `DialBLegHangupCauseName` | Hangup reason                             |
| `DialBLegHangupCauseCode` | Hangup code                               |
| `DialBLegHangupSource`    | Who hung up                               |
| `STIRVerification`        | STIR/SHAKEN attestation                   |

### Dial to SIP

```xml  theme={null}
<Response>
    <Dial>
        <User>sip:alice@sip.example.com</User>
    </Dial>
</Response>
```

***

## Redirect

The `<Redirect>` element transfers call execution to a different URL. Plivo fetches new XML instructions from the specified URL and continues the call.

### Basic Usage

```xml  theme={null}
<Response>
    <Redirect>https://example.com/new-flow/</Redirect>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.RedirectElement('https://example.com/new-flow/'))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addRedirect('https://example.com/new-flow/');
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addRedirect('https://example.com/new-flow/')
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addRedirect('https://example.com/new-flow/');
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;

  Response response = new Response()
      .children(new Redirect("https://example.com/new-flow/"));
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  response.AddRedirect("https://example.com/new-flow/");
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.RedirectElement).SetContents("https://example.com/new-flow/"),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### Redirect Attributes

| Attribute | Type   | Default | Description                        |
| --------- | ------ | ------- | ---------------------------------- |
| `method`  | string | `POST`  | HTTP method to use (`GET`, `POST`) |

### Dynamic Routing

Redirect based on conditions:

```python  theme={null}
@app.route('/route-call/', methods=['POST'])
def route_call():
    caller = request.form.get('From')
    response = plivoxml.ResponseElement()

    # VIP callers get priority queue
    if is_vip(caller):
        response.add(plivoxml.RedirectElement('https://example.com/vip-queue/'))
    else:
        response.add(plivoxml.RedirectElement('https://example.com/standard-queue/'))

    return Response(response.to_string(), mimetype='application/xml')
```

### After Dial Failure

Redirect when a dial attempt fails:

```xml  theme={null}
<Response>
    <Dial timeout="20">
        <Number>+14155551234</Number>
    </Dial>
    <Redirect>https://example.com/voicemail/</Redirect>
</Response>
```

If the dial fails or times out, the call redirects to voicemail.

### Conditional IVR Flow

```xml  theme={null}
<Response>
    <GetDigits action="https://example.com/ivr-choice/" numDigits="1">
        <Speak>Press 1 for English, press 2 for Spanish.</Speak>
    </GetDigits>
    <Redirect>https://example.com/ivr-timeout/</Redirect>
</Response>
```

### Menu Loop

Create a menu that returns to itself:

```python  theme={null}
@app.route('/main-menu/', methods=['POST'])
def main_menu():
    digits = request.form.get('Digits', '')
    response = plivoxml.ResponseElement()

    if digits == '1':
        response.add(plivoxml.RedirectElement('https://example.com/sales/'))
    elif digits == '2':
        response.add(plivoxml.RedirectElement('https://example.com/support/'))
    elif digits == '9':
        # Repeat menu
        getdigits = plivoxml.GetDigitsElement(
            action='https://example.com/main-menu/',
            numDigits=1
        )
        getdigits.add(plivoxml.SpeakElement('Press 1 for sales, 2 for support, 9 to repeat.'))
        response.add(getdigits)
        response.add(plivoxml.RedirectElement('https://example.com/main-menu/'))
    else:
        response.add(plivoxml.SpeakElement('Invalid option.'))
        response.add(plivoxml.RedirectElement('https://example.com/main-menu/'))

    return Response(response.to_string(), mimetype='application/xml')
```

### Redirect with GET Method

```xml  theme={null}
<Response>
    <Redirect method="GET">https://example.com/next-step/?lang=en</Redirect>
</Response>
```

### Redirect Request Parameters

When Plivo calls the redirect URL, it includes all standard [request parameters](/voice/xml/overview/#request-parameters):

| Parameter    | Description             |
| ------------ | ----------------------- |
| `CallUUID`   | Unique call identifier  |
| `From`       | Caller's number         |
| `To`         | Called number           |
| `CallStatus` | Current call status     |
| `Direction`  | `inbound` or `outbound` |

### Redirect Best Practices

1. **Avoid infinite loops** - Ensure redirects eventually lead to an endpoint that doesn't redirect
2. **Handle errors** - Your redirect URL should always return valid XML
3. **Use HTTPS** - All URLs should use HTTPS
4. **Pass context** - Use query parameters to pass state between endpoints

***

## Hangup

The `<Hangup>` element terminates the current call. Use it to gracefully end calls after completing a flow.

### Basic Usage

```xml  theme={null}
<Response>
    <Speak>Thank you for calling. Goodbye!</Speak>
    <Hangup/>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.SpeakElement('Thank you for calling. Goodbye!'))
  response.add(plivoxml.HangupElement())
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addSpeak('Thank you for calling. Goodbye!');
  response.addHangup();
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addSpeak('Thank you for calling. Goodbye!')
  response.addHangup()
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addSpeak('Thank you for calling. Goodbye!');
  $response->addHangup();
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;

  Response response = new Response()
      .children(
          new Speak("Thank you for calling. Goodbye!"),
          new Hangup()
      );
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  response.AddSpeak("Thank you for calling. Goodbye!");
  response.AddHangup();
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.SpeakElement).AddSpeak("Thank you for calling. Goodbye!"),
              new(xml.HangupElement),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### Hangup Attributes

| Attribute  | Type    | Default | Description                       |
| ---------- | ------- | ------- | --------------------------------- |
| `reason`   | string  | -       | Hangup reason: `rejected`, `busy` |
| `schedule` | integer | -       | Seconds to wait before hanging up |

### Scheduled Hangup

End the call after a delay:

```xml  theme={null}
<Response>
    <Speak>This call will end in 60 seconds.</Speak>
    <Hangup schedule="60"/>
    <Play loop="0">https://example.com/hold-music.mp3</Play>
</Response>
```

This schedules a hangup while continuing to execute subsequent elements.

### Reject with Reason

Provide a hangup reason to simulate different call states:

```xml  theme={null}
<Response>
    <Hangup reason="busy"/>
</Response>
```

| Reason     | Effect                      |
| ---------- | --------------------------- |
| `rejected` | Caller hears rejection tone |
| `busy`     | Caller hears busy signal    |

### After IVR Timeout

```xml  theme={null}
<Response>
    <GetDigits action="/handle-input/" numDigits="1" timeout="10" retries="2">
        <Speak>Press 1 to continue.</Speak>
    </GetDigits>
    <Speak>We didn't receive any input. Goodbye.</Speak>
    <Hangup/>
</Response>
```

### After Business Hours

```python  theme={null}
@app.route('/answer/', methods=['POST'])
def answer():
    response = plivoxml.ResponseElement()

    if not is_business_hours():
        response.add(plivoxml.SpeakElement(
            'Our office is currently closed. Please call back during business hours.'
        ))
        response.add(plivoxml.HangupElement())
    else:
        response.add(plivoxml.SpeakElement('Welcome! Please hold.'))
        dial = plivoxml.DialElement()
        dial.add(plivoxml.NumberElement('+14155551234'))
        response.add(dial)

    return Response(response.to_string(), mimetype='application/xml')
```

### Block Spam Callers

```python  theme={null}
@app.route('/answer/', methods=['POST'])
def answer():
    caller = request.form.get('From')
    response = plivoxml.ResponseElement()

    if is_blocked(caller):
        response.add(plivoxml.HangupElement(reason='rejected'))
    else:
        response.add(plivoxml.SpeakElement('Hello! How can I help you?'))
        # Continue with normal flow

    return Response(response.to_string(), mimetype='application/xml')
```

### Implicit Hangup

If your XML doesn't end with `<Hangup>`, the call automatically ends when all elements are executed. However, it's good practice to include it explicitly for clarity.

***

## Wait

The `<Wait>` element pauses call execution for a specified duration. Use it for hold times, delays, or with answering machine detection.

### Basic Usage

```xml  theme={null}
<Response>
    <Speak>Please hold while we connect you.</Speak>
    <Wait length="5"/>
    <Speak>Thank you for waiting.</Speak>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  response.add(plivoxml.SpeakElement('Please hold while we connect you.'))
  response.add(plivoxml.WaitElement(length=5))
  response.add(plivoxml.SpeakElement('Thank you for waiting.'))
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  response.addSpeak('Please hold while we connect you.');
  response.addWait({ length: 5 });
  response.addSpeak('Thank you for waiting.');
  console.log(response.toXML());
  ```

  ```ruby Ruby theme={null}
  require 'plivo'

  include Plivo::XML

  response = Response.new
  response.addSpeak('Please hold while we connect you.')
  response.addWait(length: 5)
  response.addSpeak('Thank you for waiting.')
  puts PlivoXML.new(response).to_xml
  ```

  ```php PHP theme={null}
  <?php
  require 'vendor/autoload.php';
  use Plivo\XML\Response;

  $response = new Response();
  $response->addSpeak('Please hold while we connect you.');
  $response->addWait(['length' => 5]);
  $response->addSpeak('Thank you for waiting.');
  echo $response->toXML();
  ```

  ```java Java theme={null}
  import com.plivo.api.xml.*;

  Response response = new Response()
      .children(
          new Speak("Please hold while we connect you."),
          new Wait().length(5),
          new Speak("Thank you for waiting.")
      );
  System.out.println(response.toXmlString());
  ```

  ```csharp .NET theme={null}
  using Plivo.XML;

  var response = new Response();
  response.AddSpeak("Please hold while we connect you.");
  response.AddWait(new Dictionary<string, string>() { {"length", "5"} });
  response.AddSpeak("Thank you for waiting.");
  Console.WriteLine(response.ToString());
  ```

  ```go Go theme={null}
  package main

  import "github.com/plivo/plivo-go/v7/xml"

  func main() {
      response := xml.ResponseElement{
          Contents: []interface{}{
              new(xml.SpeakElement).AddSpeak("Please hold."),
              new(xml.WaitElement).Length(5),
              new(xml.SpeakElement).AddSpeak("Thank you for waiting."),
          },
      }
      print(response.String())
  }
  ```
</CodeGroup>

### Wait Attributes

| Attribute    | Type    | Default | Description                             |
| ------------ | ------- | ------- | --------------------------------------- |
| `length`     | integer | `1`     | Seconds to wait                         |
| `silence`    | boolean | `false` | Play silence (vs default hold music)    |
| `minSilence` | integer | -       | Minimum silence milliseconds to detect  |
| `beep`       | string  | -       | Detect beeps: `true` or beep parameters |

### Silent Wait

By default, `<Wait>` plays hold music. For silence:

```xml  theme={null}
<Response>
    <Wait length="10" silence="true"/>
</Response>
```

### Delayed Call Answer

Use `<Wait>` to delay answering (useful for screening):

```xml  theme={null}
<Response>
    <Wait length="3"/>
    <Speak>Hello, you've reached Acme Corp.</Speak>
</Response>
```

### Answering Machine Detection

Detect answering machines by listening for beeps:

```xml  theme={null}
<Response>
    <Wait length="10" beep="true"/>
    <Speak>Hello, this is an automated message from Acme Corp.</Speak>
</Response>
```

#### Beep Detection Parameters

For fine-grained control, pass beep parameters as a comma-separated string:

```xml  theme={null}
<Wait beep="duration=300,inter_silence=50,intra_silence=500,threshold=256"/>
```

| Parameter       | Default | Description                        |
| --------------- | ------- | ---------------------------------- |
| `duration`      | 300     | Beep duration in ms to match       |
| `inter_silence` | 50      | Silence between beeps (ms)         |
| `intra_silence` | 500     | Silence after beep to confirm (ms) |
| `threshold`     | 256     | Audio level threshold              |

### Silence Detection

Detect when the other party stops speaking:

```xml  theme={null}
<Response>
    <Wait length="30" silence="true" minSilence="1000"/>
    <Speak>It seems like you're done speaking.</Speak>
</Response>
```

`minSilence` is the minimum silence duration in milliseconds to trigger detection.

### Machine Detection Flow

Combine with `<Speak>` for voicemail drops:

```xml  theme={null}
<Response>
    <Wait length="5" beep="true"/>
    <Speak>
        Hello, this is a reminder from Dr. Smith's office
        about your appointment tomorrow at 2 PM.
        Please call us at 555-1234 to confirm.
    </Speak>
</Response>
```

### Use in PreAnswer

Delay before answering the call:

```xml  theme={null}
<Response>
    <PreAnswer>
        <Wait length="2"/>
        <Play>https://example.com/ring.mp3</Play>
    </PreAnswer>
    <Speak>Hello, thank you for calling.</Speak>
</Response>
```

***

## PreAnswer

The `<PreAnswer>` element plays audio to the caller before the call is answered. This is useful for custom ringback tones or screening calls. The caller is not billed during this phase.

### Basic Usage

```xml  theme={null}
<Response>
    <PreAnswer>
        <Speak>Please wait while we connect your call.</Speak>
    </PreAnswer>
    <Dial>
        <Number>+14155551234</Number>
    </Dial>
</Response>
```

<CodeGroup>
  ```python Python theme={null}
  from plivo import plivoxml

  response = plivoxml.ResponseElement()
  preanswer = plivoxml.PreAnswerElement()
  preanswer.add(plivoxml.SpeakElement('Please wait while we connect your call.'))
  response.add(preanswer)
  dial = plivoxml.DialElement()
  dial.add(plivoxml.NumberElement('+14155551234'))
  response.add(dial)
  print(response.to_string())
  ```

  ```javascript Node.js theme={null}
  const plivo = require('plivo');

  const response = plivo.Response();
  const preanswer = response.addPreAnswer();
  preanswer.addSpeak('Please wait while we connect your call.');
  const dial = response.addDial();
  dial.addNumber('+14155551234');
  console.log(response.toXML());
  ```
</CodeGroup>

### Nested Elements

`<PreAnswer>` can contain:

* `<Speak>` - Text-to-speech messages
* `<Play>` - Audio files
* `<Wait>` - Pauses

### Custom Ringback

Play music while connecting:

```xml  theme={null}
<Response>
    <PreAnswer>
        <Play loop="0">https://example.com/custom-ringback.mp3</Play>
    </PreAnswer>
    <Dial>
        <Number>+14155551234</Number>
    </Dial>
</Response>
```

### Use Cases

| Use Case        | Description                                  |
| --------------- | -------------------------------------------- |
| Custom ringback | Replace standard ring with music or branding |
| Legal notices   | "This call may be recorded" disclaimers      |
| Spam screening  | Delay answering to deter robocalls           |
| Queue position  | "You are caller number 3" before answering   |

### Limitations

* Only `Speak`, `Play`, and `Wait` elements are allowed
* Call is not "answered" during PreAnswer, so some carriers may timeout
* Recommended to keep PreAnswer duration under 30 seconds

***

## Related

* [Audio Output](/voice/xml/audio-output/) - Speak, Play, DTMF
* [Input Collection](/voice/xml/input/) - GetDigits, GetInput
* [Conferencing](/voice/xml/conferencing/) - Conference, MultiPartyCall
* [Audio Streaming](/voice/xml/audio-streaming/) - Stream real-time audio
