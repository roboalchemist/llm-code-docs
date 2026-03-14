# Source: https://docs.edgeimpulse.com/datasets/image/dice-colors.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dice colors

**Task:** Object Detection

**License:** [BSD 3-Clause Clear](https://spdx.org/licenses/BSD-3-Clause-Clear.html)

<Frame caption="Dataset Screenshot">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/dataset-screenshot/497418.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=1ac1e8bf06988983aeddf82e17e9b74a" width="1600" height="719" data-path=".assets/images/dataset-screenshot/497418.png" />
</Frame>

## Description

This dataset has been collected by Edge Impulse teams and is a variant of the "Object Detection - Dice" dataset. It images of dice on a white background labeled by color.

### Compatible Blocks

* **Feature extraction**: [Image](/studio/projects/processing-blocks/blocks/image)
* **Learning block**: [Object Detection](/studio/projects/learning-blocks/blocks/object-detection)

*Not sure what to choose? Try out this dataset with the [EON Tuner](/studio/projects/eon-tuner).*

### Dataset Details

* **Total Data Items:** 85

* **Labeling Method:** object detection

* **Train/Test Split:** 80.00% / 20.00%

|                      | **Training Set**                         | **Testing Set**                          |
| -------------------- | ---------------------------------------- | ---------------------------------------- |
| **Total Data Items** | 68                                       | 17                                       |
| **Labels**           | blue, green, orange, purple, red, yellow | blue, green, orange, purple, red, yellow |

## Usage

The dataset can be added to a project in two ways: cloning the dataset public project or downloading the dataset and importing it into another project.

* **Clone the [public project](https://studio.edgeimpulse.com/public/497418/latest)**

  To clone and use this project, visit the [Edge Impulse Studio link](https://studio.edgeimpulse.com/public/497418/latest), click on the **Clone** button on the top-right corner and follow the cloning instructions.

* **Download and import**

  * [Download link](https://cdn.edgeimpulse.com/datasets/Object+Detection+-+Dice+colors.zip)

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
@misc{edgeimpulse_dataset_497418,
    title = {Object Detection - Dice colors},
    author = {Edge Impulse},
    year = {2024},
    url = {https://studio.edgeimpulse.com/public/497418/latest},
    note = {BSD 3-Clause Clear}
}
```


Built with [Mintlify](https://mintlify.com).