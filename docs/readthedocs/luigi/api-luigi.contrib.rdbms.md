# luigi.contrib.rdbms

A common module for postgres like databases, such as postgres or redshift

Classes

`CopyToTable`(*args, **kwargs)

An abstract task for inserting a data set into RDBMS.

`Query`(*args, **kwargs)

An abstract task for executing an RDBMS query.

class luigi.contrib.rdbms.CopyToTable(**args*, ***kwargs*)

An abstract task for inserting a data set into RDBMS.

Usage:

Subclass and override the following attributes:

- 

host,

- 

database,

- 

user,

- 

password,

- 

table

- 

columns

- 

port