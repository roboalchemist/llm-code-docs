# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/openmv.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/sdks/openmv.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/sdks/openmv.md

# Source: https://docs.roboflow.com/deploy/sdks/openmv.md

# OpenMV

The OpenMV camera is an extremely low-power camera-compute unit that uses an image processing SOC to run micropython programs directly on the same board as the camera. It uses less than 0.5W of power and can run models at up to \~13 fps (with quantization and low resolutions).

#### Train a compatible model

Train a Roboflow 3.0 model to allow for OpenMV deployments. Models are quantized and scaled by our model post-processing (so that it fits on the low-power SOC) so the the real-world performance might be lower than the metrics in platform might reveal. Please also use a resolution of 224 or 256 for best results (thats what we scale to in post-processing).

#### Download Quantized Artifact

Use the deployments page to download the OpenMV artifact which should consist of a `.tflite` file which is compatible with OpenMV devices.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FR7t5VJwcgqw5BtKALjlC%2FScreenshot%202025-12-19%20at%2011.47.22%E2%80%AFAM.png?alt=media&#x26;token=b829cf49-985c-41d4-ab37-357a4020c815" alt=""><figcaption></figcaption></figure>

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2F2uJncfmf7vomaH0QcbpA%2FScreenshot%202025-12-19%20at%2011.47.35%E2%80%AFAM.png?alt=media&#x26;token=3e5df4cb-7897-409e-aa8b-316d55959f15" alt=""><figcaption></figcaption></figure>

#### Deploy model to OpenMV device

You can then use the [OpenMV IDE](https://openmv.io/pages/download) to deploy the model to the edge device. You will need the model weights we just downloaded along with the class list which you can find in the roboflow dashboard as mentioned in this [video by OpenMV](https://www.youtube.com/watch?v=aRnn2LeAS4c). The video demonstrates this [example script](https://github.com/openmv/openmv/blob/4d7247e11e9f4605802f4e285ac65701a2079b4d/scripts/examples/03-Machine-Learning/00-TensorFlow/yolo_v8_detector.py) for running YOLOv8 (Roboflow 3.0) models on OpenMV devices and should be used as a starting point for developing with Roboflow models on OpenMV.
