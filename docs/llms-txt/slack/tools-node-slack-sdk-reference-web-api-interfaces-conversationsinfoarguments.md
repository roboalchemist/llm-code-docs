Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/ConversationsInfoArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ConversationsInfoArguments

# Interface: ConversationsInfoArguments

Defined in: [packages/web-api/src/types/request/conversations.ts:101](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L101)

## Extends {#extends}

* `Channel`.`TokenOverridable`.`LocaleAware`

## Properties {#properties}

### channel {#channel}

```text
channel: string;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:15](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L15)

#### Description {#description}

ID of conversation.

#### Inherited from {#inherited-from}

```text
Channel.channel
```

* * *

### include_locale? {#include_locale}

```text
optional include_locale: boolean;
```

Defined in: [packages/web-api/src/types/request/common.ts:51](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L51)

#### Description {#description-1}

Set this to `true` to receive the locale with the response.

#### Inherited from {#inherited-from-1}

```text
LocaleAware.include_locale
```

* * *

### include_num_members? {#include_num_members}

```text
optional include_num_members: boolean;
```

Defined in: [packages/web-api/src/types/request/conversations.ts:105](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/conversations.ts#L105)

#### Description {#description-2}

Set to `true` to include the member count for the specified conversation. Defaults to `false`.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-3}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-2}

```text
TokenOverridable.token
```
