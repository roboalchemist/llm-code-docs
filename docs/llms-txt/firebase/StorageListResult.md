# Source: https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult.md.txt

# FirebaseStorage Framework Reference

# StorageListResult

    @available(iOS 13, tvOS 13, macOS 10.15, watchOS 7, *)
    @objc(FIRStorageListResult)
    open class StorageListResult : NSObject

Contains the prefixes and items returned by a `StorageReference.list()` call.
- `
  ``
  ``
  `

  ### [prefixes](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult#/c:@M@FirebaseStorage@objc(cs)FIRStorageListResult(py)prefixes)

  `
  `  
  The prefixes (folders) returned by a `list()` operation.  

  #### Declaration

  Swift  

      @objc
      public let prefixes: [https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html]

- `
  ``
  ``
  `

  ### [items](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult#/c:@M@FirebaseStorage@objc(cs)FIRStorageListResult(py)items)

  `
  `  
  The objects (files) returned by a `list()` operation.  

  #### Declaration

  Swift  

      @objc
      public let items: [https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageReference.html]

- `
  ``
  ``
  `

  ### [pageToken](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult#/c:@M@FirebaseStorage@objc(cs)FIRStorageListResult(py)pageToken)

  `
  `  
  A token that can be used to resume a previous `list()` operation. `nil`
  indicates that there are no more results.  

  #### Declaration

  Swift  

      @objc
      public let pageToken: String?

[## NSObject overrides](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult#/NSObject-overrides)

- `
  ``
  ``
  `

  ### [copy()](https://firebase.google.com/docs/reference/swift/firebasestorage/api/reference/Classes/StorageListResult#/c:@M@FirebaseStorage@objc(cs)FIRStorageListResult(im)copy)

  `
  `  
  Undocumented  

  #### Declaration

  Swift  

      override open func copy() -> Any