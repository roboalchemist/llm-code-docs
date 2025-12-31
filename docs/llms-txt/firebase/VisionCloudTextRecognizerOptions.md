# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudTextRecognizerOptions.md.txt

# FirebaseMLVision Framework Reference

# VisionCloudTextRecognizerOptions

    class VisionCloudTextRecognizerOptions : NSObject

Options for a cloud text recognizer.
- `
  ``
  ``
  `

  ### [modelType](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudTextRecognizerOptions#/c:objc(cs)FIRVisionCloudTextRecognizerOptions(py)modelType)

  `
  `  
  Model type for cloud text recognition. The default is [VisionCloudTextModelType.sparse](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionCloudTextModelType.html#/c:@E@FIRVisionCloudTextModelType@FIRVisionCloudTextModelTypeSparse).  

  #### Declaration

  Swift  

      var modelType: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionCloudTextModelType.html { get set }

- `
  ``
  ``
  `

  ### [languageHints](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudTextRecognizerOptions#/c:objc(cs)FIRVisionCloudTextRecognizerOptions(py)languageHints)

  `
  `  
  An array of hinted language codes for cloud text recognition. The default is `nil`. See
  <https://cloud.google.com/vision/docs/languages> for supported language codes.  

  #### Declaration

  Swift  

      var languageHints: [String]? { get set }

- `
  ``
  ``
  `

  ### [apiKeyOverride](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudTextRecognizerOptions#/c:objc(cs)FIRVisionCloudTextRecognizerOptions(py)APIKeyOverride)

  `
  `  
  API key to use for Cloud Vision API. If `nil`, the default API key from FirebaseApp will be used.  

  #### Declaration

  Swift  

      var apiKeyOverride: String? { get set }

- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudTextRecognizerOptions#/c:objc(cs)FIRVisionCloudTextRecognizerOptions(im)init)

  `
  `  
  Designated initializer that creates a new instance of cloud text recognizer options.  

  #### Declaration

  Swift  

      init()