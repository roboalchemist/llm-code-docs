Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/EntityEditSupport

[@slack/types](/tools/node-slack-sdk/reference/types/) / EntityEditSupport

# Interface: EntityEditSupport

Defined in: [message-metadata.ts:112](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L112)

## Properties {#properties}

### enabled {#enabled}

```text
enabled: boolean;
```

Defined in: [message-metadata.ts:113](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L113)

* * *

### hint? {#hint}

```text
optional hint: PlainTextElement;
```

Defined in: [message-metadata.ts:115](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L115)

* * *

### number? {#number}

```text
optional number: object;
```

Defined in: [message-metadata.ts:124](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L124)

#### is_decimal_allowed? {#is_decimal_allowed}

```text
optional is_decimal_allowed: boolean;
```

#### max_value? {#max_value}

```text
optional max_value: number;
```

#### min_value? {#min_value}

```text
optional min_value: number;
```

* * *

### optional? {#optional}

```text
optional optional: boolean;
```

Defined in: [message-metadata.ts:116](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L116)

* * *

### placeholder? {#placeholder}

```text
optional placeholder: PlainTextElement;
```

Defined in: [message-metadata.ts:114](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L114)

* * *

### select? {#select}

```text
optional select: object;
```

Defined in: [message-metadata.ts:117](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L117)

#### current_value? {#current_value}

```text
optional current_value: string;
```

#### current_values? {#current_values}

```text
optional current_values: string[];
```

#### fetch_options_dynamically? {#fetch_options_dynamically}

```text
optional fetch_options_dynamically: boolean;
```

#### min_query_length? {#min_query_length}

```text
optional min_query_length: number;
```

#### static_options? {#static_options}

```text
optional static_options: Option[];
```

* * *

### text? {#text}

```text
optional text: object;
```

Defined in: [message-metadata.ts:129](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/message-metadata.ts#L129)

#### max_length? {#max_length}

```text
optional max_length: number;
```

#### min_length? {#min_length}

```text
optional min_length: number;
```
