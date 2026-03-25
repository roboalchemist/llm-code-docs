# Source: https://docs.wandb.ai/models/ref/python/custom-charts/confusion_matrix.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# confusion_matrix()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/plot/confusion_matrix.py" />

### <kbd>function</kbd> `confusion_matrix`

```python  theme={null}
confusion_matrix(
    probs: 'Sequence[Sequence[float]] | None' = None,
    y_true: 'Sequence[T] | None' = None,
    preds: 'Sequence[T] | None' = None,
    class_names: 'Sequence[str] | None' = None,
    title: 'str' = 'Confusion Matrix Curve',
    split_table: 'bool' = False
) → CustomChart
```

Constructs a confusion matrix from a sequence of probabilities or predictions.

**Args:**

* `probs`:  A sequence of predicted probabilities for each  class. The sequence shape should be (N, K) where N is the number of samples  and K is the number of classes. If provided, `preds` should not be provided.
* `y_true`:  A sequence of true labels.
* `preds`:  A sequence of predicted class labels. If provided,  `probs` should not be provided.
* `class_names`:  Sequence of class names. If not  provided, class names will be defined as "Class\_1", "Class\_2", etc.
* `title`:  Title of the confusion matrix chart.
* `split_table`:  Whether the table should be split into a separate section  in the W\&B UI. If `True`, the table will be displayed in a section named  "Custom Chart Tables". Default is `False`.

**Returns:**

* `CustomChart`:  A custom chart object that can be logged to W\&B. To log the  chart, pass it to `wandb.log()`.

**Raises:**

* `ValueError`:  If both `probs` and `preds` are provided or if the number of  predictions and true labels are not equal. If the number of unique  predicted classes exceeds the number of class names or if the number of  unique true labels exceeds the number of class names.
* `wandb.Error`:  If numpy is not installed.

**Examples:**
Logging a confusion matrix with random probabilities for wildlife classification:

```python  theme={null}
import numpy as np
import wandb

# Define class names for wildlife
wildlife_class_names = ["Lion", "Tiger", "Elephant", "Zebra"]

# Generate random true labels (0 to 3 for 10 samples)
wildlife_y_true = np.random.randint(0, 4, size=10)

# Generate random probabilities for each class (10 samples x 4 classes)
wildlife_probs = np.random.rand(10, 4)
wildlife_probs = np.exp(wildlife_probs) / np.sum(
    np.exp(wildlife_probs),
    axis=1,
    keepdims=True,
)

# Initialize W&B run and log confusion matrix
with wandb.init(project="wildlife_classification") as run:
    confusion_matrix = wandb.plot.confusion_matrix(
         probs=wildlife_probs,
         y_true=wildlife_y_true,
         class_names=wildlife_class_names,
         title="Wildlife Classification Confusion Matrix",
    )
    run.log({"wildlife_confusion_matrix": confusion_matrix})
```

In this example, random probabilities are used to generate a confusion matrix.

Logging a confusion matrix with simulated model predictions and 85% accuracy:

```python  theme={null}
import numpy as np
import wandb

# Define class names for wildlife
wildlife_class_names = ["Lion", "Tiger", "Elephant", "Zebra"]

# Simulate true labels for 200 animal images (imbalanced distribution)
wildlife_y_true = np.random.choice(
    [0, 1, 2, 3],
    size=200,
    p=[0.2, 0.3, 0.25, 0.25],
)

# Simulate model predictions with 85% accuracy
wildlife_preds = [
    y_t
    if np.random.rand() < 0.85
    else np.random.choice([x for x in range(4) if x != y_t])
    for y_t in wildlife_y_true
]

# Initialize W&B run and log confusion matrix
with wandb.init(project="wildlife_classification") as run:
    confusion_matrix = wandb.plot.confusion_matrix(
         preds=wildlife_preds,
         y_true=wildlife_y_true,
         class_names=wildlife_class_names,
         title="Simulated Wildlife Classification Confusion Matrix",
    )
    run.log({"wildlife_confusion_matrix": confusion_matrix})
```

In this example, predictions are simulated with 85% accuracy to generate a confusion matrix.
