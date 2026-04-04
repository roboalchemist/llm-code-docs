# Source: https://mastra.ai/reference/voice/speechify

# Speechify

The Speechify voice implementation in Mastra provides text-to-speech capabilities using Speechify's API.

## Usage Example

```typescript
import { SpeechifyVoice } from '@mastra/voice-speechify'

// Initialize with default configuration (uses SPEECHIFY_API_KEY environment variable)
const voice = new SpeechifyVoice()

// Initialize with custom configuration
const voice = new SpeechifyVoice({
  speechModel: {
    name: 'simba-english',
    apiKey: 'your-api-key',
  },
  speaker: 'george', // Default voice
})

// Convert text to speech
const audioStream = await voice.speak('Hello, world!', {
  speaker: 'henry', // Override default voice
})
```

## Constructor Parameters

**speechModel** (`SpeechifyConfig`): Configuration for text-to-speech functionality (Default: `{ name: 'simba-english' }`)

**speechModel.name** (`VoiceModelName`): The Speechify model to use

**speechModel.apiKey** (`string`): Speechify API key. Falls back to SPEECHIFY\_API\_KEY environment variable

**speaker** (`SpeechifyVoiceId`): Default voice ID to use for speech synthesis (Default: `'george'`)

## Methods

### speak()

Converts text to speech using the configured speech model and voice.

**input** (`string | NodeJS.ReadableStream`): Text to convert to speech. If a stream is provided, it will be converted to text first.

**options** (`Options`): Configuration options.

**options.speaker** (`string`): Override the default speaker for this request

**options.model** (`VoiceModelName`): Override the default model for this request

Returns: `Promise<NodeJS.ReadableStream>`

### getSpeakers()

Returns an array of available voice options, where each node contains:

**voiceId** (`string`): Unique identifier for the voice

**name** (`string`): Display name of the voice

**language** (`string`): Language code for the voice

**gender** (`string`): Gender of the voice

### listen()

This method isn't supported by Speechify and will throw an error. Speechify doesn't provide speech-to-text functionality.

## Notes

- Speechify requires an API key for authentication
- The default model is 'simba-english'
- Speech-to-text functionality isn't supported
- Additional audio stream options can be passed through the speak() method's options parameter