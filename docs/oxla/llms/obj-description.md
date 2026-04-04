# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/obj-description.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# obj_description()

## Overview

The <a href="https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-COMMENT" target="_blank">obj\_description()</a> is a comment information function that returns the comment associated with a specific database object.

## Syntax

The syntax for the `obj_description()` function is as follows:

<pre><code>obj\_description (object\_oid, catalog\_name) → NULL</code></pre>

## Parameters

The following parameters are required to execute this function:

* <a href="https://www.postgresql.org/docs/current/datatype-oid.html" target="_blank">object\_oid</a>:
  specifies the object identifier (OID) of the database object for which you want to retrieve the comment
* <a href="https://www.postgresql.org/docs/current/catalogs.html" target="_blank">catalog\_name</a>:
  specifies the name of the system catalog that contains the object

## Restrictions

* This function always returns `NULL` if there are no parameters specified
