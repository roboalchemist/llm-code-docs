# Source: https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part.md.txt

# FirebaseVertexAI Framework Reference

# Part

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public protocol Part : https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/PartsRepresentable.html, Decodable, Encodable, Equatable, Sendable

A discrete piece of data in a media format interpretable by an AI model.

Within a single value of `Part`, different data types may not mix.
- `


  ### [partsValue](https://firebase.google.com/docs/reference/swift/firebasevertexai/api/reference/Protocols/Part#/s:16FirebaseVertexAI4PartPAAE10partsValueSayAaB_pGvp)


  ` Extension method Undocumented

  #### Declaration

  Swift

      var partsValue: [any Part] { get }