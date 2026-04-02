Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/type-aliases/ImageElement

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / ImageElement

# Type Alias: ImageElement

```typescript
type ImageElement = object &   | UrlImageObject  | SlackFileImageObject;
```

Defined in: packages/types/dist/block-kit/block-elements.d.ts:223

## Type Declaration {#type-declaration}

### alt_text {#alt_text}

```typescript
alt_text: string;
```

#### Description {#description}

A plain-text summary of the image. This should not contain any markup.

### type {#type}

```typescript
type: "image";
```

#### Description {#description-1}

The type of element. In this case `type` is always `image`.

## Description {#description-2}

Displays an image as part of a larger block of content. Use this `image` block if you want a block with only an image in it.

## See {#see}

[Image element reference](https://docs.slack.dev/reference/block-kit/block-elements/image-element).
