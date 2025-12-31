# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionOnDeviceImageLabelerOptions.md.txt

# FirebaseMLVision Framework Reference

# VisionOnDeviceImageLabelerOptions

    class VisionOnDeviceImageLabelerOptions : NSObject

Options for an on-device image labeler.
- `
  ``
  ``
  `

  ### [confidenceThreshold](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionOnDeviceImageLabelerOptions#/c:objc(cs)FIRVisionOnDeviceImageLabelerOptions(py)confidenceThreshold)

  `
  `  
  The confidence threshold for labels returned by the image labeler. Labels returned by the image
  labeler will have a confidence level higher or equal to the given threshold. Values must be in
  range \[0, 1\]. If unset or an invalid value is set, the default threshold of 0.5 is used. There is
  no limit on the maximum number of labels returned by an on-device image labeler.  

  #### Declaration

  Swift  

      var confidenceThreshold: Float { get set }

- `
  ``
  ``
  `

  ### [init()](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionOnDeviceImageLabelerOptions#/c:objc(cs)FIRVisionOnDeviceImageLabelerOptions(im)init)

  `
  `  
  Designated initializer that creates a new instance of on-device image labeler options with the
  default values.  

  #### Declaration

  Swift  

      init()