# Source: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions.md.txt

# FirebaseMLVision Framework Reference

# VisionFaceDetectorOptions

    class VisionFaceDetectorOptions : NSObject

Options for specifying a face detector.
- `
  ``
  ``
  `

  ### [classificationMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)classificationMode)

  `
  `  
  The face detector classification mode for characterizing attributes such as smiling. Defaults to
  `.none`.  

  #### Declaration

  Swift  

      var classificationMode: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorClassificationMode.html { get set }

- `
  ``
  ``
  `

  ### [performanceMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)performanceMode)

  `
  `  
  The face detector performance mode that determines the accuracy of the results and the speed of
  the detection. Defaults to `.fast`.  

  #### Declaration

  Swift  

      var performanceMode: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorPerformanceMode.html { get set }

- `
  ``
  ``
  `

  ### [landmarkMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)landmarkMode)

  `
  `  
  The face detector landmark mode that determines the type of landmark results returned by
  detection. Defaults to `.none`.  

  #### Declaration

  Swift  

      var landmarkMode: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorLandmarkMode.html { get set }

- `
  ``
  ``
  `

  ### [contourMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)contourMode)

  `
  `  
  The face detector contour mode that determines the type of contour results returned by detection.
  Defaults to `.none`.

  <br />

  The following detection results are returned when setting this mode to [.all](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Constants.html#/c:@FIRFaceContourTypeAll):

  <br />

  [performanceMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)performanceMode) set to `.fast`, and both [classificationMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)classificationMode) and [landmarkMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)landmarkMode) set to
  `.none`, then only the prominent face will be returned with detected contours.

  <br />

  [performanceMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)performanceMode) set to `.accurate`, or if [classificationMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)classificationMode) or [landmarkMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)landmarkMode) is set to
  [.all](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Constants.html#/c:@FIRFaceContourTypeAll), then all detected faces will be returned, but only the prominent face will have
  detecteted contours.  

  #### Declaration

  Swift  

      var contourMode: https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Enums/VisionFaceDetectorContourMode.html { get set }

- `
  ``
  ``
  `

  ### [minFaceSize](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)minFaceSize)

  `
  `  
  The smallest desired face size. The size is expressed as a proportion of the width of the head to
  the image width. For example, if a value of 0.1 is specified, then the smallest face to search
  for is roughly 10% of the width of the image being searched. Defaults to 0.1. This option does
  not apply to contour detection.  

  #### Declaration

  Swift  

      var minFaceSize: CGFloat { get set }

- `
  ``
  ``
  `

  ### [isTrackingEnabled](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)trackingEnabled)

  `
  `  
  Whether the face tracking feature is enabled for face detection. Defaults to NO. When
  [performanceMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)performanceMode) is set to `.fast`, and both [classificationMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)classificationMode) and [landmarkMode](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)landmarkMode) set to
  `.none`, this option will be ignored and tracking will be disabled.  

  #### Declaration

  Swift  

      var isTrackingEnabled: Bool { get set }