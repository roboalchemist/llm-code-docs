# Source: https://onnxruntime.ai/docs/tutorials/mobile/superres.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#improve-image-resolution-with-machine-learning-super-resolution-on-mobile) Improve image resolution with machine learning super resolution on mobile

Learn how to build an application to improve image resolution using ONNX Runtime Mobile, with a model that includes pre and post processing.

You can use this tutorial to build the application for Android or iOS.

The application takes an image input, performs the super resolution operation when the button is clicked and displays the image with improved resolution below, as in the following screenshot.

![Super resolution on a cat](/images/mobile-superres-cat.png)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Prepare the model](#prepare-the-model)
- [Android app](#android-app)
  - [Pre-requisites](#pre-requisites)
  - [Sample code](#sample-code)
  - [Code from scratch](#code-from-scratch)
    - [Setup project](#setup-project)
    - [Dependencies](#dependencies)
    - [Project resources](#project-resources)
    - [Main application class code](#main-application-class-code)
    - [Model inference class code](#model-inference-class-code)
  - [Build and run the app](#build-and-run-the-app)
- [iOS app](#ios-app)
  - [Pre-requisites](#pre-requisites-1)
  - [Sample code](#sample-code-1)
  - [Code from scratch](#code-from-scratch-1)
    - [Create project](#create-project)
    - [Dependencies](#dependencies-1)
    - [Project resources](#project-resources-1)
    - [Main app](#main-app)
    - [Content view](#content-view)
    - [Swift / Objective C bridging header](#swift--objective-c-bridging-header)
    - [Super resolution code](#super-resolution-code)
  - [Build and run the app](#build-and-run-the-app-1)
- [Resources](#resources)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prepare-the-model) Prepare the model

The machine learning model used in this tutorial is based on the one used in the PyTorch tutorial referenced at the bottom of this page.

We provide a convenient Python script that exports the PyTorch model into ONNX format and adds pre and post processing.

1.  Before running this script, install the following python packages:

    :::: 
    ::: highlight
    ``` highlight
     pip install torch
     pip install pillow
     pip install onnx
     pip install onnxruntime
     pip install --index-url https://aiinfra.pkgs.visualstudio.com/PublicPackages/_packaging/ORT-Nightly/pypi/simple/ onnxruntime-extensions
    ```
    :::
    ::::

    A note on versions: the best super resolution results are achieved with ONNX opset 18 (with its support for the Resize operator with anti-aliasing), which is supported by onnx 1.13.0 and onnxruntime 1.14.0 and later. The onnxruntime-extensions package is a pre-release version. The release version will be available soon.

2.  Then download the script and test image from the onnxruntime-extensions GitHub repository (if you have not already cloned this repository):

    :::: 
    ::: highlight
    ``` highlight
     curl https://raw.githubusercontent.com/microsoft/onnxruntime-extensions/main/tutorials/superresolution_e2e.py > superresolution_e2e.py
     curl https://raw.githubusercontent.com/microsoft/onnxruntime-extensions/main/tutorials/data/super_res_input.png > data/super_res_input.png
    ```
    :::
    ::::

3.  Run the script to export the core model and add pre and post processing to it

    :::: 
    ::: highlight
    ``` highlight
     python superresolution_e2e.py 
    ```
    :::
    ::::

After the script runs, you should see two ONNX files in the folder in the location that you ran the script:

``` highlight
pytorch_superresolution.onnx
pytorch_superresolution_with_pre_and_post_processing.onnx
```

If you load the two models into [netron](https://netron.app/) you can see the difference in inputs and outputs between the two. The first two images below show the original model with its inputs being batches of channel data, and the second two show the inputs and outputs being the image bytes.

![ONNX model without pre and post processing](/images/mobile-superres-before-model.png)

![ONNX model inputs and outputs without pre and post processing](/images/mobile-superres-before-model-io.png)

![ONNX model with pre and post processing](/images/mobile-superres-after-model.png)

![ONNX model inputs and outputs with pre and post processing](/images/mobile-superres-after-model-io.png)

Now it's time to write the application code.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#android-app) Android app

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#pre-requisites) Pre-requisites

- Android Studio Dolphin 2021.3.1 Patch + (installed on Mac/Windows/Linux)
- Android SDK 29+
- Android NDK r22+
- An Android device or an Android Emulator

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#sample-code) Sample code

You can find full [source code for the Android super resolution app](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/super_resolution/android) in GitHub.

To run the app from source code, clone the above repo and load the `build.gradle` file into Android studio, build and run!

To build the app, step by step, follow the following sections.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#code-from-scratch) Code from scratch

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setup-project) Setup project

Create a new project for Phone and Tablet in Android studio and select the blank template. Call the application `super_resolution` or similar.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#dependencies) Dependencies

Add the following dependencies to the app `build.gradle`:

``` highlight
implementation 'com.microsoft.onnxruntime:onnxruntime-android:latest.release'
implementation 'com.microsoft.onnxruntime:onnxruntime-extensions-android:latest.release'
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#project-resources) Project resources

1.  Add the model file as a raw resource

    Create a folder called `raw` in the `src/main/res` folder and move or copy the ONNX model into the raw folder.

2.  Add the test image as an asset

    Create a folder called `assets` in the main project folder and copy the image that you want to run super resolution on into that folder with the filename of `test_superresolution.png`

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#main-application-class-code) Main application class code

Create a file called MainActivity.kt and add the following pieces of code to it.

1.  Add import statements

    :::: 
    ::: highlight
    ``` highlight
    import ai.onnxruntime.*
    import ai.onnxruntime.extensions.OrtxPackage
    import android.annotation.SuppressLint
    import android.os.Bundle
    import android.widget.Button
    import android.widget.ImageView
    import android.widget.Toast
    import androidx.activity.*
    import androidx.appcompat.app.AppCompatActivity
    import kotlinx.android.synthetic.main.activity_main.*
    import kotlinx.coroutines.*
    import java.io.InputStream
    import java.util.*
    import java.util.concurrent.ExecutorService
    import java.util.concurrent.Executors
    ```
    :::
    ::::

2.  Create the main activity class and add the class variables

    :::: 
    ::: highlight
    ``` highlight
    class MainActivity : AppCompatActivity() 
    ```
    :::
    ::::

3.  Add the `onCreate()` method

    This is where we initialize the [ONNX Runtime session](https://onnxruntime.ai/docs/api/java/ai/onnxruntime/OrtSession.html). A session holds a reference to the model used to perform inference in the application. It also takes a session options parameter, which is where you can specify different execution providers (hardware accelerators such as NNAPI). In this case, we default to running on CPU. We do however register the custom op library where the image encoding and decoding operators at the input and output of the model are found.

    :::: 
    ::: highlight
    ``` highlight
     override fun onCreate(savedInstanceState: Bundle?)  catch (e: Exception) 
         }
     }
    ```
    :::
    ::::

4.  Add the onDestroy method

    :::: 
    ::: highlight
    ``` highlight
     override fun onDestroy() 
    ```
    :::
    ::::

5.  Add the updateUI method

    :::: 
    ::: highlight
    ``` highlight
    private fun updateUI(result: Result) 
    ```
    :::
    ::::

6.  Add the readModel method

    This method reads the ONNX model from the resources folder.

    :::: 
    ::: highlight
    ``` highlight
    private fun readModel(): ByteArray    
    ```
    :::
    ::::

7.  Add a method to read the input image

    This method reads a test image from the assets folder. Currently it reads a fixed image built into the application. The sample will soon be extended to read the image directly from the camera or the camera roll.

    :::: 
    ::: highlight
    ``` highlight
    private fun readInputImage(): InputStream    
    ```
    :::
    ::::

8.  Add the method to perform inference

    This method calls the method that is at the heart of the application: `SuperResPerformer.upscale()`, which is the method that runs inference on the model. The code for this is shown in the next section.

    :::: 
    ::: highlight
    ``` highlight
     private fun performSuperResolution(ortSession: OrtSession)    
    ```
    :::
    ::::

9.  Add the TAG object

    :::: 
    ::: highlight
    ``` highlight
    companion object 
    ```
    :::
    ::::

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#model-inference-class-code) Model inference class code

Create a file called `SuperResPerformer.kt` and add the following snippets of code to it.

1.  Add imports

    :::: 
    ::: highlight
    ``` highlight
    import ai.onnxruntime.OnnxJavaType
    import ai.onnxruntime.OrtSession
    import ai.onnxruntime.OnnxTensor
    import ai.onnxruntime.OrtEnvironment
    import android.graphics.Bitmap
    import android.graphics.BitmapFactory
    import java.io.InputStream
    import java.nio.ByteBuffer
    import java.util.*
    ```
    :::
    ::::

2.  Create a result class

    :::: 
    ::: highlight
    ``` highlight
    internal data class Result(
        var outputBitmap: Bitmap? = null
    ) 
    ```
    :::
    ::::

3.  Create the super resolution performer class

    This class and its main function `upscale` are where most of the calls to ONNX Runtime live.

    - The [OrtEnvironment](https://onnxruntime.ai/docs/api/java/ai/onnxruntime/OrtEnvironment.html) singleton maintains properties of the environment and configured logging levels
    - [OnnxTensor.createTensor()](https://onnxruntime.ai/docs/api/java/ai/onnxruntime/OnnxTensor.html#createTensor(ai.onnxruntime.OrtEnvironment,java.nio.ByteBuffer,long%5B%5D,ai.onnxruntime.OnnxJavaType)) is used to create a tensor made up of the input image bytes, suitable as input to the model
    - [OnnxJavaType.UINT8](https://onnxruntime.ai/docs/api/java/ai/onnxruntime/OnnxJavaType.html) is the data type of the ByteBuffer of the input tensor
    - [OrtSession.run()](https://onnxruntime.ai/docs/api/java/ai/onnxruntime/OrtSession.html#run(java.util.Map)) run the inference (prediction) on the model to get the output upscaled image

    :::: 
    ::: highlight
    ``` highlight
    internal class SuperResPerformer(
    ) 
            }
            return result
        }
    ```
    :::
    ::::

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-and-run-the-app) Build and run the app

Within Android studio:

- Select Build -\> Make Project
- Run -\> app

The app runs in the device emulator. Connect to your Android device to run the app on device.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ios-app) iOS app

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#pre-requisites-1) Pre-requisites

- Install Xcode 13.0 and above (preferably latest version)
- An iOS device or iOS simulator
- Xcode command line tools `xcode-select --install`
- CocoaPods `sudo gem install cocoapods`
- A valid Apple Developer ID (if you are planning to run on device)

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#sample-code-1) Sample code

You can find full [source code for the iOS super resolution app](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/super_resolution/ios) in GitHub.

To run the app from source code:

1.  Clone the onnxruntime-inference-examples repo

    :::: 
    ::: highlight
    ``` highlight
    git clone https://github.com/microsoft/onnxruntime-inference-examples
    cd onnxruntime-inference-examples/mobile/examples/super_resolution/ios
    ```
    :::
    ::::

2.  Install required pod files

    :::: 
    ::: highlight
    ``` highlight
    pod install
    ```
    :::
    ::::

3.  Open the generated `ORTSuperResolution.xcworkspace` file in XCode

    (Optional: only required if you are running on device) Select your development team

4.  Run the application

    Connect your iOS device or simulator, build and run the app

    Click the `Perform Super Resolution` button to see the app in action

To develop the app, step by step, follow the following sections.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#code-from-scratch-1) Code from scratch

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#create-project) Create project

Create a new project in XCode using the APP template

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#dependencies-1) Dependencies

Install the following pods:

``` highlight
  # Pods for OrtSuperResolution
  pod 'onnxruntime-c'
  
  # Pre-release version pods
  pod 'onnxruntime-extensions-c', '0.5.0-dev+261962.e3663fb'
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#project-resources-1) Project resources

1.  Add the model file to the project

    Copy the model file generated at the beginning of this tutorial into the root of the project folder.

2.  Add the test image as an asset

    Copy the image that you want to run super resolution on into the root of the project folder.

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#main-app) Main app

Open the file called `ORTSuperResolutionApp.swift` and add the following code:

``` highlight
import SwiftUI

@main
struct ORTSuperResolutionApp: App 
    }
}
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#content-view) Content view

Open the file called `ContentView.swift` and add the following code:

``` highlight
import SwiftUI

struct ContentView: View  catch let error as NSError 
    }
    
    var body: some View 
                    
                    if performSuperRes  else 
                    }
                    Spacer()
                }
            }
            .padding()
        }
    }
}

struct ContentView_Previews: PreviewProvider 
}
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#swift--objective-c-bridging-header) Swift / Objective C bridging header 

Create a file called `ORTSuperResolution-Bridging-Header.h` and add the following import statement:

``` highlight
#import "ORTSuperResolutionPerformer.h"
```

#### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#super-resolution-code) Super resolution code

1.  Create a file called `ORTSuperResolutionPerformer.h` and add the following code:

    :::: 
    ::: highlight
    ``` highlight
    #ifndef ORTSuperResolutionPerformer_h
    #define ORTSuperResolutionPerformer_h

    #import <Foundation/Foundation.h>
    #import <UIKit/UIKit.h>

    NS_ASSUME_NONNULL_BEGIN

    @interface ORTSuperResolutionPerformer : NSObject

    + (nullable UIImage*)performSuperResolutionWithError:(NSError**)error;

    @end

    NS_ASSUME_NONNULL_END

    #endif
    ```
    :::
    ::::

2.  Create a file called `ORTSuperResolutionPerformer.mm` and add the following code:

    :::: 
    ::: highlight
    ``` highlight
     #import "ORTSuperResolutionPerformer.h"
     #import <Foundation/Foundation.h>
     #import <UIKit/UIKit.h>

     #include <array>
     #include <cstdint>
     #include <stdexcept>
     #include <string>
     #include <vector>

     #include <onnxruntime_cxx_api.h>
     #include <onnxruntime_extensions.h>

     @implementation ORTSuperResolutionPerformer

     + (nullable UIImage*)performSuperResolutionWithError:(NSError **)error 
                
             // Step 1: Load model
                
             NSString *model_path = [NSBundle.mainBundle pathForResource:@"pt_super_resolution_with_pre_post_processing_opset16"
                                                                 ofType:@"onnx"];
             if (model_path == nullptr) 
                
             // Step 2: Create Ort Inference Session
                
             auto sess = Ort::Session(ort_env, [model_path UTF8String], session_options);
                
             // Read input image
                
             // note: need to set Xcode settings to prevent it from messing with PNG files:
             // in "Build Settings":
             // - set "Compress PNG Files" to "No"
             // - set "Remove Text Metadata From PNG Files" to "No"
             NSString *input_image_path =
             [NSBundle.mainBundle pathForResource:@"cat_224x224" ofType:@"png"];
             if (input_image_path == nullptr) 
                
             // Step 3: Prepare input tensors and input/output names
                
             NSMutableData *input_data =
             [NSMutableData dataWithContentsOfFile:input_image_path];
             const int64_t input_data_length = input_data.length;
             const auto memoryInfo =
             Ort::MemoryInfo::CreateCpu(OrtDeviceAllocator, OrtMemTypeCPU);
                
             const auto input_tensor = Ort::Value::CreateTensor(memoryInfo, [input_data mutableBytes], input_data_length,
                                                             &input_data_length, 1, ONNX_TENSOR_ELEMENT_DATA_TYPE_UINT8);
                
             constexpr auto input_names = std::array;
             constexpr auto output_names = std::array;
                
             // Step 4: Call inference session run
                
             const auto outputs = sess.Run(Ort::RunOptions(), input_names.data(),
                                         &input_tensor, 1, output_names.data(), 1);
             if (outputs.size() != 1) 
                
             // Step 5: Analyze model outputs
                
             const auto &output_tensor = outputs.front();
             const auto output_type_and_shape_info = output_tensor.GetTensorTypeAndShapeInfo();
             const auto output_shape = output_type_and_shape_info.GetShape();
                
             if (const auto output_element_type =
                 output_type_and_shape_info.GetElementType();
                 output_element_type != ONNX_TENSOR_ELEMENT_DATA_TYPE_UINT8) 
                
             const uint8_t *output_data_raw = output_tensor.GetTensorData<uint8_t>();
                
             // Step 6: Convert raw bytes into NSData and return as displayable UIImage
                
             NSData *output_data = [NSData dataWithBytes:output_data_raw length:(output_shape[0])];
             output_image = [UIImage imageWithData:output_data];
                
         } catch (std::exception &e) ];
             }
             return nullptr;
         }
            
         if (error) 
         return output_image;
     }

     @end
    ```
    :::
    ::::

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-and-run-the-app-1) Build and run the app

In XCode, select the triangle build icon to build and run the app!

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#resources) Resources

[Original PyTorch tutorial](https://pytorch.org/tutorials/advanced/super_resolution_with_onnxruntime.html)