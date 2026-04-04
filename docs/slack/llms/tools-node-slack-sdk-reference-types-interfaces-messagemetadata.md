Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/MessageMetadata

[@slack/types](/tools/node-slack-sdk/reference/types/) / MessageMetadata

# Interface: MessageMetadata

Defined in: [message-metadata.ts:12](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L12)

## Description {#description}

Application-specific event data to attach to a Slack message.

## See {#see}

* [Using Metadata](https://docs.slack.dev/messaging/message-metadata)
* [Metadata Payload Structure](https://docs.slack.dev/messaging/message-metadata)

## Properties {#properties}

### event_payload {#event_payload}

```
event_payload: object;
```

Defined in: [message-metadata.ts:21](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L21)

#### Index Signature {#index-signature}

```
[key: string]:   | string  | number  | boolean  | MessageMetadataEventPayloadObject  | MessageMetadataEventPayloadObject[]
```

#### Description {#description-1}

A free-form object containing whatever data your application wishes to attach to messages.

* * *

### event_type {#event_type}

```
event_type: string;
```

Defined in: [message-metadata.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L17)

#### Description {#description-2}

A human readable alphanumeric string representing your application's metadata event. The value of this field may appear in the UI to developers.
