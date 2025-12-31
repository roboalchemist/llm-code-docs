# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionTextRecognizedLanguage


    @interface FIRVisionTextRecognizedLanguage : NSObject

Detected language from text recognition.
- `
  ``
  ``
  `

  ### [languageCode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage#/c:objc(cs)FIRVisionTextRecognizedLanguage(py)languageCode)

  `
  `  
  The BCP-47 language code, such as, "en-US" or "sr-Latn". For more information, see
  <http://www.unicode.org/reports/tr35/#Unicode_locale_identifier>.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSString *languageCode;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionTextRecognizedLanguage#/c:objc(cs)FIRVisionTextRecognizedLanguage(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;