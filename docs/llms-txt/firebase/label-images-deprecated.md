# Source: https://firebase.google.com/docs/ml/android/label-images-deprecated.md.txt

# Source: https://firebase.google.com/docs/ml/ios/label-images-deprecated.md.txt

| This page describes an old version of labeling objects recognized in an image using the deprecatedFirebase MLVision SDK. As an alternative, you may[call Cloud Vision APIs using Firebase Auth and Callable Functions](https://firebase.google.com/docs/ml/ios/label-images)to allow only users logged into your app to access the API.

You can useFirebase MLto label objects recognized in an image. See the[overview](https://firebase.google.com/docs/ml/label-images)for information about this API's features.
| Use of the Cloud Vision APIs is subject to the[Google Cloud Platform License Agreement](https://cloud.google.com/terms/)and[Service Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the[Pricing](https://cloud.google.com/vision/pricing)page.
| **Looking for on-device image labeling?** Try the[standalone ML Kit library](https://developers.google.com/ml-kit/vision/image-labeling).

<br />

## Before you begin

If you have not already added Firebase to your app, do so by following the steps in the[getting started guide](https://firebase.google.com/docs/ios/setup).
1. Use Swift Package Manager to install and manage Firebase dependencies.
| Visit[our installation guide](https://firebase.google.com/docs/ios/installation-methods)to learn about the different ways you can add Firebase SDKs to your Apple project, including importing frameworks directly and using CocoaPods.
1. In Xcode, with your app project open, navigate to**File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:  

```text
  https://github.com/firebase/firebase-ios-sdk.git
```
| **Note:**New projects should use the default (latest) SDK version, but you can choose an older version if needed.
3. Choose theFirebase MLlibrary.
4. Add the`-ObjC`flag to the*Other Linker Flags*section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.
2. Next, perform some in-app setup:
1. In your app, import Firebase:

   #### Swift

   ```swift
   import FirebaseMLModelDownloader
   ```

   #### Objective-C

   ```objective-c
   @import FirebaseMLModelDownloader;
   ```
3. If you haven't already enabled Cloud-based APIs for your project, do so now:

   1. Open the[Firebase MLAPIs page](https://console.firebase.google.com/project/_/ml/apis)in theFirebaseconsole.
   2. If you haven't already upgraded your project to the[pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), click**Upgrade**to do so. (You'll be prompted to upgrade only if your project isn't on the Blaze pricing plan.)

      Only projects on the Blaze pricing plan can use Cloud-based APIs.
   3. If Cloud-based APIs aren't already enabled, click**Enable Cloud-based APIs**.

   | Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml/ios/secure-api-key).

Now you are ready to label images.

## 1. Prepare the input image

Create a[`VisionImage`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImage)object using a`UIImage`or a`CMSampleBufferRef`.

To use a`UIImage`:

1. If necessary, rotate the image so that its`imageOrientation`property is`.up`.
2. Create a`VisionImage`object using the correctly-rotated`UIImage`. Do not specify any rotation metadata---the default value,`.topLeft`, must be used.  

   #### Swift

   ```swift
   let image = VisionImage(image: uiImage)
   ```

   #### Objective-C

   ```objective-c
   FIRVisionImage *image = [[FIRVisionImage alloc] initWithImage:uiImage];
   ```

To use a`CMSampleBufferRef`:

1. Create a[`VisionImageMetadata`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImageMetadata)object that specifies the orientation of the image data contained in the`CMSampleBufferRef`buffer.

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
2. Create a`VisionImage`object using the`CMSampleBufferRef`object and the rotation metadata:  

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

To label objects in an image, pass the`VisionImage`object to the`VisionImageLabeler`'s`processImage()`method.

<br />

1. First, get an instance of`VisionImageLabeler`:

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

2. Then, pass the image to the`processImage()`method:

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

If image labeling succeeds, an array of`VisionImageLabel`objects will be passed to the completion handler. From each object, you can get information about a feature recognized in the image.

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

## Next steps

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml/ios/secure-api-key).