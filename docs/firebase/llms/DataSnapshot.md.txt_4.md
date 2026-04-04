# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot.md.txt

# FirebaseDatabase Framework Reference

# DataSnapshot

    class DataSnapshot : NSObject, @unchecked Sendable

A DataSnapshot contains data from a Firebase Database location. Any time
you read Firebase data, you receive the data as a DataSnapshot.

DataSnapshots are passed to the blocks you attach with
`observe(_:with:)` or `observeSingleEvent(of:with:)`. They are
efficiently-generated immutable copies of the data at a Firebase Database
location. They can't be modified and will never change. To modify data at a
location, use a DatabaseReference (e.g. with `setValue(_:)`).
[## Navigating and inspecting a snapshot](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/Navigating-and-inspecting-a-snapshot)

- `


  ### [childSnapshot(forPath:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(im)childSnapshotForPath:)


  ` Gets a DataSnapshot for the location at the specified relative path.
  The relative path can either be a simple child key (e.g. 'fred')
  or a deeper slash-separated path (e.g. 'fred/name/first'). If the child
  location has no data, an empty DataSnapshot is returned.

  #### Declaration

  Swift

      func childSnapshot(forPath childPathString: String) -> DataSnapshot

  #### Parameters

  |---|---|
  | ` childPathString ` | A relative path to the location of child data. |

  #### Return Value

  The DataSnapshot for the child location.
- `


  ### [hasChild(_:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(im)hasChild:)


  ` Return true if the specified child exists.

  #### Declaration

  Swift

      func hasChild(_ childPathString: String) -> Bool

  #### Parameters

  |---|---|
  | ` childPathString ` | A relative path to the location of a potential child. |

  #### Return Value

  true if data exists at the specified childPathString, else false.
- `


  ### [hasChildren()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(im)hasChildren)


  ` Return true if the DataSnapshot has any children.

  #### Declaration

  Swift

      func hasChildren() -> Bool

  #### Return Value

  true if this snapshot has any children, else false.
- `


  ### [exists()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(im)exists)


  ` Return true if the DataSnapshot contains a non-null value.

  #### Declaration

  Swift

      func exists() -> Bool

  #### Return Value

  true if this snapshot contains a non-null value, else false.
[## Data export](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/Data-export)

- `


  ### [valueInExportFormat()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(im)valueInExportFormat)


  ` Returns the raw value at this location, coupled with any metadata, such as
  priority.

  Priorities, where they exist, are accessible under the ".priority" key in
  instances of NSDictionary. For leaf locations with priorities, the value will
  be under the ".value" key.

  #### Declaration

  Swift

      func valueInExportFormat() -> Any?

[## Properties](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/Properties)

- `


  ### [value](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(py)value)


  ` Returns the contents of this data snapshot as native types.

  Data types returned:
  - `Dictionary`
  - `Array`
  - `NSNumber`-bridgeable types, including `Bool`
  - `String`

  #### Declaration

  Swift

      var value: Any? { get }

  #### Return Value

  The data as a native object.
- `


  ### [childrenCount](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(py)childrenCount)


  ` Gets the number of children for this DataSnapshot.

  #### Declaration

  Swift

      var childrenCount: UInt { get }

  #### Return Value

  An integer indicating the number of children.
- `


  ### [ref](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(py)ref)


  ` Gets a DatabaseReference for the location that this data came from.

  #### Declaration

  Swift

      var ref: FIRDatabaseReference { get }

  #### Return Value

  A DatabaseReference instance for the location of this data.
- `


  ### [key](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(py)key)


  ` The key of the location that generated this DataSnapshot.

  #### Declaration

  Swift

      var key: String { get }

  #### Return Value

  A `String` containing the key for the location of this
  DataSnapshot.
- `


  ### [children](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(py)children)


  ` An iterator for snapshots of the child nodes in this snapshot.

       for var child in snapshot.children {
         // ...
       }

  #### Declaration

  Swift

      var children: NSEnumerator { get }

  #### Return Value

  An NSEnumerator of the children.
- `


  ### [priority](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/c:objc(cs)FIRDataSnapshot(py)priority)


  ` The priority of the data in this DataSnapshot.

  #### Declaration

  Swift

      var priority: Any? { get }

  #### Return Value

  The priority as a `String`, or `nil` if no priority was set.
- `


  ### [data(as:decoder:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/DataSnapshot#/s:So15FIRDataSnapshotC16FirebaseDatabaseE4data2as7decoderxxm_0C11SharedSwift0C11DataDecoderCtKSeRzlF)


  ` Retrieves the value of a snapshot and converts it to an instance of
  caller-specified type.
  Throws `DecodingError.valueNotFound`
  if the document does not exist and `T` is not an `Optional`.

  See `https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database.html#/s:So11FIRDatabaseC16FirebaseDatabaseE7Decodera` for more details about the decoding process.

  #### Declaration

  Swift

      func data<T: Decodable>(as type: T.Type,
                              decoder: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database.html.Decoder =
                                https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/Database.html.Decoder()) throws -> T