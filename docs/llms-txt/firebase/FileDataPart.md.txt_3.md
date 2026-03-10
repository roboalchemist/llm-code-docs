# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FileDataPart.md.txt

# FirebaseAILogic Framework Reference

# FileDataPart

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct FileDataPart : https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html

File data stored in Cloud Storage for Firebase, referenced by URI.
- `


  ### [uri](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FileDataPart#/s:15FirebaseAILogic12FileDataPartV3uriSSvp)


  ` Undocumented

  #### Declaration

  Swift

      public var uri: String { get }

- `


  ### [mimeType](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FileDataPart#/s:15FirebaseAILogic12FileDataPartV8mimeTypeSSvp)


  ` Undocumented

  #### Declaration

  Swift

      public var mimeType: String { get }

- `


  ### [isThought](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FileDataPart#/s:15FirebaseAILogic4PartP9isThoughtSbvp)


  `

  #### Declaration

  Swift

      public var isThought: Bool { get }

- `


  ### [init(uri:mimeType:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FileDataPart#/s:15FirebaseAILogic12FileDataPartV3uri8mimeTypeACSS_SStcfc)


  ` Constructs a new file data part.

  #### Declaration

  Swift

      public init(uri: String, mimeType: String)

  #### Parameters

  |---|---|
  | ` uri ` | The `"gs://"`-prefixed URI of the file in Cloud Storage for Firebase, for example, `"gs://bucket-name/path/image.jpg"`. |
  | ` mimeType ` | The IANA standard MIME type of the uploaded file, for example, `"image/jpeg"` or `"video/mp4"`; see [supported input files and requirements](https://firebase.google.com/docs/vertex-ai/input-file-requirements) for supported values. |