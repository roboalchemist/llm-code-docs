# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceLandmark.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionFaceLandmark


    @interface FIRVisionFaceLandmark : NSObject

A landmark on a human face detected in an image.
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceLandmark#/c:objc(cs)FIRVisionFaceLandmark(py)type)

  `
  `  
  The type of the facial landmark.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionFaceLandmark.h@T@FIRFaceLandmarkType _Nonnull type;

- `
  ``
  ``
  `

  ### [position](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceLandmark#/c:objc(cs)FIRVisionFaceLandmark(py)position)

  `
  `  
  2D position of the facial landmark.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionPoint.html *_Nonnull position;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceLandmark#/c:objc(cs)FIRVisionFaceLandmark(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;