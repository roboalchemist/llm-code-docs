# Source: https://docs.pentaho.com/pba/data-source-model-editor-cp/get-started-with-the-data-source-model-editor/tour-the-data-source-model-editorinterface.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/data-source-model-editor-cp/get-started-with-the-data-source-model-editor/tour-the-data-source-model-editorinterface.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/data-source-model-editor-cp/get-started-with-the-data-source-model-editor/tour-the-data-source-model-editorinterface.md

# Tour the Data Source Model Editor

When you first open the model editor, the center pane of the dialog box displays the active model. This model is organized into categories and fields that represent the tables and columns in your data.

![Data Source Model Editor interface](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-a48adba0b6b7fb78a3e8daaca3289bcdf5a9782c%2FProducts_Data_Source_Model_Editor_Get_Started.png?alt=media)

| Item | Name                                | Function                                                                |
| ---- | ----------------------------------- | ----------------------------------------------------------------------- |
| 1    | **Available** pane                  | Displays a list of the available tables and columns of the data source. |
| 2    | **Analysis / Reporting** model pane | Displays the active data source model.                                  |
| 3    | **Properties** pane                 | Displays the properties associated with a selected category or field.   |

## Analysis toolbar tasks

![Analysis Toolbar](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-a2cbc8aa3d04aec3f8d9ff72515850f80b36fc9f%2FProducts_Data_Source_Model_Editor_Analysis_Toolbar.png?alt=media)

| Icon Name               | Function                                 | Definition                                                                                                                                                                                                                                    |
| ----------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Add Measure**         | Add a measure to the model.              | A measure is a property on which calculations can be made, such as a sum, count, or average.                                                                                                                                                  |
| **Add Dimension**       | Add a dimension to the model.            | A dimension is used to provide filtering, grouping, or labeling capabilities. A dimension is related to fact data, and is typically something like a product model, color, size, geographic location, salespeople's names, or a unit of time. |
| **Add Hierarchy**       | Add hierarchies to a dimension.          | Hierarchies organize data by strict ranks.                                                                                                                                                                                                    |
| **Add Level**           | Add levels to a hierarchy.               | A level is a set of objects within a hierarchy that have the same rank or importance.                                                                                                                                                         |
| **Add Member Property** | Add custom member properties to a level. | Member properties are the attributes of a level.                                                                                                                                                                                              |
| **Move Up / Down**      | Move levels up and down in a hierarchy.  | Moving levels up and *down* allow you to change their ranks within the hierarchy.                                                                                                                                                             |
| **Remove field**        | Removes a field from the model.          | n/a                                                                                                                                                                                                                                           |
| **Clear Model**         | Clears the entire model.                 | n/a                                                                                                                                                                                                                                           |

## **Reporting** toolbar tasks

![Reporting toolbar](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-0548301a405c9074407b44c6a9beb2abd7b8b17e%2FProducts_Data_Source_Model_Editor_Reporting_Toolbar.png?alt=media)

| Icon Name               | Function                                 | Definition                                                                      |
| ----------------------- | ---------------------------------------- | ------------------------------------------------------------------------------- |
| **Add Category**        | Add a category to the model.             | A category is a structure that contains objects that are linked.                |
| **Add Field**           | Add a field to a category.               | A field is the place where data is stored within a category.                    |
| **Move Up / Down**      | Move levels up and down in a hierarchy.  | Moving levels up and down allow you to change their ranks within the hierarchy. |
| **Remove field**        | Remove a field.                          | n/a                                                                             |
| **Add Member Property** | Add custom member properties to a level. | Member properties are the attributes of a level.                                |
| **Clear Model**         | Clears the entire model.                 | n/a                                                                             |
