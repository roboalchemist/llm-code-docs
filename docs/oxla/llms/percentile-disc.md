# Source: https://docs.oxla.com/sql-reference/sql-functions/aggregate-functions/ordered-set-aggregate-functions/percentile-disc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# PERCENTILE_DISC()

## Overview

`PERCENTILE_DISC()` is an ordered-set aggregate function used to compute discrete percentiles from a set of values.
The **discrete percentile** returns the first input value, which position in the ordering equals or exceeds the specified fraction, while **multiple discrete percentiles** return an array of results matching the shape of the fractions parameter, with each non-null element being replaced by the input value corresponding to that percentile.

<div>
  <h2>Syntax</h2>
  <p> The syntax for this function is as follows:</p>

  <Tabs>
    <Tab title="Discrete Percentile" onClick={() => handleTabChange('tab1')}>
      <div>
        <code>
          ```sql  theme={null}
          PERCENTILE_DISC(fraction) WITHIN GROUP (ORDER BY order_list)
          ```
        </code>

        <Note>If multiple values share the same rank at the specified percentile, `PERCENTILE_DISC()` will return the first one encountered in the ordering.</Note>
        <h2>Parameters </h2>
        <p>- `fraction`: decimal value between 0 and 1 representing the desired percentile (e.g. 0.25 for the 25th percentile)</p>
      </div>
    </Tab>

    <Tab title="Multiple Discrete Percentile" onClick={() => handleTabChange('tab2')}>
      <div>
        <code>
          ```sql  theme={null}
          PERCENTILE_DISC(fractions) WITHIN GROUP (ORDER BY order_list)
          ```
        </code>

        <Note>If multiple values share the same rank at the specified percentile, `PERCENTILE_DISC` will return the first one encountered in the ordering.</Note>
        <h2>Parameters</h2>
        <p>- `fractions`: array of decimal values between 0 and 1 representing the desired percentiles (e.g. `ARRAY[0.25, 0.50, 0.75, 0.90]`)</p>
      </div>
    </Tab>
  </Tabs>
</div>

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

The query below calculates the quartile, median and the third quartile of film lengths:

```sql  theme={null}
SELECT rating, percentile_disc(ARRAY[0.25, 0.5, 0.75]) WITHIN GROUP (ORDER BY length) AS "quartiles" FROM film
GROUP BY rating;
```

By executing the code above, we will get the following output:

```sql  theme={null}
 rating |   quartiles   
--------+---------------
 G      | {54,77,125}
 PG     | {106,121,137}
 PG-13  | {47,83,142}
 NC-17  | {131,150,176}
(4 rows)
```
