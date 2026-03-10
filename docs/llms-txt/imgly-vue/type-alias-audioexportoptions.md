# Type Alias: AudioExportOptions

```
type AudioExportOptions = object;
```

Represents the options for exporting audio.

Defines the possible options for exporting audio.

*   ‘mimeType’: The MIME type of the output audio file.
*   ‘onProgress’: A callback which reports on the progress of the export.
*   ‘timeOffset’: The time offset in seconds relative to the target block.
*   ‘duration’: The duration in seconds of the final audio.
*   ‘sampleRate’: The sample rate of the exported audio.
*   ‘numberOfChannels’: The number of channels of the exported audio.
*   ‘skipEncoding’: Skip encoding (audio data will be returned immediately even if not compatible with target MIME type).

## Properties[#](#properties)

| Property | Type | Default value | Description |
| --- | --- | --- | --- |
| `mimeType?` | [`AudioMimeType`](https://img.ly/docs/cesdk/vue/api/engine/type-aliases/audiomimetype/) | `'audio/wav'` | The MIME type of the output audio file. |
| `onProgress?` | (`numberOfRenderedFrames`, `numberOfEncodedFrames`, `totalNumberOfFrames`) => `void` | `undefined` | A callback which reports on the progress of the export. |
| `timeOffset?` | `number` | `0` | The time offset in seconds relative to the target block. |
| `duration?` | `number` | `The duration of the block.` | The duration in seconds of the final audio. |
| `sampleRate?` | `number` | `48000` | The sample rate of the exported audio. |
| `numberOfChannels?` | `number` | `2` | The number of channels of the exported audio. |
| `skipEncoding?` | `boolean` | `false` | Skip encoding (audio data will be returned immediately even if not compatible with target MIME type). |
| `abortSignal?` | `AbortSignal` | `undefined` | An AbortSignal that can be used to cancel the audio export operation. |

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/type-aliases/assettransformpreset)