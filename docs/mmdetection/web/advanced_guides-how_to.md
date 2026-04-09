This tutorial collects answers to any `How to xxx with MMDetection`. Feel free to update this doc if you meet new questions about `How to` and find the answers!

# Use backbone network through MMPretrain

The model registry in MMDet, MMPreTrain, MMSeg all inherit from the root registry in MMEngine. This allows these repositories to directly use the modules already implemented by each other. Therefore, users can use backbone networks from MMPretrain in MMDetection without implementing a network that already exists in MMPretrain.

## Use backbone network implemented in MMPretrain

Suppose you want to use `MobileNetV3-small` as the backbone network of `RetinaNet`, the example config is as the following.

```
_base_ = [
    '../_base_/models/retinanet_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
# please install mmpretrain
# import mmpretrain.models to trigger register_module in mmpretrain
custom_imports = dict(imports=['mmpretrain.models'], allow_failed_imports=False)
pretrained = 'https://download.openmmlab.com/mmclassification/v0/mobilenet_v3/convert/mobilenet_v3_small-8427ecf0.pth'
model = dict(
    backbone=dict(
        _delete_=True, # Delete the backbone field in _base_
        type='mmpretrain.MobileNetV3', # Using MobileNetV3 from mmpretrain
        arch='small',
        out_indices=(3, 8, 11), # Modify out_indices
        init_cfg=dict(
            type='Pretrained',
            checkpoint=pretrained,
            prefix='backbone.')), # The pre-trained weights of backbone network in mmpretrain have prefix='backbone.'. The prefix in the keys will be removed so that these weights can be normally loaded.
    # Modify in_channels
    neck=dict(in_channels=[24, 48, 96], start_level=0))

```