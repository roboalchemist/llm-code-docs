# Source: https://docs.oxla.com/sql-reference/sql-functions/aggregate-functions/ordered-set-aggregate-functions/mode.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# MODE()

## Overview

`MODE()` is an ordered-set aggregate function that returns the most frequently occurring value (the mode) from a set of values.

## Syntax

```sql  theme={null}
MODE() WITHIN GROUP (ORDER BY order_list)
```

<Note> Null values are ignored during the calculation. If null is the most frequent value, the function will return the second most common value.</Note>

## Parameters

* `()`: this function takes no parameters, but empty parentheses is required

## Example

For the needs of this section we will use a simplified version of the `film` table from the
<a href="https://www.postgresql.org/ftp/projects/pgFoundry/dbsamples/pagila/pagila/" target="_blank">Pagila database</a>, that will contain only the `title`, `length` and `rating` columns.

```sql  theme={null}
DROP TABLE IF EXISTS film;
CREATE TABLE film (
  title text NOT NULL,
  length int,
  rating text
);
INSERT INTO film(title, length, rating) VALUES
  ('ATTRACTION NEWTON', 83, 'PG-13'),
  ('CHRISTMAS MOONSHINE', 150, 'NC-17'),
  ('DANGEROUS UPTOWN', 121, 'PG'),
  ('KILL BROTHERHOOD', 54, 'G'),
  ('HALLOWEEN NUTS', 47, 'PG-13'),
  ('HOURS RAGE', 122, 'NC-17'),
  ('PIANIST OUTFIELD', 136, 'NC-17'),
  ('PICKUP DRIVING', 77, 'G'),
  ('INDEPENDENCE HOTEL', 157, 'NC-17'),
  ('PRIVATE DROP', 106, 'PG'),
  ('SAINTS BRIDE', 125, 'G'),
  ('FOREVER CANDIDATE', 131, 'NC-17'),
  ('MILLION ACE', 142, 'PG-13'),
  ('SLEEPY JAPANESE', 137, 'PG'),
  ('WRATH MILE', 176, 'NC-17'),
  ('YOUTH KICK', 179, 'NC-17'),
  ('CLOCKWORK PARADISE', 143, 'PG-13');
```

The query below retrieves the most frequent ratings found in the film table:

```sql  theme={null}
SELECT MODE()
  WITHIN GROUP (ORDER BY rating)
FROM film; 
```

By executing the code above we will get the following output:

```sql  theme={null}
| mode  |
|-------|
| NC-17 |
```
