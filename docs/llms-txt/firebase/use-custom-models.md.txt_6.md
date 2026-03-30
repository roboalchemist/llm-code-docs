# Source: https://firebase.google.com/docs/ml/ios/use-custom-models.md.txt

If your app uses custom
[TensorFlow
Lite](https://www.tensorflow.org/lite/) models, you can use Firebase ML to deploy your models. By
deploying models with Firebase, you can reduce the initial download size of
your app and update your app's ML models without releasing a new version of
your app. And, with Remote Config and A/B Testing, you can dynamically
serve different models to different sets of users.

<br />

The `MLModelInterpreter` library, which provided both a model downloading API and an interface to the TensorFlow Lite interpreter, is deprecated. This page describes how to use the newer `MLModelDownloader` library along with TensorFlow Lite's native interpreter interface.

## Prerequisites

- The `MLModelDownloader` library is only available for Swift.
- TensorFlow Lite runs only on devices using iOS 9 and newer.

## TensorFlow Lite models

TensorFlow Lite models are ML models that are optimized to run on mobile
devices. To get a TensorFlow Lite model:

- Use a pre-built model, such as one of the [official
  TensorFlow Lite models](https://www.tensorflow.org/lite/models).
- [Convert
  a TensorFlow model, Keras model, or concrete function to TensorFlow
  Lite.](https://www.tensorflow.org/lite/convert)

## Before you begin

To use TensorFlowLite with Firebase, you must use CocoaPods as TensorFlowLite
currently does not support installation with Swift Package Manager. See the
[CocoaPods installation guide](https://firebase.google.com/docs/ios/installation-methods#cocoapods) for
instructions on how to install `MLModelDownloader`.

Once installed, import Firebase and TensorFlowLite in order to use them.

### Swift

    import FirebaseMLModelDownloader
    import TensorFlowLite

## 1. Deploy your model

Deploy your custom TensorFlow models using either the Firebase console or
the Firebase Admin Python and Node.js SDKs. See
[Deploy and manage custom models](https://firebase.google.com/docs/ml/manage-hosted-models).

After you add a custom model to your Firebase project, you can reference the
model in your apps using the name you specified. At any time, you can deploy
a new TensorFlow Lite model and download the new model onto users' devices by
calling `getModel()` (see below).

## 2. Download the model to the device and initialize a TensorFlow Lite interpreter

To use your TensorFlow Lite model in your app, first use the Firebase ML SDK to download the latest version of the model to the device.

<br />

To start the model download, call the model downloader's `getModel()` method,
specifying the name you assigned the model when you uploaded it, whether you
want to always download the latest model, and the conditions under which you
want to allow downloading.

You can choose from three download behaviors:

| Download type | Description |
|---|---|
| `localModel` | Get the local model from the device. If there is no local model available, this behaves like `latestModel`. Use this download type if you are not interested in checking for model updates. For example, you're using Remote Config to retrieve model names and you always upload models under new names (recommended). |
| `localModelUpdateInBackground` | Get the local model from the device and start updating the model in the background. If there is no local model available, this behaves like `latestModel`. |
| `latestModel` | Get the latest model. If the local model is the latest version, returns the local model. Otherwise, download the latest model. This behavior will block until the latest version is downloaded (not recommended). Use this behavior only in cases where you explicitly need the latest version. |

You should disable model-related functionality---for example, grey-out or
hide part of your UI---until you confirm the model has been downloaded.

### Swift

    let conditions = ModelDownloadConditions(allowsCellularAccess: false)
    ModelDownloader.modelDownloader()
        .getModel(name: "your_model",
                  downloadType: .localModelUpdateInBackground,
                  conditions: conditions) { result in
            switch (result) {
            case .success(let customModel):
                do {
                    // Download complete. Depending on your app, you could enable the ML
                    // feature, or switch from the local model to the remote model, etc.

                    // The CustomModel object contains the local path of the model file,
                    // which you can use to instantiate a TensorFlow Lite interpreter.
                    let interpreter = try Interpreter(modelPath: customModel.path)
                } catch {
                    // Error. Bad model file?
                }
            case .failure(let error):
                // Download was unsuccessful. Don't enable ML features.
                print(error)
            }
    }

Many apps start the download task in their initialization code, but you can do
so at any point before you need to use the model.

## 3. Perform inference on input data

### Get your model's input and output shapes

The TensorFlow Lite model interpreter takes as input and produces as output
one or more multidimensional arrays. These arrays contain either
`byte`, `int`, `long`, or `float`
values. Before you can pass data to a model or use its result, you must know
the number and dimensions ("shape") of the arrays your model uses.

If you built the model yourself, or if the model's input and output format is
documented, you might already have this information. If you don't know the
shape and data type of your model's input and output, you can use the
TensorFlow Lite interpreter to inspect your model. For example:

#### Python

```python
import tensorflow as tf

interpreter = tf.lite.Interpreter(model_path="your_model.tflite")
interpreter.allocate_tensors()

# Print input shape and type
inputs = interpreter.get_input_details()
print('{} input(s):'.format(len(inputs)))
for i in range(0, len(inputs)):
    print('{} {}'.format(inputs[i]['shape'], inputs[i]['dtype']))

# Print output shape and type
outputs = interpreter.get_output_details()
print('\n{} output(s):'.format(len(outputs)))
for i in range(0, len(outputs)):
    print('{} {}'.format(outputs[i]['shape'], outputs[i]['dtype']))
```

Example output:

```
1 input(s):
[  1 224 224   3] <class 'numpy.float32'>

1 output(s):
[1 1000] <class 'numpy.float32'>
```

### Run the interpreter

After you have determined the format of your model's input and output, get your input data and perform any transformations on the data that are necessary to get an input of the right shape for your model.

<br />

For example, if your model processes images, and your model has input dimensions
of `[1, 224, 224, 3]` floating-point values, you might have to scale
the image's color values to a floating-point range as in the following example:

### Swift

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

    var inputData = Data()
    for row in 0 ..&lt; 224 {
      for col in 0 ..&lt; 224 {
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
        memcpy(&amp;bytes, &amp;normalizedRed, elementSize)
        inputData.append(&amp;bytes, count: elementSize)
        memcpy(&amp;bytes, &amp;normalizedGreen, elementSize)
        inputData.append(&amp;bytes, count: elementSize)
        memcpy(&ammp;bytes, &amp;normalizedBlue, elementSize)
        inputData.append(&amp;bytes, count: elementSize)
      }
    }

Then, copy your input `NSData` to the interpreter and run it:

### Swift

    try interpreter.allocateTensors()
    try interpreter.copy(inputData, toInputAt: 0)
    try interpreter.invoke()

You can get the model's output by calling the interpreter's `output(at:)` method.
How you use the output depends on the model you are using.

For example, if you are performing classification, as a next step, you might
map the indexes of the result to the labels they represent:

### Swift

    let output = try interpreter.output(at: 0)
    let probabilities =
            UnsafeMutableBufferPointer<Float32>.allocate(capacity: 1000)
    output.data.copyBytes(to: probabilities)

    guard let labelPath = Bundle.main.path(forResource: "retrained_labels", ofType: "txt") else { return }
    let fileContents = try? String(contentsOfFile: labelPath)
    guard let labels = fileContents?.components(separatedBy: "\n") else { return }

    for i in labels.indices {
        print("\(labels[i]): \(probabilities[i])")
    }

## Appendix: Model security

Regardless of how you make your TensorFlow Lite models available to
Firebase ML, Firebase ML stores them in the standard serialized protobuf format in
local storage.

In theory, this means that anybody can copy your model. However,
in practice, most models are so application-specific and obfuscated by
optimizations that the risk is similar to that of competitors disassembling and
reusing your code. Nevertheless, you should be aware of this risk before you use
a custom model in your app.