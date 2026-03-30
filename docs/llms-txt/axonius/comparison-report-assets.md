# Source: https://docs.axonius.com/docs/comparison-report-assets.md

# Comparison Report for Assets

You can create and export a report that will show the difference between the values of a predefined list of fields on one or more assets between two defined dates. You can also choose a field and see the assets on which it changed. In this way you can see changes in defined fields on an asset between these dates.

<Callout icon="📘" theme="info">
  Note

  You need to have Export CSV permission for all of the asset types you want to compare,  in order to create Comparison reports.
</Callout>

## To Create a Comparison Report

1. On the Asset   page select one or more assets. Note that you can't create a Comparison Report for more than 100,000 entities.
2. From the **Action** menu choose **Comparison Report**; the **Comparison Report** dialog opens, showing the number of devices selected. Alternately, from the **Asset Investigation** tab, choose **Comparison Report**.
3. In the **Set base date** field set a starting date. You can compare dates either when the first date is earlier than the later date, or when the first date is later than the second date.
4. In the **Set Comparison Date** field set a date to compare. When you choose the current date, information is taken from the latest data available.
5. The Available fields pane shows all of the fields available.
6. Select the fields that you want to investigate and click **Add**; they now appear in the **Fields to Investigate** pane.
7. If needed **Remove** fields which you are not interested in seeing.
8. You can select **Show only differences** if you want to show only what changed. This is useful if you have already run this report.
9. Click **Generate Report** to generate the **Comparison Report**.
   A CSV file is created in the format 'Comparison-Report--'
   The followed parameters appear in the file:

* **Asset Name** or  **User Name** – The values in the Asset Name field for the asset - Can have multiple values. When comparing users, this column is called User Name.
* **Asset Unique ID** - The Asset Unique ID field, a unique identification assigned by Axonius to any asset record.
* **Field Name** – the name of the field you want to investigate
* **Date** – the value of this field on the date that you set in the **Set base date** field (whether the date is earlier in time or not). The heading of the column is the *base date* that you set. The value is the value of the field as it was on the set date.

<Callout icon="📘" theme="info">
  Note

  If an asset did not exist on the base date the value of the Base Date field will be *asset not found on this date*.
</Callout>

* **Second date** - the value of this field on the date that you set in the **Set Comparison Date** field (whether the date is earlier in time or not). The heading is the *Comparison date* that you set. The value is the value of the field as it was on the set date.
* **Values Added** – shows all values that were added to the field between the 2 dates. If a value changed, then the new value is considered as added.
* **Values Removed** - shows all the values that were removed from the field between the 2 dates. When a value was changed, the old value is considered as removed.
* **Changed** – *Yes* or *No* – tells you if the value of the field changed.