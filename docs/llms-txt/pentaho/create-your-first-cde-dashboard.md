# Source: https://docs.pentaho.com/pba-ctools/cde-quick-start-guide/create-your-first-cde-dashboard.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-quick-start-guide/create-your-first-cde-dashboard.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide/create-your-first-cde-dashboard.md

# Create your first CDE dashboard

In this walk-through tutorial, you will create your first CDE dashboard using the Steel Wheels sample data included in your Pentaho Enterprise edition.

Your goal for this tutorial is to create a simple dashboard with a centered title. The dashboard will include a product selection field and a line chart in a side-by-side layout. This process is broken down into five basic steps.

## Create and save a new dashboard

This task assumes you are in the Pentaho User Console (PUC).

1. [Open CDE.](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide/open-cde-ctools-cde-quick-start)
2. On the CDE menu bar, click **Save**.
3. On the Save as dialog box which displays, navigate to the folder where you want to save your file.

   For this example, navigate to the `myDashboards` folder.
4. In the **File Name** field, enter a descriptive name for your dashboard, such as `myFirstDashboard`.
5. Click the **Dashboard** option.
6. Click **Ok**.

   Your dashboard is now saved.

   ![Saving the myFirstDashboard example dashboard](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-6c615f6e8ee0829a555fd568f65f424e16315686%2FsaveAsPopup.png?alt=media)

## Create the layout for the dashboard

The CDE Layout perspective allows you to design the layout of your dashboard from scratch or using a template. While defining the layout you can apply styles and add HTML elements such as text or images. [Click here](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/layout-perspective) for a tour of the Layout perspective.

**Note:** It is recommended that you use camel case for value names. Also note, you must press Tab or Enter to save values.

In this tutorial, you will use the Layout perspective to create the placeholders for the selector (and its title) and the line chart.

### Add the main row

1. On the **Layout Structure** toolbar, click the **Add Row** icon.
2. Enter a name for the row. In the **Properties** pane, click in the **Value** column for the **Name** property and type `mainRow`. Press Tab or Enter.

### Add the main column

1. On the **Layout Structure** toolbar, click the **Add Column** icon.
2. Enter a name for the column. In the **Properties** pane, click in the **Value** column for the **Name** property and type `mainColumn`. Press Tab or Enter.

### Set the width of the main column

You can assign the width of the column with the properties across multiple devices. You only need to assign the values to one of these types of devices. For example, if you do not need to have a site which fits well in all devices, you can set the values only for the **Extra Small Devices**. That way, all the other devices will inherit the layout which you assign for that category.

1. In the **Properties** pane, locate the **Extra Small Devices** property and click in the **Value** column.
2. In the text box, type `12` and press Tab or Enter. Because of the inclusion of Bootstrap libraries, the columns in a row must occupy 12 spans, which is the total span size for Bootstrap. For more information on Bootstrap in CDE, see [Tour of the CDE](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-dashboard-overview/community-dashboard-editor-cde-perspectives-ctools/dimensions).

### Add rows to the main column

1. In the left pane, select the **mainColumn**.
2. On the **Layout Structure** toolbar, click the **Add Row** icon twice.

   Two rows are added to the column in the **Layout Structure** pane.

### Enter a dashboard title

When adding HTML text to a dashboard, the HTML must be added to a column. In this task, we add a column to the top row so we can add the HTML text for the dashboard title.

1. Select the top row in the **mainColumn**, and then click the **Add Column** icon.

   This column will contain the title for the dashboard.
2. In the **Properties** pane, click in the **Value** column for the **Name** property and type `dashboardTitle`. Press Tab or Enter.
3. To center the title in the column, locate the **Text Align** property and click in the **Value** column. On the keyboard, press the down arrow to display a dropdown menu and select **Center**.
4. Add HTML text for the dashboardTitle. In the **Layout Structure** pane, click to select the **dashboardTitle** column, and then on the **Layout Structure** toolbar, click the **Add Html** icon.
5. On the **Properties** pane, locate the HTML property and click the ellipsis button. An **Edit** window will display. Type the title of the dashboard using HTML tags, such as `<h1>My First Dashboard</h1>`, and then click **Ok**.

### Enter the dashboard content

1. Select the bottom row.

   This row will be used for the content of the dashboard.
2. In the **Properties** pane, click in the **Value** column for the **Name** property and type `dashboardContent`. Press Tab or Enter.
3. Add one column. In the **Layout Structure** pane, click the **Add Column** icon.

   This column will be the container for the selector, including the title of the selector and the selector itself.
