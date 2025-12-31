# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDetectorOptions.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionCloudDetectorOptions


    @interface FIRVisionCloudDetectorOptions : NSObject

Generic options of a vision cloud detector.
- `
  ``
  ``
  `

  ### [modelType](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDetectorOptions#/c:objc(cs)FIRVisionCloudDetectorOptions(py)modelType)

  `
  `  
  Type of model to use in vision cloud detection API. Defaults to `.stable`.  

  #### Declaration

  Objective-C  

      @property (nonatomic) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionCloudModelType.html modelType;

- `
  ``
  ``
  `

  ### [maxResults](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDetectorOptions#/c:objc(cs)FIRVisionCloudDetectorOptions(py)maxResults)

  `
  `  
  Maximum number of results to return. Defaults to 10. Does not apply to `VisionTextRecognizer`
  and `VisionDocumentTextRecognizer`.  

  #### Declaration

  Objective-C  

      @property (nonatomic) NSUInteger maxResults;

- `
  ``
  ``
  `

  ### [APIKeyOverride](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudDetectorOptions#/c:objc(cs)FIRVisionCloudDetectorOptions(py)APIKeyOverride)

  `
  `  
  API key to use for Cloud Vision API. If `nil`, the default API key from FirebaseApp will be used.  

  #### Declaration

  Objective-C  

      @property (nonatomic, copy, nullable) NSString *APIKeyOverride;