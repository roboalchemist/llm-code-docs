# Source: https://firebase.google.com/docs/ml-kit/ios/use-custom-models.md.txt

> [!CAUTION]
> This page is about an old version of the
> Custom Model API, which was part of ML Kit for
> Firebase. For the latest docs, see
> [the latest version](https://firebase.google.com/docs/ml/ios/use-custom-models)
> in the
> Firebase ML section.


You can use ML Kit to perform on-device inference with a
[TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) model.

<br />

ML Kit can use TensorFlow Lite models only on devices running iOS 9 and
newer.

## Before you begin

<br />

1. If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:

   ```
   pod 'Firebase/MLModelInterpreter', '6.25.0'
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
4. Convert the TensorFlow model you want to use to TensorFlow Lite format. See [TOCO: TensorFlow Lite Optimizing Converter](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/toco).

## Host or bundle your model


Before you can use a TensorFlow Lite model for inference in your app, you
must make the model available to ML Kit. ML Kit can use TensorFlow Lite
models hosted remotely using Firebase, bundled with the app binary, or both.

By hosting a model on Firebase, you can update the model without releasing a
new app version, and you can use Remote Config and A/B Testing to
dynamically serve different models to different sets of users.

If you choose to only provide the model by hosting it with Firebase, and not
bundle it with your app, you can reduce the initial download size of your app.
Keep in mind, though, that if the model is not bundled with your app, any
model-related functionality will not be available until your app downloads the
model for the first time.

By bundling your model with your app, you can ensure your app's ML features
still work when the Firebase-hosted model isn't available.

> [!NOTE]
> Before you use a custom model in a publicly-available app, be aware of the [security implications](https://firebase.google.com/docs/ml-kit/ios/use-custom-models#model_security).

### Host models on Firebase

To host your TensorFlow Lite model on Firebase:

1. In the **ML Kit** section of the [Firebase console](https://console.firebase.google.com/), click the **Custom** tab.
2. Click **Add custom model** (or **Add another model**).
3. Specify a name that will be used to identify your model in your Firebase project, then upload the TensorFlow Lite model file (usually ending in `.tflite` or `.lite`).

After you add a custom model to your Firebase project, you can reference the
model in your apps using the name you specified. At any time, you can upload
a new TensorFlow Lite model, and your app will download the new model and
start using it when the app next restarts. You can define the device
conditions required for your app to attempt to update the model (see below).

<br />

### Bundle models with an app

To bundle your TensorFlow Lite model with your app, add the model file (usually
ending in `.tflite` or `.lite`) to your Xcode project, taking care to select
**Copy bundle resources** when you do so. The model file will be included in the
app bundle and available to ML Kit.

## Load the model

To use your TensorFlow Lite model in your app, first configure ML Kit with
the locations where your model is available: remotely using Firebase, in
local storage, or both. If you specify both a local and remote model, you can
use the remote model if it is available, and fall back to the
locally-stored model if the remote model isn't available.

### Configure a Firebase-hosted model

If you hosted your model with Firebase, create a `CustomRemoteModel` object,
specifying the name you assigned the model when you published it:

### Swift

    let remoteModel = CustomRemoteModel(
      name: "your_remote_model"  // The name you assigned in the Firebase console.
    )

### Objective-C

    // Initialize using the name you assigned in the Firebase console.
    FIRCustomRemoteModel *remoteModel =
        [[FIRCustomRemoteModel alloc] initWithName:@"your_remote_model"];

Then, start the model download task, specifying the conditions under which you
want to allow downloading. If the model isn't on the device, or if a newer
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

Many apps start the download task in their initialization code, but you can do
so at any point before you need to use the model.

### Configure a local model

If you bundled the model with your app, create a `CustomLocalModel` object,
specifying the filename of the TensorFlow Lite model:

### Swift

    guard let modelPath = Bundle.main.path(
      forResource: "your_model",
      ofType: "tflite",
      inDirectory: "your_model_directory"
    ) else { /* Handle error. */ }
    let localModel = CustomLocalModel(modelPath: modelPath)

### Objective-C

    NSString *modelPath = [NSBundle.mainBundle pathForResource:@"your_model"
                                                        ofType:@"tflite"
                                                   inDirectory:@"your_model_directory"];
    FIRCustomLocalModel *localModel =
        [[FIRCustomLocalModel alloc] initWithModelPath:modelPath];

### Create an interpreter from your model

After you configure your model sources, create a
[`ModelInterpreter`](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInterpreter) object from one of them.

If you only have a locally-bundled model, just pass the `CustomLocalModel`
object to `modelInterpreter(localModel:)`:

### Swift

    let interpreter = ModelInterpreter.modelInterpreter(localModel: localModel)

### Objective-C

    FIRModelInterpreter *interpreter =
        [FIRModelInterpreter modelInterpreterForLocalModel:localModel];

If you have a remotely-hosted model, you will have to check that it has been
downloaded before you run it. You can check the status of the model download
task using the model manager's `isModelDownloaded(remoteModel:)` method.

Although you only have to confirm this before running the interpreter, if you
have both a remotely-hosted model and a locally-bundled model, it might make
sense to perform this check when instantiating the `ModelInterpreter`: create an
interpreter from the remote model if it's been downloaded, and from the local
model otherwise.

### Swift

    var interpreter: ModelInterpreter
    if ModelManager.modelManager().isModelDownloaded(remoteModel) {
      interpreter = ModelInterpreter.modelInterpreter(remoteModel: remoteModel)
    } else {
      interpreter = ModelInterpreter.modelInterpreter(localModel: localModel)
    }

### Objective-C

    FIRModelInterpreter *interpreter;
    if ([[FIRModelManager modelManager] isModelDownloaded:remoteModel]) {
      interpreter = [FIRModelInterpreter modelInterpreterForRemoteModel:remoteModel];
    } else {
      interpreter = [FIRModelInterpreter modelInterpreterForLocalModel:localModel];
    }

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

## Specify the model's input and output


Next, configure the model interpreter's input and output formats.

A TensorFlow Lite model takes as input and produces as output one or more
multidimensional arrays. These arrays contain either `byte`,
`int`, `long`, or `float` values. You must
configure ML Kit with the number and dimensions ("shape") of the arrays your
model uses.

If you don't know the shape and data type of your model's input and output,
you can use the TensorFlow Lite Python interpreter to inspect your model. For
example:

```
import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="my_model.tflite")
interpreter.allocate_tensors()

