# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreSource.md.txt

# FirebaseFirestore Framework Reference

# FirestoreSource

    enum FirestoreSource : UInt, @unchecked Sendable

An enum that configures the behavior of [DocumentReference.getDocument()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html#/c:objc(cs)FIRDocumentReference(im)getDocumentWithCompletion:) and
[Query.getDocuments()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/Query.html#/c:objc(cs)FIRQuery(im)getDocumentsWithCompletion:). By providing a source enum the `getDocument[s]`
methods can be configured to fetch results only from the server, only from
the local cache, or attempt to fetch results from the server and fall back to
the cache (which is the default).
- `
  ``
  ``
  `

  ### [default](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreSource#/c:@E@FIRFirestoreSource@FIRFirestoreSourceDefault)

  `
  `  
  Causes Firestore to try to retrieve an up-to-date (server-retrieved)
  snapshot, but fall back to returning cached data if the server can't be
  reached.  

  #### Declaration

  Swift  

      case `default` = 0

- `
  ``
  ``
  `

  ### [server](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreSource#/c:@E@FIRFirestoreSource@FIRFirestoreSourceServer)

  `
  `  
  Causes Firestore to avoid the cache, generating an error if the server
  cannot be reached. Note that the cache will still be updated if the
  server request succeeds. Also note that latency-compensation still takes
  effect, so any pending write operations will be visible in the returned
  data (merged into the server-provided data).  

  #### Declaration

  Swift  

      case server = 1

- `
  ``
  ``
  `

  ### [cache](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/FirestoreSource#/c:@E@FIRFirestoreSource@FIRFirestoreSourceCache)

  `
  `  
  Causes Firestore to immediately return a value from the cache, ignoring
  the server completely (implying that the returned value may be stale with
  respect to the value on the server). If there is no data in the cache to
  satisfy the `getDocument[s]` call, [DocumentReference.getDocument()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/DocumentReference.html#/c:objc(cs)FIRDocumentReference(im)getDocumentWithCompletion:) will
  return an error and `QuerySnapshot.getDocuments()` will return an empty
  [QuerySnapshot](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/QuerySnapshot.html) with no documents.  

  #### Declaration

  Swift  

      case cache = 2