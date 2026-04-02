Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/FilesCompleteUploadExternalArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesCompleteUploadExternalArguments

# Type Alias: FilesCompleteUploadExternalArguments

```typescript
type FilesCompleteUploadExternalArguments = FileDestinationArgument & TokenOverridable & object;
```

Defined in: [packages/web-api/src/types/request/files.ts:66](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L66)

## Type Declaration {#type-declaration}

### blocks? {#blocks}

```typescript
optional blocks: (KnownBlock | Block)[];
```

#### Description {#description}

An array of structured rich text blocks. If the `initial_comment` field is provided, the `blocks` field is ignored.

#### Example {#example}

```typescript
[{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]
```

#### See {#see}

[https://docs.slack.dev/reference/block-kit/blocks](https://docs.slack.dev/reference/block-kit/blocks)

### files {#files}

```typescript
files: [FileUploadComplete, ...FileUploadComplete[]];
```

#### Description {#description-1}

Array of file IDs and their corresponding (optional) titles.

#### Example {#example-1}

```typescript
[{"id":"F044GKUHN9Z", "title":"slack-test"}]
```

### initial_comment? {#initial_comment}

```typescript
optional initial_comment: string;
```

#### Description {#description-2}

The message text introducing the file in the specified channel.
