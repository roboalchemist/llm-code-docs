# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/InlineDataPart.md.txt

# FirebaseVertexAI Framework Reference

# InlineDataPart

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct InlineDataPart : https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.html

A data part that is provided inline in requests.

Data provided as an inline data part is encoded as base64 and included directly (inline) in the
request. For large files, see `https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/FileDataPart.html` which references content by URI instead of
including the data in the request.
Important

Only small files can be sent as inline data because of limits on total request
sizes;
see [input files and requirements](https://firebase.google.com/docs/vertex-ai/input-file-requirements#provide-file-as-inline-data)
for more details and size limits.
- `


  ### [data](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/InlineDataPart#/s:16FirebaseVertexAI14InlineDataPartV4data10Foundation0E0Vvp)


  ` The data provided in the inline data part.

  #### Declaration

  Swift

      public var data: Data { get }

- `


  ### [mimeType](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/InlineDataPart#/s:16FirebaseVertexAI14InlineDataPartV8mimeTypeSSvp)


  ` The IANA standard MIME type of the data.

  #### Declaration

  Swift

      public var mimeType: String { get }

- `


  ### [init(data:mimeType:)](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Structs/InlineDataPart#/s:16FirebaseVertexAI14InlineDataPartV4data8mimeTypeAC10Foundation0E0V_SStcfc)


  ` Creates an inline data part from data and a MIME type.
  Important

  Supported input types depend on the model on the model being used; see [input
  files and requirements](https://firebase.google.com/docs/vertex-ai/input-file-requirements)
  for more details.

  #### Declaration

  Swift

      public init(data: Data, mimeType: String)

  #### Parameters

  |---|---|
  | ` data ` | The data representation of an image, video, audio or document; see [input files and requirements](https://firebase.google.com/docs/vertex-ai/input-file-requirements) for supported media types. |
  | ` mimeType ` | The IANA standard MIME type of the data, for example, `"image/jpeg"` or `"video/mp4"`; see [input files and requirements](https://firebase.google.com/docs/vertex-ai/input-file-requirements) for supported values. |