# Source: https://docs.wandb.ai/models/ref/python/custom-charts/plot_table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# plot_table()

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/plot/custom_chart.py" />

### <kbd>function</kbd> `plot_table`

```python  theme={null}
plot_table(
    vega_spec_name: 'str',
    data_table: 'wandb.Table',
    fields: 'dict[str, Any]',
    string_fields: 'dict[str, Any] | None' = None,
    split_table: 'bool' = False
) → CustomChart
```

Creates a custom charts using a Vega-Lite specification and a `wandb.Table`.

This function creates a custom chart based on a Vega-Lite specification and a data table represented by a `wandb.Table` object. The specification needs to be predefined and stored in the W\&B backend. The function returns a custom chart object that can be logged to W\&B using `wandb.Run.log()`.

**Args:**

* `vega_spec_name`:  The name or identifier of the Vega-Lite spec  that defines the visualization structure.
* `data_table`:  A `wandb.Table` object containing the data to be  visualized.
* `fields`:  A mapping between the fields in the Vega-Lite spec and the  corresponding columns in the data table to be visualized.
* `string_fields`:  A dictionary for providing values for any string constants  required by the custom visualization.
* `split_table`:  Whether the table should be split into a separate section  in the W\&B UI. If `True`, the table will be displayed in a section named  "Custom Chart Tables". Default is `False`.

**Returns:**

* `CustomChart`:  A custom chart object that can be logged to W\&B. To log the  chart, pass the chart object as argument to `wandb.Run.log()`.

**Raises:**

* `wandb.Error`:  If `data_table` is not a `wandb.Table` object.

**Example:**

```python  theme={null}
# Create a custom chart using a Vega-Lite spec and the data table.
import wandb

data = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
table = wandb.Table(data=data, columns=["x", "y"])
fields = {"x": "x", "y": "y", "title": "MY TITLE"}

with wandb.init() as run:
   # Training code goes here

   # Create a custom title with `string_fields`.
   my_custom_chart = wandb.plot_table(
        vega_spec_name="wandb/line/v0",
        data_table=table,
        fields=fields,
        string_fields={"title": "Title"},
   )

   run.log({"custom_chart": my_custom_chart})
```
