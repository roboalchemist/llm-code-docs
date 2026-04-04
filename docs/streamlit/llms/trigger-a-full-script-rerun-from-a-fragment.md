# Source: https://docs.streamlit.io/develop/tutorials/execution-flow/trigger-a-full-script-rerun-from-a-fragment

# Trigger a full-script rerun from inside a fragment

Streamlit lets you turn functions into [fragments](/develop/concepts/architecture/fragments), which can rerun independently from the full script. When a user interacts with a widget inside a fragment, only the fragment reruns. Sometimes, you may want to trigger a full-script rerun from inside a fragment. To do this, call [st.rerun](/develop/api-reference/execution-flow/st.rerun) inside the fragment.

## Applied concepts

- Use a fragment to rerun part or all of your app, depending on user input.

## Prerequisites

- This tutorial requires the following version of Streamlit:
  ```text
  streamlit>=1.37.0
  ```
- You should have a clean working directory called `your-repository`.
- You should have a basic understanding of fragments and `st.rerun`.

## Summary

In this example, you'll build an app to display sales data. The app has two sets of elements that depend on a date selection. One set of elements displays information for the selected day. The other set of elements displays information for the associated month. If the user changes days within a month, Streamlit only needs to update the first set of elements. If the user selects a day in a different month, Streamlit needs to update all the elements.

You'll collect the day-specific elements into a fragment to avoid rerunning the full app when a user changes days within the same month. If you want to jump ahead to the fragment function definition, see [Build a function to show daily sales data](#build-a-function-to-show-daily-sales-data).

## Build the example

### Initialize your app

1. Give your app a wide layout.
2. Get your data.
3. Add a title and description for your app.
4. Create columns and call the functions to display data.

### Make it pretty

Now, you have a functioning app that uses a fragment to prevent unnecessarily redrawing the monthly data. However, things aren't aligned on the page, so you can insert a few containers to make it pretty. Add three containers into each of the display functions.

1. Add three containers to fix the height of elements in the `show_daily_sales` function.
2. Add three containers to fix the height of elements in the `show_monthly_sales` function.

## Next steps

Continue beautifying the example. Try using [st.plotly_chart](/develop/api-reference/charts/st.plotly_chart) or [st.altair_chart](/develop/api-reference/charts/st.altair_chart) to add labels to your charts and adjust their height.