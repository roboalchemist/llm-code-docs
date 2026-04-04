# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/ai-labeling.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/ai-labeling.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/ai-labeling.md

# Source: https://docs.roboflow.com/annotate/ai-labeling.md

# AI Labeling

{% hint style="info" %}
AI Labeling features use credits at the rates listed on our [credits page](https://roboflow.com/credits).
{% endhint %}

Roboflow offers four AI-powered labeling features to help speed up your Workflow:

* [Label Assist](https://docs.roboflow.com/annotate/ai-labeling/model-assisted-labeling): Use a model you have already trained to auto-label images in your dataset.
* [Smart Polygon](https://docs.roboflow.com/annotate/ai-labeling/enhanced-smart-polygon-with-sam): Use the Segment Anything Model in your browser to annotate polygon masks with a single click.
* [Box Prompting](https://docs.roboflow.com/annotate/ai-labeling/box-prompting-ai-labeling): Draw examples of an object in an image, then let Box Prompting find all other instances of that object in the image.
* [Auto Label](https://docs.roboflow.com/annotate/ai-labeling/automated-annotation-with-autodistill): Use a foundation model like Grounding DINO to auto-label all images in your dataset with a single or multiple prompts.

We recommend each solution in the following cases:

* **Label Assist**: Ideal for labeling data once you already have a trained model.
* **Enhanced Smart Polygon with SAM:** Ideal for labeling the first version of your dataset, adding new annotations that Label Assist missed, or adding annotations for new classes to a dataset.
* **Box Prompting**: Ideal if you have lots of similar objects to label in an image (i.e. if you are labeling individual screws on a tray with dozens of the same screw).
* **Auto Label**: Ideal if you need to label common objects (i.e. a vehicle) in bulk.

You can find out more about each option on their respective documentation pages.

### Supported AI Labeling Tools by Project Type

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-ed7f25623f48c20757c22133e0edace86f861992%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Supported Model Types for Use In Label Assist

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-dc1cbe626e0177a73f06dfbb9a2001d35b6a2fb8%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
