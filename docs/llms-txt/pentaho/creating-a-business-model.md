# Source: https://docs.pentaho.com/pba-metadata-editor/creating-a-business-model.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/creating-a-business-model.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/creating-a-business-model.md

# Creating a business model

The business model is how you create the logical mapping of business objects to the physical tables and columns. The model is also the place where you define the relationships between your business tables and how you organize the business view.

## Create a business model

Perform the following steps to create a business model:

1. Right-click **Business Models** in the navigation pane and select **New Business Model**.

   The Business Model Properties dialog box appears as shown below.

   ![](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-cbf269bba3ddd0597bec41a2d150634944d8c1cc%2F06_pme_business_model.png?alt=media)
2. At the top of the dialog box, there is an **ID** text field, pre-populated with a value. Pentaho recommends you accept the pre-populated value as this value must be unique across all models that you define.
3. To name your new model, enter a new value under the **Name** property text box on the right.
4. Click **OK** to save your changes and exit the dialog box.

## Add business tables and columns

After you create a business model, you must add the business tables and business columns. Then, you need to create the relationships between your business tables.

Up to this point, you have used the navigation pane to build the business objects. The workspace on the right side of the page is called the **Metadata Editor Graph**. Use the **Metadata Editor Graph** to lay out your business tables and show the relationships between them. While you can accomplish the rest of your tasks by manipulating the objects in the navigation pane, you can also use the **Metadata Editor Graph**.

![Metadata Editor Graph, PME](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-3710cb329e658c2e0d2bb0c0e7ec36557e22cbca%2F08_pme_business_table_2.png?alt=media)

Perform the following steps to create business tables and columns:

1. Right-click **Business Tables** in the navigation pane or inside the **Metadata Editor Graph** workspace, and select **Business Tables**. You can drag a physical table from the navigation pane to the **Metadata Editor Graph** workspace to create a new business table based on that physical table.

   For example, the Customers business table was created by dragging the CUSTOMERS physical table as shown above. You can also drag the physical table in the navigation pane to the **Business Tables** node to create a new business table based on that physical table.

   A list of physical tables will appear, prefixed by the connection name to which they belong.
2. Select the physical table you want associated with the new business table.
3. Click **OK** to display the Business Table Properties dialog box. In the Business Table Properties dialog box, the **ID** field is pre-populated with a value. This ID identifies a specific business table, and must be unique. Pentaho recommends that you accept the default value for this field.

   ![Business Table Properties dialog box](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-a4899c0e42b2bf87aacc12967fc6c079580c53d5%2F07_pme_business_table.png?alt=media)

The table you chose in Step 3 is listed next, then below the fields is another navigation pane with the name of your business table and all the columns inherited from the physical table included as business columns. The business columns are created for you when the new business table is created.

## Remove business columns

Perform the following steps to delete business columns:

1. In the Business Table Properties dialog box navigation pane, select the column you want to remove.

   ![Business Table Properties](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-540b16d1d0fedd518d1bedc012382a03e959f9cf%2F10_pme_delete_column.png?alt=media)
2. Click the X icon to delete column.

   The column you selected is removed from the list.
3. Repeat Steps 1 and 2 with the remaining columns you want to delete.
4. Click **OK** when you are done.

## Add relationships between business tables

Once you have all of your business tables created, you must create relationships between the tables so that the query generators and SQL generators that work with Pentaho Metadata can create the data queries correctly. This is similar to drawing a relational diagram to show primary and foreign key relationships; however, relational links are not the only relationships that can be modeled. You can create a relationship between any two tables, link any two columns between them and dictate what the relationship is (one to many, many to many, and so on). The important pieces of information to know before you try to create a relationship are:

* What two business tables would you like to associate with this relationship?
* What columns in the business tables identify the relationship?
* What type of relationship is it: one to one, one to many, many to one? See the table below for relationship types and descriptions.

| Relationship | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1:N**      | A one-to-many mandatory relationship is the most common relationship in databases. The primary key table contains only one record that relates to none, one, or many records in the related table. This relationship is similar to the one between you and one of your parents. You have one mother, but your mother may have several children.                                                                                                                                   |
| **N:1**      | A many-to-one is opposite of one to many (1:N) relationship.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **1:1**      | In a one-to-one relationship, both tables are limited to one record only on either side of the relationship. Each primary key value relates to a single record, or no record, in the associated table. The value can have only the one designated partner, or no partner at all. Most one-to-one relationships are forced by business rules. If you do not have a business rule, you can, in most cases, combine both tables into one table without breaking normalization rules. |
| **0:N**      | A zero to many optional relationship indicates that a person may have no phone, one phone, or many phones, and that the phone may not be "owned," but can only be owned by a maximum of one person.                                                                                                                                                                                                                                                                               |
| **N:0**      | Opposite of a zero to many relationship                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **0:1**      | A zero to one relationship might indicate that a person may be a programmer, but a programmer must be a person. It is assumed that the mandatory side of the relationship is the dominant.                                                                                                                                                                                                                                                                                        |
| **1:0**      | Opposite of a zero to one relationship                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **N:N**      | In a many to many relationship each record in both tables can relate to an unlimited number of records (or no records) in the other table. For example, if you have many siblings, your siblings also have many siblings. Many-to-many relationships must have a third table, referred to as an associate or linking table, because relational systems cannot accommodate the relationship directly.                                                                              |
| **0:0**      | A zero to zero optional relationship indicates that a person may occupy one parking space, but that a person is not necessary to have a space and a space does not need to have a person.                                                                                                                                                                                                                                                                                         |

