# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionPoint.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionPoint


    @interface FIRVisionPoint : NSObject

A 2D or 3D point in the image. A valid point must have both x and y coordinates. The point's
coordinates are in the same scale as the original image.
- `
  ``
  ``
  `

  ### [x](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionPoint#/c:objc(cs)FIRVisionPoint(py)x)

  `
  `  
  X coordinate. The value is float.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSNumber *_Nonnull x;

- `
  ``
  ``
  `

  ### [y](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionPoint#/c:objc(cs)FIRVisionPoint(py)y)

  `
  `  
  Y coordinate. The value is float.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly) NSNumber *_Nonnull y;

- `
  ``
  ``
  `

  ### [z](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionPoint#/c:objc(cs)FIRVisionPoint(py)z)

  `
  `  
  Z coordinate (or depth). The value is float. Z is nil if it is a 2D point.  

  #### Declaration

  Objective-C  

      @property (nonatomic, readonly, nullable) NSNumber *z;

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionPoint#/c:objc(cs)FIRVisionPoint(im)init)

  `
  `  
  Unavailable.  

  #### Declaration

  Objective-C  

      - (nonnull instancetype)init;