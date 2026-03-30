# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig.md.txt

# FirebaseVertexAI Framework Reference

# ImagenGenerationConfig

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ImagenGenerationConfig

Configuration options for generating images with Imagen.

See [Parameters for Imagen
models](https://firebase.google.com/docs/vertex-ai/model-parameters?platform=ios#imagen) to
learn about parameters available for use with Imagen models, including how to configure them.
- `


  ### [negativePrompt](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig#/s:16FirebaseVertexAI22ImagenGenerationConfigV14negativePromptSSSgvp)


  ` Specifies elements to exclude from the generated image.

  Defaults to `nil`, which disables negative prompting. Use a comma-separated list to describe
  unwanted elements or characteristics. See the [Cloud
  documentation](https://cloud.google.com/vertex-ai/generative-ai/docs/image/generate-images#negative-prompt)
  for more details.
  Important

  Support for negative prompts depends on the Imagen model.

  #### Declaration

  Swift

      public var negativePrompt: String?

- `


  ### [numberOfImages](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig#/s:16FirebaseVertexAI22ImagenGenerationConfigV14numberOfImagesSiSgvp)


  ` The number of image samples to generate; defaults to 1 if not specified.
  Important

  The number of sample images that may be generated in each request depends on the
  model (typically up to 4); see the
  [`sampleCount`](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#parameter_list)
  documentation for more details.

  #### Declaration

  Swift

      public var numberOfImages: Int?

- `


  ### [aspectRatio](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig#/s:16FirebaseVertexAI22ImagenGenerationConfigV11aspectRatioAA0d6AspectH0VSgvp)


  ` The aspect ratio of generated images.

  Defaults to to square, 1:1. Supported aspect ratios depend on the model; see
  `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenAspectRatio.html` for more details.

  #### Declaration

  Swift

      public var aspectRatio: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenAspectRatio.html?

- `


  ### [imageFormat](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig#/s:16FirebaseVertexAI22ImagenGenerationConfigV11imageFormatAA0d5ImageH0VSgvp)


  ` The image format of generated images.

  Defaults to PNG. See `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenImageFormat.html` for more details.

  #### Declaration

  Swift

      public var imageFormat: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenImageFormat.html?

- `


  ### [addWatermark](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig#/s:16FirebaseVertexAI22ImagenGenerationConfigV12addWatermarkSbSgvp)


  ` Whether to add an invisible watermark to generated images.

  If `true`, an invisible SynthID watermark is embedded in generated images to indicate that
  they are AI generated; `false` disables watermarking.
  Important

  The default value depends on the model; see the
  [`addWatermark`](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#parameter_list)
  documentation for model-specific details.

  #### Declaration

  Swift

      public var addWatermark: Bool?

- `


  ### [init(negativePrompt:numberOfImages:aspectRatio:imageFormat:addWatermark:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig#/s:16FirebaseVertexAI22ImagenGenerationConfigV14negativePrompt14numberOfImages11aspectRatio11imageFormat12addWatermarkACSSSg_SiSgAA0d6AspectM0VSgAA0d5ImageO0VSgSbSgtcfc)


  ` Initializes configuration options for generating images with Imagen.

  #### Declaration

  Swift

      public init(negativePrompt: String? = nil, numberOfImages: Int? = nil,
                  aspectRatio: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenAspectRatio.html? = nil, imageFormat: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenImageFormat.html? = nil,
                  addWatermark: Bool? = nil)

  #### Parameters

  |---|---|
  | ` negativePrompt ` | Specifies elements to exclude from the generated image; disabled if not specified. See `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig.html#/s:16FirebaseVertexAI22ImagenGenerationConfigV14negativePromptSSSgvp`. |
  | ` numberOfImages ` | The number of image samples to generate; defaults to 1 if not specified. See `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig.html#/s:16FirebaseVertexAI22ImagenGenerationConfigV14numberOfImagesSiSgvp`. |
  | ` aspectRatio ` | The aspect ratio of generated images; defaults to to square, 1:1. See `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig.html#/s:16FirebaseVertexAI22ImagenGenerationConfigV11aspectRatioAA0d6AspectH0VSgvp`. |
  | ` imageFormat ` | The image format of generated images; defaults to PNG. See `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig.html#/s:16FirebaseVertexAI22ImagenGenerationConfigV11imageFormatAA0d5ImageH0VSgvp`. |
  | ` addWatermark ` | Whether to add an invisible watermark to generated images; the default value depends on the model. See `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenGenerationConfig.html#/s:16FirebaseVertexAI22ImagenGenerationConfigV12addWatermarkSbSgvp`. |