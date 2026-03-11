# Source: https://docs.axonius.com/docs/using-predefined-enforcement-sets.md

# Using Predefined Enforcement Sets

Axonius provides predefined Enforcement Sets that you can copy to quickly and easily create new Enforcement Sets. These Enforcement Sets, located in the **Enforcements** page under the **Predefined Enforcements** sets folder, are viewable only. When you create a new Enforcement Set based on a predefined Enforcement Set, it is saved in the **Shared Enforcements** folder, provided that the **Module**, **Query**, and required fields are filled in. Otherwise, it is saved in the **Drafts** folder.

<Callout icon="📘" theme="info">
  Note

  The **Actions** menu items are disabled for predefined Enforcement Sets.
</Callout>

**To create a new Enforcement Set from a predefined Enforcement Set**

1. In the [**Enforcements** page](using-the-ec-page#opening-the-enforcements-page), under the **Predefined Enforcements sets** folder, select the Enforcement Set that is similar to the one that you want to create.

2. In the **Edit Enforcement Set** drawer that opens, make any changes that you want. To learn more, see [Creating Enforcement Sets](/docs/create-ec-set).
   * If you do not change the name in **Enforcement Set name**, the system appends **Copy of** to the beginning of the predefined Enforcement Set name. If more than one Enforcement Set is created without assigning a name, the system appends **Copy of** to the latest name. For example: Copy of Copy of Create User department tag.

3. Click ![ButtonSaveAsNew](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ButtonSaveAsNew.png).
   If your new Enforcement Set is defined with a module, query, and main action required fields, the new Enforcement Set is saved under the **Shared Enforcements** folder. Otherwise, it is saved under the **Drafts** folder. The **Edit Enforcement Set** drawer opens. (This is the same Edit dialog used to edit any Enforcement Set defined in the system.)

4. In the **Edit Enforcement Set** drawer, make further changes to the newly created Enforcement Set, as required.
   * When all required fields are filled in, the **Save**, **Test Run**, and **Save and Run** buttons become enabled, and you can click any of them. The newly created Enforcement Set is saved under the **Shared Enforcements** folder as a regular Enforcement Set and can be managed as such.
   * If not all required fields are filled in, only the **Save** button is enabled. Either fill in the missing fields or click **Save** for future use from the Drafts folder.