# Type Alias: AudioFromVideoOptions

```
type AudioFromVideoOptions = object;
```

Options for configuring audio extraction from video operations.

## Properties[#](#properties)

| Property | Type | Default value | Description |
| --- | --- | --- | --- |
| `keepTrimSettings?` | `boolean` | `true` | If true, the audio block will have the same duration, trim length, and trim offset as the source video. If false, the full audio track is extracted without trim settings. |
| `muteOriginalVideo?` | `boolean` | `true` | If true, mutes the audio of the original video fill block. |

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/engine/type-aliases/audioexportoptions)