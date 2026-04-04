Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminUsersUnsupportedVersionsExportArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminUsersUnsupportedVersionsExportArguments

# Interface: AdminUsersUnsupportedVersionsExportArguments

Defined in: [packages/web-api/src/types/request/admin/users.ts:158](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L158)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### date_end_of_support? {#date_end_of_support}

```text
optional date_end_of_support: number;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:163](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L163)

#### Description {#description}

Unix timestamp of the date of past or upcoming end of support cycles. If not provided will include all announced end of support cycles. Defaults to `0`.

* * *

### date_sessions_started? {#date_sessions_started}

```text
optional date_sessions_started: number;
```

Defined in: [packages/web-api/src/types/request/admin/users.ts:168](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/users.ts#L168)

#### Description {#description-1}

Unix timestamp of a date to start looking for user sessions. If not provided will start six months ago.

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
