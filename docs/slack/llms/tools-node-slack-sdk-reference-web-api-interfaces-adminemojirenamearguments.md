Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminEmojiRenameArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminEmojiRenameArguments

# Interface: AdminEmojiRenameArguments

Defined in: [packages/web-api/src/types/request/admin/emoji.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/emoji.ts#L38)

## Extends {#extends}

* `Name`.`TokenOverridable`

## Properties {#properties}

### name {#name}

```text
name: string;
```

Defined in: [packages/web-api/src/types/request/admin/emoji.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/emoji.ts#L10)

#### Description {#description}

The name of the emoji. Colons (:myemoji:) around the value are not required, although they may be included.

#### Inherited from {#inherited-from}

```text
Name.name
```

* * *

### new_name {#new_name}

```text
new_name: string;
```

Defined in: [packages/web-api/src/types/request/admin/emoji.ts:40](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/emoji.ts#L40)

#### Description {#description-1}

The new name of the emoji.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```
