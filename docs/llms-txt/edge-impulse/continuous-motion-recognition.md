# Source: https://docs.edgeimpulse.com/datasets/time-series/continuous-motion-recognition.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Continuous motion recognition

**Task:** Motion and Vibration Classification

**License:** [BSD 3-Clause Clear](https://spdx.org/licenses/BSD-3-Clause-Clear.html)

<Frame caption="Dataset Screenshot">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/dataset-screenshot/497631.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=036c9b647ee68b71a56c8c52665aa3b8" width="1600" height="719" data-path=".assets/images/dataset-screenshot/497631.png" />
</Frame>

## Description

This is a prebuilt dataset, collected by Edge Impulse teams, for a gesture recognition system based on continuous motion, for the [Continuous Motion Recognition tutorial](/tutorials/end-to-end/motion-recognition). It contains 15 minutes of data sampled from a MEMS accelerometer at 62.5Hz over the following four classes:

* Idle - board sits idly on your desk. There might be some movement detected, e.g. from typing while the board is present.
* Snake - board moves over the desk as a snake.
* Updown - board moves up and down in a continuous motion.
* Wave - board moves left and right like you're waving to someone.

<Frame caption="Snake">
  <img src="https://usercdn.edgeimpulse.com/project497631/ba2df914cd67fa965724c3224ec2b65d00ea43feea1681941e974fe0897de5fa" />
</Frame>

<br />

<Frame caption="Updown">
  <img src="https://usercdn.edgeimpulse.com/project497631/47f414795c67a7f729448373dccdaaea1aed3b56e394d454d72a4efd6f0b9485" />
</Frame>

<br />

<Frame caption="Wave">
  <img src="https://usercdn.edgeimpulse.com/project497631/46f0338a7a609afbb3b2e2f899c203ab88edc6503b04466b0a9e33e1484b7ad5" />
</Frame>

### Compatible Blocks

* **Feature extraction**: [Spectral Features](/studio/projects/processing-blocks/blocks/spectral-analysis) (FFTs or Wavelets)
* **Learning block**: [Classification](/studio/projects/learning-blocks/blocks/classification) + optionally [Anomaly Detection (K-Means)](/studio/projects/learning-blocks/blocks/anomaly-detection-k-means) or [Anomaly Detection (GMM)](/studio/projects/learning-blocks/blocks/anomaly-detection-gmm)

*Not sure what to choose? Try out this dataset with the [EON Tuner](/studio/projects/eon-tuner).*

### Dataset Details

* **Total Data Items:** 101

* **Labeling Method:** single label

* **Train/Test Split:** 84.16% / 15.84%

|                      | **Training Set**          | **Testing Set**                    |
| -------------------- | ------------------------- | ---------------------------------- |
| **Total Data Items** | 85                        | 16                                 |
| **Labels**           | idle, snake, updown, wave | anomaly, idle, snake, updown, wave |

## Usage

The dataset can be added to a project in two ways: cloning the dataset public project or downloading the dataset and importing it into another project.

* **Clone the [public project](https://studio.edgeimpulse.com/public/497631/latest)**

  To clone and use this project, visit the [Edge Impulse Studio link](https://studio.edgeimpulse.com/public/497631/latest), click on the **Clone** button on the top-right corner and follow the cloning instructions.

* **Download and import**

  * [Download link](https://cdn.edgeimpulse.com/datasets/Motion+Classification+-+Continuous+motion+recognition.zip)

  This dataset uses the Edge Impulse Exporter Format (`info.labels`). See [Edge Impulse labels](/tools/specifications/data-annotation/ei-labels) for more info.

  Edge Impulse also supports different [data acquisition formats](/tools/specifications/data-acquisition/json-cbor) and [dataset annotation formats](/tools/specifications/data-annotation/ei-labels) that you can import into your project to build your edge AI models:

  * [Studio uploader](/studio/projects/data-acquisition/uploader)
  * [CLI uploader](/tools/clis/edge-impulse-cli/uploader)
  * [CSV Wizard](/studio/projects/data-acquisition/csv-wizard)
  * [Python SDK](/tutorials/tools/sdks/studio/python/upload-download-data)
  * [Ingestion API](/apis/ingestion)
  * [Import from S3 buckets](/studio/projects/data-acquisition/data-sources)
  * [Upload portals](/studio/organizations/upload-portals)

## Citation

If you use this dataset in your research paper, please cite it using the following BibTeX:

```
@misc{edgeimpulse_dataset_497631,
    title = {Motion Classification - Continuous motion recognition},
    author = {Edge Impulse},
    year = {2024},
    url = {https://studio.edgeimpulse.com/public/497631/latest},
    note = {BSD 3-Clause Clear}
}
```


Built with [Mintlify](https://mintlify.com).