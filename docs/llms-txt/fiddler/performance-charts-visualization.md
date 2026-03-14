# Source: https://docs.fiddler.ai/observability/analytics/performance-charts-visualization.md

# Performance Charts Visualization

### Performance Charts Visualizations for ML and LLM Models

List of possible performance visualization depending on the model task. To see how to create a Performance chart, visit [this page](https://docs.fiddler.ai/observability/analytics/performance-charts-creation).

### Binary Classification

#### Confusion Matrix

A 2x2 table that shows how many predicted and actual values exist for positive and negative classes. Also referred as an error matrix. The percentage is computed per row.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-d33888e8bb04aecaa2be97778050be98fb238f76%2Fconfusion_matrix.png?alt=media)

#### Receiver Operating Characteristic (ROC) Curve

A graph showing the performance of a classification model at different classification thresholds. Plots the true positive rate (TPR), also known as recall, against the false positive rate (FPR).

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-45aad82436470ffe93140e4530856bfed4f4db13%2Froc.png?alt=media)

#### Precision-Recall Curve

A graph that plots the precision against the recall for different classification thresholds.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-82e2d1784232ae6cb85d9797530c74847c5debf7%2Fprecision-recall.png?alt=media)

#### Calibration Plot

A graph that tell us how well the model is calibrated. The plot is obtained by dividing the predictions into 10 quantile buckets (0-10th percentile, 10-20th percentile, etc.). The average predicted probability is plotted against the true observed probability for that set of points.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-0d7c36360c48eb7d7cef2d81cb47b8fb43a87882%2Fcalibration-plot.png?alt=media)

### Multi-class Classification

#### Confusion Matrix

A table that shows how many predicted and actual values exist for different classes. Also referred as an error matrix. The percentage is computed per row (using all classes). In the full view, up to 15 classes can be displayed. In the chart creation mode, up to 12 classes can be displayed. The displayed labels can be controlled in the chart.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-8e2ce2a60ddf84699ae2e8a70b21e12b992b1718%2Fmulti-class-confusion-matrix.png?alt=media)

### Regression

#### Prediction Scatterplot

Plots the predicted values against the actual values. The more closely the plot hugs the `y=x line`, the better the fit of the model.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-95f9a745a16f554eee10fd8b35290c7091c2e6cd%2Fprediction-scatterplot.png?alt=media)

#### Error Distribution

A histogram showing the distribution of errors (differences between model predictions and actuals). The closer to 0 the errors are, the better the fit of the model.

![](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-db8ed9b1ea19e82bea629ffdd15b458fad0580c3%2Ferror-distribution.png?alt=media)
