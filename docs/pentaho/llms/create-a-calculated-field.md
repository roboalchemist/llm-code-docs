# Source: https://docs.pentaho.com/pba/pentaho-interactive-reports-cp/use-calculated-fields-in-pentaho-interactive-reports/create-a-calculated-field.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-interactive-reports-cp/use-calculated-fields-in-pentaho-interactive-reports/create-a-calculated-field.md

# Create a calculated field

Perform the following steps to create a calculated field:

1. Select the **Data** tab in the Interactive Report in which you want to add a calculated field.
2. Navigate to the bottom of the **Data** tab, locate the **Calculated Fields** entry.

   ![Data tab with Calculated Fields](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-5f248d5aa4999633817b694fc0c04144948dafe6%2FPIR%20Data%20tab%20with%20Calculated%20Fields.png?alt=media)
3. Click the plus sign on the **Calculated Fields**.

   The **Create Calculated Field** dialog box appears.

   ![Creat Calculated Field dialog box](https://591371677-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FFgwF7oC7Y6b7XWdahykf%2Fuploads%2Fgit-blob-4f6c6063ee74809fd83d64994ef7c61b8a24bd4d%2FPIR%20Creat%20Calculated%20Field%20dialog%20box.png?alt=media)
4. Enter the values as for your calculated field as described in the following table:

| Field             | Description                                                                                                                                                                                                                      |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Display Name**  | Enter the name of the calculated field you want displayed.                                                                                                                                                                       |
| **Category**      | Select the category of the function.                                                                                                                                                                                             |
| **Select Fields** | Select the fields to use in the formula.                                                                                                                                                                                         |
| **Functions**     | Select the formula function to apply in the calculated field by double-clicking the function name. The function will appear in the **Formula** field. See the **Pentaho Report Designer** document for common formula functions. |
| **Formula**       | Edit your formula field to your specifications.                                                                                                                                                                                  |
| **Data Format**   | <p>Select the data type for the calculated field you have created. The values are:</p><ul><li>Numeric</li><li>Date</li><li>Other</li></ul>                                                                                       |
| **Description**   | Displays the description of the selected function                                                                                                                                                                                |
| **Return Type**   | Displays the return type of the selected function. For example, `SUM(2, 3)` will return an integer type, while `CONCATENATE("A", "B")` will return a string type.                                                                |

5\. Click \*\*OK\*\*

```
The calculated field is added to the list in the **Data** tab.
```

6\. (Optional) Right-click the calculated field to open a menu with the following options:

```
-   **Edit**: Select to edit the calculated field formula.
-   **Delete**: Select to delete the calculated field.
-   **Add To Report**: Select to add the calculated field to the columns in the report layout.
-   **Add To Groups**: Select to add the calculated field to the groups in the report layout.
```
