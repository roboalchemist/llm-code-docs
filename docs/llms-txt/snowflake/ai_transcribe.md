# Source: https://docs.snowflake.com/en/sql-reference/functions/ai_transcribe.md

Categories:
:   [File functions](../functions-file.md) (AI Functions)

# AI_TRANSCRIBE

Transcribes text from an audio or video file with optional timestamps and speaker labels. AI_TRANSCRIBE supports
[numerous languages](../../user-guide/snowflake-cortex/ai-audio.md), and
audio can contain more than one language. Timestamps and speaker labels are extracted based on the specified timestamp
granularity, as shown in the table below.

| Timestamp granularity | Result |
| --- | --- |
| Default | Transcription of entire audio file in one piece |
| Word | Transcription with timestamps for each word |
| Speaker | Indicates who is speaking, and a timestamp, at each change of speaker |

## Syntax

```sqlsyntax
AI_TRANSCRIBE( <audio_file> [ , <options> ] )
```

## Arguments

**Required:**

`audio_file`
:   A FILE type object representing an audio file. Use [TO_FILE function](to_file.md) to create a reference to your staged file.

**Optional:**

`options`
:   An [OBJECT value](../data-types-semistructured.md) containing zero or more of the following fields.

    * `timestamp_granularity`: A string specifying the desired timestamp granularity. Possible values are:

      + `"word"`: The file is transcribed as a series of words, each with its own timestamp.
      + `"speaker"`: The file is transcribed as a series of conversational “turns”, each with its own timestamp and speaker label.

      If this field is not specified, the entire file is transcribed as a single segment without timestamps by default.

## Returns

An string containing a JSON representation of the transcription result. The JSON object contains the following fields:

* `"audio_duration"`: The total duration of the audio file in seconds.
* `"text"`: The transcription of the complete audio file, provided when the `timestamp_granularity` field is not specified.
* `"segments"`: An array of segments, provided when the `timestamp_granularity` field is set to `"word"` or
  `"speaker"`. Each segment is a JSON object containing the following fields:

  * `"start"`: The start time of the segment in seconds.
  * `"end"`: The end time of the segment in seconds.
  * `"text"`: The transcription text for the segment.
  * `"speaker_label"`: The label of the speaker for the segment, provided when the `timestamp_granularity` field is set to `speaker`.
    Labels are of the form “SPEAKER_00”, “SPEAKER_01”, etc. and are assigned in the order speakers are detected in the audio file.

## Access control requirements

Users must use a role that has been granted the [SNOWFLAKE.CORTEX_USER database role](../snowflake-db-roles.md).
See [Cortex LLM privileges](../../user-guide/snowflake-cortex/aisql.md) for more information on this role.

## Usage notes

* AI_TRANSCRIBE supports the following languages:

  * Arabic
  * Bulgarian
  * Cantonese
  * Catalan
  * Chinese
  * Czech
  * Dutch
  * English
  * French
  * German
  * Greek
  * Hebrew
  * Hungarian
  * Indonesian
  * Italian
  * Japanese
  * Korean
  * Latvian
  * Norwegian
  * Polish
  * Portuguese
  * Romanian
  * Russian
  * Serbian
  * Slovenian
  * Spanish
  * Swedish
  * Thai
  * Turkish
  * Ukrainian

  Supported languages are automatically detected. A file can contain multiple languages, each of which is recognized and
  transcribed. For accurate language detection, speech must begin within the first five seconds of the file.
* AI_TRANSCRIBE supports the following audio and video file formats:

  |  |  |
  | --- | --- |
  | Audio | FLAC, MP3, MP4, OGG, WAV, WEBM |
  | Video | MKV, MP4, OGV, WEBM |

  Video files must contain at least one audio track in FLAC, MP3, OPUS, VORBIS, or WAV format.

  Factors such as sample rate, bit depth, and number of channels do not affect transcription, but they might make the
  file too large to process if they are too high. Internally, AI_TRANSCRIBE uses monophonic audio at 16 KHz, and
  resamples input files when they are not already in this format.
* The maximum audio file size is 700 MB.
* The maximum audio file duration is 60 minutes when timestamp granularity is set to “word” or “speaker”.
  If timestamp granularity is not used, the maximum duration is 120 minutes.

## Examples

For examples, see [AI Audio examples](../../user-guide/snowflake-cortex/ai-audio.md).

## Troubleshooting

If the function fails, it returns an error response. Common error messages include:

| Error Message | Situation and Solution |
| --- | --- |
| Invalid options object | The option provided for the `timestamp_granularity` field, if provided, must be “word” or “speaker”. |
| No response from server | The audio file cannot be retrieved, perhaps because of an expired scoped URL. |
| File too large. Maximum size is 734,003,200 Bytes, file exceeds this limit. | The provided audio file exceeds the maximum file size. |
| Invalid file format. Only [‘flac’, ‘mp3’, ‘ogg’, ‘wav’, ‘webm’] files are supported, or WebM file does not contain an audio stream. | The audio file is not one of the supported formats, which are listed in the error message. WebM files support multiple media types, so make sure the file contains an audio stream. If the file is in a supported format, check that it is not corrupted. |
| File will be too large after resampling it to 16000 Hertz. Expected size is 3,355,444,448,000.0 Bytes. | The provided audio file is too large after resampling to 16 KHz. If the provided audio has a lower sample rate, its resampled size is larger than the original, and could potentially exceed the maximum allowed file size. |
| Audio duration too long: 6052.10 seconds. Maximum allowed: 3600 seconds. or Audio duration too long: 7335.28 seconds. Maximum allowed: 7200 seconds. | The provided audio file is too long. If you are using timestamp granularity, the maximum duration is 60 minutes (3600 seconds). |
| Unsupported detected language | The audio file contains a language that is not supported by AI_TRANSCRIBE. |

## Regional availability

AI_TRANSCRIBE is available in the following regions:

* AWS US West 2 (Oregon)
* AWS US East 1 (N. Virginia)
* AWS EU Central 1 (Frankfurt)
* Azure East US 2 (Virginia)

## Legal notices

Refer to [Snowflake AI and ML](../../guides-overview-ai-features.md).

## Limitations

Snowflake Cortex functions do not support dynamic tables.