# Print input shape and type
print(interpreter.get_input_details()[0]['shape'])  # Example: [1 224 224 3]
print(interpreter.get_input_details()[0]['dtype'])  # Example: <class 'numpy.float32'>

# Print output shape and type
print(interpreter.get_output_details()[0]['shape'])  # Example: [1 1000]
print(interpreter.get_output_details()[0]['dtype'])  # Example: <class 'numpy.float32'>
```

<br />

After you determine the format of your model's input and output, configure your
app's model interpreter by creating a
[`ModelInputOutputOptions`](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInputOutputOptions) object.

For example, a floating-point image classification model might take as input an
<var translate="no">N</var>x224x224x3 array of `Float` values, representing a batch of
<var translate="no">N</var> 224x224 three-channel (RGB) images, and produce as output a list of
1000 `Float` values, each representing the probability the image is a member of
one of the 1000 categories the model predicts.

For such a model, you would configure the model interpreter's input and output
as shown below:

#### Swift

```swift
let ioOptions = ModelInputOutputOptions()
do {
    try ioOptions.setInputFormat(index: 0, type: .float32, dimensions: [1, 224, 224, 3])
    try ioOptions.setOutputFormat(index: 0, type: .float32, dimensions: [1, 1000])
} catch let error as NSError {
    print("Failed to set input or output format with error: \(error.localizedDescription)")
}
```

#### Objective-C

```objective-c
FIRModelInputOutputOptions *ioOptions = [[FIRModelInputOutputOptions alloc] init];
NSError *error;
[ioOptions setInputFormatForIndex:0
                             type:FIRModelElementTypeFloat32
                       dimensions:@[@1, @224, @224, @3]
                            error:&error];
if (error != nil) { return; }
[ioOptions setOutputFormatForIndex:0
                              type:FIRModelElementTypeFloat32
                        dimensions:@[@1, @1000]
                             error:&error];
if (error != nil) { return; }
```

## Perform inference on input data

Finally, to perform inference using the model, get your input data, perform any
transformations on the data that might be necessary for your model, and build a
`Data` object that contains the data.

For example, if your model processes images, and your model has input dimensions
of `[BATCH_SIZE, 224, 224, 3]` floating-point values, you might have to scale
the image's color values to a floating-point range as in the following example:

#### Swift

```swift
let image: CGImage = // Your input image
guard let context = CGContext(
  data: nil,
  width: image.width, height: image.height,
  bitsPerComponent: 8, bytesPerRow: image.width * 4,
  space: CGColorSpaceCreateDeviceRGB(),
  bitmapInfo: CGImageAlphaInfo.noneSkipFirst.rawValue
) else {
  return false
}

context.draw(image, in: CGRect(x: 0, y: 0, width: image.width, height: image.height))
guard let imageData = context.data else { return false }

