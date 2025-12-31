# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudDocumentTextRecognizerOptions.md.txt

# FirebaseMLVision Framework Reference

# VisionCloudDocumentTextRecognizerOptions

    class VisionCloudDocumentTextRecognizerOptions : NSObject

Options for a cloud document text recognizer.
- `
  ``
  ``
  `

  ### [languageHints](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudDocumentTextRecognizerOptions#/c:objc(cs)FIRVisionCloudDocumentTextRecognizerOptions(py)languageHints)

  `
  `  
  An array of hinted language codes for cloud document text recognition. The default is `nil`. See
  <https://cloud.google.com/vision/docs/languages> for supported language codes.  

  #### Declaration

  Swift  

      var languageHints: [String]? { get set }

- `
  ``
  ``
  `

  ### [apiKeyOverride](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudDocumentTextRecognizerOptions#/c:objc(cs)FIRVisionCloudDocumentTextRecognizerOptions(py)APIKeyOverride)

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

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudDocumentTextRecognizerOptions#/c:objc(cs)FIRVisionCloudDocumentTextRecognizerOptions(im)init)

  `
  `  
  Designated initializer that creates a new instance of cloud document text recognizer options.  

  #### Declaration

  Swift  

      init()