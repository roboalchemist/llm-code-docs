# Source: https://docs.tavus.io/sections/changelog/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

<Update label="July 25" tags={["2025"]}>
  ## New Features

  * **Persona Editing in Developer Portal:** We've added new editing capabilities to help you refine your Personas more efficiently. You can now update system prompt, context, and layers directly in our Developer Portal, plus duplicate existing Personas to quickly create variations or use them as starting points for new projects. Find these new features in your Persona Library at platform.tavus.io.
</Update>

<Update label="July 22" tags={["2025"]}>
  ## New Features

  * **Llama 4 Support:** Your persona just got even smarter, thanks to Meta's Llama 4 model 🧠 You can start using Llama 4 by specifying `tavus-llama-4` for the LLM `model` value when creating a new persona or updating an existing one. Click <a href="https://docs.tavus.io/sections/conversational-video-interface/persona/llm#tavus-hosted-models" target="_blank">here</a> to learn more!
</Update>

<Update label="July 15" tags={["2025"]}>
  ## New Features

  * **React Component Library:** Developers can build with Tavus even faster now with our pre-defined components 🚀 Click <a href="https://docs.tavus.io/sections/conversational-video-interface/component-library/overview" target="_blank">here</a> to learn more!
</Update>

<Update label="June 27" tags={["2025"]}>
  ## New Features

  * **Multilingual Conversation Support:** CVI now supports dynamic multilingual conversations through automatic language detection. Set the language parameter to "multilingual" and CVI will automatically detect the user's spoken language and respond in the same language using ASR technology.
  * **Audio-Only Mode:** CVI now supports audio-only conversations with advanced perception (powered by Raven) and intelligent turn-taking (powered by Sparrow-1). Set `audio_only=true` in your create conversation request to enable streamlined voice-first interactions.
</Update>

<Update label="June 20" tags={["2025"]}>
  ## Enhancements

  * **Fixed CVI responsiveness issue:** Resolved an issue where CVI would occasionally ignore very brief user utterances. All user inputs, regardless of length, now receive consistent responses.
  * **Expanded tavus-llama-4 context window:** Increased maximum context window to 32,000 tokens. For optimal performance and response times, we recommend staying under 25,000 tokens.
</Update>

<Update label="June 3" tags={["2025"]}>
  ## Enhancements

  * Reduced conversation boot time by 58% (p50).
</Update>

<Update label="May 28" tags={["2025"]}>
  ## Changes

  * Added a new recording requirement to <a href="/sections/replica/replica-training" target="_blank">Replica Training</a>: Start the talking segment with a big smile.

  ## Enhancements

  * Added <a href="/sections/event-schemas/conversation-echo" target="_blank">echo</a> and <a href="/sections/event-schemas/conversation-respond" target="_blank">respond</a> events to conversational context.
</Update>

<Update label="May 17" tags={["2025"]}>
  ## Enhancements

  * **Major Phoenix 3 Enhancements for CVI**:
    * Increased frame rate from 27fps to 32fps, significantly boosting smoothness.
    * Reduced Phoenix step's warm boot time by 60% (from 5s to 2s).
    * Lipsync accuracy improved by \~22% based on AVSR metric.
    * Resolved blurriness and choppiness at conversation start.
    * Enhanced listening mode with more natural micro expressions (eyebrow movements, subtle gestures).
    * Greenscreen mode speed boosted by an additional \~1.5fps.
  * **Enhanced CVI Audio Quality**: Audio clicks significantly attenuated, providing clearer conversational audio.
  * **Phoenix 3 Visual Artifacts Fix**: Resolved visual artifacts in 4K videos on Apple devices, eliminating black spot artifacts in thumbnails.
</Update>

<Update label="May 9" tags={["2025"]}>
  ## New Features

  * Launched <a href="https://www.tavus.io/post/building-real-time-ai-video-agents-with-livekit-and-tavus" target="_blank">LiveKit Integration</a>: With Tavus video agents now integrated into LiveKit, you can add humanlike video responses to your voice agents in seconds.
  * <a href="https://docs.tavus.io/api-reference/personas/patch-persona" target="_blank">Persona API</a>: Enabled patch updates to personas.

  ## Enhancements

  * Resolved TTS (Cartesia) stability issues and addressed hallucination.
  * **Phoenix 3 Improvements**:
    * Fixed blinking/jumping issues and black spots in videos.
    * FPS optimization to resolve static and audio crackling.
</Update>

<Update label="April" tags={["2024"]}>
  ## Enhancements

  * **Replica API**:
    * Enhanced Error Messaging for Training Videos.
    * Optimized Auto QA for Training Videos.
</Update>
