# Source: https://docs.pentaho.com/pba-metadata-editor/metadata-properties-reference.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/metadata-properties-reference.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/metadata-properties-reference.md

# Metadata properties reference

This section contains the metadata properties reference.

## Out-of-the-box properties

The table below shows the properties that are provided with Pentaho Metadata Editor. Localized properties are indicated with an asterisk ( \* ) character.

| ID                          | Description                                                                                                                                                                                                                                                                                                                                                                                                                             | Category              | Values                                                                                                                                                                  |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name**\*                  | This property describes the display name for the business object.                                                                                                                                                                                                                                                                                                                                                                       | **General**           | Alphanumeric                                                                                                                                                            |
| **Description**\*           | A descriptive text entry describing the business object.                                                                                                                                                                                                                                                                                                                                                                                | **General**           | Alphanumeric                                                                                                                                                            |
| **Comments**\*              | Additional comments regarding the business object.                                                                                                                                                                                                                                                                                                                                                                                      | **General**           | Alphanumeric                                                                                                                                                            |
| **Security Information**    | Security rules for granting/restricting access to the business object.                                                                                                                                                                                                                                                                                                                                                                  | **General**           | Determined by security widget; see [Metadata security](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/metadata-security-pentaho-metadata-editor-cp). |
| **Font**                    | The font properties to apply to this business object.                                                                                                                                                                                                                                                                                                                                                                                   | **Formatting**        | Determined by selections in the font dialog box.                                                                                                                        |
| **Color of Text**           | The foreground or text color for the business object.                                                                                                                                                                                                                                                                                                                                                                                   | **Formatting**        | Determined by selections in the color dialog box.                                                                                                                       |
| **Text Alignment**          | The text alignment for the business object.                                                                                                                                                                                                                                                                                                                                                                                             | **Formatting**        | **Left**, **Right**, **Centered**, **Justified**                                                                                                                        |
| **Color of Background**     | The background color for the business object.                                                                                                                                                                                                                                                                                                                                                                                           | **Formatting**        | Determined by selections in the color dialog box                                                                                                                        |
| **Relative Size**           | This property is normally associated with business tables and is used to calculate join paths. The sum of all table relative sizes in a path are calculated when deciding on a multi-table join and the multi-table join with the smallest summed value is used for the join path.                                                                                                                                                      | **Formatting**        | Numeric                                                                                                                                                                 |
| **Aggregation Rule**        | Determines the method of aggregating the data from this business object.                                                                                                                                                                                                                                                                                                                                                                | **Model Descriptors** | **None**, **Sum**, **Count**, **Distinct Count**, **Minimum**, **Maximum**                                                                                              |
| **Data Type**               | Data type for this business object.                                                                                                                                                                                                                                                                                                                                                                                                     | **Model Descriptors** | **Unknown**, **String**, **Date**, **Boolean**, **Numeric**, **Binary**, **Image**, **URL**, and **Length** and **Precision** (Integers)                                |
| **Field Type**              | The type or relationship purpose this field serves.                                                                                                                                                                                                                                                                                                                                                                                     | **Model Descriptors** | **Other**, **Dimension** ,**Fact**, **Key**, **Attribute**                                                                                                              |
| **Table Type**              | Table type is used to automatically determine relationship types with other tables. For instance, if a **Fact** table is joined with a **Dimension** table, this is normally an **N to 1** relationship.                                                                                                                                                                                                                                | **Model Descriptors** | **Other**, **Dimension**, **Fact**                                                                                                                                      |
| **Formula**                 | This property allows you to create a calculation defining the business object. See [Pentaho metadata formulas](https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/pentaho-metadata-formulas-pentaho-metadata-editor-cp) for more information.                                                                                                                                                                            | **Calculation**       | Alphanumeric                                                                                                                                                            |
| **Is the Formula Exact?**   | <p>Determines whether the formula entered in the <strong>Value</strong> field in the <strong>Formula</strong> section is parsed by the Metadata Editor or if it is sent exactly as entered to the database:</p><ul><li>When this check box is selected, then the formula is sent to the database exactly as entered for processing.</li><li>When this check box is cleared, then the formula is parsed as a metadata formula.</li></ul> | **Calculation**       | Boolean                                                                                                                                                                 |
| **Column Width**            | The width of the column as represented for display.                                                                                                                                                                                                                                                                                                                                                                                     | **Miscellaneous**     | **Pixels**, **Percent of Page Width**, **Inches**, **Centimeters**, **Points**, and Integer                                                                             |
| **Hidden For the User?**    | Hides the object from being displayed in the **Business View** of the model.                                                                                                                                                                                                                                                                                                                                                            | **Miscellaneous**     | Boolean                                                                                                                                                                 |
| **Mask for Number or Date** | The format mask to use when the data for this object is displayed. For dates, the format follows the date/time patterns for a Java [SimpleDateFormat](http://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html) format mask. For numbers, the pattern should follow the Java [DecimalFormat](http://docs.oracle.com/javase/7/docs/api/java/text/DecimalFormat.html) format mask.                                        | **Miscellaneous**     | Alphanumeric                                                                                                                                                            |
| **Target Schema**           | Defines the database schema to use when querying the business object.                                                                                                                                                                                                                                                                                                                                                                   | **Miscellaneous**     | Alphanumeric                                                                                                                                                            |
| **Target Table**            | Defines the physical database table from which the business object is defined.                                                                                                                                                                                                                                                                                                                                                          | **Miscellaneous**     | Alphanumeric                                                                                                                                                            |

## Custom properties

You can define any number of custom properties. You must give your property an **ID** to set its type.

* String
* Date
* Numeric Value
* Color
* Font
* Type of Field
* Type of Aggregation
* Boolean
* Field Data Type
* Localized String
* Type of Table
* URL
* Metadata Security
* Text Alignment
* Column Width
* Data Constraints
* Optional Aggregations

### Custom table joins

You can also use a custom property to create table joins in Metadata Editor. To do this, you must define the custom property as **path\_build\_method** with a valid value. The following table defines the valid values for custom table joins:

| Value             | Description                                                                                                       |
| ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| **ALL**           | Use all tables and joins.                                                                                         |
| **ANY\_RELEVANT** | Use all joins that lead to any used table even if there is more than one path.                                    |
| **CLASSIC**       | Use the old generation method.                                                                                    |
| **FIRST\_SHORT**  | Returns the first path that only contains no duplicate joins between tables.                                      |
| **LOWEST\_SCORE** | Returns a path that chooses all joins that will create the smallest score based on the estimated size of a table. |
| **SHORTEST**      | (Default) Returns a path connecting every required table with the smallest number of joins.                       |

The generator defaults to **SHORTEST** if the property is not found in the model.

If this is determined to be too risky, then a Boolean value can be toggled in SqlGenerator or SQLGenerator to **preferClassicShortestPath** when set to **true**. Both classes will use **CLASSIC** if no setting is found in the model.

## Required properties per business object

The table below contains the required properties for given business objects. Required properties cannot be deleted.

| **ID**                      | Physical Table | Physical Column | Business Category | **Business Model** |
| --------------------------- | -------------- | --------------- | ----------------- | ------------------ |
| **Name**                    | Required       | Required        | Required          | Required           |
| **Description**             | Required       | Required        | Required          | Required           |
| **Security Information**    | Not required   | Not required    | Required          | Required           |
| **Table Type**              | Required       | Not required    | Not required      | Not required       |
| **Relative Size**           | Required       | Not required    | Not required      | Not required       |
| **Formula**                 | Not required   | Required        | Not required      | Not required       |
| **Field Type**              | Not required   | Required        | Not required      | Not required       |
| **Data Type**               | Not required   | Required        | Not required      | Not required       |
| **Aggregation Rule**        | Not required   | Required        | Not required      | Not required       |
| **Is the Formula Exact?**   | Not required   | Required        | Not required      | Not required       |
| **Hidden for the User?**    | Not required   | Required        | Not required      | Not required       |
| **Font**                    | Not required   | Not required    | Not required      | Not required       |
| **Mask for Number or Date** | Not required   | Not required    | Not required      | Not required       |
| **Color of Text**           | Not required   | Not required    | Not required      | Not required       |
| **Color of Background**     | Not required   | Not required    | Not required      | Not required       |
