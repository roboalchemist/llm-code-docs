# Source: https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelOutputs.md.txt

# FirebaseMLModelInterpreter Framework Reference

# FIRModelOutputs


    @interface FIRModelOutputs : NSObject

Inference results of a Firebase custom model.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelOutputs#/c:objc(cs)FIRModelOutputs(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-outputAtIndex:error:](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelOutputs#/c:objc(cs)FIRModelOutputs(im)outputAtIndex:error:)

  `
  `  
  Returns the output for a given index.  

  #### Declaration

  Objective-C  

      - (nullable id)outputAtIndex:(NSUInteger)index
                             error:(NSError *_Nullable *_Nullable)error;

  #### Parameters

  |---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*index*` ` | The index of the output to get.                                                                                                                               |
  | ` `*error*` ` | The error, if any, during the operation, including `MachineLearningErrorDomainCode.InvalidArgument` when: - There is no model output with given index. <br /> |

  #### Return Value

  The `index`-th output. Returns nil if there is an error.