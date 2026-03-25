# Source: https://docs.wandb.ai/models/ref/python/custom-charts/line.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# line()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/plot/line.py" />

### <kbd>function</kbd> `line`

```python  theme={null}
line(
    table: 'wandb.Table',
    x: 'str',
    y: 'str',
    stroke: 'str | None' = None,
    title: 'str' = '',
    split_table: 'bool' = False
) → CustomChart
```

Constructs a customizable line chart.

**Args:**

* `table`:   The table containing data for the chart.
* `x`:  Column name for the x-axis values.
* `y`:  Column name for the y-axis values.
* `stroke`:  Column name to differentiate line strokes (e.g., for  grouping lines).
* `title`:  Title of the chart.
* `split_table`:  Whether the table should be split into a separate section  in the W\&B UI. If `True`, the table will be displayed in a section named  "Custom Chart Tables". Default is `False`.

**Returns:**

* `CustomChart`:  A custom chart object that can be logged to W\&B. To log the  chart, pass it to `wandb.log()`.

**Example:**

```python  theme={null}
import math
import random
import wandb

# Create multiple series of data with different patterns
data = []
for i in range(100):
     # Series 1: Sinusoidal pattern with random noise
     data.append([i, math.sin(i / 10) + random.uniform(-0.1, 0.1), "series_1"])
     # Series 2: Cosine pattern with random noise
     data.append([i, math.cos(i / 10) + random.uniform(-0.1, 0.1), "series_2"])
     # Series 3: Linear increase with random noise
     data.append([i, i / 10 + random.uniform(-0.5, 0.5), "series_3"])

# Define the columns for the table
table = wandb.Table(data=data, columns=["step", "value", "series"])

# Initialize wandb run and log the line chart
with wandb.init(project="line_chart_example") as run:
     line_chart = wandb.plot.line(
         table=table,
         x="step",
         y="value",
         stroke="series",  # Group by the "series" column
         title="Multi-Series Line Plot",
     )
     run.log({"line-chart": line_chart})
```
