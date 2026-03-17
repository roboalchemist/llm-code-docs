# Inference with existing models

MMDetection provides hundreds of pre-trained detection models in Model Zoo [https://mmdetection.readthedocs.io/en/latest/model_zoo.html].
This note will show how to inference, which means using trained models to detect objects on images.

In MMDetection, a model is defined by a configuration file [https://mmdetection.readthedocs.io/en/latest/user_guides/config.html] and existing model parameters are saved in a checkpoint file.

To start with, we recommend RTMDet [https://github.com/open-mmlab/mmdetection/tree/main/configs/rtmdet] with this configuration file [https://github.com/open-mmlab/mmdetection/blob/main/configs/rtmdet/rtmdet_l_8xb32-300e_coco.py] and this checkpoint file [https://download.openmmlab.com/mmdetection/v3.0/rtmdet/rtmdet_l_8xb32-300e_coco/rtmdet_l_8xb32-300e_coco_20220719_112030-5a0be7c4.pth]. It is recommended to download the checkpoint file to `checkpoints` directory.

## High-level APIs for inference - `Inferencer`

In OpenMMLab, all the inference operations are unified into a new interface - Inferencer. Inferencer is designed to expose a neat and simple API to users, and shares very similar interface across different OpenMMLab libraries.
A notebook demo can be found in demo/inference_demo.ipynb [https://github.com/open-mmlab/mmdetection/blob/main/demo/inference_demo.ipynb].

### Basic Usage

You can get inference results for an image with only 3 lines of code.

```
from mmdet.apis import DetInferencer

# Initialize the DetInferencer
inferencer = DetInferencer('rtmdet_tiny_8xb32-300e_coco')

# Perform inference
inferencer('demo/demo.jpg', show=True)

```