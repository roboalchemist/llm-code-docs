# Source: https://firebase.google.com/docs/ml/android/recognize-landmarks-deprecated.md.txt

# Source: https://firebase.google.com/docs/ml/ios/recognize-landmarks-deprecated.md.txt

| This page describes an old version of recognizing well-known landmarks in images using the deprecatedFirebase MLVision SDK. As an alternative, you may[call Cloud Vision APIs using Firebase Auth and Callable Functions](https://firebase.google.com/docs/ml/ios/recognize-landmarks)to allow only users logged into your app to access the API.

You can useFirebase MLto recognize well-known landmarks in an image.
| Use of the Cloud Vision APIs is subject to the[Google Cloud Platform License Agreement](https://cloud.google.com/terms/)and[Service Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the[Pricing](https://cloud.google.com/vision/pricing)page.

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

## Configure the landmark detector

By default, the Cloud detector uses the stable version of the model and returns up to 10 results. If you want to change either of these settings, specify them with a`VisionCloudDetectorOptions`object as in the following example:  

#### Swift

```swift
let options = VisionCloudDetectorOptions()
options.modelType = .latest
options.maxResults = 20https://github.com/firebase/quickstart-ios/blob/c7b9221ceaff346fd912ed071d4984eca32bfc4f/mlvision/MLVisionExample/ViewController.swift#L463-L465
```

#### Objective-C

```objective-c
  FIRVisionCloudDetectorOptions *options =
      [[FIRVisionCloudDetectorOptions alloc] init];
  options.modelType = FIRVisionCloudModelTypeLatest;
  options.maxResults = 20;
  
```

In the next step, pass the`VisionCloudDetectorOptions`object when you create the Cloud detector object.

## Run the landmark detector

To recognize landmarks in an image, pass the image as a`UIImage`or a`CMSampleBufferRef`to the`VisionCloudLandmarkDetector`'s`detect(in:)`method:

<br />

1. Get an instance of[`VisionCloudLandmarkDetector`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmarkDetector):  

   #### Swift

   ```swift
   lazy var vision = Vision.vision()

   let cloudDetector = vision.cloudLandmarkDetector(options: options)
   // Or, to use the default settings:
   // let cloudDetector = vision.cloudLandmarkDetector()  
   https://github.com/firebase/quickstart-ios/blob/c7b9221ceaff346fd912ed071d4984eca32bfc4f/mlvision/MLVisionExample/ViewController.swift#L469-L471
   ```

   #### Objective-C

   ```objective-c
   FIRVision *vision = [FIRVision vision];
   FIRVisionCloudLandmarkDetector *landmarkDetector = [vision cloudLandmarkDetector];
   // Or, to change the default settings:
   // FIRVisionCloudLandmarkDetector *landmarkDetector =
   //     [vision cloudLandmarkDetectorWithOptions:options];
   ```
2. In order to call Cloud Vision, the image must be formatted as a base64-encoded string. To process a`UIImage`:  

   #### Swift

   ```swift
   guard let imageData = uiImage.jpegData(compressionQuality: 1.0) else { return }
   let base64encodedImage = imageData.base64EncodedString()
   ```

   #### Objective-C

   ```objective-c
   NSData *imageData = UIImageJPEGRepresentation(uiImage, 1.0f);
   NSString *base64encodedImage =
     [imageData base64EncodedStringWithOptions:NSDataBase64Encoding76CharacterLineLength];
   ```
3. Then, pass the image to the`detect(in:)`method:  

   #### Swift

   ```swift
   cloudDetector.detect(in: visionImage) { landmarks, error in
     guard error == nil, let landmarks = landmarks, !landmarks.isEmpty else {
       // ...
       return
     }

     // Recognized landmarks
     // ...
   }https://github.com/firebase/quickstart-ios/blob/c7b9221ceaff346fd912ed071d4984eca32bfc4f/mlvision/MLVisionExample/ViewController.swift#L475-L504
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

If landmark recognition succeeds, an array of[`VisionCloudLandmark`](https://firebase.google.com/docs/reference/swift/firebasemlvision/api/reference/Classes/VisionCloudLandmark)objects will be passed to the completion handler. From each object, you can get information about a landmark recognized in the image.

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

- Before you deploy to production an app that uses a Cloud API, you should take some additional steps to[prevent and mitigate the effect of unauthorized API access](https://firebase.google.com/docs/ml/ios/secure-api-key).