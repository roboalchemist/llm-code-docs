# Source: https://firebase.google.com/docs/ml-kit/ios/label-images-with-automl.md.txt

> [!CAUTION]
> This page describes an old version of the AutoML Vision Edge API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Label images with an AutoML-trained model on iOS](https://developers.google.com/ml-kit/vision/auto-ml-vision-edge/ios)
> for the latest documentation.


After you [train your own
model using AutoML Vision Edge](https://firebase.google.com/docs/ml-kit/train-image-labeler), you can use it in your app to label
images.

<br />

## Before you begin

<br />

<br />

1. If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:

   ```
   pod 'Firebase/MLVision', '6.25.0'
   pod 'Firebase/MLVisionAutoML', '6.25.0'
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

## 1. Load the model

ML Kit runs your AutoML-generated models on the device. However, you can
configure ML Kit to load your model either remotely from Firebase, from
local storage, or both.

By hosting the model on Firebase, you can update the model without releasing
a new app version, and you can use Remote Config and A/B Testing to
dynamically serve different models to different sets of users.

If you choose to only provide the model by hosting it with Firebase, and not
bundle it with your app, you can reduce the initial download size of your app.
Keep in mind, though, that if the model is not bundled with your app, any
model-related functionality will not be available until your app downloads the
model for the first time.

By bundling your model with your app, you can ensure your app's ML features
still work when the Firebase-hosted model isn't available.

### Configure a Firebase-hosted model source

To use the remotely-hosted model, create an `AutoMLRemoteModel` object,
specifying the name you assigned the model when you published it:

### Swift

    let remoteModel = AutoMLRemoteModel(
        name: "your_remote_model"  // The name you assigned in the Firebase console.
    )

### Objective-C

    FIRAutoMLRemoteModel *remoteModel = [[FIRAutoMLRemoteModel alloc]
        initWithName:@"your_remote_model"];  // The name you assigned in the Firebase console.

Then, start the model download task, specifying the conditions under which
you want to allow downloading. If the model isn't on the device, or if a newer
version of the model is available, the task will asynchronously download the
model from Firebase:

### Swift

    let downloadConditions = ModelDownloadConditions(
      allowsCellularAccess: true,
      allowsBackgroundDownloading: true
    )

    let downloadProgress = ModelManager.modelManager().download(
      remoteModel,
      conditions: downloadConditions
    )

### Objective-C

    FIRModelDownloadConditions *downloadConditions =
        [[FIRModelDownloadConditions alloc] initWithAllowsCellularAccess:YES
                                             allowsBackgroundDownloading:YES];

    NSProgress *downloadProgress =
        [[FIRModelManager modelManager] downloadRemoteModel:remoteModel
                                                 conditions:downloadConditions];

Many apps start the download task in their initialization code, but you
can do so at any point before you need to use the model.

### Configure a local model source

To bundle the model with your app:

1. Extract the model and its metadata from the zip archive you downloaded from Firebase console into a folder:

   ```
   your_model_directory
     |____dict.txt
     |____manifest.json
     |____model.tflite
   ```
   All three files must be in the same folder. We recommend you use the files as you downloaded them, without modification (including the file names).
2. Copy the folder to your Xcode project, taking care to select **Create folder references** when you do so. The model file and metadata will be included in the app bundle and available to ML Kit.
3. Create an `AutoMLLocalModel` object, specifying the path to the model manifest file:

   ### Swift

       guard let manifestPath = Bundle.main.path(
           forResource: "manifest",
           ofType: "json",
           inDirectory: "your_model_directory"
       ) else { return true }
       let localModel = AutoMLLocalModel(manifestPath: manifestPath)

   ### Objective-C

       NSString *manifestPath = [NSBundle.mainBundle pathForResource:@"manifest"
                                                              ofType:@"json"
                                                         inDirectory:@"your_model_directory"];
       FIRAutoMLLocalModel *localModel = [[FIRAutoMLLocalModel alloc] initWithManifestPath:manifestPath];

### Create an image labeler from your model

After you configure your model sources, create a `VisionImageLabeler` object
from one of them.

If you only have a locally-bundled model, just create a labeler from your
`AutoMLLocalModel` object and configure the confidence score threshold you want
to require (see [Evaluate your model](https://firebase.google.com/docs/ml-kit/train-image-labeler#evaluate_the_model)):

### Swift

    let options = VisionOnDeviceAutoMLImageLabelerOptions(localModel: localModel)
    options.confidenceThreshold = 0  // Evaluate your model in the Firebase console
                                     // to determine an appropriate value.
    let labeler = Vision.vision().onDeviceAutoMLImageLabeler(options: options)

### Objective-C

    FIRVisionOnDeviceAutoMLImageLabelerOptions *options =
        [[FIRVisionOnDeviceAutoMLImageLabelerOptions alloc] initWithLocalModel:localModel];
    options.confidenceThreshold = 0;  // Evaluate your model in the Firebase console
                                      // to determine an appropriate value.
    FIRVisionImageLabeler *labeler =
        [[FIRVision vision] onDeviceAutoMLImageLabelerWithOptions:options];

If you have a remotely-hosted model, you will have to check that it has been
downloaded before you run it. You can check the status of the model download
task using the model manager's `isModelDownloaded(remoteModel:)` method.

Although you only have to confirm this before running the labeler, if you
have both a remotely-hosted model and a locally-bundled model, it might make
sense to perform this check when instantiating the `VisionImageLabeler`: create
a labeler from the remote model if it's been downloaded, and from the local
model otherwise.

### Swift

    var options: VisionOnDeviceAutoMLImageLabelerOptions?
    if (ModelManager.modelManager().isModelDownloaded(remoteModel)) {
      options = VisionOnDeviceAutoMLImageLabelerOptions(remoteModel: remoteModel)
    } else {
      options = VisionOnDeviceAutoMLImageLabelerOptions(localModel: localModel)
    }
    options.confidenceThreshold = 0  // Evaluate your model in the Firebase console
                                     // to determine an appropriate value.
    let labeler = Vision.vision().onDeviceAutoMLImageLabeler(options: options)

### Objective-C

    VisionOnDeviceAutoMLImageLabelerOptions *options;
    if ([[FIRModelManager modelManager] isModelDownloaded:remoteModel]) {
      options = [[FIRVisionOnDeviceAutoMLImageLabelerOptions alloc] initWithRemoteModel:remoteModel];
    } else {
      options = [[FIRVisionOnDeviceAutoMLImageLabelerOptions alloc] initWithLocalModel:localModel];
    }
    options.confidenceThreshold = 0.0f;  // Evaluate your model in the Firebase console
                                         // to determine an appropriate value.
    FIRVisionImageLabeler *labeler = [[FIRVision vision] onDeviceAutoMLImageLabelerWithOptions:options];

If you only have a remotely-hosted model, you should disable model-related
functionality---for example, gray-out or hide part of your UI---until
you confirm the model has been downloaded.

You can get the model download status by attaching observers to the default
Notification Center. Be sure to use a weak reference to `self` in the observer
block, since downloads can take some time, and the originating object can be
freed by the time the download finishes. For example:

### Swift

```swift
NotificationCenter.default.addObserver(
    forName: .firebaseMLModelDownloadDidSucceed,
    object: nil,
    queue: nil
) { [weak self] notification in
    guard let strongSelf = self,
        let userInfo = notification.userInfo,
        let model = userInfo[ModelDownloadUserInfoKey.remoteModel.rawValue]
            as? RemoteModel,
        model.name == "your_remote_model"
        else { return }
    // The model was downloaded and is available on the device
}

NotificationCenter.default.addObserver(
    forName: .firebaseMLModelDownloadDidFail,
    object: nil,
    queue: nil
) { [weak self] notification in
    guard let strongSelf = self,
        let userInfo = notification.userInfo,
        let model = userInfo[ModelDownloadUserInfoKey.remoteModel.rawValue]
            as? RemoteModel
        else { return }
    let error = userInfo[ModelDownloadUserInfoKey.error.rawValue]
    // ...
}
```

### Objective-C

```objective-c
__weak typeof(self) weakSelf = self;

[NSNotificationCenter.defaultCenter
    addObserverForName:FIRModelDownloadDidSucceedNotification
                object:nil
                 queue:nil
            usingBlock:^(NSNotification *_Nonnull note) {
              if (weakSelf == nil | note.userInfo == nil) {
                return;
              }
              __strong typeof(self) strongSelf = weakSelf;

              FIRRemoteModel *model = note.userInfo[FIRModelDownloadUserInfoKeyRemoteModel];
              if ([model.name isEqualToString:@"your_remote_model"]) {
                // The model was downloaded and is available on the device
              }
            }];

[NSNotificationCenter.defaultCenter
    addObserverForName:FIRModelDownloadDidFailNotification
                object:nil
                 queue:nil
            usingBlock:^(NSNotification *_Nonnull note) {
              if (weakSelf == nil | note.userInfo == nil) {
                return;
              }
              __strong typeof(self) strongSelf = weakSelf;

              NSError *error = note.userInfo[FIRModelDownloadUserInfoKeyError];
            }];
```

## 2. Prepare the input image

Then, for each image you want to label, create a `VisionImage` object using one
of the options described in this section and pass it to an instance of
`VisionImageLabeler` (described in the next section).

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

## 3. Run the image labeler

To label objects in an image, pass the `VisionImage` object to the
`VisionImageLabeler`'s `process()` method:

### Swift

    labeler.process(image) { labels, error in
        guard error == nil, let labels = labels else { return }

        // Task succeeded.
        // ...
    }

### Objective-C

    [labeler
        processImage:image
          completion:^(NSArray<FIRVisionImageLabel *> *_Nullable labels, NSError *_Nullable error) {
            if (error != nil || labels == nil) {
              return;
            }

            // Task succeeded.
            // ...
          }];

If image labeling succeeds, an array of `VisionImageLabel` objects will be
passed to the completion handler. From each object, you can get information
about a feature recognized in the image.

For example:

### Swift

    for label in labels {
        let labelText = label.text
        let confidence = label.confidence
    }

### Objective-C

    for (FIRVisionImageLabel *label in labels) {
      NSString *labelText = label.text;
      NSNumber *confidence = label.confidence;
    }

> [!NOTE]
> **Note:** when using an AutoML-trained model, `VisionImageLabel.entityID` from the returned labels is always `nil`.

## Tips to improve real-time performance

- Throttle calls to the detector. If a new video frame becomes available while the detector is running, drop the frame.
- If you are using the output of the detector to overlay graphics on the input image, first get the result from ML Kit, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame. See the [previewOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Controllers/FIRVideoCamViewController.m#L856) and [FIRDetectionOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Views/FIRDetectionOverlayView.m) classes in the showcase sample app for an example.