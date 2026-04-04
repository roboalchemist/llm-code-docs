# Source: https://docs.wandb.ai/models/app/features/panels/query-panels.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Some features on this page are in beta, hidden behind a feature flag. Add `weave-plot` to your bio on your profile page to unlock all related features.

# Query panels overview

<Note>
  Looking for W\&B Weave? W\&B's suite of tools for Generative AI application building? Find the docs for weave here: [wandb.me/weave](https://wandb.github.io/weave/?utm_source=wandb_docs\&utm_medium=docs\&utm_campaign=weave-nudge).
</Note>

Use query panels to query and interactively visualize your data.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/pretty_panel.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=bbaa3d860550d8f8088bca0062e21d28" alt="Query panel" width="2212" height="1326" data-path="images/weave/pretty_panel.png" />
</Frame>

## Create a query panel

Add a query to your workspace or within a report.

<Tabs>
  <Tab title="Project workspace">
    1. Navigate to your project's workspace.
    2. In the upper right hand corner, click `Add panel`.
    3. From the dropdown, select `Query panel`.
  </Tab>

  <Tab title="W&B Report">
    Type and select `/Query panel`.

    <Frame>
      <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/add_weave_panel_report_1.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=20f4bae1adc4264297ec79a979cd1be8" alt="Query panel option" width="473" height="370" data-path="images/weave/add_weave_panel_report_1.png" />
    </Frame>

    Alternatively, you can associate a query with a set of runs:

    1. Within your report, type and select `/Panel grid`.
    2. Click the `Add panel` button.
    3. From the dropdown, select `Query panel`.
  </Tab>
</Tabs>

## Query components

### Expressions

Use query expressions to query your data stored in W\&B such as runs, artifacts, models, tables, and more.

#### Example: Query a table

Suppose you want to query a W\&B Table. In your training code you log a table called `"cifar10_sample_table"`:

```python  theme={null}
import wandb
with wandb.init() as run:
  run.log({"cifar10_sample_table":<MY_TABLE>})
```

Within the query panel you can query your table with:

```python  theme={null}
runs.summary["cifar10_sample_table"]
```

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/basic_weave_expression.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=b4767631afdad8b3e6994bb9e01a21f6" alt="Table query expression" width="316" height="56" data-path="images/weave/basic_weave_expression.png" />
</Frame>

Breaking this down:

