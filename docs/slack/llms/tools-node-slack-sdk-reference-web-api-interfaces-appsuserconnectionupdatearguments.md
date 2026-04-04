Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AppsUserConnectionUpdateArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AppsUserConnectionUpdateArguments

# Interface: AppsUserConnectionUpdateArguments

Defined in: [packages/web-api/src/types/request/apps.ts:36](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/apps.ts#L36)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### status {#status}

```text
status: string;
```

Defined in: [packages/web-api/src/types/request/apps.ts:40](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/apps.ts#L40)

#### Description {#description}

The connection status value to assign to the user. `connected` or `disconnected`.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-1}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```

* * *

### user_id {#user_id}

```text
user_id: string;
```

Defined in: [packages/web-api/src/types/request/apps.ts:38](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/apps.ts#L38)

#### Description {#description-2}

The identifier for the user receiving the status update.
