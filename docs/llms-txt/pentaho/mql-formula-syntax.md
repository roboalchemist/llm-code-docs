# Source: https://docs.pentaho.com/pba-metadata-editor/mql-formula-syntax.md

# Source: https://docs.pentaho.com/pba-metadata-editor/pdia-9.3-metadata-editor/mql-formula-syntax.md

# Source: https://docs.pentaho.com/pba-metadata-editor/10.2-metadata-editor/mql-formula-syntax.md

# MQL formula syntax

You can apply global or user and role row-level constraints using MQL.

## Global constraints

You can use all of the standard operators, and any of the following functions when defining a global constraint:

| Function Name | Parameters                                     | Description                                                                                                                                                                                              |
| ------------- | ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `OR`          | Two or more Boolean expressions                | Returns `true` if one or more parameters are true.                                                                                                                                                       |
| `AND`         | Two or more Boolean expressions                | Returns `true` if all parameters are true.                                                                                                                                                               |
| `LIKE`        | Two                                            | Compares a column to a regular expression, using `%` as a wild card.                                                                                                                                     |
| `IN`          | Two or more                                    | Checks to see if the first parameter is in the following list of parameters.                                                                                                                             |
| `NOW`         | N/A                                            | The current date                                                                                                                                                                                         |
| `DATE`        | Three numeric parameters: Year, month, and day | The specified date                                                                                                                                                                                       |
| `DATEVALUE`   | One text parameter: year-month-day             | The specified date                                                                                                                                                                                       |
| `CASE`        | Two or more                                    | Evaluates the odd-numbered parameters, and returns the even numbered parameter values. If there are an odd number of parameters, the last parameter is returned if no other parameter evaluates to true. |
| `COALESCE`    | One or more                                    | Returns the first non-null parameter. If all parameters are null, the message in the last parameter is returned.                                                                                         |
| `DATEMATH`    | One expression                                 | Returns a date value based on a `DATEMATH` expression (see [DateMath Javadoc for full syntax](http://javadoc.pentaho.com/bi-platform/2.0.x/org/pentaho/platform/util/DateMath.html)).                    |

The following table contains examples of the functions:

<table data-header-hidden><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Function Name</td><td>Example</td></tr><tr><td><code>OR</code></td><td><pre><code>OR( [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME] = "EuroCars";
    [BT_CUSTOMERS.BC_CUSTOMERS_CREDITLIMIT] > 1000 ) 
</code></pre></td></tr><tr><td><code>AND</code></td><td><pre><code>AND( [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME] = "EuroCars";
     [BT_CUSTOMERS.BC_CUSTOMERS_CREDITLIMIT] > 1000 )
</code></pre></td></tr><tr><td><code>LIKE</code></td><td><pre><code>LIKE([BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME]; "%SMITH%")
</code></pre></td></tr><tr><td><code>IN</code></td><td><pre><code>IN([BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME]; "Adam Smith"; "Brian Jones")
</code></pre></td></tr><tr><td><code>NOW</code></td><td><pre><code>NOW()
</code></pre></td></tr><tr><td><code>DATE</code></td><td><pre><code>DATE(2008;4;15)
</code></pre></td></tr><tr><td><code>DATEVALUE</code></td><td><pre><code>DATEVALUE("2008-04-15")
</code></pre></td></tr><tr><td><code>CASE</code></td><td><pre><code>CASE( [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME] = "EuroCars"; "European Cars";
      [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME] = "AsiaCars"; "Asian Cars"; "Unknown Cars")
</code></pre></td></tr><tr><td><code>COALESCE</code></td><td><pre><code>COALESCE( [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERNAME];
          [BT_CUSTOMERS.BC_CUSTOMERS_CUSTOMERID]; "Customer is Null" )
</code></pre></td></tr><tr><td><code>DATEMATH</code></td><td><pre><code>DATEMATH("0:ME -1:DS")
</code></pre><p>This expression represents 00:00:00.000 on the day before the last day of the current month.</p></td></tr></tbody></table>

## User and role row-level constraints

The MQL Formula syntax for defining a user or role row constraint is:

```
[table.column] = "row"
```

The table and column are defined as part of a metadata business model. Here is an example that isolates access to data from the Sales department:

```
[BT_OFFICE.BC_DEPARTMENT]="Sales"
```

It is also possible to give or deny access to an entire role, or a single user, by selecting that user or role, then using a TRUE() or FALSE() Boolean for a constraint.
