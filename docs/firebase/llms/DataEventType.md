# Source: https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType.md.txt

# FirebaseDatabase Framework Reference

# DataEventType

    enum DataEventType : Int, @unchecked Sendable

This enum is the set of events that you can observe at a Firebase Database
location.
- `
  ``
  ``
  `

  ### [childAdded](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType#/c:@E@FIRDataEventType@FIRDataEventTypeChildAdded)

  `
  `  
  A new child node is added to a location.  

  #### Declaration

  Swift  

      case childAdded = 0

- `
  ``
  ``
  `

  ### [childRemoved](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType#/c:@E@FIRDataEventType@FIRDataEventTypeChildRemoved)

  `
  `  
  A child node is removed from a location.  

  #### Declaration

  Swift  

      case childRemoved = 1

- `
  ``
  ``
  `

  ### [childChanged](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType#/c:@E@FIRDataEventType@FIRDataEventTypeChildChanged)

  `
  `  
  A child node at a location changes.  

  #### Declaration

  Swift  

      case childChanged = 2

- `
  ``
  ``
  `

  ### [childMoved](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType#/c:@E@FIRDataEventType@FIRDataEventTypeChildMoved)

  `
  `  
  A child node moves relative to the other child nodes at a location.  

  #### Declaration

  Swift  

      case childMoved = 3

- `
  ``
  ``
  `

  ### [value](https://firebase.google.com/docs/reference/swift/firebasedatabase/api/reference/Enums/DataEventType#/c:@E@FIRDataEventType@FIRDataEventTypeValue)

  `
  `  
  Any data changes at a location or, recursively, at any child node.  

  #### Declaration

  Swift  

      case value = 4