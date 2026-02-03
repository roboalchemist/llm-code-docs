# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses/advanced-settings.md

# Source: https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/advanced-settings.md

# Source: https://docs.avaamo.com/user-guide/skills/prompt-skill/advanced-settings.md

# Advanced Settings

The **Advanced Settings** section lets you configure and fine-tune your agent's behavior, ensuring optimal performance during customer interactions. This includes selecting the AI model, defining a voice persona, adding custom parameters, and adding ASR Entities.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FNsTJWoTpVmUyZpZReYAp%2FScreenshot%202025-10-14%20at%2011.49.37%E2%80%AFAM.png?alt=media&#x26;token=02ca1b9a-91a2-43c9-83b0-650dada87690" alt=""><figcaption></figcaption></figure>

### Model Selection

Users can choose from available AI models to power their assistants. The model determines the assistant's processing capability, response accuracy, and efficiency.

You can choose a voice from the dropdown list.

### Voice Persona

The **Voice Persona** setting allows users to define the assistant's voice characteristics. Different voice personas cater to different user experiences, ensuring a more engaging, natural interaction.&#x20;

You can choose a voice from the dropdown list.

### Advanced Customization Parameters

You can include custom parameters to fine-tune or modify the assistant’s behavior.&#x20;

You can assign values by entering the parameter key and its parameter value in the available fields, and then click `Add`.

Below are some examples of Parameter key and Parameter Value.

| Parameter key         | Parameter Value                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------- |
| tts\_props            | {"voice": "Heart"}                                                                           |
| tts\_props            | {"instructions": "Speak in a calm and friendly tone with clear pauses.","speed": <0.25–4.0>} |
| disable\_idle\_prompt | true                                                                                         |
| enable\_barge\_in     | true                                                                                         |

For example, enter `tts_props` in the Parameter Key field and `{"instructions": "Speak in a calm and friendly tone with clear pauses.","speed": <0.25–4.0>}` in the Parameter Value field. Then click **Add** to include the advanced custom parameters.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F1ul9YEhuKIBfYayoJ9rB%2FScreenshot%202025-12-03%20at%2012.27.39%E2%80%AFPM.png?alt=media&#x26;token=cd26aa35-1762-4a0b-a571-d88c613486eb" alt=""><figcaption></figcaption></figure>

The list below contains the commonly used TTS configuration options and their supported values.

1. **OpenAI Custom Configuration:** If you select an OpenAI voice persona such as Alloy, Ash, or Onyx, you can enter the parameter key and value using the format and examples shown below.

Format:

```json
tts_props: {
  "instructions": "<tts prompt>",
  "speed": <0.25–4.0>
}
```

Example:

```json
tts_props: {
  "instructions": "Speak in a calm and friendly tone with clear pauses.",
  "speed": 1.2
}
```

Additional examples for OpenAI voice instructions:

* **Affect / Personality:** Warm, professional medical concierge — attentive and reassuring.
* **Tone:** Even, sincere, conversational. Avoid sounding singsong, overly cheerful, or robotic. Maintain a neutral warmth that makes the listener feel cared for.
* **Pronunciation:** Clear and precise, as if confirming essential details over the phone.
* **Emotion:** Calm and reassuring, especially during authentication or while reading appointment details.
* **Pacing:** Natural, steady pace with slight upward inflection for questions and micro-pauses between phrases.
* **Pauses:** Insert a short pause before/after apologies and after the compliance notice.
* **Accent:** Soft **Southern American** accent — gentle drawl, slightly elongated vowels, warm and hospitable, but always clear.
* **Rhythm:** Slightly vary the sentence melody to avoid monotony. Add soft warmth in transitions (e.g., “Alright,” “Let’s see”).
* **Acknowledgment Rule:** Before asking the next question, briefly acknowledge the patient’s last response with a short, neutral sentence.
  * Examples: *“Thank you for sharing that.”*, *“Alright, I understand.”*, *“Got it, thanks.”*, *“I appreciate that.”*

2. **Eleven Labs Custom Configs:** If you select an ElevenLabs voice persona, you can enter the parameter key and value using the format and examples shown below.

Format:

```json
tts_props: {
  "speed": <0.7–1.2>,
  "style": <0.0–1.0>,
  "stability": <0.0–1.0>,
  "similarity_boost": <0.0–1.0>,
  "use_speaker_boost": <true/false>
}
```

Example:

```json
tts_props: {
  "speed": 1.0,
  "style": 0.8,
  "stability": 0.6,
  "similarity_boost": 0.9,
  "use_speaker_boost": true
}
```

3. **Avaamo one-shot voices:** If you select a one-shot voice persona, you can enter the parameter key and value using the format and examples shown below.

Format:

```json
tts_props: {
  "voice": "<VOICE_NAME>"
}
```

Example:

```json
tts_props: {
  "voice": "Heart"
}
```

### ASR Entities

You can select the available ASR entities from the dropdown list.
