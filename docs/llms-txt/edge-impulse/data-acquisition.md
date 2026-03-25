# Source: https://docs.edgeimpulse.com/studio/projects/data-acquisition.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Data acquisition

All collected data for each project can be viewed on the **Data acquisition** tab. You can see how your data has been split for train/test set as well as the data distribution for each class in your dataset. You can also send new sensor data to your project either by file upload, WebUSB, Edge Impulse API, or Edge Impulse CLI.

<Frame caption="Edge Impulse Studio - Data acquisition view.">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-acquisition-overview-grid-view.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=0586b88c5c8834caaa258553cc6dd91d" width="955" height="1000" data-path=".assets/images/studio-data-acquisition-overview-grid-view.png" />
</Frame>

## Add data to your project

<Info>
  **Organization data**

  Since the creation of Edge Impulse, we have been helping our customers deal with complex data pipelines, complex data transformation methods and complex clinical validation studies.

  The organizational data gives you tools to centralize, validate and transform datasets so they can be easily imported into your projects.

  See the [Organization data](/studio/organizations/data) documentation.
</Info>

### Collect data

The panel on the right allows you to collect data directly from any fully supported platform:

* Through [WebUSB](https://edgeimpulse.com/blog/collect-sensor-data-straight-from-your-web-browser).
* Using the [Edge Impulse CLI daemon](/tools/clis/edge-impulse-cli/serial-daemon).
* From the [Edge Impulse for Linux CLI](/tools/clis/edge-impulse-linux-cli).

The WebUSB and the Edge Impulse daemon work with any fully supported device by flashing the pre-built Edge Impulse firmware to your board. See the list of [fully supported boards](/hardware).

When using the Edge Impulse for Linux CLI, run `edge-impulse-linux --clean` and it will add your platform to the device list of your project. You will then will be able to interact with it from the **Collect data** panel.

<Info>
  **Need more?**

  If your device is not in the officially supported list, you can also collect data using the [CLI data forwarder](/tools/clis/edge-impulse-cli/data-forwarder) by directly writing the sensor values over a serial connection. The "data forwarder" then signs the data and sends it to the ingestion service.
</Info>

### Upload existing datasets

Edge Impulse also supports different [data acquisition formats](/tools/specifications/data-acquisition/json-cbor) and [dataset annotation formats](/tools/specifications/data-annotation/object-detection) (Pascal VOC, YOLO TXT, COCO JSON, Edge Impulse Object Detection, OpenImage CSV) that you can import into your project to build your edge AI models:

* [Studio uploader](/studio/projects/data-acquisition/uploader)
* [CLI uploader](/tools/clis/edge-impulse-cli/uploader)
* [CSV Wizard](/studio/projects/data-acquisition/csv-wizard)
* [Ingestion API](/apis/ingestion)
* [Import from cloud storage](/studio/organizations/data/cloud-data-storage)
* [Upload portals](/studio/organizations/upload-portals) (Enterprise feature)

<Info>
  #### Edge Impulse Datasets

  Need inspiration? Check out our [Edge Impulse datasets collection](/datasets) that contains publicly available datasets collected, generated or curated by Edge Impulse or its partners.

  These datasets highlight specific use cases, helping you understand the types of data commonly encountered in projects like object detection, audio classification, and visual anomaly detection.
</Info>

## Data sample preview

### Time-series data samples

For time-series data samples (including audio), you can visualize the time-series graphs on the right panel with a dark-blue background:

<Frame caption="Time-series data sample preview">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-sample-preview-time-series.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=c7ab4dd846c8ffdf51dd869ff19f6ccf" width="1348" height="956" data-path=".assets/images/data-acquisition-sample-preview-time-series.png" />
</Frame>

If you are dealing with multi-label data samples. Here is the corresponding preview:

<Frame caption="Multi-label sample preview">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-sample-preview-time-series-multi-label.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=968590aa74dab7a7bd12f5c3ac5c41bb" width="1344" height="956" data-path=".assets/images/data-acquisition-sample-preview-time-series-multi-label.png" />
</Frame>

### Non-time-series & pre-processed data samples

Preview the values of tabular non-time-series & pre-processed data samples:

<Frame caption="Tabular data sample preview">
  <img src="https://mintcdn.com/edgeimpulse/b53JLZcI-O3Jueox/.assets/images/tabular-data/preview.png?fit=max&auto=format&n=b53JLZcI-O3Jueox&q=85&s=37e3eed02b5e714e99cc9e63c7fd12a4" width="1332" height="1000" data-path=".assets/images/tabular-data/preview.png" />
</Frame>

### Images data samples

Raw images can be directly visualized from the preview:

<Frame caption="Raw image sample preview">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-sample-preview-images.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=9b04babef7d8f8af0b4d132ea4e359e6" width="1354" height="716" data-path=".assets/images/data-acquisition-sample-preview-images.png" />
</Frame>

For object detection projects, we can overlay the corresponding bounding boxes:

<Frame caption="Object detection sample preview">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-sample-preview-object-detection.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=48ce9e5593427df397b23d074f84e94b" width="1348" height="714" data-path=".assets/images/data-acquisition-sample-preview-object-detection.png" />
</Frame>

### Video data samples

Raw videos (.mp4) can be directly visualized from the preview. Please note that you will need to split the videos into frames as we do not support training on videos files:

<Frame caption="Video samples preview">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-sample-preview-video.gif?s=2904ed35ed080e52a407fb7cde285ca2" width="680" height="478" data-path=".assets/images/data-acquisition-sample-preview-video.gif" />
</Frame>

## Dataset overview

You can change the default view (list) to a grid view to quickly overview your datasets by clicking on the <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-change-view.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=2a580812f8a2d81bf756114501328021" alt="change view icon" width="68" height="56" data-path=".assets/images/data-acquisition-change-view.png" /> icon.

<Tabs>
  <Tab title="List view">
    #### List view

    <Frame caption="Edge Impulse Studio - Data acquisition view.">
      <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-acquisition-overview.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=d1adcec167928447121e56a2d0e7fd7e" width="1089" height="1000" data-path=".assets/images/studio-data-acquisition-overview.png" />
    </Frame>
  </Tab>

  <Tab title="Grid view">
    #### Grid view

    <Frame caption="Edge Impulse Studio - Data acquisition view.">
      <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-acquisition-overview-grid-view.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=0586b88c5c8834caaa258553cc6dd91d" width="955" height="1000" data-path=".assets/images/studio-data-acquisition-overview-grid-view.png" />
    </Frame>
  </Tab>
</Tabs>

## Dataset train/test split ratio

The train/test split is a technique for training and evaluating the performance of machine learning algorithms. It indicates how your data is split between training and testing samples. For example, an 80/20 split indicates that 80% of the dataset is used for model training purposes while 20% is used for model testing.

This section also shows how your data samples in each class are distributed to prevent imbalanced datasets which might introduce **bias** during model training.

<Frame caption="Rebalance panel">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-balance.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=9684511beb186b8eef6f5ff71811fe55" width="1296" height="1000" data-path=".assets/images/data-acquisition-balance.png" />
</Frame>

## Data acquisition filters

Manually navigating to some categories of data can be time-consuming, especially when dealing with a large dataset. The data acquisition filter enables the user to filter data samples based on some criteria of choice. This can be based on:

* **Label** - class to which a sample represents.
* **Sample name** - unique ID representing a sample.
* **Signature validity**
* **Enabled and disabled samples**
* **Length of sample** - duration of a sample.

<Frame caption="Filters">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-filters.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=f20774a26adda8ec0927c1b5c0da2b84" width="1170" height="1000" data-path=".assets/images/data-acquisition-filters.png" />
</Frame>

The filtered samples can then be manipulated by editing labels, deleting, and moving from the training set to the testing set (and vice versa), a shown in the image above.

## Data sample actions

The data manipulations above can also be applied at the data sample level by simply navigating to the individual data sample by clicking on "**⋮**" and selecting the type of action you might want to perform on the specific sample. This might be renaming, editing its label, disabling, cropping, splitting, downloading, and even deleting the sample when desired.

<Frame caption="Actions">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-sample-actions.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=2e301ed0b16bebca1e73a3415a2abad8" width="476" height="636" data-path=".assets/images/data-acquisition-sample-actions.png" />
</Frame>

### Edit label(s)

* **Single label**

<Frame caption="Edit label">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-acquition-edit-label.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=50bef949bfb1a0afd235afac2852fd33" width="1600" height="915" data-path=".assets/images/studio-data-acquition-edit-label.png" />
</Frame>

* **Multi-label**

<Frame caption="Edit labels">
  <img src="https://mintcdn.com/edgeimpulse/UMiv9oezYdq-CZ8W/.assets/images/studio-data-acquition-edit-labels.png?fit=max&auto=format&n=UMiv9oezYdq-CZ8W&q=85&s=502e2381140c480bcf8325ebc12ce634" width="1585" height="1000" data-path=".assets/images/studio-data-acquition-edit-labels.png" />
</Frame>

See [Data Acquisition -> Multi-label -> Edit multi-label samples](/studio/projects/data-acquisition/multi-label#edit-multi-label-samples) for more information.

### Cropping samples

To crop a data sample, go to the sample you want to crop and click **⋮**, then select **Crop sample**. You can specify a length, or drag the handles to resize the window, then move the window around to make your selection.

Made a wrong crop? No problem, just click **Crop sample** again and you can move your selection around. To undo the crop, just set the sample length to a high number, and the whole sample will be selected again.

<Frame caption="Crop">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-acquisition-crop.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=4ec6fa96eaa209edfb1a7ca488adffd0" width="1600" height="916" data-path=".assets/images/data-acquisition-crop.png" />
</Frame>

### Splitting data sample

Besides cropping you can also split data automatically. Here you can perform one motion repeatedly, or say a keyword over and over again, and the events are detected and can be stored as individual samples. This makes it easy to very quickly build a high-quality dataset of discrete events. To do so head to Data Acquisition, record some new data, click, and select Split sample. You can set the window length, and all events are automatically detected. If you're splitting audio data you can also listen to events by clicking on the window, the audio player is automatically populated with that specific split.

<Frame caption="Split">
  <img src="https://mintcdn.com/edgeimpulse/XrFPT-8z2fazEgaU/.assets/images/83ae234-screenshot_2020-11-19_at_222215.png?fit=max&auto=format&n=XrFPT-8z2fazEgaU&q=85&s=c39f02fb9c67afb273a32d12dfe344a6" width="1137" height="643" data-path=".assets/images/83ae234-screenshot_2020-11-19_at_222215.png" />
</Frame>

Samples are automatically centered in the window, which might lead to problems on some models (the neural network could learn a shortcut where data in the middle of the window is always associated with a certain label), so you can select "Shift samples" to automatically move the data a little bit around.

Splitting data is - like cropping data - non-destructive. If you're not happy with a split just click Crop sample and you can move the selection around easily.

## Labeling tools

The [labeling queue](/studio/projects/data-acquisition/labeling-queue) will only appear on your data acquisition page if you are dealing with **object detection tasks**.

If you are not dealing with an object detection task, you can simply change the *Labeling method configuration* by going to **Dashboard > Project info > Labeling method** and clicking the dropdown and selecting "one label per data item" as shown in the image below.

<Frame caption="Labeling method">
  <img src="https://mintcdn.com/edgeimpulse/BkCfxv-ghnIJglm7/.assets/images/labeling-method.png?fit=max&auto=format&n=BkCfxv-ghnIJglm7&q=85&s=17a729a19b3cd0c1e231ff34d4a3d64b" width="1201" height="371" data-path=".assets/images/labeling-method.png" />
</Frame>

Also, see our [Label image data using GPT-4o](/tutorials/topics/data/label-image-data-gpt-4o) tutorial to see how to leverage the power of LLMs to automatically label your data samples based on simple prompts.

## Post-Processing

The **Post-Processing** section in Data Acquisition is designed for uploading and managing video data that will be used for advanced postprocessing features, such as object tracking. Here, you can upload representative video files (e.g., footage from your production line or surveillance cameras) to configure and test postprocessing algorithms directly in Edge Impulse Studio.

This section is especially useful if you want to enable features like object tracking, which can turn raw bounding box detections into stable, persistent object identities across frames. For more information on how to use object tracking and postprocessing, see our [Object Tracking documentation](/studio/projects/post-processing/object-tracking).


Built with [Mintlify](https://mintlify.com).