# Source: https://novita.ai/docs/api-reference/model-apis-minimax-speech-2.8-turbo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Speech 2.8 Turbo Sync Text-to-Speech

MiniMax synchronous text-to-speech API using HTTP protocol. Supports various voice, emotion, speed and other parameter settings.

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="text" type="string" required={true}>
  Text to synthesize into speech, length limit is less than 10000 characters. If text length is greater than 3000 characters, streaming output is recommended. Supports paragraph breaks (newline), pause control (`&lt;#x#&gt;` tag), and interjection tags (such as (laughs), (coughs), etc., only supported by speech-2.8-hd/turbo)
</ParamField>

<ParamField body="stream" type="boolean" default={false}>
  Controls whether to enable streaming output. Default is false
</ParamField>

<ParamField body="voice_modify" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="pitch" type="integer">
      Pitch adjustment (deep/bright), range \[-100, 100]. Values closer to -100 produce deeper voice; closer to 100 produce brighter voice

      Value range: \[-100, 100]
    </ParamField>

    <ParamField body="timbre" type="integer">
      Timbre adjustment (rich/crisp), range \[-100, 100]. Values closer to -100 produce richer voice; closer to 100 produce crisper voice

      Value range: \[-100, 100]
    </ParamField>

    <ParamField body="intensity" type="integer">
      Intensity adjustment (powerful/soft), range \[-100, 100]. Values closer to -100 produce more powerful voice; closer to 100 produce softer voice

      Value range: \[-100, 100]
    </ParamField>

    <ParamField body="sound_effects" type="string">
      Sound effect setting, only one can be selected at a time. Options: spacious\_echo (spacious echo), auditorium\_echo (auditorium broadcast), lofi\_telephone (telephone distortion), robotic (electronic)

      Optional values: `spacious_echo`, `auditorium_echo`, `lofi_telephone`, `robotic`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="audio_setting" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="format" type="string" default="mp3">
      Audio output format. wav is only supported in non-streaming output

      Optional values: `mp3`, `pcm`, `flac`, `wav`
    </ParamField>

    <ParamField body="bitrate" type="integer" default={128000}>
      Audio bitrate. Options: \[32000, 64000, 128000, 256000], default is 128000. This parameter only applies to mp3 format

      Optional values: `32000`, `64000`, `128000`, `256000`
    </ParamField>

    <ParamField body="channel" type="integer" default={1}>
      Number of audio channels. Options: \[1, 2], where 1 is mono and 2 is stereo. Default is 1

      Optional values: `1`, `2`
    </ParamField>

    <ParamField body="force_cbr" type="boolean" default={false}>
      Controls constant bitrate (CBR) encoding. When set to true, audio will be encoded with constant bitrate. Note: This parameter only works when streaming output is enabled and audio format is mp3
    </ParamField>

    <ParamField body="sample_rate" type="integer" default={32000}>
      Audio sample rate. Options: \[8000, 16000, 22050, 24000, 32000, 44100], default is 32000

      Optional values: `8000`, `16000`, `22050`, `24000`, `32000`, `44100`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="output_format" type="string" default="hex">
  Controls output format, options are url or hex, default is hex. This parameter is only valid in non-streaming scenarios. URL is valid for 24 hours

  Optional values: `url`, `hex`
</ParamField>

<ParamField body="voice_setting" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="vol" type="number" default={1}>
      Audio volume, higher value means louder. Range (0, 10], default is 1.0

      Value range: \[0, 10]
    </ParamField>

    <ParamField body="pitch" type="integer" default={0}>
      Audio pitch, range \[-12, 12], default is 0, where 0 is original voice output

      Value range: \[-12, 12]
    </ParamField>

    <ParamField body="speed" type="number" default={1}>
      Speech speed, higher value means faster. Range \[0.5, 2], default is 1.0

      Value range: \[0.5, 2]
    </ParamField>

    <ParamField body="emotion" type="string">
      Controls the emotion of synthesized speech. Options correspond to 8 emotions: happy, sad, angry, fearful, disgusted, surprised, calm, fluent, whisper. The model will automatically match appropriate emotion based on input text

      Optional values: `happy`, `sad`, `angry`, `fearful`, `disgusted`, `surprised`, `calm`, `fluent`, `whisper`
    </ParamField>

    <ParamField body="voice_id" type="string" required={true}>
      Voice ID for audio synthesis. If mixed voice is needed, set timber\_weights parameter and leave this empty. Supports system voice, cloned voice, and text-generated voice
    </ParamField>

    <ParamField body="latex_read" type="boolean" default={false}>
      Controls whether to read LaTeX formulas, default is false. Only supports Chinese. When enabled, language\_boost will be set to Chinese
    </ParamField>

    <ParamField body="text_normalization" type="boolean" default={false}>
      Whether to enable Chinese/English text normalization, which can improve performance in number reading scenarios but slightly increases latency. Default is false
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="aigc_watermark" type="boolean" default={false}>
  Controls whether to add audio rhythm identifier at the end of synthesized audio, default is false. This parameter is only valid for non-streaming synthesis
</ParamField>

