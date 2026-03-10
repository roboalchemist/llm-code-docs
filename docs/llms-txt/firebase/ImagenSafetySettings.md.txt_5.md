# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenSafetySettings.md.txt

# FirebaseVertexAI Framework Reference

# ImagenSafetySettings

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ImagenSafetySettings

Settings for controlling the aggressiveness of filtering out sensitive content.

See the [Responsible AI and usage
guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#config-safety-filters)
for more details.
- `


  ### [init(safetyFilterLevel:personFilterLevel:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenSafetySettings#/s:16FirebaseVertexAI20ImagenSafetySettingsV17safetyFilterLevel06personhI0AcA0dehI0VSg_AA0d6PersonhI0VSgtcfc)


  ` Initializes safety settings for the Imagen model.

  #### Declaration

  Swift

      public init(safetyFilterLevel: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenSafetyFilterLevel.html? = nil,
                  personFilterLevel: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenPersonFilterLevel.html? = nil)

  #### Parameters

  |---|---|
  | ` safetyFilterLevel ` | A filter level controlling how aggressively to filter out sensitive content from generated images. |
  | ` personFilterLevel ` | A filter level controlling whether generation of images containing people or faces is allowed. |