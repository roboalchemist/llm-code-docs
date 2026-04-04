# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorPerformanceMode.md.txt

# FirebaseMLVision Framework Reference

# VisionFaceDetectorPerformanceMode

    enum VisionFaceDetectorPerformanceMode : UInt

@enum VisionFaceDetectorPerformanceMode
Performance preference for accuracy or speed of face detection.
- `
  ``
  ``
  `

  ### [fast](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorPerformanceMode#/c:@E@FIRVisionFaceDetectorPerformanceMode@FIRVisionFaceDetectorPerformanceModeFast)

  `
  `  
  Face detection performance mode that runs faster, but may detect fewer faces and/or return
  results with lower accuracy.  

  #### Declaration

  Swift  

      case fast = 1

- `
  ``
  ``
  `

  ### [accurate](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorPerformanceMode#/c:@E@FIRVisionFaceDetectorPerformanceMode@FIRVisionFaceDetectorPerformanceModeAccurate)

  `
  `  
  Face detection performance mode that runs slower, but may detect more faces and/or return
  results with higher accuracy.  

  #### Declaration

  Swift  

      case accurate = 2