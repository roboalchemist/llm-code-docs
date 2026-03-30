# Source: https://docs.fiddler.ai/observability/model-ui/model-schema-editing.md

# Model Schema Editing

## Overview

This guide explains how to edit your model's schema in Fiddler to better align with production data. Schema editing helps you maintain accurate monitoring as your data evolves.

Key capabilities

* Adjust numeric feature ranges when real-world data deviates from your original sample data
* Edit categorical feature values to add or remove categories as new patterns emerge
* Add metadata columns to include additional contextual information for improved insights

### Adjusting numeric feature ranges

**Access the Schema tab**

1. Navigate to the Model Page of your desired model
2. Select the Schema tab

**Edit numeric column range**

1. Find the numeric column you want to adjust
2. Select the edit icon (✏️) next to the column name
3. In the dialog box, modify the minimum and/or maximum values
4. Select Update to save your changes

**Impact of changes**

* **Data drift metrics**: Changes apply to all data, including historical data
  * A job will run to recalculate aggregates and update metrics
* **Data integrity metrics**: Changes only apply to new data going forward

#### Editing categorical variables

**Access the Schema tab**

1. Navigate to the Model Page of your desired model
2. Select the **Schema** tab

**Edit categorical column**

1. Locate the categorical column you want to modify
2. Select the edit icon (✏️) next to the column name
3. Add or remove categories as needed
4. Select Update to save your changes

**Impact of changes**

* For both data drift and data integrity metrics:
  * Changes only apply to new data going forward
  * Historical data remains unchanged

#### Adding metadata columns

**Access the Schema tab**

1. Navigate to the Model Page of your desired model
2. Select the Schema tab

**Add a Metadata Column**

1. Select Add Metadata
2. Provide the required information:
   * Column Name: Specify the name of the new metadata column
   * Data Type: Choose a data type (integer, float, string, or boolean)
   * Range: For numeric types, define minimum and maximum values
3. Select Add to save

**Impact of Changes**

* New metadata columns are effective immediately for new data

### Best Practices

* Analyze production data to set realistic range values and identify useful metadata columns
* Monitor metrics after adjustments to ensure changes effectively address your needs
* Use annotations for transparency to maintain a clear history of schema changes

### Frequently Asked Questions

**Can I change column names or data types?**

No, changing column names or data types is not supported.

**What if I make a mistake?**

You can edit the values again and save the updated schema.

**How long do changes take to apply?**

Application time depends on dataset size and complexity. For example, processing 10 million rows over six months takes approximately 12 minutes.

**Can I delete a metadata column?**

No, metadata columns cannot be deleted once added.

**What happens if I add a category that doesn't exist in the data?**

The category will be listed but won't impact existing calculations.
