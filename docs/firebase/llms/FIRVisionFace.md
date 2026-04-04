# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionFace


    @interface FIRVisionFace : NSObject

A human face detected in an image.
- `
  ``
  ``
  `

  ### [frame](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)frame)

  `
  `  
  The rectangle that holds the discovered relative to the detected image in the view
  coordinate system.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGRect frame;

- `
  ``
  ``
  `

  ### [hasTrackingID](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)hasTrackingID)

  `
  `  
  Indicates whether the face has a tracking ID.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL hasTrackingID;

- `
  ``
  ``
  `

  ### [trackingID](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)trackingID)

  `
  `  
  The tracking identifier of the face.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSInteger trackingID;

- `
  ``
  ``
  `

  ### [hasHeadEulerAngleY](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)hasHeadEulerAngleY)

  `
  `  
  Indicates whether the detector found the head y euler angle.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL hasHeadEulerAngleY;

- `
  ``
  ``
  `

  ### [headEulerAngleY](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)headEulerAngleY)

  `
  `  
  Indicates the rotation of the face about the vertical axis of the image. Positive y euler angle
  is when the face is turned towards the right side of the image that is being processed.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGFloat headEulerAngleY;

- `
  ``
  ``
  `

  ### [hasHeadEulerAngleZ](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)hasHeadEulerAngleZ)

  `
  `  
  Indicates whether the detector found the head z euler angle.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL hasHeadEulerAngleZ;

- `
  ``
  ``
  `

  ### [headEulerAngleZ](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)headEulerAngleZ)

  `
  `  
  Indicates the rotation of the face about the axis pointing out of the image. Positive z euler
  angle is a counter-clockwise rotation within the image plane.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGFloat headEulerAngleZ;

- `
  ``
  ``
  `

  ### [hasSmilingProbability](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)hasSmilingProbability)

  `
  `  
  Indicates whether a smiling probability is available.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL hasSmilingProbability;

- `
  ``
  ``
  `

  ### [smilingProbability](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)smilingProbability)

  `
  `  
  Probability that the face is smiling.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGFloat smilingProbability;

- `
  ``
  ``
  `

  ### [hasLeftEyeOpenProbability](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)hasLeftEyeOpenProbability)

  `
  `  
  Indicates whether a left eye open probability is available.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL hasLeftEyeOpenProbability;

- `
  ``
  ``
  `

  ### [leftEyeOpenProbability](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)leftEyeOpenProbability)

  `
  `  
  Probability that the face's left eye is open.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGFloat leftEyeOpenProbability;

- `
  ``
  ``
  `

  ### [hasRightEyeOpenProbability](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)hasRightEyeOpenProbability)

  `
  `  
  Indicates whether a right eye open probability is available.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) BOOL hasRightEyeOpenProbability;

- `
  ``
  ``
  `

  ### [rightEyeOpenProbability](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(py)rightEyeOpenProbability)

  `
  `  
  Probability that the face's right eye is open.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) CGFloat rightEyeOpenProbability;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;

- `
  ``
  ``
  `

  ### [-landmarkOfType:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(im)landmarkOfType:)

  `
  `  
  Returns the landmark, if any, of the given type in this detected face.  

  #### Declaration

  Objective-C  

      - (nullable https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceLandmark.html *)landmarkOfType:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionFaceLandmark.h@T@FIRFaceLandmarkType)type;

  #### Parameters

  |--------------|----------------------------------|
  | ` `*type*` ` | The type of the facial landmark. |

  #### Return Value

  The landmark of the given type in this face. `nil` if there isn't one.
- `
  ``
  ``
  `

  ### [-contourOfType:](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFace#/c:objc(cs)FIRVisionFace(im)contourOfType:)

  `
  `  
  Returns the contour, if any, of the given type in this detected face.  

  #### Declaration

  Objective-C  

      - (nullable https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceContour.html *)contourOfType:
          (nonnull https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionFaceContour.h@T@FIRFaceContourType)type;

  #### Parameters

  |--------------|---------------------------------|
  | ` `*type*` ` | The type of the facial contour. |

  #### Return Value

  The contour of the given type in this face. `nil` if there isn't one.