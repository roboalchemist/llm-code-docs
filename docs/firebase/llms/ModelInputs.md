# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInputs.md.txt

# FirebaseMLModelInterpreter Framework Reference

# ModelInputs

    class ModelInputs : NSObject

Input data for a Firebase custom model.
- `
  ``
  ``
  `

  ### [addInput(_:)](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInputs#/c:objc(cs)FIRModelInputs(im)addInput:error:)

  `
  `  
  Appends an input at the next index. The index starts from 0 and is incremented each time an
  input is added.  

  #### Declaration

  Swift  

      func addInput(_ input: Any) throws

  #### Parameters

  |---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*input*` ` | Input data for the next index. Input can be `NSData`, or a one-dimensional or multi-dimensional array of `NSNumber`s (float, int, char, long).                               |
  | ` `*error*` ` | The error, if any, during the operation, including `MLKitErrorDomainCode.InvalidArgument` when: - `input` is nil. - The input type is neither `NSData` nor `NSArray`. <br /> |

  #### Return Value

  Whether the operation is successful.