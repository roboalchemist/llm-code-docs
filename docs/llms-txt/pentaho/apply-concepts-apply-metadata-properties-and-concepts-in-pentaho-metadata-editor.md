# Source: https://docs.pentaho.com/pba-metadata-editor/apply-metadata-properties-and-concepts-in-pentaho-metadata-editor-cp/apply-concepts-apply-metadata-properties-and-concepts-in-pentaho-metadata-editor.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/apply-metadata-properties-and-concepts-in-pentaho-metadata-editor-cp/apply-concepts-apply-metadata-properties-and-concepts-in-pentaho-metadata-editor.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/apply-metadata-properties-and-concepts-in-pentaho-metadata-editor-cp/apply-concepts-apply-metadata-properties-and-concepts-in-pentaho-metadata-editor.md

# Apply concepts

As with relational data modeling, three levels of concepts for the business objects in the business model define your metadata. One level is an inherited level, so you need to learn to work with only two concept application processes: self concepts and parent concepts.

## Use the Concept Editor

Parent concepts are independent hierarchies of concepts that can be assigned to one or more business objects through the navigation tree. Before you can assign a parent concept you must first learn how to create one.

The Concept Editor allows you to build concepts to be used as parent concepts. The ability to isolate the concepts, name them, then associate the named concept with one or more business objects gives you flexibility and good concept management. Another feature of the Concept Editor is that you can define concepts that build upon other concepts. By nesting concepts this way, you minimize the number of properties you must repeatedly define and create a good inheritance hierarchy.

![Concept Editor](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-193d242534acbd736db8d1258e434d32386f033f%2F40_pme_concept_editor.png?alt=media)

### The default concept

The default concept is the default set of properties assigned to objects, mainly used for formatting. For example, the mask for all currencies could be set to **$#,##0.00;($#,##0.00)** by default. Every model contains a default concept called **Base**. This concept is applied as the parent concept to all physical columns created under a connection. The default concept includes metadata properties that are commonly defined and sets a base line set of metadata for all physical columns in the metadata model. The purpose of the default concept is to provide legitimate values for common metadata properties that may not be set in other places in your hierarchy. You can update, add, and delete metadata properties on the default concept. You can also remove the default concept as the parent concept for any and all physical columns. You cannot, however, delete the default concept from the list of concepts in the Concept Editor.

## Build concepts

The set of instructions below is an example of how to build a concept:

1. On the main page of the Pentaho Metadata Editor toolbar, click the Pencil icon top open the Concept Editor.
2. With the **Base** concept selected in the **Concepts** list, click the Plus Sign to add concepts. Add a nested concept. Name this concept, `Number`.
3. Make sure the Number concept is selected in the **Concepts** list.

   Note that the properties from **Base** have been inherited by Number.
4. Add a **Mask** property to Number, with a value of **$###,##0.00**.
5. With Number selected in the **Concepts** list, add another nested concept called `ID`.
6. Select ID in the **Concepts** list, find the inherited **Mask** property (under **Settings**).
7. Click the override icon and enter an override value of `0` (zero) for the mask.

   **Note:** You now have three defined concepts that can be used anywhere in your business model. Each concept serves a different type of business object: **Base** for default, generic columns; **Number** for those columns you know contain numeric financial data; and, **ID** for ID columns.
8. Click **OK** to save the concepts.

## Add parent concepts

Perform the following steps to add a parent concept and its metadata properties to the business object:

1. Select any physical table in the navigation tree.

   In this sample walkthrough exercises the **Customers** physical table is used.
2. Expand the columns under the table in navigation tree. Apply the **ID** concept to the column **Customernumber**.
3. Right-click (or CTRL and click) on the column, and select **Set Parent Concept** from the menu.
4. Choose the **ID** concept and click **OK**.

You should see the concept in the right column of the navigation tree on all objects to which it was applied.

## Remove parent concepts

Perform the following steps to remove the parent concept and its metadata properties from the business object:

1. Select any physical table in the navigation tree.
2. Expand the columns under the table in navigation tree and select the column that contains the concept you want to remove.
3. Right-click (or CTRL and click) on the column and select **Clear Parent Concept** from the menu.

The parent concept and its metadata properties are removed from the object.
