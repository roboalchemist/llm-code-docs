# Source: https://docs.galileo.ai/galileo-ai-research/galileo-data-error-potential-dep.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

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
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-1.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=ce16cb431790d47416a6055fe474b009" data-og-width="1475" width="1475" data-og-height="669" height="669" data-path="images/galileo-rag-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-1.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=f3d421af5bf2e3d5b4da517d1c0767f6 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-1.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=cea49b83bf2af804a4c63e36381cbf60 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-1.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=7975a19eb57a73a3a8cb733e678791b4 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-1.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=0ca81bc8d963064df203d272a2ef1ea9 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-1.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=3d9f4aa82a86bb276d8096be3e70758f 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-1.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b66abe47d287a459318a71a8f7637c22 2500w" />
</Frame>

#### DEP score calculation

The base calculation behind the DEP score is a hybrid ‘**Area Under Margin’ (AUM)** mechanism. AUM is the cross-epoch average of the model uncertainty for each data sample (calculated as the difference between the ground truth confidence and the maximum confidence on a non ground truth label).

**AUM = p(y\*) - p(ymax)y^max!=y\***

We then dynamically leverage K-Distinct Neighbors, IH Metrics (multiple weak learners) and Energy Functions on Logits, to clearly separate out annotator mistakes from samples that are confusing to the model or are outliers and noise. The 'dynamic' element comes from the fact that DEP takes into account the level of class imbalance, variability etc to cater to the nuances of each dataset.

#### DEP score efficacy

To measure the efficacy of the DEP score, we performed experiments on a public dataset and induced varying degrees of noise. We observed that unlike Confidence scores, the DEP score was successfully able to separate bad data (red) from the good (green). This demonstrates true data-centricity (model independence) of Galileo’s DEP score. Below are results from experiments on the public Banking Intent dataset. The dotted lines indicate a dynamic thresholding value (adapting to each dataset) that segments noisy (red) and clean (green) samples of the dataset.

| Galileo DEP score                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Model confidence score                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <Frame caption="Noise recall: 99.2%"><img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-2.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=26526a0687ba0431c2f25614c977aa14" data-og-width="868" width="868" data-og-height="408" height="408" data-path="images/galileo-rag-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-2.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=1957045878357198b14cac8106b928ae 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-2.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=797ba6ddbc578462f08609d7ea651f61 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-2.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=8461cd1f3d1dad0c736266989c0a4c6f 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-2.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=8cf92f6c3effecce5412549bed984261 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-2.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=9122d668775a11d58448d00d9948b7ba 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-2.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=427152988d5686ce9077e4c0ad3aac5d 2500w" /></Frame>         | <Frame caption="Noise recall: 87.5%"><img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-3.avif?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=be48a9545204ce7b914067fea961f667" data-og-width="900" width="900" data-og-height="416" height="416" data-path="images/galileo-rag-3.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-3.avif?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=eb9f1f25f6723f9cfd9c9f373f13895b 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-3.avif?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=e5391b4cb90ed6f350144c8f62996db9 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-3.avif?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=341e35324fde97870932ef3711c2b5d9 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-3.avif?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=ef9ee3f4f50847a91d9eb706eecec157 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-3.avif?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=96707a37bf26ca2c60644cac751182ab 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-3.avif?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=a27fb423cd627e8be805b446da5369be 2500w" /></Frame> |
| <Frame caption="Noise recall: 89.0%"><img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-4.avif?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=9beb4ff6831f18ba112d5303ed8252e4" data-og-width="900" width="900" data-og-height="408" height="408" data-path="images/galileo-rag-4.avif" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-4.avif?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b9302fec7b5f36ecef34daac3cbb2bf8 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-4.avif?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=c73ddc3bed289f0c1b75741eceb05fb6 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-4.avif?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=e60c6a7ff3b4cf6e959872112684b523 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-4.avif?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=562c89c856b1064becf697e9fb092800 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-4.avif?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=ed2ed1542053ff87f07943cf800323b8 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-4.avif?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=bb0a38b1ba1be7c0f43d4bd790fc81a7 2500w" /></Frame> | <Frame caption="Noise recall: 64.9%"><img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-6.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=fd47e880819a22f6b1793ff7b7d30861" data-og-width="624" width="624" data-og-height="305" height="305" data-path="images/galileo-rag-6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-6.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=0ff5d1bfb172b8aecfe8503763ba4445 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-6.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=7d1df045670e858da3395fb4ade42eb2 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-6.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=06086bea886bccb2f20dacd9842bfda7 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-6.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=fc1e4b94a1b75d49467a2cf2eb562b41 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-6.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=59dc249da7c1bde73dc11d431bd2d320 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-6.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=9a9a096e1e79f119ba21edb754bf5d1c 2500w" /></Frame>         |

