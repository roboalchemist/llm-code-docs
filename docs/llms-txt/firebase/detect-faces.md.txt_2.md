# Source: https://firebase.google.com/docs/ml-kit/ios/detect-faces.md.txt

> [!CAUTION]
> This page describes an old version of the Face Detection API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Detect faces with ML Kit on iOS](https://developers.google.com/ml-kit/vision/face-detection/ios)
> for the latest documentation.


You can use ML Kit to detect faces in images and video.

<br />

## Before you begin

1. If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:

   ```
   pod 'Firebase/MLVision', '6.25.0'
   # If you want to detect face contours (landmark detection and classification
   # don't require this additional model):
   pod 'Firebase/MLVisionFaceModel', '6.25.0'
   ```
   After you install or update your project's Pods, be sure to open your Xcode project using its `.xcworkspace`.
3. In your app, import Firebase:

   #### Swift

   ```swift
   import Firebase
   ```

   #### Objective-C

   ```objective-c
   @import Firebase;
   ```

## Input image guidelines

For ML Kit to accurately detect faces, input images must contain faces
that are represented by sufficient pixel data. In general, each face you want
to detect in an image should be at least 100x100 pixels. If you want to detect
the contours of faces, ML Kit requires higher resolution input: each face
should be at least 200x200 pixels.

If you are detecting faces in a real-time application, you might also want
to consider the overall dimensions of the input images. Smaller images can be
processed faster, so to reduce latency, capture images at lower resolutions
(keeping in mind the above accuracy requirements) and ensure that the
subject's face occupies as much of the image as possible. Also see
[Tips to improve real-time performance](https://firebase.google.com/docs/ml-kit/ios/detect-faces#performance_tips).

Poor image focus can hurt accuracy. If you aren't getting acceptable results,
try asking the user to recapture the image.

The orientation of a face relative to the camera can also affect what facial
features ML Kit detects. See
[Face Detection
Concepts](https://firebase.google.com/docs/ml-kit/face-detection-concepts#landmarks).

## 1. Configure the face detector

Before you apply face detection to an image, if you want to change any of the face detector's default settings, specify those settings with a [`VisionFaceDetectorOptions`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions) object. You can change the following settings:

<br />

| Settings ||
|---|---|
| `performanceMode` | `fast` (default) \| `accurate` Favor speed or accuracy when detecting faces. |
| `landmarkMode` | `none` (default) \| `all` Whether to attempt to detect the facial "landmarks"---eyes, ears, nose, cheeks, mouth---of all detected faces. |
| `contourMode` | `none` (default) \| `all` Whether to detect the contours of facial features. Contours are detected for only the most prominent face in an image. |
| `classificationMode` | `none` (default) \| `all` Whether or not to classify faces into categories such as "smiling", and "eyes open". |
| `minFaceSize` | `CGFloat` (default: `0.1`) The minimum size, relative to the image, of faces to detect. |
| `isTrackingEnabled` | `false` (default) \| `true` Whether or not to assign faces an ID, which can be used to track faces across images. Note that when contour detection is enabled, only one face is detected, so face tracking doesn't produce useful results. For this reason, and to improve detection speed, don't enable both contour detection and face tracking. |

For example, build a [`VisionFaceDetectorOptions`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetectorOptions)
object like one of the following examples:

#### Swift

```swift
// High-accuracy landmark detection and face classification
let options = VisionFaceDetectorOptions()
options.performanceMode = .accurate
options.landmarkMode = .all
options.classificationMode = .all

// Real-time contour detection of multiple faces
let options = VisionFaceDetectorOptions()
options.contourMode = .all
```

#### Objective-C

```objective-c
// High-accuracy landmark detection and face classification
FIRVisionFaceDetectorOptions *options = [[FIRVisionFaceDetectorOptions alloc] init];
options.performanceMode = FIRVisionFaceDetectorPerformanceModeAccurate;
options.landmarkMode = FIRVisionFaceDetectorLandmarkModeAll;
options.classificationMode = FIRVisionFaceDetectorClassificationModeAll;

// Real-time contour detection of multiple faces
FIRVisionFaceDetectorOptions *options = [[FIRVisionFaceDetectorOptions alloc] init];
options.contourMode = FIRVisionFaceDetectorContourModeAll;
```

## 2. Run the face detector

To detect faces in an image, pass the image as a `UIImage` or a `CMSampleBufferRef` to the `VisionFaceDetector`'s `detect(in:)` method:

<br />

1. Get an instance of [`VisionFaceDetector`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFaceDetector):

   #### Swift

   ```swift
   lazy var vision = Vision.vision()

   let faceDetector = vision.faceDetector(options: options)
   ```

   #### Objective-C

   ```objective-c
   FIRVision *vision = [FIRVision vision];
   FIRVisionFaceDetector *faceDetector = [vision faceDetector];
   // Or, to change the default settings:
   // FIRVisionFaceDetector *faceDetector =
   //     [vision faceDetectorWithOptions:options];
   ```
2. Create a [`VisionImage`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImage) object using a `UIImage` or a
   `CMSampleBufferRef`.

   To use a `UIImage`:
   1. If necessary, rotate the image so that its `imageOrientation` property is `.up`.
   2. Create a `VisionImage` object using the correctly-rotated `UIImage`. Do not specify any rotation metadata---the default value, `.topLeft`, must be used.

      #### Swift

      ```swift
      let image = VisionImage(image: uiImage)
      ```

      #### Objective-C

      ```objective-c
      FIRVisionImage *image = [[FIRVisionImage alloc] initWithImage:uiImage];
      ```

   To use a `CMSampleBufferRef`:
   1. Create a [`VisionImageMetadata`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageMetadata) object that specifies the
      orientation of the image data contained in the
      `CMSampleBufferRef` buffer.

      To get the image orientation:

      #### Swift

      ```swift
      func imageOrientation(
          deviceOrientation: UIDeviceOrientation,
          cameraPosition: AVCaptureDevice.Position
          ) -> VisionDetectorImageOrientation {
          switch deviceOrientation {
          case .portrait:
              return cameraPosition == .front ? .leftTop : .rightTop
          case .landscapeLeft:
              return cameraPosition == .front ? .bottomLeft : .topLeft
          case .portraitUpsideDown:
              return cameraPosition == .front ? .rightBottom : .leftBottom
          case .landscapeRight:
              return cameraPosition == .front ? .topRight : .bottomRight
          case .faceDown, .faceUp, .unknown:
              return .leftTop
          }
      }
      ```

      #### Objective-C

      ```objective-c
      - (FIRVisionDetectorImageOrientation)
          imageOrientationFromDeviceOrientation:(UIDeviceOrientation)deviceOrientation
                                 cameraPosition:(AVCaptureDevicePosition)cameraPosition {
        switch (deviceOrientation) {
          case UIDeviceOrientationPortrait:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationLeftTop;
            } else {
              return FIRVisionDetectorImageOrientationRightTop;
            }
          case UIDeviceOrientationLandscapeLeft:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationBottomLeft;
            } else {
              return FIRVisionDetectorImageOrientationTopLeft;
            }
          case UIDeviceOrientationPortraitUpsideDown:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationRightBottom;
            } else {
              return FIRVisionDetectorImageOrientationLeftBottom;
            }
          case UIDeviceOrientationLandscapeRight:
            if (cameraPosition == AVCaptureDevicePositionFront) {
              return FIRVisionDetectorImageOrientationTopRight;
            } else {
              return FIRVisionDetectorImageOrientationBottomRight;
            }
          default:
            return FIRVisionDetectorImageOrientationTopLeft;
        }
      }
      ```

      Then, create the metadata object:

      #### Swift

      ```swift
      let cameraPosition = AVCaptureDevice.Position.back  // Set to the capture device you used.
      let metadata = VisionImageMetadata()
      metadata.orientation = imageOrientation(
          deviceOrientation: UIDevice.current.orientation,
          cameraPosition: cameraPosition
      )
      ```

      #### Objective-C

      ```objective-c
      FIRVisionImageMetadata *metadata = [[FIRVisionImageMetadata alloc] init];
      AVCaptureDevicePosition cameraPosition =
          AVCaptureDevicePositionBack;  // Set to the capture device you used.
      metadata.orientation =
          [self imageOrientationFromDeviceOrientation:UIDevice.currentDevice.orientation
                                       cameraPosition:cameraPosition];
      ```
   2. Create a `VisionImage` object using the `CMSampleBufferRef` object and the rotation metadata:

      #### Swift

      ```swift
      let image = VisionImage(buffer: sampleBuffer)
      image.metadata = metadata
      ```

      #### Objective-C

      ```objective-c
      FIRVisionImage *image = [[FIRVisionImage alloc] initWithBuffer:sampleBuffer];
      image.metadata = metadata;
      ```
3. Then, pass the image to the `detect(in:)` method:

   #### Swift

   ```swift
   faceDetector.process(visionImage) { faces, error in
     guard error == nil, let faces = faces, !faces.isEmpty else {
       // ...
       return
     }

     // Faces detected
     // ...
   }
   ```

   #### Objective-C

   ```objective-c
   [faceDetector detectInImage:image
                    completion:^(NSArray<FIRVisionFace *> *faces,
                                 NSError *error) {
     if (error != nil) {
       return;
     } else if (faces != nil) {
       // Recognized faces
     }
   }];
   ```

## 3. Get information about detected faces

If the face detection operation succeeds, the face detector passes an array of [`VisionFace`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionFace) objects to the completion handler. Each `VisionFace` object represents a face that was detected in the image. For each face, you can get its bounding coordinates in the input image, as well as any other information you configured the face detector to find. For example:

<br />

#### Swift

```swift
for face in faces {
  let frame = face.frame
  if face.hasHeadEulerAngleY {
    let rotY = face.headEulerAngleY  // Head is rotated to the right rotY degrees
  }
  if face.hasHeadEulerAngleZ {
    let rotZ = face.headEulerAngleZ  // Head is rotated upward rotZ degrees
  }

  // If landmark detection was enabled (mouth, ears, eyes, cheeks, and
  // nose available):
  if let leftEye = face.landmark(ofType: .leftEye) {
    let leftEyePosition = leftEye.position
  }

  // If contour detection was enabled:
  if let leftEyeContour = face.contour(ofType: .leftEye) {
    let leftEyePoints = leftEyeContour.points
  }
  if let upperLipBottomContour = face.contour(ofType: .upperLipBottom) {
    let upperLipBottomPoints = upperLipBottomContour.points
  }

  // If classification was enabled:
  if face.hasSmilingProbability {
    let smileProb = face.smilingProbability
  }
  if face.hasRightEyeOpenProbability {
    let rightEyeOpenProb = face.rightEyeOpenProbability
  }

  // If face tracking was enabled:
  if face.hasTrackingID {
    let trackingId = face.trackingID
  }
}
```

#### Objective-C

```objective-c
for (FIRVisionFace *face in faces) {
  // Boundaries of face in image
  CGRect frame = face.frame;

  if (face.hasHeadEulerAngleY) {
    CGFloat rotY = face.headEulerAngleY;  // Head is rotated to the right rotY degrees
  }
  if (face.hasHeadEulerAngleZ) {
    CGFloat rotZ = face.headEulerAngleZ;  // Head is tilted sideways rotZ degrees
  }

  // If landmark detection was enabled (mouth, ears, eyes, cheeks, and
  // nose available):
  FIRVisionFaceLandmark *leftEar = [face landmarkOfType:FIRFaceLandmarkTypeLeftEar];
  if (leftEar != nil) {
    FIRVisionPoint *leftEarPosition = leftEar.position;
  }

  // If contour detection was enabled:
  FIRVisionFaceContour *upperLipBottomContour = [face contourOfType:FIRFaceContourTypeUpperLipBottom];
  if (upperLipBottomContour != nil) {
    NSArray<FIRVisionPoint *> *upperLipBottomPoints = upperLipBottomContour.points;
    if (upperLipBottomPoints.count > 0) {
      NSLog("Detected the bottom contour of the subject's upper lip.")
    }
  }

  // If classification was enabled:
  if (face.hasSmilingProbability) {
    CGFloat smileProb = face.smilingProbability;
  }
  if (face.hasRightEyeOpenProbability) {
    CGFloat rightEyeOpenProb = face.rightEyeOpenProbability;
  }

  // If face tracking was enabled:
  if (face.hasTrackingID) {
    NSInteger trackingID = face.trackingID;
  }
}
```

### Example of face contours

When you have face contour detection enabled, you get a list of points for
each facial feature that was detected. These points represent the shape of the
feature. See the [Face
Detection Concepts Overview](https://firebase.google.com/docs/ml-kit/face-detection-concepts#contours) for details about how contours are
represented.

The following image illustrates how these points map to a face (click the
image to enlarge):
[![](https://firebase.google.com/static/docs/ml-kit/images/examples/face_contours.svg)](https://firebase.google.com/static/docs/ml-kit/images/examples/face_contours.svg)

## Real-time face detection

If you want to use face detection in a real-time application, follow these
guidelines to achieve the best framerates:

- [Configure the face detector](https://firebase.google.com/docs/ml-kit/ios/detect-faces#1-configure-the-face-detector) to use either
  face contour detection or classification and landmark detection, but not both:

  Contour detection  

  Landmark detection  

  Classification  

  Landmark detection and classification  

  Contour detection and landmark detection  

  Contour detection and classification  

  Contour detection, landmark detection, and classification  
- Enable `fast` mode (enabled by default).

- Consider capturing images at a lower resolution. However, also keep in mind
  this API's image dimension requirements.

- Throttle calls to the detector. If a new video frame becomes available while the detector is running, drop the frame.
- If you are using the output of the detector to overlay graphics on the input image, first get the result from ML Kit, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame. See the [previewOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Controllers/FIRVideoCamViewController.m#L856) and [FIRDetectionOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Views/FIRDetectionOverlayView.m) classes in the showcase sample app for an example.