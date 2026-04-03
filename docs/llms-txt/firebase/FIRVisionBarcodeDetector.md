# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetector.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionBarcodeDetector


    @interface FIRVisionBarcodeDetector : NSObject

A barcode detector that detects barcodes in an image.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetector#/c:objc(cs)FIRVisionBarcodeDetector(im)init)

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

  ### [-detectInImage:completion:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionBarcodeDetector#/c:objc(cs)FIRVisionBarcodeDetector(im)detectInImage:completion:)

  `
  `  
  Detects barcodes in the given image.  

  #### Declaration

  Objective-C  

      - (void)detectInImage:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage.html *)image
                 completion:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionBarcodeDetector.h@T@FIRVisionBarcodeDetectionCallback)completion;

  #### Parameters

  |--------------------|-------------------------------------------------------------------------|
  | ` `*image*` `      | The image to use for detecting barcodes.                                |
  | ` `*completion*` ` | Handler to call back on the main queue with barcodes detected or error. |