Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/DialogOpenArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / DialogOpenArguments

# Interface: DialogOpenArguments

Defined in: [packages/web-api/src/types/request/dialog.ts:5](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/dialog.ts#L5)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### dialog {#dialog}

```text
dialog: Dialog;
```

Defined in: [packages/web-api/src/types/request/dialog.ts:9](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/dialog.ts#L9)

#### Description {#description}

The dialog definition.

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

### trigger_id {#trigger_id}

```text
trigger_id: string;
```

Defined in: [packages/web-api/src/types/request/dialog.ts:7](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/dialog.ts#L7)

#### Description {#description-2}

Exchange a trigger to post to the user.
