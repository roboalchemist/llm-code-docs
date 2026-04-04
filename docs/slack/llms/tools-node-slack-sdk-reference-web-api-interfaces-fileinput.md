Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/FileInput

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / FileInput

# Interface: FileInput

Defined in: packages/types/dist/block-kit/block-elements.d.ts:169

## Description {#description}

Allows user to upload files. In order to use the `file_input` element within your app, your app must have the `files:read` scope.

## See {#see}

[File input element reference](https://docs.slack.dev/reference/block-kit/block-elements/file-input-element).

## Extends {#extends}

* [`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable)

## Properties {#properties}

### action_id? {#action_id}

```text
optional action_id: string;
```

Defined in: packages/types/dist/block-kit/extensions.d.ts:12

@description: An identifier for this action. You can use this when you receive an interaction payload to [identify the source of the action](https://docs.slack.dev/interactivity/handling-user-interaction#payloads). Should be unique among all other `action_id`s in the containing block. Maximum length for this field is 255 characters.

#### Inherited from {#inherited-from}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`action_id`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#action_id)

* * *

### filetypes? {#filetypes}

```text
optional filetypes: string[];
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:179

#### Description {#description-1}

An array of valid [file extensions](https://docs.slack.dev/reference/objects/file-object) that will be accepted for this element. All file extensions will be accepted if `filetypes` is not specified. This validation is provided for convenience only, and you should perform your own file type validation based on what you expect to receive.

* * *

### max_files? {#max_files}

```text
optional max_files: number;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:184

#### Description {#description-2}

Maximum number of files that can be uploaded for this `file_input` element. Minimum of `1`, maximum of `10`. Defaults to `10` if not specified.

* * *

### type {#type}

```text
type: "file_input";
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:173

#### Description {#description-3}

The type of element. In this case `type` is always `file_input`.

#### Overrides {#overrides}

[`Actionable`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable).[`type`](/tools/node-slack-sdk/reference/web-api/interfaces/Actionable#type)
