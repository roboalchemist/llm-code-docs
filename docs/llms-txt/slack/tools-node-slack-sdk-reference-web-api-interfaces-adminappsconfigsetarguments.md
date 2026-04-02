Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/AdminAppsConfigSetArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / AdminAppsConfigSetArguments

# Interface: AdminAppsConfigSetArguments

Defined in: [packages/web-api/src/types/request/admin/apps.ts:73](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/apps.ts#L73)

## Extends {#extends}

* `AppID`.`TokenOverridable`

## Properties {#properties}

### app_id {#app_id}

```
app_id: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:101](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L101)

#### Description {#description}

The ID of the app.

#### Inherited from {#inherited-from}

```
AppID.app_id
```

* * *

### domain_restrictions? {#domain_restrictions}

```
optional domain_restrictions: object;
```

Defined in: [packages/web-api/src/types/request/admin/apps.ts:75](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/apps.ts#L75)

#### emails? {#emails}

```
optional emails: string[];
```

##### Description {#description-1}

Sets emails for connector authorization.

#### urls? {#urls}

```
optional urls: string[];
```

##### Description {#description-2}

Sets allowed URLs for the app.

#### Description {#description-3}

Domain restrictions for the app.

* * *

### token? {#token}

```
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-1}

```
TokenOverridable.token
```

* * *

### workflow_auth_strategy? {#workflow_auth_strategy}

```
optional workflow_auth_strategy: "builder_choice" | "end_user_only";
```

Defined in: [packages/web-api/src/types/request/admin/apps.ts:82](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/admin/apps.ts#L82)

#### Description {#description-5}

The workflow auth permission.
