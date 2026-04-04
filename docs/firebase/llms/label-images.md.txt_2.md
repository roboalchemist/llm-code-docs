# Source: https://firebase.google.com/docs/ml-kit/ios/label-images.md.txt

> [!CAUTION]
> This page describes an old version of the Image Labeling API, which was part
> of ML Kit for Firebase. The functionality of this API has been split into
> two new APIs ([learn more](https://developers.google.com/ml-kit/migration)):
>
> - [On-device image labeling](https://developers.google.com/ml-kit/vision/image-labeling/ios) is part of the new standalone ML Kit SDK, which you can use with or without Firebase.
> - [Cloud image labeling](https://firebase.google.com/docs/ml/ios/label-images) is part of Firebase ML, which includes all of Firebase's cloud-based ML features.


You can use ML Kit to label objects recognized in an image, using either
an on-device model or a cloud model. See the
[overview](https://firebase.google.com/docs/ml-kit/label-images) to learn about the benefits of
each approach.
Use of ML Kit to access Cloud ML functionality is subject to the [Google Cloud Platform License
Agreement](https://cloud.google.com/terms/) and [Service
Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the Firebase [Pricing](https://firebase.google.com/pricing) page.

<br />

## Before you begin

1. If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:

   ```
   pod 'Firebase/MLVision', '6.25.0'

   # If using the on-device API:
   pod 'Firebase/MLVisionLabelModel', '6.25.0'
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
4. If you want to use the Cloud-based model, and you have not already enabled
   the Cloud-based APIs for your project, do so now:

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

   If you want to use only the on-device model, you can skip this step.

Now you are ready to label images using either an on-device model or a
cloud-based model.

## 1. Prepare the input image

Create a [`VisionImage`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImage) object using a `UIImage` or a
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

## 2. Configure and run the image labeler

To label objects in an image, pass the `VisionImage` object to the `VisionImageLabeler`'s `processImage()` method.

<br />

1. First, get an instance of `VisionImageLabeler`.

   If you want to use the on-device image labeler:

   ### Swift

       let labeler = Vision.vision().onDeviceImageLabeler()

       // Or, to set the minimum confidence required:
       // let options = VisionOnDeviceImageLabelerOptions()
       // options.confidenceThreshold = 0.7
       // let labeler = Vision.vision().onDeviceImageLabeler(options: options)

   ### Objective-C

       FIRVisionImageLabeler *labeler = [[FIRVision vision] onDeviceImageLabeler];

       // Or, to set the minimum confidence required:
       // FIRVisionOnDeviceImageLabelerOptions *options =
       //         [[FIRVisionOnDeviceImageLabelerOptions alloc] init];
       // options.confidenceThreshold = 0.7;
       // FIRVisionImageLabeler *labeler =
       //         [[FIRVision vision] onDeviceImageLabelerWithOptions:options];

   If you want to use the cloud image labeler:

   ### Swift

       let labeler = Vision.vision().cloudImageLabeler()

       // Or, to set the minimum confidence required:
       // let options = VisionCloudImageLabelerOptions()
       // options.confidenceThreshold = 0.7
       // let labeler = Vision.vision().cloudImageLabeler(options: options)

   ### Objective-C

       FIRVisionImageLabeler *labeler = [[FIRVision vision] cloudImageLabeler];

       // Or, to set the minimum confidence required:
       // FIRVisionCloudImageLabelerOptions *options =
       //         [[FIRVisionCloudImageLabelerOptions alloc] init];
       // options.confidenceThreshold = 0.7;
       // FIRVisionImageLabeler *labeler =
       //         [[FIRVision vision] cloudImageLabelerWithOptions:options];

2. Then, pass the image to the `processImage()` method:

   ### Swift

       labeler.process(image) { labels, error in
           guard error == nil, let labels = labels else { return }

           // Task succeeded.
           // ...
       }

   ### Objective-C

       [labeler processImage:image
                  completion:^(NSArray<FIRVisionImageLabel *> *_Nullable labels,
                               NSError *_Nullable error) {
                      if (error != nil) { return; }

                      // Task succeeded.
                      // ...
                  }];

## 3. Get information about labeled objects

If image labeling succeeds, an array of `VisionImageLabel` objects will be passed to the completion handler. From each object, you can get information about a feature recognized in the image.

<br />

For example:

### Swift

    for label in labels {
        let labelText = label.text
        let entityId = label.entityID
        let confidence = label.confidence
    }

### Objective-C

    for (FIRVisionImageLabel *label in labels) {
       NSString *labelText = label.text;
       NSString *entityId = label.entityID;
       NSNumber *confidence = label.confidence;
    }

## Tips to improve real-time performance

If you want to label images in a real-time application, follow these
guidelines to achieve the best framerates:

- Throttle calls to the image labeler. If a new video frame becomes available while the image labeler is running, drop the frame.
- If you are using the output of the image labeler to overlay graphics on the input image, first get the result from ML Kit, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame. See the [previewOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Controllers/FIRVideoCamViewController.m#L856) and [FIRDetectionOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Views/FIRDetectionOverlayView.m) classes in the showcase sample app for an example.

## Next steps

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to [prevent and mitigate the
  effect of unauthorized API access](https://firebase.google.com/docs/ml-kit/ios/secure-api-key).