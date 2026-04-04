Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/EntityEditSupport

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / EntityEditSupport

# Interface: EntityEditSupport

Defined in: packages/types/dist/message-metadata.d.ts:94

## Properties {#properties}

### enabled {#enabled}

```text
enabled: boolean;
```

Defined in: packages/types/dist/message-metadata.d.ts:95

* * *

### hint? {#hint}

```text
optional hint: PlainTextElement;
```

Defined in: packages/types/dist/message-metadata.d.ts:97

* * *

### number? {#number}

```text
optional number: object;
```

Defined in: packages/types/dist/message-metadata.d.ts:106

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

Defined in: packages/types/dist/message-metadata.d.ts:98

* * *

### placeholder? {#placeholder}

```text
optional placeholder: PlainTextElement;
```

Defined in: packages/types/dist/message-metadata.d.ts:96

* * *

### select? {#select}

```text
optional select: object;
```

Defined in: packages/types/dist/message-metadata.d.ts:99

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

Defined in: packages/types/dist/message-metadata.d.ts:111

#### max_length? {#max_length}

```text
optional max_length: number;
```

#### min_length? {#min_length}

```text
optional min_length: number;
```
