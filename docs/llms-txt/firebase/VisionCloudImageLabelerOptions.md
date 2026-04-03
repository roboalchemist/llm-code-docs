# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudImageLabelerOptions.md.txt

# FirebaseMLVision Framework Reference

# VisionCloudImageLabelerOptions

    class VisionCloudImageLabelerOptions : NSObject

Options for a cloud image labeler.
- `
  ``
  ``
  `

  ### [confidenceThreshold](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudImageLabelerOptions#/c:objc(cs)FIRVisionCloudImageLabelerOptions(py)confidenceThreshold)

  `
  `  
  The confidence threshold for labels returned by the image labeler. Labels returned by the image
  labeler will have a confidence level higher or equal to the given threshold. Values must be in
  range \[0, 1\]. If unset or an invalid value is set, the default threshold of 0.5 is used. Up to 20
  labels with the top confidence will be returned.  

  #### Declaration

  Swift  

      var confidenceThreshold: Float { get set }

- `
  ``
  ``
  `

  ### [apiKeyOverride](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudImageLabelerOptions#/c:objc(cs)FIRVisionCloudImageLabelerOptions(py)APIKeyOverride)

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

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudImageLabelerOptions#/c:objc(cs)FIRVisionCloudImageLabelerOptions(im)init)

  `
  `  
  Designated initializer that creates a new instance of cloud image labeler options with the
  default values.  

  #### Declaration

  Swift  

      init()