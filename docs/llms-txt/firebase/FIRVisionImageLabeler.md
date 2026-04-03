# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabeler.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionImageLabeler


    @interface FIRVisionImageLabeler : NSObject

An on-device or cloud image labeler for labeling images.
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabeler#/c:objc(cs)FIRVisionImageLabeler(py)type)

  `
  `  
  The image labeler type.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionImageLabelerType.html type;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabeler#/c:objc(cs)FIRVisionImageLabeler(im)init)

  `
  `  
  Unavailable. Use `Vision` factory methods.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-processImage:completion:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImageLabeler#/c:objc(cs)FIRVisionImageLabeler(im)processImage:completion:)

  `
  `  
  Processes the given image for on-device or cloud image labeling.  

  #### Declaration

  Objective-C  

      - (void)processImage:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage.html *)image
                completion:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionImageLabeler.h@T@FIRVisionImageLabelerCallback)completion;

  #### Parameters

  |--------------------|--------------------------------------------------------------|
  | ` `*image*` `      | The image to process.                                        |
  | ` `*completion*` ` | Handler to call back on the main queue with labels or error. |