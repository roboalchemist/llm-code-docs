# Source: https://docs.wandb.ai/weave/reference/typescript-sdk/interfaces/weaveimage.md

# Source: https://docs.wandb.ai/weave/reference/typescript-sdk/functions/weaveimage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# weaveImage

> TypeScript SDK reference

# weaveImage

▸ **weaveImage**(`options`): [`WeaveImage`](../interfaces/weaveimage)

Create a new WeaveImage object

#### Parameters

| Name      | Type              | Description                                                                                                                                              |
| :-------- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `options` | `WeaveImageInput` | The options for this media type - data: The raw image data as a Buffer - imageType: (Optional) The type of image file, currently only 'png' is supported |

#### Returns

[`WeaveImage`](../interfaces/weaveimage)

`Example`

```ts  theme={null}
const imageBuffer = fs.readFileSync('path/to/image.png');
const weaveImage = weaveImage({ data: imageBuffer });
```

#### Defined in

[media.ts:28](https://github.com/wandb/weave/blob/1aee4006a95d913addb45881dfc950de7ce7b0bd/sdks/node/src/media.ts#L28)

***
