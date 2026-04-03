# Source: https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Backend.md.txt

# FirebaseAI Framework Reference

# Backend

    public struct Backend

Represents available backend APIs for the Firebase AI SDK.
[## Public API](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Backend#/Public-API)

- `
  ``
  ``
  `

  ### [vertexAI(location:)](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Backend#/s:10FirebaseAI7BackendV06vertexB08locationACSS_tFZ)

  `
  `  
  Initializes a `Backend` configured for the Gemini API in Vertex AI.  

  #### Declaration

  Swift  

      public static func vertexAI(location: String = "us-central1") -> Backend

  #### Parameters

  |------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*location*` ` | The region identifier, defaulting to `us-central1`; see [Vertex AI locations](https://firebase.google.com/docs/vertex-ai/locations?platform=ios#available-locations) for a list of supported locations. |

- `
  ``
  ``
  `

  ### [googleAI()](https://firebase.google.com/docs/reference/swift/firebaseai/api/reference/Structs/Backend#/s:10FirebaseAI7BackendV06googleB0ACyFZ)

  `
  `  
  Initializes a `Backend` configured for the Google Developer API.  

  #### Declaration

  Swift  

      public static func googleAI() -> Backend