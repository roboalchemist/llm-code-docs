# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/dataset-versions/image-augmentation/augmentation-types/brightness-augmentation.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/dataset-versions/image-augmentation/augmentation-types/brightness-augmentation.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/dataset-versions/image-augmentation/augmentation-types/brightness-augmentation.md

# Source: https://docs.roboflow.com/datasets/dataset-versions/image-augmentation/augmentation-types/brightness-augmentation.md

# Brightness Augmentation

Add variability to image brightness to help your model be more resilient to lighting and camera setting changes. From the percentage that you select, can choose to either brighten your images, darken them, or both.

## Example

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2347cf534e5a3427388b281e11477df72becafab%2Fimage%20(5).png?alt=media" alt=""><figcaption><p>Original Image</p></figcaption></figure>

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-a19af029f2604f37fdaac3e422402eb229579b2b%2Fimage.png?alt=media" alt=""><figcaption><p>Brightness Augmentation set to 10% Lighten</p></figcaption></figure>

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c8ad65ceb5798c6329b51a9574699d5843d45bf5%2Fimage.png?alt=media" alt=""><figcaption><p>Brightness Augmentation set to 10% Darken</p></figcaption></figure>

## FAQs

<details>

<summary>How does brightness differ from exposure?</summary>

Brightness augmentation makes the image uniformly lighter or darker by adding a constant value to all pixels.

Brightness does not respect relative intensity. Shadows and highlights may shift equally, leading to potential loss of contrast.

</details>
