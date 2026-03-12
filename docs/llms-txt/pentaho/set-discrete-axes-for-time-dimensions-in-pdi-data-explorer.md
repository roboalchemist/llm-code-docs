# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/customize-pdi-data-explorer/use-discrete-axis-for-line-area-and-scatter-charts/set-discrete-axes-for-time-dimensions-in-pdi-data-explorer.md

# Set discrete axes for time dimensions in PDI Data Explorer

To display Time dimensions in the line and area visualizations on a discrete axis, perform the following steps:

1. Navigate to the `pentaho/design-tools/data-integration/system/karaf/config/web-client` system directory and open the `config.js` file with any text editor.
2. Locate the `Example Rule 9 - Disable the continuous date strategy` code block, as shown in this example:

   ```javascript
   // Example Rule 9 - Disable the continuous date strategy, to revert
   // to the old behavior (Before 8.1) that represents Time dimensions in a discrete axis.
   /*
   {
     select: { module: "pentaho/visual/role/adaptation/EntityWithTimeIntervalKeyStrategy" },
     apply: { isBrowsable: false }
   },
   */
   ```
3. Remove the `/*` marker and the `*/` marker to uncomment the `EntityWithTimeIntervalKeyStrategy` command.
4. Save and close the file, then refresh the browser.

Your line and area visualizations will display Time dimensions on a discrete axis and the scatter visualization will not be able to provide Time dimensions.
