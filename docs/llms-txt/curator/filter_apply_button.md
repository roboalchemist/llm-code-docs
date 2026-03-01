# Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/filter_apply_button.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter Apply Button

> Configure apply buttons for filters to control when filter changes are applied to dashboard visualizations.

Each Filter and Parameter gets applied as soon as their values are changed. When you have many filters and parameters,
this can become time-consuming. To alleviate this issue we have created the "Apply" button. This button will not apply
any of your changes until you click on it.

## Enable the Filter Apply Button

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on the **Settings** > **Tableau** > **Tableau Server Settings** in the left-hand menu.
4. Click the "General" tab at the top.
5. Expand the "Filters and Parameters" section.
6. Click to switch on the "Filters and Parameters Apply Button".
7. Click the "Save" button.

*Note*: Date Range Filters have their own apply button. As a result, they are applied
to the report immediately after this button is pressed. They do not respond to Curator's
Apply button.
