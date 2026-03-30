# Train predefined models on standard datasets

MMDetection also provides out-of-the-box tools for training detection models.
This section will show how to train *predefined* models (under configs) on standard datasets i.e. COCO.

## Prepare datasets

Preparing datasets is also necessary for training. See section Prepare datasets above for details.

**Note**:
Currently, the config files under `configs/cityscapes` use COCO pre-trained weights to initialize.
If your network connection is slow or unavailable, it’s advisable to download existing models before beginning training to avoid errors.