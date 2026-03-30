# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenPersonFilterLevel.md.txt

# FirebaseVertexAI Framework Reference

# ImagenPersonFilterLevel

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct ImagenPersonFilterLevel : ProtoEnum

A filter level controlling whether generation of images containing people or faces is allowed.

See the
[`personGeneration`](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/imagen-api#parameter_list)
documentation for more details.
- `


  ### [blockAll](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenPersonFilterLevel#/s:16FirebaseVertexAI23ImagenPersonFilterLevelV8blockAllACvpZ)


  ` Disallow generation of images containing people or faces; images of people are filtered out.

  #### Declaration

  Swift

      public static let blockAll: ImagenPersonFilterLevel

- `


  ### [allowAdult](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenPersonFilterLevel#/s:16FirebaseVertexAI23ImagenPersonFilterLevelV10allowAdultACvpZ)


  ` Allow generation of images containing adults only; images of children are filtered out.
  Important

  Generation of images containing people or faces may require your use case to be
  reviewed and approved by Cloud support; see the [Responsible AI and usage
  guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen)
  for more details.

  #### Declaration

  Swift

      public static let allowAdult: ImagenPersonFilterLevel

- `


  ### [allowAll](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/ImagenPersonFilterLevel#/s:16FirebaseVertexAI23ImagenPersonFilterLevelV8allowAllACvpZ)


  ` Allow generation of images containing people of all ages.
  Important

  Generation of images containing people or faces may require your use case to be
  reviewed and approved; see the [Responsible AI and usage
  guidelines](https://cloud.google.com/vertex-ai/generative-ai/docs/image/responsible-ai-imagen#person-face-gen)
  for more details.

  #### Declaration

  Swift

      public static let allowAll: ImagenPersonFilterLevel