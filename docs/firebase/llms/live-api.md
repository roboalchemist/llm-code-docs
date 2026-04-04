# Source: https://firebase.google.com/docs/ai-logic/live-api.md.txt

<br />

| **Preview** : Using theFirebase AI LogicSDKs with theGemini Live APIis a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

TheGemini Live APIenables low-latency, real-time voice and video interactions with aGeminimodel that is*bidirectional*.

TheLive APIand its special family of models can process continuous streams of audio, video, or text to deliver immediate, human-like spoken responses, creating a natural conversational experience for your users.

This page describes how to**get started with the most common capability --- streaming audio input and output** , but theLive APIsupports many different[capabilities](https://firebase.google.com/docs/ai-logic/live-api/capabilities)and[configuration options](https://firebase.google.com/docs/ai-logic/live-api/configuration).
| **Important:** TheGemini Live APIis for*live real-time streaming* that's bidirectional and specifically for*audio responses* .  
| If you want*basic streaming of text responses* (using`generateContentStream`or`sendMessageStream`), then check out our overview of how to[stream text responses](https://firebase.google.com/docs/ai-logic/stream-responses).

TheLive APIis a stateful API that creates a WebSocket connection to establish a***session*** between the client and theGeminiserver. For details, see theLive APIreference documentation ([Gemini Developer API](https://ai.google.dev/api/live)\|[Vertex AIGemini API](https://cloud.google.com//vertex-ai/generative-ai/docs/model-reference/multimodal-live#messages)).

[arrow_downwardJump to code samples](https://firebase.google.com/docs/ai-logic/live-api#audio-in-audio-out)

## Check out helpful resources

- **Swift** - coming soon! \|**Android** -[quickstart app](https://github.com/firebase/quickstart-android/tree/master/firebase-ai/app/src/main/java/com/google/firebase/quickstart/ai/feature/live)\|**Web** -[quickstart app](https://github.com/firebase/quickstart-js/blob/master/ai/ai-react-app/src/views/LiveView.tsx)\|**Flutter** -[quickstart app](https://github.com/firebase/flutterfire/blob/main/packages/firebase_ai/firebase_ai/example/lib/pages/bidi_page.dart)\|**Unity**- coming soon!

- Experience theGemini Live APIin a real deployed app - check out the[Flutter AI Playground app](https://firebase.google.com/docs/ai-logic/live-api/g.co/firebase/flutter-ai-playground)accessible via theFirebaseconsole

## Before you begin

If you haven't already, complete the[getting started guide](https://firebase.google.com/docs/ai-logic/get-started), which describes how to set up your Firebase project, connect your app to Firebase, add the SDK, initialize the backend service for your chosenGemini APIprovider, and create a`LiveModel`instance.

You can prototype with prompts and theLive APIin[Google AI Studio](https://aistudio.google.com)or[Vertex AI Studio](https://cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart).

#### Models that support this capability

Gemini 2.5 Flash Livemodels are the*native audio* models that support theGemini Live API. Even though the model has different model names depending on theGeminiAPI provider, the behavior and features of the model are the same.

- **Gemini Developer API**

  - `gemini-2.5-flash-native-audio-preview-12-2025`
  - `gemini-2.5-flash-native-audio-preview-09-2025`

  Even though these are preview models, they're available on the "free tier" of theGemini Developer API.
- **Vertex AIGemini API**

  - `gemini-live-2.5-flash-native-audio`*(released in December 2025)*
  - `gemini-live-2.5-flash-preview-native-audio-09-2025`

  When using theVertex AIGemini API, theLive APImodels are*not* supported in the`global`location.

## Stream audio input and output

|----------------------------------------------------------------------------------------------------------------------------------|
| *Click yourGemini APIprovider to view provider-specific content and code on this page.* Gemini Developer APIVertex AI Gemini API |

The following example shows the**basic implementation** to send streamed***audio*input** and receive streamed***audio*output**.

For additional options and capabilities for theLive API, review the["What else can you do?"](https://firebase.google.com/docs/ai-logic/live-api#what-else-can-you-do)section later on this page.  

### Swift

To use theLive API, create a[`LiveModel`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel)instance and set the[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)to`audio`.  


    import FirebaseAILogic

    // Initialize the Gemini Developer API backend service
    // Create a `liveModel` instance with a model that supports the Live API
    let liveModel = FirebaseAI.firebaseAI(backend: .googleAI()).liveModel(
      modelName: "gemini-2.5-flash-native-audio-preview-12-2025",
      // Configure the model to respond with audio
      generationConfig: LiveGenerationConfig(
        responseModalities: [.audio]
      )
    )

    do {
      let session = try await liveModel.connect()

      // Load the audio file, or tap a microphone
      guard let audioFile = NSDataAsset(name: "audio.pcm") else {
        fatalError("Failed to load audio file")
      }

      // Provide the audio data
      await session.sendAudioRealtime(audioFile.data)

      var outputText = ""
      for try await message in session.responses {
        if case let .content(content) = message.payload {
          content.modelTurn?.parts.forEach { part in
            if let part = part as? InlineDataPart, part.mimeType.starts(with: "audio/pcm") {
              // Handle 16bit pcm audio data at 24khz
              playAudio(part.data)
            }
          }
          // Optional: if you don't require to send more requests.
          if content.isTurnComplete {
            await session.close()
          }
        }
      }
    } catch {
      fatalError(error.localizedDescription)
    }

### Kotlin

To use theLive API, create a[`LiveModel`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel)instance and set the[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)to`AUDIO`.  


    // Initialize the Gemini Developer API backend service
    // Create a `liveModel` instance with a model that supports the Live API
    val liveModel = Firebase.ai(backend = GenerativeBackend.googleAI()).liveModel(
        modelName = "gemini-2.5-flash-native-audio-preview-12-2025",
        // Configure the model to respond with audio
        generationConfig = liveGenerationConfig {
            responseModality = ResponseModality.AUDIO
       }
    )

    val session = liveModel.connect()

    // This is the recommended approach.
    // However, you can create your own recorder and handle the stream.
    session.startAudioConversation()

### Java

To use theLive API, create a[`LiveModel`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel)instance and set the[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)to`AUDIO`.  


    ExecutorService executor = Executors.newFixedThreadPool(1);
    // Initialize the Gemini Developer API backend service
    // Create a `liveModel` instance with a model that supports the Live API
    LiveGenerativeModel lm = FirebaseAI.getInstance(GenerativeBackend.googleAI()).liveModel(
            "gemini-2.5-flash-native-audio-preview-12-2025",
            // Configure the model to respond with audio
            new LiveGenerationConfig.Builder()
                    .setResponseModality(ResponseModality.AUDIO)
                    .build()
    );
    LiveModelFutures liveModel = LiveModelFutures.from(lm);

    ListenableFuture<LiveSession> sessionFuture =  liveModel.connect();

    Futures.addCallback(sessionFuture, new FutureCallback<LiveSession>() {
        @Override
        public void onSuccess(LiveSession ses) {
    	 LiveSessionFutures session = LiveSessionFutures.from(ses);
            session.startAudioConversation();
        }
        @Override
        public void onFailure(Throwable t) {
            // Handle exceptions
        }
    }, executor);

### Web

To use theLive API, create a[`LiveGenerativeModel`](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel)instance and set the[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)to`AUDIO`.  


    import { initializeApp } from "firebase/app";
    import { getAI, getLiveGenerativeModel, GoogleAIBackend, ResponseModality } from "firebase/ai";

    // TODO(developer) Replace the following with your app's Firebase configuration
    // See: https://firebase.google.com/docs/web/learn-more#config-object
    const firebaseConfig = {
      // ...
    };

    // Initialize FirebaseApp
    const firebaseApp = initializeApp(firebaseConfig);

    // Initialize the Gemini Developer API backend service
    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    // Create a `LiveGenerativeModel` instance with a model that supports the Live API
    const liveModel = getLiveGenerativeModel(ai, {
      model: "gemini-2.5-flash-native-audio-preview-12-2025",
      // Configure the model to respond with audio
      generationConfig: {
        responseModalities: [ResponseModality.AUDIO],
      },
    });

    const session = await liveModel.connect();

    // Start the audio conversation
    const audioConversationController = await startAudioConversation(session);

    // ... Later, to stop the audio conversation
    // await audioConversationController.stop()

### Dart

To use theLive API, create a[`LiveGenerativeModel`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/LiveGenerativeModel-class.html)instance and set the[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)to`audio`.  


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';
    import 'package:your_audio_recorder_package/your_audio_recorder_package.dart';

    late LiveModelSession _session;
    final _audioRecorder = YourAudioRecorder();

    await Firebase.initializeApp(
      options: DefaultFirebaseOptions.currentPlatform,
    );

    // Initialize the Gemini Developer API backend service
    // Create a `liveGenerativeModel` instance with a model that supports the Live API
    final liveModel = FirebaseAI.googleAI().liveGenerativeModel(
      model: 'gemini-2.5-flash-native-audio-preview-12-2025',
      // Configure the model to respond with audio
      liveGenerationConfig: LiveGenerationConfig(
        responseModalities: [ResponseModalities.audio],
      ),
    );

    _session = await liveModel.connect();

    final audioRecordStream = _audioRecorder.startRecordingStream();
    // Map the Uint8List stream to InlineDataPart stream
    final mediaChunkStream = audioRecordStream.map((data) {
      return InlineDataPart('audio/pcm', data);
    });
    await _session.startMediaStream(mediaChunkStream);

    // In a separate thread, receive the audio response from the model
    await for (final message in _session.receive()) {
       // Process the received message
    }

### Unity

To use theLive API, create a[`LiveModel`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-generative-model)instance and set the[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)to`Audio`.  


    using Firebase;
    using Firebase.AI;

    async Task SendTextReceiveAudio() {
      // Initialize the Gemini Developer API backend service
      // Create a `LiveModel` instance with a model that supports the Live API
      var liveModel = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetLiveModel(
          modelName: "gemini-2.5-flash-native-audio-preview-12-2025",
          // Configure the model to respond with audio
          liveGenerationConfig: new LiveGenerationConfig(
              responseModalities: new[] { ResponseModality.Audio })
        );

      LiveSession session = await liveModel.ConnectAsync();

      // Start a coroutine to send audio from the Microphone
      var recordingCoroutine = StartCoroutine(SendAudio(session));

      // Start receiving the response
      await ReceiveAudio(session);
    }

    IEnumerator SendAudio(LiveSession liveSession) {
      string microphoneDeviceName = null;
      int recordingFrequency = 16000;
      int recordingBufferSeconds = 2;

      var recordingClip = Microphone.Start(microphoneDeviceName, true,
                                           recordingBufferSeconds, recordingFrequency);

      int lastSamplePosition = 0;
      while (true) {
        if (!Microphone.IsRecording(microphoneDeviceName)) {
          yield break;
        }

        int currentSamplePosition = Microphone.GetPosition(microphoneDeviceName);

        if (currentSamplePosition != lastSamplePosition) {
          // The Microphone uses a circular buffer, so we need to check if the
          // current position wrapped around to the beginning, and handle it
          // accordingly.
          int sampleCount;
          if (currentSamplePosition > lastSamplePosition) {
            sampleCount = currentSamplePosition - lastSamplePosition;
          } else {
            sampleCount = recordingClip.samples - lastSamplePosition + currentSamplePosition;
          }

          if (sampleCount > 0) {
            // Get the audio chunk
            float[] samples = new float[sampleCount];
            recordingClip.GetData(samples, lastSamplePosition);

            // Send the data, discarding the resulting Task to avoid the warning
            _ = liveSession.SendAudioAsync(samples);

            lastSamplePosition = currentSamplePosition;
          }
        }

        // Wait for a short delay before reading the next sample from the Microphone
        const float MicrophoneReadDelay = 0.5f;
        yield return new WaitForSeconds(MicrophoneReadDelay);
      }
    }

    Queue audioBuffer = new();

    async Task ReceiveAudio(LiveSession liveSession) {
      int sampleRate = 24000;
      int channelCount = 1;

      // Create a looping AudioClip to fill with the received audio data
      int bufferSamples = (int)(sampleRate * channelCount);
      AudioClip clip = AudioClip.Create("StreamingPCM", bufferSamples, channelCount,
                                        sampleRate, true, OnAudioRead);

      // Attach the clip to an AudioSource and start playing it
      AudioSource audioSource = GetComponent();
      audioSource.clip = clip;
      audioSource.loop = true;
      audioSource.Play();

      // Start receiving the response
      await foreach (var message in liveSession.ReceiveAsync()) {
        // Process the received message
        foreach (float[] pcmData in message.AudioAsFloat) {
          lock (audioBuffer) {
            foreach (float sample in pcmData) {
              audioBuffer.Enqueue(sample);
            }
          }
        }
      }
    }

    // This method is called by the AudioClip to load audio data.
    private void OnAudioRead(float[] data) {
      int samplesToProvide = data.Length;
      int samplesProvided = 0;

      lock(audioBuffer) {
        while (samplesProvided < samplesToProvide && audioBuffer.Count > 0) {
          data[samplesProvided] = audioBuffer.Dequeue();
          samplesProvided++;
        }
      }

      while (samplesProvided < samplesToProvide) {
        data[samplesProvided] = 0.0f;
        samplesProvided++;
      }
    }

<br />

*** ** * ** ***

## Pricing and token counting

You can find pricing information for theLive APImodels in the documentation for your chosenGemini APIprovider:[Gemini Developer API](https://ai.google.dev/gemini-api/docs/pricing)\|[Vertex AIGemini API](https://cloud.google.com/vertex-ai/generative-ai/pricing).

Regardless of yourGemini APIprovider, theLive APIdoes*not*support the Count Tokens API.
| **Note:** Firebase AI Logicdoes*not yet* support receiving`UsageMetadata`in the response.

<br />

*** ** * ** ***

## What else can you do?

- Check out the full suite of[capabilities](https://firebase.google.com/docs/ai-logic/live-api/capabilities)for theLive API, like streaming various input modalities (audio, text, or video + audio).

- Customize your implementation by using various[configuration options](https://firebase.google.com/docs/ai-logic/live-api/configuration), like adding transcription or setting the response voice.

- Supercharge your implementation by giving the model access to tools, like function calling and grounding with Google Search. Official documentation for using tools with theLive APIis coming soon!

- Learn about[limits and specifications](https://firebase.google.com/docs/ai-logic/live-api/limits-and-specs), for using theLive API, like session length, rate limits, supported languages, etc.