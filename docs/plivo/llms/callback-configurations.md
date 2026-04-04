# Source: https://plivo.com/docs/voice/concepts/callback-configurations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Callback Configurations

> Configure webhook URLs and HTTP methods for voice call event notifications

Plivo sends HTTP webhooks as callbacks during different states of a call and to many URLs, such as answer\_url, fallback\_url, hangup\_url, action, and callback\_url. To enable users to optimize for lower latency and build fault tolerance into webhook interactions, Plivo offers optional parameters that let developers configure timeouts (the timeframe Plivo has to wait to receive a response from your application server), retry policy, and edge region from which the webhook request is sent to the URL. Regions correspond to Plivo points of presence (PoP). See [SIP Trunking FAQ](/faq/voice-api-and-SIP-trunking/sip-trunking#data-centers) for details on Plivo's global data center locations.

## Callback retry scenarios

Having the ability to configure callback retries and timeouts improves reliability and event recovery by letting you:

* Configure a custom timeout based on your use case.
* Set higher timeouts during network problems on your application server.
* Set shorter timeouts during an outage on your application server to ensure faster failover to your fallback URL.
* Enable retries during client-side service interruptions and delays.

## Configuration mechanism

To set callback configurations for any given URL (answer\_url, fallback\_url, , ring\_url, etc.), you need to append configuration parameters to it in the form of URL extensions (or ”[fragments](https://en.wikipedia.org/wiki/Fragment_identifier)”) as key-value pairs.

* The first key-value pair should start with #
* Key and value should be separated by =
* Key-value pairs should be separated by &

For example:

```url  theme={null}
https://example.com/answer_url?query=123#param1=2500&param2=5500
```

<Note>
  <strong>Note:</strong> If you don’t append any parameters, the default values from the tables below will apply.
</Note>

## Timeouts

When Plivo sends an HTTP callback to your webhook URLs during events, you should capture the request (POST or GET based on the type you’ve defined for the URL) and respond with a 200 OK response. When you process the callback, you can store the data in your database.

Plivo automatically retries webhooks for a certain timeframe if an HTTP 200 status code is not returned. The timeframe Plivo has to wait to receive a response from your application server is called a timeout. This table shows the allowed and default timeouts available for webhook URLs.

| Parameter | Name               | Description                                                                                                                                                     | Allowed Values | Default |
| --------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------- |
| ct        | Connection timeout | The time in milliseconds (ms) for Plivo to wait while establishing a TCP connection                                                                             | 100 – 10000    | 2000    |
| rt        | Read timeout       | The time in milliseconds for Plivo to wait:<br /><br />— to start receiving a response after sending the initial request<br /><br />— for delay between packets | 100 – 40000    | 40000   |
| tt        | Total timeout      | Upper limit on total time allowed for all timeouts, including retries on a given URL (not including fallback URL)                                               | 100 – 55000    | 55000   |

### Examples

1. [https://example.com/answer\_url?query=123#ct=2000](https://example.com/answer_url?query=123#ct=2000)<br />*Connection timeout of two seconds*

2. [https://example.com/answer\_url?query=123#ct=2000\&rt=3000](https://example.com/answer_url?query=123#ct=2000\&rt=3000)<br />*Connection timeout of two seconds and a read timeout of three seconds*

## Retries

Plivo lets you configure the number of retries it makes for different webhook URLs and the policy it should use depending on HTTP failure status codes.

| Param | Name         | Description                                                                                                                                                                                                                                                                                          | Allowed Values                                         | Default |
| ----- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------- |
| rc    | Retry count  | Number of retry attempts to be made to the same URL if the initial connection fails (not including to fallback URL)                                                                                                                                                                                  | 0 – 5                                                  | 1       |
| rp    | Retry policy | Type of failure to retry on:<br /><br />**4xx** → only on 4xx responses<br /><br />**5xx** → only on 5xx responses<br /><br />**ct** → TCP/TLS connection failures within the connection timeout<br /><br />**rt** → no response received within the read timeout<br /><br />**all** → all the above | Comma-separated list of values — for example, rp=ct,rt | ct,rt   |

<Note>
  <strong>Note:</strong> If a partial response is received from your app server, Plivo will not make a retry attempt.
</Note>

### Examples

1. [https://example.com/answer\_url?query=123#rt=3000\&rp=ct,rt](https://example.com/answer_url?query=123#rt=3000\&rp=ct,rt)<br />*Retry on both connect and read timeout, and reduce the read timeout to three seconds.*

2. [https://example.com/answer\_url?query=123#rc=3\&ct=2000](https://example.com/answer_url?query=123#rc=3\&ct=2000)<br />*Retry on connection failure, but with a two-second connection timeout. If there is no connection in two seconds, retry three times, for a total of four attempts to connect.*

## Edge Region

An edge region is the geographical region from which Plivo initiates an HTTP webhook to the answer\_url, fallback\_url, hangup\_url, action, or callback\_url URLs. Plivo maintains edge clusters in four regions:

* North California (United states)
* North Virginia (United States)
* Frankfurt (Germany)
* Singapore
* Mumbai (India)

To ensure minimum latency, Plivo automatically chooses the nearest region for all callbacks we initiate, but developers can configure the region for each URL using the `er` parameter:

| Param | Name        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Allowed Values                                                                                                                       | Default |
| ----- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| er    | Edge Region | Specifies the edge region where webhooks get initiated from. This parameter needs to be either a selection strategy or a specific region.<br /><u>Region Selection Strategies:</u><br />**nearest** → selects the region geographically closest to the location of the URL.<br />**local** → selects the same region as the media server where the call media is hosted.<br /><u>Specific region:</u><br />n\_california, n\_virginia, frankfurt, singapore, mumbai | <ul><li>nearest</li><li>local</li><li>n\_california</li><li>n\_virginia</li><li>frankfurt</li><li>singapore</li><li>mumbai</li></ul> | nearest |

### Examples

1. [https://example.com/answer\_url?query=123#er=n\_california](https://example.com/answer_url?query=123#er=n_california)<br />*The HTTP webhook to this URL from Plivo will be initiated from Plivo’s North California edge region.*

2. [https://example.com/answer\_url?query=123#er=nearest](https://example.com/answer_url?query=123#er=nearest)<br />*The HTTP webhook to this URL from Plivo will be initiated from the Plivo’s edge region that is nearest to the location of the URL.*

## Applicable URLs

Callback retries apply to this list of URLs associated with Plivo’s [Voice applications on the console](https://cx.plivo.com/xml-applications), API requests, and XML elements:

### Voice applications on console

* Primary Answer URL
* Fallback Answer URL
* Hangup URL

### API

[Make a call](/voice/api/calls/#make-a-call):

* answer\_url
* ring\_url
* hangup\_url
* fallback\_url
* machine\_detection\_url

[Transfer a call](/voice/api/calls/#transfer-a-call):

* aleg\_url
* bleg\_url

[Record a call](/voice/api/recordings):

* transcription\_url
* callback\_url

[Record a conference](/voice/api/recordings):

* transcription\_url
* callback\_url

### XML

[Dial](/voice/xml/routing#dial):

* action
* confirmSound
* dialMusic
* callbackUrl

[Conference](/voice/xml/conferencing):

* action
* callbackUrl
* waitSound

[GetInput](/voice/xml/input#getinput):

* action
* interimSpeechResultsCallback

[GetDigits](/voice/xml/input#getdigits):

* action

[Record](/voice/xml/record/):

* action
* transcriptionUrl
* callbackUrl

[Redirect](/voice/xml/routing#redirect)

## Inapplicable URLs

Callback retry parameters don’t apply to any of these audio URLs:

### API

[Play audio on a call](/voice/api/calls#play-audio)<br />[Play audio to a conference member](/voice/api/conferences#play-audio-to-member)

### XML

[PreAnswer XML](/voice/xml/routing#preanswer)<br />[Play XML](/voice/xml/audio-output#play)

These URLs use our standard configuration values:

* Connection timeout: 2 seconds
* Read timeout: 120 seconds
* Retry count: 1
* Retry policy: all
