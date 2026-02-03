# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/pg-get-statisticsobjdef-columns.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# pg_get_statisticsobjdef_columns()

## Overview

The <a href="https://www.postgresql.org/docs/current/functions-info.html#FUNCTIONS-INFO-CATALOG" target="_blank">pg\_get\_statisticsobjdef\_columns()</a> is a system catalog information function that retrieves information about the columns associated with an extended statistics object.

## Syntax

The syntax for the `pg_get_statisticsobjdef_columns()` function is as follows:

<pre><code>pg\_get\_statisticsobjdef\_columns() → NULL</code></pre>

## Restrictions

* This function always returns `NULL` if there are no parameters specified