4. To set the column width, in the **Properties** pane, locate the **Extra Small Devices** property and click in the **Value** column. Type `4` and press Tab or Enter.
5. Add two rows to nest inside this column. In the **Layout Structure** pane, click the **Add Row** icon twice.
6. Add the selector.

   1. In the **Layout Structure** pane, click to select the bottom row and then click the **Add Column** icon.
   2. In the **Properties** pane for the newly added column, click in the **Value** column for the **Name** property and type `selectorObj`. Press Tab or Enter.

   **Note:** This column will be the placeholder for the selector, so we should remember its name. It will be referred on the **htmlObject** property of the select component which we will add later.
7. Add the title of the selector.
   1. In the **Layout Structure** pane, click to select the row above the **selectorObj**, and then click the **Add Column** icon.
   2. In the **Properties** pane for the newly added column, click in the **Value** column for the **Name** property and type `selectorTitle`. Press Tab or Enter.
   3. In the **Layout Structure** pane, click to select the **selectorTitle** column and then on the **Layout Structure** toolbar, click the **Add Html** icon.
   4. Locate the **HTML** property and click the ellipsis button. An Edit window displays. Type the title of the selector using HTML tags, such as `<b>Select Product</b>`, and then click **Ok**.
8. On the **Layout Structure** pane, click to select the **dashboardContent** row, and add one column by clicking the **Add Column** icon.
9. Name the column. In the **Properties** pane, click in the **Value** column for the **Name** property and type `chartObj`. Press Tab or Enter.
10. To set the column width, click in the **Value** column for the **Extra Small Devices** property and type `8`. Press Tab or Enter.

    **Note:** This column will be the placeholder for the line chart, so we should remember its name.

### Save the dashboard

To save the dashboard, on the **CDE** menu bar, click **Save**.

As a precaution, it is a good practice to save the dashboard regularly. This is how the **Layout Structure** pane should look like after you follow the steps so far:

![The myFirstDashboard example in the Layout Structure pane](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-a24b6a4634b754d528178b024b9292dda77077ed%2FCDE_QuickStart_LayoutPanel.png?alt=media)

## Customize the Data Source perspective

In this example, we will use two MDX queries: one for the dropdown selector and one for the line chart. The same exercise can be done with SQL sources or other options.

### Select a data source

1. To view the Data Sources perspective, on the **CDE Perspectives** toolbar, click the **Data Sources Panel** icon.
2. To add an MDX over mondrianjndi data source, from the **Data Source** list, expand **MDX Queries**, and then click **mdx over mondrianjndi**.

### Customize the data source

1. Name this data source. In the **Properties** pane, click in the **Value** column for the **Name** property and type `selectorQuery`. Press Tab or Enter.
2. Select the JNDI connection. In the **Properties** pane, click in the **Value** column for the **Jndi** property. On the keyboard, press the down arrow to display a drop-down menu and select the **SampleData** connection.
3. Select the **Steel Wheels** schema. In the **Properties** pane, click in the **Value** column for the **Mondrian schema** property. On the keyboard, press the down arrow to display a dropdown menu and select the **SteelWheels** schema.

### Enter an MDX Query

1. Enter the **MDX Query**. In the **Properties** pane, locate the **Query** property and click the ellipsis icon to the right. The MDX Editor window displays. Enter the following **MDX Query** and then click **Ok**.

   ```
   WITH
       MEMBER [Measures].[Product Member Name] AS
   [Product].[Product].CurrentMember.UniqueName
   SELECT
       [Measures].[Product Member Name] ON COLUMNS,
       [Product].[Product].Members ON ROWS
   FROM [SteelWheelsSales]
   ```
2. You will want the selector to display the names of products to the user while using the product's internal name or ID for selecting the corresponding data in the chart. Therefore, you will need to change the order of your columns.
   1. Click in the **Value** column for the **Output Columns** property.
   2. In the new window, click the **Add** button once to add another index field for a total of two index fields.
   3. In the first Index field, type `1`. In the second Index field, type `0` and click **Ok**.

You have created your first **MDX Query**.

### Add a query with parameters

Here, we will add a query with parameters.

1. [Select a Data Source](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide/broken-reference).
2. Name this data source. In the **Properties** pane, click in the **Value** column for the **Name** property and type `chartQuery`. Press Tab or Enter.
3. Complete steps 2 and 3 of the [Customize the Data Source](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide/broken-reference) task.
4. Enter the **MDX Query**. In the **Properties** pane, locate the **Query** property and click the ellipsis icon to the right. The MDX Editor window displays.
5. You will add the following query to the **chartQuery**:

   ```sql
   SELECT
       [Measures].[Sales] ON COLUMNS,
       [Time].[Months].Members ON ROWS
   FROM
       [SteelWheelsSales]
   WHERE ${productParam}
   ```

   You can notice the parameter **productParam** being referred on the `WHERE` clause (identified with the syntax *${parameterName}*).
