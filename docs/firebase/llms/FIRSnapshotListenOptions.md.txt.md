# Source: https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotListenOptions.md.txt

# FirebaseFirestore Framework Reference

# FIRSnapshotListenOptions


    @interface FIRSnapshotListenOptions : NSObject

Options to configure the behavior of `Firestore.addSnapshotListenerWithOptions()`. Instances
of this class control settings like whether metadata-only changes trigger events and the
preferred data source.
- `


  ### [source](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotListenOptions#/c:objc(cs)FIRSnapshotListenOptions(py)source)


  ` The source the snapshot listener retrieves data from.

  #### Declaration

  Objective-C

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRListenSource.html source;

- `


  ### [includeMetadataChanges](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotListenOptions#/c:objc(cs)FIRSnapshotListenOptions(py)includeMetadataChanges)


  ` Indicates whether metadata-only changes should trigger snapshot events.

  #### Declaration

  Objective-C

      @property (nonatomic, readonly) BOOL includeMetadataChanges;

- `


  ### [-init](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotListenOptions#/c:objc(cs)FIRSnapshotListenOptions(im)init)


  ` Creates and returns a new `SnapshotListenOptions` object with all properties initialized to their
  default values.

  #### Declaration

  Objective-C

      - (nonnull instancetype)init;

  #### Return Value

  The created `SnapshotListenOptions` object.
- `


  ### [-optionsWithIncludeMetadataChanges:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotListenOptions#/c:objc(cs)FIRSnapshotListenOptions(im)optionsWithIncludeMetadataChanges:)


  ` Creates and returns a new `SnapshotListenOptions` object with all properties of the current
  `SnapshotListenOptions` object plus the new property specifying whether metadata-only changes
  should trigger snapshot events

  #### Declaration

  Objective-C

      - (nonnull FIRSnapshotListenOptions *)optionsWithIncludeMetadataChanges:
          (BOOL)includeMetadataChanges;

  #### Return Value

  The created `SnapshotListenOptions` object.
- `


  ### [-optionsWithSource:](https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Classes/FIRSnapshotListenOptions#/c:objc(cs)FIRSnapshotListenOptions(im)optionsWithSource:)


  ` Creates and returns a new `SnapshotListenOptions` object with all properties of the current
  `SnapshotListenOptions` object plus the new property specifying the source that the snapshot
  listener listens to.

  #### Declaration

  Objective-C

      - (nonnull FIRSnapshotListenOptions *)optionsWithSource:(https://firebase.google.com/docs/reference/ios/firebasefirestore/api/reference/Enums/FIRListenSource.html)source;

  #### Return Value

  The created `SnapshotListenOptions` object.