# Source: https://docs.pentaho.com/pba-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-5-disable-drill-through-links.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-5-disable-drill-through-links.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-5-disable-drill-through-links.md

# Step 5: Disable drill-through links

You can permanently disable drill-through links for all analysis reports by editing the `analyzer.properties` file, or you can disable drill-through links on a cube-by-cube basis. Both methods are described in the steps below.

1. Global Disable: Perform these steps to disable drill-through links for all cubes and analysis data sources.

   1. Open your `analyzer.properties` file with a text editor and find the property called **report.drill.links.disabled**.
   2. Set the value from *false* to *true* as shown here.

      From:

      ```
      report.drill.links.disabled=false
      ```

      To:

      ```
      report.drill.links.disabled=true
      ```

   Drill-through links are now disabled for all cubes and analysis data sources. The option for drill-through links is no longer visible on the Report Options dialog box.
2. Individual Cubes: Perform these steps to disable drill-through links on a cube-by-cube basis.

   1. Open the schema for the particular cube on which you want to disable drill-through links.
   2. Find the Cube element in the schema file and add this annotation to disable the links:

      ```
      <Annotations><Annotation name="AnalyzerDisableDrillLinks">true</Annotation></Annotations>
      ```
   3. Save and close the schema.

   Drill-through links are now completely disabled for that cube, and the option to show drill-through links is no longer visible on the Report Options dialog box for the cube.
