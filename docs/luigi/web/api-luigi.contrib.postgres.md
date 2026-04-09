# luigi.contrib.postgres

Implements a subclass of `Target` that writes data to Postgres.
Also provides a helper task to copy data into a Postgres table.

Functions

`db_error_code`(exception)

`update_error_codes`()

Classes

`CopyToTable`(*args, **kwargs)

Template task for inserting a data set into Postgres

`MultiReplacer`(replace_pairs)

Object for one-pass replace of multiple words

`PostgresQuery`(*args, **kwargs)

Template task for querying a Postgres compatible database

`PostgresTarget`(host, database, user, ...[, port])

Target for a resource in Postgres.

luigi.contrib.postgres.update_error_codes()

luigi.contrib.postgres.db_error_code(*exception*)

class luigi.contrib.postgres.MultiReplacer(*replace_pairs*)

Object for one-pass replace of multiple words

Substituted parts will not be matched against other replace patterns, as opposed to when using multipass replace.
The order of the items in the replace_pairs input will dictate replacement precedence.

Constructor arguments:
replace_pairs – list of 2-tuples which hold strings to be replaced and replace string

Usage:

```
>>> replace_pairs = [("a", "b"), ("b", "c")]
>>> MultiReplacer(replace_pairs)("abcd")
'bccd'
>>> replace_pairs = [("ab", "x"), ("a", "x")]
>>> MultiReplacer(replace_pairs)("ab")
'x'
>>> replace_pairs.reverse()
>>> MultiReplacer(replace_pairs)("ab")
'xb'

```