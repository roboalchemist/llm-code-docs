# Source: https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Extensions/DatabaseReference.md.txt

# FirebaseDatabaseSwift Framework Reference

# DatabaseReference

    public extension DatabaseReference

- `


  ### [setValue(from:encoder:completion:)](https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Extensions/DatabaseReference#/s:So20FIRDatabaseReferenceC21FirebaseDatabaseSwiftE8setValue4from7encoder10completionyx_0c6SharedE00C11DataEncoderCys5Error_pSgcSgtKSERzlF)


  ` Encodes an instance of `Encodable` and overwrites the encoded data
  to the path referred by this `DatabaseReference`. If no value exists,
  it is created. If a value already exists, it is overwritten.

  See `https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Extensions/Database.html#/s:So11FIRDatabaseC21FirebaseDatabaseSwiftE7Encodera` for more details about the encoding process.

  #### Declaration

  Swift

      func setValue<T: Encodable>(from value: T,
                                  encoder: Database.Encoder = Database.Encoder(),
                                  completion: ((Error?) -> Void)? =
                                    nil) throws

  #### Parameters

  |---|---|
  | ` value ` | An instance of `Encodable` to be encoded to a document. |
  | ` encoder ` | An encoder instance to use to run the encoding. |
  | ` completion ` | A block to execute once the value has been successfully written to the server. This block will not be called while the client is offline, though local changes will be visible immediately. |