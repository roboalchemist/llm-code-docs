# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizer.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionTextRecognizer


    @interface FIRVisionTextRecognizer : NSObject

An on-device or cloud text recognizer that recognizes text in an image.
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizer#/c:objc(cs)FIRVisionTextRecognizer(py)type)

  `
  `  
  The text recognizer type.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionTextRecognizerType.html type;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizer#/c:objc(cs)FIRVisionTextRecognizer(im)init)

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

  ### [-processImage:completion:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizer#/c:objc(cs)FIRVisionTextRecognizer(im)processImage:completion:)

  `
  `  
  Processes the given image for on-device or cloud text recognition.  

  #### Declaration

  Objective-C  

      - (void)processImage:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionImage.html *)image
                completion:(nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionTextRecognizer.h@T@FIRVisionTextRecognitionCallback)completion;

  #### Parameters

  |--------------------|-------------------------------------------------------------------------|
  | ` `*image*` `      | The image to process for recognizing text.                              |
  | ` `*completion*` ` | Handler to call back on the main queue when text recognition completes. |