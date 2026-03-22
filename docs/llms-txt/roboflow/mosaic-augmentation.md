# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/dataset-versions/image-augmentation/augmentation-types/mosaic-augmentation.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/dataset-versions/image-augmentation/augmentation-types/mosaic-augmentation.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/dataset-versions/image-augmentation/augmentation-types/mosaic-augmentation.md

# Source: https://docs.roboflow.com/datasets/dataset-versions/image-augmentation/augmentation-types/mosaic-augmentation.md

# Mosaic Augmentation

{% hint style="info" %}
Mosaic Augmentation is an Enhanced Augmentation, a **premium** feature.

For up-to-date information on our plans and their associated features, see our [pricing page](https://roboflow.com/pricing).
{% endhint %}

Add mosaic to help your model perform better on small objects.

{% hint style="danger" %}
Warning: Many modern models apply Mosaic as an online augmentation during training; applying it twice can cause undesirable results. We do not recommend using this with Roboflow 3.0 or YOLOv8.
{% endhint %}

## Example

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2347cf534e5a3427388b281e11477df72becafab%2Fimage%20(5).png?alt=media" alt=""><figcaption><p>Original Image</p></figcaption></figure>