### DEP Thresholding

The goal is to plot AUM scores and highlight the mean AUM and mean F1 of the dataset. Two different thresholds, t\_easy and t\_hard, are marked as follows:

* t\_easy = mean AUM, so all samples above the mean AUM are considered easy.

* t\_hard = \[t\_mean - t\_std, -1], so samples in this range are considered hard or ambiguous.

The samples between t\_mean and t\_mean - t\_std are considered ambiguous.

<Frame>
  <img src="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-7.png?fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=7fc68c26ff7d60eee9c3be8d83613d64" data-og-width="1371" width="1371" data-og-height="590" height="590" data-path="images/galileo-rag-7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-7.png?w=280&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=f4872e5ba6a98b4c3ff4271aed7ea920 280w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-7.png?w=560&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=7b983ea1b3d3eb0a1d3988c6ee751348 560w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-7.png?w=840&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b0c8856bb8bb68545ebbab32ed5f15a5 840w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-7.png?w=1100&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=b8c44bd4282795b26081acb8ebd01b67 1100w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-7.png?w=1650&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=791381bfb4a5c8fcf65fc3355fd8ab0a 1650w, https://mintcdn.com/galileo/_xpCBW-9wyhpIMLs/images/galileo-rag-7.png?w=2500&fit=max&auto=format&n=_xpCBW-9wyhpIMLs&q=85&s=c7b998dc91f08b0c350b8767fdee9c81 2500w" />
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
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-1.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=a42ae461eca2ed12527beaa2ec82da9b" data-og-width="624" width="624" data-og-height="305" height="305" data-path="images/dep-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-1.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=fc5796f47df7d776591ece52cd9ba0af 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-1.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=74c76aeb11297b1e981f0d1eb021c0d7 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-1.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=e8baef2e99a9f32e2327a986ad4a59d0 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-1.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=e2c92e21a913b24341a4602fcb80220e 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-1.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=fd840bbe8b16a1ef1b8ebf0cf5d07f97 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-1.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=03e04391b29761486f861b7166d06746 2500w" />
</Frame>

{" "}

<Frame
  caption="Benchmark (Train): Final Epoch Train Performance
"
>
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-2.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=51b89a72e8cd674df66c113c0ed57c1b" data-og-width="1371" width="1371" data-og-height="590" height="590" data-path="images/dep-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-2.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=5b31deca4dc4e1e712aa1ffa4d0caaa8 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-2.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=55cb25430bfa6ac7a0ab6302e898b8e4 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-2.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=d9f89754334cad58c6fb7d515f71d0d6 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-2.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=96f0bf36d6ccf0b0a1ad501f11d7f640 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-2.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=0c8199c33c93c9dd41ad7d0f63384410 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-2.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=cc88b5de66fbef45de131ab761000c1c 2500w" />
</Frame>

{" "}

<Frame
  caption="Benchmark (Train): Average across all epochs
"
>
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-3.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=1df5225f2db03adf4df7e1e90cd74e5f" data-og-width="1368" width="1368" data-og-height="537" height="537" data-path="images/dep-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-3.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=e376003edb5d5fe05e3a575e4f489e34 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-3.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c9646841667a01c985009c58928b486a 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-3.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=0648b75a8e285a965d9b56a90783c5f6 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-3.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=38760b05e85679f934e4a68d36209c8d 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-3.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c54bf4d82f2261dba8161291256b24b4 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-3.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=714a178c781f917f4e8f52b6ff330cab 2500w" />
</Frame>

{" "}

<Frame caption="Benchmark (Test): Average across all epochs">
  <img src="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-4.png?fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=5bf7e6b2c3b4ecc038a4d7e0b7e018cb" data-og-width="1349" width="1349" data-og-height="536" height="536" data-path="images/dep-4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-4.png?w=280&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=c5938fcf7cec1250d3d89eee3a32a49e 280w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-4.png?w=560&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=05acb33ed0dd16bbf9b5d8c79c1782b4 560w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-4.png?w=840&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=aa3bf878852a0c876ca919648f339d62 840w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-4.png?w=1100&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=22083fcdff3d2b323451221225d0ec88 1100w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-4.png?w=1650&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=284c28065a9453db54b6b275dc5afc8a 1650w, https://mintcdn.com/galileo/foTqVxFiTFn9-DRK/images/dep-4.png?w=2500&fit=max&auto=format&n=foTqVxFiTFn9-DRK&q=85&s=25e7f1ca4881f25469ba8354945dbf46 2500w" />
</Frame>

[PreviousRAG Quality Metrics using ChainPoll](/galileo/gen-ai-studio-products/galileo-ai-research/rag-quality-metrics-using-chainpoll)

[NextData Drift Detection](/galileo/gen-ai-studio-products/galileo-ai-research/data-drift-detection)
