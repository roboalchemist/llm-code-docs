# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionDeclaration.md.txt

# FirebaseAILogic Framework Reference

# FunctionDeclaration

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public struct FunctionDeclaration : Sendable

    extension FunctionDeclaration: Encodable

Structured representation of a function declaration.

This `FunctionDeclaration` is a representation of a block of code that can be used as a `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/Tool.html`
by the model and executed by the client.
- `


  ### [init(name:description:parameters:optionalParameters:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionDeclaration#/s:15FirebaseAILogic19FunctionDeclarationV4name11description10parameters18optionalParametersACSS_SSSDySSAA6SchemaCGSaySSGtcfc)


  ` Constructs a new `FunctionDeclaration`.

  #### Declaration

  Swift

      public init(name: String, description: String, parameters: [String: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Classes/Schema.html],
                  optionalParameters: [String] = [])

  #### Parameters

  |---|---|
  | ` name ` | The name of the function; must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 63. |
  | ` description ` | A brief description of the function. |
  | ` parameters ` | Describes the parameters to this function. |
  | ` optionalParameters ` | The names of parameters that may be omitted by the model in function calls; by default, all parameters are considered required. |

[## Codable Conformance](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionDeclaration#/Codable-Conformance)

- `


  ### [encode(to:)](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/FunctionDeclaration#/s:SE6encode2toys7Encoder_p_tKF)


  `

  #### Declaration

  Swift

      public func encode(to encoder: Encoder) throws