# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRListenSource.md.txt

# FirebaseFirestore Framework Reference

# FIRListenSource

    enum FIRListenSource : NSUInteger {}

The source the snapshot listener retrieves data from.
- `
  ``
  ``
  `

  ### [FIRListenSourceDefault](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRListenSource#/c:@E@FIRListenSource@FIRListenSourceDefault)

  `
  `  
  The default behavior. The listener attempts to return initial snapshot from cache and retrieve
  up-to-date snapshots from the Firestore server. Snapshot events will be triggered on local
  mutations and server-side updates.  

  #### Declaration

  Objective-C  

      FIRListenSourceDefault

- `
  ``
  ``
  `

  ### [FIRListenSourceCache](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRListenSource#/c:@E@FIRListenSource@FIRListenSourceCache)

  `
  `  
  The listener retrieves data and listens to updates from the local Firestore cache without
  attempting to send the query to the server. If some documents gets updated as a result from
  other queries, they will be picked up by listeners using the cache.

  Note that the data might be stale if the cache hasn't synchronized with recent server-side
  changes.  

  #### Declaration

  Objective-C  

      FIRListenSourceCache