Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminEmojiAddArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminEmojiAddArguments

# Interface: AdminEmojiAddArguments

Defined in: [packages/web-api/src/types/request/admin/emoji.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/emoji.ts#L14)

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

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```text
TokenOverridable.token
```

* * *

### url {#url}

```text
url: string;
```

Defined in: [packages/web-api/src/types/request/admin/emoji.ts:19](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/emoji.ts#L19)

#### Description {#description-2}

The URL of a file to use as an image for the emoji. Square images under 128KB and with transparent backgrounds work best.
