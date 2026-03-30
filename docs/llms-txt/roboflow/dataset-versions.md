# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/dataset-versions.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/dataset-versions.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/dataset-versions.md

# Source: https://docs.roboflow.com/datasets/dataset-versions.md

# Dataset Versions

Versions are point-in-time snapshots of the images and labels in your dataset. When you create a Version, you can apply preprocessing steps and augmentations to your dataset.

To train a model in Roboflow, you need to create a Dataset Version.

This section of our documentation walks through how to prepare to train a model. You will need to:

{% stepper %}
{% step %}
**Open the Versions page and create a new version**

Follow our guide to get to the [page that lets you create a dataset version](https://docs.roboflow.com/datasets/dataset-versions/create-a-dataset-version).
{% endstep %}

{% step %}
**Choose preprocessing steps**

Select the [preprocessing steps](https://docs.roboflow.com/datasets/dataset-versions/image-preprocessing) you need to train your model.
{% endstep %}

{% step %}
**Apply augmentations**

[Apply any augmentations to your dataset](https://docs.roboflow.com/datasets/dataset-versions/image-augmentation). We have a guide that walks through which augmentations are appropriate for different use cases.
{% endstep %}

{% step %}
**Confirm your Version**

Your Version will be created and will now be available for use in training models.
{% endstep %}

{% step %}
**Train a model**

Follow our [model training documentation](https://docs.roboflow.com/train/train) to configure your training job.

You can also [export a dataset version](https://docs.roboflow.com/datasets/dataset-versions/exporting-data).
{% endstep %}
{% endstepper %}
