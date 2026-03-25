# Source: https://docs.wandb.ai/models/runs/filter-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Learn how to filter runs in the Runs table using the expression editor.

# Filter runs

Filter runs based on their name, state, [tags](#filter-runs-with-tags), or other properties with the expression editor in the Runs Table.

When you add a filter, you first choose a field (for example, tags, timestamp, or entity). Each field has an underlying type, such as text, time, or ID.

The list of operators you see (for example, is, in, ≥, within last) depends on this type. After you choose a field, the UI only shows operators that are valid for that field’s type.

## Common operators by type

| Filter type | Example fields      | Common operators       | Example usage                      |
| ----------- | ------------------- | ---------------------- | ---------------------------------- |
| Tags        | `tags`              | is, is not, in, not in | `tags is "baseline"`               |
| Time        | `created timestamp` | ≤, ≥, within last      | `created timestamp` ≥ `01/16/2026` |
| String      | `state`             | =, ≠, IN, NOT IN       | `state = "finished"`               |

<Note>
  The above table shows only a subset of available fields and operators. The expression editor shows all available fields and operators.
</Note>

## Create a filter expression

1. Navigate to the **Runs** tab from the project sidebar.
2. Select the **Filter** button, which looks like a funnel, above the runs table.
3. From left to right, select a column name, a logical operator, and a filter value to create a filter expression.
4. Optionally select **New Filter** to apply additional filters.

The following image filters runs based on loss values less than or equal to `1`:

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/HPMLIguh3EdiRO94/images/data_vis/filter.png?fit=max&auto=format&n=HPMLIguh3EdiRO94&q=85&s=fbe393d6e6ce9f6bef98d1bad9fdbf10" alt="Incorrect predictions filter" width="1497" height="587" data-path="images/data_vis/filter.png" />
</Frame>

The following sections show some examples of how to filter runs in the Runs table.

### Example: Filter runs with tags

Filter runs based on their tags:

1. Click on the **Runs** tab from the project sidebar.
2. Select the **Filter** button, which looks like a funnel, above the runs table.
3. From left to right, select `"Tags"` from the dropdown menu select a logic operator.
4. Select is, is not, in, or not in from the second dropdown menu.
5. Enter the tag name you want to filter by from the third dropdown menu.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/ZDqxXQYvQVF43fU1/images/app_ui/filter_runs.gif?s=ed74c1eb9c3cb38819502f84190008ac" alt="Filter runs by tags" width="2716" height="1378" data-path="images/app_ui/filter_runs.gif" />
</Frame>

## Default filters

By default, W\&B provides the following filters:

* **Show only my works**: Shows only runs created by the current user.
* **Hide crashed runs**: Hides runs with the `crashed` state.

Default filters appear as toggles below the **New filter** button in the filter expression editor.

## Remove a filter

To remove a filter from the Runs table:

1. Click on the **Filter** button, which looks like a funnel, above the runs table.
2. Select the `x` icon next to the filter you want to remove.

{/*
  Look for a green dot next to the name of runs— this indicates they're active in the table and on the graph legends.
  */}

{/*
  ## Select all runs in table

  Click the checkbox in the upper left corner of the table, and click "Select all runs" to select every run that matches the current set of filters.

  <Frame>
    <img src="/images/app_ui/all_runs_select.gif"  />
  </Frame>
  */}
