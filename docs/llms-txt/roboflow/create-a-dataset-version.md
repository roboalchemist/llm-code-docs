# Source: https://docs.roboflow.com/developer/python-sdk/create-a-dataset-version.md

# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/dataset-versions/create-a-dataset-version.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/dataset-versions/create-a-dataset-version.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/dataset-versions/create-a-dataset-version.md

# Source: https://docs.roboflow.com/datasets/dataset-versions/create-a-dataset-version.md

# Create a Dataset Version

A version is a point-in-time snapshot of your dataset. We keep these versions since by keeping track of exactly which images, preprocessing, and augmentation steps were used in each iteration of your model, you maintain the ability to reproduce the results. This allows you to scientifically test across various models and frameworks while remaining confident that the results are attributable to the model changes and not due to a bug/change in the data pipeline.

<a href="../../workspaces/key-concepts" class="button primary">Key Concepts: What are Workspaces & Projects?</a>

{% hint style="info" %}
Once a version is created, it is frozen in time, which means changes to the project whether that be adding/removing images, annotations, or other data, won't affect versions that were created before.
{% endhint %}

### How To Create a Dataset Version

To create a dataset version, click "Versions" in the sidebar associated with your Roboflow project. Then, click "Generate New Version".

From this page, you can set a train/test/valid split and specify preprocessing steps and augmentations for your new dataset version.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-15210ee011b26459ed30a427ac60bdfb85934980%2FScreenshot%202023-06-22%20at%2015.37.50.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

Once you have specified the preprocessing steps and augmentations you want to apply to your data, click "Generate". This will generate a new dataset version. You can then use this dataset version to train a model in Roboflow. You can also [export your dataset](https://docs.roboflow.com/datasets/dataset-versions/exporting-data) for use in training a model manually.

### Readjusting Train/Validation/Test Splits

During the version creation process, you can also readjust the balance of your training, validation and test set splitting. To do this, go to "Step 2: Train/Test Split" and click the "Rebalance" button.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-4c91693393b132f1503c086f5ebf67f27dd9a4b9%2Fimage.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>
