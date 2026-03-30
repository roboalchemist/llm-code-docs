# Print the content of the response
print(chat_response.choices[0].message.content)
```
  </TabItem>
  <TabItem value="typescript" label="typescript">

```typescript


const apiKey = process.env["MISTRAL_API_KEY"];

const client = new Mistral({ apiKey: apiKey });

// If local document, upload and retrieve the signed url
const audio_file = fs.readFileSync('local_audio.mp3');
const uploaded_audio = await client.files.upload({
  file: audio_file,
  purpose: "audio",
});
const signedUrl = await client.files.getSignedUrl({
    fileId: uploaded_audio.id,
});

// Get the chat response
const chatResponse = await client.chat.complete({
  model: "voxtral-mini-latest",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "input_audio",
          input_audio: signedUrl.url,
        },
        {
          type: "text",
          text: "What's in this file?",
        },
      ],
    },
  ],
});

// Print the content of the response
console.log(chatResponse.choices[0].message.content);
```

  </TabItem>
  <TabItem value="curl" label="curl" default>

**Upload the Audio File**
```bash
curl --location https://api.mistral.ai/v1/files \
  --header "Authorization: Bearer $MISTRAL_API_KEY" \
  --form purpose="audio" \
  --form file="@local_audio.mp3"
```

**Get the Signed URL**
```bash
curl --location "https://api.mistral.ai/v1/files/$id/url?expiry=24" \
    --header "Accept: application/json" \
    --header "Authorization: Bearer $MISTRAL_API_KEY"
```

**Send Completion Request**
```bash
curl --location https://api.mistral.ai/v1/chat/completions \
  --header "Authorization: Bearer $MISTRAL_API_KEY" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "voxtral-mini-2507",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_audio",
            "input_audio": "<signed_url>"
          },
          {
            "type": "text",
            "text": "What'\''s in this file?"
          }
        ]
      }
    ]
  }'
```
  </TabItem>
</Tabs>

<details>
<summary><b>Samples</b></summary>
  <Tabs>
    <TabItem value="chat" label="Chat" default>

        **User**

        <audio controls>
          <source src="/audio/chat.wav" type="audio/wav"/>
          Your browser does not support the audio element.
        </audio>

        **Assistant**

        Sure, here is the transcription of what you said:  
        "Today on July 15th, 2025, Mistral AI is announcing the new Voxtral models."  
        And here is the Python code to generate the first n digits of the Fibonacci sequence:  
        ```python
            def fibonacci(n):
        if n <= 0:
            return []
        elif n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        fib_sequence = [0, 1]
        for i in range(2, n):
            next_value = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_value)

        return fib_sequence

        # Example usage:
        n = 10  # Change this value to get the first n digits of the Fibonacci sequence
        print(fibonacci(n))
        ```
        This code defines a function `fibonacci` that takes an integer `n` and returns a list containing the first `n` digits of the Fibonacci sequence. You can change the value of `n` to get the desired number of Fibonacci digits.

    </TabItem>
    <TabItem value="music" label="Music">
    
        **User**

        <audio controls>
          <source src="/audio/music.mp3" type="audio/mp3"/>
          Your browser does not support the audio element.
        </audio>
        What's in this file?

        **Assistant**

        The audio file contains music.
    </TabItem>
    <TabItem value="compare_speakers" label="Compare Speakers">
    
        **User**

        <audio controls>
          <source src="/audio/obama.mp3" type="audio/mp3"/>
          Your browser does not support the audio element.
        </audio>
        <audio controls>
          <source src="/audio/bcn_weather.mp3" type="audio/mp3"/>
          Your browser does not support the audio element.
        </audio>
        
        Which speaker do you prefer between the two? Why? How are they different from each other?

        **Assistant**

        The speaker who delivers the farewell address is more engaging and inspiring.  
        They express gratitude and optimism, emphasizing the importance of self-government and citizenship.  
        They also share personal experiences and observations, making the speech more relatable and heartfelt.  
        In contrast, the second speaker provides factual information about the weather in Barcelona, which is less engaging and lacks the emotional depth of the first speaker's address.
    </TabItem>
  </Tabs>
</details>

## Transcription

Transcription provides an optimized endpoint for transcription purposes and currently supports `voxtral-mini-latest`, which runs **Voxtral Mini Transcribe**.

**Parameters**  
We provide different settings and parameters for transcription, such as:
- `timestamp_granularities`: This allows you to set timestamps to track not only "what" was said but also "when". You can find more about timestamps [here](#transcription-with-timestamps).
- `language`: Our transcription service also works as a language detection service. However, you can manually set the language of the transcription for better accuracy if the language of the audio is already known.

### Passing an Audio File

Among the different methods to pass the audio, you can directly provide a path to a file to upload and transcribe it as follows:

<Tabs groupId="code">
  <TabItem value="python" label="python">

```python

from mistralai import Mistral