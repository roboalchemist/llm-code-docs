Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/HomeView

[@slack/types](/tools/node-slack-sdk/reference/types/) / HomeView

# Interface: HomeView

Defined in: [views.ts:25](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L25)

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

### external_id? {#external_id}

```
optional external_id: string;
```

Defined in: [views.ts:21](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L21)

#### Description {#description-2}

A custom identifier that must be unique for all views on a per-team basis.

#### Inherited from {#inherited-from-2}

```
BaseView.external_id
```

* * *

### private_metadata? {#private_metadata}

```
optional private_metadata: string;
```

Defined in: [views.ts:13](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L13)

#### Description {#description-3}

String that will be sent to your app in [\`view\_submission\`](https://docs.slack.dev/reference/interaction-payloads/view-interactions-payload#view_submission) and [\`block\_actions\`](https://docs.slack.dev/reference/interaction-payloads/block_actions-payload) events. Maximum length of 3000 characters.

#### Inherited from {#inherited-from-3}

```
BaseView.private_metadata
```

* * *

### type {#type}

```
type: "home";
```

Defined in: [views.ts:27](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/views.ts#L27)

#### Description {#description-4}

The type of view. Set to `home` for Home tabs.
