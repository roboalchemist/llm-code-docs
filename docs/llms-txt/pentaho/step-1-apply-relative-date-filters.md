# Source: https://docs.pentaho.com/pba-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-1-apply-relative-date-filters.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-9.3-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-1-apply-relative-date-filters.md

# Source: https://docs.pentaho.com/pba-schema-workbench/pdia-10.2-schema-workbench/adapt-mondrian-schemas-to-work-with-analyzer/step-1-apply-relative-date-filters.md

# Step 1: Apply relative date filters

Analyzer supports many types of relative date filters, but in order to apply them for a given level, you need to define the format string used to construct MDX members for that level. This is because each data warehouse implementation may have a different date format and set of hierarchy levels.

## Common relative date filters

In the Steel Wheels sample data cube provided by Pentaho for evaluation and testing, the Month level uses abbreviated three-letter month names. Furthermore, the Month level sits under the Quarter level. In Steel Wheels, the format string for an MDX member from the Month level would look like this:

```
[yyyy].['QTR'q].[MMM]
```

Some other common date formats:

* `[yyyy]` (Year)
* `[yyyy].[q]` (Quarter)
* `[yyyy].[q].[M]` (Month)
* `[yyyy].[q].[M].[w]` (Week)
* `[yyyy].[q].[M].[w].[yyyy-MM-dd]` (Day)

