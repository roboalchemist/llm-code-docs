Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/FilesUploadV2Arguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FilesUploadV2Arguments

# Type Alias: FilesUploadV2Arguments

```typescript
type FilesUploadV2Arguments = TokenOverridable &   | FileUploadV2  | Omit<FileUploadV2, "file" | "content"> & FilesUploadV2ArgumentsMultipleFiles;
```

Defined in: [packages/web-api/src/types/request/files.ts:183](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/files.ts#L183)
