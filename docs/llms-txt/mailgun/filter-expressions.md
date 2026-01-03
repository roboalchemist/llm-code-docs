# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/events/filter-expressions.md

# Filter Expression

Possible filtering expressions are listed below:

| Expression | Description |
|  --- | --- |
| foo bar | Matches field values that contain both term `foo` and term `bar`. |
| foo AND bar | Same as above. |
| foo OR bar | Matches field values that contain either term `foo` or term `bar`. |
| "foo bar" | Matches field values that literally contain `foo bar`. |
| NOT foo | Matches field values that do not contain term `foo`. |
| >10000 | Matches values that greater than 10000. This filter can be applied to numeric fields only. |
| >10000 <20000 | Matches values that are greater than 10000 and less than 20000. This filter can be applied to numeric fields only. |


info
Note that more than one expression can be used as a filter value and parentheses can be used to specify grouping. E.g.: (Hello AND NOT Rachel) OR (Farewell AND Monica).