# Source: https://docs.wandb.ai/models/ref/python/custom-charts/scatter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# scatter()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/plot/scatter.py" />

### <kbd>function</kbd> `scatter`

```python  theme={null}
scatter(
    table: 'wandb.Table',
    x: 'str',
    y: 'str',
    title: 'str' = '',
    split_table: 'bool' = False
) → CustomChart
```

Constructs a scatter plot from a wandb.Table of data.

**Args:**

* `table`:  The W\&B Table containing the data to visualize.
* `x`:  The name of the column used for the x-axis.
* `y`:  The name of the column used for the y-axis.
* `title`:  The title of the scatter chart.
* `split_table`:  Whether the table should be split into a separate section  in the W\&B UI. If `True`, the table will be displayed in a section named  "Custom Chart Tables". Default is `False`.

**Returns:**

* `CustomChart`:  A custom chart object that can be logged to W\&B. To log the  chart, pass it to `wandb.log()`.

**Example:**

```python  theme={null}
import math
import random
import wandb

# Simulate temperature variations at different altitudes over time
data = [
   [i, random.uniform(-10, 20) - 0.005 * i + 5 * math.sin(i / 50)]
   for i in range(300)
]

# Create W&B table with altitude (m) and temperature (°C) columns
table = wandb.Table(data=data, columns=["altitude (m)", "temperature (°C)"])

# Initialize W&B run and log the scatter plot
with wandb.init(project="temperature-altitude-scatter") as run:
   # Create and log the scatter plot
   scatter_plot = wandb.plot.scatter(
        table=table,
        x="altitude (m)",
        y="temperature (°C)",
        title="Altitude vs Temperature",
   )
   run.log({"altitude-temperature-scatter": scatter_plot})
```
