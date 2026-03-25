# Source: https://docs.edgeimpulse.com/studio/projects/data-acquisition/data-explorer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data explorer

The data explorer is a visual tool to explore your dataset, find outliers or mislabeled data, and to help label unlabeled data. The data explorer first tries to extract meaningful features from your data (through signal processing and neural network embeddings) and then uses a dimensionality reduction algorithm to map these features to a 2D space. This gives you a one-look overview of your complete dataset.

<Frame caption="Showing a keywords dataset, unlabeled data marked in gray.">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-explorer-unlabelled.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=63bf7a89f816ac7fe92e41bce69a0488" width="1600" height="986" data-path=".assets/images/data-explorer-unlabelled.png" />
</Frame>

<Info>
  The **Data explorer** tab is available for audio classification, image classification and regression projects only.
</Info>

### Using the data explorer

To access the data explorer head to **Data acquisition**, click **Data explorer**, then select a way to generate the data explorer. Depending on you data you'll see three options:

* Using a pre-trained model - here we use a large neural network trained on a varied dataset to generate the embeddings. This works very well if you don't have any labeled data yet, or want to look at new clusters of data. This option is available for keywords and for images.
* Using your trained impulse - here we use the neural network block in your impulse to generate the embeddings. This typically creates even better visualizations, but will fail if you have completely new clusters of data as the neural network hasn't learned anything about them. This option is only available if you have a trained impulse.
* Using the preprocessing blocks in your impulse - here we skip the embeddings, and just use your selected signal processing blocks to create the data explorer. This creates a similar visualization as the [feature explorer](https://edgeimpulse.com/blog/visualizing-complex-datasets-in-edge-impulse) but in a 2D space and with extra labeling tools. This is very useful if you don't have any labeled data yet, or if you have new clusters of data that your neural network hasn't learned yet.

<Frame caption="Selecting a way to generate the data explorer">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-explorer-generating.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=71e648d41c8570d63a55c9e89634f9bb" width="943" height="622" data-path=".assets/images/data-explorer-generating.png" />
</Frame>

Then click Generate data explorer to create the data explorer. If you want to make a different choice after creating the data explorer click ⋮ in the top right corner and select Clear data explorer.

<Info>
  Want to see examples of the same dataset visualized in different ways? Scroll down!
</Info>

#### Viewing and modifying data

To view an item in your dataset just click on any of the dots (some basic information appears on hover). Information about the sample, and a preview of the data item appears at the bottom of the data explorer. You can click Set label (or l on your keyboard) to set a new label for the data item, or press Delete item (or d on your keyboard) to remove the data item. These changes are queued until you click **Save labels** (at the top of the data explorer).

<Frame caption="Changes are queued until you click 'Save labels'.">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-explorer-quee.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=b05db5a92892f1a20209cc9bff8b1420" width="1600" height="235" data-path=".assets/images/data-explorer-quee.png" />
</Frame>

### Assisted labeling

The data explorer marks unlabeled data in gray (with an 'Unlabeled' label). To label this data you click on any gray dot. To then set a label by clicking the Set label button (or by pressing `l` on your keyboard) and enter a label. Other unlabeled data in the vicinity of this item will automatically be labeled as well. This way you can quickly label clustered data.

To upload unlabeled data you can either:

* Use the [upload UI](/studio/projects/data-acquisition/uploader) and select the 'Leave data unlabeled' option.
* Select the items in your dataset under **Data acquisition**, select all relevant items, click *Edit labels* and set the label to an empty string.
* When uploading data through the [Ingestion API](/apis/ingestion), set the `x-no-label` header to 1, and the `x-label` to an empty string.

Or, if you want to start from scratch, click the three dots on top of the data explorer, and select `Clear all labels`.

### Wait, how does this work?

The data explorer uses a three-stage process:

1. It runs your data through an input and a DSP block - like any impulse.
2. It passes the result of 1) through part of a neural network. This forces the neural network to compress the DSP output even further, but to features that are highly specialized to distinguish the exact type of data in your dataset (called 'embeddings').
3. The embeddings are passed through t-SNE, a dimensionality reduction algorithm.

So what are these embeddings actually? Let's imagine you have the model from the [Continuous motion recognition tutorial](/tutorials/end-to-end/motion-recognition). Here we slice data up in 2-second windows and run a signal processing step to extract features. Then we use a neural network to classify between motions. This network consists of:

* 33 input features (from the signal processing step)
* A layer with 20 neurons
* A layer with 10 neurons
* A layer with 4 neurons (the number of different classes)

While training the neural network we try to find the mathematical formula that best maps the input to the output. We do this by tweaking each neuron (each neuron is a parameter in our formula). The interesting part is that each layer of the neural network will start acting like a feature extracting step - just like our signal processing step - but highly tuned for your specific data. For example, in the first layer, it'll learn what features are correlated, in the second it derives new features, and in the final layer, it learns how to distinguish between classes of motions.

In the data explorer we now cut off the final layer of the neural network, and thus we get the derived features back - these are called "embeddings". Contrary to features we extract using signal processing we don't really know what these features are - they're specific to your data. In essence, they provide a peek into the brain of the neural network. Thus, if you see data in the data explorer that you can't easily separate, the neural network probably can't either - and that's a great way to spot outliers - or if there's unlabeled data close to a labeled cluster they're probably very similar - great for labeling unknown data!

### Examples of different embeddings

Here's an example of using the data explorer to visualize a very complex computer vision dataset (distinguishing between the four cats of one of our infrastructure engineers).

#### No embeddings (just running t-SNE over the images)

<Frame caption="Visualizing a complex dataset of cats without embeddings">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-explorer-without-embeddings.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=235ecb6d5ba8a007bb43e9a6f2d5d100" width="1146" height="790" data-path=".assets/images/data-explorer-without-embeddings.png" />
</Frame>

#### With embeddings from a pre-trained MobileNetV2 model

<Frame caption="Visualizing a complex dataset of cats with embeddings from a pre-trained MobileNetV2 model">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-explorer-mobilenet.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=3d1350b56330871be2cc38147a2f2223" width="1600" height="961" data-path=".assets/images/data-explorer-mobilenet.png" />
</Frame>

#### With embeddings from a custom ML model

<Frame caption="Visualizing a complex dataset of cats with embeddings from a custom ML model">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-explorer-custom-ML.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=610ef5212bd8c4835f37257ead7dd0e1" width="1600" height="962" data-path=".assets/images/data-explorer-custom-ML.png" />
</Frame>

For less complex datasets, or lower-dimensional data you'll typically see more separation, even without custom models.

### Questions? Excited?

If you have any questions about the data explorer or embeddings, we'd be happy to help on the [forums](https://forum.edgeimpulse.com/) or reach out to your solutions engineer. Excited? [Talk to us](https://edgeimpulse.com/pricing) to get access to the data explorer, and finally be able to label all that sensor data you've collected!


Built with [Mintlify](https://mintlify.com).