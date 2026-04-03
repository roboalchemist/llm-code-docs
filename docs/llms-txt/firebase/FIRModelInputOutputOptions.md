# Source: https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInputOutputOptions.md.txt

# FirebaseMLModelInterpreter Framework Reference

# FIRModelInputOutputOptions


    @interface FIRModelInputOutputOptions : NSObject

Options for a custom model specifying input and output data types and dimensions.
- `
  ``
  ``
  `

  ### [-setInputFormatForIndex:type:dimensions:error:](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInputOutputOptions#/c:objc(cs)FIRModelInputOutputOptions(im)setInputFormatForIndex:type:dimensions:error:)

  `
  `  
  Sets the type and dimensions for the input at a given index.  

  #### Declaration

  Objective-C  

      - (BOOL)setInputFormatForIndex:(NSUInteger)index
                                type:(https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Enums/FIRModelElementType.html)type
                          dimensions:(nonnull NSArray<NSNumber *> *)dimensions
                               error:(NSError *_Nullable *_Nullable)error;

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

  ### [-setOutputFormatForIndex:type:dimensions:error:](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRModelInputOutputOptions#/c:objc(cs)FIRModelInputOutputOptions(im)setOutputFormatForIndex:type:dimensions:error:)

  `
  `  
  Sets the type and dimensions for the output at a given index.  

  #### Declaration

  Objective-C  

      - (BOOL)setOutputFormatForIndex:(NSUInteger)index
                                 type:(https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Enums/FIRModelElementType.html)type
                           dimensions:(nonnull NSArray<NSNumber *> *)dimensions
                                error:(NSError *_Nullable *_Nullable)error;

  #### Parameters

  |--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | ` `*index*` `      | The index of the output to configure.                                                                                                                                                                                                                                                                                        |
  | ` `*type*` `       | The element type for the output at a given index.                                                                                                                                                                                                                                                                            |
  | ` `*dimensions*` ` | The array of dimensions for the output at a given index. Each dimension should have an `NSUInteger` value. For example, for a 2 dimensional output with 4 rows and 9 columns, the corresponding dimensions should be provided as an `NSArray` containing two `NSNumber`s with unsigned integer values, 4 and 9 respectively. |
  | ` `*error*` `      | The error, if any, during the operation, including `MachineLearningErrorDomainCode.InvalidArgument` when: - `type` is invalid. - `dimensions` are nil or empty. - Any of the `dimensions` is 0 (it must be positive). <br />                                                                                                 |

  #### Return Value

  Whether the operation is successful.