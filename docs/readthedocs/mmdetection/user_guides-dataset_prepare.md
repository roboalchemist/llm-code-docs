# Dataset Prepare

## Basic Detection Dataset Preparation

MMDetection supports multiple public datasets including COCO, Pascal VOC, CityScapes, and more.

Public datasets like Pascal VOC [http://host.robots.ox.ac.uk/pascal/VOC/index.html] or mirror and COCO [https://cocodataset.org/#download] are available from official websites or mirrors. Note: In the detection task, Pascal VOC 2012 is an extension of Pascal VOC 2007 without overlap, and we usually use them together.
It is recommended to download and extract the dataset somewhere outside the project directory and symlink the dataset root to `$MMDETECTION/data` as below.
If your folder structure is different, you may need to change the corresponding paths in config files.

We provide a script to download datasets such as COCO, you can run `python tools/misc/download_dataset.py --dataset-name coco2017` to download COCO dataset.
For users in China, more datasets can be downloaded from the opensource dataset platform: OpenDataLab [https://opendatalab.com/?source=OpenMMLab%20GitHub].

For more usage please refer to dataset-download

```
mmdetection
├── mmdet
├── tools
├── configs
├── data
│   ├── coco
│   │   ├── annotations
│   │   ├── train2017
│   │   ├── val2017
│   │   ├── test2017
│   ├── cityscapes
│   │   ├── annotations
│   │   ├── leftImg8bit
│   │   │   ├── train
│   │   │   ├── val
│   │   ├── gtFine
│   │   │   ├── train
│   │   │   ├── val
│   ├── VOCdevkit
│   │   ├── VOC2007
│   │   ├── VOC2012

```