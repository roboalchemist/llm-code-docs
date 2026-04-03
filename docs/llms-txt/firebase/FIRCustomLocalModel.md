# Source: https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRCustomLocalModel.md.txt

# FirebaseMLModelInterpreter Framework Reference

# FIRCustomLocalModel


    @interface FIRCustomLocalModel

A custom model stored locally on the device.
- `
  ``
  ``
  `

  ### [-initWithModelPath:](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRCustomLocalModel#/c:objc(cs)FIRCustomLocalModel(im)initWithModelPath:)

  `
  `  
  Creates a new instance with the given model file path.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithModelPath:(nonnull NSString *)modelPath;

  #### Parameters

  |-------------------|----------------------------------------------------------------------------------|
  | ` `*modelPath*` ` | An absolute path to the TensorFlow Lite model file stored locally on the device. |

  #### Return Value

  A new `CustomLocalModel` instance.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRCustomLocalModel#/c:objc(cs)FIRCustomLocalModel(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;