# Source: https://docs.edgeimpulse.com/datasets/image/bottles-rack.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Bottles rack

**Task:** Object Detection

**License:** [BSD 3-Clause Clear](https://spdx.org/licenses/BSD-3-Clause-Clear.html)

<Frame caption="Dataset Screenshot">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/dataset-screenshot/497424.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=85915d1b8a81044587d8bb0305c87a2d" width="1600" height="719" data-path=".assets/images/dataset-screenshot/497424.png" />
</Frame>

## Description

This dataset has been collected by Edge Impulse teams and contains images of bottle racks on different backgrounds and different orientations. It can be used to count the number of beers in the rack.
The two labels - empty or full - is used to distinguish if the beer has a cap or not.

### Compatible Blocks

* **Feature extraction**: [Image](/studio/projects/processing-blocks/blocks/image)
* **Learning block**: [Object Detection](/studio/projects/learning-blocks/blocks/object-detection)

*Not sure what to choose? Try out this dataset with the [EON Tuner](/studio/projects/eon-tuner).*

### Dataset Details

* **Total Data Items:** 130

* **Labeling Method:** object detection

* **Train/Test Split:** 74.62% / 25.38%

|                      | **Training Set** | **Testing Set** |
| -------------------- | ---------------- | --------------- |
| **Total Data Items** | 97               | 33              |
| **Labels**           | empty, full      | empty, full     |

## Usage

The dataset can be added to a project in two ways: cloning the dataset public project or downloading the dataset and importing it into another project.

* **Clone the [public project](https://studio.edgeimpulse.com/public/497424/latest)**

  To clone and use this project, visit the [Edge Impulse Studio link](https://studio.edgeimpulse.com/public/497424/latest), click on the **Clone** button on the top-right corner and follow the cloning instructions.

* **Download and import**

  * [Download link](https://cdn.edgeimpulse.com/datasets/Object+Detection+-+Bottles+rack.zip)

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
@misc{edgeimpulse_dataset_497424,
    title = {Object Detection - Bottles rack},
    author = {Edge Impulse},
    year = {2024},
    url = {https://studio.edgeimpulse.com/public/497424/latest},
    note = {BSD 3-Clause Clear}
}
```


Built with [Mintlify](https://mintlify.com).