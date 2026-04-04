# Source: https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs.md.txt

# FirebaseFunctions Framework Reference

# Structures

The following structures are available globally.
- `


  ### [Callable](https://firebase.google.com/docs/reference/swift/firebasefunctions/api/reference/Structs/Callable)


  ` A `Callable` is a reference to a particular Callable HTTPS trigger in Cloud Functions.
  Note
  If the Callable HTTPS trigger accepts no parameters, `Never` can be used for iOS 17.0+. Otherwise, a simple encodable placeholder type (e.g., `struct EmptyRequest: Encodable {}`) can be used.

  #### Declaration

  Swift

      public struct Callable<Request, Response> : Sendable where Request : Encodable, Response : Decodable