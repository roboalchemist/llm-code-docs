# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ai/FirebaseAI.md.txt

# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/ai/FirebaseAI.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/FirebaseAI.md.txt

# FirebaseAI

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public final class FirebaseAI : Sendable

The Firebase AI SDK provides access to Gemini models directly from your app.
[## Public APIs](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/FirebaseAI#/Public-APIs)

- `
  ``
  ``
  `

  ### [firebaseAI(app:backend:useLimitedUseAppCheckTokens:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/FirebaseAI#/s:10FirebaseAIAAC08firebaseB03app7backend27useLimitedUseAppCheckTokensABSo6FIRAppCSg_AA7BackendVSbtFZ)

  `
  `  
  Creates an instance of `FirebaseAI`.  

  #### Declaration

  Swift  

      public static func firebaseAI(app: FirebaseApp? = nil,
                                    backend: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Backend.html = .googleAI(),
                                    useLimitedUseAppCheckTokens: Bool = false) -> FirebaseAI

  #### Parameters

  |-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*app*` `                         | A custom `FirebaseApp` used for initialization; if not specified, uses the default `FirebaseApp`.                                                                                                                                                                                                                                        |
  | ` `*backend*` `                     | The backend API for the Firebase AI SDK; if not specified, uses the default [googleAI()](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Backend.html#/s:10FirebaseAI7BackendV06googleB0ACyFZ) (Gemini Developer API).                                                                                 |
  | ` `*useLimitedUseAppCheckTokens*` ` | When sending tokens to the backend, this option enables the usage of App Check's limited-use tokens instead of the standard cached tokens. Learn more about [limited-use tokens](https://firebase.google.com/docs/ai-logic/app-check), including their nuances, when to use them, and best practices for integrating them into your app. |

  #### Return Value

  A `FirebaseAI` instance, configured with the custom `FirebaseApp`.
- `
  ``
  ``
  `

  ### [generativeModel(modelName:generationConfig:safetySettings:tools:toolConfig:systemInstruction:requestOptions:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/FirebaseAI#/s:10FirebaseAIAAC15generativeModel9modelName16generationConfig14safetySettings5tools04toolH017systemInstruction14requestOptionsAA010GenerativeD0CSS_AA010GenerationH0VSgSayAA13SafetySettingVGSgSayAA4ToolVGSgAA0uH0VSgAA0D7ContentVSgAA07RequestP0VtF)

  `
  `  
  Initializes a generative model with the given parameters.  
  Note

  Refer to [Gemini models](https://firebase.google.com/docs/vertex-ai/gemini-models) for
  guidance on choosing an appropriate model for your use case.  

  #### Declaration

  Swift  

      public func generativeModel(modelName: String,
                                  generationConfig: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/GenerationConfig.html? = nil,
                                  safetySettings: [https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/SafetySetting.html]? = nil,
                                  tools: [https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool.html]? = nil,
                                  toolConfig: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ToolConfig.html? = nil,
                                  systemInstruction: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ModelContent.html? = nil,
                                  requestOptions: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/RequestOptions.html = https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/RequestOptions.html())
        -> https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/GenerativeModel.html

  #### Parameters

  |---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*modelName*` `         | The name of the model to use, for example `"gemini-1.5-flash"`; see [available model names](https://firebase.google.com/docs/vertex-ai/gemini-models#available-model-names) for a list of supported model names. |
  | ` `*generationConfig*` `  | The content generation parameters your model should use.                                                                                                                                                         |
  | ` `*safetySettings*` `    | A value describing what types of harmful content your model should allow.                                                                                                                                        |
  | ` `*tools*` `             | A list of [Tool](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool.html) objects that the model may use to generate the next response.                                      |
  | ` `*toolConfig*` `        | Tool configuration for any [Tool](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool.html) specified in the request.                                                         |
  | ` `*systemInstruction*` ` | Instructions that direct the model to behave a certain way; currently only text content is supported.                                                                                                            |
  | ` `*requestOptions*` `    | Configuration parameters for sending requests to the backend.                                                                                                                                                    |

- `
  ``
  ``
  `

  ### [imagenModel(modelName:generationConfig:safetySettings:requestOptions:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/FirebaseAI#/s:10FirebaseAIAAC11imagenModel9modelName16generationConfig14safetySettings14requestOptionsAA06ImagenD0CSS_AA0m10GenerationH0VSgAA0m6SafetyJ0VSgAA07RequestL0VtF)

  `
  `  
  Initializes an [ImagenModel](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/ImagenModel.html) with the given parameters.  
  Important

  Only Imagen 3 models (named `imagen-3.0-*`) are supported.  

  #### Declaration

  Swift  

      public func imagenModel(modelName: String, generationConfig: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenGenerationConfig.html? = nil,
                              safetySettings: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ImagenSafetySettings.html? = nil,
                              requestOptions: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/RequestOptions.html = https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/RequestOptions.html()) -> https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/ImagenModel.html

  #### Parameters

  |--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*modelName*` `        | The name of the Imagen 3 model to use, for example `"imagen-3.0-generate-002"`; see [model versions](https://firebase.google.com/docs/vertex-ai/models) for a list of supported Imagen 3 models. |
  | ` `*generationConfig*` ` | Configuration options for generating images with Imagen.                                                                                                                                         |
  | ` `*safetySettings*` `   | Settings describing what types of potentially harmful content your model should allow.                                                                                                           |
  | ` `*requestOptions*` `   | Configuration parameters for sending requests to the backend.                                                                                                                                    |

- `
  ``
  ``
  `

  ### [liveModel(modelName:generationConfig:tools:toolConfig:systemInstruction:requestOptions:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/FirebaseAI#/s:10FirebaseAIAAC9liveModel9modelName16generationConfig5tools04toolH017systemInstruction14requestOptionsAA014LiveGenerativeD0CSS_AA0o10GenerationH0VSgSayAA4ToolVGSgAA0rH0VSgAA0D7ContentVSgAA07RequestN0VtF)

  `
  `  
  **\[Public Preview\]** Initializes a [LiveGenerativeModel](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/LiveGenerativeModel.html) with the given parameters.  
  Warning

  Using the Firebase AI Logic SDKs with the Gemini Live API is in Public
  Preview, which means that the feature is not subject to any SLA or deprecation policy and
  could change in backwards-incompatible ways.

  Important: Only models that support the Gemini Live API (typically containing `live-*` in
  the name) are supported.  

  #### Declaration

  Swift  

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public func liveModel(modelName: String,
                            generationConfig: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/LiveGenerationConfig.html? = nil,
                            tools: [https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool.html]? = nil,
                            toolConfig: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ToolConfig.html? = nil,
                            systemInstruction: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/ModelContent.html? = nil,
                            requestOptions: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/RequestOptions.html = https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/RequestOptions.html()) -> https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Classes/LiveGenerativeModel.html

  #### Parameters

  |---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*modelName*` `         | The name of the model to use, for example `"gemini-live-2.5-flash-preview"`; see [model versions](https://firebase.google.com/docs/ai-logic/live-api?api=dev#models-that-support-capability) for a list of supported models. |
  | ` `*generationConfig*` `  | The content generation parameters your model should use.                                                                                                                                                                     |
  | ` `*tools*` `             | A list of [Tool](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool.html) objects that the model may use to generate the next response.                                                  |
  | ` `*toolConfig*` `        | Tool configuration for any [Tool](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Tool.html) specified in the request.                                                                     |
  | ` `*systemInstruction*` ` | Instructions that direct the model to behave a certain way; currently only text content is supported.                                                                                                                        |
  | ` `*requestOptions*` `    | Configuration parameters for sending requests to the backend.                                                                                                                                                                |