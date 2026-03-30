# Source: https://firebase.google.com/docs/ai-logic/live-api/configuration.md.txt

> [!WARNING]
> **Preview** : Using the Firebase AI Logic SDKs with the Gemini Live API is a feature that's in Preview, which means that it isn't subject to any SLA or deprecation policy and could change in backwards-incompatible ways.

<br />

Even with the basic implementation for the Live API, you can build engaging
and powerful interactions for your users.
You can optionally customize the experience even more by using the following
configuration options:

- [Response voice and language](https://firebase.google.com/docs/ai-logic/live-api/configuration#change-voice-and-language)

- [Transcriptions for audio input and output](https://firebase.google.com/docs/ai-logic/live-api/configuration#transcriptions)

- [Voice activity detection (VAD)](https://firebase.google.com/docs/ai-logic/live-api/configuration#vad)

- [Session management](https://firebase.google.com/docs/ai-logic/live-api/configuration#session-management)

> [!NOTE]
> **Note:** Firebase AI Logic does *not yet* support the following when using the Live API (but they're coming soon!):  
> Adding a thinking configuration, setting the input media resolution, or configuring and disabling VAD.

<br />

*** ** * ** ***

## Response voice and language

You can make the model
[respond in a specific voice](https://firebase.google.com/docs/ai-logic/live-api/configuration#specify-response-voice) and
influence the model to
[respond in different languages](https://firebase.google.com/docs/ai-logic/live-api/configuration#influence-response-language).

### Specify a response voice

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

The Live API uses Chirp 3 to support synthesized speech responses in
HD voices.

If you don't specify a response voice, the default is `Puck`.

<br />

View list of response voice options

<br />

For demos of what each voice sounds like, see
[Chirp 3: HD voices](https://cloud.google.com/text-to-speech/docs/chirp3-hd).

|---|---|---|
| `Zephyr` -- *Bright* `Kore` -- *Firm* `Orus` -- *Firm* `Autonoe` -- *Bright* `Umbriel` -- *Easy-going* `Erinome` -- *Clear* `Laomedeia` -- *Upbeat* `Schedar` -- *Even* `Achird` -- *Friendly* `Sadachbia` -- *Lively* | `Puck` -- *Upbeat* `Fenrir` -- *Excitable* `Aoede` -- *Breezy* `Enceladus` -- *Breathy* `Algieba` -- *Smooth* `Algenib` -- *Gravelly* `Achernar` -- *Soft* `Gacrux` -- *Mature* `Zubenelgenubi` -- *Casual* `Sadaltager` -- *Knowledgeable* | `Charon` -- *Informative* `Leda` -- *Youthful* `Callirrhoe` -- *Easy-going* `Iapetus` -- *Clear* `Despina` -- *Smooth* `Rasalgethi` -- *Informative* `Alnilam` -- *Firm* `Pulcherrima` -- *Forward* `Vindemiatrix` -- *Gentle* `Sulafat` -- *Warm* |

<br />

<br />

To specify a response voice, set the voice name within the `speechConfig` object
as part of the
[model configuration](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api).

### Swift


    // ...

    let liveModel = FirebaseAI.firebaseAI(backend: .googleAI()).liveModel(
      modelName: "gemini-2.5-flash-native-audio-preview-12-2025",
      // Configure the model to use a specific voice for its audio response
      generationConfig: LiveGenerationConfig(
        responseModalities: [.audio],
        speech: SpeechConfig(voiceName: "VOICE_NAME")
      )
    )

    // ...

### Kotlin


    // ...

    val model = Firebase.ai(backend = GenerativeBackend.googleAI()).liveModel(
        modelName = "gemini-2.5-flash-native-audio-preview-12-2025",
        // Configure the model to use a specific voice for its audio response
        generationConfig = liveGenerationConfig {
            responseModality = ResponseModality.AUDIO
            speechConfig = SpeechConfig(voice = Voice("VOICE_NAME"))
        }
    )

    // ...

### Java


    // ...

    LiveGenerativeModel lm = FirebaseAI.getInstance(GenerativeBackend.googleAI()).liveModel(
        "gemini-2.5-flash-native-audio-preview-12-2025",
        // Configure the model to use a specific voice for its audio response
        new LiveGenerationConfig.Builder()
            .setResponseModality(ResponseModality.AUDIO)
            .setSpeechConfig(new SpeechConfig(new Voice("VOICE_NAME")))
            .build()
    );

    // ...

### Web


    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    const liveModel = getLiveGenerativeModel(ai, {
      model: "gemini-2.5-flash-native-audio-preview-12-2025",
      // Configure the model to use a specific voice for its audio response
      generationConfig: {
        responseModalities: [ResponseModality.AUDIO],
        speechConfig: {
          voiceConfig: {
            prebuiltVoiceConfig: { voiceName: "VOICE_NAME" },
          },
        },
      },
    });

    // ...

### Dart


    // ...

    final _liveModel = FirebaseAI.googleAI().liveGenerativeModel(
      model: 'gemini-2.5-flash-native-audio-preview-12-2025',
      // Configure the model to use a specific voice for its audio response
      liveGenerationConfig: LiveGenerationConfig(
        responseModalities: [ResponseModalities.audio],
        speechConfig: SpeechConfig(voiceName: 'VOICE_NAME'),
      ),
    );

    // ...

### Unity


    // ...

    var liveModel = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetLiveModel(
        modelName: "gemini-2.5-flash-native-audio-preview-12-2025",
        // Configure the model to use a specific voice for its audio response
        liveGenerationConfig: new LiveGenerationConfig(
            responseModalities: new[] { ResponseModality.Audio },
            speechConfig: SpeechConfig.UsePrebuiltVoice("VOICE_NAME")
        )
    );

    // ...

### Influence the response language

> [!IMPORTANT]
> **Important:** The Live API models do *not* support explicitly setting a response *language* in the configuration. Instead, these models automatically choose the appropriate language for their responses.

The Live API models automatically choose the appropriate language for their
responses.

<br />

View list of supported languages

<br />

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

<br />

<br />

If you want the model to respond in a non-English language or always in a
specific language, you can use influence the model's responses by using
[system instructions](https://firebase.google.com/docs/ai-logic/system-instructions) like these examples:

- Reinforce to the model that a non-English language may be appropriate

      Listen to the speaker carefully. If you detect a non-English language, respond
      in the language you hear from the speaker. You must respond unmistakably in the
      speaker's language.

- Tell the model to always respond in a specific language

      RESPOND IN LANGUAGE. YOU MUST RESPOND UNMISTAKABLY IN LANGUAGE.

<br />

*** ** * ** ***

## Transcriptions for audio input and output

|---|
| *Click your Gemini API provider to view provider-specific content and code on this page.* <button value="dev" default="">Gemini Developer API</button> <button value="vertex">Vertex AI Gemini API</button> |

As part of the model's response, you can receive transcriptions of the
audio input and the model's audio response. You set this configuration as part
of the
[model configuration](https://firebase.google.com/docs/ai-logic/model-parameters#config-gemini-live-api).

- For transcription of the audio input, add
  `inputAudioTranscription`.

- For transcription of the model's audio response, add
  `outputAudioTranscription`.

Note the following:

- You can configure the model to return transcriptions of both input and output
  (as shown in the following example), or you can configure it to return only
  one or the other.

- The transcripts are streamed along with the audio, so it's best to collect
  them like you do text parts with each turn.

- The transcription language is inferred from the audio input and the model's
  audio response.

### Swift


    // ...

    let liveModel = FirebaseAI.firebaseAI(backend: .googleAI()).liveModel(
      modelName: "gemini-2.5-flash-native-audio-preview-12-2025",
      // Configure the model to return transcriptions of the audio input and output
      generationConfig: LiveGenerationConfig(
        responseModalities: [.audio],
        inputAudioTranscription: AudioTranscriptionConfig(),
        outputAudioTranscription: AudioTranscriptionConfig()
      )
    )

    var inputTranscript: String = ""
    var outputTranscript: String = ""

    do {
      let session = try await liveModel.connect()
      for try await response in session.responses {
        if case let .content(content) = response.payload {
          if let inputText = content.inputAudioTranscription?.text {
            // Handle transcription text of the audio input
            inputTranscript += inputText
          }

          if let outputText = content.outputAudioTranscription?.text {
            // Handle transcription text of the audio output
            outputTranscript += outputText
          }

          if content.isTurnComplete {
            // Log the transcripts after the current turn is complete
            print("Input audio: \(inputTranscript)")
            print("Output audio: \(outputTranscript)")

            // Reset the transcripts for the next turn
            inputTranscript = ""
            outputTranscript = ""
          }
        }
      }


    } catch {
      // Handle error
    }

    // ...

### Kotlin


    // ...

    val liveModel = Firebase.ai(backend = GenerativeBackend.googleAI()).liveModel(
        modelName = "gemini-2.5-flash-native-audio-preview-12-2025",
        // Configure the model to return transcriptions of the audio input and output
        generationConfig = liveGenerationConfig {
            responseModality = ResponseModality.AUDIO
            inputAudioTranscription = AudioTranscriptionConfig()
            outputAudioTranscription = AudioTranscriptionConfig()
       }
    )

    val liveSession = liveModel.connect()

    fun handleTranscription(input: Transcription?, output: Transcription?) {
        input?.text?.let { text ->
            // Handle transcription text of the audio input
            println("Input Transcription: $text")
        }
        output?.text?.let { text ->
            // Handle transcription text of the audio output
            println("Output Transcription: $text")
        }
    }

    liveSession.startAudioConversation(null, ::handleTranscription)

    // ...

### Java


    // ...

    ExecutorService executor = Executors.newFixedThreadPool(1);

    LiveGenerativeModel lm = FirebaseAI.getInstance(GenerativeBackend.googleAI()).liveModel(
        "gemini-2.5-flash-native-audio-preview-12-2025",
        // Configure the model to return transcriptions of the audio input and output
        new LiveGenerationConfig.Builder()
                .setResponseModality(ResponseModality.AUDIO)
                .setInputAudioTranscription(new AudioTranscriptionConfig())
                .setOutputAudioTranscription(new AudioTranscriptionConfig())
                .build()
        );

    LiveModelFutures liveModel = LiveModelFutures.from(lm);
    ListenableFuture sessionFuture = liveModel.connect();

    Futures.addCallback(sessionFuture, new FutureCallback() {
        @Override
        public void onSuccess(LiveSessionFutures ses) {
            LiveSessionFutures session = ses;
            session.startAudioConversation((Transcription input, Transcription output) -> {
                if (input != null) {
                    // Handle transcription text of the audio input
                    System.out.println("Input Transcription: " + input.getText());
                }
                if (output != null) {
                    // Handle transcription text of the audio output
                    System.out.println("Output Transcription: " + output.getText());
                }
                return null;
            });
        }

        @Override
        public void onFailure(Throwable t) {
            // Handle exceptions
            t.printStackTrace();
        }
    }, executor);

    // ...

### Web


    // ...

    const ai = getAI(firebaseApp, { backend: new GoogleAIBackend() });

    const liveModel = getLiveGenerativeModel(ai, {
      model: 'gemini-2.5-flash-native-audio-preview-12-2025',
      // Configure the model to return transcriptions of the audio input and output
      generationConfig: {
        responseModalities: [ResponseModality.AUDIO],
        inputAudioTranscription: {},
        outputAudioTranscription: {},
      },
    });

    const liveSession = await liveModel.connect();

    liveSession.sendAudioRealtime({ data, mimeType: "audio/pcm" });

    const messages = liveSession.receive();
    for await (const message of messages) {
      switch (message.type) {
        case 'serverContent':
          if (message.inputTranscription) {
            // Handle transcription text of the audio input
            console.log(`Input transcription: ${message.inputTranscription.text}`);
          }
          if (message.outputTranscription) {
            // Handle transcription text of the audio output
            console.log(`Output transcription: ${message.outputTranscription.text}`);
          } else {
          	 // Handle other message types (modelTurn, turnComplete, interruption)
          }
        default:
          // Handle other message types (toolCall, toolCallCancellation)
      }
    }

    // ...

### Dart


    // ...

    final _liveModel = FirebaseAI.googleAI().liveGenerativeModel(
      model: 'gemini-2.5-flash-native-audio-preview-12-2025',
      // Configure the model to return transcriptions of the audio input and output
      liveGenerationConfig: LiveGenerationConfig(
        responseModalities: [ResponseModalities.audio],
        inputAudioTranscription: AudioTranscriptionConfig(),
        outputAudioTranscription: AudioTranscriptionConfig(),
      ),
    );

    final LiveSession _session = _liveModel.connect();

    await for (final response in _session.receive()) {
      LiveServerContent message = response.message;
      if (message.inputTranscription?.text case final inputText?) {
        // Handle transcription text of the audio input
        print('Input: $inputText');
      }

      if (message.outputTranscription?.text case final outputText?) {
        // Handle transcription text of the audio output
        print('Output: $outputText');
      }
    }

    // ...

### Unity


    // ...

    var liveModel = FirebaseAI.GetInstance(FirebaseAI.Backend.GoogleAI()).GetLiveModel(
        modelName: "gemini-2.5-flash-native-audio-preview-12-2025",
        // Configure the model to return transcriptions of the audio input and output
        liveGenerationConfig: new LiveGenerationConfig(
            responseModalities: new[] { ResponseModality.Audio },
            inputAudioTranscription: new AudioTranscriptionConfig(),
            outputAudioTranscription: new AudioTranscriptionConfig()
        )
    );

    try
    {
        var session = await liveModel.ConnectAsync();
        var stream = session.ReceiveAsync();
        await foreach (var response in stream) {
            if (response.Message is LiveSessionContent sessionContent) {
                if (!string.IsNullOrEmpty(sessionContent.InputTranscription?.Text)) {
                  // handle transcription text of input audio
                }

                if (!string.IsNullOrEmpty(sessionContent.OutputTranscription?.Text)) {
                  // handle transcription text of output audio
                }
            }
        }
    }
    catch (Exception e)
    {
        // Handle error
    }

    // ...

<br />

*** ** * ** ***

## Voice activity detection (VAD)

The model automatically performs voice activity detection (VAD) on a continuous
audio input stream. VAD is enabled by default.

> [!NOTE]
> **Note:** Firebase AI Logic does *not yet* support disabling VAD or configuring VAD parameters. Check back soon!

<br />

*** ** * ** ***

## Session management

- Learn about the following sessions-related topics:

  - Advanced capabilities, including:

    - [Updating system instructions mid-session](https://firebase.google.com/docs/ai-logic/live-api/sessions#update-system-instructions-mid-session)

    - [Adding incremental content updates](https://firebase.google.com/docs/ai-logic/live-api/sessions#add-incremental-content-updates)

  - [Session-related limits](https://firebase.google.com/docs/ai-logic/live-api/sessions#limits),
    including connection and session length limits,
    session context window limits, and
    rate limits.

- Firebase AI Logic does *not yet* support the following features for
  session management. Check back soon!

  - Handling interruptions
  - Extending session length
  - Resuming a session
  - Maintaining context across sessions and requests
  - Compressing the context window