# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDocumentTextRecognizerOptions.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionCloudDocumentTextRecognizerOptions


    @interface FIRVisionCloudDocumentTextRecognizerOptions : NSObject

Options for a cloud document text recognizer.
- `
  ``
  ``
  `

  ### [languageHints](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDocumentTextRecognizerOptions#/c:objc(cs)FIRVisionCloudDocumentTextRecognizerOptions(py)languageHints)

  `
  `  
  An array of hinted language codes for cloud document text recognition. The default is `nil`. See
  <https://cloud.google.com/vision/docs/languages> for supported language codes.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSArray<NSString *> *languageHints;

- `
  ``
  ``
  `

  ### [APIKeyOverride](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDocumentTextRecognizerOptions#/c:objc(cs)FIRVisionCloudDocumentTextRecognizerOptions(py)APIKeyOverride)

  `
  `  
  API key to use for Cloud Vision API. If `nil`, the default API key from FirebaseApp will be used.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *APIKeyOverride;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDocumentTextRecognizerOptions#/c:objc(cs)FIRVisionCloudDocumentTextRecognizerOptions(im)init)

  `
  `  
  Designated initializer that creates a new instance of cloud document text recognizer options.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;