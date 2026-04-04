# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmarkDetector.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionCloudLandmarkDetector


    @interface FIRVisionCloudLandmarkDetector : NSObject

A landmark detector that detects landmark in an image.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmarkDetector#/c:objc(cs)FIRVisionCloudLandmarkDetector(im)init)

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

  ### [-detectInImage:completion:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudLandmarkDetector#/c:objc(cs)FIRVisionCloudLandmarkDetector(im)detectInImage:completion:)

  `
  `  
  Detects landmark in a given image.  

  #### Declaration

  Objective-C  

      - (void)detectInImage:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage.html *)image
                 completion:
                     (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionCloudLandmarkDetector.h@T@FIRVisionCloudLandmarkDetectionCompletion)completion;

  #### Parameters

  |--------------------|-------------------------------------------------------------------------|
  | ` `*image*` `      | The image to use for detecting landmark.                                |
  | ` `*completion*` ` | Handler to call back on the main queue with landmark detected or error. |