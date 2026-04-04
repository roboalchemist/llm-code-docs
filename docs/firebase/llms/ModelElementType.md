# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Enums/ModelElementType.md.txt

# FirebaseMLModelInterpreter Framework Reference

# ModelElementType

    enum ModelElementType : UInt

@enum ModelElementType
This enum specifies the type of elements in the custom model's input or output.
- `
  ``
  ``
  `

  ### [unknown](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Enums/ModelElementType#/c:@E@FIRModelElementType@FIRModelElementTypeUnknown)

  `
  `  
  Element type unknown/undefined.  

  #### Declaration

  Swift  

      case unknown = 0

- `
  ``
  ``
  `

  ### [float32](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Enums/ModelElementType#/c:@E@FIRModelElementType@FIRModelElementTypeFloat32)

  `
  `  
  32-bit single precision floating point.  

  #### Declaration

  Swift  

      case float32 = 1

- `
  ``
  ``
  `

  ### [int32](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Enums/ModelElementType#/c:@E@FIRModelElementType@FIRModelElementTypeInt32)

  `
  `  
  32-bit signed integer.  

  #### Declaration

  Swift  

      case int32 = 2

- `
  ``
  ``
  `

  ### [uInt8](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Enums/ModelElementType#/c:@E@FIRModelElementType@FIRModelElementTypeUInt8)

  `
  `  
  8-bit unsigned integer.  

  #### Declaration

  Swift  

      case uInt8 = 3

- `
  ``
  ``
  `

  ### [int64](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Enums/ModelElementType#/c:@E@FIRModelElementType@FIRModelElementTypeInt64)

  `
  `  
  64-bit signed integer.  

  #### Declaration

  Swift  

      case int64 = 4