# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextRecognizer.md.txt

# FirebaseMLVision Framework Reference

# VisionTextRecognizer

    class VisionTextRecognizer : NSObject

An on-device or cloud text recognizer that recognizes text in an image.
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextRecognizer#/c:objc(cs)FIRVisionTextRecognizer(py)type)

  `
  `  
  The text recognizer type.  

  #### Declaration

  Swift  

      var type: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionTextRecognizerType.html { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextRecognizer#/c:objc(cs)FIRVisionTextRecognizer(im)init)

  `
  `  
  Unavailable. Use [Vision](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision.html) factory methods.
- `
  ``
  ``
  `

  ### [process(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextRecognizer#/c:objc(cs)FIRVisionTextRecognizer(im)processImage:completion:)

  `
  `  
  Processes the given image for on-device or cloud text recognition.  

  #### Declaration

  Swift  

      func process(_ image: FIRVisionImage, completion: @escaping https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionTextRecognizer.h@T@FIRVisionTextRecognitionCallback)

  #### Parameters

  |--------------------|-------------------------------------------------------------------------|
  | ` `*image*` `      | The image to process for recognizing text.                              |
  | ` `*completion*` ` | Handler to call back on the main queue when text recognition completes. |