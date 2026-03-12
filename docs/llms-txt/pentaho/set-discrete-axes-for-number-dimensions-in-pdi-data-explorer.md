# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/customize-pdi-data-explorer/use-discrete-axis-for-line-area-and-scatter-charts/set-discrete-axes-for-number-dimensions-in-pdi-data-explorer.md

# Set discrete axes for number dimensions in PDI Data Explorer

To display Number dimensions in the line and area visualizations on a discrete axis, perform the following steps:

1. Navigate to the `pentaho/design-tools/data-integration/system/karaf/config/web-client` system directory and open the `config.js` file with any text editor.
2. Locate the `Example Rule 10 - Disable the continuous number strategy` code block, as shown in this example:

   ```javascript
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
