Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ImageBlock

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ImageBlock

# Type Alias: ImageBlock

```typescript
type ImageBlock = object & Block &   | UrlImageObject  | SlackFileImageObject;
```

Defined in: packages/types/dist/block-kit/blocks.d.ts:137

## Type Declaration {#type-declaration}

### alt_text {#alt_text}

```typescript
alt_text: string;
```

#### Description {#description}

A plain-text summary of the image. This should not contain any markup. Maximum length for this field is 2000 characters.

### title? {#title}

```typescript
optional title: PlainTextElement;
```

#### Description {#description-1}

An optional title for the image in the form of a [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) object. Maximum length for the text in this field is 2000 characters.

### type {#type}

```typescript
type: "image";
```

#### Description {#description-2}

The type of block. For an image block, `type` is always `image`.

## Description {#description-3}

Displays an image. A simple image block, designed to make those cat photos really pop.

## See {#see}

[Image block reference](https://docs.slack.dev/reference/block-kit/blocks/image-block).
