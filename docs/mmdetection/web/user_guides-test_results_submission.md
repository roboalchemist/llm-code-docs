# Test Results Submission

## Panoptic segmentation test results submission

The following sections introduce how to produce the prediction results of panoptic segmentation models on the COCO test-dev set and submit the predictions to COCO evaluation server [https://competitions.codalab.org/competitions/19507].

### Prerequisites

- 

Download COCO test dataset images [http://images.cocodataset.org/zips/test2017.zip], testing image info [http://images.cocodataset.org/annotations/image_info_test2017.zip], and panoptic train/val annotations [http://images.cocodataset.org/annotations/panoptic_annotations_trainval2017.zip], then unzip them, put ‘test2017’ to `data/coco/`, put json files and annotation files to `data/coco/annotations/`.

```
# suppose data/coco/ does not exist
mkdir -pv data/coco/

# download test2017
wget -P data/coco/ http://images.cocodataset.org/zips/test2017.zip
wget -P data/coco/ http://images.cocodataset.org/annotations/image_info_test2017.zip
wget -P data/coco/ http://images.cocodataset.org/annotations/panoptic_annotations_trainval2017.zip

# unzip them
unzip data/coco/test2017.zip -d data/coco/
unzip data/coco/image_info_test2017.zip -d data/coco/
unzip data/coco/panoptic_annotations_trainval2017.zip -d data/coco/

# remove zip files (optional)
rm -rf data/coco/test2017.zip data/coco/image_info_test2017.zip data/coco/panoptic_annotations_trainval2017.zip

```