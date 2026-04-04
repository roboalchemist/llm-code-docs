Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/CallsUpdateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / CallsUpdateArguments

# Interface: CallsUpdateArguments

Defined in: [packages/web-api/src/types/request/calls.ts:57](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L57)

## Extends {#extends}

* `ID`.`Partial`<`CallDetails`\>.`TokenOverridable`

## Properties {#properties}

### desktop_app_join_url? {#desktop_app_join_url}

```text
optional desktop_app_join_url: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:22](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L22)

#### Description {#description}

When supplied, available Slack clients will attempt to directly launch the 3rd-party Call with this URL.

#### Inherited from {#inherited-from}

[`CallsAddArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/CallsAddArguments).[`desktop_app_join_url`](/tools/node-slack-sdk/reference/web-api/interfaces/CallsAddArguments#desktop_app_join_url)

* * *

### id {#id}

```text
id: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:6](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L6)

#### Description {#description-1}

`id` returned when registering the call using the `calls.add` method.

#### Inherited from {#inherited-from-1}

```text
ID.id
```

* * *

### join_url? {#join_url}

```text
optional join_url: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:17](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L17)

#### Description {#description-2}

The URL required for a client to join the Call.

#### Inherited from {#inherited-from-2}

[`CallsAddArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/CallsAddArguments).[`join_url`](/tools/node-slack-sdk/reference/web-api/interfaces/CallsAddArguments#join_url)

* * *

### title? {#title}

```text
optional title: string;
```

Defined in: [packages/web-api/src/types/request/calls.ts:24](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/calls.ts#L24)

#### Description {#description-3}

The name of the Call.

#### Inherited from {#inherited-from-3}

[`CallsAddArguments`](/tools/node-slack-sdk/reference/web-api/interfaces/CallsAddArguments).[`title`](/tools/node-slack-sdk/reference/web-api/interfaces/CallsAddArguments#title)

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-4}

```text
TokenOverridable.token
```
