Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/EntityCustomField

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / EntityCustomField

# Interface: EntityCustomField

Defined in: packages/types/dist/message-metadata.d.ts:236

## Properties {#properties}

### alt_text? {#alt_text}

```text
optional alt_text: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:247

* * *

### boolean? {#boolean}

```text
optional boolean:   | EntityBooleanCheckboxField  | EntityBooleanTextField;
```

Defined in: packages/types/dist/message-metadata.d.ts:253

* * *

### edit? {#edit}

```text
optional edit: EntityEditSupport;
```

Defined in: packages/types/dist/message-metadata.d.ts:249

* * *

### entity_ref? {#entity_ref}

```text
optional entity_ref: EntityRefField;
```

Defined in: packages/types/dist/message-metadata.d.ts:252

* * *

### format? {#format}

```text
optional format: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:244

* * *

### icon? {#icon}

```text
optional icon: EntityIconField;
```

Defined in: packages/types/dist/message-metadata.d.ts:242

* * *

### image_url? {#image_url}

```text
optional image_url: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:245

* * *

### item_type? {#item_type}

```text
optional item_type: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:250

* * *

### key {#key}

```text
key: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:238

* * *

### label {#label}

```text
label: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:237

* * *

### link? {#link}

```text
optional link: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:241

* * *

### long? {#long}

```text
optional long: boolean;
```

Defined in: packages/types/dist/message-metadata.d.ts:243

* * *

### slack_file? {#slack_file}

```text
optional slack_file: SlackFile;
```

Defined in: packages/types/dist/message-metadata.d.ts:246

* * *

### tag_color? {#tag_color}

```text
optional tag_color: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:248

* * *

### type {#type}

```text
type: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:239

* * *

### user? {#user}

```text
optional user:   | EntityUserIDField  | EntityUserField;
```

Defined in: packages/types/dist/message-metadata.d.ts:251

* * *

### value? {#value}

```text
optional value: string | number | EntityArrayItemField[];
```

Defined in: packages/types/dist/message-metadata.d.ts:240
