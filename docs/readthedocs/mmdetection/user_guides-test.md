# Test existing models on standard datasets

To evaluate a model’s accuracy, one usually tests the model on some standard datasets, please refer to dataset prepare guide to prepare the dataset.

This section will show how to test existing models on supported datasets.

## Test existing models

We provide testing scripts for evaluating an existing model on the whole dataset (COCO, PASCAL VOC, Cityscapes, etc.).
The following testing environments are supported:

- 

single GPU

- 

CPU

- 

single node multiple GPUs

- 

multiple nodes

Choose the proper script to perform testing depending on the testing environment.

```
# Single-gpu testing
python tools/test.py \
    ${CONFIG_FILE} \
    ${CHECKPOINT_FILE} \
    [--out ${RESULT_FILE}] \
    [--show]

# CPU: disable GPUs and run single-gpu testing script
export CUDA_VISIBLE_DEVICES=-1
python tools/test.py \
    ${CONFIG_FILE} \
    ${CHECKPOINT_FILE} \
    [--out ${RESULT_FILE}] \
    [--show]

# Multi-gpu testing
bash tools/dist_test.sh \
    ${CONFIG_FILE} \
    ${CHECKPOINT_FILE} \
    ${GPU_NUM} \
    [--out ${RESULT_FILE}]

```