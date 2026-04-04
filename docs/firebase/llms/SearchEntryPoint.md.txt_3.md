# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/SearchEntryPoint.md.txt

# FirebaseAILogic Framework Reference

# SearchEntryPoint

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct SearchEntryPoint : Sendable, Equatable, Hashable

    extension https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.html.SearchEntryPoint: Decodable

A struct representing the Google Search entry point.
- `


  ### [renderedContent](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/SearchEntryPoint#/s:15FirebaseAILogic17GroundingMetadataV16SearchEntryPointV15renderedContentSSvp)


  ` An HTML/CSS snippet that can be embedded in your app.

  To ensure proper rendering, it's recommended to display this content within a `WKWebView`.

  #### Declaration

  Swift

      public let renderedContent: String