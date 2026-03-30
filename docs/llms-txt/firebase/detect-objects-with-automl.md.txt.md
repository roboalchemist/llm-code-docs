# Source: https://firebase.google.com/docs/ml/android/detect-objects-with-automl.md.txt

After you [train your own model using AutoML Vision Edge](https://firebase.google.com/docs/ml/train-object-detector),
you can use it in your app to detect objects in images.

> [!WARNING]
> Firebase ML's AutoML Vision Edge features are deprecated. Consider using [Vertex AI](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide) to automatically train ML models, which you can either [export as TensorFlow
> Lite models](https://cloud.google.com/vertex-ai/docs/export/export-edge-model) for on-device use or [deploy for cloud-based
> inference](https://cloud.google.com/vertex-ai/docs/predictions/overview).

There are two ways to integrate models trained from AutoML Vision Edge: You can
bundle the model by putting it inside your app's asset folder, or you can
dynamically download it from Firebase.

| Model bundling options ||
|---|---|
| Bundled in your app | - The model is part of your app's APK - The model is available immediately, even when the Android device is offline - No need for a Firebase project |
| Hosted with Firebase | - Host the model by uploading it to [Firebase Machine Learning](https://firebase.google.com/docs/ml) - Reduces APK size - The model is downloaded on demand - Push model updates without republishing your app - Easy A/B testing with [Firebase Remote Config](https://firebase.google.com/docs/remote-config) - Requires a Firebase project |

## Before you begin

1. **If you want to download a model** , make sure you
   [add Firebase to your Android project](https://firebase.google.com/docs/android/setup),
   if you have not already done so. This is not required when you bundle the model.

2. Add the dependencies for the TensorFlow Lite Task library to your module's
   app-level gradle file, which is usually `app/build.gradle`:

   For bundling a model with your app:

       dependencies {
         // ...
         // Object detection with a bundled Auto ML model
         implementation 'org.tensorflow:tensorflow-lite-task-vision:0.0.0-nightly-SNAPSHOT'
       }

   For dynamically downloading a model from Firebase, also add the Firebase ML
   dependency:

       dependencies {
         // ...
         // Object detection with an Auto ML model deployed to Firebase
         implementation platform('com.google.firebase:firebase-bom:26.1.1')
         implementation 'com.google.firebase:firebase-ml-model-interpreter'

         implementation 'org.tensorflow:tensorflow-lite-task-vision:0.0.0-nightly'
       }

## 1. Load the model

### Configure a local model source

To bundle the model with your app:

1. Extract the model from the zip archive you downloaded from the Google Cloud console.
2. Include your model in your app package:
   1. If you don't have an assets folder in your project, create one by right-clicking the `app/` folder, then clicking **New \> Folder \> Assets Folder**.
   2. Copy your `tflite` model file with embedded metadata to the assets folder.
3. Add the following to your app's `build.gradle` file to ensure
   Gradle doesn't compress the model file when building the app:

       android {
           // ...
           aaptOptions {
               noCompress "tflite"
           }
       }

   The model file will be included in the app package and available
   as a raw asset.

   > [!NOTE]
   > **Note:** starting from version 4.1 of the Android Gradle plugin, .tflite will be added to the noCompress list by default and the above is not needed anymore.

### Configure a Firebase-hosted model source

To use the remotely-hosted model, create a `RemoteModel` object,
specifying the name you assigned the model when you published it:

### Java

    // Specify the name you assigned when you deployed the model.
    FirebaseCustomRemoteModel remoteModel =
            new FirebaseCustomRemoteModel.Builder("your_model").build();

### Kotlin

    // Specify the name you assigned when you deployed the model.
    val remoteModel =
        FirebaseCustomRemoteModel.Builder("your_model_name").build()

Then, start the model download task, specifying the conditions under which
you want to allow downloading. If the model isn't on the device, or if a newer
version of the model is available, the task will asynchronously download the
model from Firebase:

### Java

    DownloadConditions downloadConditions = new DownloadConditions.Builder()
            .requireWifi()
            .build();
    RemoteModelManager.getInstance().download(remoteModel, downloadConditions)
            .addOnSuccessListener(new OnSuccessListener<Void>() {
                @Override
                public void onSuccess(@NonNull Task<Void> task) {
                    // Success.
                }
            });

### Kotlin

    val downloadConditions = DownloadConditions.Builder()
        .requireWifi()
        .build()
    RemoteModelManager.getInstance().download(remoteModel, downloadConditions)
        .addOnSuccessListener {
            // Success.
        }

Many apps start the download task in their initialization code, but you
can do so at any point before you need to use the model.

### Create an object detector from your model

After you configure your model sources, create a `ObjectDetector` object from one
of them.

If you only have a locally-bundled model, just create an object detector from your
model file and configure the confidence score
threshold you want to require (see [Evaluate your model](https://firebase.google.com/docs/ml/train-object-detector#evaluate_the_model)):

### Java

    // Initialization
    ObjectDetectorOptions options = ObjectDetectorOptions.builder()
        .setScoreThreshold(0)  // Evaluate your model in the Google Cloud console
                               // to determine an appropriate value.
        .build();
    ObjectDetector objectDetector = ObjectDetector.createFromFileAndOptions(context, modelFile, options);

### Kotlin

    // Initialization
    val options = ObjectDetectorOptions.builder()
        .setScoreThreshold(0)  // Evaluate your model in the Google Cloud console
                               // to determine an appropriate value.
        .build()
    val objectDetector = ObjectDetector.createFromFileAndOptions(context, modelFile, options)

If you have a remotely-hosted model, you will have to check that it has been
downloaded before you run it. You can check the status of the model download
task using the model manager's `isModelDownloaded()` method.

Although you only have to confirm this before running the object detector, if you
have both a remotely-hosted model and a locally-bundled model, it might make
sense to perform this check when instantiating the object detector: create an
object detector from the remote model if it's been downloaded, and from the local
model otherwise.

### Java

    FirebaseModelManager.getInstance().isModelDownloaded(remoteModel)
            .addOnSuccessListener(new OnSuccessListener<Boolean>() {
                @Override
                public void onSuccess(Boolean isDownloaded) {
                }
            });

### Kotlin

    FirebaseModelManager.getInstance().isModelDownloaded(remoteModel)
            .addOnSuccessListener { success ->

            }

If you only have a remotely-hosted model, you should disable model-related
functionality---for example, grey-out or hide part of your UI---until
you confirm the model has been downloaded. You can do so by attaching a listener
to the model manager's `download()` method.

Once you know your model has been downloaded, create an object detector from the
model file:

### Java

    FirebaseModelManager.getInstance().getLatestModelFile(remoteModel)
            .addOnCompleteListener(new OnCompleteListener<File>() {
                @Override
                public void onComplete(@NonNull Task<File> task) {
                    File modelFile = task.getResult();
                    if (modelFile != null) {
                        ObjectDetectorOptions options = ObjectDetectorOptions.builder()
                                .setScoreThreshold(0)
                                .build();
                        objectDetector = ObjectDetector.createFromFileAndOptions(
                                getApplicationContext(), modelFile.getPath(), options);
                    }
                }
            });

### Kotlin

    FirebaseModelManager.getInstance().getLatestModelFile(remoteModel)
            .addOnSuccessListener { modelFile ->
                val options = ObjectDetectorOptions.builder()
                        .setScoreThreshold(0f)
                        .build()
                objectDetector = ObjectDetector.createFromFileAndOptions(
                        applicationContext, modelFile.path, options)
            }

## 2. Prepare the input image

Then, for each image you want to label, create a `TensorImage` object from your
image. You can create a `TensorImage` object from a `Bitmap` using the
`fromBitmap` method:

### Java

    TensorImage image = TensorImage.fromBitmap(bitmap);

### Kotlin

    val image = TensorImage.fromBitmap(bitmap)

If your image data isn't in a `Bitmap`, you can load a pixel array as shown in
the [TensorFlow Lite docs](https://www.tensorflow.org/lite/inference_with_metadata/lite_support#basic_image_manipulation_and_conversion).

## 3. Run the object detector

To detect objects in an image, pass the `TensorImage` object to the
`ObjectDetector`'s `detect()` method.

### Java

    List<Detection> results = objectDetector.detect(image);

### Kotlin

    val results = objectDetector.detect(image)

## 4. Get information about labeled objects

If the object detection operation succeeds, it returns a list of `Detection`
objects. Each `Detection` object represents something that was detected in the
image. You can get each object's bounding box and its labels.

For example:

### Java

    for (Detection result : results) {
        RectF bounds = result.getBoundingBox();
        List<Category> labels = result.getCategories();
    }

### Kotlin

    for (result in results) {
        val bounds = result.getBoundingBox()
        val labels = result.getCategories()
    }

## Tips to improve real-time performance

If you want to label images in a real-time application, follow these
guidelines to achieve the best framerates:

- Throttle calls to the image labeler. If a new video frame becomes available while the image labeler is running, drop the frame. See the [`VisionProcessorBase`](https://github.com/firebase/quickstart-android/blob/master/mlkit/app/src/main/java/com/google/firebase/samples/apps/mlkit/java/VisionProcessorBase.java) class in the quickstart sample app for an example.
- If you are using the output of the image labeler to overlay graphics on the input image, first get the result, then render the image and overlay in a single step. By doing so, you render to the display surface only once for each input frame. See the [`CameraSourcePreview`](https://github.com/firebase/quickstart-android/blob/master/mlkit/app/src/main/java/com/google/firebase/samples/apps/mlkit/common/CameraSourcePreview.java) and [`GraphicOverlay`](https://github.com/firebase/quickstart-android/blob/master/mlkit/app/src/main/java/com/google/firebase/samples/apps/mlkit/common/GraphicOverlay.java) classes in the quickstart sample app for an example.
- If you use the Camera2 API, capture images in
  `ImageFormat.YUV_420_888` format.

  If you use the older Camera API, capture images in
  `ImageFormat.NV21` format.

<br />