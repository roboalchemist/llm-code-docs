# Source: https://docs.wandb.ai/models/ref/python/custom-charts/line_series.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# line_series()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/plot/line_series.py" />

### <kbd>function</kbd> `line_series`

```python  theme={null}
line_series(
    xs: 'Iterable[Iterable[Any]] | Iterable[Any]',
    ys: 'Iterable[Iterable[Any]]',
    keys: 'Iterable[str] | None' = None,
    title: 'str' = '',
    xname: 'str' = 'x',
    split_table: 'bool' = False
) → CustomChart
```

Constructs a line series chart.

**Args:**

* `xs`:  Sequence of x values. If a singular  array is provided, all y values are plotted against that x array. If  an array of arrays is provided, each y value is plotted against the  corresponding x array.
* `ys`:  Sequence of y values, where each iterable represents  a separate line series.
* `keys`:  Sequence of keys for labeling each line series. If  not provided, keys will be automatically generated as "line\_1",  "line\_2", etc.
* `title`:  Title of the chart.
* `xname`:  Label for the x-axis.
* `split_table`:  Whether the table should be split into a separate section  in the W\&B UI. If `True`, the table will be displayed in a section named  "Custom Chart Tables". Default is `False`.

**Returns:**

* `CustomChart`:  A custom chart object that can be logged to W\&B. To log the  chart, pass it to `wandb.log()`.

**Examples:**
Logging a single x array where all y series are plotted against the same x values:

```python  theme={null}
import wandb

# Initialize W&B run
with wandb.init(project="line_series_example") as run:
    # x values shared across all y series
    xs = list(range(10))

    # Multiple y series to plot
    ys = [
         [i for i in range(10)],  # y = x
         [i**2 for i in range(10)],  # y = x^2
         [i**3 for i in range(10)],  # y = x^3
    ]

    # Generate and log the line series chart
    line_series_chart = wandb.plot.line_series(
         xs,
         ys,
         title="title",
         xname="step",
    )
    run.log({"line-series-single-x": line_series_chart})
```

In this example, a single `xs` series (shared x-values) is used for all `ys` series. This results in each y-series being plotted against the same x-values (0-9).

Logging multiple x arrays where each y series is plotted against its corresponding x array:

```python  theme={null}
import wandb

# Initialize W&B run
with wandb.init(project="line_series_example") as run:
    # Separate x values for each y series
    xs = [
         [i for i in range(10)],  # x for first series
         [2 * i for i in range(10)],  # x for second series (stretched)
         [3 * i for i in range(10)],  # x for third series (stretched more)
    ]

    # Corresponding y series
    ys = [
         [i for i in range(10)],  # y = x
         [i**2 for i in range(10)],  # y = x^2
         [i**3 for i in range(10)],  # y = x^3
    ]

    # Generate and log the line series chart
    line_series_chart = wandb.plot.line_series(
         xs, ys, title="Multiple X Arrays Example", xname="Step"
    )
    run.log({"line-series-multiple-x": line_series_chart})
```

In this example, each y series is plotted against its own unique x series. This allows for more flexibility when the x values are not uniform across the data series.

Customizing line labels using `keys`:

```python  theme={null}
import wandb

# Initialize W&B run
with wandb.init(project="line_series_example") as run:
    xs = list(range(10))  # Single x array
    ys = [
         [i for i in range(10)],  # y = x
         [i**2 for i in range(10)],  # y = x^2
         [i**3 for i in range(10)],  # y = x^3
    ]

    # Custom labels for each line
    keys = ["Linear", "Quadratic", "Cubic"]

    # Generate and log the line series chart
    line_series_chart = wandb.plot.line_series(
         xs,
         ys,
         keys=keys,  # Custom keys (line labels)
         title="Custom Line Labels Example",
         xname="Step",
    )
    run.log({"line-series-custom-keys": line_series_chart})
```

This example shows how to provide custom labels for the lines using the `keys` argument. The keys will appear in the legend as "Linear", "Quadratic", and "Cubic".