6. To add this parameter to the data source, click in the **Value** column for the **Parameters** property.
7. In the **Name** column, type `productParam`. In the **Value** column, type `[Product].[Planes].[Autoart Studio Design].[1900s Vintage Bi-Plane]`. Leave the **Type** column defaulted to String. Click **Ok**.
8. [Save your dashboard](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide/broken-reference).

![MDX Query of the data source customize example](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-ec93d8878d19ad1cd01cdfc1298cbfe16af8ef37%2Fdatasources.png?alt=media)

## Customize the Components perspective

Finally, switch to the Components perspective.

To view the Components perspective, on the **CDE Perspectives** toolbar, click the **Components Panel** icon.

### Add a parameter

1. To add a simple parameter, from the **Components** list, expand **Generic**, and then click **Simple Parameter**.
2. For this parameter, use the same name and default value as the chart query parameter in the **Add a Query** with Parameters task. In the **Properties** pane:
3. Name the parameter. In the **Properties** pane, click in the **Value** column for the **Name** property and type `productParam`. Press Tab or Enter.
4. Set the default value. Click in the **Value** column for the **Property** value property and type `[Product].[Planes].[Autoart Studio Design].[1900s Vintage Bi-Plane]`. Press Tab or Enter.

### Add a selector

1. From the **Components** list, expand **Selects**, and then click**Select Component**.
2. Customize the selector in the **Properties** pane.
   1. Name the selector. Click in the **Value** column for the **Name** property and type `productSelector`. Press Tab or Enter.
   2. Select the parameter. Click in the **Value** column for the **Parameter** property. On the keyboard, press the down arrow to display a dropdown menu and select **productParam**, which is the previous parameter you have created.
   3. Set the **Value as id** to **False**. Click in the **Value** column for the **Value as id** property. On the keyboard, press the down arrow to display a dropdown menu and select **False**.
   4. Select the data source. Click in the **Value** column for the **Datasource** property. On the keyboard, press the down arrow to display a dropdown menu and select **selectorQuery**.
   5. Select the HTML object. Click in the **Value** column for the **HtmlObject** property. On the keyboard, press the down arrow to display a dropdown menu and select **selectorObj**, which is the placeholder you created in the **Layout** perspective.

### Add a line chart

1. From the **Components** list, expand **Charts**, and then click **CCC Line Chart**.
2. Name the line chart. In the **Properties** pane, click in the **Value** column for the **Name** property and type `lineChart`. Press Tab or Enter.
3. Specify the parameters to be used on the **lineChartQuery**. In the **Properties** pane, click in the **Value** column for the **Parameters** property.
   1. In the **Arg** field, type `productParam`.
   2. Click in the **Value** field. On the keyboard, press the down arrow key to display a dropdown menu and select **productParam**. The name on the left (**Arg**) is the “CDA/Data source parameter name." The name on the right (**Value**) is the “CDE parameter” which you created in this same section. It is recommended that you use the same name for both sides.
   3. Click **Ok**.
4. Select the data source. Click in the **Value** column for the **Datasource** property. On the keyboard, press the down arrow to display a dropdown menu and select **chartQuery**.
5. Set the width and height for the chart:
   1. Click in the **Value** column for the Width property and type `500`. Press Tab or Enter.
   2. Click in the **Value** column for the **Height** property and type `200`. Press Tab or Enter.
6. Select the HTML object. Click in the **Value** column for the **HtmlObject** property. On the keyboard, press the down arrow to display a dropdown menu and select **chartObj**. This is the placeholder which you have selected before for this component in the Layout perspective.

### Link two components using parameter listening

To make the line chart respond to the changes on the product selector, we need to specify that the chart component listens to the parameter that the **productSelector** controls, which **isproductParam**.

1. Click to select the **lineChart** component.
2. To set the listeners, click in the **Value** column for the **Listeners** property.
3. Click the dropdown arrow and then click to select the **productParam** checkbox.
4. Save the dashboard.

![Linking two components using parameter listening example](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-cb83e59090fc55fe679f3f5c6a893b815b9c66e1%2Fcomponents.png?alt=media)

## Preview the dashboard

While designing your dashboard, it is recommended that you preview your dashboard from time to time to inspect how the layout will look to your users.

1. On the **CDE Perspectives** tool bar, click the **Preview your Dashboard** icon.

   The Preview window displays.
2. Test your dashboard by changing the displayed values in the dropdown selector.
3. Close the Preview window.

![Preview of the results for the myFirstDashboard example](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-2dcef0ee75e71b7d36ee155507a0f521499ec439%2FCDE_QuickStart_DashboardPreview.png?alt=media)

If you followed these instructions, you should now have a functioning dashboard created in CDE.

A lot of styling and customizing work still remains. Keep in mind that each component has a life cycle which has only been briefly addressed when we added the listeners.
