# Source: https://docs.wandb.ai/models/ref/python/custom-charts/pr_curve.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# pr_curve()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/plot/pr_curve.py" />

### <kbd>function</kbd> `pr_curve`

```python  theme={null}
pr_curve(
    y_true: 'Iterable[T] | None' = None,
    y_probas: 'Iterable[numbers.Number] | None' = None,
    labels: 'list[str] | None' = None,
    classes_to_plot: 'list[T] | None' = None,
    interp_size: 'int' = 21,
    title: 'str' = 'Precision-Recall Curve',
    split_table: 'bool' = False
) → CustomChart
```

Constructs a Precision-Recall (PR) curve.

The Precision-Recall curve is particularly useful for evaluating classifiers on imbalanced datasets. A high area under the PR curve signifies both high precision (a low false positive rate) and high recall (a low false negative rate). The curve provides insights into the balance between false positives and false negatives at various threshold levels, aiding in the assessment of a model's performance.

**Args:**

* `y_true`:  True binary labels. The shape should be (`num_samples`,).
* `y_probas`:  Predicted scores or probabilities for each class.  These can be probability estimates, confidence scores, or non-thresholded  decision values. The shape should be (`num_samples`, `num_classes`).
* `labels`:  Optional list of class names to replace  numeric values in `y_true` for easier plot interpretation.  For example, `labels = ['dog', 'cat', 'owl']` will replace 0 with  'dog', 1 with 'cat', and 2 with 'owl' in the plot. If not provided,  numeric values from `y_true` will be used.
* `classes_to_plot`:  Optional list of unique class values from  y\_true to be included in the plot. If not specified, all unique  classes in y\_true will be plotted.
* `interp_size`:  Number of points to interpolate recall values. The  recall values will be fixed to `interp_size` uniformly distributed  points in the range \[0, 1], and the precision will be interpolated  accordingly.
* `title`:  Title of the plot. Defaults to "Precision-Recall Curve".
* `split_table`:  Whether the table should be split into a separate section  in the W\&B UI. If `True`, the table will be displayed in a section named  "Custom Chart Tables". Default is `False`.

**Returns:**

* `CustomChart`:  A custom chart object that can be logged to W\&B. To log the  chart, pass it to `wandb.log()`.

**Raises:**

* `wandb.Error`:  If NumPy, pandas, or scikit-learn is not installed.

**Example:**

```python  theme={null}
import wandb

# Example for spam detection (binary classification)
y_true = [0, 1, 1, 0, 1]  # 0 = not spam, 1 = spam
y_probas = [
    [0.9, 0.1],  # Predicted probabilities for the first sample (not spam)
    [0.2, 0.8],  # Second sample (spam), and so on
    [0.1, 0.9],
    [0.8, 0.2],
    [0.3, 0.7],
]

labels = ["not spam", "spam"]  # Optional class names for readability

with wandb.init(project="spam-detection") as run:
    pr_curve = wandb.plot.pr_curve(
         y_true=y_true,
         y_probas=y_probas,
         labels=labels,
         title="Precision-Recall Curve for Spam Detection",
    )
    run.log({"pr-curve": pr_curve})
```
