# Source: https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRCustomRemoteModel.md.txt

# FirebaseMLModelInterpreter Framework Reference

# FIRCustomRemoteModel


    @interface FIRCustomRemoteModel

A custom model that is stored remotely on the server and downloaded to the device.
- `
  ``
  ``
  `

  ### [-initWithName:](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRCustomRemoteModel#/c:objc(cs)FIRCustomRemoteModel(im)initWithName:)

  `
  `  
  Creates a new instance with the given values.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)initWithName:(nonnull NSString *)name;

  #### Parameters

  |--------------|--------------------------------------------------------------------------------------------------------------------|
  | ` `*name*` ` | The name of the remote model. Specify the name assigned to the model when it was uploaded to the Firebase Console. |

  #### Return Value

  A new `CustomRemoteModel` instance.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlmodelinterpreter/api/reference/Classes/FIRCustomRemoteModel#/c:objc(cs)FIRCustomRemoteModel(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;