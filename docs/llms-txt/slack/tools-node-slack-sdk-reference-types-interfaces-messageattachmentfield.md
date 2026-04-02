Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/MessageAttachmentField

[@slack/types](/tools/node-slack-sdk/reference/types/) / MessageAttachmentField

# Interface: MessageAttachmentField

Defined in: [message-attachments.ts:124](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-attachments.ts#L124)

## Description {#description}

A field object to include in a [MessageAttachment](/tools/node-slack-sdk/reference/types/interfaces/MessageAttachment).

## See {#see}

[Field objects reference](https://docs.slack.dev/messaging/formatting-message-text#attachments).

## Properties {#properties}

### short? {#short}

```
optional short: boolean;
```

Defined in: [message-attachments.ts:138](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-attachments.ts#L138)

#### Description {#description-1}

Indicates whether the field object is short enough to be displayed side-by-side with other field objects. Defaults to `false`.

* * *

### title {#title}

```
title: string;
```

Defined in: [message-attachments.ts:129](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-attachments.ts#L129)

#### Description {#description-2}

Shown as a bold heading displayed in the field object. It cannot contain markup and will be escaped for you.

* * *

### value {#value}

```
value: string;
```

Defined in: [message-attachments.ts:133](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-attachments.ts#L133)

#### Description {#description-3}

The text value displayed in the field object. It can be formatted as plain text, or with [\`mrkdwn\`](https://docs.slack.dev/messaging/formatting-message-text) by using the `mrkdwn_in` option of [MessageAttachment](/tools/node-slack-sdk/reference/types/interfaces/MessageAttachment).