The Day line, above, also specifies a format to represent the entire date. Without this format, a simple `[d]` parameter would be difficult to put into context. For more information on date format strings, refer to the [SimpleDateFormat](http://icu-project.org/apiref/icu4j/com/ibm/icu/text/SimpleDateFormat.html) page on the ICU Project site.

To set up relative date filtering, for each level, you need to do the following:

* In your Mondrian schema file, set the **levelType** XML attribute to `TimeYears`, `TimeMonths`, `TimeQuarters`, `TimeWeeks` or `TimeDate`.
* Define the MDX date member format as an annotation with the name `AnalyzerDateFormat`.

Here is an example from the Pentaho sample data (Steel Wheels) Time dimension:

```
<Level name="Years" levelType="TimeYears" ... >
   <Annotations><Annotation name="AnalyzerDateFormat">[yyyy]</Annotation></Annotations>
</Level>
<Level name="Quarters" levelType="TimeQuarters" ... >
   <Annotations><Annotation name="AnalyzerDateFormat">[yyyy].['QTR'q]</Annotation></Annotations>
</Level>
<Level name="Months" levelType="TimeMonths" ... >
   <Annotations><Annotation name="AnalyzerDateFormat">[yyyy].['QTR'q].[MMM]</Annotation></Annotations>
</Level>
```

## Relative date filters for weeks

Use relative date filters for weeks to control the starting day of the week, the number of days comprising the first calendar week, and the starting calendar week of each year. If your week number and week year are required to be ISO8601 week-date compliant, or if you need to account for cultural time-keeping differences, you can customize how week numbers and week years are generated for the `w` and `YYYY` format strings.

Configure the following **filter.relative.dates.week** properties in the `analyzer.properties` file:

| Property                                                     | Description                                                                                                                                                                                       | Default value |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **filter.relative.dates.week.firstDayOfWeek**                | Specifies the first day of the week. Values are Sunday=`1`, Monday=`2`, Tuesday=`3`, Wednesday=`4`, Thursday=`5`, Friday=`6`, and Saturday=`7`.                                                   | 2             |
| **filter.relative.dates.week.minimalDaysInFirstWeek**        | Specifies the number of days considered to define the first week of a year. The ISO8601 standard requires 4 days to be present before counting the first week.                                    | 4             |
| **filter.relative.dates.week.firstWeekOnJanuary1st**         | Specifies the week number so that the first week of the calendar always starts on January 1st. When this property is set to `true`, the week year and the calendar year are the same.             | false         |
| **filter.relative.dates.week.firstWeekOnJanuary1st.fromOne** | If **filter.relative.dates.week.firstWeekOnJanuary1st**=`true` and the first week does not have the minimal number of days, this property specifies if week numbering should start at `0` or `1`. | false         |

For example, an alternative method for week numbering commonly used in the United States starts week 1 of every year on January 1st with the first day of all subsequent weeks starting on a Sunday. For this method, configure the following properties with the associated values:

* **filter.relative.dates.week.firstDayOfWeek**=`1`
* **filter.relative.dates.week.minimalDaysInFirstWeek**=`4`
* **filter.relative.dates.week.firstWeekOnJanuary1s**t=`true`
* **filter.relative.dates.week.firstWeekOnJanuary1st.fromOne**=`true`

**Note:** The week year (`YYYY`) uses a different format string than the calendar year (`yyyy`). For example, in the ISO8601 week date, the date 2018-12-31 belongs to week 2019-W1, so the calendar year is 2018 and the week year is 2019. In the previous United States week example, the calendar year and the week year are always the same, so the format string may use `yyyy` or `YYYY`.

## Other relative date filters

Other types of relative date filters are often used, especially for the fiscal year in the business sector. A fiscal year varies with each business and is based on how that business calculates its annual financial statements. You can define a Fiscal Calendar dimension in your Mondrian schema to accommodate this calculation, so Analyzer uses the current date to look up fiscal time periods in the fiscal time dimension.

For example, a business may define their fiscal year to always start on the first of May. Their fiscal time dimension table would look like the following table:

| Date       | Fiscal Week | Fiscal Month | Fiscal Quarter | Fiscal Year |
| ---------- | ----------- | ------------ | -------------- | ----------- |
| 2014-04-30 | 2014-W53    | 2014-M12     | 2014-Q4        | 2014        |
| 2014-05-01 | 2015-W1     | 2015-M1      | 2015-Q1        | 2015        |
| 2014-05-02 | 2015-W1     | 2015-M1      | 2015-Q1        | 2015        |

Looking at the table and using a date such as 2014-05-01, we can find which Fiscal Week, Fiscal Month, Fiscal Quarter, or Fiscal Year that it belongs to. Just look for the date in the table, then look further up the hierarchy to find 2015-M1. If you need to get the Current Month and Previous Month, you can first find 2015-M1 and then look back on the hierarchy to find 2014-M12, which is a sibling of 2015-M1 in the hierarchy.

There are a few key points to keep in mind about this dimension, before you get started:

* The bottommost level must be a Date, which will be used to look up a parent-level member based on the current date.
* The Date level must specify a new **AnalyzerFiscalDateFormat** annotation. This annotation value should specify a Java format string, which when evaluated with the current date, yields the MDX name of the Date level member. This format string should not include the format string for any parents above the Date level. This is different from the **AnalyzerDateFormat** annotation in which parents are also included in the format string.
* The Date level members must be unique within the level, so **uniquemembers** is set to `true`. This does not need to be the same for parent levels, but it is a good practice to do so since this is a time dimension.
* All levels in this hierarchy need to specify the **levelType** attribute.
* Levels above the Date level should not specify the **AnalyzerDateFormat** annotations.

Here is an example of a Fiscal Calendar dimension defined within a Mondrian schema:

```xml
<Dimension name="Fiscal Calendar" type="TimeDimension">
  <Hierarchy hasAll="true" primaryKey="DATE_KEY">
    <Table schema="FOODMART" name="CALENDAR"/>
    <Level name="Fiscal Year" levelType="TimeYears" column="FSC_YEAR_STR" uniqueMembers="true" type="String" ordinalColumn="FSC_YEAR" />
    <Level name="Fiscal Quarter" levelType="TimeQuarters" column="FSC_QUARTER_YEAR_STR" uniqueMembers="true" type="String" ordinalColumn="FSC_DIM_QUARTER_NUM" />
    <Level name="Fiscal Month" levelType="TimeMonths" column="FSC_MONTH_YEAR_STR" uniqueMembers="true" type="String" ordinalColumn="FSC_DIM_MONTH_NUM" />
    <Level name="Fiscal Week" levelType="TimeWeeks" column="FSC_WEEK_YEAR_STR" uniqueMembers="false" type="String" ordinalColumn="FSC_DIM_WEEK_NUM" />
    <Level name="Date" levelType="TimeDays" column="CAL_DATE" uniqueMembers="true" type="Date" ordinalColumn="DATE_KEY" >
      <Annotations><Annotation name="AnalyzerFiscalDateFormat">[yyyy-MM-dd]</Annotation></Annotations>
    </Level>
  </Hierarchy>
</Dimension>
```

With this set up, Analyzer will be able to generate the MDX to turn a filter like Current Month into the correct Fiscal Month member:

```
Ancestor([Fiscal Calendar].[Date].[1997-06-28],[Fiscal Calendar].[Fiscal Month])
```

This MDX references a specific date member in the Date level, and then uses the Ancestor function to locate the parent month. Finding the Previous Month would be as simple as using the Lag MDX function:

```
Ancestor([Fiscal Calendar].[Date].[1997-06-28],[Fiscal Calendar].[Fiscal Month]).Lag(1)

```

Once you have these set up, your users will be able to apply this filter by selecting **Choose a commonly used time period** in the Filter on Fiscal Month dialog box.

## Verify the relative date filter values

You can verify whether your **AnalyzerDateFormat** and **AnalyzerFiscalDateFormat** annotations are generating the expected time period members. Perform the following steps to produce the time period members for every level in the cube.

1. In Analyzer, click the **More actions and options** icon.
2. Go to **Administration** > **MDX**.
3. Click **Check AnalyzerDateFormat**.

All current and previous 365 time period members are displayed.

## Configure default values in filter dialog

When filtering on a level, by default, the filter dialog box will show the first N values as configured by the `filter.members.max.count` property. However, if you want to show a relative range of time periods, you can set the **AnalyzerDateFilterStart** and **AnalyzerDateFilterEnd** annotations to specify a range of time periods relative to the current date. For example, if for the Date level, you want to show the Last 30 Days, Today and Next 7 Days, you can set **AnalyzerDateFilterStart** to `-30` and **AnalyzerDateFilterEnd** to `7`. **AnalyzerDateFilterStart** can contain a negative or zero integer indicating a previous time period or the current time period as a starting range. **AnalyzerDateFilterEnd** can contain a zero or positive integer indicating a current or future time period as an ending range.

When using the range filter, you can also set the default value for the Before, After and Between operators using the **AnalyzerDateFilterDefaultStart** and **AnalyzerDateFilterDefaultEnd** annotations. For example, if you want to set the Before, After and the Between Start and End values to the Current Date, you can set **AnalyzerDateFilterDefaultStart** and **AnalyzerDateFilterDefaultEnd** to `0`. The values specified for **AnalyzerDateFilterDefaultStart** and **AnalyzerDateFilterDefaultEnd** must be within the range specified by **AnalyzerDateFilterStart** and **AnalyzerDateFilterEnd**.
