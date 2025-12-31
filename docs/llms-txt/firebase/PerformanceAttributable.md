# Source: https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Protocols/PerformanceAttributable.md.txt

# FirebasePerformance Framework Reference

# PerformanceAttributable

    protocol PerformanceAttributable : NSObjectProtocol

Defines the interface that allows adding/removing attributes to any object.
- `
  ``
  ``
  `

  ### [attributes](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Protocols/PerformanceAttributable#/c:objc(pl)FIRPerformanceAttributable(py)attributes)

  `
  `  
  List of attributes.  

  #### Declaration

  Swift  

      var attributes: [String : String] { get }

- `
  ``
  ``
  `

  ### [setValue(_:forAttribute:)](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Protocols/PerformanceAttributable#/c:objc(pl)FIRPerformanceAttributable(im)setValue:forAttribute:)

  `
  `  
  Sets a value as a string for the specified attribute. Updates the value of the attribute if a
  value had already existed.  

  #### Declaration

  Swift  

      func setValue(_ value: String, forAttribute attribute: String)

  #### Parameters

  |-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*value*` `     | The value that needs to be set/updated for an attribute. If the length of the value exceeds the maximum allowed, the value will be truncated to the maximum allowed. |
  | ` `*attribute*` ` | The name of the attribute. If the length of the value exceeds the maximum allowed, the value will be truncated to the maximum allowed.                               |

- `
  ``
  ``
  `

  ### [value(forAttribute:)](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Protocols/PerformanceAttributable#/c:objc(pl)FIRPerformanceAttributable(im)valueForAttribute:)

  `
  `  
  Reads the value for the specified attribute. If the attribute does not exist, returns nil.  

  #### Declaration

  Swift  

      func value(forAttribute attribute: String) -> String?

  #### Parameters

  |-------------------|----------------------------|
  | ` `*attribute*` ` | The name of the attribute. |

  #### Return Value

  The value for the attribute. Returns nil if the attribute does not exist.
- `
  ``
  ``
  `

  ### [removeAttribute(_:)](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Protocols/PerformanceAttributable#/c:objc(pl)FIRPerformanceAttributable(im)removeAttribute:)

  `
  `  
  Removes an attribute from the list. Does nothing if the attribute does not exist.  

  #### Declaration

  Swift  

      func removeAttribute(_ attribute: String)

  #### Parameters

  |-------------------|----------------------------|
  | ` `*attribute*` ` | The name of the attribute. |