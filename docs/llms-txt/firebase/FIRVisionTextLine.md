# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextLine.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionTextLine


    @interface FIRVisionTextLine : NSObject

A text line recognized in an image that consists of an array of elements.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextLine#/c:objc(cs)FIRVisionTextLine(py)text)

  `
  `  
  String representation of the text line that was recognized.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull text;

- `
  ``
  ``
  `

  ### [elements](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextLine#/c:objc(cs)FIRVisionTextLine(py)elements)

  `
  `  
  An array of text elements that make up the line.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextElement.html *> *_Nonnull elements;

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextLine#/c:objc(cs)FIRVisionTextLine(py)frame)

  `
  `  
  The rectangle that contains the text line relative to the image in the default coordinate space.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGRect frame;

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextLine#/c:objc(cs)FIRVisionTextLine(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the text line. On-device text recognizers only detect
  Latin-based languages, while cloud text recognizers can detect multiple languages. If no
  languages are recognized, the array is empty.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage.html *> *_Nonnull recognizedLanguages;

- `
  ``
  ``
  `

  ### [cornerPoints](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextLine#/c:objc(cs)FIRVisionTextLine(py)cornerPoints)

  `
  `  
  The four corner points of the text line in clockwise order starting with the top left point
  relative to the image in the default coordinate space. The `NSValue` objects are `CGPoint`s. For
  cloud text recognizers, the array is `nil`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSArray<NSValue *> *cornerPoints;

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextLine#/c:objc(cs)FIRVisionTextLine(py)confidence)

  `
  `  
  The confidence of the recognized text line. The value is `nil` for all text recognizers except
  for cloud text recognizers with model type `VisionCloudTextModelType.dense`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSNumber *confidence;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextLine#/c:objc(cs)FIRVisionTextLine(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;