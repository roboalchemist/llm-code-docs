# Source: https://firebase.google.com/docs/ai-logic/live-api/capabilities.md.txt

> [!WARNING]
> **Preview** : Using the Firebase AI Logic SDKs with the Gemini Live API is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

This page describes the capabilities of the Live API when you use it via
Firebase AI Logic, including:

- Supported input modalities, including:

  - [Audio input](https://firebase.google.com/docs/ai-logic/live-api/capabilities#audio-in-audio-out)
  - [Text + audio input](https://firebase.google.com/docs/ai-logic/live-api/capabilities#text-in-audio-out)
  - [Video + audio input](https://firebase.google.com/docs/ai-logic/live-api/capabilities#video-in-audio-out)
- Lists of
  [not supported features](https://firebase.google.com/docs/ai-logic/live-api/capabilities#not-supported-features), many of which are coming
  soon!

Visit other pages to learn about customizing your implementation by using
various [configuration options](https://firebase.google.com/docs/ai-logic/live-api/configuration),
like adding transcription or setting the response voice. You can also learn
about [managing sessions](https://firebase.google.com/docs/ai-logic/live-api/sessions).

<br />

*** ** * ** ***

## Input modalities

This section describes how to send various types of inputs to a Live API
model. Native audio models always ***require audio input*** (along with
*optional additional* modalities of text or video input), and they always
***respond with audio output***.

- [Audio input](https://firebase.google.com/docs/ai-logic/live-api/capabilities#audio-in-audio-out)

- [Text + audio input](https://firebase.google.com/docs/ai-logic/live-api/capabilities#text-in-audio-out)

- [Video + audio input](https://firebase.google.com/docs/ai-logic/live-api/capabilities#video-in-audio-out)

### Stream audio input

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

The most common capability of the Live API is bidirectional *audio*
streaming, meaning real-time streaming of both audio input and output.

The Live API supports the following audio formats:

- **Input audio format:** Raw 16 bit PCM audio at 16kHz little-endian
- **Output audio format:** Raw 16 bit PCM audio at 24kHz little-endian

- **Supported MIME types** : `audio/x-aac`, `audio/flac`, `audio/mp3`,
  `audio/m4a`, `audio/mpeg`, `audio/mpga`, `audio/mp4`, `audio/ogg`,
  `audio/pcm`, `audio/wav`, `audio/webm`

To convey the sample rate of input audio, set the MIME type of each
audio-containing Blob to a value like `audio/pcm;rate=16000`.

### Swift

To use the Live API, create a
[`LiveModel`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `audio`.


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

To use the Live API, create a
[`LiveModel`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `AUDIO`.


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

To use the Live API, create a
[`LiveModel`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `AUDIO`.


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

To use the Live API, create a
[`LiveGenerativeModel`](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `AUDIO`.


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

To use the Live API, create a
[`LiveGenerativeModel`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/LiveGenerativeModel-class.html)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `audio`.


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

To use the Live API, create a
[`LiveModel`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-generative-model)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `Audio`.


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

### Stream text + audio input

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

If needed, you can send *text* input along with the audio input and receive
streamed *audio* output.

### Swift

To use the Live API, create a
[`LiveModel`](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `audio`.


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

      // Provide a text prompt
      let text = "tell a short story"

      await session.sendTextRealtime(text)

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

To use the Live API, create a
[`LiveModel`](https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/LiveGenerativeModel)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `AUDIO`.


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

    // Provide a text prompt
    val text = "tell a short story"

    session.send(text)

    session.receive().collect {
        if(it.turnComplete) {
            // Optional: if you don't require to send more requests.
            session.stopReceiving();
        }
        // Handle 16bit pcm audio data at 24khz
        playAudio(it.data)
    }

### Java

To use the Live API, create a
[`LiveModel`](https://firebase.google.com/docs/reference/android/com/google/firebase/ai/LiveGenerativeModel)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `AUDIO`.


    ExecutorService executor = Executors.newFixedThreadPool(1);
    // Initialize the Gemini Developer API backend service
    // Create a `liveModel` instance with a model that supports the Live API
    LiveGenerativeModel lm = FirebaseAI.getInstance(GenerativeBackend.googleAI()).liveModel(
            "gemini-2.5-flash-native-audio-preview-12-2025",
            // Configure the model to respond with text
            new LiveGenerationConfig.Builder()
                    .setResponseModality(ResponseModality.AUDIO)
                    .build()
    );
    LiveModelFutures model = LiveModelFutures.from(lm);
    ListenableFuture<LiveSession> sessionFuture =  model.connect();
    class LiveContentResponseSubscriber implements Subscriber<LiveContentResponse> {
        @Override
        public void onSubscribe(Subscription s) {
            s.request(Long.MAX_VALUE); // Request an unlimited number of items
        }
        @Override
        public void onNext(LiveContentResponse liveContentResponse) {
            // Handle 16bit pcm audio data at 24khz
    	liveContentResponse.getData();
        }
        @Override
        public void onError(Throwable t) {
            System.err.println("Error: " + t.getMessage());
        }
        @Override
        public void onComplete() {
            System.out.println("Done receiving messages!");
        }
    }
    Futures.addCallback(sessionFuture, new FutureCallback<LiveSession>() {
        @Override
        public void onSuccess(LiveSession ses) {
    	 LiveSessionFutures session = LiveSessionFutures.from(ses);
            // Provide a text prompt
            String text = "tell me a short story?";
            session.send(text);
            Publisher<LiveContentResponse> publisher = session.receive();
            publisher.subscribe(new LiveContentResponseSubscriber());
        }
        @Override
        public void onFailure(Throwable t) {
            // Handle exceptions
        }
    }, executor);

### Web

To use the Live API, create a
[`LiveGenerativeModel`](https://firebase.google.com/docs/reference/js/ai.livegenerativemodel)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `AUDIO`.


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

    // Provide a text prompt
    const prompt = "tell a short story";
    session.send(prompt);

    // Handle the model's audio output
    const messages = session.receive();
    for await (const message of messages) {
      switch (message.type) {
        case "serverContent":
          if (message.turnComplete) {
            // TODO(developer): Handle turn completion
          } else if (message.interrupted) {
            // TODO(developer): Handle the interruption
            break;
          } else if (message.modelTurn) {
            const parts = message.modelTurn?.parts;
            parts?.forEach((part) => {
              if (part.inlineData) {
                // TODO(developer): Play the audio chunk
              }
            });
          }
          break;
        case "toolCall":
          // Ignore
        case "toolCallCancellation":
          // Ignore
      }
    }

### Dart

To use the Live API, create a
[`LiveGenerativeModel`](https://pub.dev/documentation/firebase_ai/latest/firebase_ai/LiveGenerativeModel-class.html)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `audio`.


    import 'package:firebase_ai/firebase_ai.dart';
    import 'package:firebase_core/firebase_core.dart';
    import 'firebase_options.dart';
    import 'dart:async';
    import 'dart:typed_data';

    late LiveModelSession _session;

    Future<Stream<Uint8List>> textToAudio(String textPrompt) async {
      WidgetsFlutterBinding.ensureInitialized();

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

      final prompt = Content.text(textPrompt);

      await _session.send(input: prompt);

      return _session.receive().asyncMap((response) async {
        if (response is LiveServerContent && response.modelTurn?.parts != null) {
           for (final part in response.modelTurn!.parts) {
             if (part is InlineDataPart) {
               return part.bytes;
             }
           }
        }
        throw Exception('Audio data not found');
      });
    }

    Future<void> main() async {
      try {
        final audioStream = await textToAudio('Convert this text to audio.');

        await for (final audioData in audioStream) {
          // Process the audio data (e.g., play it using an audio player package)
          print('Received audio data: ${audioData.length} bytes');
          // Example using flutter_sound (replace with your chosen package):
          // await _flutterSoundPlayer.startPlayer(fromDataBuffer: audioData);
        }
      } catch (e) {
        print('Error: $e');
      }
    }

### Unity

To use the Live API, create a
[`LiveModel`](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-generative-model)
instance and set the
[response modality](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api)
to `Audio`.


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

      // Provide a text prompt
      var prompt = ModelContent.Text("Convert this text to audio.");
      await session.SendAsync(content: prompt, turnComplete: true);

      // Start receiving the response
      await ReceiveAudio(session);
    }

    Queue<float> audioBuffer = new();

    async Task ReceiveAudio(LiveSession session) {
      int sampleRate = 24000;
      int channelCount = 1;

      // Create a looping AudioClip to fill with the received audio data
      int bufferSamples = (int)(sampleRate * channelCount);
      AudioClip clip = AudioClip.Create("StreamingPCM", bufferSamples, channelCount,
                                        sampleRate, true, OnAudioRead);

      // Attach the clip to an AudioSource and start playing it
      AudioSource audioSource = GetComponent<AudioSource>();
      audioSource.clip = clip;
      audioSource.loop = true;
      audioSource.Play();

      // Start receiving the response
      await foreach (var message in session.ReceiveAsync()) {
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

Note that you can also send text as
[incremental content updates](https://firebase.google.com/docs/ai-logic/live-api/sessions#add-incremental-content-updates)
during an active session.

### Stream video + audio input

Providing input video content provides visual context for the input audio.

The Live API expects a sequence of discrete image frames and supports video
frames input at 1 frame per second (FPS).

- **Recommended input**: native 768x768 resolution at 1 FPS.

- **Supported MIME types** : `video/x-flv`, `video/quicktime`, `video/mpeg`,
  `video/mpegs`, `video/mpg`, `video/mp4`, `video/webm`, `video/wmv`, `video/3gpp`

Streaming video + audio input is a more advanced implementation, so check out a
sample app to learn how to implement this capability:
**Swift** - coming soon! \|
**Android** - [sample app](https://github.com/firebase/quickstart-android/tree/master/firebase-ai/app/src/main/java/com/google/firebase/quickstart/ai/feature/live) \|
**Web** - coming soon! \|
**Flutter** - [sample app](https://github.com/flutter/demos/tree/main/firebase_ai_logic_showcase/lib/demos/live_api) \|
**Unity** - coming soon!

<br />

*** ** * ** ***

## Not supported features

- Features *not **yet*** supported by
  Firebase AI Logic when using the Live API,
  but they're coming soon!

  - Handling interruptions

  - Some aspects of session management, including
    resuming a session across multiple connections,
    extending the session length, or
    compressing the context window.
    Note, though, that
    [*going away* notifications](https://firebase.google.com/docs/ai-logic/live-api/sessions#going-away-notification)
    are supported.

  - Disabling and configuring voice activity detection (VAD)

  - Setting input media resolution

  - Adding a thinking configuration

  - Enabling affective dialogue or proactive audio

  - Receiving `UsageMetadata` in the response

- Features *not* supported by
  Firebase AI Logic when using the Live API,
  and they're unplanned right now.

  - Server prompt templates

  - Hybrid or on-device inference

  - AI monitoring in the Firebase console

> [!NOTE]
> **Note:** Firebase AI Logic does *not yet* support using text-to-speech (TTS) models, speech-to-speech (S2S) models, or Lyria models.

<br />

*** ** * ** ***

## What else can you do?

- Customize your implementation by using various
  [configuration options](https://firebase.google.com/docs/ai-logic/live-api/configuration),
  like adding transcription or setting the response voice.

- Learn about
  [managing sessions](https://firebase.google.com/docs/ai-logic/live-api/sessions), including updating
  content mid-session and detecting when a session is about to end.

- Supercharge your implementation by giving the model access to
  tools, like function calling and grounding with Google Search. Official
  documentation for using tools with the Live API is coming soon!

- Learn about
  [limits and specifications](https://firebase.google.com/docs/ai-logic/live-api/limits-and-specs),
  for using the Live API,
  like session length, rate limits, supported languages, etc.