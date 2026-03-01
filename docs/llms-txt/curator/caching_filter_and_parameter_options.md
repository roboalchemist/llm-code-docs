# Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/caching_filter_and_parameter_options.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Caching Filter and Parameter Options

> Optimize performance by configuring caching strategies for filter and parameter options to reduce load times.

Curator has the ability to populate the filter and parameter options from the Dashboard's data by using the
"Get Filter Options from data". This option is normally only enabled when you have a large number of options to
retrieve for the filter. The time to retrieve all these options can take a while if you have several hundred or several
thousands of options. While we can't speed up the initial time, we can make subsequent requests faster. To do this
enable "Cache filter/parameter options from data" after enabling "Get Filter options from data".

## To enable Cache Filter/Parameter Options

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`).
2. Log in if prompted.
3. Click on "Tableau" in the left-hand menu.
4. Click on the "Filters" or "Parameters" link on the left.
5. Click to switch on the "Cache filter options from data" under the Display Options section of a filter or parameter.
6. Select the desired cache time from the dropdown below the switch.
7. Click the "Save" button.
