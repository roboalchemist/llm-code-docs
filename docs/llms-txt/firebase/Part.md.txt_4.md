# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.md.txt

# FirebaseAILogic Framework Reference

# Part

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public protocol Part : https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/PartsRepresentable.html, Decodable, Encodable, Equatable, Sendable

A discrete piece of data in a media format interpretable by an AI model.

Within a single value of `Part`, different data types may not mix.
- `


  ### [isThought](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part#/s:15FirebaseAILogic4PartP9isThoughtSbvp)


  ` Indicates whether this `Part` is a summary of the model's internal thinking process.

  When `includeThoughts` is set to `true` in `https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Structs/ThinkingConfig.html`, the model may return one or
  more "thought" parts that provide insight into how it reasoned through the prompt to arrive
  at the final answer. These parts will have `isThought` set to `true`.

  #### Declaration

  Swift

      var isThought: Bool { get }

- `


  ### [partsValue](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part#/s:15FirebaseAILogic4PartPAAE10partsValueSayAaB_pGvp)


  ` Extension method Undocumented

  #### Declaration

  Swift

      var partsValue: [any Part] { get }