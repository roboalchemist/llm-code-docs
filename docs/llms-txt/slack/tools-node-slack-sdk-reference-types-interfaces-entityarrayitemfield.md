Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/EntityArrayItemField

[@slack/types](/tools/node-slack-sdk/reference/types/) / EntityArrayItemField

# Interface: EntityArrayItemField

Defined in: [message-metadata.ts:188](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L188)

## Extends {#extends}

* `Omit`<[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField), `"type"`\>

## Properties {#properties}

### alt_text? {#alt_text}

```text
optional alt_text: string;
```

Defined in: [message-metadata.ts:202](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L202)

#### Inherited from {#inherited-from}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`alt_text`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#alt_text)

* * *

### edit? {#edit}

```text
optional edit: EntityEditSupport;
```

Defined in: [message-metadata.ts:203](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L203)

#### Inherited from {#inherited-from-1}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`edit`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#edit)

* * *

### entity_ref? {#entity_ref}

```text
optional entity_ref: EntityRefField;
```

Defined in: [message-metadata.ts:206](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L206)

#### Inherited from {#inherited-from-2}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`entity_ref`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#entity_ref)

* * *

### format? {#format}

```text
optional format: string;
```

Defined in: [message-metadata.ts:199](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L199)

#### Inherited from {#inherited-from-3}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`format`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#format)

* * *

### icon? {#icon}

```text
optional icon: EntityIconField;
```

Defined in: [message-metadata.ts:197](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L197)

#### Inherited from {#inherited-from-4}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`icon`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#icon)

* * *

### image_url? {#image_url}

```text
optional image_url: string;
```

Defined in: [message-metadata.ts:200](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L200)

#### Inherited from {#inherited-from-5}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`image_url`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#image_url)

* * *

### label? {#label}

```text
optional label: string;
```

Defined in: [message-metadata.ts:194](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L194)

#### Inherited from {#inherited-from-6}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`label`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#label)

* * *

### link? {#link}

```text
optional link: string;
```

Defined in: [message-metadata.ts:196](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L196)

#### Inherited from {#inherited-from-7}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`link`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#link)

* * *

### long? {#long}

```text
optional long: boolean;
```

Defined in: [message-metadata.ts:198](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L198)

#### Inherited from {#inherited-from-8}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`long`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#long)

* * *

### slack_file? {#slack_file}

```text
optional slack_file: SlackFile;
```

Defined in: [message-metadata.ts:201](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L201)

#### Inherited from {#inherited-from-9}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`slack_file`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#slack_file)

* * *

### tag_color? {#tag_color}

```text
optional tag_color: string;
```

Defined in: [message-metadata.ts:204](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L204)

#### Inherited from {#inherited-from-10}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`tag_color`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#tag_color)

* * *

### type? {#type}

```text
optional type: string;
```

Defined in: [message-metadata.ts:189](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L189)

* * *

### user? {#user}

```text
optional user:   | EntityUserIDField  | EntityUserField;
```

Defined in: [message-metadata.ts:205](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L205)

#### Inherited from {#inherited-from-11}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`user`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#user)

* * *

### value? {#value}

```text
optional value: string | number;
```

Defined in: [message-metadata.ts:195](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L195)

#### Inherited from {#inherited-from-12}

[`EntityTypedField`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField).[`value`](/tools/node-slack-sdk/reference/types/interfaces/EntityTypedField#value)
