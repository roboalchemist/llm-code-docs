# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudTextRecognizerOptions.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionCloudTextRecognizerOptions


    @interface FIRVisionCloudTextRecognizerOptions : NSObject

Options for a cloud text recognizer.
- `
  ``
  ``
  `

  ### [modelType](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudTextRecognizerOptions#/c:objc(cs)FIRVisionCloudTextRecognizerOptions(py)modelType)

  `
  `  
  Model type for cloud text recognition. The default is `VisionCloudTextModelType.sparse`.  

  #### Declaration

  Objective-C  

      @property (nonatomic) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionCloudTextModelType.html modelType;

- `
  ``
  ``
  `

  ### [languageHints](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudTextRecognizerOptions#/c:objc(cs)FIRVisionCloudTextRecognizerOptions(py)languageHints)

  `
  `  
  An array of hinted language codes for cloud text recognition. The default is `nil`. See
  <https://cloud.google.com/vision/docs/languages> for supported language codes.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSArray<NSString *> *languageHints;

- `
  ``
  ``
  `

  ### [APIKeyOverride](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudTextRecognizerOptions#/c:objc(cs)FIRVisionCloudTextRecognizerOptions(py)APIKeyOverride)

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

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudTextRecognizerOptions#/c:objc(cs)FIRVisionCloudTextRecognizerOptions(im)init)

  `
  `  
  Designated initializer that creates a new instance of cloud text recognizer options.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;