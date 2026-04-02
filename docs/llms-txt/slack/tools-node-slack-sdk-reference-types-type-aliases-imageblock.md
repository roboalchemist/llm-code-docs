Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/type-aliases/ImageBlock

[@slack/types](/tools/node-slack-sdk/reference/types/) / ImageBlock

# Type Alias: ImageBlock

```
type ImageBlock = object & Block &   | UrlImageObject  | SlackFileImageObject;
```

Defined in: [block-kit/blocks.ts:208](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/blocks.ts#L208)

## Type Declaration {#type-declaration}

### alt_text {#alt_text}

```
alt_text: string;
```

#### Description {#description}

A plain-text summary of the image. This should not contain any markup. Maximum length for this field is 2000 characters.

### title? {#title}

```
optional title: PlainTextElement;
```

#### Description {#description-1}

An optional title for the image in the form of a [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) object. Maximum length for the text in this field is 2000 characters.

### type {#type}

```
type: "image";
```

#### Description {#description-2}

The type of block. For an image block, `type` is always `image`.

## Description {#description-3}

Displays an image. A simple image block, designed to make those cat photos really pop.

## See {#see}

[Image block reference](https://docs.slack.dev/reference/block-kit/blocks/image-block).
