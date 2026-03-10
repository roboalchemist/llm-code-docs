# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult.md.txt

# FirebaseFirestore Framework Reference

# PipelineResult

    public struct PipelineResult : @unchecked Sendable

Undocumented
- `


  ### [ref](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult#/s:17FirebaseFirestore14PipelineResultV3refSo20FIRDocumentReferenceCSgvp)


  ` The reference of the document, if the query returns the `__name__` field.

  #### Declaration

  Swift

      public let ref: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html?

- `


  ### [id](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult#/s:17FirebaseFirestore14PipelineResultV2idSSSgvp)


  ` The ID of the document for which this `PipelineResult` contains data, if available.

  #### Declaration

  Swift

      public let id: String?

- `


  ### [createTime](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult#/s:17FirebaseFirestore14PipelineResultV10createTimeSo12FIRTimestampCSgvp)


  ` The time the document was created, if available.

  #### Declaration

  Swift

      public let createTime: Timestamp?

- `


  ### [updateTime](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult#/s:17FirebaseFirestore14PipelineResultV10updateTimeSo12FIRTimestampCSgvp)


  ` The time the document was last updated when the snapshot was generated.

  #### Declaration

  Swift

      public let updateTime: Timestamp?

- `


  ### [data](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult#/s:17FirebaseFirestore14PipelineResultV4dataSDySSs8Sendable_pSgGvp)


  ` Retrieves all fields in the result as a dictionary.

  #### Declaration

  Swift

      public let data: [String : Sendable?]

- `


  ### [get(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult#/s:17FirebaseFirestore14PipelineResultV3getys8Sendable_pSgSSF)


  ` Retrieves the field specified by `fieldPath`.

  #### Declaration

  Swift

      public func get(_ fieldName: String) -> Sendable?

  #### Parameters

  |---|---|
  | ` fieldPath ` | The field path (e.g., "foo" or "foo.bar"). |

  #### Return Value

  The data at the specified field location or `nil` if no such field exists.
- `


  ### [get(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult#/s:17FirebaseFirestore14PipelineResultV3getys8Sendable_pSgSo12FIRFieldPathCF)


  ` Retrieves the field specified by `fieldPath`.

  #### Declaration

  Swift

      public func get(_ fieldPath: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/FieldPath.html) -> Sendable?

  #### Parameters

  |---|---|
  | ` fieldPath ` | The field path (e.g., "foo" or "foo.bar"). |

  #### Return Value

  The data at the specified field location or `nil` if no such field exists.
- `


  ### [get(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineResult#/s:17FirebaseFirestore14PipelineResultV3getys8Sendable_pSgAA5FieldVF)


  ` Retrieves the field specified by `fieldPath`.

  #### Declaration

  Swift

      public func get(_ field: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Field.html) -> Sendable?

  #### Parameters

  |---|---|
  | ` fieldPath ` | The field path (e.g., "foo" or "foo.bar"). |

  #### Return Value

  The data at the specified field location or `nil` if no such field exists.