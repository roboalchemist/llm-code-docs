Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FilesDeleteArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesDeleteArguments

# Interface: FilesDeleteArguments

Defined in: [packages/web-api/src/types/request/files.ts:84](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L84)

## Extends {#extends}

* `FileArgument`.`TokenOverridable`

## Properties {#properties}

### file {#file}

```text
file: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:14](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L14)

#### Description {#description}

Encoded file ID.

#### Inherited from {#inherited-from}

```text
FileArgument.file
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
