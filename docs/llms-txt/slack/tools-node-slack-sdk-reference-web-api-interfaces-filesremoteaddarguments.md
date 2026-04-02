Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FilesRemoteAddArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesRemoteAddArguments

# Interface: FilesRemoteAddArguments

Defined in: [packages/web-api/src/types/request/files.ts:215](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L215)

## Extends {#extends}

* `SharedFile`.`FileType`.`ExternalIDArgument`.`TokenOverridable`

## Properties {#properties}

### external_id {#external_id}

```text
external_id: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:18](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L18)

#### Description {#description}

Creator defined GUID for the file.

#### Inherited from {#inherited-from}

```text
ExternalIDArgument.external_id
```

* * *

### external_url {#external_url}

```text
external_url: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:204](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L204)

#### Description {#description-1}

URL of the remote file.

#### Inherited from {#inherited-from-1}

```text
SharedFile.external_url
```

* * *

### filetype? {#filetype}

```text
optional filetype: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:32](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L32)

#### Description {#description-2}

A file type identifier.

#### See {#see}

[File types](https://docs.slack.dev/reference/objects/file-object) for a complete list of supported file types.

#### Inherited from {#inherited-from-2}

```text
FileType.filetype
```

* * *

### indexable_file_contents? {#indexable_file_contents}

```text
optional indexable_file_contents: Buffer<ArrayBufferLike> | Stream;
```

Defined in: [packages/web-api/src/types/request/files.ts:211](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L211)

#### Description {#description-3}

A text file (txt, pdf, doc, etc.) containing textual search terms that are used to improve discovery of the remote file.

#### Inherited from {#inherited-from-3}

```text
SharedFile.indexable_file_contents
```

* * *

### preview_image? {#preview_image}

```text
optional preview_image: Buffer<ArrayBufferLike> | Stream;
```

Defined in: [packages/web-api/src/types/request/files.ts:206](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L206)

#### Description {#description-4}

Preview of the document.

#### Inherited from {#inherited-from-4}

```text
SharedFile.preview_image
```

* * *

### title {#title}

```text
title: string;
```

Defined in: [packages/web-api/src/types/request/files.ts:202](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L202)

#### Description {#description-5}

Title of the file being shared.

#### Inherited from {#inherited-from-5}

```text
SharedFile.title
```

* * *

### token? {#token}

```text
optional token: string;
```

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-6}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from-6}

```text
TokenOverridable.token
```
