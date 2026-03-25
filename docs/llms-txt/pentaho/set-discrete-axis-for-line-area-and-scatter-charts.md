# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-pentaho-analyzer/set-discrete-axis-for-line-area-and-scatter-charts.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-pentaho-analyzer/set-discrete-axis-for-line-area-and-scatter-charts.md

# Set discrete axis for line, area, and scatter charts

Line, Area, and Scatter charts in Analyzer and custom charts in VizAPI 3.0 provide Time and Number dimensions and associated hierarchic members on a continuous scale axis. However, if you prefer the Time and Number dimensions in Line and Area visualizations on a discrete axis, and to disable the Time and Number dimensions in Scatter visualizations, perform either or both of the following procedures to edit the global mapping configurations:

## Set time dimensions to discrete axes in Analyzer

1. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system/karaf/config/web-client` system directory and open the `config.js` file with any text editor.
2. Locate the `Example Rule 9 - Disable hierarchical dates strategy` code block, as shown in this example:

   ```
   // Example Rule 9 - Disable the continuous date strategy, to revert
   // to the old behavior (Before 8.1) that represents Time dimensions in a discrete axis.
   /*
   {
     select: { module: "pentaho/visual/role/adaptation/EntityWithTimeIntervalKeyStrategy" },
     apply: { isBrowsable: false }
   },
   */ 
   ```
3. Remove the `/*` marker and the `*/` marker to uncomment the`EntityWithTimeIntervalKeyStrategy` command.
4. Save and close the file, then refresh the browser.

Your line and area visualizations will display Time dimensions on a discrete axis and the scatter visualization will not be able to provide Time dimensions.

## Set number dimensions to discrete axes in Analyzer

1. Navigate to the `pentaho/server/pentaho-server/pentaho-solutions/system/karaf/config/web-client` system directory and open the `config.js` file with any text editor.
2. Locate the `Example Rule 10 - Disable the continuous number strategy` code block, as shown in this example:

   ```
   // Example Rule 10 - Disable the continuous number strategy, to revert
   // to the old behavior (Before 8.2) that represents Number dimensions in a discrete axis.
   /*
   {
     select: { module: "pentaho/visual/role/adaptation/EntityWithNumberKeyStrategy" },
     apply: { isBrowsable: false }
   },
   */
   ```
3. Remove the `/*` marker and the `*/` marker to uncomment the `EntityWithNumberKeyStrategy` command.
4. Save and close the file, then refresh the browser.

Your line and area visualizations will display Number dimensions on a discrete axis and the scatter visualization will not be able to provide Number dimensions.
