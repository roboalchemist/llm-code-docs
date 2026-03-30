# Source: https://mastra.ai/reference/voice/sarvam

# Sarvam

The SarvamVoice class in Mastra provides text-to-speech and speech-to-text capabilities using Sarvam AI models.

## Usage Example

```typescript
import { SarvamVoice } from '@mastra/voice-sarvam'

// Initialize with default configuration using environment variables
const voice = new SarvamVoice()

// Or initialize with specific configuration
const voiceWithConfig = new SarvamVoice({
  speechModel: {
    model: 'bulbul:v1',
    apiKey: process.env.SARVAM_API_KEY!,
    language: 'en-IN',
    properties: {
      pitch: 0,
      pace: 1.65,
      loudness: 1.5,
      speech_sample_rate: 8000,
      enable_preprocessing: false,
      eng_interpolation_wt: 123,
    },
  },
  listeningModel: {
    model: 'saarika:v2',
    apiKey: process.env.SARVAM_API_KEY!,
    languageCode: 'en-IN',
    filetype: 'wav',
  },
  speaker: 'meera', // Default voice
})

// Convert text to speech
const audioStream = await voice.speak('Hello, how can I help you?')

// Convert speech to text
const text = await voice.listen(audioStream, {
  filetype: 'wav',
})
```

### Sarvam API Docs -

<https://docs.sarvam.ai/api-reference-docs/endpoints/text-to-speech>

## Configuration

### Constructor Options

**speechModel** (`SarvamVoiceConfig`): Configuration for text-to-speech synthesis. (Default: `{ model: 'bulbul:v1', language: 'en-IN' }`)

**speechModel.apiKey** (`string`): Sarvam API key. Falls back to SARVAM\_API\_KEY environment variable.

**speechModel.model** (`SarvamTTSModel`): Specifies the model to use for text-to-speech conversion.

**speechModel.language** (`SarvamTTSLanguage`): Target language for speech synthesis. Available options: hi-IN, bn-IN, kn-IN, ml-IN, mr-IN, od-IN, pa-IN, ta-IN, te-IN, en-IN, gu-IN

**speechModel.properties** (`object`): Additional voice properties for customization.

**speechModel.properties.pitch** (`number`): Controls the pitch of the audio. Lower values result in a deeper voice, while higher values make it sharper. The suitable range is between -0.75 and 0.75.

**speechModel.properties.pace** (`number`): Controls the speed of the audio. Lower values result in slower speech, while higher values make it faster. The suitable range is between 0.5 and 2.0. Default is 1.0. Required range: 0.3 <= x <= 3

**speechModel.properties.loudness** (`number`): Controls the loudness of the audio. Lower values result in quieter audio, while higher values make it louder. The suitable range is between 0.3 and 3.0. Required range: 0 <= x <= 3

**speechModel.properties.speech\_sample\_rate** (`8000 | 16000 | 22050`): Audio sample rate in Hz.

**speechModel.properties.enable\_preprocessing** (`boolean`): Controls whether normalization of English words and numeric entities (e.g., numbers, dates) is performed. Set to true for better handling of mixed-language text. Default is false.

**speechModel.properties.eng\_interpolation\_wt** (`number`): Weight for interpolating with English speaker at encoder.

**speaker** (`SarvamVoiceId`): The speaker to be used for the output audio. If not provided, Meera will be used as default. AvailableOptions - meera, pavithra, maitreyi, arvind, amol, amartya, diya, neel, misha, vian, arjun, maya (Default: `'meera'`)

**listeningModel** (`SarvamListenOptions`): Configuration for speech-to-text recognition. (Default: `{ model: 'saarika:v2', language_code: 'unknown' }`)

**listeningModel.apiKey** (`string`): Sarvam API key. Falls back to SARVAM\_API\_KEY environment variable.

**listeningModel.model** (`SarvamSTTModel`): Specifies the model to use for speech-to-text conversion. Note:- Default model is saarika:v2 . Available options: saarika:v1, saarika:v2, saarika:flash

**listeningModel.languageCode** (`SarvamSTTLanguage`): Specifies the language of the input audio. This parameter is required to ensure accurate transcription. For the saarika:v1 model, this parameter is mandatory. For the saarika:v2 model, it is optional. unknown: Use this when the language is not known; the API will detect it automatically. Note:- that the saarika:v1 model does not support unknown language code. Available options: unknown, hi-IN, bn-IN, kn-IN, ml-IN, mr-IN, od-IN, pa-IN, ta-IN, te-IN, en-IN, gu-IN

**listeningModel.filetype** (`'mp3' | 'wav'`): Audio format of the input stream.

## Methods

### speak()

Converts text to speech using Sarvam's text-to-speech models.

**input** (`string | NodeJS.ReadableStream`): Text or text stream to convert to speech.

**options** (`Options`): Configuration options.

**options.speaker** (`SarvamVoiceId`): Voice ID to use for speech synthesis.

Returns: `Promise<NodeJS.ReadableStream>`

### listen()

Transcribes audio using Sarvam's speech recognition models.

**input** (`NodeJS.ReadableStream`): Audio stream to transcribe.

**options** (`SarvamListenOptions`): Configuration options for speech recognition.

Returns: `Promise<string>`

### getSpeakers()

Returns an array of available voice options.

Returns: `Promise<Array<{voiceId: SarvamVoiceId}>>`

## Notes

- API key can be provided via constructor options or the `SARVAM_API_KEY` environment variable
- If no API key is provided, the constructor will throw an error
- The service communicates with the Sarvam AI API at `https://api.sarvam.ai`
- Audio is returned as a stream containing binary audio data
- Speech recognition supports mp3 and wav audio formats