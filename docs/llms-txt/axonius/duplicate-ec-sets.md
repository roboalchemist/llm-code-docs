# Source: https://docs.axonius.com/docs/duplicate-ec-sets.md

# Duplicating Enforcement Sets

You can duplicate Enforcement Sets. Duplicating an Enforcement Set is useful if you want to create a new Enforcement Set that has several similar Enforcement Actions.

<Callout icon="📘" theme="info">
  Note

  * You cannot duplicate an Enforcement Set from the Predefined Enforcements sets folder.

  * Only one Enforcement Set can be duplicated at a time.
</Callout>

**To duplicate an Enforcement Set**

1. In the table on the [**Enforcements** page](using-the-ec-page#opening-the-enforcement-sets-page), do one of the following:
   * Hover over the row of an Enforcement Set, and then at the end of the row, click the **Duplicate** icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DuplicateIcon\(1\).png).
   * Select the checkbox of a single Enforcement Set, and then on the top right of the table, click the **Duplicate** action ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DuplicateAction\(1\).png).

The 'Make a copy of ' dialog opens.

<Image align="center" alt="duplicate2.png" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/duplicate2.png" />

2. Set the following:

* **Enforcement set name** – Use the name provided or type a new meaningful name.
* **Clone automation settings** – Select the checkbox (the default) to use the same automation (run schedule) settings as the original enforcement set, or clear the checkbox to remove the automation settings in the copy. You can edit the copy to configure new automation settings in the **Scheduling type** section.

3. Click **Create a Copy**. The Enforcement Set configuration screen opens, and a message is displayed on top informing you that the Enforcement Set was created successfully.

4. Make changes to the new Enforcement Set as required, and then click **Save**. The system tells you that you saved the Enforcement Set.

   The new Enforcement Set now appears in the **Enforcements** page.

<Callout icon="📘" theme="info">
  Note

  The copy of an Enforcement Set scheduled to run every discovery cycle is assigned the run priority of the Enforcement Set.
</Callout>