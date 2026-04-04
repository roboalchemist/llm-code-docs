# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotListenOptions.md.txt

# FirebaseFirestore Framework Reference

# SnapshotListenOptions

    class SnapshotListenOptions : NSObject, @unchecked Sendable

Options to configure the behavior of `Firestore.addSnapshotListenerWithOptions()`. Instances
of this class control settings like whether metadata-only changes trigger events and the
preferred data source.
- `


  ### [source](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotListenOptions#/c:objc(cs)FIRSnapshotListenOptions(py)source)


  ` The source the snapshot listener retrieves data from.

  #### Declaration

  Swift

      var source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ListenSource.html { get }

- `


  ### [includeMetadataChanges](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotListenOptions#/c:objc(cs)FIRSnapshotListenOptions(py)includeMetadataChanges)


  ` Indicates whether metadata-only changes should trigger snapshot events.

  #### Declaration

  Swift

      var includeMetadataChanges: Bool { get }

- `


  ### [init()](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotListenOptions#/c:objc(cs)FIRSnapshotListenOptions(im)init)


  ` Creates and returns a new `SnapshotListenOptions` object with all properties initialized to their
  default values.

  #### Declaration

  Swift

      init()

  #### Return Value

  The created `SnapshotListenOptions` object.
- `


  ### [withIncludeMetadataChanges(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotListenOptions#/c:objc(cs)FIRSnapshotListenOptions(im)optionsWithIncludeMetadataChanges:)


  ` Creates and returns a new `SnapshotListenOptions` object with all properties of the current
  `SnapshotListenOptions` object plus the new property specifying whether metadata-only changes
  should trigger snapshot events

  #### Declaration

  Swift

      func withIncludeMetadataChanges(_ includeMetadataChanges: Bool) -> SnapshotListenOptions

  #### Return Value

  The created `SnapshotListenOptions` object.
- `


  ### [withSource(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/SnapshotListenOptions#/c:objc(cs)FIRSnapshotListenOptions(im)optionsWithSource:)


  ` Creates and returns a new `SnapshotListenOptions` object with all properties of the current
  `SnapshotListenOptions` object plus the new property specifying the source that the snapshot
  listener listens to.

  #### Declaration

  Swift

      func withSource(_ source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Enums/ListenSource.html) -> SnapshotListenOptions

  #### Return Value

  The created `SnapshotListenOptions` object.