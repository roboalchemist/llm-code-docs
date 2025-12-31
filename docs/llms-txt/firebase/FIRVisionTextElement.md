# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextElement.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionTextElement


    @interface FIRVisionTextElement : NSObject

A text element recognized in an image. A text element is roughly equivalent to a space-separated
word in most Latin-script languages.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextElement#/c:objc(cs)FIRVisionTextElement(py)text)

  `
  `  
  String representation of the text element that was recognized.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull text;

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextElement#/c:objc(cs)FIRVisionTextElement(py)frame)

  `
  `  
  The rectangle that contains the text element relative to the image in the default coordinate
  space.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGRect frame;

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextElement#/c:objc(cs)FIRVisionTextElement(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the text element. (Cloud API only.)  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage.html *> *_Nonnull recognizedLanguages;

- `
  ``
  ``
  `

  ### [cornerPoints](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextElement#/c:objc(cs)FIRVisionTextElement(py)cornerPoints)

  `
  `  
  The four corner points of the text element in clockwise order starting with the top left point
  relative to the image in the default coordinate space. The `NSValue` objects are `CGPoint`s. For
  cloud text recognizers, the array is `nil`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSArray<NSValue *> *cornerPoints;

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextElement#/c:objc(cs)FIRVisionTextElement(py)confidence)

  `
  `  
  The confidence of the recognized text element. The value is `nil` for all text recognizers except
  for cloud text recognizers with model type `VisionCloudTextModelType.dense`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSNumber *confidence;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextElement#/c:objc(cs)FIRVisionTextElement(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;