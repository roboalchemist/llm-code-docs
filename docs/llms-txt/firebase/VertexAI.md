# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/VertexAI.md.txt

# FirebaseVertexAI Framework Reference

# VertexAI

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public class VertexAI

The Vertex AI for Firebase SDK provides access to Gemini models directly from your app.
[## Public APIs](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/VertexAI#/Public-APIs)

- `
  ``
  ``
  `

  ### [vertexAI(app:location:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/VertexAI#/s:16FirebaseVertexAI0bC0C06vertexC03app8locationACSo6FIRAppCSg_SStFZ)

  `
  `  
  Creates an instance of `VertexAI`.  

  #### Declaration

  Swift  

      public static func vertexAI(app: FirebaseApp? = nil,
                                  location: String = "us-central1") -> VertexAI

  #### Return Value

  A `VertexAI` instance, configured with the custom `FirebaseApp`.
- `
  ``
  ``
  `

  ### [generativeModel(modelName:generationConfig:safetySettings:tools:toolConfig:systemInstruction:requestOptions:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/VertexAI#/s:16FirebaseVertexAI0bC0C15generativeModel9modelName16generationConfig14safetySettings5tools04toolI017systemInstruction14requestOptionsAA010GenerativeE0CSS_AA010GenerationI0VSgSayAA13SafetySettingVGSgSayAA4ToolVGSgAA0vI0VSgAA0E7ContentVSgAA07RequestQ0VtF)

  `
  `  
  Initializes a generative model with the given parameters.  
  Note

  Refer to [Gemini models](https://firebase.google.com/docs/vertex-ai/gemini-models) for
  guidance on choosing an appropriate model for your use case.  

  #### Declaration

  Swift  

      public func generativeModel(modelName: String,
                                  generationConfig: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/GenerationConfig.html? = nil,
                                  safetySettings: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/SafetySetting.html]? = nil,
                                  tools: [https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Tool.html]? = nil,
                                  toolConfig: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ToolConfig.html? = nil,
                                  systemInstruction: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ModelContent.html? = nil,
                                  requestOptions: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/RequestOptions.html = https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/RequestOptions.html())
        -> https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/GenerativeModel.html

  #### Parameters

  |---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*modelName*` `         | The name of the model to use, for example `"gemini-1.5-flash"`; see [available model names](https://firebase.google.com/docs/vertex-ai/gemini-models#available-model-names) for a list of supported model names. |
  | ` `*generationConfig*` `  | The content generation parameters your model should use.                                                                                                                                                         |
  | ` `*safetySettings*` `    | A value describing what types of harmful content your model should allow.                                                                                                                                        |
  | ` `*tools*` `             | A list of [Tool](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Tool.html) objects that the model may use to generate the next response.                                |
  | ` `*toolConfig*` `        | Tool configuration for any [Tool](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/Tool.html) specified in the request.                                                   |
  | ` `*systemInstruction*` ` | Instructions that direct the model to behave a certain way; currently only text content is supported.                                                                                                            |
  | ` `*requestOptions*` `    | Configuration parameters for sending requests to the backend.                                                                                                                                                    |

- `
  ``
  ``
  `

  ### [imagenModel(modelName:generationConfig:safetySettings:requestOptions:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/VertexAI#/s:16FirebaseVertexAI0bC0C11imagenModel9modelName16generationConfig14safetySettings14requestOptionsAA06ImagenE0CSS_AA0n10GenerationI0VSgAA0n6SafetyK0VSgAA07RequestM0VtF)

  `
  `  
  **\[Public Preview\]** Initializes an [ImagenModel](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/ImagenModel.html) with the given parameters.  
  Warning

  For Vertex AI in Firebase, image generation using Imagen 3 models is in Public
  Preview, which means that the feature is not subject to any SLA or deprecation policy and
  could change in backwards-incompatible ways.

  Important: Only Imagen 3 models (named `imagen-3.0-*`) are supported.  

  #### Declaration

  Swift  

      public func imagenModel(modelName: String, generationConfig: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig.html? = nil,
                              safetySettings: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenSafetySettings.html? = nil,
                              requestOptions: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/RequestOptions.html = https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/RequestOptions.html()) -> https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Classes/ImagenModel.html

  #### Parameters

  |--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*modelName*` `        | The name of the Imagen 3 model to use, for example `"imagen-3.0-generate-002"`; see [model versions](https://firebase.google.com/docs/vertex-ai/models) for a list of supported Imagen 3 models. |
  | ` `*generationConfig*` ` | Configuration options for generating images with Imagen.                                                                                                                                         |
  | ` `*safetySettings*` `   | Settings describing what types of potentially harmful content your model should allow.                                                                                                           |
  | ` `*requestOptions*` `   | Configuration parameters for sending requests to the backend.                                                                                                                                    |