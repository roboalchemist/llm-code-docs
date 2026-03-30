# Source: https://firebase.google.com/docs/ml-kit/ios/recognize-landmarks.md.txt

> [!CAUTION]
> This page is about an old version of the
> Landmark Recognition API, which was part of ML Kit for
> Firebase. For the latest docs, see
> [the latest version](https://firebase.google.com/docs/ml/ios/recognize-landmarks)
> in the
> Firebase ML section.


You can use ML Kit to recognize well-known landmarks in an image.
Use of ML Kit to access Cloud ML functionality is subject to the [Google Cloud Platform License
Agreement](https://cloud.google.com/terms/) and [Service
Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the Firebase [Pricing](https://firebase.google.com/pricing) page.

<br />

## Before you begin

1. If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:

   ```
   pod 'Firebase/MLVision', '6.25.0'
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
4. If you have not already enabled Cloud-based APIs for your project, do so
   now:

   1. Open the [ML Kit
      APIs page](https://console.firebase.google.com/project/_/ml/apis) of the Firebase console.
   2. If you have not already upgraded your project to a Blaze pricing plan, click
      **Upgrade** to do so. (You will be prompted to upgrade only if your
      project isn't on the Blaze plan.)

      Only Blaze-level projects can use Cloud-based APIs.
   3. If Cloud-based APIs aren't already enabled, click **Enable Cloud-based
      APIs**.

   Before you deploy to production an app that uses a Cloud API, you should take some additional steps to [prevent and mitigate the
   effect of unauthorized API access](https://firebase.google.com/docs/ml-kit/ios/secure-api-key).

## Configure the landmark detector

By default, the Cloud detector uses the stable version of the model and
returns up to 10 results. If you want to change either of these settings,
specify them with a `VisionCloudDetectorOptions` object as
in the following example:

#### Swift

```swift
let options = VisionCloudDetectorOptions()
options.modelType = .latest
options.maxResults = 20
```

#### Objective-C

```objective-c
  FIRVisionCloudDetectorOptions *options =
      [[FIRVisionCloudDetectorOptions alloc] init];
  options.modelType = FIRVisionCloudModelTypeLatest;
  options.maxResults = 20;
  
```

In the next step, pass the `VisionCloudDetectorOptions`
object when you create the Cloud detector object.

## Run the landmark detector

To recognize landmarks in an image, pass the image as a `UIImage` or a `CMSampleBufferRef` to the `VisionCloudLandmarkDetector`'s `detect(in:)` method:

<br />

1. Get an instance of [`VisionCloudLandmarkDetector`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmarkDetector):

   #### Swift

   ```swift
   lazy var vision = Vision.vision()

   let cloudDetector = vision.cloudLandmarkDetector(options: options)
   // Or, to use the default settings:
   // let cloudDetector = vision.cloudLandmarkDetector()
   ```

   #### Objective-C

   ```objective-c
   FIRVision *vision = [FIRVision vision];
   FIRVisionCloudLandmarkDetector *landmarkDetector = [vision cloudLandmarkDetector];
   // Or, to change the default settings:
   // FIRVisionCloudLandmarkDetector *landmarkDetector =
   //     [vision cloudLandmarkDetectorWithOptions:options];
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
   cloudDetector.detect(in: visionImage) { landmarks, error in
     guard error == nil, let landmarks = landmarks, !landmarks.isEmpty else {
       // ...
       return
     }

     // Recognized landmarks
     // ...
   }
   ```

   #### Objective-C

   ```objective-c
   [landmarkDetector detectInImage:image
                        completion:^(NSArray<FIRVisionCloudLandmark *> *landmarks,
                                     NSError *error) {
     if (error != nil) {
       return;
     } else if (landmarks != nil) {
       // Got landmarks
     }
   }];
   ```

## Get information about the recognized landmarks

If landmark recognition succeeds, an array of [`VisionCloudLandmark`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmark) objects will be passed to the completion handler. From each object, you can get information about a landmark recognized in the image.

<br />

For example:

#### Swift

```swift
for landmark in landmarks {
  let landmarkDesc = landmark.landmark
  let boundingPoly = landmark.frame
  let entityId = landmark.entityId

  // A landmark can have multiple locations: for example, the location the image
  // was taken, and the location of the landmark depicted.
  for location in landmark.locations {
    let latitude = location.latitude
    let longitude = location.longitude
  }

  let confidence = landmark.confidence
}
```

#### Objective-C

```objective-c
for (FIRVisionCloudLandmark *landmark in landmarks) {
   NSString *landmarkDesc = landmark.landmark;
   CGRect frame = landmark.frame;
   NSString *entityId = landmark.entityId;

   // A landmark can have multiple locations: for example, the location the image
   // was taken, and the location of the landmark depicted.
   for (FIRVisionLatitudeLongitude *location in landmark.locations) {
     double latitude = [location.latitude doubleValue];
     double longitude = [location.longitude doubleValue];
   }

   float confidence = [landmark.confidence floatValue];
}
```

## Next steps

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to [prevent and mitigate the
  effect of unauthorized API access](https://firebase.google.com/docs/ml-kit/ios/secure-api-key).