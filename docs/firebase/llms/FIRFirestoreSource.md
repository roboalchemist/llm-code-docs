# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreSource.md.txt

# FirebaseFirestore Framework Reference

# FIRFirestoreSource

    enum FIRFirestoreSource : NSUInteger {}

An enum that configures the behavior of `DocumentReference.getDocument()` and
`Query.getDocuments()`. By providing a source enum the `getDocument[s]`
methods can be configured to fetch results only from the server, only from
the local cache, or attempt to fetch results from the server and fall back to
the cache (which is the default).
- `
  ``
  ``
  `

  ### [FIRFirestoreSourceDefault](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreSource#/c:@E@FIRFirestoreSource@FIRFirestoreSourceDefault)

  `
  `  
  Causes Firestore to try to retrieve an up-to-date (server-retrieved)
  snapshot, but fall back to returning cached data if the server can't be
  reached.  

  #### Declaration

  Objective-C  

      FIRFirestoreSourceDefault

- `
  ``
  ``
  `

  ### [FIRFirestoreSourceServer](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreSource#/c:@E@FIRFirestoreSource@FIRFirestoreSourceServer)

  `
  `  
  Causes Firestore to avoid the cache, generating an error if the server
  cannot be reached. Note that the cache will still be updated if the
  server request succeeds. Also note that latency-compensation still takes
  effect, so any pending write operations will be visible in the returned
  data (merged into the server-provided data).  

  #### Declaration

  Objective-C  

      FIRFirestoreSourceServer

- `
  ``
  ``
  `

  ### [FIRFirestoreSourceCache](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRFirestoreSource#/c:@E@FIRFirestoreSource@FIRFirestoreSourceCache)

  `
  `  
  Causes Firestore to immediately return a value from the cache, ignoring
  the server completely (implying that the returned value may be stale with
  respect to the value on the server). If there is no data in the cache to
  satisfy the `getDocument[s]` call, `DocumentReference.getDocument()` will
  return an error and `QuerySnapshot.getDocuments()` will return an empty
  `QuerySnapshot` with no documents.  

  #### Declaration

  Objective-C  

      FIRFirestoreSourceCache