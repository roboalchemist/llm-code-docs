# Source: https://docs.pentaho.com/pba/pentaho-analyzer-cp/working-with-analyzer-fields/fields-in-analyzer/types-of-fields-in-analyzer.md

# Source: https://docs.pentaho.com/pba/9.3-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/fields-in-analyzer/types-of-fields-in-analyzer.md

# Source: https://docs.pentaho.com/pba/10.2-analytics/pentaho-analyzer-cp/working-with-analyzer-fields/fields-in-analyzer/types-of-fields-in-analyzer.md

# Types of fields in Analyzer

The following types of fields are available:

* **Levels**

  Fields, such as Names, Types, and Categories are most often text-based. For example, if you were working for an athletic equipment vendor, you would use **Product Name** level in your reports. In this level, you might have 'Snow Sports' and 'Cycling' as possible values for the **Product Name** field. These individual values are often referred to as members of that level.
* **Time Period Fields**

  While Time fields are technically Level fields as well, Time fields are critical to nearly all reports and are often regarded as their own category of fields. Time period fields such as 'Fiscal Year' and 'Order Month' are commonly used in reports. Possible values for those fields could be '2004' and 'Jan-2006', respectively.
* **Measures**

  Measure fields are numeric and most often represent business metrics. These types of fields are designed for mathematical activities such as summing, dividing, and creating averages. 'Sales Revenue' and 'Profit Margin' are examples of measures.

In Analyzer reports, fields are color-coded by type in both the report and the **Layout** panel. The colors are assigned as follows:

* Levels including Time Period fields are defaulted with a yellow background.
* Measures are defaulted with a blue background.

You can create a report without any knowledge of field types, but knowing how field types work can sometimes help you understand how different charts display data and how filters work together.
