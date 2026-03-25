# Source: https://docs.snowflake.com/en/sql-reference-classes.md

# SQL class reference

These topics provide reference information for Snowflake [classes](sql-reference/snowflake-db-classes.md).

Each class supports one or more of the following SQL operations:

* ALTER: Modifies the properties of an instance of a class.
* CREATE: Creates an instance of a class.
* DROP: Deletes an instance of a class.
* SHOW: Lists instances of a class.

An instance of a class can have one or more methods. A method is a stored procedure or function and can be called by
using the instance name and method name, and arguments (if any) required by the method. For example,
`CALL instance_name!method_name(...)`.

## Updating your search path

You can add the schema for classes you use frequently to your search path to save typing and make your SQL statements
more concise. For more information about updating your search path, see [Update your search path](sql-reference/snowflake-db-classes.md).

## Available classes

Snowflake provides the following system-defined (built-in) classes.

[ANOMALY_DETECTION (SNOWFLAKE.ML)](sql-reference/classes/anomaly_detection.md)
:   Allows you to detect outliers in your time series data.

[ANOMALY_INSIGHTS (SNOWFLAKE.LOCAL)](sql-reference/classes/anomaly_insights.md)
:   Allows you to detect outliers in your costs.

[BUDGET (SNOWFLAKE.CORE)](sql-reference/classes/budget.md)
:   Allows you to monitor credit usage of supported objects.

[CLASSIFICATION (SNOWFLAKE.ML)](sql-reference/classes/classification.md)
:   Automatically sorts data into categories based on features in the data.

[CLASSIFICATION_PROFILE (SNOWFLAKE.DATA_PRIVACY)](sql-reference/classes/classification_profile.md)
:   Allows you to automatically classify sensitive data.

[CUSTOM_CLASSIFIER (SNOWFLAKE.DATA_PRIVACY)](sql-reference/classes/custom_classifier.md)
:   Allows you to define custom classifiers to extend your data classification capabilities.

[DOCUMENT_INTELLIGENCE (SNOWFLAKE.ML)](sql-reference/classes/document-intelligence.md)
:   Represents a Document AI model build.

[FORECAST (SNOWFLAKE.ML)](sql-reference/classes/forecast.md)
:   Represents a forecast model that produces a forecast for a single or multiple time series.

[TOP_INSIGHTS (SNOWFLAKE.ML)](sql-reference/classes/top-insights.md)
:   Allows you to determine the segments driving changes in a metric.
