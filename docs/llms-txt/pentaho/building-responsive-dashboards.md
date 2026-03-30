# Source: https://docs.pentaho.com/pba-ctools/cde-advanced-solutions/building-responsive-dashboards.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-advanced-solutions/building-responsive-dashboards.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions/building-responsive-dashboards.md

# Building responsive dashboards

CTools includes Bootstrap’s responsive library, so you can develop dashboards which work across a range of different devices, such as laptops, tablets, and smart phones. In this walk-through tutorial, you will convert the **demoDashboard** you created in the [Create a dashboard using RequireJS](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/CTools/CDE%20advanced%20solutions/CDE%20advanced%20solutions/Create%20a%20dashboard%20using%20RequireJS=GUID-2EF401C9-C356-43A3-B041-9546712FB647=1=en=.md) or [Exporting charts](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions/exporting-charts) tutorials to a responsive dashboard.

These instructions assume that you are familiar with the [main features in CDE](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/CTools/CDE%20dashboard%20overview/CDE%20dashboard%20overview=GUID-45B6F4DA-C45F-482D-AA7A-99BE0016F616=4=en=.md) and the basic steps of [creating a dashboard in CDE](https://github.com/pentaho/documentation/blob/main/PDIA/10.2/CTools/CDE%20quick%20start%20guide/CDE%20quick%20start%20guide=GUID-4DBA97DB-6E34-4E20-8815-6332FB0D8626=3=en=.md). In addition, these instructions assume that you have [activated the CDE plugin](https://docs.pentaho.com/pba-ctools/10.2-ctools/activate-cde).

1. Open the **demoDashboard** in CDE.

   For detailed instructions, see Step 1 in [Exporting Charts with CGG](https://docs.pentaho.com/pba-ctools/10.2-ctools/exporting-charts#exporting-charts-with-cgg).
2. In the Layout perspective, locate and expand the **chartTableRow** row.

   1. Select the **tableObj** column and in the **Properties** pane, set the **Medium Devices** property to `6` spans. Additionally, set the**Extra Small Devices** property to `12` spans.
   2. Select the **chartObj** column and in the **Properties** pane, set the **Medium Devices** property to `6` spans. Additionally, set the**Extra Small Devices** property to `12` spans.

   ![](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-facce98f6a73921c71f2b31a0fe018814684f706%2FResponsive_Bootstrap_Properties.png?alt=media)

   **Note:** The **Small Devices** property will inherit its value from the **Extra Small Devices** property, and the **Large Devices** property will inherit its value from the **Medium Devices** property. For more information about how Bootstrap works in CDE, see the [CDE Dashboard Overview](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-dashboard-overview).
3. Save the **demoDashboard**.
4. In Pentaho User Console, navigate to the Browse Files perspective and double-click the `demoDashboard` file. When rendered, the dashboard will look similar to the following:

   ![Resulting example dashboard](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-69468762baf78b4f0f1986d56b997305988eaad3%2FExportCharts_ChartPreview.png?alt=media)
5. To test the responsiveness of your dashboard, reduce the size of your browser window. The dashboard layout will respond accordingly:

   ![Example dashboard responding accordingly](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-6b1720f34da0f8f3d82a11683ee51119ead5a60d%2FResponsive_Dashboard.png?alt=media)
