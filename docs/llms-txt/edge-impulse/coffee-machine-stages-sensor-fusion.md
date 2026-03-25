# Source: https://docs.edgeimpulse.com/datasets/time-series/coffee-machine-stages-sensor-fusion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Coffee machine stages (sensor fusion)

**Task:** Sensor Fusion Classification

**License:** [BSD 3-Clause Clear](https://spdx.org/licenses/BSD-3-Clause-Clear.html)

<Frame caption="Dataset Screenshot">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/dataset-screenshot/497832.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=918d9a6321bc67e7317a0d6ff7d2ef70" width="1600" height="719" data-path=".assets/images/dataset-screenshot/497832.png" />
</Frame>

## Description

This dataset has been collected by Edge Impulse team to demonstrate how to perform Sensor Fusion Classification leveraging Neural Networks Embeddings.

*Sensor fusion refers to the process of combining data from different types of sensors to give more information to the neural network. To extract meaningful information from this data, you can use the same DSP block, multiples DSP blocks, or use neural networks embeddings.*

You can have a look at this [tutorial](/tutorials/topics/feature-extraction/use-embeddings-sensor-fusion) for more information to see how to use this dataset.

This dataset combines audio data and accelerometer data.

### Recommended Impulse

* **Feature extraction**: Audio Embeddings ([Spectrogram](/studio/projects/processing-blocks/blocks/spectrogram) + Convolution Neural Network Embeddings) + [Spectral Analysis](/studio/projects/processing-blocks/blocks/spectral-analysis) (accelerometer)
* **Learning block**: [Classification](/studio/projects/learning-blocks/blocks/classification) using a fully-connected network

### Dataset Details

* **Total Data Items:** 36

* **Labeling Method:** single label

* **Train/Test Split:** 91.67% / 8.33%

|                      | **Training Set**           | **Testing Set** |
| -------------------- | -------------------------- | --------------- |
| **Total Data Items** | 33                         | 3               |
| **Labels**           | extract, grind, idle, pump |                 |

## Usage

The dataset can be added to a project in two ways: cloning the dataset public project or downloading the dataset and importing it into another project.

* **Clone the [public project](https://studio.edgeimpulse.com/public/497832/latest)**

  To clone and use this project, visit the [Edge Impulse Studio link](https://studio.edgeimpulse.com/public/497832/latest), click on the **Clone** button on the top-right corner and follow the cloning instructions.

* **Download and import**

  * [Download link](https://cdn.edgeimpulse.com/datasets/Sensor+Fusion+Classification+-+Coffee+machine+stages.zip)

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
@misc{edgeimpulse_dataset_497832,
    title = {Sensor Fusion Classification - Coffee machine stages},
    author = {Edge Impulse},
    year = {2024},
    url = {https://studio.edgeimpulse.com/public/497832/latest},
    note = {BSD 3-Clause Clear}
}
```


Built with [Mintlify](https://mintlify.com).