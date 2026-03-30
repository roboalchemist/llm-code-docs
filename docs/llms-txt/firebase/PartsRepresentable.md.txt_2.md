# Source: https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/PartsRepresentable.md.txt

# FirebaseAILogic Framework Reference

# PartsRepresentable

    @available(iOS 15.0, macOS 12.0, tvOS 15.0, watchOS 8.0, *)
    public protocol PartsRepresentable

A protocol describing any data that could be serialized to model-interpretable input data,
where the serialization process cannot fail with an error.
- `


  ### [partsValue](https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/PartsRepresentable#/s:15FirebaseAILogic18PartsRepresentableP10partsValueSayAA4Part_pGvp)


  ` Undocumented

  #### Declaration

  Swift

      var partsValue: [any https://firebase.google.com/docs/reference/swift/firebaseailogic/api/reference/Protocols/Part.html] { get }