# Source: https://firebase.google.com/docs/ml-kit/android/detect-objects.md.txt

# Source: https://firebase.google.com/docs/ml-kit/ios/detect-objects.md.txt

| This page describes an old version of the Object Detection and Tracking API, which was part of ML Kit for Firebase. Development of this API has been moved to the standalone ML Kit SDK, which you can use with or without Firebase.[Learn more](https://developers.google.com/ml-kit/migration).
|
| See[Detect and track objects with ML Kit on iOS](https://developers.google.com/ml-kit/vision/object-detection/ios)for the latest documentation.

<br />

You can use ML Kit to detect and track objects across frames of video.

When you pass ML Kit images, ML Kit returns, for each image, a list of up to five detected objects and their position in the image. When detecting objects in video streams, every object has an ID that you can use to track the object across images. You can also optionally enable coarse object classification, which labels objects with broad category descriptions.

<br />

## Before you begin

1. If you have not already added Firebase to your app, do so by following the steps in the[getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:  

   ```
   pod 'Firebase/MLVision', '6.25.0'
   pod 'Firebase/MLVisionObjectDetection', '6.25.0'
   ```
   After you install or update your project's Pods, be sure to open your Xcode project using its`.xcworkspace`.
3. In your app, import Firebase:  

   #### Swift

   ```swift
   import Firebase
   ```

   #### Objective-C

   ```objective-c
   @import Firebase;
   ```

<br />

| **Note:** ML Kit's object detection and tracking API only runs on 64-bit devices. If you build your app with 32-bit support, check the device's architecture before using this API.

## 1. Configure the object detector

To start detecting and tracking objects, first create an instance of`VisionObjectDetector`, optionally specifying any detector settings you want to change from the default.

1. Configure the object detector for your use case with a`VisionObjectDetectorOptions`object. You can change the following settings:

   |                                                                                                                                                                                                                                                                                                                                                                                                                                                          Object Detector Settings                                                                                                                                                                                                                                                                                                                                                                                                                                                          ||
   |-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | Detection mode                    | `.stream`(default) \|`.singleImage` In stream mode (default), the object detector runs with very low latency, but might produce incomplete results (such as unspecified bounding boxes or category) on the first few invocations of the detector. Also, in stream mode, the detector assigns tracking IDs to objects, which you can use to track objects across frames. Use this mode when you want to track objects, or when low latency is important, such as when processing video streams in real time. In single image mode, the object detector waits until a detected object's bounding box and (if you enabled classification) category are available before returning a result. As a consequence, detection latency is potentially higher. Also, in single image mode, tracking IDs are not assigned. Use this mode if latency isn't critical and you don't want to deal with partial results. |
   | Detect and track multiple objects | `false`(default) \|`true` Whether to detect and track up to five objects or only the most prominent object (default).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | Classify objects                  | `false`(default) \|`true` Whether or not to classify detected objects into coarse categories. When enabled, the object detector classifies objects into the following categories: fashion goods, food, home goods, places, plants, and unknown.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

   The object detection and tracking API is optimized for these two core use cases:
   - Live detection and tracking of the most prominent object in the camera viewfinder
   - Detection of multiple objects in a static image

   To configure the API for these use cases:  

   ### Swift

       // Live detection and tracking
       let options = VisionObjectDetectorOptions()
       options.detectorMode = .stream
       options.shouldEnableMultipleObjects = false
       options.shouldEnableClassification = true  // Optional

       // Multiple object detection in static images
       let options = VisionObjectDetectorOptions()
       options.detectorMode = .singleImage
       options.shouldEnableMultipleObjects = true
       options.shouldEnableClassification = true  // Optional

   ### Objective-C

       // Live detection and tracking
       FIRVisionObjectDetectorOptions *options = [[FIRVisionObjectDetectorOptions alloc] init];
       options.detectorMode = FIRVisionObjectDetectorModeStream;
       options.shouldEnableMultipleObjects = NO;
       options.shouldEnableClassification = YES;  // Optional

       // Multiple object detection in static images
       FIRVisionObjectDetectorOptions *options = [[FIRVisionObjectDetectorOptions alloc] init];
       options.detectorMode = FIRVisionObjectDetectorModeSingleImage;
       options.shouldEnableMultipleObjects = YES;
       options.shouldEnableClassification = YES;  // Optional

2. Get an instance of`FirebaseVisionObjectDetector`:

   ### Swift

       let objectDetector = Vision.vision().objectDetector()

       // Or, to change the default settings:
       let objectDetector = Vision.vision().objectDetector(options: options)

   ### Objective-C

       FIRVisionObjectDetector *objectDetector = [[FIRVision vision] objectDetector];

       // Or, to change the default settings:
       FIRVisionObjectDetector *objectDetector = [[FIRVision vision] objectDetectorWithOptions:options];

## 2. Run the object detector

To detect and track objects, do the following for each image or frame of video. If you enabled stream mode, you must create`VisionImage`objects from`CMSampleBufferRef`s.

1. Create a[`VisionImage`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionImage)object using a`UIImage`or a`CMSampleBufferRef`.

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
2. Pass the`VisionImage`to one of the object detector's image processing methods. You can either use the asynchronous`process(image:)`method or the synchronous`results()`method.

   To detect objects asynchronously:  

   ### Swift

       objectDetector.process(image) { detectedObjects, error in
         guard error == nil else {
           // Error.
           return
         }
         guard let detectedObjects = detectedObjects, !detectedObjects.isEmpty else {
           // No objects detected.
           return
         }

         // Success. Get object info here.
         // ...
       }

   ### Objective-C

       [objectDetector processImage:image
                         completion:^(NSArray<FIRVisionObject *> * _Nullable objects,
                                      NSError * _Nullable error) {
                           if (error == nil) {
                             return;
                           }
                           if (objects == nil | objects.count == 0) {
                             // No objects detected.
                             return;
                           }

                           // Success. Get object info here.
                           // ...
                         }];

   To detect objects synchronously:  

   ### Swift

       var results: [VisionObject]? = nil
       do {
         results = try objectDetector.results(in: image)
       } catch let error {
         print("Failed to detect object with error: \(error.localizedDescription).")
         return
       }
       guard let detectedObjects = results, !detectedObjects.isEmpty else {
         print("Object detector returned no results.")
         return
       }

       // ...

   ### Objective-C

       NSError *error;
       NSArray<FIRVisionObject *> *objects = [objectDetector resultsInImage:image
                                                                      error:&error];
       if (error == nil) {
         return;
       }
       if (objects == nil | objects.count == 0) {
         // No objects detected.
         return;
       }

       // Success. Get object info here.
       // ...

3. If the call to the image processor succeeds, it either passes a list of`VisionObject`s to the completion handler or returns the list, depending on whether you called the asynchronous or synchronous method.

   | **Note:** In streaming mode, the object detector might need to process 30 or more frames, depending on device performance, before it detects the first object.

   Each`VisionObject`contains the following properties:

   |--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
   | `frame`                  | A`CGRect`indicating the position of the object in the image.                                                                                                         |
   | `trackingID`             | An integer that identifies the object across images. Nil in single image mode.                                                                                       |
   | `classificationCategory` | The coarse category of the object. If the object detector doesn't have classification enabled, this is always`.unknown`.                                             |
   | `confidence`             | The confidence value of the object classification. If the object detector doesn't have classification enabled, or the object is classified as unknown, this is`nil`. |

   ### Swift

       // detectedObjects contains one item if multiple object detection wasn't enabled.
       for obj in detectedObjects {
         let bounds = obj.frame
         let id = obj.trackingID

         // If classification was enabled:
         let category = obj.classificationCategory
         let confidence = obj.confidence
       }

   ### Objective-C

       // The list of detected objects contains one item if multiple
       // object detection wasn't enabled.
       for (FIRVisionObject *obj in objects) {
         CGRect bounds = obj.frame;
         if (obj.trackingID) {
           NSInteger id = obj.trackingID.integerValue;
         }

         // If classification was enabled:
         FIRVisionObjectCategory category = obj.classificationCategory;
         float confidence = obj.confidence.floatValue;
       }

## Improving usability and performance

For the best user experience, follow these guidelines in your app:

- Successful object detection depends on the object's visual complexity. Objects with a small number of visual features might need to take up a larger part of the image to be detected. You should provide users with guidance on capturing input that works well with the kind of objects you want to detect.
- When using classification, if you want to detect objects that don't fall cleanly into the supported categories, implement special handling for unknown objects.

Also, check out the \[ML Kit Material Design showcase app\]\[showcase-link\]{: .external } and the Material Design[Patterns for machine learning-powered features](https://material.io/collections/machine-learning/)collection.

When using streaming mode in a real-time application, follow these guidelines to achieve the best framerates:

- Don't use multiple object detection in streaming mode, as most devices won't be able to produce adequate framerates.

- Disable classification if you don't need it.

- Throttle calls to the detector. If a new video frame becomes available while the detector is running, drop the frame.
- If you are using the output of the detector to overlay graphics on the input image, first get the result from ML Kit, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame. See the[previewOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Controllers/FIRVideoCamViewController.m#L856)and[FIRDetectionOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Views/FIRDetectionOverlayView.m)classes in the showcase sample app for an example.