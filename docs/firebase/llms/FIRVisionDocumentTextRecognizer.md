# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextRecognizer.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionDocumentTextRecognizer


    @interface FIRVisionDocumentTextRecognizer : NSObject

A cloud document text recognizer that recognizes text in an image.
- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextRecognizer#/c:objc(cs)FIRVisionDocumentTextRecognizer(im)init)

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

  ### [-processImage:completion:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionDocumentTextRecognizer#/c:objc(cs)FIRVisionDocumentTextRecognizer(im)processImage:completion:)

  `
  `  
  Processes the given image for cloud document text recognition.  

  #### Declaration

  Objective-C  

      - (void)processImage:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage.html *)image
                completion:
                    (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionDocumentTextRecognizer.h@T@FIRVisionDocumentTextRecognitionCallback)completion;

  #### Parameters

  |--------------------|----------------------------------------------------------------------------------|
  | ` `*image*` `      | The image to process for recognizing document text.                              |
  | ` `*completion*` ` | Handler to call back on the main queue when document text recognition completes. |