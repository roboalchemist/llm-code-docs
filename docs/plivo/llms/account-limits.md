# Source: https://plivo.com/docs/voice/concepts/account-limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Account and feature limits

> Default rate limits, CPS caps, and concurrent call thresholds

The Plivo features and components mentioned here have default limits. You can change them through our APIs or XML, or by contacting us.

## Understanding CPS vs Concurrent Calls

Two important concepts for voice call capacity:

| Term                       | Definition                                    |
| -------------------------- | --------------------------------------------- |
| **CPS (Calls Per Second)** | Rate at which new calls can be initiated      |
| **Concurrent Calls**       | Total number of calls active at the same time |

<Note>
  **Key difference:** CPS limits how fast you can *start* calls. Concurrent calls is how many calls can be *active simultaneously*.
</Note>

### Global (outside India)

| Limit Type           | Default      | Notes                 |
| -------------------- | ------------ | --------------------- |
| Outbound CPS         | 2            | Can be increased      |
| Inbound CPS          | 10           | Can be increased      |
| **Concurrent Calls** | **No limit** | Only CPS limits apply |

### India

India has additional concurrency limits:

| Limit Type           | Calculation  | Example                         |
| -------------------- | ------------ | ------------------------------- |
| Outbound CPS         | Default: 2   | —                               |
| **Concurrent Calls** | **CPS × 25** | 2 CPS = 50 concurrent calls max |

<Warning>
  **India-specific:** If your account has 2 CPS for India, you can have a maximum of 50 concurrent calls (2 × 25). To increase concurrent call capacity for India, you must increase your CPS allocation.
</Warning>

To increase CPS limits, contact [Plivo Sales](https://www.plivo.com/contact/sales/).

***

### Outbound Call API limits

By default, all accounts come with a limit of two calls per second. All outbound Call API requests are queued upon acceptance, then dequeued and initiated as per the calls per second (CPS) configured for your Plivo account.

### SIP/browser calls and inbound calls to Plivo numbers

Inbound CPS refers to the limitation on outbound calls from SIP and browser clients and inbound calls to Plivo numbers. (These are all called Inbound CPS because outgoing call requests from SIP and browser clients are also inbound requests to Plivo.) The default Inbound CPS limit is 10.

Here are three scenarios that show how Inbound CPS limits might apply. In all three, only 10 calls per second will be processed; the rest will be rejected.

**Scenario 1**

Outbound SIP/browser calls: 11 calls<br />Inbound calls to Plivo numbers: 0 calls

**Scenario 2**

Outbound SIP/browser calls: 0 calls<br />Inbound calls to Plivo numbers: 11 calls

**Scenario 3**

Outbound SIP/browser calls: 5 calls<br />Inbound calls to Plivo numbers: 6 calls

### Make-call API limits

By default, Plivo limits all accounts to 300 API requests per five seconds. This limit is for below APIs:

* Make an Outbound Call API
* Add a Participant to a multiparty call using API

If you send more requests than the specified limit in the specified duration, Plivo will block the requests and respond with the HTTP error *429 Too Many Requests*. If you see this error, throttle your API requests and retry

### Non-call API limits

By default, Plivo limits all accounts to 300 API requests per five seconds. This limit is for all APIs excluding those that initiate a call:

* All Call APIs (except “initiate a call”)
* All Recording APIs
* All Conference APIs
* All Endpoint APIs
* All Application APIs

If you send more non-call requests than the specified limit in the specified duration, Plivo will block the requests and respond with the HTTP error *429 Too Many Requests*. If you see this error, throttle your API requests and retry.

**Note:** You can increase your account’s CPS or the rate of non-call API requests, but because doing so incurs extra costs on the part of carriers and server providers, Plivo requires a minimum commitment, the level of which depends on the rate of calls per second or non-call API requests you want. Please [contact our sales team](https://www.plivo.com/contact/sales/) to discuss your situation.

## Feature-level limits

In addition to the account-level limits, Plivo has some feature-level limits.

### Time limit for calls

The default maximum duration for outbound and inbound calls connected using [Make a Call API](/voice/api/calls/#make-a-call) and [Dial XML](/voice/xml/routing#dial) is four hours starting from the time a call is answered. You can extend the limit to 86,400 seconds (24 hours).

### Call recordings

By default, the maximum duration for call recordings is 60 seconds. For calls that you record using [Record API](/voice/api/recordings) or [Record XML](/voice/xml/record/), the maximum recording duration is 24 hours.

### Conference calls

Two limits have to do with conference calls.

* **Participants**: You can have a maximum of 20 participants in a conference room. You can set the maxMembers to be between 1 to 20.
* **Duration**: The maximum duration for a conference is 86,400 seconds (24 hours). A conference call will get disconnected after 24 hours.

Refer to the [Conference XML element](/voice/xml/conferencing) reference page for details.

### Voice transcriptions

You can transcribe a call using the [Record API](/voice/api/recordings), [Record Conference API](/voice/api/recordings), [Record XML](/voice/xml/record/), and [Conference XML](/voice/xml/conferencing).

* **Duration**: Our transcription service is limited to calls with a duration greater than 5 seconds and less than four hours.
* **Recording file size**: The maximum recording file size is 2GB.
