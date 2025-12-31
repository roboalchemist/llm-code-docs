# Source: https://docs.tavus.io/sections/conversational-video-interface/persona/stt.md

# Speech-to-Text (STT)

> Learn how to configure the STT layer to enable smart turn detection and enhance conversational flow.

The STT Layer in Tavus empowers your persona to transcribe and comprehend spoken input in real time. By default, the STT layer in Tavus leverages `smart_turn_detection`, powered by **Sparrow**, for dynamic and responsive conversation flow with intelligent turn-taking.

## Configuring the STT Layer

Define the STT layer under the `layers.stt` object. Below are the parameters available:

### 1. `participant_pause_sensitivity`

Controls how long the participant can pause before the replica responds. This setting helps you fine-tune the pacing of the conversation.

* **Options**:

  * `high`: The replica replies quickly after short pauses. Good for fast and casual conversations.
  * `medium` **(default)**: Balanced timing. Allows natural pauses without feeling rushed or delayed.
  * `low`: The replica waits a bit longer before replying. Useful for slower or more thoughtful discussions.
  * `verylow`: The replica allows even longer pauses before responding.
  * `superlow`: The replica has the longest response delay, making it suitable for conversations where participants often pause.

```json  theme={null}
"participant_pause_sensitivity": "medium"
```

### 2. `participant_interrupt_sensitivity`

Controls how easily the participant can interrupt the replica while it is talking. This setting helps adjust how the replica handles overlap in conversation.

* **Options**:

  * `high`: The replica stops speaking immediately when the participant starts talking. Ideal for quick and back-and-forth exchanges.
  * `medium` **(default)**: Balanced behavior. Allows short interruptions without breaking the flow.
  * `low`: The participant needs to speak more clearly or for a bit longer to interrupt.
  * `verylow`: The replica usually keeps talking unless the interruption is strong.
  * `superlow`: The replica rarely stops mid-sentence. It will usually finish speaking before responding.

```json  theme={null}
"participant_interrupt_sensitivity": "medium"
```

### 3. `hotwords`

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

### 4. `Turn-taking model`

Enables dynamic turn-taking using the Sparrow model, which dynamically adjusts the timeout based on what the users say. It sets a longer timeout when the user is likely not done speaking, and a shorter timeout when the user is likely done speaking.

```json  theme={null}
"smart_turn_detection": true
```

#### How Turn-taking Works

<Frame>
    <img src="https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/stt-works.png?fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=110b73821f8b6dee00a4378ab722ecca" alt="" data-og-width="1685" width="1685" data-og-height="1599" height="1599" data-path="images/stt-works.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/stt-works.png?w=280&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=9b1893d42587b724b77473127b595a19 280w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/stt-works.png?w=560&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=5c4ae544e7815e82643097cbbb1bbde4 560w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/stt-works.png?w=840&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=4ee1a2c64f33605f991b88e725d53114 840w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/stt-works.png?w=1100&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=faf5f0a4c4856ae74d07965eee1e879c 1100w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/stt-works.png?w=1650&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=b45145be3e8d2bf64db52e08d99b7afc 1650w, https://mintcdn.com/tavus/_cI_e0wGUkj7b2SY/images/stt-works.png?w=2500&fit=max&auto=format&n=_cI_e0wGUkj7b2SY&q=85&s=bcfc157c7293200aad614a7d699e7960 2500w" />
</Frame>

<Warning>
  * `smart_turn_detection` is only supported by the `tavus-advanced` engine.
  * Disabling `smart_turn_detection` turns off **Sparrow** and uses a fixed response delay based on `participant_pause_sensitivity`.
</Warning>

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
      "participant_pause_sensitivity": "medium",
      "participant_interrupt_sensitivity": "low",
      "hotwords": "support",
      "smart_turn_detection": true
    }
  }
}
```

<Note>
  Refer to the <a href="/api-reference/personas/create-persona" target="_blank">Create Persona API</a> for a complete list of supported fields.
</Note>
