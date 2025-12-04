# Source: https://onnxruntime.ai/docs/tutorials/on-device-training/android-app.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#on-device-training-building-an-android-application) On-Device Training: Building an Android Application 

In this tutorial, we will explore how to build an Android application that incorporates ONNX Runtime's On-Device Training solution. On-device training refers to the process of training a machine learning model directly on an edge device without relying on cloud services or external servers.

Here is what the application will look like at the end of this tutorial:

![an image classification app with Tom Cruise in the middle.](../../../images/on-device-training-application-prediction-tom.jpg)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#introduction) Introduction 

We will guide you through the steps to create an Android app that can train a simple image classification model using on-device training techniques. This tutorial showcases the `transfer learning` technique where knowledge gained from training a model on one task is leveraged to improve the performance of a model on a different but related task. Instead of starting the learning process from scratch, transfer learning allows us to transfer the knowledge or features learned by a pre-trained model to a new task.

For this tutorial, we will leverage the `MobileNetV2` model which has been trained on large-scale image datasets such as ImageNet (which has 1,000 classes). We will use this model for classifying custom data into one of four classes. The initial layers of MobileNetV2 serve as a feature extractor, capturing generic visual features applicable to various tasks, and only the final classifier layer will be trained for the task at hand.

In this tutorial, we will use data to learn to:

- Classify animals into one of four categories using a pre-packed animals dataset.
- Classify celebrities into one of four categories using a custom celebrities dataset.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#table-of-contents) Table of Contents

