# Source: https://docs.edgeimpulse.com/tutorials/integrations/nvidia-omniverse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# NVIDIA Omniverse

[NVIDIA Omniverse™](https://developer.nvidia.com/omniverse) is a scalable, multi-GPU real-time reference development platform for building and operating metaverse applications and based on Pixar's Universal Scene Description and NVIDIA RTX™ technology.

<Frame caption="NVIDIA Omniverse stack">
  <img src="https://mintcdn.com/edgeimpulse/VGjHB--ZSDHOyx4y/.assets/images/nvidia-omniverse.jpeg?fit=max&auto=format&n=VGjHB--ZSDHOyx4y&q=85&s=8371c397f9db0a50cc292034db928582" width="1197" height="1000" data-path=".assets/images/nvidia-omniverse.jpeg" />
</Frame>

This tutorial describes how you can use the Edge Impulse extension within NVIDIA Omniverse to upload your synthetic datasets to your Edge Impulse project for computer vision tasks, validate your trained model locally, and view inferencing results directly in your Omniverse synthetic environment.

## Getting started with NVIDIA Omniverse

Check out [NVIDIA's documentation](https://developer.nvidia.com/omniverse/get-started) for information on getting started as a first-time user with the Omniverse platform.

### Preliminary steps

* [Create an NVIDIA Omniverse account](https://developer.nvidia.com/login)
* [Create an Edge Impulse account](https://studio.edgeimpulse.com)

Now continue with [NVIDIA's Omniverse installation guide](https://docs.omniverse.nvidia.com/prod_install-guide/prod_install-guide/overview.html).

### Installing the Edge Impulse Omniverse extension

Once you have installed NVIDIA Omniverse, you can now install the Edge Impulse extension into your Omniverse environment by [following the README in the extension's GitHub repository](https://github.com/edgeimpulse/edge-impulse-omniverse-ext).

### Generating a synthetic dataset

[Follow this tutorial](/projects/expert-network/nvidia-omniverse-replicator) by Edge Impulse expert George Igwegbe to create a synthetic dataset using NVIDIA Omniverse Replicator.

#### Note: Adding bounding boxes

In order to collect bounding box data from your scene, semantic information for the objects of interest must be specified. A comprehensive guide on how to do this can be found [here](https://docs.omniverse.nvidia.com/extensions/latest/ext_replicator/semantics_schema_editor.html).

To preview your bounding boxes, click on the icon to the right of the camera perspective button, select either tight or loose 2D bounding boxes and then "Show Window".

<Frame caption="Select Window">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/hannah/show-window.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=4c9ca409d6b42c127000cf61c7bd98d6" width="1279" height="662" data-path=".assets/images/hannah/show-window.png" />
</Frame>

You should see a popup like this:

<Frame caption="Preview Bounding Boxes">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/hannah/display.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=e640b51d179cb74290fec42e4133dafc" width="792" height="486" data-path=".assets/images/hannah/display.png" />
</Frame>

Once you have confirmed your bounding boxes, you can check "bounding\_box\_2d\_loose" and/or "bounding\_box\_2d\_tight" under the "Parameters" tab in the Synthetic Data Recorder and the bounding boxes for your recorded data will appear in the output directory:

<Frame caption="Data Recorder">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/hannah/data-recorder.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=8e561db80885c1ff4cfa2eedb148c3ef" width="501" height="466" data-path=".assets/images/hannah/data-recorder.png" />
</Frame>

Then, using the Edge Impulse extension you installed in the previous step, upload your dataset and download your trained model by following the steps below:

<Frame caption="NVIDIA Omniverse Edge Impulse extension">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/omniverse-preview-rev.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=c711a1437e272f6eb26f3b03523d4f03" width="1424" height="1000" data-path=".assets/images/omniverse-preview-rev.png" />
</Frame>

1. Create a free Edge Impulse account: [https://studio.edgeimpulse.com/](https://studio.edgeimpulse.com/)
2. Connect to your Edge Impulse project by setting your API key (this key is obtained from your Edge Impulse project **Dashboard** > **Keys** > **API Keys**), then click **Connect**
3. Once your project is connected to your Edge Impulse Omniverse extension, select either the **Data Upload** or **Classification** drop-downs:

For synthetic data collection, select **Data Upload**, then specify your dataset's local path on your computer, select the dataset category to upload to (training, testing, or anomaly), then click **Upload to Edge Impulse**:

<Frame caption="Data Upload">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/hannah/data-upload.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=c829e3c7067fa73dca5bea2a5f5f20f6" width="816" height="430" data-path=".assets/images/hannah/data-upload.png" />
</Frame>

To add bounding box data, click the checkbox next to "Add Bounding Boxes" and then specify and RGB path with your RGB images and Bounding Box path with the raw bounding box data from Replicator, then click **Upload to Edge Impulse**:

<Frame caption="Data Upload with Bounding Boxes">
  <img src="https://mintcdn.com/edgeimpulse/ykTERfSIYjBmgAC2/.assets/images/hannah/data-upload-bb.png?fit=max&auto=format&n=ykTERfSIYjBmgAC2&q=85&s=3ee9bbad1560c4cbd069d5ca753b34be" width="813" height="439" data-path=".assets/images/hannah/data-upload-bb.png" />
</Frame>

For classification tasks and to see the results of inferencing from your trained model in Omniverse, select **Classification**, then click **Classify current scene frame** to start inferencing locally on the edge within your Omniverse environment:

<Frame caption="Classification">
  <img src="https://mintcdn.com/edgeimpulse/gFdZuMrTME9p3UIR/.assets/images/omniverse-classification.png?fit=max&auto=format&n=gFdZuMrTME9p3UIR&q=85&s=841ffea362dacb1c1207680044dcd2de" width="1600" height="878" data-path=".assets/images/omniverse-classification.png" />
</Frame>

## Next steps: building a machine learning model

With everything set up you can now build your machine learning model with these tutorials:

* [Image classification](/tutorials/end-to-end/image-classification/)
* [Detect objects with bounding boxes](/tutorials/end-to-end/object-detection-bounding-boxes)
* [Detect objects with centroids (FOMO)](/tutorials/end-to-end/object-detection-centroids)

Looking to connect different sensors? The [Data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) lets you easily send data from any sensor into Edge Impulse.


Built with [Mintlify](https://mintlify.com).