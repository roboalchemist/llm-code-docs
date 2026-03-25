# Semi-supervised Object Detection

Semi-supervised object detection uses both labeled data and unlabeled data for training. It not only reduces the annotation burden for training high-performance object detectors but also further improves the object detector by using a large number of unlabeled data.

A typical procedure to train a semi-supervised object detector is as below:

- 

Semi-supervised Object Detection

  - 

Prepare and split dataset

  - 

Configure multi-branch pipeline

  - 

Configure semi-supervised dataloader

  - 

Configure semi-supervised model

  - 

Configure MeanTeacherHook

  - 

Configure TeacherStudentValLoop

## Prepare and split dataset

We provide a dataset download script, which downloads the coco2017 dataset by default and decompresses it automatically.

```
python tools/misc/download_dataset.py

```