- [Table of Contents](#table-of-contents)
- [Prerequisites](#prerequisites)
- [Offline Phase - Building the training artifacts](#offline-phase---building-the-training-artifacts)
- [Training Phase - Android application development](#training-phase---android-application-development)
- [Training Phase - Running the application on a device](#training-phase---running-the-application-on-a-device)
- [Conclusion](#conclusion)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites) Prerequisites

To follow this tutorial, you should have a basic understanding of Android app development using Java or Kotlin. Familiarity with C++ as well as familiarity with machine learning concepts such as neural networks and image classification will help as well.

- Python development environment to prepare the training artifacts
- Android Studio 4.1+
- Android SDK 29+
- Android NDK r21+
- An Android device with a camera in [developer mode](https://developer.android.com/studio/debug/dev-options) with USB debugging enabled

> **Note** The entire android application is also made available on the [`onnxruntime-training-examples`](https://github.com/microsoft/onnxruntime-training-examples/tree/master/on_device_training/mobile/android/c-cpp) GitHub repository.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#offline-phase---building-the-training-artifacts) Offline Phase - Building the training artifacts

1.  []Export the model to ONNX.

    We start with a pre-trained PyTorch model and export it to ONNX. The `MobileNetV2` model has been pretrained on the imagenet dataset that has data in 1000 categories. For our task of image classification, we want to only classify images in 4 classes. So, we change the last layer of the model to output 4 logits instead of 1,000.

    More details around how to export PyTorch models to ONNX can be found [here](https://pytorch.org/docs/stable/onnx.html).

    :::: 
    ::: highlight
    ``` highlight
    import torch
    import torchvision

    model = torchvision.models.mobilenet_v2(
       weights=torchvision.models.MobileNet_V2_Weights.IMAGENET1K_V2)

    # The original model is trained on imagenet which has 1000 classes.
    # For our image classification scenario, we need to classify among 4 categories.
    # So we need to change the last layer of the model to have 4 outputs.
    model.classifier[1] = torch.nn.Linear(1280, 4)

    # Export the model to ONNX.
    model_name = "mobilenetv2"
    torch.onnx.export(model, torch.randn(1, 3, 224, 224),
                      f"training_artifacts/.onnx",
                      input_names=["input"], output_names=["output"],
                      dynamic_axes=, "output": })
    ```
    :::
    ::::

2.  []Define the trainable and non trainable parameters

    :::: 
    ::: highlight
    ``` highlight
    import onnx

    # Load the onnx model.
    onnx_model = onnx.load(f"training_artifacts/.onnx")

    # Define the parameters that require their gradients to be computed
    # (trainable parameters) and those that do not (frozen/non trainable parameters).
    requires_grad = ["classifier.1.weight", "classifier.1.bias"]
    frozen_params = [
       param.name
       for param in onnx_model.graph.initializer
       if param.name not in requires_grad
    ]
    ```
    :::
    ::::

3.  []Generate the training artifacts.

    We will use the `CrossEntropyLoss` loss and the `AdamW` optimizer for this tutorial. More details around artifact generation can be found [here](/docs/api/python/on_device_training/training_artifacts.html).

    :::: 
    ::: highlight
    ``` highlight
    from onnxruntime.training import artifacts

    # Generate the training artifacts.
    artifacts.generate_artifacts(
       onnx_model,
       requires_grad=requires_grad,
       frozen_params=frozen_params,
       loss=artifacts.LossType.CrossEntropyLoss,
       optimizer=artifacts.OptimType.AdamW,
       artifact_directory="training_artifacts"
    )
    ```
    :::
    ::::

    That's all! The training artifacts have been generated in the `training_artifacts` folder. This marks the end of the offline phase. These artifacts are ready to be deployed to the Android device for training.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#training-phase---android-application-development) Training Phase - Android application development

1.  []Setting up the project in Android Studio

    a\. Open Android Studio and click `New Project` ![Android Studio Setup - New Project](/images/on-device-training-android-studio-setup.png)

    b\. Click on `Native C++` -\> `Next`. Fill out the `New Project` details as follows:

    - Name - `ORT Personalize`
    - Package Name - `com.example.ortpersonalize`
    - Language - `Kotlin`

    Click `Next`.

    ![Android Studio Setup - Project Name](/images/on-device-training-android-studio-project-name.png)

    c\. Select the `C++17` toolchain -\> `Finish`

    ![Android Studio Setup - Project C++ ToolChain](/images/on-device-training-android-studio-toolchain.png)

    d\. That's it! The Android Studio project has been set up. You should now be able to see the Android Studio editor with some boiler plate code.

2.  []Adding the ONNX Runtime dependency

    a\. Create two new folders called `lib` and `include\onnxruntime` under the cpp directory in the Android Studio project.

    ![lib and include folder](/images/on-device-training-lib-include.png)

    b\. Head over to [Maven Central](https://central.sonatype.com/artifact/com.microsoft.onnxruntime/onnxruntime-training-android/). Go to `Versions`-\>`Browse`-\> and download the `onnxruntime-training-android` archive package (aar file).

    c\. Rename the `aar` extension to `zip`. So `onnxruntime-training-android-1.15.0.aar` becomes `onnxruntime-training-android-1.15.0.zip`.

    d\. Extract the contents of the zip file.

    e\. Copy the `libonnxruntime.so` shared library from the `jni\arm64-v8a` folder to your Android project under the newly created `lib` folder.

    f\. Copy the contents of the `headers` folder to the newly created `include\onnxruntime` folder.

    g\. In the `native-lib.cpp` file, include the training cxx header file.

    :::: 
    ::: highlight
    ``` highlight
    #include "onnxruntime_training_cxx_api.h"
    ```
    :::
    ::::

    h\. Add `abiFilters` to the `build.gradle (Module)` file so as to select `arm64-v8a`. This setting must be added under `defaultConfig` in `build.gradle`:

    :::: 
    ::: highlight
    ``` highlight
    ndk 
    ```
    :::
    ::::

    Note that the `defaultConfig` section of the `build.gradle` file should look like:

    :::: 
    ::: highlight
    ``` highlight
     defaultConfig 
        }
    +   ndk 
       
     }
    ```
    :::
    ::::

    i\. Add the `onnxruntime` shared library to the `CMakeLists.txt` so that `cmake` can find and build against the shared library. To do this, add these lines after the `ortpersonalize` library is added in the `CMakeLists.txt`:

    :::: 
    ::: highlight
    ``` highlight
    add_library(onnxruntime SHARED IMPORTED)
    set_target_properties(onnxruntime PROPERTIES IMPORTED_LOCATION $/lib/libonnxruntime.so)
    ```
    :::
    ::::

    Let `CMake` know where the ONNX Runtime header files can be found by adding this line right after the above two lines:

    :::: 
    ::: highlight
    ``` highlight
    target_include_directories(ortpersonalize PRIVATE $/include/onnxruntime)
    ```
    :::
    ::::

    Link the Android C++ project against the `onnxruntime` library by adding the `onnxruntime` library to `target_link_libraries`:

    :::: 
    ::: highlight
    ``` highlight
    target_link_libraries( # Specifies the target library.
         ortpersonalize

         # Links the target library to the log library
         # included in the NDK.
         $

         onnxruntime)
    ```
    :::
    ::::

    Note that the `CMakeLists.txt` file should look like:

    :::: 
    ::: highlight
    ``` highlight
    project("ortpersonalize")

    add_library( # Sets the name of the library.
          ortpersonalize

          # Sets the library as a shared library.
          SHARED

          # Provides a relative path to your source file(s).
          native-lib.cpp
    +     utils.cpp
    +     inference.cpp
    +     train.cpp)
    + add_library(onnxruntime SHARED IMPORTED)
    + set_target_properties(onnxruntime PROPERTIES IMPORTED_LOCATION $/lib/libonnxruntime.so)
    + target_include_directories(ortpersonalize PRIVATE $/include/onnxruntime)

    find_library( # Sets the name of the path variable.
          log-lib

          # Specifies the name of the NDK library that
          # you want CMake to locate.
          log)

    target_link_libraries( # Specifies the target library.
          ortpersonalize

          # Links the target library to the log library
          # included in the NDK.
          $
    +     onnxruntime)
    ```
    :::
    ::::

    j\. Build the application and wait for success to confirm that the app has included the ONNX Runtime headers and can link against the shared onnxruntime library successfully.

3.  []Packaging the Prebuilt Training Artifacts and Dataset

    a\. Create a new `assets` folder inside the `app` from the left pane of the Android Studio project by right click app -\> New -\> Folder -\> Assets Folder and place it under main.

    b\. Copy the training artifacts generated in step 2 to this folder.

    c\. Now, head over to the [`onnxruntime-training-examples`](https://github.com/microsoft/onnxruntime-training-examples/tree/master/on_device_training/mobile/android/c-cpp/data) repo and download the dataset (`images.zip`) to your machine and extract it. This dataset was modified from the orignal [`animals-10`](https://www.kaggle.com/datasets/alessiocorrado99/animals10) dataset available on Kaggle created by [Corrado Alessio](https://www.kaggle.com/alessiocorrado99).

    d\. Copy the downloaded `images` folder to `assets/images` directory in Android Studio.

    The left pane of the project should look like this:

    ![Project Assets](/images/on-device-training-project-assets.png)

4.  []Interfacing with ONNX Runtime - C++ Code

    a\. We will implement the following four functions in C++ that will be called from the application:

    - `createSession`: Will be invoked on the application startup. It will create a new `CheckpointState` and `TrainingSession` objects.
    - `releaseSession`: Will be invoked when the application is about to close. This function will free up resources that were allocated at the start of the application.
    - `performTraining`: Will be invoked when the user clicks the `Train` button on the UI.
    - `performInference`: Will be invoked when the user clicks the `Infer` button on the UI.

    b\. Create Session

    This function gets called when the application is launched. This will use the training artifacts assets to create the `C++` CheckpointState and TrainingSession objects. These objects will be used for training the model on the device.

    The arguments to `createSession` are:

    - `checkpoint_path`: Cached path to the checkpoint artifact.
    - `train_model_path`: Cached path to the training model artifact.
    - `eval_model_path`: Cached path to the eval model artifact.
    - `optimizer_model_path`: Cached path to the optimizer model artifact.
    - `cache_dir_path`: Path to the cache dir on the android device. The cache dir is used as a way to access the training artifacts from the C++ code.

    The function returns a `long` that represents the pointer to the `session_cache` object. This `long` can be cast to `SessionCache` whenever we need access to the training session.

    :::: 
    ::: highlight
    ``` highlight
    extern "C" JNIEXPORT jlong JNICALL
    Java_com_example_ortpersonalize_MainActivity_createSession(
          JNIEnv *env, jobject /* this */,
          jstring checkpoint_path, jstring train_model_path, jstring eval_model_path,
          jstring optimizer_model_path, jstring cache_dir_path)
    
    ```
    :::
    ::::

    As can be seen from the function body above, this function creates a unique pointer to an object of the class `SessionCache`. The definition of `SessionCache` is provided below.

    :::: 
    ::: highlight
    ``` highlight
    struct SessionCache 
    };
    ```
    :::
    ::::

    The definition of `ArtifactPaths` is:

    :::: 
    ::: highlight
    ``` highlight
    struct ArtifactPaths 
    };
    ```
    :::
    ::::

    c\. Release Session

    This function gets called when the application is about to shutdown. It releases the resources that were created when the application was launched, mainly the CheckpointState and the TrainingSession.

    The arguments to `releaseSession` are:

    - `session`: `long` representing the `SessionCache` object.

    :::: 
    ::: highlight
    ``` highlight
    extern "C" JNIEXPORT void JNICALL
    Java_com_example_ortpersonalize_MainActivity_releaseSession(
          JNIEnv *env, jobject /* this */,
          jlong session) 
    ```
    :::
    ::::

    d\. Perform Training

    This function gets called for every batch that needs to be trained. The training loop is written on the application side in Kotlin, and within the training loop, the `performTraining` function gets invoked for every batch.

    The arguments to `performTraining` are:

    - `session`: `long` representing the `SessionCache` object.
    - `batch`: Input images as a float array to be passed in for training.
    - `labels`: Labels as an int array associated with the input images provided for training.
    - `batch_size`: Number of images to process with each `TrainStep`.
    - `channels`: Number of channels in the image. For our example, this will always be invoked with the value `3`.
    - `frame_rows`: Number of rows in the image. For our example, this will always be invoked with the value `224`.
    - `frame_cols`: Number of columns in the image. For our example, this will always be invoked with the value `224`.

    The function returns a `float` that represents the training loss for this batch.

    :::: 
    ::: highlight
    ``` highlight
    extern "C"
    JNIEXPORT float JNICALL
    Java_com_example_ortpersonalize_MainActivity_performTraining(
          JNIEnv *env, jobject /* this */,
          jlong session, jfloatArray batch, jintArray labels, jint batch_size,
          jint channels, jint frame_rows, jint frame_cols) 

       // Update the model parameters using this batch of inputs.
       return training::train_step(session_cache, env->GetFloatArrayElements(batch, nullptr),
                                  env->GetIntArrayElements(labels, nullptr), batch_size,
                                  channels, frame_rows, frame_cols);
    }
    ```
    :::
    ::::

    The above function leverages the `train_step` function. The definition of the `train_step` function is as follows:

    :::: 
    ::: highlight
    ``` highlight
    namespace training );
          const std::vector<int64_t> labels_shape();

          Ort::MemoryInfo memory_info = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);
          std::vector<Ort::Value> user_inputs; // 
          // Inputs batched
          user_inputs.emplace_back(Ort::Value::CreateTensor(memory_info, batches,
                                                             batch_size * image_channels * image_rows * image_cols * sizeof(float),
                                                             input_shape.data(), input_shape.size(),
                                                             ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT));

          // Labels batched
          user_inputs.emplace_back(Ort::Value::CreateTensor(memory_info, labels,
                                                             batch_size * sizeof(int32_t),
                                                             labels_shape.data(), labels_shape.size(),
                                                             ONNX_TENSOR_ELEMENT_DATA_TYPE_INT32));

          // Run the train step and execute the forward + loss + backward.
          float loss = *(session_cache->training_session.TrainStep(user_inputs).front().GetTensorMutableData<float>());

          // Update the model parameters by taking a step in the direction of the gradients computed above.
          session_cache->training_session.OptimizerStep();

          // Reset the gradients now that the parameters have been updated.
          // New set of gradients can then be computed for the next round of inputs.
          session_cache->training_session.LazyResetGrad();

          return loss;
       }

    } // namespace training
    ```
    :::
    ::::

    e\. Perform Inference

    This function gets called when the user wants to perform inferencing.

    The arguments to `performInference` are:

    - `session`: `long` representing the `SessionCache` object.
    - `image_buffer`: Input images as a float array to be passed in for training.
    - `batch_size`: Number of images to process with each inference. For our example, this will always be invoked with the value `1`.
    - `image_channels`: Number of channels in the image. For our example, this will always be invoked with the value `3`.
    - `image_rows`: Number of rows in the image. For our example, this will always be invoked with the value `224`.
    - `image_cols`: Number of columns in the image. For our example, this will always be invoked with the value `224`.
    - `classes`: List of strings representing all the four custom classes.

    The function returns a `string` that represents one of the four custom classes provided. This is the prediction of the model.

    :::: 
    ::: highlight
    ``` highlight
    extern "C"
    JNIEXPORT jstring JNICALL
    Java_com_example_ortpersonalize_MainActivity_performInference(
          JNIEnv *env, jobject  /* this */,
          jlong session, jfloatArray image_buffer, jint batch_size, jint image_channels, jint image_rows,
          jint image_cols, jobjectArray classes) 

       auto* session_cache = reinterpret_cast<SessionCache *>(session);
       if (!session_cache->inference_session) );
          session_cache->inference_session = std::make_unique<Ort::Session>(
                   session_cache->ort_env, session_cache->artifact_paths.inference_model_path.c_str(),
                   session_cache->session_options).release();
       }

       auto prediction = inference::classify(
                session_cache, env->GetFloatArrayElements(image_buffer, nullptr),
                batch_size, image_channels, image_rows, image_cols, classes_str);

       return env->NewStringUTF(prediction.first.c_str());
    }
    ```
    :::
    ::::

    The above function calls `classify`. The definition of classify is:

    :::: 
    ::: highlight
    ``` highlight
    namespace inference ;
          size_t input_count = 1;

          std::vector<const char *> output_names = ;
          size_t output_count = 1;

          std::vector<int64_t> input_shape();

          Ort::MemoryInfo memory_info = Ort::MemoryInfo::CreateCpu(OrtArenaAllocator, OrtMemTypeDefault);
          std::vector<Ort::Value> input_values; // 
          input_values.emplace_back(Ort::Value::CreateTensor(memory_info, image_data,
                                                             batch_size * image_channels * image_rows * image_cols * sizeof(float),
                                                             input_shape.data(), input_shape.size(),
                                                             ONNX_TENSOR_ELEMENT_DATA_TYPE_FLOAT));

          std::vector<Ort::Value> output_values;
          output_values.emplace_back(nullptr);

          // get the logits
          session_cache->inference_session->Run(Ort::RunOptions(), input_names.data(), input_values.data(),
                                                 input_count, output_names.data(), output_values.data(), output_count);

          float *output = output_values.front().GetTensorMutableData<float>();

          // run softmax and get the probabilities of each class
          std::vector<float> probabilities = Softmax(output, classes.size());
          size_t best_index = std::distance(probabilities.begin(), std::max_element(probabilities.begin(), probabilities.end()));

          return ;
       }

    } // namespace inference
    ```
    :::
    ::::

    The classify function invokes another function called `Softmax`. The definition of `Softmax` is:

    :::: 
    ::: highlight
    ``` highlight
    std::vector<float> Softmax(float *logits, size_t num_logits) 

       if (sum != 0.0f) 
       }

       return probabilities;
    }
    ```
    :::
    ::::

5.  []Image Preprocessing

    a\. The `MobileNetV2` model expects that the input image provided be

    - of size `3 x 224 x 224`.
    - a normalized image with the mean `(0.485, 0.456, 0.406)` subtracted and divided by the standard deviation `(0.229, 0.224, 0.225)`

    This preprocessing is done in Java/Kotlin using the android provided libraries.

    Let's create a new file called `ImageProcessingUtil.kt` under the `app/src/main/java/com/example/ortpersonalize` directory. We will add the utility methods for cropping and resizing, and normalizing the images in this file.

    b\. Cropping and resizing the image.

    :::: 
    ::: highlight
    ``` highlight
    fun processBitmap(bitmap: Bitmap) : Bitmap  else 

       // Resize the image to be channels x width x height as needed by the mobilenetv2 model
       val width: Int = 224
       val height: Int = 224
       val bitmapResized: Bitmap = Bitmap.createScaledBitmap(bitmapCropped, width, height, false)

       return bitmapResized
    }
    ```
    :::
    ::::

    c\. Normalizing the image.

    :::: 
    ::: highlight
    ``` highlight
    fun processImage(bitmap: Bitmap, buffer: FloatBuffer, offset: Int) 
       }
    }
    ```
    :::
    ::::

    d\. Getting a Bitmap from a Uri

    :::: 
    ::: highlight
    ``` highlight
    fun bitmapFromUri(uri: Uri, contentResolver: ContentResolver): Bitmap 
    ```
    :::
    ::::

6.  []Application Frontend

    a\. For this tutorial, we will be using the following user interface elements:

    - Train and Infer buttons
    - Class buttons
    - Status message text
    - Image display
    - Progress dialogue

    b\. This tutorial does not intend to show how the graphical user interface is created. For this reason, we will simply re-use the files available on [GitHub](https://github.com/microsoft/onnxruntime-training-examples/).

    c\. Copy all the string definitions from [`strings.xml`](https://github.com/microsoft/onnxruntime-training-examples/blob/206521eb22e496b2ea50bef956e63273b6b1d5bf/on_device_training/mobile/android/c-cpp/app/ORTPersonalize/app/src/main/res/values/strings.xml) to `strings.xml` local to your Android Studio.

    d\. Copy the contents from [`activity_main.xml`](https://github.com/microsoft/onnxruntime-training-examples/blob/206521eb22e496b2ea50bef956e63273b6b1d5bf/on_device_training/mobile/android/c-cpp/app/ORTPersonalize/app/src/main/res/layout/activity_main.xml) to `activity_main.xml` local to your Android Studio.

    e\. Create a new file under the `layout` folder called `dialog.xml`. Copy the contents from [`dialog.xml`](https://github.com/microsoft/onnxruntime-training-examples/blob/206521eb22e496b2ea50bef956e63273b6b1d5bf/on_device_training/mobile/android/c-cpp/app/ORTPersonalize/app/src/main/res/layout/dialog.xml) to the newly created `dialog.xml` local to your Android Studio.

    f\. The remainder of the changes in this section need to be made in the [MainActivity.kt](https://github.com/microsoft/onnxruntime-training-examples/blob/master/on_device_training/mobile/android/c-cpp/app/ORTPersonalize/app/src/main/java/com/example/ortpersonalize/MainActivity.kt) file.

    g\. Launching the application

    When the application launches, the `onCreate` function gets invoked. This function is responsible for setting up the session cache and the user interface handlers.

    Please refer to the `onCreate` function in the `MainActivity.kt` file for the code.

    h\. Custom class button handlers - We would like to use the class buttons for users to select their custom images for training. We need to add the listeners for these buttons to do this. These listeners will do exactly that.

    Please refer to these button handlers in `MainActivity.kt`:

    - onClassAClickedListener
    - onClassBClickedListener
    - onClassXClickedListener
    - onClassYClickedListener

    i\. Personalize the custom class labels

    By default, the custom class labels are `[A, B, X, Y]`. But, let's allow users to rename these labels for clarity. This is achieved by long click listeners namely (defined in `MainActivity.kt`):

    - onClassALongClickedListener
    - onClassBLongClickedListener
    - onClassXLongClickedListener
    - onClassYLongClickedListener

    j\. Toggling the custom classes.

    When the custom class toggle is turned off, the prepackaged animals dataset is run. And when it is turned on, the user is expected to bring their own dataset for training. To handle this transition, the `onCustomClassSettingChangedListener` switch handler is implemented in `MainActivity.kt`.

    k\. Training handler

    When each class has at least 1 image, the `Train` button can be enabled. When the `Train` button is clicked, training kicks in for the selected images. The training handler is responsible for:

    - collecting the training images into one container.
    - shuffling the order of the images.
    - cropping and resizing the images.
    - normalizing the images.
    - batching the images.
    - executing the training loop (invoking the C++ `performTraining` function in a loop).

    The `onTrainButtonClickedListener` function defined in `MainActivity.kt` does the above.

    l\. Inference handler

    Once training is complete, the user can click the `Infer` button to infer any image. The inference handler is responsible for

    - collecting the inference image.
    - cropping and resizing the image.
    - normalizing the image.
    - invoking the C++ `performInference` function.
    - Reporting the inferred output to the user interface.

    This is achieved by the `onInferenceButtonClickedListener` function in `MainActivity.kt`.

    m\. Handler for all the activities mentioned above

    Once the image(s) have been selected for inference or for the custom classes, they need to be processed. The `onActivityResult` function defined in `MainActivity.kt` does that.

    n\. One last thing. Add the following in the `AndroidManifest.xml` file to use the camera:

    :::: 
    ::: highlight
    ``` highlight
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-feature android:name="android.hardware.camera" />
    ```
    :::
    ::::

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#training-phase---running-the-application-on-a-device) Training Phase - Running the application on a device

1.  []Running the application on a device

    a\. Let's connect our Android device to the machine and run the application on the device.

    b\. Launching the application on the device should look like this:

    ![Barebones ORT Personalize app](../../../images/on-device-training-application-landing-page.jpg)

2.  []Training with a pre-loaded dataset - Animals

    a\. Let's get started with training using the pre-loaded animals device by launching the application on the device.

    b\. Toggle the `Custom classes` switch at the bottom.

    c\. The class labels will change to `Dog`, `Cat`, `Elephant` and `Cow`.

    d\. Run `Training` and wait for the progress dialog to disappear (upon training completion).

    e\. Use any animal image from your library for inferencing now.

    ![ORT Personalize app with an image of a cow](../../../images/on-device-training-application-prediction-cow.jpg)

    As can be seen from the image above, the model correctly predicted `Cow`.

3.  []Training with a custom dataset - Celebrities

    a\. Download images of Tom Cruise, Leonardo DiCaprio, Ryan Reynolds and Brad Pitt from the web.

    b\. Make sure you launch a fresh session of the app by closing the app and relaunching it.

    c\. After the application launches, rename the four classes to `Tom`, `Leo`, `Ryan`, `Brad` respectively using the long click.

    d\. Click on the button for each class and select images associated with that celebrity. We can use around 10\~15 images per category.

    e\. Hit the `Train` button and let the application learn from the data provided.

    f\. Once the training is complete, we can hit the `Infer` button and provide an image that the application has not seen yet.

    g\. That's it!. Hopefully the application classified the image correctly.

    ![an image classification app with Tom Cruise in the middle.](../../../images/on-device-training-application-prediction-tom.jpg)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#conclusion) Conclusion

Congratulations! You have successfully built an Android application that learns to classify images using ONNX Runtime on the device. The application is also made available on GitHub at [`onnxruntime-training-examples`](https://github.com/microsoft/onnxruntime-training-examples/tree/master/on_device_training/mobile/android/c-cpp).