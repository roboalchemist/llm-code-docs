# Source: https://docs.roboflow.com/roboflow/roboflow-ko/annotate/ai-labeling/box-prompting-ai-labeling.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/anotto/ai-labeling/box-prompting-ai-labeling.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/annotate/ai-labeling/box-prompting-ai-labeling.md

# Source: https://docs.roboflow.com/annotate/ai-labeling/box-prompting-ai-labeling.md

# Box Prompting

{% hint style="info" %}
Box Prompting is one of many [AI Labeling](https://docs.roboflow.com/annotate/ai-labeling) features. Using this feature will consume [credits](https://docs.roboflow.com/billing/credits) at the rates listed on our [credits page](https://roboflow.com/credits).
{% endhint %}

{% embed url="<https://www.youtube.com/watch?v=qvDRO8fRzhg>" %}
Activate Box Prompting in the annotation toolbar.
{% endembed %}

Box Prompting takes one (or more) prompt bounding boxes to generate annotations for similar objects. Each example fine-tunes a model that improves with each image. With Box Prompting, you save hours of time manually drawing bounding boxes around objects that appear multiple times in a dataset.

### Step 1: Annotate at least one example of each class

Box prompting requires you to create at least one bounding box annotation to provide as an example for generating predictions.

### Step 2: Activate the Box Prompting tool

Make sure the Box Prompting tool is active to see the magic happen! Box Prompting will generate predictions based on your annotations. Predictions will appear with dotted lines any time you save or delete an annotation.

{% hint style="info" %}
Predictions are not annotations and will not be saved when navigating away from the image. See Step 4 for how to save your predictions.
{% endhint %}

### Step 3: Fine-tune your predictions

From here, you can:

#### **Adjust the confidence**

Adjust the confidence threshold using the slider to adjust the number of predictions displayed. Higher confidence means less predictions.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-07b162e57967839d6994b874de016649369da2e3%2Fconfidence.png?alt=media" alt=""><figcaption><p>Adjust the number of predictions displayed by changing the confidence threshold.</p></figcaption></figure>

#### Provide negative examples

If any incorrect predictions occur, you can right click on the box and select "Convert to Negative". This will teach the model to not label this type of object in the future. Negative examples will appear shaded in.

You can also convert existing annotations to negative through the same right click menu.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-da8d79ecc0406a5e1d7b8cb8907cab1f40ceb488%2FConvert%20to%20Negative.gif?alt=media" alt=""><figcaption><p>Right click on incorrect predictions and <strong>Convert to Negative</strong> to provide a negative prompt.</p></figcaption></figure>

#### Add additional examples

Any additional annotations you create with other labels will help the model differentiate between different objects in the image. After adding more examples, you can click "Predict" to generate new predictions.

For best results, provide 1-2 examples of every unique object in your images.

{% hint style="info" %}
You may find it easier to fine-tune predictions by lowering the confidence & converting excess predictions to negative, rather than setting the confidence high.
{% endhint %}

### Step 4: Approve predictions

Once the predictions are to your liking, click "Approve Predictions". This will convert all predictions to annotations, and ensure they'll be saved if you navigate away.

From here, you can edit & delete annotations as usual.

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-a9e51bb5ebabae5033c97d689cfe303de52de380%2Fapprove-preds.png?alt=media" alt=""><figcaption><p>Approve predictions to save them to the image.</p></figcaption></figure>

### Step 5: Run on more images

#### As you annotate, images are added to your training set.

As you annotate images, Box Prompting will be trained on any images with human-drawn or human-edited annotations. (Predictions that are approved without edits will not be included.)

This means you can click "Predict" on new images without drawing a single box & still generate predictions! You can check the number of images included in the training set in the tool menu.

## Best Practices

#### Provide an example for each visually distinct object.

On images that contain several objects with similar appearances, it can be helpful to provide at least one example for each significant color, size or camera angle variation.

#### Annotate similar images in the same annotation session.

Box prompting works best when your images have similar contents, allowing you to quickly reuse your training examples while generating predictions.

#### Tighten bounding boxes to avoid accumulating errors.

Often, the predicted bounding box is larger than it should be - reduce the size to avoid erroneously including parts of the background.

#### Box Prompting works best on photographs or still frames.

Although we can provide predictions for documents or computer graphics, Box Prompting works best for identifying repetitive items in photos.

#### Provide negative examples to improve accuracy.

If you notice a particular annotation class produces false positive predictions, you can right click & select "Convert to Negative" to provide a negative example to the Box Prompting model.

### Limitations

The Box Prompting model has to downscale images when inferring. Therefore, when trying to detect small items on a large image you may get unsatisfactory results.

You get optimal results with images 1000px or less in either dimension, and you'll get a warning when the image is 2000px+ with small bounding boxes (less than \~5% of the width/height) that will not work well

{% hint style="info" %}
These limitations only apply to Box Prompting. When model training, you can apply Tiling as a [preprocessing step](https://docs.roboflow.com/datasets/dataset-versions/image-preprocessing) during version generation to prevent these effects for trained models.
{% endhint %}
