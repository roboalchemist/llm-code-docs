Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/SlackFile

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / SlackFile

# Type Alias: SlackFile

```typescript
type SlackFile = SlackFileViaUrl | SlackFileViaId;
```

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:235

## Description {#description}

Defines an object containing Slack file information to be used in an image block or image element. This file [https://docs.slack.dev/reference/objects/file-object](https://docs.slack.dev/reference/objects/file-object) must be an image and you must provide either the URL or ID. In addition, the user posting these blocks must have access to this file. If both are provided then the payload will be rejected. Currently only `png`, `jpg`, `jpeg`, and `gif` Slack image files are supported.

## See {#see}

[Slack File object reference](https://docs.slack.dev/reference/block-kit/composition-objects/slack-file-object).
