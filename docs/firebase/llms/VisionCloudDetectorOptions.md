# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudDetectorOptions.md.txt

# FirebaseMLVision Framework Reference

# VisionCloudDetectorOptions

    class VisionCloudDetectorOptions : NSObject

Generic options of a vision cloud detector.
- `
  ``
  ``
  `

  ### [modelType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudDetectorOptions#/c:objc(cs)FIRVisionCloudDetectorOptions(py)modelType)

  `
  `  
  Type of model to use in vision cloud detection API. Defaults to `.stable`.  

  #### Declaration

  Swift  

      var modelType: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionCloudModelType.html { get set }

- `
  ``
  ``
  `

  ### [maxResults](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudDetectorOptions#/c:objc(cs)FIRVisionCloudDetectorOptions(py)maxResults)

  `
  `  
  Maximum number of results to return. Defaults to 10. Does not apply to [VisionTextRecognizer](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionTextRecognizer.html)
  and [VisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionDocumentTextRecognizer.html).  

  #### Declaration

  Swift  

      var maxResults: UInt { get set }

- `
  ``
  ``
  `

  ### [apiKeyOverride](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudDetectorOptions#/c:objc(cs)FIRVisionCloudDetectorOptions(py)APIKeyOverride)

  `
  `  
  API key to use for Cloud Vision API. If `nil`, the default API key from FirebaseApp will be used.  

  #### Declaration

  Swift  

      var apiKeyOverride: String? { get set }