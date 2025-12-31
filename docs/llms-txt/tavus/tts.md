# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/tts.md

# Text-to-Speech (TTS)

> Discover how to integrate custom voices from third-party TTS engines for multilingual or localized speech output.

The **TTS Layer** in Tavus enables your persona to generate natural-sounding voice responses.
You can configure the TTS layer using a third-party tts engine provider. If `layers.tts` is not specified, Tavus will default to `cartesia` engine.

<Note>
  If you use the default engine, you do not need to specify any parameters within the `tts` layer.
</Note>

## Configuring the TTS Layer

Define the TTS layer under the `layers.tts` object. Below are the parameters available:

### 1. `tts_engine`

Specifies the supported third-party TTS engine.

* **Options**:  `cartesia`, `elevenlabs`.

```json  theme={null}
"tts": {
  "tts_engine": "cartesia"
}
```

### 2. `api_key`

Authenticates requests to your selected third-party TTS provider. You can obtain an API key from one of the following:

<Warning>
  Only required when using private voices.
</Warning>

* <a href="https://play.cartesia.ai/keys" target="_blank">Cartesia</a>
* <a href="https://elevenlabs.io/app/settings/api-keys" target="_blank">ElevenLabs</a>

```json  theme={null}
"tts": {
  "api_key": "your-api-key"
}
```

### 3. `external_voice_id`

Specifies which voice to use with the selected TTS engine. To find supported voice IDs, refer to the provider’s documentation:

* <a href="https://docs.cartesia.ai/api-reference/voices/list" target="_blank">Cartesia</a>
* <a href="https://elevenlabs.io/docs/api-reference/voices/search" target="_blank">ElevenLabs</a>

<Note>
  You can use any publicly accessible custom voice from ElevenLabs or Cartesia without the provider's API key. If the custom voice is private, you still need to use the provider's API key.
</Note>

```json  theme={null}
"tts": {
  "external_voice_id": "external-voice-id"
}
```

### 4. `tts_model_name`

Model name used by the TTS engine. Refer to:

* <a href="https://docs.cartesia.ai/2025-04-16/build-with-cartesia/models" target="_blank">Cartesia</a>
* <a href="https://elevenlabs.io/docs/models" target="_blank">ElevenLabs</a>

```json  theme={null}
"tts": {
  "tts_model_name": "sonic"
}
```

### 5. `tts_emotion_control`

If set to `true`, enables emotion control in speech.

<Note>
  Only available for the `cartesia` engine.
</Note>

```json  theme={null}
"tts": {
  "tts_emotion_control": true
}
```

### 6. `voice_settings`

Optional object containing additional settings specific to the selected TTS engine.

These settings vary per engine:

| Parameter           | Cartesia (**Sonic-1 only**)                                  | ElevenLabs                                                  |
| ------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| `speed`             | Range `-1.0` to `1.0` (negative = slower, positive = faster) | Range `0.7` to `1.2` (`0.7` = slowest, `1.2` = fastest)     |
| `emotion`           | Array of `"emotion:level"` tags (e.g., `"positivity:high"`)  | Not available                                               |
| `stability`         | Not available                                                | Range `0.0` to `1.0` (`0.0` = variable, `1.0` = stable)     |
| `similarity_boost`  | Not available                                                | Range `0.0` to `1.0` (`0.0` = creative, `1.0` = original)   |
| `style`             | Not available                                                | Range `0.0` to `1.0` (`0.0` = neutral, `1.0` = exaggerated) |
| `use_speaker_boost` | Not available                                                | Boolean (enhances speaker similarity)                       |

<Note>
  For more information on each voice setting, see:\
  • <a href="https://docs.cartesia.ai/2024-11-13/build-with-cartesia/capability-guides/control-speed-and-emotion" target="_blank">Cartesia Speed and Emotion Controls</a>\
  • <a href="https://elevenlabs.io/docs/api-reference/voices/settings/get" target="_blank">ElevenLabs Voice Settings</a>
</Note>

```json  theme={null}
"tts": {
  "voice_settings": {
    "speed": 0.5,
    "emotion": ["positivity:high", "curiosity"]
  }
}
```

## Example Configuration

Below is an example persona with a fully configured TTS layer:

<CodeGroup>
  ```json Cartesia theme={null}
  {
    "persona_name": "AI Presenter",
    "system_prompt": "You are a friendly and informative video host.",
    "pipeline_mode": "full",
    "context": "You're delivering updates in a conversational tone.",
    "default_replica_id": "r665388ec672",
    "layers": {
      "tts": {
        "tts_engine": "cartesia",
        "api_key": "your-api-key",
        "external_voice_id": "external-voice-id",
        "voice_settings": {
          "speed": "normal",
          "emotion": ["positivity:high", "curiosity"]
        },
        "tts_emotion_control": true,
        "tts_model_name": "sonic"
      }
    }
  }
  ```

  ```json ElevenLabs theme={null}
  {
    "persona_name": "Narrator",
    "system_prompt": "You narrate long stories with clarity and consistency.",
    "pipeline_mode": "full",
    "context": "You're reading a fictional audiobook.",
    "default_replica_id": "r665388ec672",
    "layers": {
      "tts": {
        "tts_engine": "elevenlabs",
        "api_key": "your-api-key",
        "external_voice_id": "elevenlabs-voice-id",
        "voice_settings": {
          "speed": "normal"
        },
        "tts_model_name": "eleven_multilingual_v2"
      }
    }
  }
  ```
</CodeGroup>

<Note>
  Refer to the <a href="https://docs.tavus.io/api-reference/personas/create-persona" target="_blank">Create Persona API</a> for a complete list of supported fields.
</Note>
