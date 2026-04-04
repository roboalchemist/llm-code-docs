# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GoogleSearch.md.txt

# FirebaseAILogic Framework Reference

# GoogleSearch

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct GoogleSearch : Sendable

    extension GoogleSearch: Encodable

A tool that allows the generative model to connect to Google Search to access and incorporate
up-to-date information from the web into its responses.
Important

When using this feature, you are required to comply with the
"Grounding with Google Search" usage requirements for your chosen API provider:
[Gemini Developer API](https://ai.google.dev/gemini-api/terms#grounding-with-google-search)
or Vertex AI Gemini API (see [Service Terms](https://cloud.google.com/terms/service-terms)
section within the Service Specific Terms).
- `


  ### [init()](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/GoogleSearch#/s:15FirebaseAILogic12GoogleSearchVACycfc)


  ` Undocumented

  #### Declaration

  Swift

      public init()