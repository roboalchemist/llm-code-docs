# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextBlock.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionTextBlock


    @interface FIRVisionTextBlock : NSObject

A text block recognized in an image that consists of an array of text lines.
- `
  ``
  ``
  `

  ### [text](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)text)

  `
  `  
  String representation of the text block that was recognized.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSString *_Nonnull text;

- `
  ``
  ``
  `

  ### [lines](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)lines)

  `
  `  
  An array of text lines that make up the block.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextLine.html *> *_Nonnull lines;

- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)frame)

  `
  `  
  The rectangle that contains the text block relative to the image in the default coordinate space.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGRect frame;

- `
  ``
  ``
  `

  ### [recognizedLanguages](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)recognizedLanguages)

  `
  `  
  An array of recognized languages in the text block. On-device text recognizers only detect
  Latin-based languages, while cloud text recognizers can detect multiple languages. If no
  languages are recognized, the array is empty.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage.html *> *_Nonnull recognizedLanguages;

- `
  ``
  ``
  `

  ### [cornerPoints](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)cornerPoints)

  `
  `  
  The four corner points of the text block in clockwise order starting with the top left point
  relative to the image in the default coordinate space. The `NSValue` objects are `CGPoint`s. For
  cloud text recognizers, the array is `nil`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSArray<NSValue *> *cornerPoints;

- `
  ``
  ``
  `

  ### [confidence](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextBlock#/c:objc(cs)FIRVisionTextBlock(py)confidence)

  `
  `  
  The confidence of the recognized text block. The value is `nil` for all text recognizers except
  for cloud text recognizers with model type `VisionCloudTextModelType.dense`.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSNumber *confidence;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextBlock#/c:objc(cs)FIRVisionTextBlock(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;