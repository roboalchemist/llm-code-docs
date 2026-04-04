# Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/parameters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Parameters

> Set up parameters to control dashboard behavior and calculations, enabling dynamic user interactions with analytics content.

Parameters are used for various purposes within a Dashboard. The system provides a user-friendly way to enter and
change the parameter values for dashboards. Parameters can even be shared with more than one Dashboard.

## To create a parameter

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on **Tableau** > **Parameters** in the left-hand menu.
4. Click the "New Parameter" button.
5. Enter the name of the parameter you want to be shown to your users in the "Display Name" field.
6. Enter the name of the parameter from the Dashboard in the "Parameter Name" field. This field text should be edited
   to match the field name in the data exactly. If there are any trailing white-spaces those will be removed on saving so
   you will need to remove them from the data name.
7. Select the parameter type.
8. Select the filter category if desired. See the [Filter Categories Section](/embedding_using_analytics/filters_parameters/filter_categories)
   for more
   information.
9. Select existing dashboards to add the parameter to them.
10. If you want to, enter a default value for the parameter to load the Dashboard with initially.
11. If you want the parameter value to be remembered from one Dashboard to the next, turn on the sticky parameter feature.
12. If you want to get the parameter options from the Dashboard's allowable values list, turn on that feature.
13. If you want to get the parameter options from the Dashboard's data, turn on the "get parameter options from data"
    feature. Note that this will be slow if the Dashboard contains a lot of data.
14. Add parameter options if not getting the options directly from the Dashboard.
15. Click the "Save" button.

## Or add a parameter to a Dashboard from the Dashboard

1. While editing the Dashboard, click on the "Misc" tab.
2. Expand the "Filters & Parameters" section.
3. Select the parameter(s) that are applicable to the Dashboard.
4. Click the "Save" button.

## To apply a Parameter

1. Navigate to the frontend of the system (e.g. `http://curatorexample.com`).
2. Log in if prompted.
3. Navigate to the desired Dashboard by using the navigation menu.
4. Open the filter menu on the right side of the screen.
5. Select or enter the value of the parameter.

### Multi Select Parameter Controls

Currently, Tableau does not offer multi-select-parameter controls. Instead, you can select one parameter value at a
time or type the long names by hand. In Curator, you can set up a parameter to allow multi-selection of your parameter
values without typing everything in.

1. Navigate to Tableau Desktop (or Tableau Server Edit Mode), and go to the sheet that the parameter should be applied to.
2. Create the parameter you need, and make sure
   * the Data type is a ***String***
   * the Current value is set to ***(ALL)***
   * the Allowable values is set to ***All***
3. Create a calculated field
   * `[param name]='(ALL)' OR CONTAINS([param name], [values field])`
   * Drag the calculated field onto the filter shelf and allow only ***True***
4. Publish Dashboard.
5. Do the steps described above to create a parameter in Curator backend, make sure
   * the Parameter type is ***Multi-Select***
   * toggle on ***Get parameter options from a field in the data***
   * enter the name of \[values field] (see 3.a) in ***Field Name*** input field
6. Click the "Save" button

### Step-by-step Guide

You can also follow the
[step-by-step guide](https://interworks.com/blog/tladd/2018/07/16/5-steps-to-enabling-a-multi-select-parameter-control-in-tableau/)
with screenshots that Tanner put together.
