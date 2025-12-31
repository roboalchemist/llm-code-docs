# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryLRUGCSettings.md.txt

# FirebaseFirestore Framework Reference

# MemoryLRUGCSettings

    class MemoryLRUGCSettings : NSObject, NSCopying, https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols.html#/c:objc(pl)FIRMemoryGarbageCollectorSettings

Configures the SDK to use a least-recently-used garbage collector for memory cache.

Once configured, the SDK will attempt to remove documents that are least recently used in
batches, if the current cache size is larger than the given target cache size. Default cache size
is 100MB.

To use, create an instance using one of the initializers, then initialize
[MemoryCacheSettings](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryCacheSettings.html) with this instance.
- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryLRUGCSettings#/c:objc(cs)FIRMemoryLRUGCSettings(im)init)

  `
  `  
  Creates an instance of `FIRMemoryLRUGCSettings`, with default target cache size 100MB. The SDK
  will run garbage collection if the current cache size is larger than 100MB.  

  #### Declaration

  Swift  

      init()

- `
  ``
  ``
  `

  ### [init(sizeBytes:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/MemoryLRUGCSettings#/c:objc(cs)FIRMemoryLRUGCSettings(im)initWithSizeBytes:)

  `
  `  
  Creates an instance of `FIRMemoryLRUGCSettings`, with a custom target cache size. The SDK will
  run garbage collection if the current cache size is larger than the given size.  

  #### Declaration

  Swift  

      init(sizeBytes size: NSNumber)