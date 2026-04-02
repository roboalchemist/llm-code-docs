Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/EntityCustomField

[@slack/types](/tools/node-slack-sdk/reference/types/) / EntityCustomField

# Interface: EntityCustomField

Defined in: [message-metadata.ts:270](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L270)

## Properties {#properties}

### alt_text? {#alt_text}

```text
optional alt_text: string;
```

Defined in: [message-metadata.ts:281](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L281)

* * *

### boolean? {#boolean}

```text
optional boolean:   | EntityBooleanCheckboxField  | EntityBooleanTextField;
```

Defined in: [message-metadata.ts:287](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L287)

* * *

### edit? {#edit}

```text
optional edit: EntityEditSupport;
```

Defined in: [message-metadata.ts:283](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L283)

* * *

### entity_ref? {#entity_ref}

```text
optional entity_ref: EntityRefField;
```

Defined in: [message-metadata.ts:286](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L286)

* * *

### format? {#format}

```text
optional format: string;
```

Defined in: [message-metadata.ts:278](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L278)

* * *

### icon? {#icon}

```text
optional icon: EntityIconField;
```

Defined in: [message-metadata.ts:276](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L276)

* * *

### image_url? {#image_url}

```text
optional image_url: string;
```

Defined in: [message-metadata.ts:279](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L279)

* * *

### item_type? {#item_type}

```text
optional item_type: string;
```

Defined in: [message-metadata.ts:284](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L284)

* * *

### key {#key}

```text
key: string;
```

Defined in: [message-metadata.ts:272](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L272)

* * *

### label {#label}

```text
label: string;
```

Defined in: [message-metadata.ts:271](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L271)

* * *

### link? {#link}

```text
optional link: string;
```

Defined in: [message-metadata.ts:275](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L275)

* * *

### long? {#long}

```text
optional long: boolean;
```

Defined in: [message-metadata.ts:277](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L277)

* * *

### slack_file? {#slack_file}

```text
optional slack_file: SlackFile;
```

Defined in: [message-metadata.ts:280](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L280)

* * *

### tag_color? {#tag_color}

```text
optional tag_color: string;
```

Defined in: [message-metadata.ts:282](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L282)

* * *

### type {#type}

```text
type: string;
```

Defined in: [message-metadata.ts:273](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L273)

* * *

### user? {#user}

```text
optional user:   | EntityUserIDField  | EntityUserField;
```

Defined in: [message-metadata.ts:285](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L285)

* * *

### value? {#value}

```text
optional value: string | number | EntityArrayItemField[];
```

Defined in: [message-metadata.ts:274](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L274)