### With the navigation pane

To create a new relationship between business tables in the navigation pane, first make sure that the model you want to add this relationship to is selected, and that the **Relationships** node is visible.

1. Right-click **Relationships** in the navigation pane.
2. Select **New Relationship**.

   The Relationship Properties dialog box appears.
3. Select a business table from the **From Table/Field** list.

   This is the first relationship.
4. Select a business table from the **To Table/Field** list.

   This steps sets up a relationship between two tables.
5. Specify the business columns (from the adjacent lists) from each business table that identify this relationship. If the business column names are similar, click **Guess Matching Fields** and let Pentaho Metadata Editor attempt to determine the columns for you.
6. Define the relationship from the **Relationship** drop-down list.
7. Click **OK** when you are done.

   You should see a new relationship line drawn between the two tables on the editor graph, and the relationship represented in the navigation pane.

   ![](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-9d51abff9eb56e6b4db7f8d875bf9f1b227b5221%2F11_pme_relationships.png?alt=media)

   **Note:** Complex joins appear in the `WHERE` clause of the SQL statement, so currently any joining that takes place in the `FROM` clause of the SQL statement is not supported. An example of a complex join might be TABLE\_A.COL\_A=TABLE\_B.COL\_A AND TABLE\_A.COL\_B=TABLE\_B.COL\_B. This represents a join of two tables based on two key columns versus a single join column. Also note, the complex join expression provided must use the names of the physical tables and physical columns, not business tables and business column names.

### With the editor graph

In the editor graph, creating a new relationship is somewhat simplified because you select the two business tables on the canvas, and the Relationship Properties dialog box is pre-populated with your selections. Before you start, make sure that the model you want to add a relationship to is selected, and that the business tables are displayed in the editor graph.

1. Select the two business tables you want to include in the new relationship, either by clicking and dragging a marquee around the tables or by holding the SHIFT CTRL keys, then clicking on the tables.
2. Once your business tables are selected, right-click on the selection. Click **Add Relationship** in the popup menu.

   ![Editor graph menu](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-40938c24a737a73a49f571b64d51c37935161465%2F11a_pme_relationships.png?alt=media)
3. When the Relationship Properties dialog box appears, select a business table from the **From Table/Field** list.

   This is the first relationship.
4. Select a business table from the **To Table/Field** list.

   This steps sets up a relationship between two tables.
5. Specify the business columns (from the adjacent lists) from each business table that identify this relationship. If the business column names are similar, click **Guess Matching Fields** and let Pentaho Metadata Editor attempt to determine the columns for you.
6. Define the relationship from the **Relationship** drop-down list.
7. Click **OK** when you are done.

   You should see a new relationship line drawn between the two tables on the editor graph, and the relationship represented in the navigation pane.

   ![](https://735364065-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FHzvIaQQIf5LLaf5hBGV8%2Fuploads%2Fgit-blob-9d51abff9eb56e6b4db7f8d875bf9f1b227b5221%2F11_pme_relationships.png?alt=media)

   **Note:** Complex joins appear in the `WHERE` clause of the SQL statement, so currently any joining that takes place in the `FROM` clause of the SQL statement is not supported. An example of a complex join might be TABLE\_A.COL\_A=TABLE\_B.COL\_A AND TABLE\_A.COL\_B=TABLE\_B.COL\_B. This represents a join of two tables based on two key columns versus a single join column. Also note, the complex join expression provided must use the names of the physical tables and physical columns, not business tables and business column names.

## Hadoop Hive-specific SQL limitations

There are a few key limitations in Hive that prevent some regular Metadata Editor features from working as intended, and limit the structure of your SQL queries in Report Designer:

* Outer joins are not supported.
* Each column can only be used once in a `SELECT` clause. Duplicate columns in `SELECT` statements cause errors.
* Conditional joins can only use the `=` conditional unless you use a `WHERE` clause. Any non-equal conditional in a `FROM` statement forces the Metadata Editor to use a Cartesian join and a `WHERE` clause conditional to limit it.
