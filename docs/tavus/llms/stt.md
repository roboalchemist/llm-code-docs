# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/stt.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Speech-to-Text (STT)

> Learn how to configure the STT layer to enable smart turn detection and enhance conversational flow.

The STT Layer in Tavus empowers your persona to transcribe and comprehend spoken input in real time.

<Note>
  **Turn-taking settings have moved**: Turn-taking is now configured on the [Conversational Flow layer](/sections/conversational-video-interface/persona/conversational-flow).
</Note>

## Configuring the STT Layer

Define the STT layer under the `layers.stt` object. Below are the parameters available:

### 1. `hotwords`

Use this to prioritize certain names or terms that are difficult to transcribe.

<Note>
  This field is only available for `tavus-advanced` engine.
</Note>

```json  theme={null}
"hotwords": "Roey is the name of the person you're speaking with."
```

The above query helps the model transcribe "Roey" correctly instead of "Rowie."

<Tip>
  Use hotwords for proper nouns, brand names, or domain-specific language that standard STT engines might struggle with.
</Tip>

## Example Configuration

Below is an example persona with a fully configured STT layer:

```json  theme={null}
{
  "persona_name": "Customer Service Agent",
  "system_prompt": "You assist users by listening carefully and providing helpful answers.",
  "pipeline_mode": "full",
  "context": "You're handling voice-based customer support inquiries.",
  "default_replica_id": "rfe12d8b9597",
  "layers": {
    "stt": {
      "hotwords": "support"
    }
  }
}
```

<Note>
  Refer to the <a href="/api-reference/personas/create-persona" target="_blank">Create Persona API</a> for a complete list of supported fields.
</Note>
