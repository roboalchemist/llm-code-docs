# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelOutputs.md.txt

# FirebaseMLModelInterpreter Framework Reference

# ModelOutputs

    class ModelOutputs : NSObject

Inference results of a Firebase custom model.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelOutputs#/c:objc(cs)FIRModelOutputs(im)init)

  `
  `  
  Unavailable.
- `
  ``
  ``
  `

  ### [output(index:)](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelOutputs#/c:objc(cs)FIRModelOutputs(im)outputAtIndex:error:)

  `
  `  
  Returns the output for a given index.  

  #### Declaration

  Swift  

      func output(index: UInt) throws -> Any

  #### Parameters

  |---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*index*` ` | The index of the output to get.                                                                                                                               |
  | ` `*error*` ` | The error, if any, during the operation, including `MachineLearningErrorDomainCode.InvalidArgument` when: - There is no model output with given index. <br /> |

  #### Return Value

  The `index`-th output. Returns nil if there is an error.