Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FilesGetUploadURLExternalArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesGetUploadURLExternalArguments

# Interface: FilesGetUploadURLExternalArguments

Defined in: [packages/web-api/src/types/request/files.ts:87](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L87)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### alt_text? {#alt_text}

```text
optional alt_text: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:93](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L93)

#### Description {#description}

Description of image for screen-reader.

* * *

### filename {#filename}

```text
filename: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:89](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L89)

#### Description {#description-1}

Name of the file being uploaded.

* * *

### length {#length}

```text
length: number;
```

Defined in: [packages/web-api/src/types/request/files.ts:91](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L91)

#### Description {#description-2}

Size in bytes of the file being uploaded.

* * *

### snippet_type? {#snippet_type}

```text
optional snippet_type: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:95](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L95)

#### Description {#description-3}

Syntax type of the snippet being uploaded. E.g. `python`.

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```
