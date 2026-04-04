# Source: https://firebase.google.com/docs/ai-logic/stream-responses.md.txt

Firebase AI Logic supports basic **streaming of text responses** using
`generateContentStream` or `sendMessageStream` (for chat).

You can achieve faster interactions by not waiting for the entire result from
the model generation, and instead use streaming to handle partial results.

Check out the documentation to stream generated text responses for the
following:

- [Text-only input](https://firebase.google.com/docs/ai-logic/generate-text#streaming)

- [Analyzing images](https://firebase.google.com/docs/ai-logic/analyze-images#streaming)

- [Analyzing video](https://firebase.google.com/docs/ai-logic/analyze-video#streaming)

- [Analyzing audio](https://firebase.google.com/docs/ai-logic/analyze-audio#streaming)

- [Analyzing documents (like PDFs)](https://firebase.google.com/docs/ai-logic/analyze-documents#streaming)

- [Chat experiences](https://firebase.google.com/docs/ai-logic/chat#streaming)

> [!IMPORTANT]
> **Important:** If you're looking for low-latency *live real-time streaming* that's bidirectional and specifically for *audio responses* (for example, to let your users experience natural, human-like voice conversations), then check out [Real-time bidirectional streaming using the Gemini Live API](https://firebase.google.com/docs/ai-logic/live-api).