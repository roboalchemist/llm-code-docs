# Source: https://firebase.google.com/docs/ml/android/detect-objects-with-automl.md.txt

# Source: https://firebase.google.com/docs/ml/ios/detect-objects-with-automl.md.txt

<br />

After you[train your own model using AutoML Vision Edge](https://firebase.google.com/docs/ml/train-object-detector), you can use it in your app to detect objects in images.
| Firebase ML's AutoML Vision Edge features are deprecated. Consider using[Vertex AI](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide)to automatically train ML models, which you can either[export as TensorFlow Lite models](https://cloud.google.com/vertex-ai/docs/export/export-edge-model)for on-device use or[deploy for cloud-based inference](https://cloud.google.com/vertex-ai/docs/predictions/overview).

There are two ways to integrate models trained from AutoML Vision Edge. You can bundle the model by copying the model's files into your Xcode project, or you can dynamically download it from Firebase.

|                                                                                                                                                                          Model bundling options                                                                                                                                                                          ||
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bundled in your app  | - The model is part of the bundle - The model is available immediately, even when the Apple device is offline - No need for a Firebase project                                                                                                                                                                                                     |
| Hosted with Firebase | - Host the model by uploading it to[Firebase Machine Learning](https://firebase.google.com/docs/ml) - Reduces app bundle size - The model is downloaded on demand - Push model updates without republishing your app - Easy A/B testing with[Firebase Remote Config](https://firebase.google.com/docs/remote-config) - Requires a Firebase project |

## Before you begin

1. **If you want to download a model** , make sure you[add Firebase to your Apple project](https://firebase.google.com/docs/ios/setup), if you have not already done so. This is not required when you bundle the model.

2. Include the TensorFlow and Firebase libraries in your Podfile:

   For bundling a model with your app:  

   ### Swift

       pod 'TensorFlowLiteSwift'

   ### Objective-C

       pod 'TensorFlowLiteObjC'

   For dynamically downloading a model from Firebase, add the`Firebase/MLModelInterpreter`dependency:  

   ### Swift

       pod 'TensorFlowLiteSwift'
       pod 'Firebase/MLModelInterpreter'

   ### Objective-C

       pod 'TensorFlowLiteObjC'
       pod 'Firebase/MLModelInterpreter'

3. After you install or update your project's Pods, open your Xcode project using its`.xcworkspace`.

## 1. Load the model

### Configure a local model source

To bundle the model with your app, copy the model and labels file to your Xcode project, taking care to select**Create folder references**when you do so. The model file and labels will be included in the app bundle.

Also, look at the`tflite_metadata.json`file that was created alongside the model. You need two values:

- The model's input dimensions. This is 320x320 by default.
- The model's maximum detections. This is 40 by default.

### Configure a Firebase-hosted model source

To use the remotely-hosted model, create a`CustomRemoteModel`object, specifying the name you assigned the model when you published it:  

### Swift

    let remoteModel = CustomRemoteModel(
        name: "your_remote_model"  // The name you assigned in the Google Cloud console.
    )

### Objective-C

    FIRCustomRemoteModel *remoteModel = [[FIRCustomRemoteModel alloc]
                                         initWithName:@"your_remote_model"];

Then, start the model download task, specifying the conditions under which you want to allow downloading. If the model isn't on the device, or if a newer version of the model is available, the task will asynchronously download the model from Firebase:  

### Swift

    let downloadProgress = ModelManager.modelManager().download(
        remoteModel,
        conditions: ModelDownloadConditions(
            allowsCellularAccess: true,
            allowsBackgroundDownloading: true
        )
    )

### Objective-C

    FIRModelDownloadConditions *conditions =
            [[FIRModelDownloadConditions alloc] initWithAllowsCellularAccess:YES
                                                 allowsBackgroundDownloading:YES];
    NSProgress *progress = [[FIRModelManager modelManager] downloadModel:remoteModel
                                                              conditions:conditions];

Many apps start the download task in their initialization code, but you can do so at any point before you need to use the model.

### Create an object detector from your model

After you configure your model sources, create a TensorFlow Lite`Interpreter`object from one of them.

If you only have a locally-bundled model, just create an interpreter from the model file:  

### Swift

    guard let modelPath = Bundle.main.path(
        forResource: "model",
        ofType: "tflite"
    ) else {
      print("Failed to load the model file.")
      return true
    }
    let interpreter = try Interpreter(modelPath: modelPath)
    try interpreter.allocateTensors()

### Objective-C

    NSString *modelPath = [[NSBundle mainBundle] pathForResource:@"model"
                                                          ofType:@"tflite"];

    NSError *error;
    TFLInterpreter *interpreter = [[TFLInterpreter alloc] initWithModelPath:modelPath
                                                                      error:&error];
    if (error != NULL) { return; }

    [interpreter allocateTensorsWithError:&error];
    if (error != NULL) { return; }

If you have a remotely-hosted model, you will have to check that it has been downloaded before you run it. You can check the status of the model download task using the model manager's`isModelDownloaded(remoteModel:)`method.

Although you only have to confirm this before running the interpreter, if you have both a remotely-hosted model and a locally-bundled model, it might make sense to perform this check when instantiating the`Interpreter`: create an interpreter from the remote model if it's been downloaded, and from the local model otherwise.  

### Swift

    var modelPath: String?
    if ModelManager.modelManager().isModelDownloaded(remoteModel) {
        ModelManager.modelManager().getLatestModelFilePath(remoteModel) { path, error in
            guard error == nil else { return }
            guard let path = path else { return }
            modelPath = path
        }
    } else {
        modelPath = Bundle.main.path(
            forResource: "model",
            ofType: "tflite"
        )
    }

    guard modelPath != nil else { return }
    let interpreter = try Interpreter(modelPath: modelPath)
    try interpreter.allocateTensors()

### Objective-C

    __block NSString *modelPath;
    if ([[FIRModelManager modelManager] isModelDownloaded:remoteModel]) {
        [[FIRModelManager modelManager] getLatestModelFilePath:remoteModel
                                                    completion:^(NSString * _Nullable filePath,
                                                                 NSError * _Nullable error) {
            if (error != NULL) { return; }
            if (filePath == NULL) { return; }
            modelPath = filePath;
        }];
    } else {
        modelPath = [[NSBundle mainBundle] pathForResource:@"model"
                                                    ofType:@"tflite"];
    }

    NSError *error;
    TFLInterpreter *interpreter = [[TFLInterpreter alloc] initWithModelPath:modelPath
                                                                      error:&error];
    if (error != NULL) { return; }

    [interpreter allocateTensorsWithError:&error];
    if (error != NULL) { return; }

If you only have a remotely-hosted model, you should disable model-related functionality---for example, gray-out or hide part of your UI---until you confirm the model has been downloaded.

You can get the model download status by attaching observers to the default Notification Center. Be sure to use a weak reference to`self`in the observer block, since downloads can take some time, and the originating object can be freed by the time the download finishes. For example:  

### Swift

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

### Objective-C

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

## 2. Prepare the input image

Next, you need to prepare your images for the TensorFlow Lite interpreter.

1. Crop and scale the image to the model's input dimensions, as specified in the`tflite_metadata.json`file (320x320 pixels by default). You can do this with Core Image or a third-party library

2. Copy the image data into a`Data`(`NSData`object):

   ### Swift

       guard let image: CGImage = // Your input image
       guard let context = CGContext(
         data: nil,
         width: image.width, height: image.height,
         bitsPerComponent: 8, bytesPerRow: image.width * 4,
         space: CGColorSpaceCreateDeviceRGB(),
         bitmapInfo: CGImageAlphaInfo.noneSkipFirst.rawValue
       ) else {
         return nil
       }

       context.draw(image, in: CGRect(x: 0, y: 0, width: image.width, height: image.height))
       guard let imageData = context.data else { return nil }

       var inputData = Data()
       for row in 0 ..< 320 {    // Model takes 320x320 pixel images as input
         for col in 0 ..< 320 {
           let offset = 4 * (col * context.width + row)
           // (Ignore offset 0, the unused alpha channel)
           var red = imageData.load(fromByteOffset: offset+1, as: UInt8.self)
           var green = imageData.load(fromByteOffset: offset+2, as: UInt8.self)
           var blue = imageData.load(fromByteOffset: offset+3, as: UInt8.self)

           inputData.append(&red, count: 1)
           inputData.append(&green, count: 1)
           inputData.append(&blue, count: 1)
         }
       }

   ### Objective-C

       CGImageRef image = // Your input image
       long imageWidth = CGImageGetWidth(image);
       long imageHeight = CGImageGetHeight(image);
       CGContextRef context = CGBitmapContextCreate(nil,
                                                    imageWidth, imageHeight,
                                                    8,
                                                    imageWidth * 4,
                                                    CGColorSpaceCreateDeviceRGB(),
                                                    kCGImageAlphaNoneSkipFirst);
       CGContextDrawImage(context, CGRectMake(0, 0, imageWidth, imageHeight), image);
       UInt8 *imageData = CGBitmapContextGetData(context);

       NSMutableData *inputData = [[NSMutableData alloc] initWithCapacity:0];

       for (int row = 0; row < 300; row++) {
         for (int col = 0; col < 300; col++) {
           long offset = 4 * (row * imageWidth + col);
           // (Ignore offset 0, the unused alpha channel)
           UInt8 red = imageData[offset+1];
           UInt8 green = imageData[offset+2];
           UInt8 blue = imageData[offset+3];

           [inputData appendBytes:&red length:1];
           [inputData appendBytes:&green length:1];
           [inputData appendBytes:&blue length:1];
         }
       }

## 3. Run the object detector

Next, pass the prepared input to the interpreter:  

### Swift

    try interpreter.copy(inputData, toInputAt: 0)
    try interpreter.invoke()

### Objective-C

    TFLTensor *input = [interpreter inputTensorAtIndex:0 error:&error];
    if (error != nil) { return; }

    [input copyData:inputData error:&error];
    if (error != nil) { return; }

    [interpreter invokeWithError:&error];
    if (error != nil) { return; }

## 4. Get information about detected objects

If object detection succeeds, the model produces as output three arrays of 40 elements (or whatever was specified in the`tflite_metadata.json`file) each. Each element corresponds to one potential object. The first array is an array of bounding boxes; the second, an array of labels; and the third, an array of confidence values. To get the model outputs:  

### Swift

    var output = try interpreter.output(at: 0)
    let boundingBoxes =
        UnsafeMutableBufferPointer<Float32>.allocate(capacity: 4 * 40)
    output.data.copyBytes(to: boundingBoxes)

    output = try interpreter.output(at: 1)
    let labels =
        UnsafeMutableBufferPointer<Float32>.allocate(capacity: 40)
    output.data.copyBytes(to: labels)

    output = try interpreter.output(at: 2)
    let probabilities =
        UnsafeMutableBufferPointer<Float32>.allocate(capacity: 40)
    output.data.copyBytes(to: probabilities)

### Objective-C

    TFLTensor *output = [interpreter outputTensorAtIndex:0 error:&error];
    if (error != nil) { return; }
    NSData *boundingBoxes = [output dataWithError:&error];
    if (error != nil) { return; }

    output = [interpreter outputTensorAtIndex:1 error:&error];
    if (error != nil) { return; }
    NSData *labels = [output dataWithError:&error];
    if (error != nil) { return; }

    output = [interpreter outputTensorAtIndex:2 error:&error];
    if (error != nil) { return; }
    NSData *probabilities = [output dataWithError:&error];
    if (error != nil) { return; }

Then, you can combine the label outputs with your label dictionary:  

### Swift

    guard let labelPath = Bundle.main.path(
        forResource: "dict",
        ofType: "txt"
    ) else { return true }
    let fileContents = try? String(contentsOfFile: labelPath)
    guard let labelText = fileContents?.components(separatedBy: "\n") else { return true }

    for i in 0 ..< 40 {
        let top = boundingBoxes[0 * i]
        let left = boundingBoxes[1 * i]
        let bottom = boundingBoxes[2 * i]
        let right = boundingBoxes[3 * i]

        let labelIdx = Int(labels[i])
        let label = labelText[labelIdx]
        let confidence = probabilities[i]

        if confidence > 0.66 {
            print("Object found: \(label) (confidence: \(confidence))")
            print("  Top-left: (\(left),\(top))")
            print("  Bottom-right: (\(right),\(bottom))")
        }
    }

### Objective-C

    NSString *labelPath = [NSBundle.mainBundle pathForResource:@"dict"
                                                        ofType:@"txt"];
    NSString *fileContents = [NSString stringWithContentsOfFile:labelPath
                                                       encoding:NSUTF8StringEncoding
                                                          error:&error];
    if (error != nil || fileContents == NULL) { return; }
    NSArray<NSString*> *labelText = [fileContents componentsSeparatedByString:@"\n"];

    for (int i = 0; i < 40; i++) {
        Float32 top, right, bottom, left;
        Float32 labelIdx;
        Float32 confidence;

        [boundingBoxes getBytes:&top range:NSMakeRange(16 * i + 0, 4)];
        [boundingBoxes getBytes:&left range:NSMakeRange(16 * i + 4, 4)];
        [boundingBoxes getBytes:&bottom range:NSMakeRange(16 * i + 8, 4)];
        [boundingBoxes getBytes:&right range:NSMakeRange(16 * i + 12, 4)];

        [labels getBytes:&labelIdx range:NSMakeRange(4 * i, 4)];
        [probabilities getBytes:&confidence range:NSMakeRange(4 * i, 4)];

        if (confidence > 0.5f) {
            NSString *label = labelText[(int)labelIdx];
            NSLog(@"Object detected: %@", label);
            NSLog(@"  Confidence: %f", confidence);
            NSLog(@"  Top-left: (%f,%f)", left, top);
            NSLog(@"  Bottom-right: (%f,%f)", right, bottom);
        }
    }

## Tips to improve real-time performance

If you want to label images in a real-time application, follow these guidelines to achieve the best framerates:

- Throttle calls to the detector. If a new video frame becomes available while the detector is running, drop the frame.
- If you are using the output of the detector to overlay graphics on the input image, first get the result, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame. See the[previewOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Controllers/FIRVideoCamViewController.m#L856)and[FIRDetectionOverlayView](https://github.com/firebase/mlkit-material-ios/blob/81bd5a028eabcbdc6b1c9c248de70ff38f0ba84a/ShowcaseApp/ShowcaseApp/Views/FIRDetectionOverlayView.m)classes in the showcase sample app for an example.