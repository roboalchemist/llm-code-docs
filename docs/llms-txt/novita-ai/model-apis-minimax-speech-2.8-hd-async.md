# Source: https://novita.ai/docs/api-reference/model-apis-minimax-speech-2.8-hd-async.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# MiniMax Speech 2.8 HD Async Text-to-Speech

MiniMax asynchronous text-to-speech API, supports various voice, emotion, speed and other parameter settings, text length limit up to 50,000 characters, supports file input (up to 100,000 characters)

<Tip>
  This is an **asynchronous** API; only the **task\_id** will be returned. You should use the **task\_id** to request the [**Task Result API**](/api-reference/model-apis-task-result) to retrieve the video generation results.
</Tip>

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Supports: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Request Body

<ParamField body="text" type="string">
  Text to synthesize into audio, maximum length is 50,000 characters. Either `text` or `text_file_id` is required.

  * Interjection tags: Only supported when model is `speech-2.8-hd` or `speech-2.8-turbo`. Supported interjections: `(laughs)` (laughter), `(chuckle)` (light laugh), `(coughs)` (cough), `(clear-throat)` (clear throat), `(groans)` (groan), `(breath)` (normal breathing), `(pant)` (panting), `(inhale)` (inhale), `(exhale)` (exhale), `(gasps)` (gasp), `(sniffs)` (sniff), `(sighs)` (sigh), `(snorts)` (snort), `(burps)` (burp), `(lip-smacking)` (lip smacking), `(humming)` (humming), `(hissing)` (hissing), `(emm)` (um), `(whistles)` (whistle), `(sneezes)` (sneeze), `(crying)` (crying), `(applause)` (applause)
</ParamField>

<ParamField body="text_file_id" type="integer">
  Text file ID for audio synthesis, single file length limit is less than 100,000 characters, supported file formats: txt, zip. Either `text` or `text_file_id` is required, format will be automatically validated.

  * **txt file**: Length limit \<100000 characters. Supports custom pause using `&lt;#x#&gt;` tag. x is pause duration (in seconds), range \[0.01, 99.99], up to 2 decimal places. Pause must be set between two pronounceable text segments, cannot use multiple pause tags consecutively
  * **zip file**:
    * Compressed package must contain txt or json files of the same format.
    * json file format: Supports \[`title`, `content`, `extra`] three fields, representing title, body, and additional information. If all three fields exist, 3 groups of results will be produced, 9 files in total, stored in one folder. If a field does not exist or is empty, no corresponding result will be generated
</ParamField>

<ParamField body="voice_modify" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="pitch" type="integer">
      Pitch adjustment (deep/bright), range \[-100, 100], values closer to -100 produce deeper voice; closer to 100 produce brighter voice

      Value range: \[-100, 100]
    </ParamField>

    <ParamField body="timbre" type="integer">
      Timbre adjustment (rich/crisp), range \[-100, 100], values closer to -100 produce richer voice; closer to 100 produce crisper voice

      Value range: \[-100, 100]
    </ParamField>

    <ParamField body="intensity" type="integer">
      Intensity adjustment (powerful/soft), range \[-100, 100], values closer to -100 produce more powerful voice; closer to 100 produce softer voice

      Value range: \[-100, 100]
    </ParamField>

    <ParamField body="sound_effects" type="string">
      Sound effect setting, only one can be selected at a time. Options:

      1. spacious\_echo (spacious echo)
      2. auditorium\_echo (auditorium broadcast)
      3. lofi\_telephone (telephone distortion)
      4. robotic (electronic)

      Optional values: `spacious_echo`, `auditorium_echo`, `lofi_telephone`, `robotic`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="audio_setting" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="format" type="string" default="mp3">
      Audio output format. Options `[mp3, pcm, flac]`, default is `mp3`

      Optional values: `mp3`, `pcm`, `flac`
    </ParamField>

    <ParamField body="bitrate" type="integer" default={128000}>
      Audio bitrate. Options `[32000, 64000, 128000, 256000]`, default is `128000`. This parameter only applies to `mp3` format
    </ParamField>

    <ParamField body="channel" type="integer" default={2}>
      Number of audio channels. Options: `[1, 2]`, where `1` is mono and `2` is stereo, default is 1
    </ParamField>

    <ParamField body="audio_sample_rate" type="integer" default={32000}>
      Audio sample rate. Options `[8000, 16000, 22050, 24000, 32000, 44100]`, default is `32000`
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="voice_setting" type="object" required={true}>
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="vol" type="number" default={1}>
      Audio volume, higher value means louder. Range (0, 10], default is 1.0

      Value range: \[0, 10]
    </ParamField>

    <ParamField body="pitch" type="integer" default={0}>
      Audio pitch, range `[-12, 12]`, default is 0, where 0 is original voice output

      Value range: \[-12, 12]
    </ParamField>

    <ParamField body="speed" type="number" default={1}>
      Speech speed, higher value means faster. Range `[0.5, 2]`, default is 1.0

      Value range: \[0.5, 2]
    </ParamField>

    <ParamField body="emotion" type="string">
      Controls the emotion of synthesized speech. Options `["happy", "sad", "angry", "fearful", "disgusted", "surprised", "calm", "fluent", "whisper"]` correspond to 8 emotions: happy, sad, angry, fearful, disgusted, surprised, calm, fluent, whisper

      * The model will automatically match appropriate emotion based on input text, usually no need to specify manually
      * This parameter only works for `speech-2.6-hd`, `speech-2.6-turbo`, `speech-02-hd`, `speech-02-turbo`, `speech-01-hd`, `speech-01-turbo` models
      * Options `fluent`, `whisper` only work for `speech-2.6-turbo`, `speech-2.6-hd` models

      Optional values: `happy`, `sad`, `angry`, `fearful`, `disgusted`, `surprised`, `calm`, `fluent`, `whisper`
    </ParamField>

    <ParamField body="voice_id" type="string" required={true}>
      Voice ID for audio synthesis. If mixed voice is needed, set timber\_weights parameter and leave this empty. Supports system voice, cloned voice, and text-generated voice. Below are some of the latest system voices (ID)

      <ul>
        <li><strong>Chinese</strong>: moss\_audio\_ce44fc67-7ce3-11f0-8de5-96e35d26fb85, moss\_audio\_aaa1346a-7ce7-11f0-8e61-2e6e3c7ee85d, Chinese (Mandarin)\_Lyrical\_Voice, Chinese (Mandarin)\_HK\_Flight\_Attendant</li>
        <li><strong>English</strong>: English\_Graceful\_Lady, English\_Insightful\_Speaker, English\_radiant\_girl, English\_Persuasive\_Man, moss\_audio\_6dc281eb-713c-11f0-a447-9613c873494c, moss\_audio\_570551b1-735c-11f0-b236-0adeeecad052, moss\_audio\_ad5baf92-735f-11f0-8263-fe5a2fe98ec8, English\_Lucky\_Robot</li>
        <li><strong>Japanese</strong>: Japanese\_Whisper\_Belle, moss\_audio\_24875c4a-7be4-11f0-9359-4e72c55db738, moss\_audio\_7f4ee608-78ea-11f0-bb73-1e2a4cfcd245, moss\_audio\_c1a6a3ac-7be6-11f0-8e8e-36b92fbb4f95</li>
      </ul>
    </ParamField>

    <ParamField body="english_normalization" type="boolean" default={false}>
      Supports English text normalization, which can improve performance in number reading scenarios but slightly increases latency, default false
    </ParamField>
  </Expandable>
