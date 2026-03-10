# Print the content of the response
print(transcription_response)
```
  </TabItem>
  <TabItem value="typescript" label="typescript">

```typescript


// Retrieve the API key from environment variables
const apiKey = process.env["MISTRAL_API_KEY"];

// Initialize the Mistral client
const client = new Mistral({ apiKey: apiKey });

// Get the transcription
const audio_file = fs.readFileSync('/path/to/file/audio.mp3');
const transcriptionResponse = await client.audio.transcriptions.complete({
  model: "voxtral-mini-latest",
  file: {
    fileName: "audio.mp3",
    content: audio_file,
  },
  // language: "en"
});

// Log the content of the response
console.log(transcriptionResponse);
```

  </TabItem>
  <TabItem value="curl" label="curl" default>

```bash
curl --location 'https://api.mistral.ai/v1/audio/transcriptions' \
  --header "x-api-key: $MISTRAL_API_KEY" \
  --form 'file=@"/path/to/file/audio.mp3"' \
  --form 'model="voxtral-mini-2507"' \
```

**With Language defined**  
```bash
curl --location 'https://api.mistral.ai/v1/audio/transcriptions' \
  --header "x-api-key: $MISTRAL_API_KEY" \
  --form 'file=@"/path/to/file/audio.mp3"' \
  --form 'model="voxtral-mini-2507"' \
  --form 'language="en"'
```
  </TabItem>
</Tabs>

### Passing an Audio URL

Similarly, you can provide an url of an audio file.

<Tabs groupId="code">
  <TabItem value="python" label="python">

```python

from mistralai import Mistral