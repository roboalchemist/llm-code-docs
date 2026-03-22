# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/annotate-keypoints.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/annotate-keypoints.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/annotate-keypoints.md

# Source: https://docs.roboflow.com/annotate/annotate-keypoints.md

# Annotate Keypoints

## Editing Keypoints

In Keypoint Detection projects, the annotation Bounding Box tool will include keypoints for you to position and edit. Before labelling, make sure you have [set up your Keypoint skeleton](https://docs.roboflow.com/annotate/edit-keypoint-skeletons).

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-5e2c7bba9a00f0c4fedd8fffd90a4959afbf96da%2FScreenshot%202023-12-29%20at%203.52.36%E2%80%AFPM.png?alt=media" alt="" width="563"><figcaption><p>Bounding box with keypoints inside the Annotation Tool</p></figcaption></figure>

After selecting a bounding box, you can drag each point to the correct position on the image. Each point can be right-clicked to change the point's visibility.

### Point Visibility

**Visible**: Default state for a point.

**Occluded**: Point is in image, but not visible due to being behind another object in the image. Occluded points are marked with an X in the Annotation Tool.

**Deleted**: Point is not present in the image. Either the point is not present in this object, or is outside the bounds of the image.

You can also edit point visibility by right-clicking the bounding box and selecting Edit Keypoint Visibility. From here you can edit the visibility of each point.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-6105035eb9afa2efcc42cb2395fc34fb82eae073%2FScreenshot%202023-12-29%20at%203.58.22%E2%80%AFPM.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
