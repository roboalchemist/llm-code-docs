Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsersSessionSetSettingsArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsersSessionSetSettingsArguments

# Interface: AdminUsersSessionSetSettingsArguments

Defined in: [packages/web-api/src/types/request/admin/users.ts:132](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L132)

## Extends {#extends}

* `UserIDs`.`TokenOverridable`

## Properties {#properties}

### desktop_app_browser_quit? {#desktop_app_browser_quit}

```text
optional desktop_app_browser_quit: boolean;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:134](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L134)

#### Description {#description}

Terminate the session when the client—either the desktop app or a browser window—is closed.

* * *

### duration? {#duration}

```text
optional duration: number;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:139](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L139)

#### Description {#description-1}

The session duration in seconds. The minimum value is 28800, which represents 8 hours; the max value is 315569520 or 10 years (that's a long Slack session).

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-2}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```

* * *

### user_ids {#user_ids}

```text
user_ids: [string, ...string[]];
```

Defined in: [packages/web-api/src/types/request/common.ts:92](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L92)

#### Description {#description-3}

List of encoded user IDs.

#### Inherited from {#inherited-from-1}

```text
UserIDs.user_ids
```
