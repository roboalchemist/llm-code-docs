# Source: https://docs.wandb.ai/weave/reference/typescript-sdk/interfaces/weaveaudio.md

# Source: https://docs.wandb.ai/weave/reference/typescript-sdk/functions/weaveaudio.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# weaveAudio

> TypeScript SDK reference

# weaveAudio

▸ **weaveAudio**(`options`): [`WeaveAudio`](../interfaces/weaveaudio)

Create a new WeaveAudio object

#### Parameters

| Name      | Type              | Description                                                                                                                                              |
| :-------- | :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `options` | `WeaveAudioInput` | The options for this media type - data: The raw audio data as a Buffer - audioType: (Optional) The type of audio file, currently only 'wav' is supported |

#### Returns

[`WeaveAudio`](../interfaces/weaveaudio)

`Example`

```ts  theme={null}
const audioBuffer = fs.readFileSync('path/to/audio.wav');
const weaveAudio = weaveAudio({ data: audioBuffer });
```

#### Defined in

[media.ts:62](https://github.com/wandb/weave/blob/1aee4006a95d913addb45881dfc950de7ce7b0bd/sdks/node/src/media.ts#L62)

***
