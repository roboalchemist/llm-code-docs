Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminEmojiAddAliasArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminEmojiAddAliasArguments

# Interface: AdminEmojiAddAliasArguments

Defined in: [packages/web-api/src/types/request/admin/emoji.ts:23](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/emoji.ts#L23)

## Extends {#extends}

* `Name`.`TokenOverridable`

## Properties {#properties}

### alias_for {#alias_for}

```
alias_for: string;
```

Defined in: [packages/web-api/src/types/request/admin/emoji.ts:28](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/emoji.ts#L28)

#### Description {#description}

Name of the emoji for which the alias is being made. Any wrapping whitespace or colons will be automatically trimmed.

* * *

### name {#name}

```
name: string;
```

Defined in: [packages/web-api/src/types/request/admin/emoji.ts:10](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/emoji.ts#L10)

#### Description {#description-1}

The name of the emoji. Colons (:myemoji:) around the value are not required, although they may be included.

#### Inherited from {#inherited-from}

```
Name.name
```

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```
TokenOverridable.token
```