let inputs = ModelInputs()
var inputData = Data()
do {
  for row in 0 ..< 224 {
    for col in 0 ..< 224 {
      let offset = 4 * (row * context.width + col)
      // (Ignore offset 0, the unused alpha channel)
      let red = imageData.load(fromByteOffset: offset+1, as: UInt8.self)
      let green = imageData.load(fromByteOffset: offset+2, as: UInt8.self)
      let blue = imageData.load(fromByteOffset: offset+3, as: UInt8.self)

      // Normalize channel values to [0.0, 1.0]. This requirement varies
      // by model. For example, some models might require values to be
      // normalized to the range [-1.0, 1.0] instead, and others might
      // require fixed-point values or the original bytes.
      var normalizedRed = Float32(red) / 255.0
      var normalizedGreen = Float32(green) / 255.0
      var normalizedBlue = Float32(blue) / 255.0

      // Append normalized values to Data object in RGB order.
      let elementSize = MemoryLayout.size(ofValue: normalizedRed)
      var bytes = [UInt8](repeating: 0, count: elementSize)
      memcpy(&bytes, &normalizedRed, elementSize)
      inputData.append(&bytes, count: elementSize)
      memcpy(&bytes, &normalizedGreen, elementSize)
      inputData.append(&bytes, count: elementSize)
      memcpy(&ammp;bytes, &normalizedBlue, elementSize)
      inputData.append(&bytes, count: elementSize)
    }
  }
  try inputs.addInput(inputData)
} catch let error {
  print("Failed to add input: \(error)")
}
```

#### Objective-C

```objective-c
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

FIRModelInputs *inputs = [[FIRModelInputs alloc] init];
NSMutableData *inputData = [[NSMutableData alloc] initWithCapacity:0];

for (int row = 0; row < 224; row++) {
  for (int col = 0; col < 224; col++) {
    long offset = 4 * (row * imageWidth + col);
    // Normalize channel values to [0.0, 1.0]. This requirement varies
    // by model. For example, some models might require values to be
    // normalized to the range [-1.0, 1.0] instead, and others might
    // require fixed-point values or the original bytes.
    // (Ignore offset 0, the unused alpha channel)
    Float32 red = imageData[offset+1] / 255.0f;
    Float32 green = imageData[offset+2] / 255.0f;
    Float32 blue = imageData[offset+3] / 255.0f;

    [inputData appendBytes:&red length:sizeof(red)];
    [inputData appendBytes:&green length:sizeof(green)];
    [inputData appendBytes:&blue length:sizeof(blue)];
  }
}

[inputs addInput:inputData error:&error];
if (error != nil) { return nil; }
```

After you prepare your model input (and after you confirm the model is
available), pass the input and input/output options to
your [model interpreter](https://firebase.google.com/docs/reference/swift/firebasemlmodelinterpreter/api/reference/Classes/ModelInterpreter)'s `run(inputs:options:completion:)`
method.

#### Swift

```swift
interpreter.run(inputs: inputs, options: ioOptions) { outputs, error in
    guard error == nil, let outputs = outputs else { return }
    // Process outputs
    // ...
}
```

#### Objective-C

```objective-c
[interpreter runWithInputs:inputs
                   options:ioOptions
                completion:^(FIRModelOutputs * _Nullable outputs,
                             NSError * _Nullable error) {
  if (error != nil || outputs == nil) {
    return;
  }
  // Process outputs
  // ...
}];
```

You can get the output by calling the `output(index:)` method of the object that
is returned. For example:

#### Swift

```swift
// Get first and only output of inference with a batch size of 1
let output = try? outputs.output(index: 0) as? [[NSNumber]]
let probabilities = output??[0]
```

#### Objective-C

```objective-c
// Get first and only output of inference with a batch size of 1
NSError *outputError;
NSArray *probabilites = [outputs outputAtIndex:0 error:&outputError][0];
```

How you use the output depends on the model you are using.

For example, if you are performing classification, as a next step, you might
map the indexes of the result to the labels they represent. Suppose you had a
text file with label strings for each of your model's categories; you could map
the label strings to the output probabilities by doing something like the
following:

#### Swift

```swift
guard let labelPath = Bundle.main.path(forResource: "retrained_labels", ofType: "txt") else { return }
let fileContents = try? String(contentsOfFile: labelPath)
guard let labels = fileContents?.components(separatedBy: "\n") else { return }

for i in 0 ..< labels.count {
  if let probability = probabilities?[i] {
    print("\(labels[i]): \(probability)")
  }
}
```

#### Objective-C

```objective-c
NSError *labelReadError = nil;
NSString *labelPath = [NSBundle.mainBundle pathForResource:@"retrained_labels"
                                                    ofType:@"txt"];
NSString *fileContents = [NSString stringWithContentsOfFile:labelPath
                                                   encoding:NSUTF8StringEncoding
                                                      error:&labelReadError];
if (labelReadError != nil || fileContents == NULL) { return; }
NSArray<NSString *> *labels = [fileContents componentsSeparatedByString:@"\n"];
for (int i = 0; i < labels.count; i++) {
    NSString *label = labels[i];
    NSNumber *probability = probabilites[i];
    NSLog(@"%@: %f", label, probability.floatValue);
}
```

## Appendix: Model security

Regardless of how you make your TensorFlow Lite models available to
ML Kit, ML Kit stores them in the standard serialized protobuf format in
local storage.

In theory, this means that anybody can copy your model. However,
in practice, most models are so application-specific and obfuscated by
optimizations that the risk is similar to that of competitors disassembling and
reusing your code. Nevertheless, you should be aware of this risk before you use
a custom model in your app.