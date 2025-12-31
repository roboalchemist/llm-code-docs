# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDetectorImageOrientation.md.txt

# FirebaseMLVision Framework Reference

# VisionDetectorImageOrientation

    enum VisionDetectorImageOrientation : UInt

@enum VisionDetectorImageOrientation
This enum specifies where the origin (0,0) of the image is located. The constant has the same
value as defined by EXIF specifications.
- `
  ``
  ``
  `

  ### [topLeft](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDetectorImageOrientation#/c:@E@FIRVisionDetectorImageOrientation@FIRVisionDetectorImageOrientationTopLeft)

  `
  `  
  Orientation code indicating the 0th row is the top and the 0th column is the left side.  

  #### Declaration

  Swift  

      case topLeft = 1

- `
  ``
  ``
  `

  ### [topRight](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDetectorImageOrientation#/c:@E@FIRVisionDetectorImageOrientation@FIRVisionDetectorImageOrientationTopRight)

  `
  `  
  Orientation code indicating the 0th row is the top and the 0th column is the right side.  

  #### Declaration

  Swift  

      case topRight = 2

- `
  ``
  ``
  `

  ### [bottomRight](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDetectorImageOrientation#/c:@E@FIRVisionDetectorImageOrientation@FIRVisionDetectorImageOrientationBottomRight)

  `
  `  
  Orientation code indicating the 0th row is the bottom and the 0th column is the right side.  

  #### Declaration

  Swift  

      case bottomRight = 3

- `
  ``
  ``
  `

  ### [bottomLeft](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDetectorImageOrientation#/c:@E@FIRVisionDetectorImageOrientation@FIRVisionDetectorImageOrientationBottomLeft)

  `
  `  
  Orientation code indicating the 0th row is the bottom and the 0th column is the left side.  

  #### Declaration

  Swift  

      case bottomLeft = 4

- `
  ``
  ``
  `

  ### [leftTop](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDetectorImageOrientation#/c:@E@FIRVisionDetectorImageOrientation@FIRVisionDetectorImageOrientationLeftTop)

  `
  `  
  Orientation code indicating the 0th row is the left side and the 0th column is the top.  

  #### Declaration

  Swift  

      case leftTop = 5

- `
  ``
  ``
  `

  ### [rightTop](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDetectorImageOrientation#/c:@E@FIRVisionDetectorImageOrientation@FIRVisionDetectorImageOrientationRightTop)

  `
  `  
  Orientation code indicating the 0th row is the right side and the 0th column is the top.  

  #### Declaration

  Swift  

      case rightTop = 6

- `
  ``
  ``
  `

  ### [rightBottom](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDetectorImageOrientation#/c:@E@FIRVisionDetectorImageOrientation@FIRVisionDetectorImageOrientationRightBottom)

  `
  `  
  Orientation code indicating the 0th row is the right side and the 0th column is the bottom.  

  #### Declaration

  Swift  

      case rightBottom = 7

- `
  ``
  ``
  `

  ### [leftBottom](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionDetectorImageOrientation#/c:@E@FIRVisionDetectorImageOrientation@FIRVisionDetectorImageOrientationLeftBottom)

  `
  `  
  Orientation code indicating the 0th row is the left side and the 0th column is the
  bottom.  

  #### Declaration

  Swift  

      case leftBottom = 8