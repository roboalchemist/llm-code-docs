# Source: https://docs.edgeimpulse.com/hardware/deployments/run-cpp-android.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run C++ library on Android

Impulses exported as a [Android Library variant of the C++ library](/hardware/deployments/run-cpp-overview) can be integrated into Android applications to run locally on-device as an Android distributable binary (APK).

<Frame caption="Deploy as Android Library (C++)">
  <img src="https://mintcdn.com/edgeimpulse/lJhiQoQYLc2c0-kV/.assets/images/android/android-deploy.png?fit=max&auto=format&n=lJhiQoQYLc2c0-kV&q=85&s=5659059afda8ab6a07a52137a566aab2" alt="Android library (C++)" width="250" data-path=".assets/images/android/android-deploy.png" />
</Frame>

This option now comes with a **preconfigured CMake build system** tailored for Android projects. The provided `CMakeLists.txt` automatically links the Edge Impulse SDK, your model, and TensorFlow Lite runtime libraries—making it easier to build and run inference without manual configuration.

This deployment path is built on top of the [Android NDK](https://developer.android.com/ndk), which enables native C++ code execution inside Android applications.

Our sample repository works with Object detection, Image classification, Audio classification, and Sensor data projects. It also includes a WearOS example for motion data.

Here is a sample of the GMM Cracks demo project running on an Android device, using the camera to detect cracks in concrete.

<Frame caption="Android Studio - FOMO-AD - live debugging">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/android/android_studio_gmm_cracks.gif?s=ea58ff1b86eaf24b00bfaadd9f612b6f" width="1956" height="802" data-path=".assets/images/android/android_studio_gmm_cracks.gif" />
</Frame>

#### Try the example above on your Android device:

To try out an example, we have created an application that you can download and run on your Android device. The APK contains our [GMM Cracks demo project](/studio/projects/learning-blocks/blocks/visual-anomaly-detection-fomo-ad) to detect cracks in concrete.

<Frame caption="Download the GMM Test APK">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/android/edgeimp.com_AndroidAPK.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=4efad15c5bf7ef4b4ea2ebda6a300080" alt="Android GMM Cracks APK" width="250" data-path=".assets/images/android/edgeimp.com_AndroidAPK.png" />
</Frame>

Or continue reading to build your own project as an Android application. This document will guide you through the high level process of building an Android application. See the example-android-inferencing [README](https://github.com/edgeimpulse/example-android-inferencing) for more details, and any latest updates.

## Prerequisites

Make sure you followed the [Visual anomaly detection (FOMO-AD)](/studio/projects/learning-blocks/blocks/visual-anomaly-detection-fomo-ad) tutorial, and have a trained impulse, or clone [Visual GMM cracks](/studio/projects/learning-blocks/blocks/visual-anomaly-detection-fomo-ad).

Also install the following software:

* [Android Studio](https://developer.android.com/studio)
* [Android NDK](https://developer.android.com/ndk)
* [example-android-inferencing repository](https://github.com/edgeimpulse/example-android-inferencing)

## Clone the base repository

We created an example repository which contains a sample application for Android, and wearOS which you can use to build on, and experiment using your own impulse. Download the application as a .zip, or import this repository using Git:

```bash  theme={"system"}
git clone https://github.com/edgeimpulse/example-android-inferencing
```

* WearOS - [example\_motion\_WearOS](https://github.com/edgeimpulse/example-android-inferencing/tree/main/example_motion_WearOS)
* Android - [example\_camera\_inference](https://github.com/edgeimpulse/example-android-inferencing/tree/main/example_camera_inference)
* Static Buffer - [example\_static\_buffer](https://github.com/edgeimpulse/example-android-inferencing/tree/main/example_static_buffer)
  Open Android Studio.

## Deploy your C++ project

Make sure you have exported your impulse as a C++ library. If you haven't done this yet, follow the steps in the [C++ Library](/hardware/deployments/run-cpp-overview) documentation. Ensure that **TensorFlow lite** is selected, before the C++ library is generated.

<Frame caption="Deploy C++ Library">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/android/cpp_tflite.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=a1aaf275bd0f3c6ca29cea3ff48cb07c" width="1588" height="1000" data-path=".assets/images/android/cpp_tflite.png" />
</Frame>

## Import your C++ project

Depending on the example you want to use, import the project into Android Studio:

### Static buffer

The Static Buffer example is a simple application that uses a static buffer to run the impulse on the device. The application will show the result of the inference on the screen.

To get inference to work, we need to add raw data from one of our samples to native-lib.cpp. Head back to the studio and click on **Live classification**. Then load a validation sample, and click on a row under 'Detailed result'. Make a note of the classification results, as we want our local application to produce the same numbers from inference.

<Frame caption="Selecting the row with timestamp '320' under 'Detailed result'.">
  <img src="https://mintcdn.com/edgeimpulse/d_Ddn0QCYskBYT93/.assets/images/5442de6-detailed-result.png?fit=max&auto=format&n=d_Ddn0QCYskBYT93&q=85&s=e8e583288e584ff20321d4d96eeaa05b" width="438" height="357" data-path=".assets/images/5442de6-detailed-result.png" />
</Frame>

Here we replace the raw\_features array in native-lib.cpp with the raw data from the sample.

<Frame caption="Static Buffer Inference">
  <img src="https://mintcdn.com/edgeimpulse/XwnzH-Jo3nDoEg0b/.assets/images/android/static_buffer_android.png?fit=max&auto=format&n=XwnzH-Jo3nDoEg0b&q=85&s=dfc7de5190b646f7c479502df2c94874" width="1472" height="278" data-path=".assets/images/android/static_buffer_android.png" />
</Frame>

The application will show the result of the inference on the screen.

### Android

The Android example is a simple application that uses the camera to collect data, and run the impulse on the device. The application will show the result of the inference on the screen.

<Frame caption="Android GMM Cracks">
  <img src="https://mintcdn.com/edgeimpulse/yFhUTvBmotQWHOGx/.assets/images/android/debugging_gmm.png?fit=max&auto=format&n=yFhUTvBmotQWHOGx&q=85&s=e59d5d7b33a2181540eb9c50a6fef778" width="1588" height="1000" data-path=".assets/images/android/debugging_gmm.png" />
</Frame>

### WearOS

The WearOS example is a simple application that uses the accelerometer sensor to collect data, and run the impulse on the device. The application will show the result of the inference on the screen.

<Frame caption="WearOS Motion Inference">
  <img src="https://mintcdn.com/edgeimpulse/XwnzH-Jo3nDoEg0b/.assets/images/android/wearos-sensors.png?fit=max&auto=format&n=XwnzH-Jo3nDoEg0b&q=85&s=24e14597ea346ddfcfdf09639d638642" width="1600" height="894" data-path=".assets/images/android/wearos-sensors.png" />
</Frame>

## Add Edge Impulse C++ files

Unzip your Edge Impulse C++ Library export. Copy these folders into your project's `app/src/main/cpp/` directory:

* `edge-impulse-sdk/`
* `model-parameters/`
* `tflite-model/`

### Download the TFLite libraries

Run the Windows / Linux / OSX script to fetch resources

```bash  theme={"system"}
cd example-android-inferencing/example_static_buffer/app/src/main/cpp/tflite
sh download_tflite_libs.bat # download_tflite_libs.sh for OSX and Linux
```

Now you can build the application.

## Building the application

To build the application, open the project in Android Studio, and click on the 'Run' button. This will build the application and deploy it to your Android device.

## Adding additional sensors

If you want to integrate additional sensors, such as a Gyroscope or Heart Rate Sensor, follow these steps:

1. Enable the Sensor in the Code In MainActivity.kt, locate the sensor initialization section and uncomment the corresponding lines:

```java (kotlin) theme={"system"}
// Uncomment to add Gyroscope support
private var gyroscope: Sensor? = null

// Uncomment to add Heart Rate sensor support
private var heartRateSensor: Sensor? = null
```

2. Initialize the Sensor in onCreate Inside onCreate(), uncomment and initialize the sensor:

```java (kotlin) theme={"system"}
 gyroscope = sensorManager.getDefaultSensor(Sensor.TYPE_GYROSCOPE)
// heartRateSensor = sensorManager.getDefaultSensor(Sensor.TYPE_HEART_RATE)
```

3. Register the Sensor in onResume To start collecting sensor data when the app is active, uncomment the registration logic:

```java (kotlin) theme={"system"}
 gyroscope?.also {
     sensorManager.registerListener(this, it, SensorManager.SENSOR_DELAY_NORMAL)
 }

// heartRateSensor?.also {
//     sensorManager.registerListener(this, it, SensorManager.SENSOR_DELAY_NORMAL)
// }
```

4. Handle Sensor Data in onSensorChanged Modify the onSensorChanged() function to collect new sensor data:

```java (kotlin) theme={"system"}

 Gyroscope data
 Sensor.TYPE_GYROSCOPE -> {
     ringBuffer[ringBufferIndex++] = event.values[0] // X rotation
     ringBuffer[ringBufferIndex++] = event.values[1] // Y rotation
     ringBuffer[ringBufferIndex++] = event.values[2] // Z rotation
 }

// Heart Rate data
// Sensor.TYPE_HEART_RATE -> {
//     ringBuffer[ringBufferIndex++] = event.values[0] // Heart rate BPM
// }
```

5. Unregister the Sensor in onPause To save battery and improve performance, ensure sensors stop when the app is paused:

```java (kotlin) theme={"system"}

sensorManager.unregisterListener(this)
```

### Update the CMakeLists.txt for additional libraries or options (optional step for entire projects e.g. HRV)

This is the where you can add additional libraries or options to the CMakeLists.txt file. For example, to enable the full TFLite library, you can add the following line to the CMakeLists.txt file:

```cmake  theme={"system"}
add_definitions(-DEI_CLASSIFIER_ENABLE_DETECTION_POSTPROCESS_OP=1
    -DEI_DSP_ENABLE_RUNTIME_HR == 1
    -DEI_CLASSIFIER_USE_FULL_TFLITE=1
    -DNDEBUG
)
```

## Hardware Acceleration (Coming soon)

To further optimize inference on Android, future updates will include:

GPU acceleration with LiteRT delegate: Improves performance for TFLite models.

For now, refer to [Google's LiteRT documentation](https://ai.google.dev/edge/litert/android/gpu#use_gpu_with_litert_with_google_play_services) for details, or contact [sales](https://edgeimpulse.com/contact-sales) for more information.

## Conclusion

You now have a working Android application that runs your impulse on the device. You can use this as a starting point to build your own application, or integrate it into an existing application.

Android opens up the ability to distribute Android APKs for a wide range of platforms, including WearOS, Automotive, Television, Unity, and eXtended Reality (XR). This ease of distribution is a powerful tool for deploying your impulse on a wide range of devices.

We hope this tutorial has been helpful. If you have any questions, or need further assistance, please reach out to us on the [Edge Impulse forum](https://forum.edgeimpulse.com/).

## References

* [Android Studio](https://developer.android.com/studio)
* [Android NDK](https://developer.android.com/ndk)
* [Google's LiteRT documentation](https://ai.google.dev/edge/litert/android/gpu#use_gpu_with_litert_with_google_play_services)


Built with [Mintlify](https://mintlify.com).