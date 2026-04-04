# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/col-description.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# col_description()

## Overview

The <a href="https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-COMMENT" target="_blank">col\_description()</a> is a comment information function that retrieves the comment associated with a specified table column.

## Syntax

The syntax for the `col_description()` function is as follows:

<pre><code>col\_description (table\_oid, column\_number) → NULL</code></pre>

## Parameters

The following parameters are required to execute this function:

* <a href="https://www.postgresql.org/docs/current/datatype-oid.html" target="_blank">table\_oid</a>:
  specifies the object identifier (OID) of the table containing the column for which you want to retrieve the comment
* <a href="https://www.postgresql.org/docs/current/datatype-numeric.html#DATATYPE-INT" target="_blank">column\_number</a>: indicates the ordinal position of the column within the table (starting from 1 for the first column)

<Note>It is important to note that the column number must be provided as an object identifier (OID), which can be achieved by casting the table name to `regclass`</Note>

## Restrictions

* This function always returns `NULL` if there are no parameters specified
