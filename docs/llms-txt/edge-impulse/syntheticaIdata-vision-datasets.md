# Source: https://docs.edgeimpulse.com/tutorials/integrations/syntheticaIdata-vision-datasets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# syntheticAIdata Vision Datasets

**[Vision Datasets](https://visiondatasets.com)**  is a platform by **[syntheticAIdata](https://visiondatasets.com)** that offers curated, high-quality
computer vision datasets. These datasets consist of synthetic images designed to
provide diverse and comprehensive training data. By following this guide, you will learn how to create and upload a dataset from Vision Datasets to Edge Impulse, just like this [Screws Nuts Bolts and Washers dataset](https://studio.edgeimpulse.com/public/722959/live) that is available in Edge Impulse Studio.:

<Frame caption="Screws Nuts Bolts and Washers Dataset">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntheticAIdata/dataset-eoin.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=ab3602ac097d33d36ef5af6cd28941a4" width="1588" height="1000" data-path=".assets/images/syntheticAIdata/dataset-eoin.png" />
</Frame>

## Getting started with syntheticAIdata

This guide explains how to import image datasets from Vision Datasets into Edge
Impulse for training, testing, and deployment of computer vision models. This
integration simplifies your workflow by eliminating the need for manual data
collection or preprocessing.

<Frame caption="Vision Datasets">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntheticAIdata/vision-datasets-documentation-01.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=e8899412c74d6ea26c783e2fbd85060e" width="1600" height="889" data-path=".assets/images/syntheticAIdata/vision-datasets-documentation-01.png" />
</Frame>

## Prerequisites

* An [Edge Impulse](https://studio.edgeimpulse.com) account with a project created.
* A [Vision Datasets](https://visiondatasets.com) account (free to sign up).

## Select and upload a dataset to Edge Impulse

To get started with Vision Datasets and Edge Impulse integration, follow these steps:

1. Log in to the Vision Datasets dashboard.

<Frame caption="Vision Datasets - Screws Nuts Bolts and Washers Dataset">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntheticAIdata/vision-datasets-documentation-04.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=07974775135cee132e3db5d8077cdfe1" width="1600" height="887" data-path=".assets/images/syntheticAIdata/vision-datasets-documentation-04.png" />
</Frame>

2. Browse or search for a relevant dataset.

* Each dataset card shows:
  * Description, preview images, image count, file size, classes, version, license

3. Click **Upload to Edge Impulse** on your chosen dataset.

<Frame caption="Vision Datasets - Download or Upload to Edge Impulse">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntheticAIdata/vision-datasets-documentation-05.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=cf04163bd92cc2ea6fb44074c01d3f3e" width="704" height="281" data-path=".assets/images/syntheticAIdata/vision-datasets-documentation-05.png" />
</Frame>

4. In the popup, provide:

* **Edge Impulse API Key**
  * Find it in your Edge Impulse project:
    `Dashboard` → `Keys` → `API Keys`
* **Image volume** (number of images to upload)
* **Image resolution** (e.g., 96×96, 320×320, 512×512)
* **Classes to include** (select one or more)

<Frame caption="Vision Datasets - Classes to include">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntheticAIdata/vision-datasets-documentation-06.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=06878549fe1c7704038328e460382f85" width="932" height="894" data-path=".assets/images/syntheticAIdata/vision-datasets-documentation-06.png" />
</Frame>

<Info>
  Example: Selecting 500 images and 2 classes uploads 1,000 images (500 per class).\*
</Info>

5. Click **Upload** to start the transfer.
6. After upload, you’ll see a success confirmation.

<Frame caption="Vision Datasets - Confirmation">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntheticAIdata/vision-datasets-documentation-07.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=c9c882166dde0591827ba1f46857ad98" width="612" height="102" data-path=".assets/images/syntheticAIdata/vision-datasets-documentation-07.png" />
</Frame>

All data appears under **Data Acquisition** in Edge Impulse, pre-labeled and ready to use.

<Info>
  You can also use **Download** to export the dataset locally for inspection.
</Info>

## Review and verify data in Edge Impulse

1. Go to [Edge Impulse Studio](https://studio.edgeimpulse.com) and open your project.
2. Navigate to **Data Acquisition**.
3. Review your uploaded images:

* Correct labels (per selected class)
* Selected resolution
* Training/testing split

4. Use filters or search to explore specific classes or subsets.
5. Click any image to preview.

<Frame caption="Vision Datasets - Preview image">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntheticAIdata/vision-datasets-documentation-08.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=74d0b9162e342dfefc39d0b1ffb9aaa0" width="1600" height="770" data-path=".assets/images/syntheticAIdata/vision-datasets-documentation-08.png" />
</Frame>

<Info>
  Verifying your data ensures high-quality inputs for your pipeline.
  To rebalance or modify your dataset, repeat the upload or manually add/remove data.
</Info>

You can repeat uploads with different classes, resolutions, or volumes anytime from Vision Datasets.

<Frame caption="Vision Datasets - Enter Project API Key">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntheticAIdata/vision-datasets-documentation-06.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=06878549fe1c7704038328e460382f85" width="932" height="894" data-path=".assets/images/syntheticAIdata/vision-datasets-documentation-06.png" />
</Frame>

## Summary

By combining the breadth of **Vision Datasets** with the edge-deployment power of **Edge Impulse**, you can go from zero images to a fully-trained, device-ready model in record time. Try the integration yourself and let us know what you build!

Head over to **[visiondatasets.com](https://visiondatasets.com)**, grab a free sample, and start building computer-vision models faster than ever.

## Next steps: building a machine learning model

With everything set up you can now build your first machine learning model with these tutorials:

* [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* [Sound recognition](/tutorials/end-to-end/sound-recognition)
* [Image classification](/tutorials/end-to-end/image-classification/)
* [Detect objects with bounding boxes](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Detect objects with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

### Troubleshooting

If you encounter issues during the registration or upload process, here are some common troubleshooting steps:

**Unable to Register or Receive Confirmation Email**

* Check spam/junk folders.
* Ensure your email is correct.
* Resend the code or use a different email if needed.

<Frame caption="Vision Datasets - Upload confirmed">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntheticAIdata/vision-datasets-documentation-07.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=c9c882166dde0591827ba1f46857ad98" width="612" height="102" data-path=".assets/images/syntheticAIdata/vision-datasets-documentation-07.png" />
</Frame>

**Edge Impulse API Key Not Accepted**

* Use an API key from your Edge Impulse project (`Dashboard` → `Keys` → `API Keys`).
* Remove extra spaces/characters.
* Generate a new API key if needed.

**Data Not Labeled in Edge Impulse Studio**

* In Edge Impulse Studio, go to **Dashboard**.
* On the **Project info** card, set **Labeling method** to *Bounding boxes (object detection)* for correct labeling and display.

<Frame caption="Vision Datasets - Label with another method">
  <img src="https://mintcdn.com/edgeimpulse/kO1SQOWn4i-BYeHy/.assets/images/syntheticAIdata/vision-datasets-documentation-09.png?fit=max&auto=format&n=kO1SQOWn4i-BYeHy&q=85&s=18e5079ebe17bcf1ebf0974b54cacb1b" width="536" height="253" data-path=".assets/images/syntheticAIdata/vision-datasets-documentation-09.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).