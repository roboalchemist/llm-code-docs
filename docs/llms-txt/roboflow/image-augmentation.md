# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/dataset-versions/image-augmentation.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/dataset-versions/image-augmentation.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/dataset-versions/image-augmentation.md

# Source: https://docs.roboflow.com/datasets/dataset-versions/image-augmentation.md

# Image Augmentation

Image augmentation is a step where augmentations are applied to existing images marked as "Train" in your dataset. This process can help improve the ability of your model to generalize and thus perform more effectively on unseen images.

{% hint style="success" %}
We recommend starting a project with no augmentations. This allows you to evaluate the quality of your raw dataset. If you add augmentations and your dataset doesn't perform as well as expected, you will not have a baseline to which you can compare model performance.

If your model doesn't perform well without augmentations, you may need to investigate class balance, data representation, and dataset size. When you have a dataset on which you have successfully trained a model without augmentations, you can add augmentations to further help improve model performance.
{% endhint %}

Augmentations are applied through a dataset version ("offline augmentation") rather than at the time of training for a few key reasons:

1. **Model reproducibility is increased**. With Roboflow, you have a copy of how each image was augmented. For example, you may find your model performs better on bright images rather than dark images, so you should collect more low-light training data.
2. **Training time is decreased**. Augmentations are CPU-constrained operations. When you’re training on your GPU and conducting augmentations on-the-fly, your GPU is often waiting for your CPU to provide augmented data at each epoch. That adds up!
3. **Training costs are decreased**. Because augmentations are CPU-constrained operations, your expensive, rented GPU is often waiting to be fed images for training.

## How Augmentations Are Applied

Augmentations are always applied to training images after [preprocessing steps](https://docs.roboflow.com/datasets/dataset-versions/image-preprocessing). The selected augmentations are stacked together, with randomization for the augmentation settings, and values for each setting, applied to each augmented image. Any images that appear as duplicates during this process are filtered out of the created version.

For example, if you select augmentations to “flip horizontally” and “salt and pepper noise,” a given image will randomly be reflected as a horizontal flip and receive random salt and pepper noise.

### Limiting Augmentations

When creating a dataset version with augmentations, you can select the maximum number of augmented images to include through the "Maximum Version Size" option.

For example, selecting 3x means that your final dataset version will contain each training source image with [preprocessing steps](https://docs.roboflow.com/datasets/dataset-versions/image-preprocessing) applied and 2 random augmentations of each image based on the settings you select.

If you had 100 images in your dataset with a train/valid/test split of 70/20/10 and selected 3x augmentations, your final dataset would roughly have a 210/20/10 split.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6e1eab9e86e8e1271b32261c1f214c503ed7afc7%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Your version's final number of images may be smaller than this estimate because we de-duplicate images and certain options (like "Filter Null") can remove images from the output.
{% endhint %}

## Augmentation Options

Augmentations in Roboflow can either be "Basic" or "Enhanced" and can be applied at two different levels.

### Image Level Augmentations

Image level augmentations create new training data by applying transformations to the entire image rather than individual objects or regions. By modifying the full image, developers can simulate a wider range of visual conditions, helping models learn to generalize better to new data.

### Bounding Box Level Augmentations

Bounding box level augmentation creates new training data by only altering the content of a source image’s bounding boxes. In doing so, developers have greater control over creating training data that is more suitable to their problem’s conditions.

A [2019 paper](https://arxiv.org/pdf/1906.11172.pdf) from Google researchers introduces the idea of using bounding box only augmentation to create optimal data for their models. In this paper, researchers showed bounding box only modifications create systemic improvements, especially for models that were fit on small datasets.

{% hint style="info" %}
Enhanced Augmentations and Bounding Box Augmentations are **premium** features.

For up-to-date information on our plans and their associated features, see our [pricing page](https://roboflow.com/pricing).
{% endhint %}

<table><thead><tr><th></th><th data-type="checkbox">Image Level Augmentation</th><th data-type="checkbox">Bounding Box Augmentation</th><th>Augmentation Type<select><option value="Z8F06MhppTfn" label="Enhanced" color="blue"></option><option value="sdEDfdaf9Z03" label="Basic" color="blue"></option></select></th></tr></thead><tbody><tr><td><a href="image-augmentation/augmentation-types/flip-augmentation">Flip Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/90o-rotate-augmentation">90ª Rotate Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/crop-augmentation">Crop Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/rotation-augmentation">Rotation Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/shear-augmentation">Shear Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/grayscale-augmentation">Grayscale Augmentation</a></td><td>true</td><td>false</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/hue-augmentation">Hue Augmentation</a></td><td>true</td><td>false</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/saturation-augmentation">Saturation Augmentation</a></td><td>true</td><td>false</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/brightness-augmentation">Brightness Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/exposure-augmentation">Exposure Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/blur-augmentation">Blur Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/noise-augmentation">Noise Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/camera-gain-augmentation">Camera Gain Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/motion-blur-augmentation">Motion Blur Augmentation</a></td><td>true</td><td>true</td><td><span data-option="sdEDfdaf9Z03">Basic</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/cutout-augmentation">Cutout Augmentation</a></td><td>true</td><td>false</td><td><span data-option="Z8F06MhppTfn">Enhanced</span></td></tr><tr><td><a href="image-augmentation/augmentation-types/mosaic-augmentation">Mosaic Augmentation</a></td><td>true</td><td>false</td><td><span data-option="Z8F06MhppTfn">Enhanced</span></td></tr></tbody></table>

## Learn More

* [The Ultimate Guide for Data Augmentation](https://blog.roboflow.com/data-augmentation/)
* [How to Augment Images for Object Detection](https://blog.roboflow.com/object-detection-augmentation/)
