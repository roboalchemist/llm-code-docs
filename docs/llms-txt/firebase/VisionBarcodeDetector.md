# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetector.md.txt

# FirebaseMLVision Framework Reference

# VisionBarcodeDetector

    class VisionBarcodeDetector : NSObject

A barcode detector that detects barcodes in an image.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetector#/c:objc(cs)FIRVisionBarcodeDetector(im)init)

  `
  `  
  Unavailable. Use [Vision](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/Vision.html) factory methods.
- `
  ``
  ``
  `

  ### [detect(in:completion:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionBarcodeDetector#/c:objc(cs)FIRVisionBarcodeDetector(im)detectInImage:completion:)

  `
  `  
  Detects barcodes in the given image.  

  #### Declaration

  Swift  

      func detect(in image: FIRVisionImage, completion: @escaping https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionBarcodeDetector.h@T@FIRVisionBarcodeDetectionCallback)

  #### Parameters

  |--------------------|-------------------------------------------------------------------------|
  | ` `*image*` `      | The image to use for detecting barcodes.                                |
  | ` `*completion*` ` | Handler to call back on the main queue with barcodes detected or error. |