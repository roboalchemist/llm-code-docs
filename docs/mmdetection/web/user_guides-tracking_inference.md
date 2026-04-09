# Inference

We provide demo scripts to inference a given video or a folder that contains continuous images. The source codes are available here [https://github.com/open-mmlab/mmdetection/tree/tracking/demo].

Note that if you use a folder as the input, the image names there must be  **sortable** , which means we can re-order the images according to the numbers contained in the filenames. We now only support reading the images whose filenames end with `.jpg`, `.jpeg` and `.png`.

## Inference MOT models

This script can inference an input video / images with a multiple object tracking or video instance segmentation model.

```
python demo/mot_demo.py \
    ${INPUTS}
    ${CONFIG_FILE} \
    [--checkpoint ${CHECKPOINT_FILE}] \
    [--detector ${DETECTOR_FILE}] \
    [--reid ${REID_FILE}] \
    [--score-thr ${SCORE_THR}] \
    [--device ${DEVICE}] \
    [--out ${OUTPUT}] \
    [--show]

```