# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionFaceDetectorPerformanceMode.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionFaceDetectorPerformanceMode

    enum FIRVisionFaceDetectorPerformanceMode {}

@enum VisionFaceDetectorPerformanceMode
Performance preference for accuracy or speed of face detection.
- `
  ``
  ``
  `

  ### [FIRVisionFaceDetectorPerformanceModeFast](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionFaceDetectorPerformanceMode#/c:@E@FIRVisionFaceDetectorPerformanceMode@FIRVisionFaceDetectorPerformanceModeFast)

  `
  `  
  Face detection performance mode that runs faster, but may detect fewer faces and/or return
  results with lower accuracy.  

  #### Declaration

  Objective-C  

      FIRVisionFaceDetectorPerformanceModeFast = 1

- `
  ``
  ``
  `

  ### [FIRVisionFaceDetectorPerformanceModeAccurate](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionFaceDetectorPerformanceMode#/c:@E@FIRVisionFaceDetectorPerformanceMode@FIRVisionFaceDetectorPerformanceModeAccurate)

  `
  `  
  Face detection performance mode that runs slower, but may detect more faces and/or return
  results with higher accuracy.  

  #### Declaration

  Objective-C  

      FIRVisionFaceDetectorPerformanceModeAccurate