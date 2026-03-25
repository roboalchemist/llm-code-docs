# Source: https://docs.edgeimpulse.com/datasets/audio/faucet-vs-noise.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Faucet vs noise

**Task:** Audio Classification

**License:** [BSD 3-Clause Clear](https://spdx.org/licenses/BSD-3-Clause-Clear.html)

<Frame caption="Dataset Screenshot">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/dataset-screenshot/497635.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=ff321dd7d6b87cad056b6d82217ec299" width="1600" height="719" data-path=".assets/images/dataset-screenshot/497635.png" />
</Frame>

## Description

This dataset has been collected by Edge Impulse teams to recognize the sound of water running from a faucet, even in the presence of other background noise.

You can also follow [our tutorial](/tutorials/end-to-end/sound-recognition) learn how to collect audio data from microphones, use signal processing to extract the most important information, and train a deep neural network that can tell you whether the sound of running water can be heard in a given clip of audio. Finally, you'll deploy the system to an embedded device and evaluate how well it works.

### Compatible Blocks

* **Feature extraction**: [Audio (MFE)](/studio/projects/processing-blocks/blocks/audio-mfe), [Spectrogram](/studio/projects/processing-blocks/blocks/spectrogram), [Raw Data](/studio/projects/processing-blocks/blocks/raw-data)
* **Learning block**: [Classification](/studio/projects/learning-blocks/blocks/classification)

*Not sure what to choose? Try out this dataset with the [EON Tuner](/studio/projects/eon-tuner).*

### Dataset Details

* **Total Data Items:** 18

* **Total Data Length:** 0h 15m 40s

* **Axis Summary:** audio

* **Labeling Method:** single label

* **Train/Test Split:** 88.89% / 11.11%

|                       | **Training Set** | **Testing Set** |
| --------------------- | ---------------- | --------------- |
| **Total Data Items**  | 16               | 2               |
| **Labels**            | faucet, noise    | faucet, noise   |
| **Total Data Length** | 0h 13m 40s       | 0h 2m 0s        |

## Usage

The dataset can be added to a project in two ways: cloning the dataset public project or downloading the dataset and importing it into another project.

* **Clone the [public project](https://studio.edgeimpulse.com/public/497635/latest)**

  To clone and use this project, visit the [Edge Impulse Studio link](https://studio.edgeimpulse.com/public/497635/latest), click on the **Clone** button on the top-right corner and follow the cloning instructions.

* **Download and import**

  * [Download link](https://cdn.edgeimpulse.com/datasets/Audio+Classification+-+Faucet+vs+noise.zip)

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
@misc{edgeimpulse_dataset_497635,
    title = {Audio Classification - Faucet vs noise},
    author = {Edge Impulse},
    year = {2024},
    url = {https://studio.edgeimpulse.com/public/497635/latest},
    note = {BSD 3-Clause Clear}
}
```


Built with [Mintlify](https://mintlify.com).