# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudImageLabelerOptions.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionCloudImageLabelerOptions


    @interface FIRVisionCloudImageLabelerOptions : NSObject

Options for a cloud image labeler.
- `
  ``
  ``
  `

  ### [confidenceThreshold](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudImageLabelerOptions#/c:objc(cs)FIRVisionCloudImageLabelerOptions(py)confidenceThreshold)

  `
  `  
  The confidence threshold for labels returned by the image labeler. Labels returned by the image
  labeler will have a confidence level higher or equal to the given threshold. Values must be in
  range \[0, 1\]. If unset or an invalid value is set, the default threshold of 0.5 is used. Up to 20
  labels with the top confidence will be returned.  

  #### Declaration

  Objective-C  

      @property (nonatomic) float confidenceThreshold;

- `
  ``
  ``
  `

  ### [APIKeyOverride](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudImageLabelerOptions#/c:objc(cs)FIRVisionCloudImageLabelerOptions(py)APIKeyOverride)

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

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionCloudImageLabelerOptions#/c:objc(cs)FIRVisionCloudImageLabelerOptions(im)init)

  `
  `  
  Designated initializer that creates a new instance of cloud image labeler options with the
  default values.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;