# Source: https://docs.edgeimpulse.com/tutorials/topics/android/keyword-spotting.md

# Source: https://docs.edgeimpulse.com/tutorials/end-to-end/keyword-spotting.md

# Source: https://docs.edgeimpulse.com/datasets/audio/keyword-spotting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Keyword Spotting

**Task:** Audio Classification

**License:** [BSD 3-Clause Clear](https://spdx.org/licenses/BSD-3-Clause-Clear.html)

<Frame caption="Dataset Screenshot">
  <img src="https://mintcdn.com/edgeimpulse/pssAI2UB-dmQQKtc/.assets/images/dataset-screenshot/499022.png?fit=max&auto=format&n=pssAI2UB-dmQQKtc&q=85&s=d2f0ebd6bd8fee8fbe50230397545394" width="1600" height="565" data-path=".assets/images/dataset-screenshot/499022.png" />
</Frame>

## Description

Have you ever wanted to make your own "Ok, Google" or "Alexa" keyword spotting model? The `helloworld` class has been collected by Edge Impulse teams, the added `noise` samples come from the [Microsoft Scalable Noisy Speech Dataset](https://github.com/microsoft/MS-SNSD) and the `unknown` samples are based on a subset of data in the [Google Speech Commands Dataset](https://research.google/blog/launching-the-speech-commands-dataset/).

This dataset can be used to build an Edge AI project detecting the "Hello World" keyword phrase.

You can also follow [our tutorial](/tutorials/end-to-end/keyword-spotting) to guide you through building your keyword spotting model, from data collection to deployment on embedded devices.

### Compatible Blocks

* **Feature extraction**: [Audio (MFCC)](/studio/projects/processing-blocks/blocks/audio-mfcc), [Audio (MFE)](/studio/projects/processing-blocks/blocks/audio-mfe), [Spectrogram](/studio/projects/processing-blocks/blocks/spectrogram), [Raw Data](/studio/projects/processing-blocks/blocks/raw-data)
* **Learning block**: [Classification](/studio/projects/learning-blocks/blocks/classification), [Transfer Learning (Keyword Spotting)](/studio/projects/learning-blocks/blocks/transfer-learning-keyword)

*Not sure what to choose? Try out this dataset with the [EON Tuner](/studio/projects/eon-tuner).*

### Dataset Details

* **Total Data Items:** 2062

* **Total Data Length:** 0h 34m 22s

* **Axis Summary:** audio

* **Labeling Method:** single label

* **Train/Test Split:** 79.97% / 20.03%

|                       | **Training Set**           | **Testing Set**            |
| --------------------- | -------------------------- | -------------------------- |
| **Total Data Items**  | 1649                       | 413                        |
| **Labels**            | helloworld, noise, unknown | helloworld, noise, unknown |
| **Total Data Length** | 0h 27m 29s                 | 0h 6m 53s                  |

## Usage

The dataset can be added to a project in two ways: cloning the dataset public project or downloading the dataset and importing it into another project.

* **Clone the [public project](https://studio.edgeimpulse.com/public/499022/latest)**

  To clone and use this project, visit the [Edge Impulse Studio link](https://studio.edgeimpulse.com/public/499022/latest), click on the **Clone** button on the top-right corner and follow the cloning instructions.

* **Download and import**

  * [Download link](https://cdn.edgeimpulse.com/datasets/Audio+Classification+-+Keyword+Spotting.zip)

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
@misc{edgeimpulse_dataset_499022,
    title = {Audio Classification - Keyword Spotting},
    author = {Edge Impulse},
    year = {2024},
    url = {https://studio.edgeimpulse.com/public/499022/latest},
    note = {BSD 3-Clause Clear}
}
```


Built with [Mintlify](https://mintlify.com).