# Source: https://docs.galileo.ai/galileo-ai-research/galileo-data-error-potential-dep.md

# Galileo Data Error Potential  (Dep) 

> Learn about Galileo's Data Error Potential (DEP) score, a metric to identify and categorize machine learning data errors, enhancing data quality and model performance.

Today teams typically leverage model confidence scores to separate well trained from poorly trained data. This has two major problems:

* **Confidence scores** are highly model centric. There is high bias towards training performance and very little use of inherent data quality to segregate the good data from the bad (results below)

* Even with powerful pre-trained models, confidence scores are unable to capture nuanced sub-categories of data errors (details below)

The **Galileo Data Error Potential (DEP)** score has been built to provide a per sample holistic data quality score to identify samples in the dataset contributing to low or high model performance i.e. ‘pulling’ the model up or down respectively. In other words, the DEP score measures the potential for "misfit" of an observation to the given model.

Categorization of "misfit" data samples includes:

* Mislabelled samples (annotation mistakes)

* Boundary samples or overlapping classes

* Outlier samples or Anomalies

* Noisy Input

* Misclassified samples

* Other errors

This sub-categorization is crucial as different dataset actions are required for each category of errors. For example, one can augment the dataset with samples similar to boundary samples to improve classification.

As shown in below, we assign a DEP score to every sample in the data. The *Data Error Potential (DEP) Slider* can be used to filter samples based on DEP score, allowing you to filter for samples with DEP greater than x, less than y, or within a specific range \[x, y].

<Frame caption="Galileo Platform surfaces mislabeled, garbage samples by ordering in desc order of DEP score">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/galileo-rag-1.png" />
</Frame>

#### DEP score calculation

The base calculation behind the DEP score is a hybrid ‘**Area Under Margin’ (AUM)** mechanism. AUM is the cross-epoch average of the model uncertainty for each data sample (calculated as the difference between the ground truth confidence and the maximum confidence on a non ground truth label).

**AUM = p(y\*) - p(ymax)y^max!=y\***

We then dynamically leverage K-Distinct Neighbors, IH Metrics (multiple weak learners) and Energy Functions on Logits, to clearly separate out annotator mistakes from samples that are confusing to the model or are outliers and noise. The 'dynamic' element comes from the fact that DEP takes into account the level of class imbalance, variability etc to cater to the nuances of each dataset.

#### DEP score efficacy

To measure the efficacy of the DEP score, we performed experiments on a public dataset and induced varying degrees of noise. We observed that unlike Confidence scores, the DEP score was successfully able to separate bad data (red) from the good (green). This demonstrates true data-centricity (model independence) of Galileo’s DEP score. Below are results from experiments on the public Banking Intent dataset. The dotted lines indicate a dynamic thresholding value (adapting to each dataset) that segments noisy (red) and clean (green) samples of the dataset.

| Galileo DEP score                                                                                                                        | Model confidence score                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| <Frame caption="Noise recall: 99.2%"><img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/galileo-rag-2.png" /></Frame>  | <Frame caption="Noise recall: 87.5%"><img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/galileo-rag-3.avif" /></Frame> |
| <Frame caption="Noise recall: 89.0%"><img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/galileo-rag-4.avif" /></Frame> | <Frame caption="Noise recall: 64.9%"><img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/galileo-rag-6.png" /></Frame>  |

### DEP Thresholding

The goal is to plot AUM scores and highlight the mean AUM and mean F1 of the dataset. Two different thresholds, t\_easy and t\_hard, are marked as follows:

* t\_easy = mean AUM, so all samples above the mean AUM are considered easy.

* t\_hard = \[t\_mean - t\_std, -1], so samples in this range are considered hard or ambiguous.

The samples between t\_mean and t\_mean - t\_std are considered ambiguous.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/galileo-rag-7.png" />
</Frame>

### DEP Benchmarks

To ensure DEP calibrations follow the fundamentals of a good ML metric, it should have more noisy samples in hard section and correspondingly less noisy data in easy region. AUM outperforms prediction confidence as well as similar metrics such as **Ground Truth confidence** as well as **Model uncertainty**, in being able to surface more noisy samples in the hard category.

Below are some benchmarks we calibrated on various well-known and peer reviewed datasets.

![]()

{" "}

<Frame
  caption="
Benchmark (Train): Performance on Noisy Datasets
"
>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dep-1.png" />
</Frame>

{" "}

<Frame
  caption="Benchmark (Train): Final Epoch Train Performance
"
>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dep-2.png" />
</Frame>

{" "}

<Frame
  caption="Benchmark (Train): Average across all epochs
"
>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dep-3.png" />
</Frame>

{" "}

<Frame caption="Benchmark (Test): Average across all epochs">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/dep-4.png" />
</Frame>

[PreviousRAG Quality Metrics using ChainPoll](/galileo/gen-ai-studio-products/galileo-ai-research/rag-quality-metrics-using-chainpoll)

[NextData Drift Detection](/galileo/gen-ai-studio-products/galileo-ai-research/data-drift-detection)
