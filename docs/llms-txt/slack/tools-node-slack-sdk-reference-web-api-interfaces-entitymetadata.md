Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/EntityMetadata

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / EntityMetadata

# Interface: EntityMetadata

Defined in: packages/types/dist/message-metadata.d.ts:26

## Description {#description}

Metadata that represents a work object entity.

## Properties {#properties}

### app_unfurl_url? {#app_unfurl_url}

```text
optional app_unfurl_url: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:56

#### Description {#description-1}

The exact URL posted in the source message. Required in metadata passed to `chat.unfurl`.

* * *

### entity_payload {#entity_payload}

```text
entity_payload: object;
```

Defined in: packages/types/dist/message-metadata.d.ts:34

#### actions? {#actions}

```text
optional actions: object;
```

##### actions.overflow_actions? {#actionsoverflow_actions}

```text
optional overflow_actions: EntityActionButton[];
```

##### actions.primary_actions? {#actionsprimary_actions}

```text
optional primary_actions: EntityActionButton[];
```

#### attributes {#attributes}

```text
attributes: EntityAttributes;
```

#### custom_fields? {#custom_fields}

```text
optional custom_fields: EntityCustomField[];
```

#### display_order? {#display_order}

```text
optional display_order: string[];
```

#### fields? {#fields}

```text
optional fields:   | ContentItemEntityFields  | FileEntityFields  | IncidentEntityFields  | TaskEntityFields;
```

#### slack_file? {#slack_file}

```text
optional slack_file: FileEntitySlackFile;
```

#### Description {#description-2}

Schema for the given entity type.

* * *

### entity_type {#entity_type}

```text
entity_type: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:30

#### Description {#description-3}

Entity type.

* * *

### external_ref {#external_ref}

```text
external_ref: ExternalRef;
```

Defined in: packages/types/dist/message-metadata.d.ts:48

#### Description {#description-4}

Reference (and optional type) used to identify an entity within the developer's system.

* * *

### url {#url}

```text
url: string;
```

Defined in: packages/types/dist/message-metadata.d.ts:52

#### Description {#description-5}

URL used to identify an entity within the developer's system.
