# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/ImagenModel.md.txt

# FirebaseAILogic Framework Reference

# ImagenModel

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public final class ImagenModel

Represents a remote Imagen model with the ability to generate images using text prompts.

See the [generate images
documentation](https://firebase.google.com/docs/vertex-ai/generate-images-imagen?platform=ios)
for more details about the image generation capabilities offered by the Imagen model in the
Firebase AI SDK SDK.
- `


  ### [generateImages(prompt:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/ImagenModel#/s:15FirebaseAILogic11ImagenModelC14generateImages6promptAA0C18GenerationResponseVyAA0C11InlineImageVGSS_tYaKF)


  ` Generates images using the Imagen model and returns them as inline data.

  The individual `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ImagenInlineImage.html#/s:15FirebaseAILogic17ImagenInlineImageV4data10Foundation4DataVvp` is provided for each of the generated
  `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ImagenGenerationResponse.html#/s:15FirebaseAILogic24ImagenGenerationResponseV6imagesSayxGvp`.
  Note

  By default, 1 image sample is generated; see `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ImagenGenerationConfig.html#/s:15FirebaseAILogic22ImagenGenerationConfigV14numberOfImagesSiSgvp`
  to configure the number of images that are generated.

  #### Declaration

  Swift

      public func generateImages(prompt: String) async throws
        -> https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ImagenGenerationResponse.html<https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ImagenInlineImage.html>

  #### Parameters

  |---|---|
  | ` prompt ` | A text prompt describing the image(s) to generate. |