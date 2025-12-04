# Source: https://onnxruntime.ai/docs/tutorials/mobile/pose-detection.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#object-detection-and-pose-estimation-on-mobile-with-yolov8) Object detection and pose estimation on mobile with YOLOv8

Learn how to build and run ONNX models on mobile with built-in pre and post processing for object detection and pose estimation.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Object detection with YOLOv8](#object-detection-with-yolov8)
  - [Build the ONNX model with built-in pre and post processing](#build-the-onnx-model-with-built-in-pre-and-post-processing)
  - [Build an Android application](#build-an-android-application)
- [Pose estimation with YOLOv8](#pose-estimation-with-yolov8)
  - [Build the pose estimation model](#build-the-pose-estimation-model)
  - [Run examples of pose estimation](#run-examples-of-pose-estimation)
  - [Develop your mobile application](#develop-your-mobile-application)
- [Additional resources](#additional-resources)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#object-detection-with-yolov8) Object detection with YOLOv8

You can find the full source code for the [Android](https://github.com/microsoft/) app in the ONNX Runtime inference examples repository.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-the-onnx-model-with-built-in-pre-and-post-processing) Build the ONNX model with built-in pre and post processing

This step is optional as the model is available in the examples repository in the applications folders above. If you are interested, the following steps show you how to build the model yourself.

Create a Python environment and install the following packages.

``` highlight
pip install --upgrade onnx onnxruntime onnxruntime-extensions pillow
```

Download the following script to build the model.

``` highlight
curl https://raw.githubusercontent.com/microsoft/onnxruntime-extensions/main/tutorials/yolo_e2e.py > yolo_e2e.py
```

Run the script.

``` highlight
python yolo_e2e.py [--test_image <image to test on>]
```

After the script has run, you will see one PyTorch model and two ONNX models:

- `yolov8n.pt`: The original YOLOv8 PyTorch model
- `yolov8n.onnx`: The exported YOLOv8 ONNX model
- `yolov8n.with_pre_post_processing.onnx`: The ONNX model with pre and post processing included in the model
- `<test image>.out.jpg`: Your test image with bounding boxes supplied.

For example, the wolves test image in the extensions repo:

![Image of three white wolves with red bounding boxes](/images/wolves-with-bounding-boxes.png)

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-an-android-application) Build an Android application

Load the Android application into Android Developer Studio.

You see the main inference code in [ObjectDetector.kt](https://github.com/microsoft/onnxruntime-inference-examples/blob/main/mobile/examples/object_detection/android/app/src/main/java/ai/onnxruntime/example/objectdetection/ObjectDetector.kt). It's as simple as loading the image image into byte array, and running it through the model with ONNX Runtime to get the original image with boxes.

``` highlight
    fun detect(inputStream: InputStream, ortEnv: OrtEnvironment, ortSession: OrtSession): Result 
        }
    }
```

![Image of person with bicycle](/images/person-with-bicycle-and-bounding-boxes.png)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#pose-estimation-with-yolov8) Pose estimation with YOLOv8

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-the-pose-estimation-model) Build the pose estimation model

Note: this part of the tutorial uses Python. Android and iOS samples are coming soon!

Create a Python environment and install the following packages.

``` highlight
pip install --upgrade onnx onnxruntime onnxruntime-extensions pillow
```

Download the following script to build the model.

``` highlight
curl https://raw.githubusercontent.com/microsoft/onnxruntime-extensions/main/tutorials/yolov8_pose_e2e.py > yolov8_pose_e2e.py
```

Run the script.

``` highlight
python yolov8_pose_e2e.py 
```

After the script has run, you will see one PyTorch model and two ONNX models:

- `yolov8n-pose.pt`: The original YOLOv8 PyTorch model
- `yolov8n-pose.onnx`: The exported YOLOv8 ONNX model
- `yolov8n-pose.with_pre_post_processing.onnx`: The ONNX model with pre and post processing included in the model

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#run-examples-of-pose-estimation) Run examples of pose estimation

You can use the same script to run the model, supplying your own image to detect poses.

``` highlight
python yolov8_pose_e2e.py --test_image person.jpg --run_model
```

And the output is drawn on the original image!

![Person with pose drawn](/images/person-with-pose.png)

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#develop-your-mobile-application) Develop your mobile application

You can use the Python inference code as a basis for developing your mobile application.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#additional-resources) Additional resources

[ONNX Runtime examples repository](https://github.com/microsoft/onnxruntime-inference-examples) [ONNX Runtime extentions repository](https://github.com/microsoft/onnxruntime-extensions)