</ParamField>

<ParamField body="aigc_watermark" type="boolean" default={false}>
  Controls whether to add audio rhythm identifier at the end of synthesized audio, default is False. This parameter is only valid for non-streaming synthesis
</ParamField>

<ParamField body="language_boost" type="string">
  Whether to enhance recognition ability for specified minor languages and dialects. Default is `null`, can be set to `auto` to let the model decide automatically.

  Optional values: `Chinese`, `Chinese,Yue`, `English`, `Arabic`, `Russian`, `Spanish`, `French`, `Portuguese`, `German`, `Turkish`, `Dutch`, `Ukrainian`, `Vietnamese`, `Indonesian`, `Japanese`, `Italian`, `Korean`, `Thai`, `Polish`, `Romanian`, `Greek`, `Czech`, `Finnish`, `Hindi`, `Bulgarian`, `Danish`, `Hebrew`, `Malay`, `Persian`, `Slovak`, `Swedish`, `Croatian`, `Filipino`, `Hungarian`, `Norwegian`, `Slovenian`, `Catalan`, `Nynorsk`, `Tamil`, `Afrikaans`, `auto`
</ParamField>

<ParamField body="continuous_sound" type="boolean" default={false}>
  Enable this parameter to make clause transitions more natural, only supported by `speech-2.8-hd` and `speech-2.8-turbo` models
</ParamField>

<ParamField body="pronunciation_dict" type="object">
  <Expandable title="properties" defaultOpen={true}>
    <ParamField body="tone" type="array">
      Defines pronunciation or replacement rules for special characters or symbols. For Chinese text, tones are represented by numbers:
      1st tone = 1, 2nd tone = 2, 3rd tone = 3, 4th tone = 4, neutral tone = 5
      Example:
      `["omg/oh my god"]`
    </ParamField>
  </Expandable>
</ParamField>

## Response

<ResponseField name="file_id" type="integer" required={false}>
  Corresponding audio file ID returned after task creation.

  * After task completion, use file\_id to download

  * This field is not returned when request fails

  Note: The download URL is valid for 9 hours (32400 seconds) from generation. After expiration, the file will become invalid and generated information will be lost. Please pay attention to download timing
</ResponseField>

<ResponseField name="task_id" type="string" required={false}>
  Use the task\_id to retrieve the generated outputs.
</ResponseField>

<ResponseField name="base_resp" type="object" required={false}>
  <Expandable title="properties" defaultOpen={true}>
    <ResponseField name="status_msg" type="string" required={true}>
      Status details
    </ResponseField>

    <ResponseField name="status_code" type="integer" required={true}>
      Status code

      <ul>
        <li>`0`: Success</li>
        <li>`1002`: Rate limit</li>
        <li>`1004`: Authentication failed</li>
        <li>`1039`: TPM rate limit triggered</li>
        <li>`1042`: Invalid characters exceed 10%</li>
        <li>`2013`: Parameter error</li>
      </ul>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="task_token" type="string" required={false}>
  Token used to complete the current task
</ResponseField>

<ResponseField name="usage_characters" type="integer" required={false}>
  Billable character count
</ResponseField>


Built with [Mintlify](https://mintlify.com).