# Source: https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Enums/FIRDataEventType.md.txt

# FirebaseDatabase Framework Reference

# FIRDataEventType

    enum FIRDataEventType : NSInteger {}

This enum is the set of events that you can observe at a Firebase Database
location.
- `
  ``
  ``
  `

  ### [FIRDataEventTypeChildAdded](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Enums/FIRDataEventType#/c:@E@FIRDataEventType@FIRDataEventTypeChildAdded)

  `
  `  
  A new child node is added to a location.  

  #### Declaration

  Objective-C  

      FIRDataEventTypeChildAdded

- `
  ``
  ``
  `

  ### [FIRDataEventTypeChildRemoved](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Enums/FIRDataEventType#/c:@E@FIRDataEventType@FIRDataEventTypeChildRemoved)

  `
  `  
  A child node is removed from a location.  

  #### Declaration

  Objective-C  

      FIRDataEventTypeChildRemoved

- `
  ``
  ``
  `

  ### [FIRDataEventTypeChildChanged](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Enums/FIRDataEventType#/c:@E@FIRDataEventType@FIRDataEventTypeChildChanged)

  `
  `  
  A child node at a location changes.  

  #### Declaration

  Objective-C  

      FIRDataEventTypeChildChanged

- `
  ``
  ``
  `

  ### [FIRDataEventTypeChildMoved](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Enums/FIRDataEventType#/c:@E@FIRDataEventType@FIRDataEventTypeChildMoved)

  `
  `  
  A child node moves relative to the other child nodes at a location.  

  #### Declaration

  Objective-C  

      FIRDataEventTypeChildMoved

- `
  ``
  ``
  `

  ### [FIRDataEventTypeValue](https://firebase.google.com/docs/reference/ios/firebasedatabase/api/reference/Enums/FIRDataEventType#/c:@E@FIRDataEventType@FIRDataEventTypeValue)

  `
  `  
  Any data changes at a location or, recursively, at any child node.  

  #### Declaration

  Objective-C  

      FIRDataEventTypeValue