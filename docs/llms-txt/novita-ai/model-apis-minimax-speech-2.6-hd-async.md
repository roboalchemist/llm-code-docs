# Source: https://novita.ai/docs/api-reference/model-apis-minimax-speech-2.6-hd-async.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Speech-2.6-hd Async Long TTS

MiniMax's high-definition text-to-speech model, Compared to Speech 02 released in May, Speech 2.6 has three major breakthroughs: stronger multilingual expressiveness, more accurate voice replication, and broader coverage with 40 languages.

<Tip>Best suited for long-form text-to-speech generation, such as entire books. Task queue times may be longer. For short sentence generation, voice chat, or online social scenarios, we recommend using [synchronous TTS](/api-reference/model-apis-minimax-speech-2.6-hd).</Tip>

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="text" type="string" required={true}>
  The text to be synthesized. Maximum length: 50,000 characters.
</ParamField>

<ParamField body="voice_setting" type="object" required={true}>
  <Expandable title="properties">
    <ParamField body="speed" type="number" default={1.0}>
      Range: \[0.5, 2], default is 1.0.

      Controls the speech rate of the generated audio. Optional. Higher values result in faster speech.
    </ParamField>

    <ParamField body="vol" type="number" default={1.0}>
      Range: (0, 10], default is 1.0.

      Controls the volume of the generated audio. Optional. Higher values result in louder audio.
    </ParamField>

    <ParamField body="pitch" type="number" default={0}>
      Range: \[-12, 12], default is 0.

      Controls the pitch of the generated audio. Optional. 0 means original timbre. The value must be an integer.
    </ParamField>

    <ParamField body="voice_id" type="string">
      The requested voice ID.

      Supports both system voices (ID) and cloned voices (ID). The available system voice IDs are as follows:

      * Wise\_Woman
      * Friendly\_Person
      * Inspirational\_girl
      * Deep\_Voice\_Man
      * Calm\_Woman
      * Casual\_Guy
      * Lively\_Girl
      * Patient\_Man
      * Young\_Knight
      * Determined\_Man
      * Lovely\_Girl
      * Decent\_Boy
      * Imposing\_Manner
      * Elegant\_Man
      * Abbess
      * Sweet\_Girl\_2
      * Exuberant\_Girl
    </ParamField>

    <ParamField body="emotion" type="string">
      Controls the emotion of the synthesized speech.

      Currently supports 7 emotions: happy, sad, angry, fearful, disgusted, surprised, neutral.

      Allowed values: `["happy", "sad", "angry", "fearful", "disgusted", "surprised", "neutral"]`
    </ParamField>

    <ParamField body="text_normalization" type="bool" default="false">
      This parameter supports English text normalization, which improves performance in number-reading scenarios, but this comes at the cost of a slight increase in latency. If not provided, the default is false.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="audio_setting" type="object">
  <Expandable title="properties">
    <ParamField body="sample_rate" type="number" default={32000}>
      Range: \[8000, 16000, 22050, 24000, 32000, 44100]

      The sample rate of the generated audio. Optional, default is 32000.
    </ParamField>

    <ParamField body="bitrate" type="number" default={128000}>
      Range: \[32000, 64000, 128000, 256000]

      The bitrate of the generated audio. Optional, default is 128000. This parameter only applies to mp3 audio format.
    </ParamField>

    <ParamField body="format" type="string" default="mp3">
      The audio format of the output. Default is mp3. Options: `mp3`, `pcm`, `flac`, `wav`. wav is only supported for non-streaming output.
    </ParamField>

    <ParamField body="channel" type="number" default={1}>
      Number of audio channels. Default is 1 (mono). Options:

      1: mono

      2: stereo
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="pronunciation_dict" type="object">
  <Expandable title="properties">
    <ParamField body="tone" type="list">
      Replacement of text, symbols and corresponding pronunciations that require manual handling.
      Replace the pronunciation (adjust the tone/replace the pronunciation of other characters) using the following format:

      \[“omg/oh my god”]

      For Chinese texts, tones are replaced by numbers, with 1 for the first tone (high), 2 for the second tone (rising), 3 for the third tone (low/dipping), 4 for the fourth tone (falling), and 5 for the fifth tone (neutral).
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="language_boost" type="string" default="null">
  Enhances recognition of specified minor languages and dialects. Setting this parameter can improve speech performance in the specified language/dialect scenarios. If the minor language type is not clear, you can set it to "auto" and the model will automatically determine the language type. Supported values:

  `'Chinese', 'Chinese,Yue', 'English', 'Arabic', 'Russian', 'Spanish', 'French', 'Portuguese', 'German', 'Turkish', 'Dutch', 'Ukrainian', 'Vietnamese', 'Indonesian', 'Japanese', 'Italian', 'Korean', 'Thai', 'Polish', 'Romanian', 'Greek', 'Czech', 'Finnish', 'Hindi', 'Bulgarian', 'Danish', 'Hebrew', 'Malay', 'Persian', 'Slovak', 'Swedish', 'Croatian', 'Filipino', 'Hungarian', 'Norwegian', 'Slovenian', 'Catalan', 'Nynorsk', 'Tamil', 'Afrikaans', 'auto'`
</ParamField>

<ParamField body="voice_modify" type="object">
  Voice FX settings. Supported audio formats for this parameter: mp3, wav, flac

  <Expandable title="properties">
    <ParamField body="pitch" type="integer">
      Pitch adjustment (darker/brighter). Range: \[-100, 100]. Values closer to -100 generate a deeper (darker) voice; values closer to 100 produce a brighter voice.
    </ParamField>

    <ParamField body="intensity" type="integer">
      Intensity adjustment (powerful/soft). Range: \[-100, 100]. Values closer to -100 generate a more powerful sound; values closer to 100 result in a softer sound.
    </ParamField>

    <ParamField body="timbre" type="integer">
      Timbre adjustment (magnetic/crisp). Range: \[-100, 100]. Values closer to -100 make the voice more full/magnetic; values closer to 100 make it crisper.
    </ParamField>

    <ParamField body="sound_effects" type="string">
      Sound effect setting (only one may be selected per request). Valid values:

      * `spacious_echo` (large space echo)
      * `auditorium_echo` (auditorium broadcast)
      * `lofi_telephone` (telephone distortion)
      * `robotic` (robotic effect)
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="task_id" type="string" required={false}>
  Use the task\_id to request the [Task Result API](/api-reference/model-apis-task-result) to retrieve the generated outputs.
</ResponseField>


Built with [Mintlify](https://mintlify.com).