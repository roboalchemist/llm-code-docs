# Source: https://firebase.google.com/docs/ml/ios/label-images-with-automl.md.txt

After you [train your own model using AutoML Vision Edge](https://firebase.google.com/docs/ml/train-image-labeler),
you can use it in your app to label images.

> [!WARNING]
> Firebase ML's AutoML Vision Edge features are deprecated. Consider using [Vertex AI](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide) to automatically train ML models, which you can either [export as TensorFlow
> Lite models](https://cloud.google.com/vertex-ai/docs/export/export-edge-model) for on-device use or [deploy for cloud-based
> inference](https://cloud.google.com/vertex-ai/docs/predictions/overview).

There are two ways to integrate models trained from AutoML Vision Edge. You can
bundle the model by copying the model's files into your Xcode project, or you
can dynamically download it from Firebase.

| Model bundling options ||
|---|---|
| Bundled in your app | - The model is part of the bundle - The model is available immediately, even when the Apple device is offline - No need for a Firebase project |
| Hosted with Firebase | - Host the model by uploading it to [Firebase Machine Learning](https://firebase.google.com/docs/ml) - Reduces app bundle size - The model is downloaded on demand - Push model updates without republishing your app - Easy A/B testing with [Firebase Remote Config](https://firebase.google.com/docs/remote-config) - Requires a Firebase project |

> [!NOTE]
> **Note:** ML Kit iOS APIs only run on 64-bit devices. If you build your app with 32-bit support, check the device's architecture before using this API.

## Before you begin

1. Include the ML Kit libraries in your Podfile:

   For bundling a model with your app:

       pod 'GoogleMLKit/ImageLabelingCustom'

   For dynamically downloading a model from Firebase, add the `LinkFirebase`
   dependency:

       pod 'GoogleMLKit/ImageLabelingCustom'
       pod 'GoogleMLKit/LinkFirebase'

2. After you install or update your project's Pods, open your Xcode project
   using its `.xcworkspace`. ML Kit is supported in Xcode version 12.2 or
   higher.

3. **If you want to download a model** , make sure you
   [add Firebase to your Android project](https://firebase.google.com/docs/ios/setup),
   if you have not already done so. This is not required when you bundle the
   model.

## 1. Load the model

### Configure a local model source

To bundle the model with your app:

1. Extract the model and its metadata from the zip archive you downloaded
   from Firebase console into a folder:

       your_model_directory
         |____dict.txt
         |____manifest.json
         |____model.tflite

   All three files must be in the same folder. We recommend you use the files
   as you downloaded them, without modification (including the file names).
2. Copy the folder to your Xcode project, taking care to select
   **Create folder references** when you do so. The model file and metadata
   will be included in the app bundle and available to ML Kit.

3. Create `LocalModel` object, specifying the path to the
   model manifest file:

   ### Swift

       guard let manifestPath = Bundle.main.path(
           forResource: "manifest",
           ofType: "json",
           inDirectory: "your_model_directory"
       ) else { return true }
       let localModel = LocalModel(manifestPath: manifestPath)

   ### Objective-C

       NSString *manifestPath =
           [NSBundle.mainBundle pathForResource:@"manifest"
                                         ofType:@"json"
                                    inDirectory:@"your_model_directory"];
       MLKLocalModel *localModel =
           [[MLKLocalModel alloc] initWithManifestPath:manifestPath];

### Configure a Firebase-hosted model source

To use the remotely-hosted model, create an `CustomRemoteModel`
object, specifying the name you assigned the model when you published it:

### Swift

    // Initialize the model source with the name you assigned in
    // the Firebase console.
    let remoteModelSource = FirebaseModelSource(name: "your_remote_model")
    let remoteModel = CustomRemoteModel(remoteModelSource: remoteModelSource)

### Objective-C

    // Initialize the model source with the name you assigned in
    // the Firebase console.
    MLKFirebaseModelSource *firebaseModelSource =
        [[MLKFirebaseModelSource alloc] initWithName:@"your_remote_model"];
    MLKCustomRemoteModel *remoteModel =
        [[MLKCustomRemoteModel alloc] initWithRemoteModelSource:firebaseModelSource];

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

    MLKModelDownloadConditions *downloadConditions =
        [[MLKModelDownloadConditions alloc] initWithAllowsCellularAccess:YES
                                             allowsBackgroundDownloading:YES];

    NSProgress *downloadProgress =
        [[MLKModelManager modelManager] downloadRemoteModel:remoteModel
                                                 conditions:downloadConditions];

Many apps start the download task in their initialization code, but you
can do so at any point before you need to use the model.

### Create an image labeler from your model

After you configure your model sources, create an `ImageLabeler` object from one
of them.

If you only have a locally-bundled model, just create a labeler from your
`LocalModel` object and configure the confidence score
threshold you want to require (see [Evaluate your model](https://firebase.google.com/docs/ml/train-image-labeler#evaluate_the_model)):

### Swift

    let options = CustomImageLabelerOptions(localModel: localModel)
    options.confidenceThreshold = NSNumber(value: 0.0)  // Evaluate your model in the Cloud console
                                                        // to determine an appropriate value.
    let imageLabeler = ImageLabeler.imageLabeler(options)

### Objective-C

    CustomImageLabelerOptions *options =
        [[CustomImageLabelerOptions alloc] initWithLocalModel:localModel];
    options.confidenceThreshold = @(0.0f);  // Evaluate your model in the Cloud console
                                            // to determine an appropriate value.
    MLKImageLabeler *imageLabeler =
        [MLKImageLabeler imageLabelerWithOptions:options];

If you have a remotely-hosted model, you will have to check that it has been
downloaded before you run it. You can check the status of the model download
task using the model manager's `isModelDownloaded(remoteModel:)` method.

Although you only have to confirm this before running the labeler, if you
have both a remotely-hosted model and a locally-bundled model, it might make
sense to perform this check when instantiating the `ImageLabeler`: create a
labeler from the remote model if it's been downloaded, and from the local model
otherwise.

### Swift

    var options: CustomImageLabelerOptions
    if (ModelManager.modelManager().isModelDownloaded(remoteModel)) {
      options = CustomImageLabelerOptions(remoteModel: remoteModel)
    } else {
      options = CustomImageLabelerOptions(localModel: localModel)
    }
    options.confidenceThreshold = NSNumber(value: 0.0)  // Evaluate your model in the Firebase console
                                                        // to determine an appropriate value.
    let imageLabeler = ImageLabeler.imageLabeler(options: options)

### Objective-C

    MLKCustomImageLabelerOptions *options;
    if ([[MLKModelManager modelManager] isModelDownloaded:remoteModel]) {
      options = [[MLKCustomImageLabelerOptions alloc] initWithRemoteModel:remoteModel];
    } else {
      options = [[MLKCustomImageLabelerOptions alloc] initWithLocalModel:localModel];
    }
    options.confidenceThreshold = @(0.0f);  // Evaluate your model in the Firebase console
                                            // to determine an appropriate value.
    MLKImageLabeler *imageLabeler =
        [MLKImageLabeler imageLabelerWithOptions:options];

If you only have a remotely-hosted model, you should disable model-related
functionality---for example, gray-out or hide part of your UI---until
you confirm the model has been downloaded.

You can get the model download status by attaching observers to the default
Notification Center. Be sure to use a weak reference to `self` in the observer
block, since downloads can take some time, and the originating object can be
freed by the time the download finishes. For example:

### Swift

    NotificationCenter.default.addObserver(
        forName: .mlkitMLModelDownloadDidSucceed,
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
        forName: .mlkitMLModelDownloadDidFail,
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

### Objective-C

    __weak typeof(self) weakSelf = self;

    [NSNotificationCenter.defaultCenter
        addObserverForName:MLKModelDownloadDidSucceedNotification
                    object:nil
                     queue:nil
                usingBlock:^(NSNotification *_Nonnull note) {
                  if (weakSelf == nil | note.userInfo == nil) {
                    return;
                  }
                  __strong typeof(self) strongSelf = weakSelf;

                  MLKRemoteModel *model = note.userInfo[MLKModelDownloadUserInfoKeyRemoteModel];
                  if ([model.name isEqualToString:@"your_remote_model"]) {
                    // The model was downloaded and is available on the device
                  }
                }];

    [NSNotificationCenter.defaultCenter
        addObserverForName:MLKModelDownloadDidFailNotification
                    object:nil
                     queue:nil
                usingBlock:^(NSNotification *_Nonnull note) {
                  if (weakSelf == nil | note.userInfo == nil) {
                    return;
                  }
                  __strong typeof(self) strongSelf = weakSelf;

                  NSError *error = note.userInfo[MLKModelDownloadUserInfoKeyError];
                }];

## 2. Prepare the input image

Create a [`VisionImage`](https://developers.google.com/ml-kit/reference/swift/mlkitvision/api/reference/Classes/VisionImage) object using a `UIImage` or a
`CMSampleBufferRef`.

If you use a `UIImage`, follow these steps:

- Create a `VisionImage` object with the `UIImage`. Make sure to specify the correct `.orientation`.

  #### Swift

  ```swift
  let image = VisionImage(image: uiImage)
  visionImage.orientation = image.imageOrientation
  ```

  #### Objective-C

  ```objective-c
  MLKVisionImage *visionImage = [[MLKVisionImage alloc] initWithImage:image];
  visionImage.orientation = image.imageOrientation;
  ```

If you use a `CMSampleBufferRef`, follow these steps:

- Specify the orientation of the image data contained in the
  `CMSampleBufferRef` buffer.

  To get the image orientation:

  #### Swift

  ```swift
  func imageOrientation(
    deviceOrientation: UIDeviceOrientation,
    cameraPosition: AVCaptureDevice.Position
  ) -> UIImage.Orientation {
    switch deviceOrientation {
    case .portrait:
      return cameraPosition == .front ? .leftMirrored : .right
    case .landscapeLeft:
      return cameraPosition == .front ? .downMirrored : .up
    case .portraitUpsideDown:
      return cameraPosition == .front ? .rightMirrored : .left
    case .landscapeRight:
      return cameraPosition == .front ? .upMirrored : .down
    case .faceDown, .faceUp, .unknown:
      return .up
    }
  }
        
  ```

  #### Objective-C

  ```objective-c
  - (UIImageOrientation)
    imageOrientationFromDeviceOrientation:(UIDeviceOrientation)deviceOrientation
                           cameraPosition:(AVCaptureDevicePosition)cameraPosition {
    switch (deviceOrientation) {
      case UIDeviceOrientationPortrait:
        return position == AVCaptureDevicePositionFront ? UIImageOrientationLeftMirrored
                                                        : UIImageOrientationRight;

      case UIDeviceOrientationLandscapeLeft:
        return position == AVCaptureDevicePositionFront ? UIImageOrientationDownMirrored
                                                        : UIImageOrientationUp;
      case UIDeviceOrientationPortraitUpsideDown:
        return position == AVCaptureDevicePositionFront ? UIImageOrientationRightMirrored
                                                        : UIImageOrientationLeft;
      case UIDeviceOrientationLandscapeRight:
        return position == AVCaptureDevicePositionFront ? UIImageOrientationUpMirrored
                                                        : UIImageOrientationDown;
      case UIDeviceOrientationUnknown:
      case UIDeviceOrientationFaceUp:
      case UIDeviceOrientationFaceDown:
        return UIImageOrientationUp;
    }
  }
        
  ```
- Create a `VisionImage` object using the `CMSampleBufferRef` object and orientation:

  #### Swift

  ```swift
  let image = VisionImage(buffer: sampleBuffer)
  image.orientation = imageOrientation(
    deviceOrientation: UIDevice.current.orientation,
    cameraPosition: cameraPosition)
  ```

  #### Objective-C

  ```objective-c
   MLKVisionImage *image = [[MLKVisionImage alloc] initWithBuffer:sampleBuffer];
   image.orientation =
     [self imageOrientationFromDeviceOrientation:UIDevice.currentDevice.orientation
                                  cameraPosition:cameraPosition];
  ```

## 3. Run the image labeler

Asynchronously:

### Swift

    imageLabeler.process(image) { labels, error in
        guard error == nil, let labels = labels, !labels.isEmpty else {
            // Handle the error.
            return
        }
        // Show results.
    }

### Objective-C

    [imageLabeler
        processImage:image
          completion:^(NSArray<MLKImageLabel *> *_Nullable labels,
                       NSError *_Nullable error) {
            if (label.count == 0) {
                // Handle the error.
                return;
            }
            // Show results.
         }];

Synchronously:

### Swift

    var labels: [ImageLabel]
    do {
        labels = try imageLabeler.results(in: image)
    } catch let error {
        // Handle the error.
        return
    }
    // Show results.

### Objective-C

    NSError *error;
    NSArray<MLKImageLabel *> *labels =
        [imageLabeler resultsInImage:image error:&error];
    // Show results or handle the error.

## 4. Get information about labeled objects

If the image labeling operation succeeds, it returns an array of
[`ImageLabel`](https://developers.google.com/android/reference/com/google/mlkit/vision/label/ImageLabel). Each `ImageLabel` represents something that was
labeled in the image. You can get each label's text description (if available in
the metadata of the TensorFlow Lite model file), confidence score, and index.
For example:

### Swift

    for label in labels {
      let labelText = label.text
      let confidence = label.confidence
      let index = label.index
    }

### Objective-C

    for (MLKImageLabel *label in labels) {
      NSString *labelText = label.text;
      float confidence = label.confidence;
      NSInteger index = label.index;
    }

## Tips to improve real-time performance

If you want to label images in a real-time application, follow these
guidelines to achieve the best framerates:

- Throttle calls to the detector. If a new video frame becomes available while the detector is running, drop the frame.
- If you are using the output of the detector to overlay graphics on the input image, first get the result, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame. See the [previewOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Controllers/FIRVideoCamViewController.m#L856) and [FIRDetectionOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Views/FIRDetectionOverlayView.m) classes in the showcase sample app for an example.