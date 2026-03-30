# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results/pentaho-data-service-sql-support-reference-and-other-development-considerations/supported-sql-literals.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/advanced-topics-pentaho-data-integration-overview/pentaho-data-services/test-a-pentaho-data-service/examine-test-results/pentaho-data-service-sql-support-reference-and-other-development-considerations/supported-sql-literals.md

# Supported SQL literals

The Pentaho Data Service supports the following literals:

* Strings have single quotation marks around them. The escape character for a single quote is another single quote, like this `''`.
* Dates have square brackets around them. The following formats are supported: `[yyyy/MM/dd HH:mm:ss.SSS]`, `[yyyy/MM/dd HH:mm:ss]`, and `[yyyy/MM/dd]`.
* For an `IN` list in a SQL statement, the date formats can have single quotation marks around them and dashes that replace slashes, like this: `SELECT * FROM BUILDS WHERE BuildDate IN ('2015-03-18', '2015-03-22')`. Note that you cannot surround a date format with a bracket date in an `IN` list.
* `Number` and `BigNumber` should have no grouping symbols. Use a period to represent a decimal, like this: `123.45`.
* Integers should contain only digits.
* Boolean values can be TRUE or FALSE.
