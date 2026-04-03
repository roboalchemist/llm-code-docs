# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionPoint.md.txt

# FirebaseMLVision Framework Reference

# VisionPoint

    class VisionPoint : NSObject

A 2D or 3D point in the image. A valid point must have both x and y coordinates. The point's
coordinates are in the same scale as the original image.
- `
  ``
  ``
  `

  ### [x](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionPoint#/c:objc(cs)FIRVisionPoint(py)x)

  `
  `  
  X coordinate. The value is float.  

  #### Declaration

  Swift  

      var x: NSNumber { get }

- `
  ``
  ``
  `

  ### [y](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionPoint#/c:objc(cs)FIRVisionPoint(py)y)

  `
  `  
  Y coordinate. The value is float.  

  #### Declaration

  Swift  

      var y: NSNumber { get }

- `
  ``
  ``
  `

  ### [z](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionPoint#/c:objc(cs)FIRVisionPoint(py)z)

  `
  `  
  Z coordinate (or depth). The value is float. Z is nil if it is a 2D point.  

  #### Declaration

  Swift  

      var z: NSNumber? { get }

- `
  ``
  ``
  `

  ### [-init](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionPoint#/c:objc(cs)FIRVisionPoint(im)init)

  `
  `  
  Unavailable.