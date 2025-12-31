# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextRecognizer.md.txt

# FirebaseMLVision Framework Reference

# VisionDocumentTextRecognizer

    class VisionDocumentTextRecognizer : NSObject

A cloud document text recognizer that recognizes text in an image.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextRecognizer#/c:objc(cs)FIRVisionDocumentTextRecognizer(im)init)

  `
  `  
  Unavailable. Use [Vision](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision.html) factory methods.
- `
  ``
  ``
  `

  ### [process(_:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextRecognizer#/c:objc(cs)FIRVisionDocumentTextRecognizer(im)processImage:completion:)

  `
  `  
  Processes the given image for cloud document text recognition.  

  #### Declaration

  Swift  

      func process(_ image: FIRVisionImage, completion: @escaping https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionDocumentTextRecognizer.h@T@FIRVisionDocumentTextRecognitionCallback)

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------|
  | ` `*image*` `      | The image to process for recognizing document text.                              |
  | ` `*completion*` ` | Handler to call back on the main queue when document text recognition completes. |