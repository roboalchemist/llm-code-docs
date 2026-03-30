# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/advanced-topics/defining-hyperlinks-cp/create-hyperlinks-to-a-report-in-the-pentaho-repository.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/advanced-topics/defining-hyperlinks-cp/create-hyperlinks-to-a-report-in-the-pentaho-repository.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/advanced-topics/defining-hyperlinks-cp/create-hyperlinks-to-a-report-in-the-pentaho-repository.md

# Create hyperlinks to a report in the Pentaho Repository

Perform the following steps to create hyperlinks in reports:

1. Create an Analyzer report or open an existing one.
2. Right-click a row or column level and select **Hyperlink**.

   The Link on dialog box appears.
3. Click **Enable Link** to activate the hyperlink feature.

   You can disable linking by clearing the **Enable Link**check box.
4. In the **Link To** drop-down menu, select **Pentaho Repository File**.
5. Click **Browse** to locate a report, chart, or dashboard in the Pentaho Repository and click **Open**.
   1. If the destination report has parameters, they automatically appear in the **Destination Parameter** list on the left. Map parameters in the row or column levels to parameters in the destination report by selecting the check box for each parameter you want to use to constrain the resulting data. Enter the related names of the row or column levels within curly brackets.
   2. If the destination report does not have parameters, the **Destination Parameter** list does not appear. Go to the next step.
6. Specify how hyperlink content displays by clicking the **Open in** drop-down menu and selecting **New Tab**, **New Window**, or **Current Window**.
7. Enter a **Tool Tip** to be displayed when you hover over hyperlinks and click **OK**. Hyperlinks appear in the Analyzer report.
8. Click the links to ensure the content associated with them appears correctly and save the report.
