Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/type-aliases/ImageElement

[@slack/types](/tools/node-slack-sdk/reference/types/) / ImageElement

# Type Alias: ImageElement

```
type ImageElement = object &   | UrlImageObject  | SlackFileImageObject;
```

Defined in: [block-kit/block-elements.ts:251](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/block-elements.ts#L251)

## Type Declaration {#type-declaration}

### alt_text {#alt_text}

```
alt_text: string;
```

#### Description {#description}

A plain-text summary of the image. This should not contain any markup.

### type {#type}

```
type: "image";
```

#### Description {#description-1}

The type of element. In this case `type` is always `image`.

## Description {#description-2}

Displays an image as part of a larger block of content. Use this `image` block if you want a block with only an image in it.

## See {#see}

[Image element reference](https://docs.slack.dev/reference/block-kit/block-elements/image-element).
