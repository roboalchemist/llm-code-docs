# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI.md.txt

# FirebaseAILogic Framework Reference

# FirebaseAI

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public final class FirebaseAI : Sendable

The Firebase AI SDK provides access to Gemini models directly from your app.
[## Public APIs](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI#/Public-APIs)

- `


  ### [firebaseAI(app:backend:useLimitedUseAppCheckTokens:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI#/s:15FirebaseAILogic0A2AIC08firebaseC03app7backend27useLimitedUseAppCheckTokensACSo6FIRAppCSg_AA7BackendVSbtFZ)


  ` Creates an instance of `FirebaseAI`.

  #### Declaration

  Swift

      public static func firebaseAI(app: FirebaseApp? = nil,
                                    backend: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Backend.html = .googleAI(),
                                    useLimitedUseAppCheckTokens: Bool = false) -> FirebaseAI

  #### Parameters

  |---|---|
  | ` app ` | A custom `FirebaseApp` used for initialization; if not specified, uses the default `FirebaseApp`. |
  | ` backend ` | The backend API for the Firebase AI SDK; if not specified, uses the default `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Backend.html#/s:15FirebaseAILogic7BackendV8googleAIACyFZ` (Gemini Developer API). |
  | ` useLimitedUseAppCheckTokens ` | When sending tokens to the backend, this option enables the usage of App Check's limited-use tokens instead of the standard cached tokens. Learn more about [limited-use tokens](https://firebase.google.com/docs/ai-logic/app-check), including their nuances, when to use them, and best practices for integrating them into your app. |

  #### Return Value

  A `FirebaseAI` instance, configured with the custom `FirebaseApp`.
- `


  ### [generativeModel(modelName:generationConfig:safetySettings:tools:toolConfig:systemInstruction:requestOptions:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI#/s:15FirebaseAILogic0A2AIC15generativeModel9modelName16generationConfig14safetySettings5tools04toolI017systemInstruction14requestOptionsAA010GenerativeE0CSS_AA010GenerationI0VSgSayAA13SafetySettingVGSgSayAA4ToolVGSgAA0vI0VSgAA0E7ContentVSgAA07RequestQ0VtF)


  ` Initializes a generative model with the given parameters.
  Note

  Refer to [Gemini models](https://firebase.google.com/docs/vertex-ai/gemini-models) for
  guidance on choosing an appropriate model for your use case.

  #### Declaration

  Swift

      public func generativeModel(modelName: String,
                                  generationConfig: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GenerationConfig.html? = nil,
                                  safetySettings: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/SafetySetting.html]? = nil,
                                  tools: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Tool.html]? = nil,
                                  toolConfig: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ToolConfig.html? = nil,
                                  systemInstruction: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent.html? = nil,
                                  requestOptions: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/RequestOptions.html = https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/RequestOptions.html())
        -> https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/GenerativeModel.html

  #### Parameters

  |---|---|
  | ` modelName ` | The name of the model to use; see [available model names](https://firebase.google.com/docs/vertex-ai/gemini-models#available-model-names) for a list of supported model names. |
  | ` generationConfig ` | The content generation parameters your model should use. |
  | ` safetySettings ` | A value describing what types of harmful content your model should allow. |
  | ` tools ` | A list of `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Tool.html` objects that the model may use to generate the next response. |
  | ` toolConfig ` | Tool configuration for any `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Tool.html` specified in the request. |
  | ` systemInstruction ` | Instructions that direct the model to behave a certain way; currently only text content is supported. |
  | ` requestOptions ` | Configuration parameters for sending requests to the backend. |

- `


  ### [imagenModel(modelName:generationConfig:safetySettings:requestOptions:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI#/s:15FirebaseAILogic0A2AIC11imagenModel9modelName16generationConfig14safetySettings14requestOptionsAA06ImagenE0CSS_AA0n10GenerationI0VSgAA0n6SafetyK0VSgAA07RequestM0VtF)


  ` Initializes an `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/ImagenModel.html` with the given parameters.
  Note

  Refer to [Imagen models](https://firebase.google.com/docs/vertex-ai/models) for
  guidance on choosing an appropriate model for your use case.

  #### Declaration

  Swift

      public func imagenModel(modelName: String, generationConfig: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ImagenGenerationConfig.html? = nil,
                              safetySettings: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ImagenSafetySettings.html? = nil,
                              requestOptions: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/RequestOptions.html = https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/RequestOptions.html()) -> https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/ImagenModel.html

  #### Parameters

  |---|---|
  | ` modelName ` | The name of the Imagen 3 model to use. |
  | ` generationConfig ` | Configuration options for generating images with Imagen. |
  | ` safetySettings ` | Settings describing what types of potentially harmful content your model should allow. |
  | ` requestOptions ` | Configuration parameters for sending requests to the backend. |

- `


  ### [templateGenerativeModel()](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI#/s:15FirebaseAILogic0A2AIC23templateGenerativeModelAA08TemplateeF0CyF)


  ` Initializes a new `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/TemplateGenerativeModel.html`.

  #### Declaration

  Swift

      public func templateGenerativeModel() -> https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/TemplateGenerativeModel.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/TemplateGenerativeModel.html` instance.
- `


  ### [templateImagenModel()](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI#/s:15FirebaseAILogic0A2AIC19templateImagenModelAA08TemplateeF0CyF)


  ` Initializes a new `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/TemplateImagenModel.html`.

  #### Declaration

  Swift

      public func templateImagenModel() -> https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/TemplateImagenModel.html

  #### Return Value

  A new `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/TemplateImagenModel.html` instance.
- `


  ### [liveModel(modelName:generationConfig:tools:toolConfig:systemInstruction:requestOptions:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/FirebaseAI#/s:15FirebaseAILogic0A2AIC9liveModel9modelName16generationConfig5tools04toolI017systemInstruction14requestOptionsAA014LiveGenerativeE0CSS_AA0p10GenerationI0VSgSayAA4ToolVGSgAA0sI0VSgAA0E7ContentVSgAA07RequestO0VtF)


  ` **\[Public Preview\]** Initializes a `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel.html` with the given parameters.
  Note
  Refer to [the Firebase docs on the Live
  API](https://firebase.google.com/docs/ai-logic/live-api#models-that-support-capability) for guidance on choosing an appropriate model for your use case. Warning

  Using the Firebase AI Logic SDKs with the Gemini Live API is in Public
  Preview, which means that the feature is not subject to any SLA or deprecation policy and
  could change in backwards-incompatible ways.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, *)
      @available(watchOS, unavailable)
      public func liveModel(modelName: String,
                            generationConfig: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/LiveGenerationConfig.html? = nil,
                            tools: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Tool.html]? = nil,
                            toolConfig: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ToolConfig.html? = nil,
                            systemInstruction: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ModelContent.html? = nil,
                            requestOptions: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/RequestOptions.html = https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/RequestOptions.html()) -> https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/LiveGenerativeModel.html

  #### Parameters

  |---|---|
  | ` modelName ` | The name of the model to use. |
  | ` generationConfig ` | The content generation parameters your model should use. |
  | ` tools ` | A list of `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Tool.html` objects that the model may use to generate the next response. |
  | ` toolConfig ` | Tool configuration for any `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Tool.html` specified in the request. |
  | ` systemInstruction ` | Instructions that direct the model to behave a certain way; currently only text content is supported. |
  | ` requestOptions ` | Configuration parameters for sending requests to the backend. |