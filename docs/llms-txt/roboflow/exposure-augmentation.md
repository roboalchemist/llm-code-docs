# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/dataset-versions/image-augmentation/augmentation-types/exposure-augmentation.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/dataset-versions/image-augmentation/augmentation-types/exposure-augmentation.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/dataset-versions/image-augmentation/augmentation-types/exposure-augmentation.md

# Source: https://docs.roboflow.com/datasets/dataset-versions/image-augmentation/augmentation-types/exposure-augmentation.md

# Exposure Augmentation

Adjust the gamma exposure of an image to be brighter or darker. This adds variability to image exposure to help your model be more resilient to lighting and camera setting changes.

* Percent: Select the percent up to which an image will be randomly brightened or darkened. Up to 100 percent bright (completely white) or 100 percent dark (completely black).

## Example

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-2347cf534e5a3427388b281e11477df72becafab%2Fimage%20(5).png?alt=media" alt=""><figcaption><p>Original Image</p></figcaption></figure>

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-89656bf64376482efa4674df6e321fad536b5f53%2Fimage.png?alt=media" alt=""><figcaption><p>Exposure Augmentation with -10% Brightness</p></figcaption></figure>

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-904b4ae1b0842e1f9ae8a0a3cddd07384db48bac%2Fimage.png?alt=media" alt=""><figcaption><p>Exposure Augmentation with +10% Brightness</p></figcaption></figure>

## FAQ

<details>

<summary>How does exposure differ from brightness?</summary>

Exposure simulates how much light the sensor "received" — similar to adjusting ISO or shutter speed in a camera.

Exposure augmentation is more faithful to real-world lighting. Bright areas get brighter faster than dark areas, preserving the image’s tonal relationships more naturally.

</details>
