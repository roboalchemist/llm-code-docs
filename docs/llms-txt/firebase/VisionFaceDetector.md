# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetector.md.txt

# FirebaseMLVision Framework Reference

# VisionFaceDetector

    class VisionFaceDetector : NSObject

A face detector that detects faces in an image.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetector#/c:objc(cs)FIRVisionFaceDetector(im)init)

  `
  `  
  Unavailable. Use [Vision](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision.html) factory methods.
- `
  ``
  ``
  `

  ### [process(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetector#/c:objc(cs)FIRVisionFaceDetector(im)processImage:completion:)

  `
  `  
  Processes the given image for face detection. The detection is performed asynchronously and calls
  back the completion handler with the detected face results or error on the main thread.  

  #### Declaration

  Swift  

      func process(_ image: FIRVisionImage, completion: @escaping https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionFaceDetector.h@T@FIRVisionFaceDetectionCallback)

  #### Parameters

  |--------------------|-----------------------------------------------------------------------|
  | ` `*image*` `      | The vision image to use for detecting faces.                          |
  | ` `*completion*` ` | Handler to call back on the main thread with faces detected or error. |

- `
  ``
  ``
  `

  ### [results(in:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetector#/c:objc(cs)FIRVisionFaceDetector(im)resultsInImage:error:)

  `
  `  
  Returns detected face results in the given image or `nil` if there was an error. The detection is
  performed synchronously on the calling thread.

  It is advised to call this method off the main thread to avoid blocking the UI. As a
  result, an `NSException` is raised if this method is called on the main thread.  

  #### Declaration

  Swift  

      func results(in image: FIRVisionImage) throws -> [FIRVisionFace]

  #### Parameters

  |---------------|--------------------------------------------------------------------------------|
  | ` `*image*` ` | The vision image to use for detecting faces.                                   |
  | ` `*error*` ` | An optional error parameter populated when there is an error during detection. |

  #### Return Value

  Array of faces detected in the given image or `nil` if there was an error.