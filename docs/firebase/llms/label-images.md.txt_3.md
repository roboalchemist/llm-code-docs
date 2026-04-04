# Source: https://firebase.google.com/docs/ml/ios/label-images.md.txt

> [!NOTE]
>
> The Firebase ML Vision SDK for labeling objects in an image is
> now deprecated
> [(See the
> outdated docs here).](https://firebase.google.com/docs/ml/ios/label-images-deprecated)
> This page describes how, as an alternative to the deprecated SDK, you can
> call Cloud Vision APIs using Firebase Auth and Firebase Functions to allow
> only authenticated users to access the API.


In order to call a Google Cloud API from your app, you need to create an intermediate
REST API that handles authorization and protects secret values such as API keys. You then need to
write code in your mobile app to authenticate to and communicate with this intermediate service.


One way to create this REST API is by using Firebase Authentication and Functions, which gives you a managed, serverless gateway to
Google Cloud APIs that handles authentication and can be called from your mobile app with
pre-built SDKs.


This guide demonstrates how to use this technique to call the Cloud Vision API from your app.
This method will allow all authenticated users to access Cloud Vision billed services through your Cloud project, so
consider whether this auth mechanism is sufficient for your use case before proceeding.
Use of the Cloud Vision APIs is subject to the [Google Cloud Platform License
Agreement](https://cloud.google.com/terms/) and [Service
Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the [Pricing](https://cloud.google.com/vision/pricing) page.

> [!NOTE]
> **Looking for on-device image labeling?** Try the [standalone ML Kit library](https://developers.google.com/ml-kit/vision/image-labeling).

<br />

## Before you begin

<br />

### Configure your project

If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).

Use Swift Package Manager to install and manage Firebase dependencies.

> [!NOTE]
> Visit [our installation guide](https://firebase.google.com/docs/ios/installation-methods) to learn about the different ways you can add Firebase SDKs to your Apple project.

1. In Xcode, with your app project open, navigate to **File \> Add Packages**.
2. When prompted, add the Firebase Apple platforms SDK repository:

```
  https://github.com/firebase/firebase-ios-sdk.git
```

> [!NOTE]
> **Note:** New projects should use the default (latest) SDK version, but you can choose an older version if needed.

3. Choose the Firebase ML library.
4. Add the `-ObjC` flag to the *Other Linker Flags* section of your target's build settings.
5. When finished, Xcode will automatically begin resolving and downloading your dependencies in the background.


Next, perform some in-app setup:

1. In your app, import Firebase:

   #### Swift

   ```swift
   import FirebaseMLModelDownloader
   ```

   #### Objective-C

   ```objective-c
   @import FirebaseMLModelDownloader;
   ```


A few more configuration steps, and we're ready to go:

1. If you haven't already enabled Cloud-based APIs for your project, do so
   now:

   1. Open the [Firebase ML
      APIs page](https://console.firebase.google.com/project/_/ml/apis) in the Firebase console.
   2. If you haven't already upgraded your project to the
      [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), click **Upgrade** to do so. (You'll be
      prompted to upgrade only if your project isn't on the
      Blaze pricing plan.)

      Only projects on the Blaze pricing plan can use
      Cloud-based APIs.
   3. If Cloud-based APIs aren't already enabled, click **Enable Cloud-based APIs**.
2. Configure your existing Firebase API keys to disallow access to the Cloud Vision API:
   1. Open the [Credentials](https://console.cloud.google.com/apis/credentials?project=_) page of the Cloud console.
   2. For each API key in the list, open the editing view, and in the Key Restrictions section, add all of the available APIs *except* the Cloud Vision API to the list.

### Deploy the callable function

Next, deploy the Cloud Function you will use to bridge your app and the Cloud
Vision API. The `functions-samples` repository contains an example
you can use.

By default, accessing the Cloud Vision API through this function will allow
only authenticated users of your app access to the Cloud Vision API. You can
modify the function for different requirements.

To deploy the function:

1. Clone or download the [functions-samples repo](https://github.com/firebase/functions-samples) and change to the `Node-1st-gen/vision-annotate-image` directory:

       git clone https://github.com/firebase/functions-samples
       cd Node-1st-gen/vision-annotate-image

2. Install dependencies:

       cd functions
       npm install
       cd ..

3. If you don't have the Firebase CLI, [install it](https://firebase.google.com/docs/cli#setup_update_cli).
4. Initialize a Firebase project in the `vision-annotate-image` directory. When prompted, select your project in the list.

   ```
   firebase init
   ```
5. Deploy the function:

   ```
   firebase deploy --only functions:annotateImage
   ```

### Add Firebase Auth to your app

The callable function deployed above will reject any request from non-authenticated
users of your app. If you have not already done so, you will need to [add Firebase
Auth to your app.](https://firebase.google.com/docs/auth/ios/start#add_to_your_app)

### Add necessary dependencies to your app


Use Swift Package Manager to install the Cloud Functions for Firebase library.

Now you are ready to label images.

## 1. Prepare the input image

In order to call Cloud Vision, the image must be formatted as a base64-encoded string. To process a `UIImage`:

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

## 2. Invoke the callable function to label the image

To label objects in an image, invoke the callable function passing a [JSON Cloud Vision request](https://cloud.google.com/vision/docs/request#json_request_format).

<br />

1. First, initialize an instance of Cloud Functions:

   ### Swift

       lazy var functions = Functions.functions()

   ### Objective-C

       @property(strong, nonatomic) FIRFunctions *functions;

2. Create a request with [Type](https://cloud.google.com/vision/docs/reference/rest/v1/Feature#type) set to `LABEL_DETECTION`:

   ### Swift

       let requestData = [
         "image": ["content": base64encodedImage],
         "features": ["maxResults": 5, "type": "LABEL_DETECTION"]
       ]

   ### Objective-C

       NSDictionary *requestData = @{
         @"image": @{@"content": base64encodedImage},
         @"features": @{@"maxResults": @5, @"type": @"LABEL_DETECTION"}
       };

3. Finally, invoke the function:

   ### Swift

       do {
         let result = try await functions.httpsCallable("annotateImage").call(requestData)
         print(result)
       } catch {
         if let error = error as NSError? {
           if error.domain == FunctionsErrorDomain {
             let code = FunctionsErrorCode(rawValue: error.code)
             let message = error.localizedDescription
             let details = error.userInfo[FunctionsErrorDetailsKey]
           }
           // ...
         }
       }

   ### Objective-C

       [[_functions HTTPSCallableWithName:@"annotateImage"]
                                 callWithObject:requestData
                                     completion:^(FIRHTTPSCallableResult * _Nullable result, NSError * _Nullable error) {
               if (error) {
                 if ([error.domain isEqualToString:@"com.firebase.functions"]) {
                   FIRFunctionsErrorCode code = error.code;
                   NSString *message = error.localizedDescription;
                   NSObject *details = error.userInfo[@"details"];
                 }
                 // ...
               }
               // Function completed succesfully
               // Get information about labeled objects

             }];

## 3. Get information about labeled objects

If the image labeling operation succeeds, a JSON response of [BatchAnnotateImagesResponse](https://cloud.google.com/vision/docs/reference/rest/v1/BatchAnnotateImagesResponse) will be returned in the task's result. Each object in the `labelAnnotations` array represents something that was labeled in the image. For each label, you can get the label's text description, its [Knowledge Graph entity ID](https://developers.google.com/knowledge-graph/) (if available), and the confidence score of the match. For example:

<br />

### Swift

    if let labelArray = (result?.data as? [String: Any])?["labelAnnotations"] as? [[String:Any]] {
      for labelObj in labelArray {
        let text = labelObj["description"]
        let entityId = labelObj["mid"]
        let confidence = labelObj["score"]
      }
    }

### Objective-C

    NSArray *labelArray = result.data[@"labelAnnotations"];
    for (NSDictionary *labelObj in labelArray) {
      NSString *text = labelObj[@"description"];
      NSString *entityId = labelObj[@"mid"];
      NSNumber *confidence = labelObj[@"score"];
    }