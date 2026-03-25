# Source: https://docs.pentaho.com/analyzer-external-javascript-api/using-pentaho-analyzer-external-javascript-api-cp/analyzer-filters-pentaho-analyzer-external-javascript-api.md

# Analyzer Filters

Filters are used to restrict or limit data in a report, building the report to show only the information you want to view.

## Filter Type Levels

Within each dimension, you can have String, Date, and Numeric level filters.

The following type levels are supported:

* **String Levels**
  * Include and Exclude
  * Contains and Does Not Contain
* **Date Levels**
  * Include and Exclude
  * Before, After, and Between
  * All relative time filters such as 'Current Year' or '3 Years Ago'
* **Numeric Levels**
  * Include and Exclude
  * Contains and Does Not Contain
  * Greater Than (or Equals), Less Than (or Equals), and Between

The following operators are supported:

* `EQUAL`
* `NOT_EQUAL`
* `CONTAIN`
* `NOT_CONTAIN`
* `BEFORE`
* `AFTER`
* `BETWEEN`
* `TIME_AGO`
* `TIME_AHEAD`
* `TIME_YAGO`
* `TIME_RANGE_PREV`
* `TIME_RANGE_NEXT`
* `NUMERIC_LESS_THAN`
* `NUMERIC_GREATER_THAN`
* `NUMERIC_LESS_THAN_EQUAL`
* `NUMERIC_GREATER_THAN_EQUAL`
* `NUMERIC_BETWEEN`

## Filter Measure Values

Within each dimension, you can have Measure value filters.

The following Measure value types are supported:

* Top N
* Greater Than/Less Than filters

The following operators are supported:

* `LESS_THAN`
* `GREATER_THAN`
* `LESS_THAN_EQUAL`
* `GREATER_THAN_EQUAL`
* `EQUAL`
* `NOT_EQUAL`
* `BETWEEN`
* `IS_NOT_EMPTY`
* `TOP`
* `BOTTOM`
* `TOP_BOTTOM`

**Note:** The UI labels for these operators can be translated in the message.properties file. These labels appear in the filter dialog, filter summary and on the last page of exported reports

## Filter Logic

Each dimension is filtered independently and the results are logically AND'd together. Level filters are always applied before measure value filters and the two groups of filters are AND'd together. Within level filters, the following operators are OR'd together: Include, Contains, Before, After, Between and relative time filters. These filters are then AND'd together with the Exclude and Does Not Contain operators.

Here's a visual representation:

```javascript
(
  Include OR Contain OR Before OR After OR Between OR Any Time Filter
) AND (
  Exclude AND Not Contain
)

```

The above filters are then AND'd with any numeric filters:

```javascript
AND (Top 10 AND Greater Than)

```

Within a Contain or Not Contain operator, the individual expressions are OR'd together.
