Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/ModalView

[@slack/types](/tools/node-slack-sdk/reference/types/) / ModalView

# Interface: ModalView

Defined in: [views.ts:31](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L31)

## Extends {#extends}

* `BaseView`

## Properties {#properties}

### blocks {#blocks}

```
blocks: AnyBlock[];
```

Defined in: [views.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L6)

#### Description {#description}

An array of [AnyBlock](/tools/node-slack-sdk/reference/types/type-aliases/AnyBlock) that defines the content of the view. Max of 100 blocks.

#### Inherited from {#inherited-from}

```
BaseView.blocks
```

* * *

### callback_id? {#callback_id}

```
optional callback_id: string;
```

Defined in: [views.ts:19](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L19)

#### Description {#description-1}

An identifier to recognize interactions and submissions of this particular view. Don't use this to store sensitive information (use `private_metadata` instead). Maximum length of 255 characters.

#### See {#see}

[Handling and responding to interactions](https://docs.slack.dev/surfaces/modals#interactions).

#### Inherited from {#inherited-from-1}

```
BaseView.callback_id
```

* * *

### clear_on_close? {#clear_on_close}

```
optional clear_on_close: boolean;
```

Defined in: [views.ts:54](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L54)

#### Description {#description-2}

When set to `true`, clicking on the close button will clear all views in a modal and close it. Defaults to `false`.

* * *

### close? {#close}

```
optional close: PlainTextElement;
```

Defined in: [views.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L43)

#### Description {#description-3}

An optional [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) that defines the text displayed in the close button at the bottom-right of the view. Maximum length of 24 characters.

* * *

### external_id? {#external_id}

```
optional external_id: string;
```

Defined in: [views.ts:21](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L21)

#### Description {#description-4}

A custom identifier that must be unique for all views on a per-team basis.

#### Inherited from {#inherited-from-2}

```
BaseView.external_id
```

* * *

### notify_on_close? {#notify_on_close}

```
optional notify_on_close: boolean;
```

Defined in: [views.ts:60](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L60)

#### Description {#description-5}

Indicates whether Slack will send your app a [\`view\_closed\`](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_closed) event when a user clicks the close button. Defaults to `false`.

* * *

### private_metadata? {#private_metadata}

```
optional private_metadata: string;
```

Defined in: [views.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L13)

#### Description {#description-6}

String that will be sent to your app in [\`view\_submission\`](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_submission) and [\`block\_actions\`](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload) events. Maximum length of 3000 characters.

#### Inherited from {#inherited-from-3}

```
BaseView.private_metadata
```

* * *

### submit? {#submit}

```
optional submit: PlainTextElement;
```

Defined in: [views.ts:49](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L49)

#### Description {#description-7}

An optional [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) that defines the text displayed in the submit button at the bottom-right of the view. `submit` is required when an input block is within the `blocks` array. Max length of 24 characters.

* * *

### title {#title}

```
title: PlainTextElement;
```

Defined in: [views.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L38)

#### Description {#description-8}

The title that appears in the top-left of the modal. Must be a [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) with a maximum length of 24 characters.

* * *

### type {#type}

```
type: "modal";
```

Defined in: [views.ts:33](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L33)

#### Description {#description-9}

The type of view. Set to `modal` for modals.
