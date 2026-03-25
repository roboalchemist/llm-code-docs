# Source: https://plivo.com/docs/voice/concepts/features.md

# Source: https://plivo.com/docs/messaging/concepts/features.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Supported Features

> These are some of the key features of the Plivo SMS Platform.

## Support for any character set

Built-in support for GSM and Unicode characters allows the use of any language, including Chinese and Arabic, as well as emojis and symbols.

## Message queuing

Send multiple SMS messages in a single API request. Plivo handles the queuing of your messages. This table shows SMS message throttling limits:

<table>
  <tbody>
    <tr>
      <td>Source Number Type</td>
      <td>Destination Country</td>
      <td>Dequeue Rate</td>
    </tr>

    <tr>
      <td>US / Canada 10-digit phone number</td>
      <td>US / Canada</td>
      <td>1 message per 4 seconds</td>
    </tr>

    <tr>
      <td>US / Canada toll-free number</td>
      <td>US / Canada</td>
      <td>40 messages per second</td>
    </tr>

    <tr>
      <td>US / Canada short code</td>
      <td>US / Canada</td>
      <td>100 messages per second</td>
    </tr>

    <tr>
      <td>International number or alpha sender ID</td>
      <td>Other countries</td>
      <td>No limit</td>
    </tr>
  </tbody>
</table>

## Long message concatenation

Plivo’s Message API allows you to send SMS messages that exceed 160 characters in length. Plivo takes care of transmitting long messages with the appropriate metadata to ensure they are delivered as one intact message on the recipient’s handset.

## Delivery report notification

Receive real-time delivery notifications for SMS messages that you send. You can also track delivery rates and review the performance of your account.

## Opt-out handling

Plivo automatically handles SMS opt-out if your Plivo number receives replies with an opt-out keyword. We support these opt-out keywords:

* Stop
* Cancel
* End
* Quit
* Unsubscribe

## SMS data redaction

You can redact sensitive information in both outbound and inbound SMS messages to ensure that sensitive message contents are not stored on Plivo servers or displayed in debug logs.

**Outbound:** To redact the content and destination number of an outbound SMS, set the **log** request parameter of the Send SMS API request to

false.

**Inbound:** Enable this feature from Messaging > [XML](https://cx.plivo.com/xml-applications) on the Plivo console. Click on an application, then, in the Message section, tick Redact Incoming Messages, then click **Apply**.

## Intelligent message encoding

Plivo replaces Unicode characters with similar GSM characters to ensure message delivery to networks that don’t support Unicode.
