# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabeler.md.txt

# FirebaseMLVision Framework Reference

# VisionImageLabeler

    class VisionImageLabeler : NSObject

An on-device or cloud image labeler for labeling images.
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabeler#/c:objc(cs)FIRVisionImageLabeler(py)type)

  `
  `  
  The image labeler type.  

  #### Declaration

  Swift  

      var type: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionImageLabelerType.html { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabeler#/c:objc(cs)FIRVisionImageLabeler(im)init)

  `
  `  
  Unavailable. Use [Vision](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision.html) factory methods.
- `
  ``
  ``
  `

  ### [process(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageLabeler#/c:objc(cs)FIRVisionImageLabeler(im)processImage:completion:)

  `
  `  
  Processes the given image for on-device or cloud image labeling.  

  #### Declaration

  Swift  

      func process(_ image: FIRVisionImage, completion: @escaping https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionImageLabeler.h@T@FIRVisionImageLabelerCallback)

  #### Parameters

  |--------------------|--------------------------------------------------------------|
  | ` `*image*` `      | The image to process.                                        |
  | ` `*completion*` ` | Handler to call back on the main queue with labels or error. |