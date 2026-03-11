# Source: https://docs.edgeimpulse.com/tutorials/topics/android/static-buffer-inference.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Static Buffer Inference on Android

> Run Edge Impulse inference with pre-loaded test data on Android

The simplest way to run Edge Impulse models on Android. Perfect for understanding the inference flow before adding sensors.

## What You'll Build

A basic Android app that:

* Loads a C++ model via Android NDK
* Runs inference on static test features
* Displays classification results

**Time**: 15 minutes\
**Difficulty**: Beginner

## Prerequisites

* Trained Edge Impulse model
* Android Studio with NDK and CMake installed
* Basic familiarity with Android development

## Step 1: Clone the Repository

```bash  theme={"system"}
git clone https://github.com/edgeimpulse/example-android-inferencing.git
cd example-android-inferencing/example_static_buffer
```

## Step 2: Download TensorFlow Lite Libraries

```bash  theme={"system"}
cd app/src/main/cpp/tflite

# Windows
download_tflite_libs.bat

# macOS/Linux
sh download_tflite_libs.sh
```

## Step 3: Export Your Model

1. In Edge Impulse Studio, go to **Deployment**
2. Select **Android (C++ library)**
3. Click **Build** and download the `.zip`

## Step 4: Integrate the Model

1. Extract the downloaded `.zip` file
2. Copy all files to:
   ```
   example_static_buffer/app/src/main/cpp/
   ```

Your structure should look like:

```
app/src/main/cpp/
├── edge-impulse-sdk/
├── model-parameters/
├── tflite-model/
├── native-lib.cpp
└── CMakeLists.txt 
```

## Step 5: Add Test Features

1. In Studio, go to **Model testing**
2. Click on a test sample
3. Copy the **raw features**
4. Paste into `native-lib.cpp`:

```cpp  theme={"system"}
// app/src/main/cpp/native-lib.cpp
std::vector<float> raw_features = {
    // Paste your raw features here
    -1.2, 0.5, 2.1, ...
};
```

## Step 6: Build and Run

1. Open the project in Android Studio
2. **Build** → **Make Project**
3. Run on a device or emulator

You should see classification results displayed on screen!

## Understanding the Code

### Native Inference (C++)

```cpp  theme={"system"}
// native-lib.cpp
extern "C" JNIEXPORT jstring JNICALL
Java_com_example_test_1cpp_MainActivity_runInference(
    JNIEnv* env, jobject /* this */) {
    
    // Create signal from raw features
    signal_t signal;
    signal.total_length = raw_features.size();
    signal.get_data = &get_feature_data;
    
    // Run classifier
    ei_impulse_result_t result = {0};
    EI_IMPULSE_ERROR res = run_classifier(&signal, &result, false);
    
    // Format results
    return env->NewStringUTF(format_results(result).c_str());
}
```

### Java/Kotlin Bridge

```kotlin  theme={"system"}
// MainActivity.kt
class MainActivity : AppCompatActivity() {
    private external fun runInference(): String
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // Load native library
        System.loadLibrary("test_cpp")
        
        // Run inference and display
        val result = runInference()
        resultTextView.text = result
    }
}
```

## Troubleshooting

<AccordionGroup>
  <Accordion title="Build fails with 'undefined reference to run_classifier'">
    **Cause**: Model files not copied correctly

    **Solution**:

    * Ensure all folders (edge-impulse-sdk, model-parameters, tflite-model) are in `app/src/main/cpp/`
    * Don't replace the existing `CMakeLists.txt`
  </Accordion>

  <Accordion title="App crashes on launch">
    **Cause**: Native library not loaded

    **Solution**:

    * Verify `System.loadLibrary("test_cpp")` matches your library name
    * Check Build output for compilation errors
  </Accordion>

  <Accordion title="Wrong classification results">
    **Cause**: Test features don't match model input

    **Solution**:

    * Copy features from Studio's Model Testing page
    * Ensure feature count matches model input size
    * Check feature order (x, y, z for accelerometer, etc.)
  </Accordion>
</AccordionGroup>

## Summary

You've built a simple Android app that runs Edge Impulse inference using static test data. This foundation allows you to explore more complex scenarios, such as real-time sensor data integration and advanced model types.

See the [Android series overview](./android-series) for more tutorials!


Built with [Mintlify](https://mintlify.com).