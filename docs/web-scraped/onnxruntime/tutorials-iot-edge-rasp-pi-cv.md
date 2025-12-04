# Source: https://onnxruntime.ai/docs/tutorials/iot-edge/rasp-pi-cv.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onnx-runtime-iot-deployment-on-raspberry-pi) ONNX Runtime IoT Deployment on Raspberry Pi 

Learn how to perform image classification on the edge using ONNX Runtime and a Raspberry Pi, taking input from the device's camera and sending the classification results to the terminal.

If you have not configured a Raspberry Pi before, check out the [Raspberry Pi documentation](https://www.raspberrypi.com/documentation/computers/getting-started.html) to get your device setup.

There are many benefits and use cases for deploying models to edge devices. Check out the list on our [IoT tutorial home page](/docs/tutorials/iot-edge/).

![Image of Raspberry Pi and camera.](../../../images/rbpi-camera.jpg)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Prerequisites](#prerequisites)
- [Download the source code, ML model and install the packages](#download-the-source-code-ml-model-and-install-the-packages)
- [Run inference on the Raspberry Pi with the `inference_mobilenet.py` script](#run-inference-on-the-raspberry-pi-with-the-inference_mobilenetpy-script)
- [Conclusion](#conclusion)
- [More examples](#more-examples)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites) Prerequisites

- [Raspberry Pi 3 B board](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/)
- SD Card Imaged with [Debian from the Raspberry Pi Imager](https://www.raspberrypi.com/software/)
- Raspberry Pi [Camera Module](https://www.raspberrypi.com/products/camera-module-v2/) or other compatible camera.
- [VNC Viewer](https://www.raspberrypi.com/documentation/computers/remote-access.html#vnc) for remote access. Optionally you can connect the board to a monitor.
- This tutorial will *not* cover imaging and setting up the Raspberry Pi. Basic understanding of how to configure and program with Python on the Raspberry Pi is expected.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#download-the-source-code-ml-model-and-install-the-packages) Download the source code, ML model and install the packages

Once you have imaged the Raspberry Pi and configured it for use its time to connect and download the source code to your device.

- Connect to your Raspberry Pi device

In this tutorial we are using VNC Viewer to remote in. If you are going to use VNC Viewer be sure to follow [these setup steps to establish a connection.](https://www.realvnc.com/en/blog/how-to-setup-vnc-connect-raspberry-pi/) Once VNC is enabled on Raspberry Pi and you have [downloaded the VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) app on your computer, then you can remote into the device.

![Image of VNC Viewer](../../../images/vncviewerrasppi.png)

- [Download the source](https://github.com/cassiebreviu/onnxruntime-raspberrypi) to your Raspberry Pi. The source code includes everything you need to run inference including a `mobilenet` ONNX model from the [model zoo](https://github.com/onnx/models) and `imagenet_classes.txt` classes.

  :::: 
  ::: highlight
  ``` highlight
    git clone https://github.com/cassiebreviu/onnxruntime-raspberrypi.git
  ```
  :::
  ::::

- Navigate to the `onnxruntime-raspberrypi` download location and install the package from the `requirements.txt` with the following command.

  :::: 
  ::: highlight
  ``` highlight
    cd onnxruntime-raspberrypi
    pip install -r requirements.txt
  ```
  :::
  ::::

  In this tutorial we are using the Raspberry Pi [Camera Module](https://www.raspberrypi.com/products/camera-module-v2/). We want to test the camera with the `cameratest.py` script provided. If you have issues getting the camera to work run `sudo apt update sudo apt upgrade` to update the board and firmware.

- Configure and test the camera by running the below command. This will create a image capture called `test.jpg` in the current directory and open a live video stream of the camera output. Hit `ESC` to cancel out of the live video output.

  :::: 
  ::: highlight
  ``` highlight
    python cameratest.py
  ```
  :::
  ::::

- The `cameratest.py` script is below for reference:

  :::: 
  ::: highlight
  ``` highlight
    import numpy as np
    import cv2

    # Create test image using opencv.
    cap = cv2.VideoCapture(0)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height

    ret, frame = cap.read()
    frame = cv2.flip(frame, -1) # Flip camera vertically
    cv2.imwrite('test.jpg', frame)
      
    # Start live video feed until `ESC` is pressed to quit.
    while(True):
        ret, frame = cap.read()
        frame = cv2.flip(frame, -1) # Flip camera vertically
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          
        cv2.imshow('frame', frame)
        cv2.imshow('gray', gray)
          
        k = cv2.waitKey(30) & 0xff
        if k == 27: # press 'ESC' to quit
            break

    cap.release()
    cv2.destroyAllWindows()
  ```
  :::
  ::::

  ## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#run-inference-on-the-raspberry-pi-with-the-inference_mobilenetpy-script) Run inference on the Raspberry Pi with the `inference_mobilenet.py` script 

Now that we have validated that the camera is connected and working on the Raspberry Pi, its time to inference the ONNX model provided in the source. The model is a [MobileNet](https://github.com/onnx/models/tree/main/validated/vision/classification/mobilenet) model that performs image classification on 1000 classes.

- Run the inference script with the below command.

  :::: 
  ::: highlight
  ``` highlight
    python inference_mobilenet.py
  ```
  :::
  ::::

- Terminal output: ![Image of VNC Viewer](../../../images/terminal-output-rasp-pi.png)

- The image that was inferenced on the Raspberry Pi: ![Image of VNC Viewer](../../../images/rasp-pi-can.png)

- The `inference_mobilenet.py` script below for reference:

  :::: 
  ::: highlight
  ``` highlight
    # Import the packages.
    from PIL import Image
    import numpy as np
    import onnxruntime
    import torch
    import cv2

    def preprocess_image(image_path, height, width, channels=3):
        image = Image.open(image_path)
        image = image.resize((width, height), Image.LANCZOS)
        image_data = np.asarray(image).astype(np.float32)
        image_data = image_data.transpose([2, 0, 1]) # transpose to CHW
        mean = np.array([0.079, 0.05, 0]) + 0.406
        std = np.array([0.005, 0, 0.001]) + 0.224
        for channel in range(image_data.shape[0]):
            image_data[channel, :, :] = (image_data[channel, :, :] / 255 - mean[channel]) / std[channel]
        image_data = np.expand_dims(image_data, 0)
        return image_data

    def softmax(x):
        """Compute softmax values for each sets of scores in x."""
        e_x = np.exp(x - np.max(x))
        return e_x / e_x.sum()

    def run_sample(session, image_file, categories):
        output = session.run([], )[0]
        output = output.flatten()
        output = softmax(output) # this is optional
        top5_catid = np.argsort(-output)[:5]
        for catid in top5_catid:
            print(categories[catid], output[catid])
        # Write the result to a file.
        with open("result.txt", "w") as f:
            for catid in top5_catid:
                f.write(categories[catid] + " " + str(output[catid]) + " \r")

    # Create main function to run inference.
    if __name__ == "__main__":
        # Read the categories from the classes file.
        with open("imagenet_classes.txt", "r") as f:
            categories = [s.strip() for s in f.readlines()]
          
        # Create Inference Session
        session = onnxruntime.InferenceSession("mobilenet_v2_float.onnx")

        # Get image from the camera.
        cap = cv2.VideoCapture(0)
        cap.set(3,640) # set Width
        cap.set(4,480) # set Height

        ret, frame = cap.read()
        frame = cv2.flip(frame, -1) # Flip camera vertically
        cv2.imwrite('capture.jpg', frame)
        cap.release()
        cv2.destroyAllWindows()

        # Run inference
        run_sample(session, 'capture.jpg', categories)
  ```
  :::
  ::::

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#conclusion) Conclusion

Now that we have successfully run inference on the Raspberry Pi, we can use the same code to run inference on any device that supports ONNX Runtime. We can also use the same code to run inference on the Raspberry Pi with a different model. Check out the other models in the [ONNX Model Zoo](https://github.com/onnx/models).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#more-examples) More examples

- [Jetson Nano embedded device: Fast model inferencing](https://github.com/Azure-Samples/onnxruntime-iot-edge/blob/master/README-ONNXRUNTIME-arm64.md)
- [Intel VPU edge device with OpenVINO: Deploy small quantized model](https://github.com/Azure-Samples/onnxruntime-iot-edge/blob/master/README-ONNXRUNTIME-OpenVINO.md)