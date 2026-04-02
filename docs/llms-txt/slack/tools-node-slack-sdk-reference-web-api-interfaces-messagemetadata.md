Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MessageMetadata

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MessageMetadata

# Interface: MessageMetadata

Defined in: packages/types/dist/message-metadata.d.ts:7

## Description {#description}

Application-specific event data to attach to a Slack message.

## See {#see}

* [Using Metadata](https://docs.slack.dev/messaging/message-metadata)
* [Metadata Payload Structure](https://docs.slack.dev/messaging/message-metadata)

## Properties {#properties}

### event_payload {#event_payload}

```text
event_payload: object;
```text

Defined in: packages/types/dist/message-metadata.d.ts:16

#### Index Signature {#index-signature}

```text
[key: string]:   | string  | number  | boolean  | MessageMetadataEventPayloadObject  | MessageMetadataEventPayloadObject[]
```text

#### Description {#description-1}

A free-form object containing whatever data your application wishes to attach to messages.

* * *

### event_type {#event_type}

```text
event_type: string;
```text

Defined in: packages/types/dist/message-metadata.d.ts:12

#### Description {#description-2}

A human readable alphanumeric string representing your application's metadata event. The value of this field may appear in the UI to developers.
