# Source: https://docs.wandb.ai/models/ref/python/custom-charts/roc_curve.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# roc_curve()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/plot/roc_curve.py" />

### <kbd>function</kbd> `roc_curve`

```python  theme={null}
roc_curve(
    y_true: 'Sequence[numbers.Number]',
    y_probas: 'Sequence[Sequence[float]] | None' = None,
    labels: 'list[str] | None' = None,
    classes_to_plot: 'list[numbers.Number] | None' = None,
    title: 'str' = 'ROC Curve',
    split_table: 'bool' = False
) → CustomChart
```

Constructs Receiver Operating Characteristic (ROC) curve chart.

**Args:**

* `y_true`:  The true class labels (ground truth)  for the target variable. Shape should be (num\_samples,).
* `y_probas`:  The predicted probabilities or  decision scores for each class. Shape should be (num\_samples, num\_classes).
* `labels`:  Human-readable labels corresponding to the class  indices in `y_true`. For example, if `labels=['dog', 'cat']`,  class 0 will be displayed as 'dog' and class 1 as 'cat' in the plot.  If None, the raw class indices from `y_true` will be used.  Default is None.
* `classes_to_plot`:  A subset of unique class labels  to include in the ROC curve. If None, all classes in `y_true` will  be plotted. Default is None.
* `title`:  Title of the ROC curve plot. Default is "ROC Curve".
* `split_table`:  Whether the table should be split into a separate  section in the W\&B UI. If `True`, the table will be displayed in a  section named "Custom Chart Tables". Default is `False`.

**Returns:**

* `CustomChart`:  A custom chart object that can be logged to W\&B. To log the  chart, pass it to `wandb.log()`.

**Raises:**

* `wandb.Error`:  If numpy, pandas, or scikit-learn are not found.

**Example:**

```python  theme={null}
import numpy as np
import wandb

# Simulate a medical diagnosis classification problem with three diseases
n_samples = 200
n_classes = 3

# True labels: assign "Diabetes", "Hypertension", or "Heart Disease" to
# each sample
disease_labels = ["Diabetes", "Hypertension", "Heart Disease"]
# 0: Diabetes, 1: Hypertension, 2: Heart Disease
y_true = np.random.choice([0, 1, 2], size=n_samples)

# Predicted probabilities: simulate predictions, ensuring they sum to 1
# for each sample
y_probas = np.random.dirichlet(np.ones(n_classes), size=n_samples)

# Specify classes to plot (plotting all three diseases)
classes_to_plot = [0, 1, 2]

# Initialize a W&B run and log a ROC curve plot for disease classification
with wandb.init(project="medical_diagnosis") as run:
   roc_plot = wandb.plot.roc_curve(
        y_true=y_true,
        y_probas=y_probas,
        labels=disease_labels,
        classes_to_plot=classes_to_plot,
        title="ROC Curve for Disease Classification",
   )
   run.log({"roc-curve": roc_plot})
```
