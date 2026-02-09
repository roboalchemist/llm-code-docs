# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-get-constraintdef.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_get_constraintdef()

## Overview

The <a href="https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-CATALOG" target="_blank">pg\_get\_constraintdef()</a> is a system catalog information function that retrieves the definition of a specific constraint in a human-readable format.

## Syntax

The syntax for the `pg_get_constraintdef()` function is as follows:

<pre><code>pg\_get\_constraintdef (constraint\_oid \[, pretty\_bool]) → NULL</code></pre>

## Parameters

The following parameters are required to execute this function:

* <a href="https://www.postgresql.org/docs/current/catalog-pg-constraint.html" target="_blank">constraint\_oid</a>:
  specifies the object identifier (OID) of the constraint for which you want to retrieve the definition
* <a href="https://www.postgresql.org/docs/current/datatype-boolean.html" target="_blank">pretty\_bool</a>:
  controls whether to format the output in a human-readable way

## Restrictions

* This function always returns `NULL` if there are no parameters specified
