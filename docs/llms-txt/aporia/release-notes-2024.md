# Source: https://docs.aporia.com/release-notes/release-notes-2024.md

# Release Notes 2024

Welcome 2024! :tada: We are extremely excited for the year ahead as we continuously enhance our platform to ensure that you and your team can observe your models in production, detect issues and improve their performance as efficiently as possible.

In this page, you'll be able to find a constantly-growing list of some of our most impactful new features and enhancements that we release every month.

## October 2024

* **Custom Metric Monitors:** Added the ability to alert on a specific segment from the Aporia UI and run comparisons to segment or training data.
* **Improved error messages for model integration:** Resolved an issue where users received JSON-formatted error messages in the "test-dataset/check compatibility" flow. The error messages are now human-readable.
* **Global Dashboards edits are now saved:** Fixed an issue with global dashboards, all edits are now properly saved once you click on ‘save changes’ on each widget.
* **Move workspace:** Fix the error with the move workspace feature.

## August - September 2024

* **Dashboard Creation via SDK:**  Users can now build dashboards programmatically using the SDK.
* **Monitor Support for Current Day Runs:**  Users can now run monitors for the current day, in addition to previous days.
* **Global Version Filters in Dashboards:**  Introduced global filters in dashboards, allowing users to change the configuration of all widgets together.
* **API for Monitor Runs and Calculation Status:**
  * **Run Monitors API:** A new external API to trigger monitor runs by ID, with success status response.
  * **Calculation Status API:** Reflects the calculation status of Models, Versions, and Datasets we have in the dashboard.

## June - July 2024

* **API for Dashboards:** CRUD for Dashboards: Support an external API to create, update  and delete dashboards.
* **Teams Connector support Power Automate:** Support for Power Automate workflows integration for Teams Connectors to work after retirement of old teams connector support by Microsoft.
* **Aporia UI Resilience:** Aporia UI and models will now continue to work even in cases of dataplane major dataplane errors (EMR/Databricks/etc clusters unreachable).
* **Dataplane Control:** Users can now reconfigure & restart their dataplane in case of errors using an API.
* **Embedding Projector UMAP Bug:** Data Points in the embedding projector should now work properly.
* **UI Overflow Issue in Segment Editing:** Addressed an issue where the UI overflowed when editing segments with many dependencies, making the confirm button unclickable.
* **Negative Values for Monitors:** Fixed an issue that prevented users from setting negative values when configuring thresholds for monitors using the Absolute Values detection method. Negative values are now supported.
* **Optional Absolute Value Thresholds:** Previously, users could not nullify the upper and lower bounds of absolute value thresholds once set. Either bound can now be nullified, but not both.
* **Data Health Table Version Comparison:** Fixed an issue where the "Compare" version in the data health table did not update correctly when switching versions. The "Compare" tab version now automatically matches the "Data" tab version.
* **Grouped Alert Resolution:** Resolving a main alert in an alert group now resolves all associated child alerts.

## April - May 2024

* **Cumulative view for time series widgets** - Aporia now allows you to configure time series widgets to display cumulative value of the chosen metric. Cumulation is computed since the start time of the series.
* **Sort workspaces list alphabetically**.
* **Move models between workspaces** - Remove visibility of “Move Workspace” action for non-admin users.
* **Deactivate version bug fix** - Aporia will now exclude deactivated versions from the following:
  * Recalculation schedules
  * Activity monitors
* **Training baseline in investigation room cells** - You can now configure training as baseline for relevant IR cells.
* **Min threshold for percentage change monitors** - you can now set both min and max thresholds for percentage change monitors.
* **Data sources UI fix** - When editing data sources, configured optional SQL transformations will now appear.

## February - March 2024

* **Move models between workspaces** - Aporia now allows account admins to move models between different workspaces. Models will be moved along with all their related resources such as monitors, alerts, dashboards, etc. In case one of the model’s datasets / monitors are using a data source / integration (respectively) that does not exist in the new workspace, a new data source / integration will automatically be created in the new workspace with the same configuration.
* **Using the same SSO integration for different Aporia accounts** - For organizations that have multiple Aporia accounts, it is now possible to use the same SSO integration in order to connect them both. The default account users log into is constant for all users and can be changed by your Aporia account representative.

## December - January 2024

* **Data Points cell** - Improving performance of the data points cell in the Investigation Room. Only filtered columns will be loaded automatically. You can still change the field's filtering as you wish.
* **Bug fix -** Fixing an issue with dates displayed at the activity histogram in the models overview page for hourly-granularity models.
* **Oracle data source** - Oracle database can now be used as an Aporia data source to directly connect your model’s data.

## November 2023

* **Code Based metrics** - Added support for sklearn as a 3rd party library.
* **Ability to set metrics recalculation schedule** - Aporia now allows you to set the cadence and extent at which you would like to recalculate metrics per each model. This can be useful to handle delayed actuals / inputs. Customizing recalculation according to your data updates schedules can be used to reduce costs.
