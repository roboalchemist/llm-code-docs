# Source: https://docs.pentaho.com/pba-report-designer/formulas-and-functions.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/formulas-and-functions.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/formulas-and-functions.md

# Formulas and functions

You can use formulas and functions to handle common formatting and editing tasks.

* [Conditional formatting](#conditional-formatting)
* [Multiple conditional formatting](#multiple-conditional-formatting)
* [Calculated dates](#calculated-dates)
* [Date and time parameters](#date-and-time-parameters)
* [Page numbering](#page-numbering)

## Conditional formatting

Perform the following steps to create a formula to highlight a given data cell with a background color depending the value of a field in your result set:

1. Open an existing report or create a new report, establish a data source and query, then drag your data-driven fields onto the canvas.
2. Select the data field you want to conditionally highlight.
3. Click the **Structure** tab and click bg-color in the text section under the **Style** tab.
4. Click the round green **+** (Add Expression) icon in the **Formula** column.

   The Expression dialog appears.
5. Click the ellipsis **(...)** to open the Formula Editor dialog box, then select **Logical** from the **Category** drop-down box.
6. Double-click the **IF** statement in the list on the left.
7. Click the **Select Field** icon, (on the far right), next to the **Test** line.
8. In the **Select Field** box, choose the field you want to conditionally format, then click **OK** to return to the Formula Editor.

   Alternatively, you can simply type the field name in \[square brackets] if you already know what it is.
9. Add a conditional statement to the **Test** line, after your field name.

   This is one of your formatting conditionals. For instance if you wanted to highlight cancelled orders in red, and this field contained order status, you could put `[STATUS]="Cancelled"` in the **Test** line, then a color value for red in the **Then\_value** line, as shown in the next step.
10. In the **Then\_value** line, type the color value or name you want to highlight this field with if the condition in the **Test** line is met.

    This can be a standard hexadecimal color value (such as #FF0000 for red), or a standard HTML color name (red, green, white, black, etc.).

    **Note:** This value must be in quotes.
11. Click **OK** to exit the Formula Editor dialog box; click **Close** to exit the Expression dialog box.
12. Click **Preview** and verify that your conditional formatting is properly executed.

    You may have to adjust your query if it does not produce a testable result set.

## Multiple conditional formatting

To highlight both cancelled and disputed orders in red, add an `OR` statement at the beginning of your **Test** line, enclose the conditions in parenthesis, and separate them with semicolons.

```
OR([STATUS]="Cancelled";[STATUS]="Disputed")
```

Your report output should now be formatted according to the specified conditions.

This is the resultant formula, following the above example for one condition and red and green colors:

### Simple conditional formatting

```
=IF([STATUS]="Cancelled";"#FF0000";"#00CC00")
```

This is the resultant formula, following the above example for two conditions and red and green colors:

### Multiple conditions

```
=IF(OR([STATUS]="Cancelled";[STATUS]="Disputed");"#FF0000";"#00CC00")
```

## Calculated dates

A date is typically displayed as a static number or a range, but this formula enables you to display specific dates like "the first Monday of the month" or "every second Wednesday."

Perform the following steps to create a formula to display a calculated date in a report:

1. Open an existing report or create a new report and establish a data source and query, then drag your data-driven fields onto the canvas.
2. Left-click the text field you want to print the calculated date in.

   If you do not have a text field dedicated to this task, create one now.
3. Click the **Structure** tab and click value in the common section under the **Attributes** tab.
4. Click the round green **+** (Add Expression) icon in the **Formula** column. The Expression dialogue will appear.
5. Click the ellipsis **(...)** to open the Formula Editor dialog box.
6. Select **Date/Time** from the **Category** drop-down box.
7. Double-click the **DATEVALUE** item in the list on the left.
8. Enter in your DATEVALUE formula, then click **OK**.

   For more information on DATEVALUE's parameters, see the OASIS reference page for

   * DATEVALUE:<http://www.oasis-open.org/committees/download.php/16826/openformula-spec-20060221.html#DATEVALUE>
   * VALUE: <http://www.oasis-open.org/committees/download.php/16826/openformula-spec-20060221.html#VALUE>\
     Alternatively, you can consult the examples below and modify them for your purposes.
9. Click **Close** to exit the Expression dialog box.
10. Click **Preview** and verify that your date values are properly calculated and formatted.

    You may have to adjust your query if it does not produce a testable result set.

The date values you specified should now appear correctly in your report.

### Some common calculated date formulas

#### 1st day of current month

```
=DATEVALUE(DATE(YEAR(NOW());MONTH(NOW());1))
```

#### Sunday of current week

```
=DATEVALUE(DATE(YEAR(NOW());MONTH(NOW());DAY(NOW())-WEEKDAY(Now();2)))
```

#### Saturday of current week

```
=DATEVALUE(DATE(YEAR(NOW());MONTH(NOW());DAY(NOW())-WEEKDAY(Now())+7))
```

#### Current day, date, and time

```
=NOW()
```

#### Current date

```
=TODAY()
```

#### Yesterday's date

```
=DATEVALUE(DATE(YEAR(NOW());MONTH(NOW());DAY(NOW()-1)))
```

## Date and time parameters

Perform the following steps to create a formula to display a calculated date in a report parameter:

1. Open an existing report or create a new report and establish a data source and query, then drag your data-driven fields onto the canvas.
2. Add a new parameter by clicking the **Master Report Parameter** button at the top of the **Data** pane.

   The Add Parameter dialog box will appear.
3. Type in an appropriate parameter name and friendly name for the parameter.
4. In the **Value Type** field, select or type in **Date**.
5. Create a formula for the **Default Value Formula**.

   If you want the current date and time to be the default, you can use `=NOW(` as your formula, or for a slightly more specific output, try `=DATEVALUE(DATE(YEAR(NOW());MONTH(NOW());DAY(NOW())-WEEKDAY(Now())))`.

   **Note:** Alternatively, to define a time-related value use the **Time Value Type** and select the appropriate option under **Timezone**.
6. In the **Display Type** field, select **Date Picker**, then click **OK** to create the parameter.
7. Click **Preview** and verify that the parameter displays and functions correctly.

   You may have to adjust your query if it does not produce a testable result set.

Your report's date-based result set can now be manually adjusted.

## Page numbering

Perform the following steps to use a function to add page numbers to your report:

1. Select the **Data** pane in the Report Designer interface.
2. Right-click the **Functions** section of the **Data** pane, then select **Add Functions** from the context menu.

   The Add Function dialog box will appear.
3. Double-click the **Common** category in **Functions**.
4. Click **Page of Pages**, then click **OK**.

   A new **Page of Pages** function will be added to your **Functions** list.
5. Drag a new text-field element to either the **Page Header** or **Page Footer** band.
6. Select the new text-field element, then go to the **Attributes** pane.

   You must select the **Structure** tab in order to access the **Attributes** pane.
7. In the field attribute's drop-down list, select the **Page of Pages** function that you created earlier.

You now have a page number printed in the header or footer of every page in your report. You can adjust the size and position of this element to match your preferences.
