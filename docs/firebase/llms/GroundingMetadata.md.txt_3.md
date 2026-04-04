# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.md.txt

# FirebaseAILogic Framework Reference

# GroundingMetadata

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct GroundingMetadata : Sendable, Equatable, Hashable

    extension GroundingMetadata: Decodable

Metadata returned to the client when grounding is enabled.
Important

If using Grounding with Google Search, you are required to comply with the
"Grounding with Google Search" usage requirements for your chosen API provider:
[Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search)
or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms)
section within the Service Specific Terms).
- `


  ### [webSearchQueries](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata#/s:15FirebaseAILogic17GroundingMetadataV16webSearchQueriesSaySSGvp)


  ` A list of web search queries that the model performed to gather the grounding information.
  These can be used to allow users to explore the search results themselves.

  #### Declaration

  Swift

      public let webSearchQueries: [String]

- `


  ### [groundingChunks](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata#/s:15FirebaseAILogic17GroundingMetadataV15groundingChunksSayAC0C5ChunkVGvp)


  ` A list of `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingChunk.html` structs. Each chunk represents a piece of retrieved content
  (e.g., from a web page) that the model used to ground its response.

  #### Declaration

  Swift

      public let groundingChunks: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingChunk.html]

- `


  ### [groundingSupports](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata#/s:15FirebaseAILogic17GroundingMetadataV17groundingSupportsSayAC0C7SupportVGvp)


  ` A list of `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingSupport.html` structs. Each object details how specific segments of the
  model's response are supported by the `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.html#/s:15FirebaseAILogic17GroundingMetadataV15groundingChunksSayAC0C5ChunkVGvp`.

  #### Declaration

  Swift

      public let groundingSupports: [https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingSupport.html]

- `


  ### [searchEntryPoint](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata#/s:15FirebaseAILogic17GroundingMetadataV16searchEntryPointAC06SearchfG0VSgvp)


  ` Google Search entry point for web searches.
  This contains an HTML/CSS snippet that **must** be embedded in an app to display a Google
  Search entry point for follow-up web searches related to the model's "Grounded Response".

  #### Declaration

  Swift

      public let searchEntryPoint: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/SearchEntryPoint.html?

- `


  ### [SearchEntryPoint](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/SearchEntryPoint.html)


  ` A struct representing the Google Search entry point.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct SearchEntryPoint : Sendable, Equatable, Hashable

      extension https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.html.SearchEntryPoint: Decodable

- `


  ### [GroundingChunk](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingChunk.html)


  ` Represents a chunk of retrieved data that supports a claim in the model's response. This is
  part of the grounding information provided when grounding is enabled.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct GroundingChunk : Sendable, Equatable, Hashable

      extension https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.html.GroundingChunk: Decodable

- `


  ### [WebGroundingChunk](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/WebGroundingChunk.html)


  ` A grounding chunk sourced from the web.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct WebGroundingChunk : Sendable, Equatable, Hashable

      extension https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata.html.WebGroundingChunk: Decodable

- `


  ### [GroundingSupport](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata/GroundingSupport.html)


  ` Provides information about how a specific segment of the model's response is supported by the
  retrieved grounding chunks.

  #### Declaration

  Swift

      @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
      public struct GroundingSupport : Sendable, Equatable, Hashable

[## Codable Conformances](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata#/Codable-Conformances)

- `


  ### [init(from:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GroundingMetadata#/s:Se4fromxs7Decoder_p_tKcfc)


  `

  #### Declaration

  Swift

      public init(from decoder: Decoder) throws