<ParamField body="language_boost" type="string">
  Whether to enhance recognition ability for specified minor languages and dialects. Default is null, can be set to auto to let the model decide automatically

  Optional values: `Chinese`, `Chinese,Yue`, `English`, `Arabic`, `Russian`, `Spanish`, `French`, `Portuguese`, `German`, `Turkish`, `Dutch`, `Ukrainian`, `Vietnamese`, `Indonesian`, `Japanese`, `Italian`, `Korean`, `Thai`, `Polish`, `Romanian`, `Greek`, `Czech`, `Finnish`, `Hindi`, `Bulgarian`, `Danish`, `Hebrew`, `Malay`, `Persian`, `Slovak`, `Swedish`, `Croatian`, `Filipino`, `Hungarian`, `Norwegian`, `Slovenian`, `Catalan`, `Nynorsk`, `Tamil`, `Afrikaans`, `auto`
</ParamField>

<ParamField body="stream_options" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="exclude_aggregated_audio" type="boolean" default={false}>
      Sets whether the last chunk contains the concatenated audio hex data. Default is false, meaning the last chunk contains the complete concatenated audio hex data
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="timber_weights" type="array">
  Mixed voice settings, supports up to 4 voice mixtures

  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="weight" type="integer" required={true}>
      Weight of each voice in the mix, must be set together with voice\_id. Range \[1, 100], supports up to 4 voice mixtures. Higher weight means more similarity to that voice

      Value range: \[1, 100]
    </ParamField>

    <ParamField body="voice_id" type="string" required={true}>
      Voice ID for audio synthesis, must be set together with weight parameter. Supports system voice, cloned voice, and text-generated voice
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="subtitle_enable" type="boolean" default={false}>
  Controls whether to enable subtitle service, default is false. This parameter is only valid in non-streaming output scenarios, and only valid for speech-2.6-hd, speech-2.6-turbo, speech-02-turbo, speech-02-hd, speech-01-turbo, speech-01-hd models
</ParamField>

<ParamField body="continuous_sound" type="boolean" default={false}>
  Enable this parameter to make clause transitions more natural, only supported by speech-2.8-hd and speech-2.8-turbo models
</ParamField>

<ParamField body="pronunciation_dict" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="tone" type="array">
      Defines pronunciation or replacement rules for special characters or symbols. For Chinese text, tones are represented by numbers: 1st tone = 1, 2nd tone = 2, 3rd tone = 3, 4th tone = 4, neutral tone = 5. Example: \["omg/oh my god"]
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="data" type="object" required={false}>
  Returned synthesis data object, may be null and needs null check

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="audio" type="string" required={false}>
      Synthesized audio data in hex encoding, format matches the output format specified in request
    </ResponseField>

    <ResponseField name="status" type="integer" required={false}>
      Current audio stream status: 1 means synthesizing, 2 means synthesis completed
    </ResponseField>

    <ResponseField name="subtitle_file" type="string" required={false}>
      Subtitle download link. Subtitles for the audio file, accurate to sentence (no more than 50 characters), in milliseconds, JSON format
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="trace_id" type="string" required={false}>
  Session ID for this request, used for troubleshooting
</ResponseField>

<ResponseField name="base_resp" type="object" required={false}>
  Status code and details for this request

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="status_msg" type="string" required={false}>
      Status details
    </ResponseField>

    <ResponseField name="status_code" type="integer" required={false}>
      Status code. `0`: success, `1000`: unknown error, `1001`: timeout, `1002`: rate limit triggered, `1004`: authentication failed, `1039`: TPM rate limit triggered, `1042`: invalid characters exceed 10%, `2013`: invalid input parameters
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="extra_info" type="object" required={false}>
  Additional audio information

  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="bitrate" type="integer" required={false}>
      Audio bitrate
    </ResponseField>

    <ResponseField name="audio_size" type="integer" required={false}>
      Audio file size in bytes
    </ResponseField>

    <ResponseField name="word_count" type="integer" required={false}>
      Word count of pronounced text, includes Chinese characters, numbers, letters, excludes punctuation
    </ResponseField>

    <ResponseField name="audio_format" type="string" required={false}>
      Generated audio file format. Options: \[mp3, pcm, flac]

      Optional values: `mp3`, `pcm`, `flac`
    </ResponseField>

    <ResponseField name="audio_length" type="integer" required={false}>
      Audio duration in milliseconds
    </ResponseField>

    <ResponseField name="audio_channel" type="integer" required={false}>
      Generated audio channel count, `1`: mono, `2`: stereo
    </ResponseField>

    <ResponseField name="usage_characters" type="integer" required={false}>
      Billable character count
    </ResponseField>

    <ResponseField name="audio_sample_rate" type="integer" required={false}>
      Audio sample rate
    </ResponseField>

    <ResponseField name="invisible_character_ratio" type="number" required={false}>
      Invalid character ratio. If invalid characters do not exceed 10% (inclusive), audio will be generated normally with this ratio data returned; if exceeds 10%, an error will be returned
    </ResponseField>
  </Expandable>
</ResponseField>


Built with [Mintlify](https://mintlify.com).