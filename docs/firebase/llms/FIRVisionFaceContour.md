# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceContour.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionFaceContour


    @interface FIRVisionFaceContour : NSObject

A contour on a human face detected in an image.
- `
  ``
  ``
  `

  ### [type](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceContour#/c:objc(cs)FIRVisionFaceContour(py)type)

  `
  `  
  The facial contour type.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Type-Definitions.html#/c:FIRVisionFaceContour.h@T@FIRFaceContourType _Nonnull type;

- `
  ``
  ``
  `

  ### [points](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceContour#/c:objc(cs)FIRVisionFaceContour(py)points)

  `
  `  
  An array of 2D points that make up the facial contour.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSArray<https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionPoint.html *> *_Nonnull points;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceContour#/c:objc(cs)FIRVisionFaceContour(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;