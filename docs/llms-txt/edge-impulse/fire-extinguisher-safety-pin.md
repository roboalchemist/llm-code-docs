# Source: https://docs.edgeimpulse.com/datasets/image/fire-extinguisher-safety-pin.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Fire extinguisher safety pin

**Task:** Image Classification

**License:** [BSD 3-Clause Clear](https://spdx.org/licenses/BSD-3-Clause-Clear.html)

<Frame caption="Dataset Screenshot">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/dataset-screenshot/497409.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=3e6e80d342bbb7a1ee029e1bf9ca2a77" width="1600" height="719" data-path=".assets/images/dataset-screenshot/497409.png" />
</Frame>

## Description

This dataset contains images of fire extinguisher safety pins. This dataset can be used to combine image classification and visual anomaly detection.

Label information:

* `rot-powder`: Pin for ROT powder fire extinguisher - Yellow - manufacturer reference: 06210409F
* `rot-water`: Pin for ROT water spray fire extinguisher - Blue - manufacturer reference: 06210410F
* `anomaly`: Other fire extinguisher safety pins

### Compatible Blocks

* **Feature extraction**: [Image](/studio/projects/processing-blocks/blocks/image)
* **Learning block**: [Transfer Learning (Images)](/studio/projects/learning-blocks/blocks/transfer-learning-images), [Classification](/studio/projects/learning-blocks/blocks/classification)

*Not sure what to choose? Try out this dataset with the [EON Tuner](/studio/projects/eon-tuner).*

### Dataset Details

* **Total Data Items:** 264

* **Labeling Method:** single label

* **Train/Test Split:** 79.92% / 20.08%

|                      | **Training Set**               | **Testing Set**                |
| -------------------- | ------------------------------ | ------------------------------ |
| **Total Data Items** | 211                            | 53                             |
| **Labels**           | anomaly, rot-powder, rot-water | anomaly, rot-powder, rot-water |

## Usage

The dataset can be added to a project in two ways: cloning the dataset public project or downloading the dataset and importing it into another project.

* **Clone the [public project](https://studio.edgeimpulse.com/public/497409/latest)**

  To clone and use this project, visit the [Edge Impulse Studio link](https://studio.edgeimpulse.com/public/497409/latest), click on the **Clone** button on the top-right corner and follow the cloning instructions.

* **Download and import**

  * [Download link](https://cdn.edgeimpulse.com/datasets/Image+Classification+-+Fire+extinguisher+safety+pin.zip)

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
@misc{edgeimpulse_dataset_497409,
    title = {Image Classification - Fire extinguisher safety pin},
    author = {Edge Impulse},
    year = {2024},
    url = {https://studio.edgeimpulse.com/public/497409/latest},
    note = {BSD 3-Clause Clear}
}
```


Built with [Mintlify](https://mintlify.com).