# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQueryDocumentSnapshot.md.txt

# FirebaseFirestore Framework Reference

# FIRQueryDocumentSnapshot


    @interface FIRQueryDocumentSnapshot : https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRDocumentSnapshot.html

A `QueryDocumentSnapshot` contains data read from a document in your Firestore database as
part of a query. The document is guaranteed to exist and its data can be extracted with the
`data` property or by using subscript syntax to access a specific field.

A `QueryDocumentSnapshot` offers the same API surface as a `DocumentSnapshot`. As
deleted documents are not returned from queries, its `exists` property will always be true and
`data()` will never return `nil`.
- `
  ``
  ``
  `

  ### [-data](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQueryDocumentSnapshot#/c:objc(cs)FIRQueryDocumentSnapshot(im)data)

  `
  `  
  Retrieves all fields in the document as a `Dictionary`.

  Server-provided timestamps that have not yet been set to their final value will be returned as
  `NSNull`. You can use the `data(with:)` method to configure this behavior.  

  #### Declaration

  Objective-C  

      - (nonnull NSDictionary<NSString *, id> *)data;

  #### Return Value

  A `Dictionary` containing all fields in the document.
- `
  ``
  ``
  `

  ### [-dataWithServerTimestampBehavior:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRQueryDocumentSnapshot#/c:objc(cs)FIRQueryDocumentSnapshot(im)dataWithServerTimestampBehavior:)

  `
  `  
  Retrieves all fields in the document as a `Dictionary`.  

  #### Declaration

  Objective-C  

      - (nonnull NSDictionary<NSString *, id> *)dataWithServerTimestampBehavior:
          (https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRServerTimestampBehavior.html)serverTimestampBehavior;

  #### Parameters

  |---------------------------------|------------------------------------------------------------------------------------------------------------------|
  | ` `*serverTimestampBehavior*` ` | Configures how server timestamps that have not yet been set to their final value are returned from the snapshot. |

  #### Return Value

  A `Dictionary` containing all fields in the document.