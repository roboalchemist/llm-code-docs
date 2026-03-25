# Source: https://docs.pentaho.com/pba-ctools/cde-advanced-solutions/exporting-charts.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-advanced-solutions/exporting-charts.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions/exporting-charts.md

# Exporting charts

In this tutorial, you will learn how to export charts. These instructions assume that you are familiar with the [main features in CDE](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/CTools/CDE%20dashboard%20overview/CDE%20dashboard%20overview=GUID-45B6F4DA-C45F-482D-AA7A-99BE0016F616=4=en=.md) and the basic steps of [creating a dashboard in CDE](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/CTools/CDE%20dashboard%20overview/CDE%20dashboard%20overview=GUID-45B6F4DA-C45F-482D-AA7A-99BE0016F616=4=en=.md). In addition, these instructions assume that you have [activated the CDE plugin](https://docs.pentaho.com/pba-ctools/10.2-ctools/activate-cde).

## Exporting charts with CGG

In this walk-through tutorial, you will export the bar chart with the Community Graphics Generator (CGG) using the demoDashboard CDE dashboard created in the [Create a dashboard using RequireJS](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions/create-a-dashboard-using-requirejs) tutorial. To use CGG, open an existing CDE dashboard for editing, and select which charts in the dashboard you want to render as CGG charts.

1. Open the **demoDashboard** in CDE.
   1. Log on to Pentaho User Console and navigate to the Browse Files perspective.
   2. In the **Folders** pane, click to expand the `Public` folder, and then click to highlight the `demoDashboard` folder.

      ![demoDashboard example in the Browse Files perspective](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-3e1f11e7aba287b5d0d190a9fb03d70e053b4167%2FEXP_PUC_BrowseFiles_DemoDashboard.png?alt=media)
   3. In the **Files** pane, click on **demoDashboard** and then, in the**File Actions** pane, click **Edit**.

      You are now in the Opened perspective with CDE in editing mode. The **Editing:demoDashboard** tab is now active in CDE.
2. In the Components perspective, press Shift G. In the Choose what charts to render as CGG popup, click to select the **chartComponent** check box.

   This popup lists all the components available to CGG, such as the Community Charting Components (CCC) chart components. When you save the dashboard, CGG generates a JavaScript file for each chart selected in the popup and saves it in your solutions directory.

   ![chartComponent option in the Choose what charts to render as CGG popup](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-ffe383c934c294f013409e7091c7be4143988b7c%2FEXP_CGG_Popup.png?alt=media)
3. Click the **Url** button to generate a URL link to CGG which will export the target chart image. Copy the export link by selecting the full URL text and pressing CtrlC on your keyboard. When finished, click **Close**.

   ![Url option in the Choose what charts to render as CGG popup](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-2d6cd9021dd8aaece0dac809c8be729553b18f53%2FExportChartswithCGG_URL.png?alt=media)
4. Before we can use the export URL, we need to save the dashboard so the CGG scripts are generated and saved in the proper repository. To save the dashboard, on the CDE menu bar, click **Save**.
5. View the generated CGG JavaScript files. In Pentaho User Console, navigate to your `demoDashboard` folder. Note the following files:
   * The `demoDashboard_chartComponent.js` contains the chart definitions.
   * The `chartComponent.js` contains the same content as the above file. This file is saved for backwards compatibility with previous server versions.![dempDashboard\_chartComponent.js selection](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-7d55b3b3af70bbda1c1f9add8f1e419b4b5504db%2FEXP_demodashboard_files.png?alt=media)
6. Open a browser window and paste the export URL (from Step 3) into the browser's navigation bar. Press Enter. The chart image displays in the browser window.

   ![Displayed chart image](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-ca9f2c19dcb77a97028af2553050a09590f6da56%2FEXP_Chart_Two.png?alt=media)

By default, CGG exports images in the Portable Network Graphics format (PNG). If you want CGG to export the image in the Scalable Vector Graphics format (SVG), then change the `outputType` in the URL query string to `svg` as shown below.

```
http://localhost:8080/pentaho/plugin/cgg/api/services/draw?script=/public/demoDashboard/demoDashboard_chartComponent.js&outputType=svg
```

## Exporting charts from a dashboard

In this walk-through tutorial, you will add an **Export Chart** button to export the bar chart from the demoDashboard CDE dashboard created in the [Create a dashboard using RequireJS](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions/create-a-dashboard-using-requirejs) tutorial.

1. Open the **demoDashboard** in CDE.

   (For detailed instructions, see Step 1 in [Exporting Charts with CGG](#exporting-charts-with-cgg).)
2. Customize the layout for the export button.
   1. In the Layout perspective, locate the **mainContainerColumn** column and add a row named `exportChartRow`.
   2. Select the **exportChartRow** and add a column named `exportChartObj`.
   3. Select the **exportChartObj** column and in the **Properties** pane, locate the **Text Align** property and set its value to **Center**.

      ![Text Align property in Layout Structure perspective](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-019bcde2d7fa586a38fdf48738632243d9fbd94d%2FEXP_CDE_Layout_expChartObj.png?alt=media)
3. Add and customize the export button.
   1. In the Components perspective, in the left menu, expand the **Others** group and click on the **Button Component**.

      ![Button Component in Components prespective](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-52527e74df6e40ad89e59432d15584d1f047fd4f%2FExportCharts_ButtonComp.png?alt=media)
   2. In the **Components** pane, select the **Button Component** you just added. In the **Properties** pane, set the following values:

| **Property**   | **Value**        |
| -------------- | ---------------- |
| **Name**       | `exportChart`    |
| **Label**      | `Export Chart`   |
| **HtmlObject** | `exportChartObj` |

4\. Copy the following code to the \*\*Expression\*\* property:

````
```javascript
function f() {
  this.dashboard
      .getComponentByName('render_chartComponent')
      .exportChart('png');
}
```

**Note:** This code allows you to retrieve the `chartComponent` component via the dashboard and execute its `exportChart` function by passing it the **png** parameter which defines the export file type as a PNG file.

When completed, the **Properties** pane should look similar to the image below.

![Resulting properties in example Properties pane](EXP_CDE_Component_ButtonProperties.png)
````

5\. In the Components perspective, press Shift G to display the Choose what charts to render as CGG popup. Make sure the **chartComponent** check box is selected, then click **Close**.

```
![chartComponent option in the Choose what charts to reneder as CGG popup](EXP_CGG_Popup.png)
```

6\. After saving the dashboard, return to Pentaho User Console, navigate to the **Browse Files** perspective and double-click the `demoDashboard` file. The following chart displays:

```
![Resulting demoDashboard display](../ExportCharts_ChartPreview.png)
```

7\. Press the **Export Chart** button to download the chart file as a PNG file.

```
![Example exported chart](EXP_Chart_Two.png)
```
