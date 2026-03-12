# Source: https://docs.pentaho.com/pba-report-designer/add-report-elements-in-report-designer-cp/create-a-table-of-contents.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/add-report-elements-in-report-designer-cp/create-a-table-of-contents.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/add-report-elements-in-report-designer-cp/create-a-table-of-contents.md

# Create a table of contents

The Table of Contents (TOC) feature is similar to a sub-report. It allows you to generate a TOC based on groups you have mapped inside the report or to specify the sub-reports you want included in your TOC.

Follow the instructions below to create your TOC:

1. Click and drag the table-of-contents icon onto the report canvas.

   You are prompted to make the TOC element Inline or Banded. Choose one.

   * Inline sub-reports can be placed side-by-side with other elements (even other sub-reports).
   * Banded sub-reports occupy a variable height, but 100% of the report page width, so they cannot be on the same line with other elements.
2. Click the **TOC** element and Define the following attributes for the TOC element:
   * **group-fields**

     Defines both the depth of the data-collection and the fields from where to read the **group-value-X** values. If the **group-field** given in the array is empty, the field value will be read from the current relational group and in the **details-processing**, the value will be null. If the **group-fields** list is empty, an automatic mode is activated that collects all groups extracting the **group-value** from the relational group.
   * **collect-details**

     Defines whether detail items should be included in the **data-collection**.

     **Note:** This attribute consumes a significant amount of system memory. Do not use this attribute on reports that are over a million rows.
   * **title-formula**

     Defines a formula that is evaluated when a new item has been collected. The formula will only be evaluated if the **title-field** is not set.
   * **title-field**

     Defines a field in the master-report that will be read for a valid **item-title**.
   * **title-formula**

     Defines a formula that is evaluated when a new item has been collected. The formula will only be evaluated if the title-field is not set.
   * **index-separator**

     Defines the separator text that is used between the index-elements. It defaults to ".".
3. Double-click the **TOC** element.

   A new sub-report tab opens.
4. In the new report tab, create the appropriate TOC headings and add the group value you want mapped. Add an item-page function to generate the page numbers.

   Keep in mind that all your entries will be included in the parent report. When you are finished, switch back to the main report tab.
5. Preview your report.

You should now have a TOC embedded in your current report.

If you have multiple groups, you can create bookmark links manually by using the [URL Linking feature](https://docs.pentaho.com/pba-report-designer/10.2-report-designer/apply-formatting-to-report-elements-in-report-designer-cp).
