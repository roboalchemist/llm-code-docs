# Source: https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInputOutputOptions.md.txt

# FirebaseMLModelInterpreter Framework Reference

# ModelInputOutputOptions

    class ModelInputOutputOptions : NSObject

Options for a custom model specifying input and output data types and dimensions.
- `
  ``
  ``
  `

  ### [setInputFormat(index:type:dimensions:)](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInputOutputOptions#/c:objc(cs)FIRModelInputOutputOptions(im)setInputFormatForIndex:type:dimensions:error:)

  `
  `  
  Sets the type and dimensions for the input at a given index.  

  #### Declaration

  Swift  

      func setInputFormat(index: UInt, type: https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Enums/ModelElementType.html, dimensions: [NSNumber]) throws

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*index*` `      | The index of the input to configure.                                                                                                                                                                                                                                                                                       |
  | ` `*type*` `       | The element type for the input at a given index.                                                                                                                                                                                                                                                                           |
  | ` `*dimensions*` ` | The array of dimensions for the input at a given index. Each dimension should have an `NSUInteger` value. For example, for a 2 dimensional input with 4 rows and 9 columns, the corresponding dimensions should be provided as an `NSArray` containing two `NSNumber`s with unsigned integer values, 4 and 9 respectively. |
  | ` `*error*` `      | The error, if any, during the operation, including `MachineLearningErrorDomainCode.InvalidArgument` when: - `type` is invalid. - `dimensions` are nil or empty. - Any of the `dimensions` is 0 (it must be positive). <br />                                                                                               |

  #### Return Value

  Whether the operation is successful.
- `
  ``
  ``
  `

  ### [setOutputFormat(index:type:dimensions:)](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInputOutputOptions#/c:objc(cs)FIRModelInputOutputOptions(im)setOutputFormatForIndex:type:dimensions:error:)

  `
  `  
  Sets the type and dimensions for the output at a given index.  

  #### Declaration

  Swift  

      func setOutputFormat(index: UInt, type: https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Enums/ModelElementType.html, dimensions: [NSNumber]) throws

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*index*` `      | The index of the output to configure.                                                                                                                                                                                                                                                                                        |
  | ` `*type*` `       | The element type for the output at a given index.                                                                                                                                                                                                                                                                            |
  | ` `*dimensions*` ` | The array of dimensions for the output at a given index. Each dimension should have an `NSUInteger` value. For example, for a 2 dimensional output with 4 rows and 9 columns, the corresponding dimensions should be provided as an `NSArray` containing two `NSNumber`s with unsigned integer values, 4 and 9 respectively. |
  | ` `*error*` `      | The error, if any, during the operation, including `MachineLearningErrorDomainCode.InvalidArgument` when: - `type` is invalid. - `dimensions` are nil or empty. - Any of the `dimensions` is 0 (it must be positive). <br />                                                                                                 |

  #### Return Value

  Whether the operation is successful.