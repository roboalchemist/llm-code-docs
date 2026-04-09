# Use a single stage detector as RPN

Region proposal network (RPN) is a submodule in Faster R-CNN [https://arxiv.org/abs/1506.01497], which generates proposals for the second stage of Faster R-CNN. Most two-stage detectors in MMDetection use `RPNHead` to generate proposals as RPN. However, any single-stage detector can serve as an RPN since their bounding box predictions can also be regarded as region proposals and thus be refined in the R-CNN. Therefore, MMDetection v3.0 supports that.

To illustrate the whole process, here we give an example of how to use an anchor-free single-stage model FCOS as an RPN in Faster R-CNN.

The outline of this tutorial is as below:

- 

Use `FCOSHead` as an `RPNHead` in Faster R-CNN

- 

Evaluate proposals

- 

Train the customized Faster R-CNN with pre-trained FCOS

## Use `FCOSHead` as an `RPNHead` in Faster R-CNN

To set `FCOSHead` as an `RPNHead` in Faster R-CNN, we should create a new config file named `configs/faster_rcnn/faster-rcnn_r50_fpn_fcos-rpn_1x_coco.py`, and replace with the setting of `rpn_head` with the setting of `bbox_head` in `configs/fcos/fcos_r50-caffe_fpn_gn-head_1x_coco.py`. Besides, we still use the neck setting of FCOS with strides of `[8, 16, 32, 64, 128]`, and update `featmap_strides` of `bbox_roi_extractor` to `[8, 16, 32, 64, 128]`. To avoid loss goes NAN, we apply warmup during the first 1000 iterations instead of the first 500 iterations, which means that the lr increases more slowly. The config is as follows:

```
_base_ = [
    '../_base_/models/faster-rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

model = dict(
    # copied from configs/fcos/fcos_r50-caffe_fpn_gn-head_1x_coco.py
    neck=dict(
        start_level=1,
        add_extra_convs='on_output',  # use P5
        relu_before_extra_convs=True),
    rpn_head=dict(
        _delete_=True,  # ignore the unused old settings
        type='FCOSHead',
        num_classes=1,  # num_classes = 1 for rpn, if num_classes > 1, it will be set to 1 in TwoStageDetector automatically
        in_channels=256,
        stacked_convs=4,
        feat_channels=256,
        strides=[8, 16, 32, 64, 128],
        loss_cls=dict(
            type='FocalLoss',
            use_sigmoid=True,
            gamma=2.0,
            alpha=0.25,
            loss_weight=1.0),
        loss_bbox=dict(type='IoULoss', loss_weight=1.0),
        loss_centerness=dict(
            type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0)),
    roi_head=dict(  # update featmap_strides due to the strides in neck
        bbox_roi_extractor=dict(featmap_strides=[8, 16, 32, 64, 128])))

# learning rate
param_scheduler = [
    dict(
        type='LinearLR', start_factor=0.001, by_epoch=False, begin=0,
        end=1000),  # Slowly increase lr, otherwise loss becomes NAN
    dict(
        type='MultiStepLR',
        begin=0,
        end=12,
        by_epoch=True,
        milestones=[8, 11],
        gamma=0.1)
]

```