# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/dataset-versions/image-augmentation/augmentation-types/crop-augmentation.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/dataset-versions/image-augmentation/augmentation-types/crop-augmentation.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/dataset-versions/image-augmentation/augmentation-types/crop-augmentation.md

# Source: https://docs.roboflow.com/datasets/dataset-versions/image-augmentation/augmentation-types/crop-augmentation.md

# Crop Augmentation

Add variability to positioning and size to help your model be more resilient to subject translations and camera position.

Randomly create a subset of an image. This adds variability to positioning and size to help your model be more resilient to subject translations and camera position, increasing your model's generalizability!

* Percent: The percent area of the original image **to drop**. (e.g. The percentage area of the original image to keep. (e.g. a higher percentage contains a smaller amount of the original image.)

{% hint style="warning" %}
Annotations are affected by this augmentation. At present, our implementation drops any annotations that are completely out of frame. We crop any annotation that are partially out of frame to be in line with the edge of the image. For these kept annotations, we currently keep any amount of the original object detection area.

We will soon provide the ability for you to select what percentage of annotation area you seek to maintain -- for example, if you only want to keep annotations that have at least 80% of the area of their original bounding box.
{% endhint %}

## Example

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2347cf534e5a3427388b281e11477df72becafab%2Fimage%20(5).png?alt=media" alt=""><figcaption><p>Original Image</p></figcaption></figure>

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-870c5856081c971986b565da834ed9e18a6ee1d9%2Fimage.png?alt=media" alt=""><figcaption><p>Crop Augmentation of 20%</p></figcaption></figure>

## Learn More

* [Why and How to Implement Random Crop Data Augmentation](https://blog.roboflow.com/why-and-how-to-implement-random-crop-data-augmentation/)
