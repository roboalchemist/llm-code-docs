# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.md.txt

# FirebaseFirestore Framework Reference

# FIRDocumentSnapshot


    @interface FIRDocumentSnapshot : NSObject

A `DocumentSnapshot` contains data read from a document in your Firestore database. The data
can be extracted with the `data` property or by using subscript syntax to access a specific
field.

For a `DocumentSnapshot` that points to a non-existing document, any data access will return
`nil`. You can use the `exists` property to explicitly verify a documents existence.
- `
  ``
  ``
  `

  ### [exists](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(py)exists)

  `
  `  
  True if the document exists.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL exists;

- `
  ``
  ``
  `

  ### [reference](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(py)reference)

  `
  `  
  A `DocumentReference` to the document location.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentReference.html *_Nonnull reference;

- `
  ``
  ``
  `

  ### [documentID](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(py)documentID)

  `
  `  
  The ID of the document for which this `DocumentSnapshot` contains data.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, readonly) NSString *_Nonnull documentID;

- `
  ``
  ``
  `

  ### [metadata](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(py)metadata)

  `
  `  
  Metadata about this snapshot concerning its source and if it has local modifications.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotMetadata.html *_Nonnull metadata;

- `
  ``
  ``
  `

  ### [-data](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(im)data)

  `
  `  
  Retrieves all fields in the document as a `Dictionary`. Returns `nil` if the document doesn't
  exist.

  Server-provided timestamps that have not yet been set to their final value will be returned as
  `NSNull`. You can use the `data(with:)` method to configure this behavior.  

  #### Declaration

  Objective-C  

      - (nullable NSDictionary<NSString *, id> *)data;

  #### Return Value

  A `Dictionary` containing all fields in the document or `nil` if the document doesn't
  exist.
- `
  ``
  ``
  `

  ### [-dataWithServerTimestampBehavior:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(im)dataWithServerTimestampBehavior:)

  `
  `  
  Retrieves all fields in the document as a `Dictionary`. Returns `nil` if the document doesn't
  exist.  

  #### Declaration

  Objective-C  

      - (nullable NSDictionary<NSString *, id> *)dataWithServerTimestampBehavior:
          (https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRServerTimestampBehavior.html)serverTimestampBehavior;

  #### Parameters

  |---------------------------------|------------------------------------------------------------------------------------------------------------------|
  | ` `*serverTimestampBehavior*` ` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot. |

  #### Return Value

  A `Dictionary` containing all fields in the document or `nil` if the document doesn't
  exist.
- `
  ``
  ``
  `

  ### [-valueForField:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(im)valueForField:)

  `
  `  
  Retrieves a specific field from the document. Returns `nil` if the document or the field doesn't
  exist.

  The timestamps that have not yet been set to their final value will be returned as `NSNull`. You
  can use `get(_:serverTimestampBehavior:)` to configure this behavior.  

  #### Declaration

  Objective-C  

      - (nullable id)valueForField:(nonnull id)field;

  #### Parameters

  |---------------|------------------------|
  | ` `*field*` ` | The field to retrieve. |

  #### Return Value

  The value contained in the field or `nil` if the document or field doesn't exist.
- `
  ``
  ``
  `

  ### [-valueForField:serverTimestampBehavior:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(im)valueForField:serverTimestampBehavior:)

  `
  `  
  Retrieves a specific field from the document. Returns `nil` if the document or the field doesn't
  exist.

  The timestamps that have not yet been set to their final value will be returned as `NSNull`. You
  can use `get(_:serverTimestampBehavior:)` to configure this behavior.  

  #### Declaration

  Objective-C  

      - (nullable id)valueForField:(nonnull id)field
           serverTimestampBehavior:
               (https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRServerTimestampBehavior.html)serverTimestampBehavior;

  #### Parameters

  |---------------------------------|------------------------------------------------------------------------------------------------------------------|
  | ` `*field*` `                   | The field to retrieve.                                                                                           |
  | ` `*serverTimestampBehavior*` ` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot. |

  #### Return Value

  The value contained in the field or `nil` if the document or field doesn't exist.
- `
  ``
  ``
  `

  ### [-objectForKeyedSubscript:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot#/c:objc(cs)FIRDocumentSnapshot(im)objectForKeyedSubscript:)

  `
  `  
  Retrieves a specific field from the document.  

  #### Declaration

  Objective-C  

      - (nullable id)objectForKeyedSubscript:(nonnull id)key;

  #### Parameters

  |-------------|------------------------|
  | ` `*key*` ` | The field to retrieve. |

  #### Return Value

  The value contained in the field or `nil` if the document or field doesn't exist.