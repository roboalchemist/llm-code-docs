Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ModalView

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ModalView

# Interface: ModalView

Defined in: packages/types/dist/views.d.ts:26

## Extends {#extends}

* `BaseView`

## Properties {#properties}

### blocks {#blocks}

```text
blocks: AnyBlock[];
```text

Defined in: packages/types/dist/views.d.ts:5

#### Description {#description}

An array of [AnyBlock](/tools/node-slack-sdk/reference/web-api/type-aliases/AnyBlock) that defines the content of the view. Max of 100 blocks.

#### Inherited from {#inherited-from}

```text
BaseView.blocks
```text

* * *

### callback_id? {#callback_id}

```text
optional callback_id: string;
```text

Defined in: packages/types/dist/views.d.ts:18

#### Description {#description-1}

An identifier to recognize interactions and submissions of this particular view. Don't use this to store sensitive information (use `private_metadata` instead). Maximum length of 255 characters.

#### See {#see}

[Handling and responding to interactions](https://docs.slack.dev/surfaces/modals#interactions).

#### Inherited from {#inherited-from-1}

```text
BaseView.callback_id
```text

* * *

### clear_on_close? {#clear_on_close}

```text
optional clear_on_close: boolean;
```text

Defined in: packages/types/dist/views.d.ts:49

#### Description {#description-2}

When set to `true`, clicking on the close button will clear all views in a modal and close it. Defaults to `false`.

* * *

### close? {#close}

```text
optional close: PlainTextElement;
```text

Defined in: packages/types/dist/views.d.ts:38

#### Description {#description-3}

An optional [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) that defines the text displayed in the close button at the bottom-right of the view. Maximum length of 24 characters.

* * *

### external_id? {#external_id}

```text
optional external_id: string;
```text

Defined in: packages/types/dist/views.d.ts:20

#### Description {#description-4}

A custom identifier that must be unique for all views on a per-team basis.

#### Inherited from {#inherited-from-2}

```text
BaseView.external_id
```text

* * *

### notify_on_close? {#notify_on_close}

```text
optional notify_on_close: boolean;
```text

Defined in: packages/types/dist/views.d.ts:55

#### Description {#description-5}

Indicates whether Slack will send your app a [\`view\_closed\`](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_closed) event when a user clicks the close button. Defaults to `false`.

* * *

### private_metadata? {#private_metadata}

```text
optional private_metadata: string;
```text

Defined in: packages/types/dist/views.d.ts:12

#### Description {#description-6}

String that will be sent to your app in [\`view\_submission\`](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_submission) and [\`block\_actions\`](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload) events. Maximum length of 3000 characters.

#### Inherited from {#inherited-from-3}

```text
BaseView.private_metadata
```text

* * *

### submit? {#submit}

```text
optional submit: PlainTextElement;
```text

Defined in: packages/types/dist/views.d.ts:44

#### Description {#description-7}

An optional [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) that defines the text displayed in the submit button at the bottom-right of the view. `submit` is required when an input block is within the `blocks` array. Max length of 24 characters.

* * *

### title {#title}

```text
title: PlainTextElement;
```text

Defined in: packages/types/dist/views.d.ts:33

#### Description {#description-8}

The title that appears in the top-left of the modal. Must be a [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) with a maximum length of 24 characters.

* * *

### type {#type}

```text
type: "modal";
```text

Defined in: packages/types/dist/views.d.ts:28

#### Description {#description-9}

The type of view. Set to `modal` for modals.
