# Source: https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot.md.txt

# FirebaseDatabase Framework Reference

# FIRDataSnapshot


    @interface FIRDataSnapshot : NSObject

A DataSnapshot contains data from a Firebase Database location. Any time
you read Firebase data, you receive the data as a DataSnapshot.

DataSnapshots are passed to the blocks you attach with
`observe(_:with:)` or `observeSingleEvent(of:with:)`. They are
efficiently-generated immutable copies of the data at a Firebase Database
location. They can't be modified and will never change. To modify data at a
location, use a DatabaseReference (e.g. with `setValue(_:)`).
[## Navigating and inspecting a snapshot](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/Navigating-and-inspecting-a-snapshot)

- `
  ``
  ``
  `

  ### [-childSnapshotForPath:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(im)childSnapshotForPath:)

  `
  `  
  Gets a DataSnapshot for the location at the specified relative path.
  The relative path can either be a simple child key (e.g. 'fred')
  or a deeper slash-separated path (e.g. 'fred/name/first'). If the child
  location has no data, an empty DataSnapshot is returned.  

  #### Declaration

  Objective-C  

      - (nonnull FIRDataSnapshot *)childSnapshotForPath:
          (nonnull NSString *)childPathString;

  #### Parameters

  |-------------------------|------------------------------------------------|
  | ` `*childPathString*` ` | A relative path to the location of child data. |

  #### Return Value

  The DataSnapshot for the child location.
- `
  ``
  ``
  `

  ### [-hasChild:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(im)hasChild:)

  `
  `  
  Return true if the specified child exists.  

  #### Declaration

  Objective-C  

      - (BOOL)hasChild:(nonnull NSString *)childPathString;

  #### Parameters

  |-------------------------|-------------------------------------------------------|
  | ` `*childPathString*` ` | A relative path to the location of a potential child. |

  #### Return Value

  true if data exists at the specified childPathString, else false.
- `
  ``
  ``
  `

  ### [-hasChildren](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(im)hasChildren)

  `
  `  
  Return true if the DataSnapshot has any children.  

  #### Declaration

  Objective-C  

      - (BOOL)hasChildren;

  #### Return Value

  true if this snapshot has any children, else false.
- `
  ``
  ``
  `

  ### [-exists](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(im)exists)

  `
  `  
  Return true if the DataSnapshot contains a non-null value.  

  #### Declaration

  Objective-C  

      - (BOOL)exists;

  #### Return Value

true if this snapshot contains a non-null value, else false.  
[## Data export](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/Data-export)

- `
  ``
  ``
  `

  ### [-valueInExportFormat](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(im)valueInExportFormat)

  `
  `  
  Returns the raw value at this location, coupled with any metadata, such as
  priority.

  Priorities, where they exist, are accessible under the ".priority" key in
  instances of NSDictionary. For leaf locations with priorities, the value will
  be under the ".value" key.  

  #### Declaration

  Objective-C  

      - (id _Nullable)valueInExportFormat;

[## Properties](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/Properties)

- `
  ``
  ``
  `

  ### [value](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(py)value)

  `
  `  
  Returns the contents of this data snapshot as native types.

  Data types returned:
  - `Dictionary`
  - `Array`
  - `NSNumber`-bridgeable types, including `Bool`
  - `String`

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly, nullable) id value;

  #### Return Value

  The data as a native object.
- `
  ``
  ``
  `

  ### [childrenCount](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(py)childrenCount)

  `
  `  
  Gets the number of children for this DataSnapshot.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSUInteger childrenCount;

  #### Return Value

  An integer indicating the number of children.
- `
  ``
  ``
  `

  ### [ref](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(py)ref)

  `
  `  
  Gets a DatabaseReference for the location that this data came from.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDatabaseReference.html *_Nonnull ref;

  #### Return Value

  A DatabaseReference instance for the location of this data.
- `
  ``
  ``
  `

  ### [key](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(py)key)

  `
  `  
  The key of the location that generated this DataSnapshot.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSString *_Nonnull key;

  #### Return Value

  A `String` containing the key for the location of this
  DataSnapshot.
- `
  ``
  ``
  `

  ### [children](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(py)children)

  `
  `  
  An iterator for snapshots of the child nodes in this snapshot.  

       for var child in snapshot.children {
         // ...
       }

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSEnumerator<FIRDataSnapshot *> *_Nonnull children;

  #### Return Value

  An NSEnumerator of the children.
- `
  ``
  ``
  `

  ### [priority](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRDataSnapshot#/c:objc(cs)FIRDataSnapshot(py)priority)

  `
  `  
  The priority of the data in this DataSnapshot.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly, nullable) id priority;

  #### Return Value

  The priority as a `String`, or `nil` if no priority was set.