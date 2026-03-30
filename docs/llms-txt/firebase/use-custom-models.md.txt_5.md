# Source: https://firebase.google.com/docs/ml/android/use-custom-models.md.txt

If your app uses custom
[TensorFlow
Lite](https://www.tensorflow.org/lite/) models, you can use Firebase ML to deploy your models. By
deploying models with Firebase, you can reduce the initial download size of
your app and update your app's ML models without releasing a new version of
your app. And, with Remote Config and A/B Testing, you can dynamically
serve different models to different sets of users.

<br />

The `firebase-ml-model-interpreter` library, which provided both a model downloading API and an interface to the TensorFlow Lite interpreter, is deprecated. This page describes how to use the newer `firebase-ml-modeldownloader` library along with TensorFlow Lite's native interpreter interface.

## TensorFlow Lite models

TensorFlow Lite models are ML models that are optimized to run on mobile
devices. To get a TensorFlow Lite model:

- Use a pre-built model, such as one of the [official
  TensorFlow Lite models](https://www.tensorflow.org/lite/models).
- [Convert
  a TensorFlow model, Keras model, or concrete function to TensorFlow
  Lite.](https://www.tensorflow.org/lite/convert)

## Before you begin

1. If you haven't already, [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. In your **module (app-level) Gradle file** (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`), add the dependency for the Firebase ML model downloader library for Android. We recommend using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom) to control library versioning.

   <br />

   Also, as part of setting up Firebase ML model downloader, you need to add the
   TensorFlow Lite SDK to your app.


   ```
   dependencies {
       // Import the BoM for the Firebase platform
       implementation(platform("com.google.firebase:firebase-bom:34.10.0"))

       // Add the dependency for the Firebase ML model downloader library
       // When using the BoM, you don't specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-ml-modeldownloader")

       // Also add the dependency for the TensorFlow Lite library and specify its version
       implementation("org.tensorflow:tensorflow-lite:2.3.0")
   }
   ```

   By using the [Firebase Android BoM](https://firebase.google.com/docs/android/learn-more#bom),
   your app will always use compatible versions of Firebase Android libraries.
   *(Alternative)*
   Add Firebase library dependencies *without* using the BoM

   If you choose not to use the Firebase BoM, you must specify each Firebase library version
   in its dependency line.

   **Note that if you use *multiple* Firebase libraries in your app, we strongly
   recommend using the BoM to manage library versions, which ensures that all versions are
   compatible.**

   ```groovy
   dependencies {
       // Add the dependency for the Firebase ML model downloader library
       // When NOT using the BoM, you must specify versions in Firebase library dependencies
       implementation("com.google.firebase:firebase-ml-modeldownloader:26.0.1")

       // Also add the dependency for the TensorFlow Lite library and specify its version
       implementation("org.tensorflow:tensorflow-lite:2.3.0")
   }
   ```
3. In your app's manifest, declare that INTERNET permission is required:

   ```
   <uses-permission android:name="android.permission.INTERNET" />
   ```

## 1. Deploy your model

Deploy your custom TensorFlow models using either the Firebase console or
the Firebase Admin Python and Node.js SDKs. See
[Deploy and manage custom models](https://firebase.google.com/docs/ml/manage-hosted-models).

After you add a custom model to your Firebase project, you can reference the
model in your apps using the name you specified. At any time, you can deploy
a new TensorFlow Lite model and download the new model onto users' devices by
calling `getModel()` (see below).

## 2. Download the model to the device and initialize a TensorFlow Lite interpreter

To use your TensorFlow Lite model in your app, first use the Firebase ML SDK to download the latest version of the model to the device. Then, instantiate a TensorFlow Lite interpreter with the model.

<br />

To start the model download, call the model downloader's `getModel()` method,
specifying the name you assigned the model when you uploaded it, whether you
want to always download the latest model, and the conditions under which you
want to allow downloading.

You can choose from three download behaviors:

| Download type | Description |
|---|---|
| LOCAL_MODEL | Get the local model from the device. If there is no local model available, this behaves like `LATEST_MODEL`. Use this download type if you are not interested in checking for model updates. For example, you're using Remote Config to retrieve model names and you always upload models under new names (recommended). |
| LOCAL_MODEL_UPDATE_IN_BACKGROUND | Get the local model from the device and start updating the model in the background. If there is no local model available, this behaves like `LATEST_MODEL`. |
| LATEST_MODEL | Get the latest model. If the local model is the latest version, returns the local model. Otherwise, download the latest model. This behavior will block until the latest version is downloaded (not recommended). Use this behavior only in cases where you explicitly need the latest version. |

You should disable model-related functionality---for example, grey-out or
hide part of your UI---until you confirm the model has been downloaded.

### Kotlin

    val conditions = CustomModelDownloadConditions.Builder()
            .requireWifi()  // Also possible: .requireCharging() and .requireDeviceIdle()
            .build()
    FirebaseModelDownloader.getInstance()
            .getModel("your_model", DownloadType.LOCAL_MODEL_UPDATE_IN_BACKGROUND,
                conditions)
            .addOnSuccessListener { model: CustomModel? ->
                // Download complete. Depending on your app, you could enable the ML
                // feature, or switch from the local model to the remote model, etc.

                // The CustomModel object contains the local path of the model file,
                // which you can use to instantiate a TensorFlow Lite interpreter.
                val modelFile = model?.file
                if (modelFile != null) {
                    interpreter = Interpreter(modelFile)
                }
            }

### Java

    CustomModelDownloadConditions conditions = new CustomModelDownloadConditions.Builder()
        .requireWifi()  // Also possible: .requireCharging() and .requireDeviceIdle()
        .build();
    FirebaseModelDownloader.getInstance()
        .getModel("your_model", DownloadType.LOCAL_MODEL_UPDATE_IN_BACKGROUND, conditions)
        .addOnSuccessListener(new OnSuccessListener<CustomModel>() {
          @Override
          public void onSuccess(CustomModel model) {
            // Download complete. Depending on your app, you could enable the ML
            // feature, or switch from the local model to the remote model, etc.

            // The CustomModel object contains the local path of the model file,
            // which you can use to instantiate a TensorFlow Lite interpreter.
            File modelFile = model.getFile();
            if (modelFile != null) {
                interpreter = new Interpreter(modelFile);
            }
          }
        });

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

For example, if you have an image classification model with an input shape of
`[1 224 224 3]` floating-point values, you could generate an input `ByteBuffer`
from a `Bitmap` object as shown in the following example:

### Kotlin

    val bitmap = Bitmap.createScaledBitmap(yourInputImage, 224, 224, true)
    val input = ByteBuffer.allocateDirect(224*224*3*4).order(ByteOrder.nativeOrder())
    for (y in 0 until 224) {
        for (x in 0 until 224) {
            val px = bitmap.getPixel(x, y)

            // Get channel values from the pixel value.
            val r = Color.red(px)
            val g = Color.green(px)
            val b = Color.blue(px)

            // Normalize channel values to [-1.0, 1.0]. This requirement depends on the model.
            // For example, some models might require values to be normalized to the range
            // [0.0, 1.0] instead.
            val rf = (r - 127) / 255f
            val gf = (g - 127) / 255f
            val bf = (b - 127) / 255f

            input.putFloat(rf)
            input.putFloat(gf)
            input.putFloat(bf)
        }
    }

### Java

    Bitmap bitmap = Bitmap.createScaledBitmap(yourInputImage, 224, 224, true);
    ByteBuffer input = ByteBuffer.allocateDirect(224 * 224 * 3 * 4).order(ByteOrder.nativeOrder());
    for (int y = 0; y < 224; y++) {
        for (int x = 0; x < 224; x++) {
            int px = bitmap.getPixel(x, y);

            // Get channel values from the pixel value.
            int r = Color.red(px);
            int g = Color.green(px);
            int b = Color.blue(px);

            // Normalize channel values to [-1.0, 1.0]. This requirement depends
            // on the model. For example, some models might require values to be
            // normalized to the range [0.0, 1.0] instead.
            float rf = (r - 127) / 255.0f;
            float gf = (g - 127) / 255.0f;
            float bf = (b - 127) / 255.0f;

            input.putFloat(rf);
            input.putFloat(gf);
            input.putFloat(bf);
        }
    }

Then, allocate a `ByteBuffer` large enough to contain the model's output and
pass the input buffer and output buffer to the TensorFlow Lite interpreter's
`run()` method. For example, for an output shape of `[1 1000]` floating-point
values:

### Kotlin

    val bufferSize = 1000 * java.lang.Float.SIZE / java.lang.Byte.SIZE
    val modelOutput = ByteBuffer.allocateDirect(bufferSize).order(ByteOrder.nativeOrder())
    interpreter?.run(input, modelOutput)

### Java

    int bufferSize = 1000 * java.lang.Float.SIZE / java.lang.Byte.SIZE;
    ByteBuffer modelOutput = ByteBuffer.allocateDirect(bufferSize).order(ByteOrder.nativeOrder());
    interpreter.run(input, modelOutput);

How you use the output depends on the model you are using.

For example, if you are performing classification, as a next step, you might
map the indexes of the result to the labels they represent:

### Kotlin

    modelOutput.rewind()
    val probabilities = modelOutput.asFloatBuffer()
    try {
        val reader = BufferedReader(
                InputStreamReader(assets.open("custom_labels.txt")))
        for (i in probabilities.capacity()) {
            val label: String = reader.readLine()
            val probability = probabilities.get(i)
            println("$label: $probability")
        }
    } catch (e: IOException) {
        // File not found?
    }

### Java

    modelOutput.rewind();
    FloatBuffer probabilities = modelOutput.asFloatBuffer();
    try {
        BufferedReader reader = new BufferedReader(
                new InputStreamReader(getAssets().open("custom_labels.txt")));
        for (int i = 0; i < probabilities.capacity(); i++) {
            String label = reader.readLine();
            float probability = probabilities.get(i);
            Log.i(TAG, String.format("%s: %1.4f", label, probability));
        }
    } catch (IOException e) {
        // File not found?
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

On Android API level 21 (Lollipop) and newer, the model is downloaded to a
directory that is [excluded from automatic backup](https://developer.android.com/reference/android/content/Context#getNoBackupFilesDir()).

On Android API level 20 and older, the model is downloaded to a directory
named `com.google.firebase.ml.custom.models` in app-private
internal storage. If you enabled file backup using `BackupAgent`,
you might choose to exclude this directory.