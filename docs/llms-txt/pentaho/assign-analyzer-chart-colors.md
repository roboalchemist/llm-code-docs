# Source: https://docs.pentaho.com/pdia-admin/9.3-administer/customize-pentaho-products-cp/customize-pentaho-analyzer/assign-analyzer-chart-colors.md

# Source: https://docs.pentaho.com/pdia-admin/10.2-admin/customize-pentaho-products-cp/customize-pentaho-analyzer/assign-analyzer-chart-colors.md

# Assign Analyzer chart colors

Sometimes visualizations are more clear if you assign specific chart colors to data objects. For instance, you might want to assign colors to sales volume in different regions: red for the Northern region and blue for the Southern region. You can define colors like this using a member property in the Mondrian schema or using a text-based file inside the resources folder.

The color property works differently in various situations.

* **If a series contains one level and one measure,**

  then the color depends on the level member.
* **If a series contains multiple levels and one measure,**

  then the color depends on the level member that is farthest to the right.
* **If a series contains zero or more levels, or multiple measures,**

  then the color depends on the measure member. If there are multiple measures, each measure has a unique color.

If a member has a color mapping defined in both the text-based JSON file and in the Mondrian schema using the CHART\_SERIES\_COLOR property, the JSON file takes precedence over the CHART\_SERIES\_COLOR property.

## Assigning colors using a text-based file

You can create member-to-color mappings in a text-based JSON file if you do not want to define colors in the database or do not want to change the data structure. The file is located in `system/common-ui/resources/chartseriescolor/`. You must edit the `mdx.json` file to define color information for OLAP models such as Mondrian. Analyzer then uses this information to define colors. Define the color information using a web API such as [Json Parser Online](http://json.parser.online.fr/) to ensure you are using the correct JSON syntax.

When running a report, color mapping runs for all members in the report. If the JSON file has an invalid syntax, an error posts in the log file and no color information applies.

1. Using a JSON editor, open `pentaho-server\pentaho-solutions\system\common-ui\resources\chartseriescolor\mdx.json`.
2. Edit the sample so that the elements and colors are defined appropriately. The format is *\[Hierarchy Level].\[Member].\[Color]*. Specify color using hexadecimal or decimal values.

   In this example, the colors are set for the regions, which are `Central`, `Eastern`, `Southern`, and `Western`. The colors are then set for the measures, which are `Actual`, `Budget`, and `Variance`.

   ```
   "SampleData" : {
       "[Region].[Region]": {
           "[Region].[Central]": "#0000cc",
           "[Region].[Eastern]": "#0d8ecf",
           "[Region].[Southern]": "#b0de09",
           "[Region].[Western]": "#fcd202"
       },
        "[Measures].[MeasuresLevel]": {
            "[Measures].[Actual]": "#0000cc",
            "[Measures].[Budget]": "#0d8ecf",
            "[Measures].[Variance]": "#b0de09"        
         }
       }
   }
   ```
3. Save and close the JSON file.

## Assigning colors using a member property

You can change the colors of the members in an Analyzer report by defining a member property in the Mondrian schema. There are two different methods for assigning colors to levels or assigning colors to measures. The database column that stores color information is TERRITORY\_COLOR. This column is mapped to the CHART\_SERIES\_COLOR.

### Assigning colors to levels

1. Find the level for which you want to specify colors.

   In this example, the level name is "Territory," coming from a column named TERRITORY.
2. Define the member property name as CHART\_SERIES\_COLOR, the mapping to the database column as TERRITORY\_COLOR, and the data type for the color values as Integer.

   ```
   <Level name="Territory" column="TERRITORY" type="String" uniqueMembers="true" 
   levelType="Regular" hideMemberIf="Never"
   <Property name="CHART_SERIES_COLOR" column="TERRITORY_COLOR" type=Integer></Property>
   ```

### Assigning colors to measures

1. Find the measure for which you want to specify colors.
2. Define the **CalculatedMemberProperty** name as `CHART_SERIES_COLOR`.
3. Assign the color value using either a hexidecimal or decimal value.

   ```
   Measure name="Quantity" column="QUANTITYORDERED" formatString="#,###" aggregator="sum"
   <CalculatedMemberProperty name="CHART_SERIES_COLOR" value="13369344"/>
   </Measure>
   ```
