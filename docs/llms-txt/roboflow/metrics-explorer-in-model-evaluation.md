# Source: https://docs.roboflow.com/changelog/explore-by-month/july-2025/metrics-explorer-in-model-evaluation.md

# Metrics Explorer in Model Evaluation

<figure><img src="https://2667452268-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMR3m936tBXGm5QsAcPwe%2Fuploads%2FpgE3nAE0hMfZ8xaTNm4i%2FScreenshot%202025-07-14%20at%2015.22.45.png?alt=media&#x26;token=677afece-87b2-447c-8dcf-33e3c8d9b201" alt=""><figcaption></figcaption></figure>

Model Evaluations for models trained on or uploaded to Roboflow now have a Metrics Explorer. This section lets you see how the precision, recall, and F1 score when validated against your dataset validation or test set changes as you set different confidence thresholds.

The Metrics Explorer will calculate an "Optimal Confidence" level given your dataset. You can move the line on the metrics explorer graph to see how your precision, recall, and F1 scores change at different confidence intervals.

If you trained your model prior to July 14th, 2025, you may have to click a button to toggle a new Model Evaluation calculation. This is necessary so Roboflow can calculate the statistics necessary to show your Metrics Explorer.
