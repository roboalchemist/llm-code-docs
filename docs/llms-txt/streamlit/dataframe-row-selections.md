# Get dataframe row-selections from users

Streamlit offers two commands for rendering beautiful, interactive dataframes in your app. If you need users to edit data, add rows, or delete rows, use `st.data_editor`. If you don't want users to change the data in your dataframe, use `st.dataframe`. Users can sort and search through data rendered with `st.dataframe`. Additionally, you can activate selections to work with users' row and column selections.

This tutorial uses row selections, which were introduced in Streamlit version 1.35.0. For an older workaround using `st.data_editor`, see [Get dataframe row-selections (streamlit<1.35.0)](/develop/tutorials/elements/dataframe-row-selections-old).

## Applied concepts

- Use dataframe row selections to filter a dataframe.

## Prerequisites

- This tutorial requires the following version of Streamlit:
  ```text
  streamlit>=1.35.0
  ```
- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of caching and `st.dataframe`.

## Summary

In this example, you'll build an app that displays a table of members and their activity for an imaginary organization. Within the table, a user can select one or more rows to create a filtered view. Your app will show a combined chart that compares the selected employees.

Here's a look at what you'll build:

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Combine activity data for the selected rows

1. Create an empty dictionary to store (yearly) activity data.
   ```python
   activity_df = {}
   ```
2. Iterate through selected rows and save each member's activity in the dictionary indexed by their name.
   ```python
   for person in people:
       activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
   ```
3. Convert the activity dictionary into a `pandas.DataFrame`.
   ```python
   activity_df = pd.DataFrame(activity_df)
   ```
4. Repeat the previous three steps similarly for daily activity.
   ```python
   daily_activity_df = {}
   for person in people:
       daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
   daily_activity_df = pd.DataFrame(daily_activity_df)
   ```
5. Optional: Test out your combined data by displaying it.
   ```python
   st.dataframe(activity_df)
   st.dataframe(daily_activity_df)
   ```

## Use charts to visualize the activity comparison

1. Start a conditional block to check if anyone is currently selected.
   ```python
   if len(people) > 0:
       # Since no members are selected when the app loads, this check will prevent empty charts from being displayed.
   ```
2. Add a header to identify your first chart.
   ```python
   st.header("Daily activity comparison")
   ```
3. Show the daily activity comparison in a bar chart.
   ```python
   st.bar_chart(daily_activity_df)
   ```
4. Similarly, for yearly activity, add a header and line chart.
   ```python
   st.header("Yearly activity comparison")
   st.line_chart(activity_df)
   ```
5. Complete the conditional block with a default message to show when no members are selected.
   ```python
   else:
       st.markdown("No members selected.")
   ```

## Make it pretty

You should have a functioning app at this point. Now you can beautify it. In this section, you'll separate the selection UI from the comparison by using `st.tabs`.

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people:
           daily_activity_df[df.iloc[person]["name"]] = df.iloc[person]["daily_activity"]
       daily_activity_df = pd.DataFrame(daily_activity_df)
       if len(people) > 0:
           st.header("Daily activity comparison")
           st.bar_chart(daily_activity_df)
           st.header("Yearly activity comparison")
           st.line_chart(activity_df)
       else:
           st.markdown("No members selected.")
   ```

## Build the example

1. Immediately after the column configuration definition, insert two tabs.
   ```python
   select, compare = st.tabs(["Select members", "Compare selected"])
   ```
2. Indent the code following the line in the previous step and group it into the two new tabs.
   ```python
   with select: # Add select tab
       st.header("All members")
       df = get_profile_dataset()
       event = st.dataframe(
           df,
           column_config=column_configuration,
           use_container_width=True,
           hide_index=True,
           on_select="rerun",
           selection_mode="multi-row",
       )
       st.header("Selected members")
       people = event.selection.rows
       filtered_df = df.iloc[people]
       st.dataframe(
           filtered_df,
           column_config=column_configuration,
           use_container_width=True,
       )
   with compare: # Add compare tab
       activity_df = {}
       for person in people:
           activity_df[df.iloc[person]["name"]] = df.iloc[person]["activity"]
       activity_df = pd.DataFrame(activity_df)
       daily_activity_df = {}
       for person in people: