# Source: https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.md.txt

# FirebaseMLVision Framework Reference

# FIRVisionFaceDetectorOptions


    @interface FIRVisionFaceDetectorOptions : NSObject

Options for specifying a face detector.
- `
  ``
  ``
  `

  ### [classificationMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)classificationMode)

  `
  `  
  The face detector classification mode for characterizing attributes such as smiling. Defaults to
  `.none`.  

  #### Declaration

  Objective-C  

      @property (nonatomic) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionFaceDetectorClassificationMode.html classificationMode;

- `
  ``
  ``
  `

  ### [performanceMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)performanceMode)

  `
  `  
  The face detector performance mode that determines the accuracy of the results and the speed of
  the detection. Defaults to `.fast`.  

  #### Declaration

  Objective-C  

      @property (nonatomic) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionFaceDetectorPerformanceMode.html performanceMode;

- `
  ``
  ``
  `

  ### [landmarkMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)landmarkMode)

  `
  `  
  The face detector landmark mode that determines the type of landmark results returned by
  detection. Defaults to `.none`.  

  #### Declaration

  Objective-C  

      @property (nonatomic) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionFaceDetectorLandmarkMode.html landmarkMode;

- `
  ``
  ``
  `

  ### [contourMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)contourMode)

  `
  `  
  The face detector contour mode that determines the type of contour results returned by detection.
  Defaults to `.none`.

  <br />

  The following detection results are returned when setting this mode to `.all`:

  <br />

  [performanceMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)performanceMode) set to `.fast`, and both [classificationMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)classificationMode) and [landmarkMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)landmarkMode) set to
  `.none`, then only the prominent face will be returned with detected contours.

  <br />

  [performanceMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)performanceMode) set to `.accurate`, or if [classificationMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)classificationMode) or [landmarkMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)landmarkMode) is set to
  `.all`, then all detected faces will be returned, but only the prominent face will have
  detecteted contours.  

  #### Declaration

  Objective-C  

      @property (nonatomic) https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Enums/FIRVisionFaceDetectorContourMode.html contourMode;

- `
  ``
  ``
  `

  ### [minFaceSize](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)minFaceSize)

  `
  `  
  The smallest desired face size. The size is expressed as a proportion of the width of the head to
  the image width. For example, if a value of 0.1 is specified, then the smallest face to search
  for is roughly 10% of the width of the image being searched. Defaults to 0.1. This option does
  not apply to contour detection.  

  #### Declaration

  Objective-C  

      @property (nonatomic) CGFloat minFaceSize;

- `
  ``
  ``
  `

  ### [trackingEnabled](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions#/c:objc(cs)FIRVisionFaceDetectorOptions(py)trackingEnabled)

  `
  `  
  Whether the face tracking feature is enabled for face detection. Defaults to NO. When
  [performanceMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)performanceMode) is set to `.fast`, and both [classificationMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)classificationMode) and [landmarkMode](https://firebase.google.com/docs/reference/ios/firebasemlvision/api/reference/Classes/FIRVisionFaceDetectorOptions.html#/c:objc(cs)FIRVisionFaceDetectorOptions(py)landmarkMode) set to
  `.none`, this option will be ignored and tracking will be disabled.  

  #### Declaration

  Objective-C  

      @property (nonatomic, assign, unsafe_unretained, readwrite,
                getter=isTrackingEnabled) BOOL trackingEnabled;