* `runs` is a variable automatically injected in Query Panel Expressions when the Query Panel is in a Workspace. Its "value" is the list of runs which are visible for that particular Workspace. [Read about the different attributes available within a run here](/models/track/public-api-guide/#understanding-the-different-attributes).
* `summary` is an op which returns the Summary object for a Run. Ops are *mapped*, meaning this op is applied to each Run in the list, resulting in a list of Summary objects.
* `["cifar10_sample_table"]` is a Pick op (denoted with brackets), with a parameter of `predictions`. Since Summary objects act like dictionaries or maps, this operation picks the `predictions` field off of each Summary object.

To learn how to write your own queries interactively, see the [Query panel demo](https://wandb.ai/luis_team_test/weave_example_queries/reports/Weave-queries---Vmlldzo1NzIxOTY2?accessToken=bvzq5hwooare9zy790yfl3oitutbvno2i6c2s81gk91750m53m2hdclj0jvryhcr).

### Configurations

Select the gear icon on the upper left corner of the panel to expand the query configuration. This allows the user to configure the type of panel and the parameters for the result panel.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_panel_config.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=d515278ecfa57e3c15cf13eec985cc85" alt="Panel configuration menu" width="1464" height="576" data-path="images/weave/weave_panel_config.png" />
</Frame>

### Result panels

Finally, the query result panel renders the result of the query expression, using the selected query panel, configured by the configuration to display the data in an interactive form. The following images shows a Table and a Plot of the same data.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/result_panel_table.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=7f56e3cb7d542591e1c8f39b27e05396" alt="Table result panel" width="1074" height="471" data-path="images/weave/result_panel_table.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/result_panel_plot.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=13e619c59eb3100452e2d93b6380f125" alt="Plot result panel" width="1073" height="471" data-path="images/weave/result_panel_plot.png" />
</Frame>

## Basic operations

The following common operations you can make within your query panels.

### Sort

Sort from the column options:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_sort.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=aed1594e5adb3fe74dcfbc643e74befd" alt="Column sort options" width="1072" height="471" data-path="images/weave/weave_sort.png" />
</Frame>

### Filter

You can either filter directly in the query or using the filter button in the top left corner (second image)

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_filter_1.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=3f48215246da6f0a8eed3c1fb7ede846" alt="Query filter syntax" width="1071" height="471" data-path="images/weave/weave_filter_1.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_filter_2.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=fba3799c7fc494ea3699a5a079fa3141" alt="Filter button" width="1071" height="470" data-path="images/weave/weave_filter_2.png" />
</Frame>

### Map

Map operations iterate over lists and apply a function to each element in the data. You can do this directly with a panel query  or by inserting a new column from the column options.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_map.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=1d2573b53e6a3de93a91a768c655675a" alt="Map operation query" width="1073" height="471" data-path="images/weave/weave_map.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_map.gif?s=d46c1326a948f3298912151f0f9d143a" alt="Map column insertion" width="600" height="269" data-path="images/weave/weave_map.gif" />
</Frame>

### Groupby

You can groupby using a query or from the column options.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_groupby.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=e369ebec8307c504551d33c0c3382781" alt="Group by query" width="1805" height="459" data-path="images/weave/weave_groupby.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_groupby.gif?s=a587f3e99d74436b009974b461de0edf" alt="Group by column options" width="600" height="234" data-path="images/weave/weave_groupby.gif" />
</Frame>

### Concat

The concat operation allows you to concatenate 2 tables and concatenate or join from the panel settings.

### Join

It is also possible to join tables directly in the query. Consider the following query expression:

```python  theme={null}
project("luis_team_test", "weave_example_queries").runs.summary["short_table_0"].table.rows.concat.join(\
project("luis_team_test", "weave_example_queries").runs.summary["short_table_1"].table.rows.concat,\
(row) => row["Label"],(row) => row["Label"], "Table1", "Table2",\
"false", "false")
```

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_join.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=f8316f331f0684ae8eecf8a62c5d318f" alt="Table join operation" width="1804" height="458" data-path="images/weave/weave_join.png" />
</Frame>

The table on the left is generated from:

```python  theme={null}
project("luis_team_test", "weave_example_queries").\
runs.summary["short_table_0"].table.rows.concat.join
```

The table in the right is generated from:

```python  theme={null}
project("luis_team_test", "weave_example_queries").\
runs.summary["short_table_1"].table.rows.concat
```

Where:

* `(row) => row["Label"]` are selectors for each table, determining which column to join on
* `"Table1"` and `"Table2"` are the names of each table when joined
* `true` and `false` are for left and right inner/outer join settings

## Runs object

Use query panels to access the `runs` object. Run objects store records of your experiments. You can find more details in [Accessing runs object](https://wandb.ai/luis_team_test/weave_example_queries/reports/Weave-queries---Vmlldzo1NzIxOTY2?accessToken=bvzq5hwooare9zy790yfl3oitutbvno2i6c2s81gk91750m53m2hdclj0jvryhcr#3.-accessing-runs-object) but, as quick overview, `runs` object has available:

* `summary`: A dictionary of information that summarizes the run's results. This can be scalars like accuracy and loss, or large files. By default, `wandb.Run.log()` sets the summary to the final value of a logged time series. You can set the contents of the summary directly. Think of the summary as the run's outputs.
* `history`: A list of dictionaries meant to store values that change while the model is training such as loss. The command `wandb.Run.log()` appends to this object.
* `config`: A dictionary of the run's configuration information, such as the hyperparameters for a training run or the preprocessing methods for a run that creates a dataset Artifact. Think of these as the run's "inputs"

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_runs_object.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=fed1f0c4af8b940ba620b6eee0606112" alt="Runs object structure" width="1797" height="427" data-path="images/weave/weave_runs_object.png" />
</Frame>

## Access Artifacts

Artifacts are a core concept in W\&B. They are a versioned, named collection of files and directories. Use Artifacts to track model weights, datasets, and any other file or directory. Artifacts are stored in W\&B and can be downloaded or used in other runs. You can find more details and examples in [Accessing artifacts](https://wandb.ai/luis_team_test/weave_example_queries/reports/Weave-queries---Vmlldzo1NzIxOTY2?accessToken=bvzq5hwooare9zy790yfl3oitutbvno2i6c2s81gk91750m53m2hdclj0jvryhcr#4.-accessing-artifacts). Artifacts are normally accessed from the `project` object:

* `project.artifactVersion()`: returns the specific artifact version for a given name and version within a project
* `project.artifact("")`: returns the artifact for a given name within a project. You can then use `.versions` to get a list of all versions of this artifact
* `project.artifactType()`: returns the `artifactType` for a given name within a project. You can then use `.artifacts` to get a list of all artifacts with this type
* `project.artifactTypes`: returns a list of all artifact types under the project

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wYBIlf7cqDpGjWr9/images/weave/weave_artifacts.png?fit=max&auto=format&n=wYBIlf7cqDpGjWr9&q=85&s=bca00ab31e6016af6d05a6661223565f" alt="Artifact access methods" width="1798" height="662" data-path="images/weave/weave_artifacts.png" />
</Frame>
