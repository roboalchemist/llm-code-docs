# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineSource.md.txt

# FirebaseFirestore Framework Reference

# PipelineSource

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    public struct PipelineSource : @unchecked Sendable

A `PipelineSource` is the entry point for building a Firestore pipeline. It allows you to
specify the source of the data for the pipeline, which can be a collection, a collection group,
a list of documents, or the entire database.
- `


  ### [collection(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineSource#/s:17FirebaseFirestore14PipelineSourceV10collectionyAA0C0VSSF)


  ` Specifies a collection as the data source for the pipeline.

  #### Declaration

  Swift

      public func collection(_ path: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html

  #### Parameters

  |---|---|
  | ` path ` | The path to the collection. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html` with the specified collection as its source.
- `


  ### [collection(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineSource#/s:17FirebaseFirestore14PipelineSourceV10collectionyAA0C0VSo22FIRCollectionReferenceCF)


  ` Specifies a collection as the data source for the pipeline.

  #### Declaration

  Swift

      public func collection(_ coll: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference.html) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html

  #### Parameters

  |---|---|
  | ` coll ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/CollectionReference.html` of the collection. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html` with the specified collection as its source.
- `


  ### [collectionGroup(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineSource#/s:17FirebaseFirestore14PipelineSourceV15collectionGroupyAA0C0VSSF)


  ` Specifies a collection group as the data source for the pipeline.

  #### Declaration

  Swift

      public func collectionGroup(_ collectionId: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html

  #### Parameters

  |---|---|
  | ` collectionId ` | The ID of the collection group. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html` with the specified collection group as its source.
- `


  ### [database()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineSource#/s:17FirebaseFirestore14PipelineSourceV8databaseAA0C0VyF)


  ` Specifies the entire database as the data source for the pipeline.

  #### Declaration

  Swift

      public func database() -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html` with the entire database as its source.
- `


  ### [documents(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineSource#/s:17FirebaseFirestore14PipelineSourceV9documentsyAA0C0VSaySo20FIRDocumentReferenceCGF)


  ` Specifies a list of documents as the data source for the pipeline.

  #### Declaration

  Swift

      public func documents(_ docs: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html

  #### Parameters

  |---|---|
  | ` docs ` | An array of `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html` objects. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html` with the specified documents as its source.
- `


  ### [documents(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineSource#/s:17FirebaseFirestore14PipelineSourceV9documentsyAA0C0VSaySSGF)


  ` Specifies a list of documents as the data source for the pipeline.

  #### Declaration

  Swift

      public func documents(_ paths: [String]) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html

  #### Parameters

  |---|---|
  | ` paths ` | An array of document paths. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html` with the specified documents as its source.
- `


  ### [create(from:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/PipelineSource#/s:17FirebaseFirestore14PipelineSourceV6create4fromAA0C0VSo8FIRQueryC_tF)


  ` Creates a `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html` from an existing `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query.html`.

  This allows you to convert a standard Firestore query into a pipeline, which can then be
  further modified with additional pipeline stages.

  #### Declaration

  Swift

      public func create(from query: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query.html) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html

  #### Parameters

  |---|---|
  | ` query ` | The `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query.html` to convert into a pipeline. |

  #### Return Value

  A `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs/Pipeline.html` that is equivalent to the given query.