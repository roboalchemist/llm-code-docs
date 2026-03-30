# Interface: AudioTrackInfo

Information about a single audio track from a video. This interface provides comprehensive metadata about audio tracks, including codec information, technical specifications, and track details.

## Properties[#](#properties)

| Property | Type | Description |
| --- | --- | --- |
| `audioCodec` | `string` | The codec string |
| `channels` | `number` | The number of audio channels |
| `sampleRate` | `number` | The audio sample rate |
| `audioDuration` | `number` | Duration of the audio track in seconds |
| `numAudioPackets` | `number` | The number of audio packets (matches the number of encoded chunks) |
| `numAudioFrames` | `number` | The number of audio frames |
| `trackName` | `string` | Optional track name/label if available in metadata |
| `trackIndex` | `number` | Track index in the container |
| `language` | `string` | Track language code (ISO 639-2T format: “und”, “eng”, “deu”, etc.) |

---



[Source](https:/img.ly/docs/cesdk/vue/api/engine/interfaces/assetstringproperty)