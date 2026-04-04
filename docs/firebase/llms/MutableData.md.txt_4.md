# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData.md.txt

# FirebaseDatabase Framework Reference

# MutableData

    class MutableData : NSObject

A `MutableData` instance is populated with data from a Firebase Database
location. When you are using `runTransactionBlock(_:)`, you will be given an
instance containing the current data at that location. Your block will be
responsible for updating that instance to the data you wish to save at that
location, and then returning using `https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/TransactionResult.html#/c:objc(cs)FIRTransactionResult(cm)successWithValue:`.

To modify the data, set its value property to any of the Objective-C types
supported by Firebase Database, or any equivalent natively bridgeable Swift
type:

- `NSNumber` (includes booleans)
- `NSDictionary`
- `NSArray`
- `NSString`
- `nil` / `NSNull` to remove the data

Note that changes made to a child `MutableData` instance will be visible to
the parent.
[## Inspecting and navigating the data](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData#/Inspecting-and-navigating-the-data)

- `


  ### [hasChildren()](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData#/c:objc(cs)FIRMutableData(im)hasChildren)


  ` Returns boolean indicating whether this mutable data has children.

  #### Declaration

  Swift

      func hasChildren() -> Bool

  #### Return Value

  YES if this data contains child nodes.
- `


  ### [hasChild(atPath:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData#/c:objc(cs)FIRMutableData(im)hasChildAtPath:)


  ` Indicates whether this mutable data has a child at the given path.

  #### Declaration

  Swift

      func hasChild(atPath path: String) -> Bool

  #### Parameters

  |---|---|
  | ` path ` | A path string, consisting either of a single segment, like 'child', or multiple segments, 'a/deeper/child' |

  #### Return Value

  YES if this data contains a child at the specified relative path
- `


  ### [childData(byAppendingPath:)](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData#/c:objc(cs)FIRMutableData(im)childDataByAppendingPath:)


  ` Used to obtain a `MutableData` instance that encapsulates the data at the
  given relative path. Note that changes made to the child will be visible to
  the parent.

  #### Declaration

  Swift

      func childData(byAppendingPath path: String) -> MutableData

  #### Parameters

  |---|---|
  | ` path ` | A path string, consisting either of a single segment, like 'child', or multiple segments, 'a/deeper/child' |

  #### Return Value

  A `MutableData` instance containing the data at the given path
[## Properties](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData#/Properties)

- `


  ### [value](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData#/c:objc(cs)FIRMutableData(py)value)


  ` To modify the data contained by this instance of `MutableData`, set this to
  any of the Objective-C types supported by Firebase Database, or any
  equivalent natively bridgeable Swift type:
  - `NSNumber` (includes booleans)
  - `NSDictionary`
  - `NSArray`
  - `NSString`
  - `nil` / `NSNull` to remove the data

  Note that setting this value will override the priority at this location.

  #### Declaration

  Swift

      var value: Any? { get set }

  #### Return Value

  The current data at this location as a native object
- `


  ### [priority](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData#/c:objc(cs)FIRMutableData(py)priority)


  ` Set this property to update the priority of the data at this location. Can be
  set to any of the following Objective-C types supported by Firebase Database,
  or any equivalent natively bridgeable Swift type:
  - `NSNumber` (includes booleans)
  - `NSString`
  - `nil` / `NSNull` to remove the data

  #### Declaration

  Swift

      var priority: Any? { get set }

  #### Return Value

  The priority of the data at this location
- `


  ### [childrenCount](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData#/c:objc(cs)FIRMutableData(py)childrenCount)


  `

  #### Declaration

  Swift

      var childrenCount: UInt { get }

  #### Return Value

  The number of child nodes at this location
- `


  ### [children](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData#/c:objc(cs)FIRMutableData(py)children)


  ` An enumeration of the children at this location.

  for var child in data.children {
  // ...
  }

  Note that this enumerator operates on an immutable copy of the child list.
  So, you can modify the instance during iteration, but the new additions will
  not be visible until you get a new enumerator.

  #### Declaration

  Swift

      var children: NSEnumerator { get }

- `


  ### [key](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Classes/MutableData#/c:objc(cs)FIRMutableData(py)key)


  `

  #### Declaration

  Swift

      var key: String? { get }

  #### Return Value

  The key name of this node, or `nil` if it is the top-most location