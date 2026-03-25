# Finetuning Models

Detectors pre-trained on the COCO dataset can serve as a good pre-trained model for other datasets, e.g., CityScapes and KITTI Dataset.
This tutorial provides instructions for users to use the models provided in the Model Zoo for other datasets to obtain better performance.

There are two steps to finetune a model on a new dataset.

- 

Add support for the new dataset following Customize Datasets.

- 

Modify the configs as will be discussed in this tutorial.

Take the finetuning process on Cityscapes Dataset as an example, the users need to modify five parts in the config.

## Inherit base configs

To release the burden and reduce bugs in writing the whole configs, MMDetection V3.0 support inheriting configs from multiple existing configs. To finetune a Mask RCNN model, the new config needs to inherit
`_base_/models/mask-rcnn_r50_fpn.py` to build the basic structure of the model. To use the Cityscapes Dataset, the new config can also simply inherit `_base_/datasets/cityscapes_instance.py`. For runtime settings such as logger settings, the new config needs to inherit `_base_/default_runtime.py`. For training schedules, the new config can to inherit `_base_/schedules/schedule_1x.py`. These configs are in the `configs` directory and the users can also choose to write the whole contents rather than use inheritance.

```
_base_ = [
    '../_base_/models/mask-rcnn_r50_fpn.py',
    '../_base_/datasets/cityscapes_instance.py', '../_base_/default_runtime.py',
    '../_base_/schedules/schedule_1x.py'
]

```