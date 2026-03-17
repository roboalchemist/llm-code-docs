# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/ai-labeling/model-assisted-labeling.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/ai-labeling/model-assisted-labeling.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/ai-labeling/model-assisted-labeling.md

# Source: https://docs.roboflow.com/annotate/ai-labeling/model-assisted-labeling.md

# Label Assist

{% hint style="info" %}
Label Assist is one of many [AI Labeling](https://docs.roboflow.com/annotate/ai-labeling) features. Using this feature will consume [credits](https://docs.roboflow.com/billing/credits) at the rates listed on our [credits page](https://roboflow.com/credits).
{% endhint %}

Label Assist allows you to use a previous version of a trained model or a public model on Roboflow Universe as an annotation assistant. Model-assisted labeling is ideal for identifying specific classes in an image automatically.

When model-assisted labeling is enabled, the selected model will run when you open an image in the annotation tool. The model will predict objects in the image. Annotations are added for each object the model finds.

## How to Use Label Assist

Open an image in Roboflow Annotate then click the magic wand icon in the command tray.

{% hint style="info" %}
Label Assist is currently supported on select project types. If there's a project type you'd like to see supported, let us know!
{% endhint %}

A pop-up will appear asking what model you want to use to help you label images:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-a5133c338441264b329ad7fb96f6f34dfcc974e9%2FScreenshot%202023-07-05%20at%2012.05.47.png?alt=media" alt="" width="375"><figcaption></figcaption></figure>

Select a model from the pop up. You can select a model to which you have access through the `Your Models` tab. You can select any model from Universe through the `Public Models` tab. You need to star a model on Universe before it will show up in the `Public Models` tab.

Click "Continue" once you have selected a model.

Next, you will be asked what classes you want to find. By default, the selected model will return predictions for all classes. You can uncheck classes the model should return from the pop up.

If you want to remap any class names, you can do so. This is useful if the model you are using has different class names from the classes you want to add to images in your dataset.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-c9e95415f8814925c103d31a72561e8d09be2c38%2FScreenshot%202023-07-05%20at%2012.08.49.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Once you have configured the classes for use with the selected model, click the "Select Classes" button. You will then be able to start Label Assist.

Label Assist will start running on the current image you are annotating. Label Assist will persist as you navigate through images in your dataset using the forward and back arrows in the annotation interface.

Here is an example of Label Assist recommending an annotation:

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-0537ae287ab5c5978ecbde5f53118b95644b3cbe%2FScreenshot%202023-07-05%20at%2012.13.56.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>
