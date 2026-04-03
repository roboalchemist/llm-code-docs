# Source: https://firebase.google.com/docs/ml/flutter/use-custom-models.md.txt

# Source: https://firebase.google.com/docs/ml-kit/use-custom-models.md.txt

# Source: https://firebase.google.com/docs/ml-kit/ios/use-custom-models.md.txt

# Source: https://firebase.google.com/docs/ml/ios/use-custom-models.md.txt

# Source: https://firebase.google.com/docs/ml/android/use-custom-models.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/use-custom-models.md.txt

| This page is about an old version of the Custom Model API, which was part of ML Kit for Firebase. For the latest docs, see[the latest version](https://firebase.google.com/docs/ml/android/use-custom-models)in theFirebase MLsection.

<br />

You can use ML Kit to perform on-device inference with a[TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)model.

<br />

This API requires Android SDK level 16 (Jelly Bean) or newer.

## Before you begin

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. Add the dependencies for the ML Kit Android libraries to your module (app-level) Gradle file (usually`app/build.gradle`):  

   ```carbon
   apply plugin: 'com.android.application'
   apply plugin: 'com.google.gms.google-services'

   dependencies {
     // ...

     implementation 'com.google.firebase:firebase-ml-model-interpreter:22.0.3'
   }
   ```
3. Convert the TensorFlow model you want to use to TensorFlow Lite format. See[TOCO: TensorFlow Lite Optimizing Converter](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/toco).

## Host or bundle your model

<br />

Before you can use a TensorFlow Lite model for inference in your app, you must make the model available to ML Kit. ML Kit can use TensorFlow Lite models hosted remotely using Firebase, bundled with the app binary, or both.

By hosting a model on Firebase, you can update the model without releasing a new app version, and you can useRemote ConfigandA/B Testingto dynamically serve different models to different sets of users.

If you choose to only provide the model by hosting it with Firebase, and not bundle it with your app, you can reduce the initial download size of your app. Keep in mind, though, that if the model is not bundled with your app, any model-related functionality will not be available until your app downloads the model for the first time.

By bundling your model with your app, you can ensure your app's ML features still work when the Firebase-hosted model isn't available.
| Before you use a custom model in a publicly-available app, be aware of the[security implications](https://firebase.google.com/docs/ml-kit/android/use-custom-models#model_security).

### Host models on Firebase

To host your TensorFlow Lite model on Firebase:

1. In the**ML Kit** section of the[Firebaseconsole](https://console.firebase.google.com/), click the**Custom**tab.
2. Click**Add custom model** (or**Add another model**).
3. Specify a name that will be used to identify your model in your Firebase project, then upload the TensorFlow Lite model file (usually ending in`.tflite`or`.lite`).
4. In your app's manifest, declare that INTERNET permission is required:  

   ```text
   <uses-permission android:name="android.permission.INTERNET" />
   ```

After you add a custom model to your Firebase project, you can reference the model in your apps using the name you specified. At any time, you can upload a new TensorFlow Lite model, and your app will download the new model and start using it when the app next restarts. You can define the device conditions required for your app to attempt to update the model (see below).

<br />

### Bundle models with an app

To bundle your TensorFlow Lite model with your app, copy the model file (usually ending in`.tflite`or`.lite`) to your app's`assets/`folder. (You might need to create the folder first by right-clicking the`app/`folder, then clicking**New \> Folder \> Assets Folder**.)

Then, add the following to your app's`build.gradle`file to ensure Gradle doesn't compress the models when building the app:  

    android {

        // ...

        aaptOptions {
            noCompress "tflite"  // Your model's file extension: "tflite", "lite", etc.
        }
    }

The model file will be included in the app package and available to ML Kit as a raw asset.

## Load the model

To use your TensorFlow Lite model in your app, first configure ML Kit with the locations where your model is available: remotely using Firebase, in local storage, or both. If you specify both a local and remote model, you can use the remote model if it is available, and fall back to the locally-stored model if the remote model isn't available.

<br />

### Configure a Firebase-hosted model

If you hosted your model with Firebase, create a`FirebaseCustomRemoteModel`object, specifying the name you assigned the model when you uploaded it:  

### Java

    FirebaseCustomRemoteModel remoteModel =
            new FirebaseCustomRemoteModel.Builder("your_model").build();

### Kotlin

    val remoteModel = FirebaseCustomRemoteModel.Builder("your_model").build()

Then, start the model download task, specifying the conditions under which you want to allow downloading. If the model isn't on the device, or if a newer version of the model is available, the task will asynchronously download the model from Firebase:  

### Java

    FirebaseModelDownloadConditions conditions = new FirebaseModelDownloadConditions.Builder()
            .requireWifi()
            .build();
    FirebaseModelManager.getInstance().download(remoteModel, conditions)
            .addOnCompleteListener(new OnCompleteListener<Void>() {
                @Override
                public void onComplete(@NonNull Task<Void> task) {
                    // Success.
                }
            });

### Kotlin

    val conditions = FirebaseModelDownloadConditions.Builder()
        .requireWifi()
        .build()
    FirebaseModelManager.getInstance().download(remoteModel, conditions)
        .addOnCompleteListener {
            // Success.
        }

Many apps start the download task in their initialization code, but you can do so at any point before you need to use the model.

### Configure a local model

If you bundled the model with your app, create a`FirebaseCustomLocalModel`object, specifying the filename of the TensorFlow Lite model:  

### Java

    FirebaseCustomLocalModel localModel = new FirebaseCustomLocalModel.Builder()
            .setAssetFilePath("your_model.tflite")
            .build();

### Kotlin

    val localModel = FirebaseCustomLocalModel.Builder()
        .setAssetFilePath("your_model.tflite")
        .build()

### Create an interpreter from your model

After you configure your model sources, create a`FirebaseModelInterpreter`object from one of them.

If you only have a locally-bundled model, just create an interpreter from your`FirebaseCustomLocalModel`object:  

### Java

    FirebaseModelInterpreter interpreter;
    try {
        FirebaseModelInterpreterOptions options =
                new FirebaseModelInterpreterOptions.Builder(localModel).build();
        interpreter = FirebaseModelInterpreter.getInstance(options);
    } catch (FirebaseMLException e) {
        // ...
    }

### Kotlin

    val options = FirebaseModelInterpreterOptions.Builder(localModel).build()
    val interpreter = FirebaseModelInterpreter.getInstance(options)

If you have a remotely-hosted model, you will have to check that it has been downloaded before you run it. You can check the status of the model download task using the model manager's`isModelDownloaded()`method.

Although you only have to confirm this before running the interpreter, if you have both a remotely-hosted model and a locally-bundled model, it might make sense to perform this check when instantiating the model interpreter: create an interpreter from the remote model if it's been downloaded, and from the local model otherwise.  

### Java

    FirebaseModelManager.getInstance().isModelDownloaded(remoteModel)
            .addOnSuccessListener(new OnSuccessListener<Boolean>() {
                @Override
                public void onSuccess(Boolean isDownloaded) {
                    FirebaseModelInterpreterOptions options;
                    if (isDownloaded) {
                        options = new FirebaseModelInterpreterOptions.Builder(remoteModel).build();
                    } else {
                        options = new FirebaseModelInterpreterOptions.Builder(localModel).build();
                    }
                    FirebaseModelInterpreter interpreter = FirebaseModelInterpreter.getInstance(options);
                    // ...
                }
            });

### Kotlin

    FirebaseModelManager.getInstance().isModelDownloaded(remoteModel)
        .addOnSuccessListener { isDownloaded -> 
        val options =
            if (isDownloaded) {
                FirebaseModelInterpreterOptions.Builder(remoteModel).build()
            } else {
                FirebaseModelInterpreterOptions.Builder(localModel).build()
            }
        val interpreter = FirebaseModelInterpreter.getInstance(options)
    }

If you only have a remotely-hosted model, you should disable model-related functionality---for example, grey-out or hide part of your UI---until you confirm the model has been downloaded. You can do so by attaching a listener to the model manager's`download()`method:  

### Java

    FirebaseModelManager.getInstance().download(remoteModel, conditions)
            .addOnSuccessListener(new OnSuccessListener<Void>() {
                @Override
                public void onSuccess(Void v) {
                  // Download complete. Depending on your app, you could enable
                  // the ML feature, or switch from the local model to the remote
                  // model, etc.
                }
            });

### Kotlin

    FirebaseModelManager.getInstance().download(remoteModel, conditions)
        .addOnCompleteListener {
            // Download complete. Depending on your app, you could enable the ML
            // feature, or switch from the local model to the remote model, etc.
        }

## Specify the model's input and output

Next, configure the model interpreter's input and output formats.

A TensorFlow Lite model takes as input and produces as output one or more multidimensional arrays. These arrays contain either`byte`,`int`,`long`, or`float`values. You must configure ML Kit with the number and dimensions ("shape") of the arrays your model uses.

If you don't know the shape and data type of your model's input and output, you can use the TensorFlow Lite Python interpreter to inspect your model. For example:  

```python
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

After you have determined the format of your model's input and output, you can configure your app's model interpreter by creating a[`FirebaseModelInputOutputOptions`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions.Builder)object.

For example, a floating-point image classification model might take as input an<var translate="no">N</var>x224x224x3 array of`float`values, representing a batch of<var translate="no">N</var>224x224 three-channel (RGB) images, and produce as output a list of 1000`float`values, each representing the probability the image is a member of one of the 1000 categories the model predicts.

For such a model, you would configure the model interpreter's input and output as shown below:  

### Java

```java
FirebaseModelInputOutputOptions inputOutputOptions =
        new FirebaseModelInputOutputOptions.Builder()
                .setInputFormat(0, FirebaseModelDataType.FLOAT32, new int[]{1, 224, 224, 3})
                .setOutputFormat(0, FirebaseModelDataType.FLOAT32, new int[]{1, 5})
                .build();
```

### Kotlin

```kotlin
val inputOutputOptions = FirebaseModelInputOutputOptions.Builder()
        .setInputFormat(0, FirebaseModelDataType.FLOAT32, intArrayOf(1, 224, 224, 3))
        .setOutputFormat(0, FirebaseModelDataType.FLOAT32, intArrayOf(1, 5))
        .build()
```

## Perform inference on input data

Finally, to perform inference using the model, get your input data and perform any transformations on the data that are necessary to get an input array of the right shape for your model.

<br />

For example, if you have an image classification model with an input shape of \[1 224 224 3\] floating-point values, you could generate an input array from a`Bitmap`object as shown in the following example:  

### Java

```java
Bitmap bitmap = getYourInputImage();
bitmap = Bitmap.createScaledBitmap(bitmap, 224, 224, true);

int batchNum = 0;
float[][][][] input = new float[1][224][224][3];
for (int x = 0; x < 224; x++) {
    for (int y = 0; y < 224; y++) {
        int pixel = bitmap.getPixel(x, y);
        // Normalize channel values to [-1.0, 1.0]. This requirement varies by
        // model. For example, some models might require values to be normalized
        // to the range [0.0, 1.0] instead.
        input[batchNum][x][y][0] = (Color.red(pixel) - 127) / 128.0f;
        input[batchNum][x][y][1] = (Color.green(pixel) - 127) / 128.0f;
        input[batchNum][x][y][2] = (Color.blue(pixel) - 127) / 128.0f;
    }
}
```

### Kotlin

```kotlin
val bitmap = Bitmap.createScaledBitmap(yourInputImage, 224, 224, true)

val batchNum = 0
val input = Array(1) { Array(224) { Array(224) { FloatArray(3) } } }
for (x in 0..223) {
    for (y in 0..223) {
        val pixel = bitmap.getPixel(x, y)
        // Normalize channel values to [-1.0, 1.0]. This requirement varies by
        // model. For example, some models might require values to be normalized
        // to the range [0.0, 1.0] instead.
        input[batchNum][x][y][0] = (Color.red(pixel) - 127) / 255.0f
        input[batchNum][x][y][1] = (Color.green(pixel) - 127) / 255.0f
        input[batchNum][x][y][2] = (Color.blue(pixel) - 127) / 255.0f
    }
}
```

Then, create a[`FirebaseModelInputs`](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs.Builder)object with your input data, and pass it and the model's input and output specification to the[model interpreter](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter)'s`run`method:  

### Java

```java
FirebaseModelInputs inputs = new FirebaseModelInputs.Builder()
        .add(input)  // add() as many input arrays as your model requires
        .build();
firebaseInterpreter.run(inputs, inputOutputOptions)
        .addOnSuccessListener(
                new OnSuccessListener<FirebaseModelOutputs>() {
                    @Override
                    public void onSuccess(FirebaseModelOutputs result) {
                        // ...
                    }
                })
        .addOnFailureListener(
                new OnFailureListener() {
                    @Override
                    public void onFailure(@NonNull Exception e) {
                        // Task failed with an exception
                        // ...
                    }
                });
```

### Kotlin

```kotlin
val inputs = FirebaseModelInputs.Builder()
        .add(input) // add() as many input arrays as your model requires
        .build()
firebaseInterpreter.run(inputs, inputOutputOptions)
        .addOnSuccessListener { result ->
            // ...
        }
        .addOnFailureListener { e ->
            // Task failed with an exception
            // ...
        }
```

If the call succeeds, you can get the output by calling the`getOutput()`method of the object that is passed to the success listener. For example:  

### Java

```java
float[][] output = result.getOutput(0);
float[] probabilities = output[0];
```

### Kotlin

```kotlin
val output = result.getOutput<Array<FloatArray>>(0)
val probabilities = output[0]
```

How you use the output depends on the model you are using.

For example, if you are performing classification, as a next step, you might map the indexes of the result to the labels they represent:  

### Java

```java
BufferedReader reader = new BufferedReader(
        new InputStreamReader(getAssets().open("retrained_labels.txt")));
for (int i = 0; i < probabilities.length; i++) {
    String label = reader.readLine();
    Log.i("MLKit", String.format("%s: %1.4f", label, probabilities[i]));
}
```

### Kotlin

```kotlin
val reader = BufferedReader(
        InputStreamReader(assets.open("retrained_labels.txt")))
for (i in probabilities.indices) {
    val label = reader.readLine()
    Log.i("MLKit", String.format("%s: %1.4f", label, probabilities[i]))
}
```

## Appendix: Model security

Regardless of how you make your TensorFlow Lite models available to ML Kit, ML Kit stores them in the standard serialized protobuf format in local storage.

In theory, this means that anybody can copy your model. However, in practice, most models are so application-specific and obfuscated by optimizations that the risk is similar to that of competitors disassembling and reusing your code. Nevertheless, you should be aware of this risk before you use a custom model in your app.

On Android API level 21 (Lollipop) and newer, the model is downloaded to a directory that is[excluded from automatic backup](https://developer.android.com/reference/android/content/Context#getNoBackupFilesDir()).

On Android API level 20 and older, the model is downloaded to a directory named`com.google.firebase.ml.custom.models`in app-private internal storage. If you enabled file backup using`BackupAgent`, you might choose to exclude this directory.