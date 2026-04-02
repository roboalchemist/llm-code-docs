Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/MessageAttachmentField

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / MessageAttachmentField

# Interface: MessageAttachmentField

Defined in: packages/types/dist/message-attachments.d.ts:115

## Description {#description}

A field object to include in a [MessageAttachment](/tools/node-slack-sdk/reference/web-api/interfaces/MessageAttachment).

## See {#see}

[Field objects reference](https://docs.slack.dev/messaging/formatting-message-text#attachments).

## Properties {#properties}

### short? {#short}

```text
optional short: boolean;
```text

Defined in: packages/types/dist/message-attachments.d.ts:129

#### Description {#description-1}

Indicates whether the field object is short enough to be displayed side-by-side with other field objects. Defaults to `false`.

* * *

### title {#title}

```text
title: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:120

#### Description {#description-2}

Shown as a bold heading displayed in the field object. It cannot contain markup and will be escaped for you.

* * *

### value {#value}

```text
value: string;
```text

Defined in: packages/types/dist/message-attachments.d.ts:124

#### Description {#description-3}

The text value displayed in the field object. It can be formatted as plain text, or with [\`mrkdwn\`](https://docs.slack.dev/messaging/formatting-message-text) by using the `mrkdwn_in` option of [MessageAttachment](/tools/node-slack-sdk/reference/web-api/interfaces/MessageAttachment).
