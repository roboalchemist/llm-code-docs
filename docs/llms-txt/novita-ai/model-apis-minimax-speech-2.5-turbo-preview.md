# Source: https://novita.ai/docs/api-reference/model-apis-minimax-speech-2.5-turbo-preview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Speech-2.5-turbo-preview Text to Speech

MiniMax's high-definition text-to-speech model, Compared to Speech 02 released in May, Speech 2.5 has three major breakthroughs: stronger multilingual expressiveness, more accurate voice replication, and broader coverage with 40 languages.

<Tip>Best suited for short sentence generation, voice chat, and online social scenarios. Processing is fast, but the text length is limited to less than 10,000 characters. For long-form text, we recommend using [asynchronous TTS synthesis](/api-reference/model-apis-minimax-speech-2.5-turbo-preview-async).</Tip>

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="text" type="string" required={true}>
  The text to be synthesized. The length must be less than 10,000 characters. Use line breaks to separate paragraphs.\
  To control the pause duration between speech segments, insert `<#x#>` between words or sentences, where `x` is the pause duration in seconds (supports 0.01–99.99, up to two decimal places).\
  Custom speech pauses between text segments are supported, allowing you to control the timing of pauses in the generated audio.\
  Note: Pause markers must be placed between two segments that can be pronounced, and multiple consecutive pause markers are not allowed.
</ParamField>

<ParamField body="voice_setting" type="object" required={true}>
  <Expandable title="properties">
    <ParamField body="speed" type="float" default="1.0">
      Range: \[0.5, 2], default is 1.0

      Controls the speech rate of the generated audio. Optional. Higher values result in faster speech.
    </ParamField>

    <ParamField body="vol" type="float" default="1.0">
      Range: (0, 10], default is 1.0

      Controls the volume of the generated audio. Optional. Higher values result in louder audio.
    </ParamField>

    <ParamField body="pitch" type="int" default="0">
      Range: \[-12, 12], default is 0

      Controls the pitch of the generated audio. Optional. 0 means original timbre. The value must be an integer.
    </ParamField>

    <ParamField body="voice_id" type="string">
      The requested timbre ID. Required (choose either this or timbre\_weights).

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

<ParamField body="timbre_weights" type="object[]">
  Required if voice\_id is not provided (choose one of the two).

  <Expandable title="properties">
    <ParamField body="voice_id" type="string">
      The requested timbre ID. Must be provided together with the weight parameter.
    </ParamField>

    <ParamField body="weight" type="number">
      Range: \[1, 100]

      The weight, must be provided together with voice\_id. Up to 4 timbres can be mixed. The value must be an integer. The higher the proportion for a single timbre, the more the synthesized voice will resemble it.
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="stream" type="boolean" default="false">
  Whether to enable streaming. Default is false, i.e., streaming is disabled.
</ParamField>

<ParamField body="language_boost" type="string" default="null">
  Enhances recognition of specified minor languages and dialects. Setting this parameter can improve speech performance in the specified language/dialect scenarios. If the minor language type is not clear, you can set it to "auto" and the model will automatically determine the language type. Supported values:

  `'Chinese', 'Chinese,Yue', 'English', 'Arabic', 'Russian', 'Spanish', 'French', 'Portuguese', 'German', 'Turkish', 'Dutch', 'Ukrainian', 'Vietnamese', 'Indonesian', 'Japanese', 'Italian', 'Korean', 'Thai', 'Polish', 'Romanian', 'Greek', 'Czech', 'Finnish', 'Hindi', 'Bulgarian', 'Danish', 'Hebrew', 'Malay', 'Persian', 'Slovak', 'Swedish', 'Croatian', 'Filipino', 'Hungarian', 'Norwegian', 'Slovenian', 'Catalan', 'Nynorsk', 'Tamil', 'Afrikaans', 'auto'`
</ParamField>

<ParamField body="output_format" type="string" default="hex">
  Controls the output format of the result. Optional values are `url` and `hex`. The default is `hex`. This parameter only takes effect in non-streaming scenarios; in streaming mode, only hex format is supported. The returned URL is valid for 24 hours.
</ParamField>

<ParamField body="voice_modify" type="object">
  Voice FX settings. Supported audio formats for this parameter:

  * Non-streaming: mp3, wav, flac
  * Streaming: mp3

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

<ResponseField name="audio" type="string">
  The synthesized audio segment, encoded in hex and generated in the format specified by `audio_setting.format` (mp3/pcm/flac). The return format is determined by the `output_format` parameter. When `stream` is true, only hex format is supported.
</ResponseField>

<ResponseField name="status" type="number">
  The current status of the audio stream. Returned only when `stream` is true. 1 indicates synthesis in progress, 2 indicates synthesis completed.
</ResponseField>


Built with [Mintlify](https://mintlify.com).