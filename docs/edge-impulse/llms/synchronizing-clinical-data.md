# Source: https://docs.edgeimpulse.com/knowledge/guides/reference-designs/health-reference-design/synchronizing-clinical-data.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Synchronizing clinical data with a bucket

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

In this section, we will show how to synchronize research data with a bucket in your organizational dataset. The goal of this step is to gather data from different sources and sort them to obtain a sorted dataset. We will then validate this dataset in the next section.

The reference design described in the [health reference design](/knowledge/guides/reference-designs/health-reference-design) [PPG-DaLiA DOI 10.24432/C53890](https://archive.ics.uci.edu/dataset/495/ppg+dalia) is a publicly available dataset for PPG-based heart rate estimation. This multimodal dataset features physiological and motion data, recorded from both a wrist- and a chest-worn device, of 15 subjects while performing a wide range of activities under close to real-life conditions. The included ECG data provides heart rate ground truth. The included PPG- and 3D-accelerometer data can be used for heart rate estimation, while compensating for motion artefacts. Details can be found in the dataset's readme-file.

| **File Name**    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S1\_activity.csv | Data containing labels of the activities.                                                                                                                                                                                                                                                                                                                                                                        |
| S1\_quest.csv    | Data from the questionnaire, detailing the subjects' attributes.                                                                                                                                                                                                                                                                                                                                                 |
| ACC.csv          | Data from 3-axis accelerometer sensor. The accelerometer is configured to measure acceleration in the range \[-2g, 2g]. Therefore, the unit in this file is 1/64g. Data from x, y, and z axis are respectively in the first, second, and third column.                                                                                                                                                           |
| BVP.csv          | Blood Volume Pulse (BVP) signal data from photoplethysmograph.                                                                                                                                                                                                                                                                                                                                                   |
| EDA.csv          | Electrodermal Activity (EDA) data expressed as microsiemens (μS).                                                                                                                                                                                                                                                                                                                                                |
| tags.csv         | Tags for the data, e.g., Stairs, Soccer, Cycling, Driving, Lunch, Walking, Working, Clean Baseline, No Activity.                                                                                                                                                                                                                                                                                                 |
| HR.csv           | Heart Rate (HR) data, as measured by the wearable device. Average heart rate extracted from the BVP signal. The first row is the initial time of the session expressed as a Unix timestamp in UTC. The second row is the sample rate expressed in Hz.                                                                                                                                                            |
| IBI.csv          | Inter-beat Interval (IBI) data. Time between individual heartbeats extracted from the BVP signal. No sample rate is needed for this file. The first column is the time (relative to the initial time) of the detected inter-beat interval expressed in seconds (s). The second column is the duration in seconds (s) of the detected inter-beat interval (i.e., the distance in seconds from the previous beat). |
| TEMP.csv         | Data from temperature sensor expressed in degrees on the Celsius (°C) scale.                                                                                                                                                                                                                                                                                                                                     |
| info.txt         | Metadata about the participant, e.g., Age, Gender, Height, Weight, BMI.                                                                                                                                                                                                                                                                                                                                          |

You can download the complete set of subject 1 files here:

[Download zip](https://cdn.edgeimpulse.com/datasets/HRV/S1.zip)

We've mimicked a proper research study, and have split the data up into two locations.

* Initial subject files (ACC.csv, BVP.csv, EDA.csv, HR.csv, IBI.csv, TEMP.csv, info.txt, S1\_activity.csv, tags.csv) live in the company data lake in S3. The data lake uses an internal structure with non-human readable IDs for each participant (e.g. Subject 1 as `S1_E4` for anonymized data):

```
Clinical_Dataset/
├── S1_E4/
│   ├── ACC.csv
│   ├── BVP.csv
│   ├── EDA.csv
│   ├── HR.csv
│   ├── IBI.csv
│   ├── TEMP.csv
│   ├── info.txt
│   ├── S1_activity.csv
│   ├── tags.csv
```

* Other files are uploaded by the research partner to an [upload portal](/studio/organizations/upload-portals). The files are prefixed with the subject ID:

```
├── S2_E4/
│   ├── ACC.csv
│   ├── BVP.csv
│   ├── EDA.csv
│   ├── HR.csv
│   ├── IBI.csv
│   ├── TEMP.csv
│   ├── info.txt
│   ├── S2_activity.csv
│   ├── tags.csv
```

with the directory `S2_E4` indicating that this data is from the second subject in the study, or prefixing the files with `S2_` (e.g. `S2_activity.csv`).

<Frame caption="Research data upload portal used by research partners">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/research-data-upload-portal.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=fb005aeba3090c726b3f0ff04e308c72" width="1536" height="1000" data-path=".assets/images/research-data-upload-portal.png" />
</Frame>

### Anonymizing your data (optional)

This is a manual step that some countries regulations may require, this example is for reference, but not needed or used in this example.

To create the mapping between the study ID, subjects name, and the internal data lake ID we can use a study master sheet. It contains information about all participants, ID mapping, and metadata. E.g.:

```
Subject     Internal ID     Study date     Age     BMI
Subject_1 S1_E4         2022-01-01     25     22.5
Subject_2 S2_E4         2022-01-02     30     23.5
```

*Notes: This master sheet was made using a Google Sheet but can be anything. All data (data lake, portal, output) are hosted in an Edge Impulse S3 bucket but can be stored anywhere (see below).*

### Configuring a storage bucket for your dataset

Data is stored in cloud storage buckets that are hosted in your own infrastructure. To configure a new storage bucket, head to your organization, choose **Data > Buckets**, click **Add new bucket**, and fill in your access credentials. For additional details, refer to [Cloud data storage](/studio/organizations/data/cloud-data-storage). Our solution engineers are also here to help you set up your buckets.

<Frame caption="Storage buckets overview with a single bucket configured.">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-org-bucket.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=deb8794f387fd01acb053861d084e474" width="1600" height="797" data-path=".assets/images/studio-org-bucket.png" />
</Frame>

#### About datasets

With the storage bucket in place you can create your first dataset. Datasets in Edge Impulse have three layers:

Datasets in Edge Impulse have three layers:

1. **Dataset**: A larger set of data items grouped together.
2. **Data item**: An item with metadata and  **Data file** attached.
3. **Data file**: The actual files.

### Adding research data to your organization

There are three ways of uploading data into your organization. You can either:

1. Upload data directly to the storage bucket (recommended method). In this case use **Add data... > Add dataset from bucket** and the data will be discovered automatically.
2. Upload data through the [Edge Impulse API](/apis/studio).
3. Upload the files through the [Upload Portals](/studio/organizations/upload-portals).

### Sorter and combiner

#### Sorter

The **sorter** is the first step of the [research pipeline](/studio/organizations/data-pipelines). Its job is to fetch the data from all locations (here: internal data lake, portal, metadata from study master sheet) and create a research dataset in Edge Impulse. It does this by:

1. Creating a new structure in S3 like this:

   ```
   S1_E4
   |_ info.txt
   |_ s1_activity.csv
   |_ acc.csv
   |_ bvp.csv
   |_ eda.csv
   |_ hr.csv
   |_ ibi.csv
   |_ temp.csv
   |_ tags.csv
   S2_E4
   |_ info.txt
   |_ s2_activity.csv
   |_ acc.csv
   |_ bvp.csv
   |_ eda.csv
   |_ hr.csv
   |_ ibi.csv
   |_ temp.csv
   |_ tags.csv
   ```

   ```
   ```

2. [Syncing the S3 folder](/studio/organizations/data) with a research dataset in your Edge Impulse organization (like `PPG-DaLiA Activity Study 2024`).

3. Updating the metadata with the metadata from the master sheet (`Age`, `BMI`, etc...). Read on how to [add and sync S3 data](/studio/organizations/data)

#### Combiner

With the data sorted we then:

1. Need to verify that the data is correct (see [validate your research data](/knowledge/guides/reference-designs/health-reference-design/validating-clinical-data))
2. Combine the data into a single Parquet file. This is essentially the contract we have for our dataset. By settling on a standard format (strong typed, same column names everywhere) this data is now ready to be used for ML, new algorithm development, etc. Because we also add metadata for each file here we're very quickly building up a valuable R\&D datastore.

<Info>
  #### No required format for data files

  There is no required format for data files. You can upload data in any format, whether it's CSV, Parquet, or a proprietary data format.

  Parquet is a columnar storage format that is optimized for reading and writing large datasets. It is particularly useful for data that is stored in S3 buckets, as it can be read in parallel and is highly compressed. That is why we are converting the data to Parquet in the transform block code.

  See [Parquet](https://parquet.apache.org/) for more information. or an example in our [Create a Transform Block Doc](/knowledge/guides/reference-designs/health-reference-design/transforming-clinical-data)
</Info>

All these steps can be run through different [transformation blocks](/studio/organizations/custom-blocks/custom-transformation-blocks) and executed one after the other using [data pipelines](/studio/organizations/data-pipelines).

<Frame caption="Clinical dataset overview">
  <img src="https://mintcdn.com/edgeimpulse/rTWxVUHegAMX0AbN/.assets/images/research-data-dataset.png?fit=max&auto=format&n=rTWxVUHegAMX0AbN&q=85&s=aff9749b2630820086b1004a078391cc" width="1588" height="1000" data-path=".assets/images/research-data-dataset.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).