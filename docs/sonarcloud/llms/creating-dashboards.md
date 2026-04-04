# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/dashboards/creating-dashboards.md

# Creating dashboards

This feature is available in the [Enterprise](https://www.sonarsource.com/plans-and-pricing/sonarcloud/) plan.

There are two ways to create a custom dashboard, by duplicating an existing dashboard or by creating one from scratch.

{% embed url="<https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgkayo3lNKqjg0fRI1udh%2Fcreate-custom-dashboard.mp4?alt=media&token=66a3c6ac-c6a1-499c-a381-b0fdb6abb8af>" %}

### Duplicating an existing dashboard

You can duplicate an existing dashboard and use it as a starting point. Sometimes, this is the fastest way to get started.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2FKkXAIKzDpu1aNtkeAG7L%2Fdashboards-duplicate.png?alt=media&#x26;token=9a39b482-d19c-49e4-838e-cb36e4cfb626" alt="duplicating a dashboard on All dashboards page"><figcaption></figcaption></figure>

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more information.
2. Select the **Main Branch** from the left side menu.
3. Click **Dashboards** from the top menu and select **All dashboards**.
4. Click on the action menu next to the existing dashboard and select **Duplicate**. You can only duplicate custom dashboards.
5. In the **Duplicate dashboard** modal enter the dashboard name, description and click **Create duplicate**. The new dashboard appears on the All dashboards page.
6. Click on the action menu next to the duplicated dashboard and select **Edit** to customize it.

### Creating a custom dashboard from scratch

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2FwvVsg1sRNx6dmMO70huU%2Fdashboards-create-custom-dashboard.png?alt=media&#x26;token=f7067979-1896-4489-bca2-0e083a07475d" alt="Creating a new custom dashboard"><figcaption></figcaption></figure>

To create a custom dashboard from scratch:

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more information.
2. Select the **Main Branch** from the left side menu.
3. Click **Dashboards** from the top menu and select either **All dashboards**.
4. Click **Create custom dashboard** button in the top right corner.
5. In the **Create custom dashboard** modal enter the dashboard name, description and click **Create**. The new dashboard appears on the **All dashboards** page.
6. Click on the action menu next to the new dashboard and select **Edit** to customize it.

Once you are in the edit mode you can select the following option at the top of the page:

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-572a8f9c77057461a7677c5d4d494ff120de3b77%2Fdashboards-edit-options.png?alt=media" alt="Dashboards editing options"><figcaption></figcaption></figure>

* **Add widget**: Opens a modal where you can configure the widget. See [#adding-a-widget](#adding-a-widget "mention").
* **Add section**: Sections group a set of widgets together and are collapsible. See [#adding-sections](#adding-sections "mention")
* **Cancel and exit**: Exits the edit mode without saving the changes.
* **Save changes**: Saves the current changes.

### Adding a widget

In the dashboard’s edit mode, click **Add widget** to open a modal. In the **Add new widget** modal follow these steps:

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-a4d8709285f31d1d2ea966eeb6dd16d3a63cc320%2Fdashboards-add-new-widget.png?alt=media" alt="Configuring a new widget"><figcaption></figcaption></figure></div>

{% stepper %}
{% step %}
**Define your widget**

* **Visualization**: Choose the visualization that will represent the data. The options are: **Count**, **Rating badge**, **Line chart**, **Donut chart**, and **Pie chart**. See [#viewing-dashboards](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/viewing-and-managing-dashboards#viewing-dashboards "mention") for more information about the chart options.
* **Metric**: Choose the metric you want to visualize. The metric drop-down list is filtered by metrics available for the visualization you have selected. See [#metrics](#metrics "mention") for a list of available metrics and associated visualizations.
* **Slice by**: This option appears only for pie and donut charts. Available options depend on the metric you have chosen.
  {% endstep %}

{% step %}
**Apply filters**

Depending on the metric you have selected in the previous step, appropriate filters are displayed. Feel free to explore the filters and combine them with various metrics to find the desired results.

* **Scope**: For the count, rating badge, pie, and donut chart visualizations, you can choose between **Overall code** or **New code**. For the line chart, **Overall code** is the only option and is applied by default.
* **Time range**: This option appears only for the line chart because it is a time-based chart. The options are: **All**, **Last 3 months**, and **Last month**.
* Additional filters appear that are relevant to the visualization and metric you selected in the previous step.
  {% endstep %}

{% step %}
**Customize visualization**

* **Show legend**: Select this option to display a legend for a visualization. This applies to the line, donut and pie charts.
* **Show trend indicator**: Available only to the count visualization.
  {% endstep %}
  {% endstepper %}

Once you are done configuring the widget:

* Click **Add to dashboard** at the bottom of the modal.
* Click **Save changes** at the top of the dashboard page, if you are done editing.

### Adding a section

Sections help you organize and group your widgets on a dashboard.

To create a section:

* Enter the edit mode and click **Add section** to open a modal.
* Enter the section name and description in the modal.
* Click **Create section** to add it to the dashboard.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-a761bfc892d79886970aa8a6f510cda78089360f%2Fdashboards-adding-section.png?alt=media" alt="Options for a section element"><figcaption></figcaption></figure>

1. Once the section appears on a dashboard, you can move it by clicking the handle located in the upper-left corner and dragging it to another location.
2. Click **Add widget** to add a new widget directly from within the section.
3. Click the action menu located in the upper right corner of the section to edit or delete the section.
4. **Collapse** or **Expand** the section to change its visibility. This feature works even after you save the changes and exit edit mode.
5. Click **Save changes** at the top of the page when you are done.

### Metrics

The following table shows a list of metrics and associated visualizations.

| Metrics                                  | Visualization                             | Additional information                                                                                                           |
| ---------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **Issues**                               |                                           |                                                                                                                                  |
| Issue count                              | Count, line chart, donut chart, pie chart | See [#issues](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#issues "mention")                   |
| **Security**                             |                                           |                                                                                                                                  |
| Security remediation effort              | Count, line chart                         | See [#security](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#security "mention")               |
| Security hotspots                        | Count, line chart                         | See [#security-review](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#security-review "mention") |
| Security hotspots reviewed               | Count, line chart                         | See [#security-review](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#security-review "mention") |
| Security hotspot count                   | Donut chart, pie chart                    | See [#security-review](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#security-review "mention") |
| Security rating                          | Rating badge                              | See [#security](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#security "mention")               |
| Security review rating                   | Rating badge                              | See [#security-review](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#security-review "mention") |
| **Reliability**                          |                                           |                                                                                                                                  |
| Reliability remediation effort           | Count, line chart                         | See [#reliability](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#reliability "mention")         |
| Reliability rating                       | Rating badge                              | See [#reliability](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#reliability "mention")         |
| **Maintainability**                      |                                           |                                                                                                                                  |
| Effort to reach maintainability rating A | Count, line chart                         | See [#maintainability](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#maintainability "mention") |
| Technical debt ratio                     | Count, line chart                         | See [#maintainability](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#maintainability "mention") |
| Technical dept ratio of new/changed code | Count, line chart                         | See [#maintainability](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#maintainability "mention") |
| Maintainability rating                   | Rating badge                              | See [#maintainability](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#maintainability "mention") |
| **Coverage**                             |                                           |                                                                                                                                  |
| Conditions to cover                      | Count, line chart                         | See [#coverage](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#coverage "mention")               |
| Coverage by tests                        | Count, line chart                         | See [#coverage](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#coverage "mention")               |
| Line coverage                            | Count, line chart                         | See [#coverage](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#coverage "mention")               |
| Lines to cover                           | Count, line chart                         | See [#coverage](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#coverage "mention")               |
| Uncovered conditions                     | Count, line chart                         | See [#coverage](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#coverage "mention")               |
| Uncovered lines                          | Count, line chart                         | See [#coverage](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#coverage "mention")               |
| **Duplications**                         |                                           |                                                                                                                                  |
| Duplicated blocks                        | Count, line chart                         | See [#duplications](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#duplications "mention")       |
| Duplicated files                         | Count, line chart                         | See [#duplications](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#duplications "mention")       |
| Duplicated lines                         | Count, line chart                         | See [#duplications](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#duplications "mention")       |
| Duplicated lines density                 | Count, line chart                         | See [#duplications](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#duplications "mention")       |
| **Size**                                 |                                           |                                                                                                                                  |
| Comment lines                            | Count, line chart                         | See [#size](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#size "mention")                       |
| Comment lines density                    | Count, line chart                         | See [#size](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#size "mention")                       |
| Lines                                    | Count, line chart                         | See [#size](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#size "mention")                       |
| Line count                               | Donut chart, pie chart                    | See [#size](https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/metric-definitions#size "mention")                       |

### Related pages

* [](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/dashboards "mention")
* [viewing-and-managing-dashboards](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/dashboards/viewing-and-managing-dashboards "mention")
