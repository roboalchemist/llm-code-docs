# Source: https://docs.pentaho.com/pba-report-designer/add-report-elements-in-report-designer-cp/create-an-index.md

# Source: https://docs.pentaho.com/pba-report-designer/9.3-report-designer/add-report-elements-in-report-designer-cp/create-an-index.md

# Source: https://docs.pentaho.com/pba-report-designer/10.2-report-designer/add-report-elements-in-report-designer-cp/create-an-index.md

# Create an index

The Index feature is also similar to a sub-report. It allows you to generate an index based on fields or groups in your report. When the index is generated, it displays the instances and page number where the field name appears.

Follow the instructions below to create an index:

1. Click and drag the index icon onto the report canvas.

   You are prompted to make the index element Inline or Banded. Choose one.

   * Inline sub-reports can be placed side-by-side with other elements (even other sub-reports).
   * Banded sub-reports occupy a variable height, but 100% of the report page width, so they cannot be on the same line with other elements.
2. Click the **index** element; under **Attributes**, double-click data-field and select the field to which you want to map.

   In the example below, the data-field is mapped to PRODUCT NAME.

   ![Data-field mapped to PRODUCT NAME](https://550079190-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FwlpCEXkXNwNKB6O9BgU8%2Fuploads%2Fgit-blob-0c79b51937f8aae38ed3de26db398749ce16a944%2Frd_index_data_field.png?alt=media)

   * **data-field**

     Defines the field to be used as the **item-data** or **item-key**.
   * **data-formula**

     Defines an open formula to be used as the **item-data** or **item-key**. Make sure that data-field is not defined, if this is used.
   * **index-separator**

     Defines the separator text that is used between page numbers in the **item-pages** field in the index sub report. It defaults to ",".
   * **condensed-style**

     Defines whether a `-` is used between continuous page numbers; example, `4,5,6,7` would display as `4-7`.
3. Double-click the **index** element.

   A new **sub-report** tab opens.
4. In the new report tab, create the appropriate index heading. Add the item-data and item-pages functions to generate the index data field name and page numbers.

   Keep in mind that all your entries will be included in the parent report. When you are finished, switch back to the main report tab.
5. Preview your report.

   **Note:** The index appears on the last page of your report.

You should now have an index embedded in your current report.
