# Source: https://docs.pentaho.com/pba-ctools/cde-advanced-solutions/create-a-dashboard-using-requirejs.md

# Source: https://docs.pentaho.com/pba-ctools/9.3-ctools/cde-advanced-solutions/create-a-dashboard-using-requirejs.md

# Source: https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-advanced-solutions/create-a-dashboard-using-requirejs.md

# Create a dashboard using RequireJS

In this walk-through tutorial, you will create a CTools dashboard using RequireJS. These instructions assume that you are familiar with the main features in CDE and the basic steps of creating a dashboard in CDE. In addition, these instructions assume that you have activated the CDE plugin.

The process is broken down into six basic steps.

* [Step 1: Set up folders in User Console and create the dashboard](#step-1-set-up-folders-in-user-console-and-create-the-dashboard)
* [Step 2: Add layout](#step-2-add-layout)
* [Step 3: Add external resources](#step-3-add-external-resources)
* [Step 4: Add data sources](#step-4-add-data-sources)
* [Step 5: Add components](#step-5-add-components)
* [Step 6: Preview the dashboard](#step-6-preview-the-dashboard)

## Step 1: Set up folders in User Console and create the dashboard

* Log on to the User Console and navigate to the Browse Files perspective.
* In the **Folders** pane, click on the **Public** folder and then, in the**Folder Actions** pane, click **New Folder**. Create a solutions folder called `demoDashboard`.
* Expand the **Public** folder and click on the newly created **demoDashboard** folder. In the **Folder Actions** pane, click **New Folder** and create a subfolder titled `files` which will contain the JavaScript and Cascading Style Sheets (CSS) files used in this dashboard.
* [Open CDE](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide) and create a new dashboard titled `demoDashboard`, and save it in the **public** > **demoDashboard** folder you just created.
* From the CDE menu bar, click **Settings**, and then select the **RequireJS Support** check box to convert the dashboard to a RequireJS dashboard.

  ![Settings dialog box highlighting RequireJS support](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-b4c09a3fc932b47bac5f77a62f51f8f5395760e3%2FCDE_Settings_RequireJSSupport_checkbox.png?alt=media)
* Click **Ok**.

  A message box appears warning you about possible issues with your custom JavaScript code in your dashboard. Click **Ok** to proceed. The dashboard is now saved as a RequireJS dashboard.

## Step 2: Add layout

* From the **Layout Structure** menu bar, click the **Add Bootstrap Panel** button.

  ![Add Bootstrap Panel in Layout Structure menu bar](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-6843ed542efe8ea15443e2069bbcda623bf46b94%2FBootStrapButton.png?alt=media)
* Configure your bootstrap panel to match the settings in the image below. Be sure to add and rename all displayed rows and columns.

  ![Bootstrap panel](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-dab8355cee19e3e7698243d31b23efb074603db5%2FLayoutStructure-BootstrapElements.png?alt=media)
* In the **Properties** pane, all columns by default set the **Extra Small Devices** property to `12` spans. Change the **Value** for the following columns:

  * Set **tableObj** and **chartObj** to `6` spans.\
    See [CDE dashboard overview](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-dashboard-overview) for more information on Bootstrap in CDE.

  ![Extra Small Devices property in Properties pane](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-d47848b5b628e938b0214af4a38b71dbe1d01a72%2FFigure39_BootstrapPropPanel.png?alt=media)
* Center the title and subtitle in the **Properties** pane.

  For both **titleColumnObj** and **subTitleColumnObj**, locate the **Text Align** property and click in the **Value** column. On the keyboard, press the down arrow to display a drop-down menu and select `Center`.

  ![](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-80c24ce86d07a1217d5b33df01c1c2aba67ac2e2%2FCDE_CreateDash_Step2-Point4.png?alt=media)

## Step 3: Add external resources

* In the **CDE Layout** perspective, on the **Layout Structure** toolbar, click the **Add Resource** icon.

  ![Add Resource in Layout Structure menu bar](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-7e09e040c48cb3b159b971b6735bdfb7903bff3a%2FLayoutStructureMenubar_AddResource.png?alt=media)
* In the Add Resource dialog box, enter the following data:
  * For **Resource Type**, select **Javascript**.
  * For **Resource Source**, select **External File**. Click **Ok**.![Add Resource dialog box](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-74dbeeecc4e35f89b4e0002b0f8164def5988dd0%2FAddResourceDB.png?alt=media)
* In the **Properties** pane, click in the **Value** column to the right of the **Name** property and enter `addins`. Press Tab or Enter.

  ![Name in Properties pane](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-fd21dfb089159018b2d0b190c563d9aca8ee7fc8%2FAddResource_PropertiesPanel_Addins.png?alt=media)
* Click the caret ('**^**') button to the right of the **Resource file** property and navigate to **public** > **demoDashboard** > **files**. Click **Ok**.
* In the Create File dialog box, enter `addins` and click **Ok**.

  You have now created the `addins.js` file, which will contain the JavaScript code to execute within the dashboard components. Note that the name you give to the JS file is how the file itself will be referenced within the dashboard.
* To enter content in the `addins.js` file, select the **addins** resource in the **Layout Structure** pane. Locate the **Resource file** property and click the ellipse ('**...**') button to open the Edit window. Enter the following content for this file:

  ```javascript
  define([
    "cdf/AddIn",
    "cdf/Dashboard.Clean",
    "cdf/Logger",
    "cdf/lib/jquery"
  ], function(AddIn, Dashboard, Logger, $) {
    Dashboard.registerGlobalAddIn("Table", "colType", new AddIn({
      name: "customArrow",
      label: "customArrow",
      defaults: {},
      implementation: function(tgt, st, opt) {
        if(typeof st.value !== "number") {
          Logger.warn("customArrow add-in invalid value: " + st.value);
          return;
        }
        var trend = st.value > 0 ? "up" : "down";
        $(tgt).empty()
              .append($('<ul><span class="glyphicon glyphicon-arrow-'
                + trend +'"></span>&nbsp<span>'+ st.value +'%'+'</span></ul>'));
      }
    }));
  });
  ```

  * Lines 2 to 5 specify the dependencies needed for the add-in, which are then registered for use in the function.
  * Line 7 registers the add-in, which is then available to the table component.
* Press the **Save** button and then press the **Close** button.
* Following steps 2 through 5, add a second JavaScript external resource named `title` and save a new file named `title.js` in the **public** > **demoDashboard** > **files** folder. The dashboard will have a title and a subtitle which are provided by the text components created in Step Five. These components will fetch the displayed value from an object returned by the AMD module defined in the `title.js` file.
* To enter content in the `title.js` file, in the **Layout Structure** pane select the title resource and then select the **Resource file** property. Click the ellipse ('**...**') button to open the Edit window. Enter the following content for this file:

  ```javascript
  define(function() {
    return {
      option1: 'CDE Dashboard',
      option2: 'Using a Table with a custom add-in and a CCC Bar Chart',
    };
  });
  ```

  In this file, an AMD module is defined which returns an object with two properties. This object will be accessible to the text components, using the same name as the one used for the **Name** property of the JavaScript external resource, and its properties will be used as the title and subtitle.
* Press the **Save** button and then press the **Close** button.

## Step 4: Add data sources

In this example, you will use scripted queries as the data source.

1. In the Data Source perspective, from the **Data Source** list, click **SCRIPTING Queries**, and then click **scriptable over scripting** twice.
2. In the **Datasources** panel, in the **Name** column, enter `chartQuery` for the first data source, and `tableQuery` for the second.

   ![Datasources panel](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-dfafbaf788559f1cdfd11f5bd875ebd29ce12423%2FDatasources_Group_Queries.png?alt=media)
3. Add the following script to the **Query** property for the **chartQuery** data source:

   ```java
   import org.pentaho.reporting.engine.classic.core.util.TypedTableModel;
   String[] columnNames = new String[]{
     "Country", "Population growth per City [%]"
   };
   Class[] columnTypes = new Class[]{
     String.class, Float.class
   };
   TypedTableModel model = new TypedTableModel(columnNames, columnTypes);
   model.addRow(new Object[]{
     new String("Tokyo"), new Float("60")
   });
   model.addRow(new Object[]{
     new String("Nice"), new Float("20")
   });
   model.addRow(new Object[]{
     new String("London"), new Float("-10")
   });
   model.addRow(new Object[]{
     new String("Munich"), new Float("30")
   });
   model.addRow(new Object[]{
     new String("Porto"), new Float("10")
   });
   model.addRow(new Object[]{
     new String("Brasilia"), new Float("10")
   });

   return model;
   ```
4. Add the following script to the **Query** property for the **tableQuery** data source:

   ```java
   import org.pentaho.reporting.engine.classic.core.util.TypedTableModel;
   String[] columnNames = new String[]{
     "Country", "City", "Population growth per City"
   };
   Class[] columnTypes = new Class[]{
     String.class, String.class, Float.class
   };
   TypedTableModel model = new TypedTableModel(columnNames, columnTypes);
   model.addRow(new Object[]{
     new String("Japan"), new String("Tokyo"), new Float("60")
   });
   model.addRow(new Object[]{
     new String("France"), new String("Nice"), new Float("20")
   });
   model.addRow(new Object[]{
     new String("UK"), new String("London"), new Float("-10")
   });
   model.addRow(new Object[]{
     new String("Germany"), new String("Munich"), new Float("30")
   });
   model.addRow(new Object[]{
     new String("Portugal"), new String("Porto"), new Float("10")
   });
   model.addRow(new Object[]{
     new String("Brazil"), new String("Brasilia"), new Float("10")
   });

   return model;
   ```

## Step 5: Add components

* Switch to the Components perspective.
* From the **Components** list, expand the appropriate **Group** section, and then add the following components to the dashboard with the specified **Name** and **HtmlObject** properties in the table below. (See [Customize the Components Perspective](https://docs.pentaho.com/pba-ctools/10.2-ctools/cde-quick-start-guide) for more detailed instruction.)

  | Group  | Component       | Name              | HtmlObject        |
  | ------ | --------------- | ----------------- | ----------------- |
  | Others | Text Component  | subTitleComponent | subTitleColumnObj |
  | Others | Text Component  | titleComponent    | titleColumnObj    |
  | Others | table Component | tableComponent    | tableObj          |
  | Charts | CCC Bar Chart   | chartComponent    | chartObj          |

  ![Components perspective](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-4b340f8e37b289ea1258db74ab12cfc499427fd0%2FFigure_43_Components.png?alt=media)
* Set the width and height for the **chartComponent** bar chart.
  * Click in the **Value** column for the **Height** property and type `450`. Press Tab or Enter.
  * Click in the **Value** column for the **Width** property and type `400`. Press Tab or Enter.
* Set the **titleComponent** text component by adding the following code to the **Expression** property:

  ```java
  function f() {
    return "<strong>" + title.option1 + "</strong>";
  }
  ```

  This piece of code is returning the content of **option1** defined in the `title.js` file in [Step Three](#step-3-add-external-resources).
* Set the **subTitleComponent** text component by adding the following code to the **Expression** property. Note that this code is similar to the previous step, substituting `option2` for `option1`:

  ```java
  function f() {
    return title.option2;
  }
  ```
* In the **tableComponent** component, set the **Column Types** property as follows:

  ![Column Types dialog box](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-1e8ef15553fe5b4b5ed91e8bb57bad66af81b2dd%2FTableComponent_ColumnTypes.png?alt=media)

  Notice that the third line in the table is using the non-standard **customArrow** add-in. It is now available because it was registered earlier using the `addins.js` JavaScript external resource file.
* Set the **Datasource** property for the **tableComponent** to use the **tableQuery** data source created earlier in [Step Four](#step-4-add-data-sources).
* Set the **Datasource** property for the **chartComponent** to use the **chartQuery** data source created earlier in [Step Four](#step-4-add-data-sources).

## Step 6: Preview the dashboard

* Save your dashboard and click the **Preview your Dashboard** icon in the top-right corner.

  The Preview window displays.
* Inspect your dashboard.

  Your finished dashboard should look similar to the image below.

  ![Preview of example dashboard](https://3599713356-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtirsJUGxXys7JEgE1Uzf%2Fuploads%2Fgit-blob-3a0b939c0d54239e0e6a2be0b89566c55dd3421c%2FCreateDashboard-Preview.png?alt=media)
* When finished, close the Preview window.
