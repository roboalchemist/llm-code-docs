# Source: https://firebase.google.com/docs/reference/kotlin/com/google/firebase/firestore/ListenSource.md.txt

# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/firestore/ListenSource.md.txt

# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ListenSource.md.txt

# FirebaseFirestore Framework Reference

# ListenSource

    enum ListenSource : UInt, @unchecked Sendable

The source the snapshot listener retrieves data from.
- `
  ``
  ``
  `

  ### [default](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ListenSource#/c:@E@FIRListenSource@FIRListenSourceDefault)

  `
  `  
  The default behavior. The listener attempts to return initial snapshot from cache and retrieve
  up-to-date snapshots from the Firestore server. Snapshot events will be triggered on local
  mutations and server-side updates.  

  #### Declaration

  Swift  

      case `default` = 0

- `
  ``
  ``
  `

  ### [cache](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ListenSource#/c:@E@FIRListenSource@FIRListenSourceCache)

  `
  `  
  The listener retrieves data and listens to updates from the local Firestore cache without
  attempting to send the query to the server. If some documents gets updated as a result from
  other queries, they will be picked up by listeners using the cache.

  Note that the data might be stale if the cache hasn't synchronized with recent server-side
  changes.  

  #### Declaration

  Swift  

      case cache = 1