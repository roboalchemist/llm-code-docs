# Source: https://docs.curator.interworks.com/embedding_using_analytics/filters_parameters/preloading_filters_and_parameters.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Preloading Filters and Parameters

> Improve user experience by preloading filter and parameter values to reduce wait times during dashboard interactions.

## Setup

When you filter your Tableau Dashboards in Curator, this is typically done through the Tableau JavaScript API after the
Dashboard has loaded. This post-load filtering process will cause the Dashboard to refresh. If the filter or parameter
values are already known before the Dashboard is loaded, though sticky filters/parameters or because you want to
explicitly define them, you can take advantage of Preload Filters and Parameters. This feature injects the filter and
parameter values directly into the Dashboard’s initial load request (within the HTML), rather than applying them via
JavaScript afterward. The result is a faster, cleaner user experience with no visible reload.

When using Tableau's Connected Apps for the Embed authentication ([more details on Connected Apps](/creating_integrations/tableau_connection/embed_authentication))
you can no longer preload filters and parameters by appending them to the Tableau Server Dashboard URL on the
edit page of a Dashboard. Instead you can specify them by following these steps:

1. Navigate to your Curator backend > Tableau > Dashboards.
2. Select the Dashboards you want to define filters or parameters for that should be applied on load.
3. Switch to the Filters tab and open the **Preloading Filters & Parameters** section.
4. Add an item and enter the filter's/parameter's name into the name field as shown in the datasource/in the workbook.
5. Enter the value that you want the filter/parameter to preload with into the value field. You can leave it blank if
   you want the Dashboard to listen for possible preload options given through the Curator URL or sticky filters/parameters.
6. Specify whether this is a filter or a parameter in the type field.
7. Save the Dashboard.

> **Note:** When trying to filter on secondary datasources you'll likely see unexpected behavior.
> This is due to Tableau's embedding limitations. The JavaScript API still works on secondary
> datasources, but preloading may not function as expected.

When using Tableau's Trusted Ticket authentication (Attention: Deprecated!) you can append the name-value pairs to the
Tableau Server Dashboard URL directly.

## Preload Behavior

In the value field, you can enter the specific value you want the filter or parameter to preload with when the Dashboard
is initially rendered. This value will be directly injected into the HTML and used during the first load of the
visualization. No JavaScript will be executed to apply the filter/parameter, i.e. no reload will happen.
If you leave the value field blank, Curator will look for a matching value from other sources to optimize your initial
load experience, such as sticky filters/parameters saved from previous analysis steps or values passed through the
Curator URL (e.g., ?Region=West).
This makes the preload feature flexible: you can hardcode a default if needed, or allow Curator to dynamically detect
and apply a value based on your user's context.

### Full Domain Loading for Curator Filters

*This feature is only available when using [Connected Apps](/creating_integrations/tableau_connection/embed_authentication)
to authenticate to your Tableau Server.*

Curator gives you the flexibility to control whether Curator filters load with the full domain of
available values or only the subset of preloaded values. This setting can be configured individually for
each Dashboard.

To configure this behavior:

1. Navigate to your Curator backend > Tableau > Dashboards.
2. Select the Dashboard you want to configure.
3. Switch to the Filters tab and open the **Preloading Filters & Parameters** section.
4. Use the toggle **Preload Filters with Full Domain Values** to enable full domain loading or disable it to show
   only filtered values.

When enabled, users will see all possible filter values, maintaining full filtering capability while still benefiting
from the performance improvements of preloaded filters.

**Note**: To use the full domain values feature, ensure your field is placed on at least one filter shelf in your
Dashboard. The filter doesn't need to be visible or have a value applied, just Tableau needs to recognize it as a filter.

## Migration notice

If you used the Tableau Server Dashboard URL parameters you do not need to move everything manually once you are switching
to Connected Apps. They should be migrated for you once you upgrade to version when they became available. To have the
type automatically declared you will need to have Tableau's Metadata API enabled.
In case you want to rerun the migration and make sure filters and parameters are declared correctly do:

1. Run the migration command in the browser's address bar by just appending **/up** to you Curator domain.
2. In the console on your server, navigate to the root directory and run:

   ```php {/*cspell:disable-next-line*/} theme={null}
   php artisan tableauviz:updatepreloadsettings
   ```

   This will try to connect to the primary's Tableau Metadata
   API and check whether the specified names are parameters, otherwise they will be declared as filters.

To maintain previous functionality, we decided to migrate existing preload filters to not load the full domain of values.
However you can easily adjust the setting per Dashboard according to your needs.
