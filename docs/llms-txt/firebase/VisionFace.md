# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace.md.txt

# FirebaseMLVision Framework Reference

# VisionFace

    class VisionFace : NSObject

A human face detected in an image.
- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)frame)

  `
  `  
  The rectangle that holds the discovered relative to the detected image in the view
  coordinate system.  

  #### Declaration

  Swift  

      var frame: CGRect { get }

- `
  ``
  ``
  `

  ### [hasTrackingID](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)hasTrackingID)

  `
  `  
  Indicates whether the face has a tracking ID.  

  #### Declaration

  Swift  

      var hasTrackingID: Bool { get }

- `
  ``
  ``
  `

  ### [trackingID](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)trackingID)

  `
  `  
  The tracking identifier of the face.  

  #### Declaration

  Swift  

      var trackingID: Int { get }

- `
  ``
  ``
  `

  ### [hasHeadEulerAngleY](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)hasHeadEulerAngleY)

  `
  `  
  Indicates whether the detector found the head y euler angle.  

  #### Declaration

  Swift  

      var hasHeadEulerAngleY: Bool { get }

- `
  ``
  ``
  `

  ### [headEulerAngleY](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)headEulerAngleY)

  `
  `  
  Indicates the rotation of the face about the vertical axis of the image. Positive y euler angle
  is when the face is turned towards the right side of the image that is being processed.  

  #### Declaration

  Swift  

      var headEulerAngleY: CGFloat { get }

- `
  ``
  ``
  `

  ### [hasHeadEulerAngleZ](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)hasHeadEulerAngleZ)

  `
  `  
  Indicates whether the detector found the head z euler angle.  

  #### Declaration

  Swift  

      var hasHeadEulerAngleZ: Bool { get }

- `
  ``
  ``
  `

  ### [headEulerAngleZ](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)headEulerAngleZ)

  `
  `  
  Indicates the rotation of the face about the axis pointing out of the image. Positive z euler
  angle is a counter-clockwise rotation within the image plane.  

  #### Declaration

  Swift  

      var headEulerAngleZ: CGFloat { get }

- `
  ``
  ``
  `

  ### [hasSmilingProbability](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)hasSmilingProbability)

  `
  `  
  Indicates whether a smiling probability is available.  

  #### Declaration

  Swift  

      var hasSmilingProbability: Bool { get }

- `
  ``
  ``
  `

  ### [smilingProbability](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)smilingProbability)

  `
  `  
  Probability that the face is smiling.  

  #### Declaration

  Swift  

      var smilingProbability: CGFloat { get }

- `
  ``
  ``
  `

  ### [hasLeftEyeOpenProbability](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)hasLeftEyeOpenProbability)

  `
  `  
  Indicates whether a left eye open probability is available.  

  #### Declaration

  Swift  

      var hasLeftEyeOpenProbability: Bool { get }

- `
  ``
  ``
  `

  ### [leftEyeOpenProbability](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)leftEyeOpenProbability)

  `
  `  
  Probability that the face's left eye is open.  

  #### Declaration

  Swift  

      var leftEyeOpenProbability: CGFloat { get }

- `
  ``
  ``
  `

  ### [hasRightEyeOpenProbability](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)hasRightEyeOpenProbability)

  `
  `  
  Indicates whether a right eye open probability is available.  

  #### Declaration

  Swift  

      var hasRightEyeOpenProbability: Bool { get }

- `
  ``
  ``
  `

  ### [rightEyeOpenProbability](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(py)rightEyeOpenProbability)

  `
  `  
  Probability that the face's right eye is open.  

  #### Declaration

  Swift  

      var rightEyeOpenProbability: CGFloat { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(im)init)

  `
  `  
  Unavailable.
- `
  ``
  ``
  `

  ### [landmark(ofType:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(im)landmarkOfType:)

  `
  `  
  Returns the landmark, if any, of the given type in this detected face.  

  #### Declaration

  Swift  

      func landmark(ofType type: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionFaceLandmark.h@T@FIRFaceLandmarkType) -> https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceLandmark.html?

  #### Parameters

  |--------------|----------------------------------|
  | ` `*type*` ` | The type of the facial landmark. |

  #### Return Value

  The landmark of the given type in this face. `nil` if there isn't one.
- `
  ``
  ``
  `

  ### [contour(ofType:)](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace#/c:objc(cs)FIRVisionFace(im)contourOfType:)

  `
  `  
  Returns the contour, if any, of the given type in this detected face.  

  #### Declaration

  Swift  

      func contour(ofType type: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionFaceContour.h@T@FIRFaceContourType) -> https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceContour.html?

  #### Parameters

  |--------------|---------------------------------|
  | ` `*type*` ` | The type of the facial contour. |

  #### Return Value

  The contour of the given type in this face. `nil` if there isn't one.