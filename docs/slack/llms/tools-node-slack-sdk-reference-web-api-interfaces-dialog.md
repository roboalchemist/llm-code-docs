Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/Dialog

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / Dialog

# Interface: Dialog

Defined in: packages/types/dist/dialog.d.ts:5

Reusable shapes for argument values

## Deprecated {#deprecated}

Dialogs are a deprecated surface in Slack. For more details on how to upgrade, check out our [Upgrading outmoded dialogs to modals guide](https://docs.slack.dev/block-kit/upgrading-outmoded-dialogs-to-modals). This will be removed in the next major version.

## Properties {#properties}

### callback_id {#callback_id}

```text
callback_id: string;
```

Defined in: packages/types/dist/dialog.d.ts:7

* * *

### elements {#elements}

```text
elements: object[];
```

Defined in: packages/types/dist/dialog.d.ts:8

#### data_source? {#data_source}

```text
optional data_source: "channels" | "users" | "conversations" | "external";
```

#### hint? {#hint}

```text
optional hint: string;
```

#### label {#label}

```text
label: string;
```

#### max_length? {#max_length}

```text
optional max_length: number;
```

#### min_length? {#min_length}

```text
optional min_length: number;
```

#### min_query_length? {#min_query_length}

```text
optional min_query_length: number;
```

#### name {#name}

```text
name: string;
```

#### option_groups? {#option_groups}

```text
optional option_groups: object[];
```

#### optional? {#optional}

```text
optional optional: boolean;
```

#### options? {#options}

```text
optional options: SelectOption[];
```

#### placeholder? {#placeholder}

```text
optional placeholder: string;
```

#### selected_options? {#selected_options}

```text
optional selected_options: SelectOption[];
```

#### subtype? {#subtype}

```text
optional subtype: "number" | "url" | "email" | "tel";
```

#### type {#type}

```text
type: "text" | "textarea" | "select";
```

#### value? {#value}

```text
optional value: string;
```

* * *

### notify_on_cancel? {#notify_on_cancel}

```text
optional notify_on_cancel: boolean;
```

Defined in: packages/types/dist/dialog.d.ts:29

* * *

### state? {#state}

```text
optional state: string;
```

Defined in: packages/types/dist/dialog.d.ts:30

* * *

### submit_label? {#submit_label}

```text
optional submit_label: string;
```

Defined in: packages/types/dist/dialog.d.ts:28

* * *

### title {#title}

```text
title: string;
```

Defined in: packages/types/dist/dialog.d.ts:6
