# Source: https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Extensions/DataSnapshot.md.txt

# FirebaseDatabaseSwift Framework Reference

# DataSnapshot

    public extension DataSnapshot

- `


  ### [data(as:decoder:)](https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Extensions/DataSnapshot#/s:So15FIRDataSnapshotC21FirebaseDatabaseSwiftE4data2as7decoderxxm_0c6SharedE00C11DataDecoderCtKSeRzlF)


  ` Retrieves the value of a snapshot and converts it to an instance of
  caller-specified type.
  Throws `DecodingError.valueNotFound`
  if the document does not exist and `T` is not an `Optional`.

  See `https://firebase.google.com/docs/reference/swift/firebasedatabaseswift/api/reference/Extensions/Database.html#/s:So11FIRDatabaseC21FirebaseDatabaseSwiftE7Decodera` for more details about the decoding process.

  #### Declaration

  Swift

      func data<T: Decodable>(as type: T.Type,
                              decoder: Database.Decoder =
                                Database.Decoder()) throws -> T