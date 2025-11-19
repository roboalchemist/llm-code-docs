# Source: https://docs.tavus.io/sections/conversational-video-interface/language-support.md

# Language Support

> Customize the conversation language using full language names supported by Tavus TTS engines.

## Supported Languages

Tavus supports over 30 languages for spoken interaction, powered by two integrated text-to-speech (TTS) engines: Cartesia and ElevenLabs.
If a selected language is not supported by our default TTS engine (Cartesia), your CVI will automatically switch to ElevenLabs to kick off the conversation.

* English (all variants)
* French (France, Canada)
* German
* Spanish (Spain, Mexico)
* Portuguese (Brazil, Portugal)
* Chinese
* Japanese
* Hindi
* Italian
* Korean
* Dutch
* Polish
* Russian
* Swedish
* Turkish
* Indonesian
* Filipino
* Bulgarian
* Romanian
* Arabic (Saudi Arabia, UAE)
* Czech
* Greek
* Finnish
* Croatian
* Malay
* Slovak
* Danish
* Tamil
* Ukrainian
* Hungarian
* Norwegian
* Vietnamese

For a full list of supported languages for each TTS engine, please click on the following links:

<CardGroup cols={2}>
  <Card title="Cartesia (default)" icon="c" href="https://docs.cartesia.ai/2024-11-13/build-with-cartesia/models/tts#language-support" cta="View supported languages" />

  <Card title="ElevenLabs" icon="tally-2" href="https://elevenlabs.io/docs/capabilities/text-to-speech#supported-languages" cta="View supported languages" />
</CardGroup>

<Note>
  By default, Tavus uses the **Cartesia** TTS engine.
</Note>

## Setting the Conversation Language

To specify a language, use the `language` parameter in the <a href="/api-reference/conversations/create-conversation" target="_blank" rel="noopener noreferrer">Create Conversation</a>. **You must use the full language name**, not a language code.

```shell cURL {9} theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/conversations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api_key>' \
  --data '{
  "persona_id": "pdced222244b",
  "replica_id": "rfe12d8b9597",
  "properties": {
    "language": "spanish"
   }
}'
```

<Note>
  Language names must match exactly with those supported by the selected TTS engine.
</Note>

### Smart Language Detection

To automatically detect the participant’s spoken language throughout the conversation, set `language` to `multilingual` when creating the conversation:

```shell cURL {9} theme={null}
curl --request POST \
  --url https://tavusapi.com/v2/conversations \
  --header 'Content-Type: application/json' \
  --header 'x-api-key: <api_key>' \
  --data '{
  "persona_id": "pdced222244b",
  "replica_id": "rfe12d8b9597",
  "properties": {
    "language": "multilingual"
   }
}'
```

This enables ASR (Automatic Speech Recognition) to automatically switch languages, dynamically adjusting the pipeline to transcribe and respond in the detected language throughout the conversation.
