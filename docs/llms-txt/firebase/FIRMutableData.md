# Source: https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData.md.txt

# FirebaseDatabase Framework Reference

# FIRMutableData


    @interface FIRMutableData : NSObject

A `MutableData` instance is populated with data from a Firebase Database
location. When you are using `runTransactionBlock(_:)`, you will be given an
instance containing the current data at that location. Your block will be
responsible for updating that instance to the data you wish to save at that
location, and then returning using `TransactionResult.success(withValue:)`.

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
[## Inspecting and navigating the data](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData#/Inspecting-and-navigating-the-data)

- `
  ``
  ``
  `

  ### [-hasChildren](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData#/c:objc(cs)FIRMutableData(im)hasChildren)

  `
  `  
  Returns boolean indicating whether this mutable data has children.  

  #### Declaration

  Objective-C  

      - (BOOL)hasChildren;

  #### Return Value

  YES if this data contains child nodes.
- `
  ``
  ``
  `

  ### [-hasChildAtPath:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData#/c:objc(cs)FIRMutableData(im)hasChildAtPath:)

  `
  `  
  Indicates whether this mutable data has a child at the given path.  

  #### Declaration

  Objective-C  

      - (BOOL)hasChildAtPath:(nonnull NSString *)path;

  #### Parameters

  |--------------|------------------------------------------------------------------------------------------------------------|
  | ` `*path*` ` | A path string, consisting either of a single segment, like 'child', or multiple segments, 'a/deeper/child' |

  #### Return Value

  YES if this data contains a child at the specified relative path
- `
  ``
  ``
  `

  ### [-childDataByAppendingPath:](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData#/c:objc(cs)FIRMutableData(im)childDataByAppendingPath:)

  `
  `  
  Used to obtain a `MutableData` instance that encapsulates the data at the
  given relative path. Note that changes made to the child will be visible to
  the parent.  

  #### Declaration

  Objective-C  

      - (nonnull FIRMutableData *)childDataByAppendingPath:(nonnull NSString *)path;

  #### Parameters

  |--------------|------------------------------------------------------------------------------------------------------------|
  | ` `*path*` ` | A path string, consisting either of a single segment, like 'child', or multiple segments, 'a/deeper/child' |

  #### Return Value

A `MutableData` instance containing the data at the given path  
[## Properties](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData#/Properties)

- `
  ``
  ``
  `

  ### [value](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData#/c:objc(cs)FIRMutableData(py)value)

  `
  `  
  To modify the data contained by this instance of `MutableData`, set this to
  any of the Objective-C types supported by Firebase Database, or any
  equivalent natively bridgeable Swift type:
  - `NSNumber` (includes booleans)
  - `NSDictionary`
  - `NSArray`
  - `NSString`
  - `nil` / `NSNull` to remove the data

  Note that setting this value will override the priority at this location.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, nullable) id value;

  #### Return Value

  The current data at this location as a native object
- `
  ``
  ``
  `

  ### [priority](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData#/c:objc(cs)FIRMutableData(py)priority)

  `
  `  
  Set this property to update the priority of the data at this location. Can be
  set to any of the following Objective-C types supported by Firebase Database,
  or any equivalent natively bridgeable Swift type:
  - `NSNumber` (includes booleans)
  - `NSString`
  - `nil` / `NSNull` to remove the data

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, nullable) id priority;

  #### Return Value

  The priority of the data at this location
- `
  ``
  ``
  `

  ### [childrenCount](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData#/c:objc(cs)FIRMutableData(py)childrenCount)

  `
  `  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSUInteger childrenCount;

  #### Return Value

  The number of child nodes at this location
- `
  ``
  ``
  `

  ### [children](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData#/c:objc(cs)FIRMutableData(py)children)

  `
  `  
  An enumeration of the children at this location.

  for var child in data.children {
  // ...
  }

  Note that this enumerator operates on an immutable copy of the child list.
  So, you can modify the instance during iteration, but the new additions will
  not be visible until you get a new enumerator.  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly) NSEnumerator<FIRMutableData *> *_Nonnull children;

- `
  ``
  ``
  `

  ### [key](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Classes/FIRMutableData#/c:objc(cs)FIRMutableData(py)key)

  `
  `  

  #### Declaration

  Objective-C  

      @property (nonatomic, strong, readonly, nullable) NSString *key;

  #### Return Value

  The key name of this node, or `nil` if it is the top-most location