# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/sdks/luxonis-oak.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/sdks/luxonis-oak.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/sdks/luxonis-oak.md

# Source: https://docs.roboflow.com/deploy/sdks/luxonis-oak.md

# Luxonis OAK

The [Luxonis OAK (OpenCV AI Kit)](https://shop.luxonis.com/) is an edge device that is popularly used for the deployment of embedded computer vision systems.

OAK devices are paired with a host machine that drives the operation of the downstream application. For some exciting inspiration, see [Luxonis's use cases](https://docs.luxonis.com/en/latest/#example-use-cases) and [Roboflow's case studies](https://blog.roboflow.com/tag/case-studies/).

**By the way:** if you don't have your OAK device yet, you can [buy one via the Roboflow Store](https://store.roboflow.com/) to get a 10% discount.

### Task Support

The following task types are supported by the hosted API:

| Task Type                                                                                                                                       | Supported by Luxonis OAK Deployment |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| <p>Object Detection:</p><ul><li>YOLOv8 models, trained on Roboflow, both Fast and Accurate</li><li>YOLOv11 models trained on Roboflow</li></ul> | ✅                                   |
| Classification                                                                                                                                  |                                     |
| Instance Segmentation                                                                                                                           |                                     |
| Semantic Segmentation                                                                                                                           |                                     |

### Deploy a Model to the Luxonis OAK

#### Supported Luxonis Devices and Host Requirements

The Roboflow Inference Server supports the following devices:

* OAK-D
* OAK-D-Lite
* OAK-D-POE
* OAK-1 (no depth)

#### Installation

Install the `roboflowoak`, `depthai`, and `opencv-python` packages:

```python
pip install roboflowoak
pip install depthai
pip install opencv-python
```

Now you can use the `roboflowoak` package to run your custom trained Roboflow model.

#### Running Inference: Deployment

If you are deploying to an OAK device without Depth capabilities, set `depth=False` when instantiating (creating) the `rf` object. OAK's with Depth have a "D" attached to the model name, i.e OAK-D and OAK-D-Lite.

Also, comment out `max_depth = np.amax(depth)` and `cv2.imshow("depth", depth/max_depth)`

```python
from roboflowoak import RoboflowOak
import cv2
import time
import numpy as np

if __name__ == '__main__':
    # instantiating an object (rf) with the RoboflowOak module
    rf = RoboflowOak(model="YOUR-MODEL-ID", confidence=0.05, overlap=0.5,
    version="YOUR-MODEL-VERSION-#", api_key="YOUR-PRIVATE_API_KEY", rgb=True,
    depth=True, device=None, blocking=True)
    # Running our model and displaying the video output with detections
    while True:
        t0 = time.time()
        # The rf.detect() function runs the model inference
        result, frame, raw_frame, depth = rf.detect()
        predictions = result["predictions"]
        #{
        #    predictions:
        #    [ {
        #        x: (middle),
        #        y:(middle),
        #        width:
        #        height:
        #        depth: ###->
        #        confidence:
        #        class:
        #        mask: {
        #    ]
        #}
        #frame - frame after preprocs, with predictions
        #raw_frame - original frame from your OAK
        #depth - depth map for raw_frame, center-rectified to the center camera
        
        # timing: for benchmarking purposes
        t = time.time()-t0
        print("FPS ", 1/t)
        print("PREDICTIONS ", [p.json() for p in predictions])

        # setting parameters for depth calculation
        # comment out the following 2 lines out if you're using an OAK without Depth
        max_depth = np.amax(depth)
        cv2.imshow("depth", depth/max_depth)
        # displaying the video feed as successive frames
        cv2.imshow("frame", frame)
    
        # how to close the OAK inference window / stop inference: CTRL+q or CTRL+c
        if cv2.waitKey(1) == ord('q'):
            break
```

Enter the code below (after replacing the placeholder text with the path to your Python script)

```python
# To close the window (interrupt or end inference), enter CTRL+c on your keyboard
python3 /path/to/[YOUR-PYTHON-FILE].py
```

The inference speed (in milliseconds) with the Apple Macbook Air (M1) as the host device averaged around 15 ms, or 66 FPS. ***Note**: The host device used with OAK will drastically impact FPS. Take this into consideration when creating your system.*

#### Troubleshooting

If you are experiencing issues setting up your OAK device, visit Luxonis' installation instructions and be sure that you can run the RGB example successfully on the [Luxonis installation](https://docs.luxonis.com/en/latest/#demo-script). You can also post for help on the [Roboflow Forum](https://discuss.roboflow.com/).

### See Also

* [Step-by-step Luxonis OAK setup guide](https://blog.roboflow.com/opencv-ai-kit-deployment/)
* [Installation issue when using M1 Chip · Issue #299 · luxonis/depthai · GitHub](https://github.com/luxonis/depthai/issues/299) (depthai SDK)
