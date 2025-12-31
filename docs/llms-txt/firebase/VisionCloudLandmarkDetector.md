# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmarkDetector.md.txt

# FirebaseMLVision Framework Reference

# VisionCloudLandmarkDetector

    class VisionCloudLandmarkDetector : NSObject

A landmark detector that detects landmark in an image.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmarkDetector#/c:objc(cs)FIRVisionCloudLandmarkDetector(im)init)

  `
  `  
  Unavailable. Use [Vision](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision.html) factory methods.
- `
  ``
  ``
  `

  ### [detect(in:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmarkDetector#/c:objc(cs)FIRVisionCloudLandmarkDetector(im)detectInImage:completion:)

  `
  `  
  Detects landmark in a given image.  

  #### Declaration

  Swift  

      func detect(in image: FIRVisionImage, completion: @escaping https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionCloudLandmarkDetector.h@T@FIRVisionCloudLandmarkDetectionCompletion)

  #### Parameters

  |--------------------|-------------------------------------------------------------------------|
  | ` `*image*` `      | The image to use for detecting landmark.                                |
  | ` `*completion*` ` | Handler to call back on the main queue with landmark detected or error. |