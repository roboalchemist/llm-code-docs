# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedBreak.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionTextRecognizedBreak


    @interface FIRVisionTextRecognizedBreak : NSObject

Detected break from text recognition.
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedBreak#/c:objc(cs)FIRVisionTextRecognizedBreak(py)type)

  `
  `  
  The recognized text break type.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionTextRecognizedBreakType.html type;

- `
  ``
  ``
  `

  ### [isPrefix](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedBreak#/c:objc(cs)FIRVisionTextRecognizedBreak(py)isPrefix)

  `
  `  
  Indicates whether the break prepends the text element. If `NO`, the break comes after the text
  element.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL isPrefix;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedBreak#/c:objc(cs)FIRVisionTextRecognizedBreak(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;