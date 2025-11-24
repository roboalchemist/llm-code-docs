# Source: https://docs.galileo.ai/galileo/galileo-nlp-studio/galileo-product-features/xray-insights.md

# Alerts

> Explore Galileo NLP Studio's Alerts feature, designed to detect and summarize dataset issues like mislabeling and class imbalance, enhancing data inspection.

**What are Galileo Alerts?**

After you complete a run, Galileo surfaces a summary of issues it has found in your dataset in the Alerts section. Each Alert represents a problematic pocket of data that Galileo has identified. Clicking on an alert will filter the dataset to this problematic subset of data and allow you to fix them.

Alerts will also educate you on why this subset of your data might be causing issues and tell you how you can fix this. You can think of Alerts as a partner Data Scientist working with you to find and fix your data.

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/alert.gif" />
</Frame>

## Alerts that we support today

We support a growing list of alerts, and are open to feature requests! Some of the highlights include:

|                                                                           |                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Likely Mislabeled                                                         | Leverages our Likely [Mislabeled](/galileo/gen-ai-studio-products/galileo-ai-research/likely-mislabeled) algorithm to surface the samples we believe were incorrectly labeled by your annotators                                                                   |
| Misclassified                                                             | Surfaces mismatches between your data and the model's prediction                                                                                                                                                                                                   |
| Hard For The Model                                                        | Exposes the samples we believe we hard for your model to learn. These are samples with high Data Error Potential scores                                                                                                                                            |
| Low Performing Classes                                                    | Classes that performed significantly worse than average (e.g. their F1 score was 1 std below the mean F1 score)                                                                                                                                                    |
| Low Performing Metadata                                                   | Slices the data by different metadata values and shows any subsets of data that perform significantly worse than average                                                                                                                                           |
| High Class Imbalance is Impacting Performance                             | Exposes classes that have a low relative class distribution in the training set and perform poorly in the validation/test set                                                                                                                                      |
| High Class Overlap                                                        | Surfaces classes our Class Overlap algorithm detected as being confused by one another by the model                                                                                                                                                                |
| Out Of Coverage                                                           | Surfaces samples in your validation/test split that are fundamentally different from samples contained in your training set                                                                                                                                        |
| PII                                                                       | Identifies any Personal Identifiable Information in your data                                                                                                                                                                                                      |
| Non-Primary Language                                                      | Exposes samples that are not in the primary language of your dataset                                                                                                                                                                                               |
| Semantic Cluster with High DEP                                            | Surfaces semantic clusters of data found through our [Clustering](/galileo/how-to-and-faq/galileo-product-features/clusters) algorithm that have high [Data Error Potential](/galileo/gen-ai-studio-products/galileo-ai-research/galileo-data-error-potential-dep) |
| High Uncertainty Samples                                                  | Surfaces samples that exist on the model's decision boundary                                                                                                                                                                                                       |
| \[Inference Only] Data Drift                                              | The data your model sees in this inference run has [drifted](/galileo/gen-ai-studio-products/galileo-ai-research/data-drift-detection) from what it was trained on                                                                                                 |
| \[Named Entity Recognition Only] High Frequency Problematic Word          | Shows you words that the models struggles with (i.e. have high Data Error Potential) more than 50% of the time                                                                                                                                                     |
| \[Named Entity Recognition or Semantic Segmentation Only] False Positives | Spans or Segments predicted by the model for which the Ground Truth has no annotation                                                                                                                                                                              |
| \[Named Entity Recognition Only] False Negatives                          | Surfaces spans for which the Ground Truth had an annotation but the model didn't predict any                                                                                                                                                                       |
| \[Named Entity Recognition Only] Shifted Spans                            | Surfaces spans where the beginning and end locations are not aligned in the Ground Truth and Prediction                                                                                                                                                            |
| \[Object Detection Only] Background Confusion Errors                      | Surfaces predictions that don’t overlap significantly with any Ground Truth                                                                                                                                                                                        |
| \[Object Detection Only] Localization Mistakes                            | Surfaces detected objects that overlap poorly with their corresponding Ground Truth                                                                                                                                                                                |
| \[Object Detection Only] Missed Predictions                               | Surfaces annotations the model failed to make predictions for                                                                                                                                                                                                      |
| \[Object Detection Only] Misclassified Predictions                        | Surfaces objects that were assigned a different label than their associated Ground Truths                                                                                                                                                                          |
| \[Object Detection Only]                                                  | Surfaces instances where multiple duplicate predictions were being made for the same object                                                                                                                                                                        |

## How to request a new alert?

Have a great idea for a new alert? We'd love to hear about it! File any requests under your *Profile Avatar Menu >* "Bug Report or Feature Request", and we'll immediately get your request telescope

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/galileo/images/alert-2.avif" />
</Frame>
