# Source: https://docs.roboflow.com/changelog/explore-by-month/november-2025/find-objects-with-ai-annotation-tool.md

# Find Objects with AI Annotation Tool

<figure><img src="https://2667452268-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMR3m936tBXGm5QsAcPwe%2Fuploads%2FuO5LFKvBCvibpmkgzpiP%2FScreenshot%202025-11-19%20at%2017.15.54.png?alt=media&#x26;token=b1bed055-1f59-4ab6-b292-f3c4a8a2912d" alt=""><figcaption></figcaption></figure>

Roboflow Annotate now has a "Find Objects with AI" button that lets you provide text prompts for use in labeling an image. This button appears when annotating a single image in Roboflow Annotate.

When you click the button, a window will appear in which you can specify one or more prompts for objects to find. Roboflow will then use SAM 3 to identify the objects and return segmentation masks that can be used for instance segmentation datasets. If you are labeling an object detection dataset, the masks will be automatically converted into polygons for use in training.

You can use this feature in both object detection and instance segmentation projects.
