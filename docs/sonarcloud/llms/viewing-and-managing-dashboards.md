# Source: https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/dashboards/viewing-and-managing-dashboards.md

# Viewing and managing dashboards

This feature is available in the [Enterprise](https://www.sonarsource.com/plans-and-pricing/sonarcloud/) plan.

### Retrieving dashboards

To retrieve **Dashboards**:

{% embed url="<https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2F9z9yxU5Dgsdone9Mi1rt%2Fretrieve-dashboards-no-sound.mp4?alt=media&token=f7228fb6-efbe-4d29-a594-c911ba28528d>" %}

1. Retrieve your project. See [retrieving-projects](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/retrieving-projects "mention") for more information.
2. Select the **Main Branch** from the left side menu.
3. Click **Dashboards** in the top menu. The drop-down menu provides shortcuts to the **Project health dashboard**, a built-in dashboard, and **All dashboards** page which includes your custom dashboards.

### Permissions

Private project:

* Browse permission is required to view, create and edit project dashboards.

Public projects:

* Anyone can view project dashboards, including any custom dashboards.
* Members of the organization that the project belongs to can edit and create project dashboards.

### A list of all dashboards

The **All dashboards** page shows a list of dashboards for your project.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fq95sMHF6rzNvygPOhyhY%2Fdashboards-all.png?alt=media&#x26;token=f12a6452-ebfd-4491-b637-8fdcfba5c776" alt="All dashboards page"><figcaption></figcaption></figure>

1. Click on **All**, **Built-in** or **Custom** buttons to filter the dashboard or use the search to find a dashboard by name.
2. Click **Create custom dashboards** to create a new dashboard. See [creating-dashboards](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/dashboards/creating-dashboards "mention") for more details.
3. The list is organized by **Dashboard name**, **Last edited**, and **Creator**.
4. The action menu at the end of each row shows:
   * **Edit name and description**: Available to custom dashboards.
   * **Edit**: Available to custom dashboards.
   * **Duplicate**: Available to custom and built-in dashboards.
   * **Delete dashboard**: Available to custom dashboards.

### Viewing dashboards

Dashboards comprise configurable widgets. Depending on the type of a measure they represent, the widgets are count, rating badge, line chart, pie and donut charts.

#### Count

Count represents a single metric. It displays a numerical value for a measure, for example, the number of security hotspots or the percentage of debt ratio.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-4bdbff0267ef97cf8b5c0d3f829f0d2809ce5ca4%2Fdashboards-count.png?alt=media" alt="The count widget" width="563"><figcaption></figcaption></figure></div>

* In the upper-right corner, the chart shows whether the data is applied to new or overall code.
* If enabled during widget creation, the widget displays the net change in the last 30 days. Click on it to investigate further on the Activity page.

#### Rating badge

A rating represents a single metric. It displays the current rating for a measure, for example, a security rating or reliability rating.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-822616d007b094308fa4a6b593c5866c2e39d9b6%2Fdashboards-rating%20(1).png?alt=media" alt="The rating widget" width="341"><figcaption></figcaption></figure></div>

In the upper-right corner, the chart shows whether the data is applied to new or overall code.

#### Line chart

A line chart represents metrics that change over time, displaying historical data for a selected measure.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-e3e2b77d102fc6f8de7d2d4b7f2fa07979d85428%2Fdashboards-line-chart%20(1).png?alt=media" alt="The line chart widget" width="563"><figcaption></figcaption></figure></div>

* Hover over the line to reveal a tooltip with additional information.
* In the upper-right corner, the chart shows that data is applied to overall code, which is the only option for line charts.
* If enabled during widget creation, the chart displays a legend.

#### Pie and donut charts

Pie and donut charts display information for multiple metrics.

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-1fd1335203f4d92a226bea60e48a64353bd704e7%2Fdashboards-pie-chart%20(2).png?alt=media" alt="The pie chart widget" width="563"><figcaption></figcaption></figure></div>

<div align="left"><figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-fae0557f4c4c395e86fde730de36d2ebd1113900%2Fdashboards-donut-chart%20(2).png?alt=media" alt="The donut chart widget" width="563"><figcaption></figcaption></figure></div>

* Hover over a section of the pie or donut chart to reveal a tooltip with more information.
* Click on the pie or donut chart sections, or on the legend, to drill down into the metrics.
* In the upper-right corner, the chart shows whether the data is applied to new or overall code.
* If enabled during widget creation, the chart displays a legend.

See [#metrics](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/creating-dashboards#metrics "mention") for more information about metrics and associated visualizations.

#### Missing a visualization or metric?

Your feedback is important to us. Submit your ideas for a visualization or metric that you would like to see in Dashboards through our [Portal card](https://portal.productboard.com/sonarsource/1-sonarqube-cloud/c/802-dashboards-improvements).

### Editing a dashboard

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-279bf514e7ddc0e5aba6d6fb14172504e7e93819%2Fdashboards-edit.png?alt=media" alt="Editing a dashboard"><figcaption></figcaption></figure>

Navigate to the dashboard you wish to edit and select **Edit** from the action menu located in the upper-right corner of the page. Alternatively, you can navigate to the **All dashboards** page and select **Edit** from the action menu located on the right-side of the dashboard you wish to edit.

In the edit mode you have an option to:

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-b8abaa9ec8f9ddc2c67054e413ab4d99dc6e4fbc%2Fdashboards-edit-options%20(1).png?alt=media" alt="Editing options"><figcaption></figcaption></figure>

* **Cancel and exit**: Exits the edit mode without saving the changes.
* **Save changes**: Saves the existing changes.
* **Add widget**: You can choose from available widgets.
* **Add section:** Sections group a set of widgets together and are collapsible.

See [creating-dashboards](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/dashboards/creating-dashboards "mention") for more details about how to create and customize the widgets and sections.

#### Organizing your dashboards

**Widgets**

You can organize widgets by moving them from one section to another. In edit mode, click the handle located in the top-left corner of a widget and drag it to another location.

<figure><img src="https://2223713658-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FB4UT2GNiZKjtxFtcFAL7%2Fuploads%2Fgit-blob-2a822ae1852776dbbc990eade67b584e1ad5cf1b%2Fdashboards-moving-widgets.png?alt=media" alt="Moving a widget"><figcaption></figcaption></figure>

Additionally, you can resize a widget by clicking and dragging its lower-right corner.

**Sections**

Similarly to widgets, you can drag sections from one location of the dashboard to another.

Sections are collapsible, even after you save the changes and exit the edit mode. This can help you save screen real estate and show only information that is important to you at a given moment.

### Related pages

* [](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/dashboards "mention")
* [creating-dashboards](https://docs.sonarsource.com/sonarqube-cloud/managing-your-projects/dashboards/creating-dashboards "mention")
