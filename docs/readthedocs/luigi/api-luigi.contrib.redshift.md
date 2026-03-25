# luigi.contrib.redshift

Classes

`KillOpenRedshiftSessions`(*args, **kwargs)

An task for killing any open Redshift sessions in a given database.

`RedshiftManifestTask`(*args, **kwargs)

Generic task to generate a manifest file that can be used in S3CopyToTable in order to copy multiple files from your s3 folder into a redshift table at once.

`RedshiftQuery`(*args, **kwargs)

Template task for querying an Amazon Redshift database

`RedshiftTarget`(host, database, user, ...[, port])

Target for a resource in Redshift.

`RedshiftUnloadTask`(*args, **kwargs)

Template task for running UNLOAD on an Amazon Redshift database

`S3CopyJSONToTable`(*args, **kwargs)

Template task for inserting a JSON data set into Redshift from s3.

`S3CopyToTable`(*args, **kwargs)

Template task for inserting a data set into Redshift from s3.

class luigi.contrib.redshift.RedshiftTarget(*host*, *database*, *user*, *password*, *table*, *update_id*, *port=None*)

Target for a resource in Redshift.

Redshift is similar to postgres with a few adjustments
required by redshift.

Args:

host (str): Postgres server address. Possibly a host:port string.
database (str): Database name
user (str): Database user
password (str): Password for specified user
update_id (str): An identifier for this data set
port (int): Postgres server port.

marker_table = 'table_updates'

DEFAULT_DB_PORT = 5439

use_db_timestamps = False

class luigi.contrib.redshift.S3CopyToTable(**args*, ***kwargs*)

Template task for inserting a data set into Redshift from s3.

Usage:

- 

Subclass and override the required attributes:

  - 

host,

  - 

database,

  - 

user,

  - 

password,

  - 

table,

  - 

columns,

  - 

s3_load_path.

- 

You can also override the attributes provided by the
CredentialsMixin if they are not supplied by your
configuration or environment variables.

abstractmethod s3_load_path()

Override to return the load path.

abstract property copy_options

Add extra copy options, for example:

- 

TIMEFORMAT ‘auto’

- 

IGNOREHEADER 1

- 

TRUNCATECOLUMNS

- 

IGNOREBLANKLINES

- 

DELIMITER ‘   ‘

property prune_table

Override to set equal to the name of the table which is to be pruned.
Intended to be used in conjunction with prune_column and prune_date
i.e. copy to temp table, prune production table to prune_column with a date greater than prune_date, then insert into production table from temp table

property prune_column

Override to set equal to the column of the prune_table which is to be compared
Intended to be used in conjunction with prune_table and prune_date
i.e. copy to temp table, prune production table to prune_column with a date greater than prune_date, then insert into production table from temp table

property prune_date

Override to set equal to the date by which prune_column is to be compared
Intended to be used in conjunction with prune_table and prune_column
i.e. copy to temp table, prune production table to prune_column with a date greater than prune_date, then insert into production table from temp table

property table_attributes

Add extra table attributes, for example:

DISTSTYLE KEY
DISTKEY (MY_FIELD)
SORTKEY (MY_FIELD_2, MY_FIELD_3)

property table_constraints

Add extra table constraints, for example:

PRIMARY KEY (MY_FIELD, MY_FIELD_2)
UNIQUE KEY (MY_FIELD_3)

property do_truncate_table

Return True if table should be truncated before copying new data in.

do_prune()

Return True if prune_table, prune_column, and prune_date are implemented.
If only a subset of prune variables are override, an exception is raised to remind the user to implement all or none.
Prune (data newer than prune_date deleted) before copying new data in.

property table_type

Return table type (i.e. ‘temp’).

property queries

Override to return a list of queries to be executed in order.

truncate_table(*connection*)

prune(*connection*)

create_schema(*connection*)

Will create the schema in the database

create_table(*connection*)

Override to provide code for creating the target table.

By default it will be created using types (optionally)
specified in columns.

If overridden, use the provided connection object for
setting up the table in order to create the table and
insert data using the same transaction.

run()

If the target table doesn’t exist, self.create_table
will be called to attempt to create the table.

copy(*cursor*, *f*)

Defines copying from s3 into redshift.

If both key-based and role-based credentials are provided, role-based will be used.

output()

Returns a RedshiftTarget representing the inserted dataset.

Normally you don’t override this.

does_schema_exist(*connection*)

Determine whether the schema already exists.

does_table_exist(*connection*)

Determine whether the table already exists.

init_copy(*connection*)

Perform pre-copy sql - such as creating table, truncating, or removing data older than x.

post_copy(*cursor*)

Performs post-copy sql - such as cleansing data, inserting into production table (if copied to temp table), etc.

post_copy_metacolums(*cursor*)

Performs post-copy to fill metadata columns.

class luigi.contrib.redshift.S3CopyJSONToTable(**args*, ***kwargs*)

Template task for inserting a JSON data set into Redshift from s3.

Usage:

- 

Subclass and override the required attributes:

  - 

host,

  - 

database,

  - 

user,

  - 

password,

  - 

table,

  - 

columns,

  - 

s3_load_path,

  - 

jsonpath,

  - 

copy_json_options.