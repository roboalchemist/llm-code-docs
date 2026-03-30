# Source: https://docs.edgeimpulse.com/datasets/image/cubes-on-conveyor-belt-self-attention.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cubes on conveyor belt (self attention)

**Task:** Object Detection

**License:** [BSD 3-Clause Clear](https://spdx.org/licenses/BSD-3-Clause-Clear.html)

<Frame caption="Dataset Screenshot">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/dataset-screenshot/497628.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=5a54b122da7a148056f5c5d2258d8456" width="1600" height="719" data-path=".assets/images/dataset-screenshot/497628.png" />
</Frame>

## Description

This dataset, collected by Edge Impulse team, is a variant of the [Cubes on conveyor belt (colors)](/datasets/image/cubes-on-conveyor-belt-colors) dataset. It has been used to perform spatial aware object detection using a micro transformer.

Have a look at this blog post for more information: [FOMO Self-Attention](https://www.edgeimpulse.com/blog/fomo-self-attention/)

### Compatible Blocks

* **Feature extraction**: [Image](/studio/projects/processing-blocks/blocks/image)
* **Learning block**: [FOMO](/studio/projects/learning-blocks/blocks/object-detection/fomo) (modified in Expert mode)

*Not sure what to choose? Try out this dataset with the [EON Tuner](/studio/projects/eon-tuner).*

### Dataset Details

* **Total Data Items:** 85

* **Labeling Method:** object detection

* **Train/Test Split:** 97.65% / 2.35%

|                      | **Training Set** | **Testing Set** |
| -------------------- | ---------------- | --------------- |
| **Total Data Items** | 83               | 2               |
| **Labels**           | left, right      | left, right     |

## Usage

The dataset can be added to a project in two ways: cloning the dataset public project or downloading the dataset and importing it into another project.

* **Clone the [public project](https://studio.edgeimpulse.com/public/497628/latest)**

  To clone and use this project, visit the [Edge Impulse Studio link](https://studio.edgeimpulse.com/public/497628/latest), click on the **Clone** button on the top-right corner and follow the cloning instructions.

* **Download and import**

  * [Download link](https://cdn.edgeimpulse.com/datasets/Object+Detection+-+Self+Attention+-+Cubes+on+conveyor+belt.zip)

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
@misc{edgeimpulse_dataset_497628,
    title = {Object Detection - Self Attention - Cubes on conveyor belt},
    author = {Edge Impulse},
    year = {2024},
    url = {https://studio.edgeimpulse.com/public/497628/latest},
    note = {BSD 3-Clause Clear}
}
```


Built with [Mintlify](https://mintlify.com).