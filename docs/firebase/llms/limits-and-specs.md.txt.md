# Source: https://firebase.google.com/docs/ai-logic/live-api/limits-and-specs.md.txt

> [!WARNING]
> **Preview** : Using the Firebase AI Logic SDKs with the Gemini Live API is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

This page describes various limits and specifications for using the
Live API and its models.

## Session-related limits

For the Live API, a *session* refers to a persistent connection where input
and output are streamed continuously over the same connection.

If the session exceeds ***any*** of the following limits, the connection is
terminated.

- **Connection length** is limited to around 10 minutes.

- **Session length** depends on the input modalities:

  - Audio-only input sessions are limited to 15 minutes.
  - Video + audio input are limited to 2 minutes.
- **Session context window** is limited to 128k tokens.

You'll receive a
[*going away* notification](https://firebase.google.com/docs/ai-logic/live-api/sessions#going-away-notification)
before the connection ends, allowing you to take further actions.

> [!NOTE]
> **Note:** Firebase AI Logic does *not yet* support the following configurations for session management: resuming a session across multiple connections, extending the session length, or compressing the context window.

Learn more about
[managing sessions](https://firebase.google.com/docs/ai-logic/live-api/sessions).

## Rate limits

The Live API has rate limits for both concurrent sessions per
Firebase project as well as tokens per minute (TPM).

- **Gemini Developer API**:

  - Limits vary based on your project's Gemini Developer API "usage tier" (see their [rate limits documentation](https://ai.google.dev/gemini-api/docs/rate-limits))
- **Vertex AI Gemini API**:

  - 1,000 concurrent sessions per Firebase project
  - 4M tokens per minute

## Audio formats

The Live API supports the following audio formats:

- **Input audio format:** Raw 16 bit PCM audio at 16kHz little-endian
- **Output audio format:** Raw 16 bit PCM audio at 24kHz little-endian

- **Supported MIME types** : `audio/x-aac`, `audio/flac`, `audio/mp3`,
  `audio/m4a`, `audio/mpeg`, `audio/mpga`, `audio/mp4`, `audio/ogg`,
  `audio/pcm`, `audio/wav`, `audio/webm`

To convey the sample rate of input audio, set the MIME type of each
audio-containing Blob to a value like `audio/pcm;rate=16000`.

## Video formats

The Live API expects a sequence of discrete image frames and supports video
frames input at 1 frame per second (FPS).

- **Recommended input**: native 768x768 resolution at 1 FPS.

- **Supported MIME types** : `video/x-flv`, `video/quicktime`, `video/mpeg`,
  `video/mpegs`, `video/mpg`, `video/mp4`, `video/webm`, `video/wmv`, `video/3gpp`

Note that this specification makes the Live API unsuitable for use cases
that require analyzing fast-changing video, such as play-by-play in high-speed
sports.

## Response voices

The Live API supports the following response voice options. For demos of
what each voice sounds like, see
[Chirp 3: HD voices](https://cloud.google.com/text-to-speech/docs/chirp3-hd).

If you don't specify a response voice, the default is `Puck`.

Learn how to
[specify the response voice](https://firebase.google.com/docs/ai-logic/live-api/configuration#specify-response-voice).

|---|---|---|
| `Zephyr` -- *Bright* `Kore` -- *Firm* `Orus` -- *Firm* `Autonoe` -- *Bright* `Umbriel` -- *Easy-going* `Erinome` -- *Clear* `Laomedeia` -- *Upbeat* `Schedar` -- *Even* `Achird` -- *Friendly* `Sadachbia` -- *Lively* | `Puck` -- *Upbeat* `Fenrir` -- *Excitable* `Aoede` -- *Breezy* `Enceladus` -- *Breathy* `Algieba` -- *Smooth* `Algenib` -- *Gravelly* `Achernar` -- *Soft* `Gacrux` -- *Mature* `Zubenelgenubi` -- *Casual* `Sadaltager` -- *Knowledgeable* | `Charon` -- *Informative* `Leda` -- *Youthful* `Callirrhoe` -- *Easy-going* `Iapetus` -- *Clear* `Despina` -- *Smooth* `Rasalgethi` -- *Informative* `Alnilam` -- *Firm* `Pulcherrima` -- *Forward* `Vindemiatrix` -- *Gentle* `Sulafat` -- *Warm* |

## Languages

The Live API supports the following languages.
Learn how to
[influence the response language](https://firebase.google.com/docs/ai-logic/live-api/configuration#influence-response-language).

| Language | BCP-47 Code | Language | BCP-47 Code |
|---|---|---|---|
| Arabic (Egyptian) | ar-EG | German (Germany) | de-DE |
| English (US) | en-US | Spanish (US) | es-US |
| French (France) | fr-FR | Hindi (India) | hi-IN |
| Indonesian (Indonesia) | id-ID | Italian (Italy) | it-IT |
| Japanese (Japan) | ja-JP | Korean (Korea) | ko-KR |
| Portuguese (Brazil) | pt-BR | Russian (Russia) | ru-RU |
| Dutch (Netherlands) | nl-NL | Polish (Poland) | pl-PL |
| Thai (Thailand) | th-TH | Turkish (Turkey) | tr-TR |
| Vietnamese (Vietnam) | vi-VN | Romanian (Romania) | ro-RO |
| Ukrainian (Ukraine) | uk-UA | Bengali (Bangladesh) | bn-BD |
| English (India) | en-IN \& hi-IN bundle | Marathi (India) | mr-IN |
| Tamil (India) | ta-IN | Telugu (India) | te-IN |