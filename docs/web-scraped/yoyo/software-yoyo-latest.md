# Source: https://ollycope.com/software/yoyo/latest/

Title: Yoyo database migrations — yoyo-migrations 9.0.0.dev0 documentation

URL Source: https://ollycope.com/software/yoyo/latest/

Markdown Content:
[Source repository and issue tracker](https://sr.ht/~olly/yoyo)

Yoyo is a database schema migration tool. Migrations are written as SQL files or Python scripts that define a list of migration steps. They can be as simple as this:

# file: migrations/0001.create-foo.py

from yoyo import step
steps = [
   step(
       "CREATE TABLE foo (id INT, bar VARCHAR(20), PRIMARY KEY (id))",
       "DROP TABLE foo"
   )
]

Installation and project setup[¶](https://ollycope.com/software/yoyo/latest/#installation-and-project-setup "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

Install yoyo-migrations from PyPI:

pip install yoyo-migrations

Initialize yoyo for your project, supplying a database connection string and migrations directory name, for example:

yoyo init --database sqlite:///mydb.sqlite3 migrations

This will create a new, empty directory called `migrations` and install a `yoyo.ini` configuration file in the current directory. The configuration file will contain any database credentials supplied on the command line. If you do not wish this to happen, then omit the `--database` argument from the command.

Create a new migration by running `yoyo new`. By default, a Python format file is generated, use `--sql` if you prefer SQL format:

yoyo new --sql

An editor will open with a template migration file. Add a comment explaining what the migration does followed by the SQL commands, for example:

-- Create table foo
-- depends:

CREATE TABLE foo (
 a int
);

Save and exit, and the new migration file will be created. Check your migration has been created with `yoyo list` and apply it with `yoyo apply`:

$ yoyo list
$ yoyo apply

Command line usage[¶](https://ollycope.com/software/yoyo/latest/#command-line-usage "Link to this heading")
-----------------------------------------------------------------------------------------------------------

You can see the list of available commands by running:

$ yoyo --help

You can check options for any command with `yoyo <command> --help`

### yoyo new[¶](https://ollycope.com/software/yoyo/latest/#yoyo-new "Link to this heading")

Start a new migration. `yoyo new` will create a new migration file and opens it your configured editor.

By default a Python formation migration will be created. To use the simpler SQL format, specify `--sql`.

yoyo new -m "Add column to foo"
yoyo new --sql

### yoyo list[¶](https://ollycope.com/software/yoyo/latest/#yoyo-list "Link to this heading")

List available migrations. Each migration will be prefixed with one of `U` (unapplied) or `A` (applied).

### yoyo apply[¶](https://ollycope.com/software/yoyo/latest/#yoyo-apply "Link to this heading")

Apply migrations to the target database. By default this will prompt you for each unapplied migration. To turn off prompting use `--batch` or specify `batch_mode = on` in `yoyo.ini`.

### yoyo rollback[¶](https://ollycope.com/software/yoyo/latest/#yoyo-rollback "Link to this heading")

By default this will prompt you for each applied migration, starting with the most recently applied.

If you wish to rollback a single migration, specify the migration with the `-r`/`--revision` flag. Note that this will also cause any migrations that depend on the selected migration to be rolled back.

### yoyo reapply[¶](https://ollycope.com/software/yoyo/latest/#yoyo-reapply "Link to this heading")

Reapply (ie rollback then apply again) migrations. As with [yoyo rollback](https://ollycope.com/software/yoyo/latest/#yoyo-rollback), you can select a target migration with `-r`/`--revision`

### yoyo develop[¶](https://ollycope.com/software/yoyo/latest/#yoyo-develop "Link to this heading")

Apply any unapplied migrations without prompting.

If there are no unapplied migrations, rollback and reapply the most recent migration. Use `yoyo develop -n <n>` to act on just the _n_ most recently applied migrations.

### yoyo mark[¶](https://ollycope.com/software/yoyo/latest/#yoyo-mark "Link to this heading")

Mark one or more migrations as applied, without actually applying them.

### yoyo unmark[¶](https://ollycope.com/software/yoyo/latest/#yoyo-unmark "Link to this heading")

Unmark one or more migrations as unapplied, without actually rolling them back.

Connecting to a database[¶](https://ollycope.com/software/yoyo/latest/#connecting-to-a-database "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Database connections are specified using a URL, for example:

yoyo list --database postgresql://scott:tiger@localhost/mydatabase

The protocol part of the URL (the part before `://`) is used to specify the backend. Yoyo provides the following core backends:

* `postgresql` ([psycopg2](https://pypi.org/project/psycopg2/))

* `postgresql+psycopg` ([psycopg3](https://pypi.org/project/psycopg/))

* `mysql` ([pymysql](https://pypi.org/project/pymysql/))

* `mysql+mysqldb` ([mysqlclient](https://pypi.org/project/mysqlclient/))

* `sqlite` ([sqlite3](https://docs.python.org/3/library/sqlite3.html))

And these backends have been contributed and are bundled with yoyo:

* `odbc` ([pyodbc](https://pypi.org/project/pyodbc/))

* `oracle` ([cx_Oracle](https://pypi.org/project/cx-Oracle/))

* `snowflake` ([snowflake](https://pypi.org/project/snowflake-connector-python/))

* `redshift` ([psycopg2](https://pypi.org/project/psycopg2/))

How other parts of the URL are interpreted depends on the underlying backend and the DB-API driver used. The host part especially tends to be interpreted differently by drivers. A few of the more important differences are listed below.

### MySQL connections[¶](https://ollycope.com/software/yoyo/latest/#mysql-connections "Link to this heading")

[mysqlclient](https://pypi.org/project/mysqlclient/) and [pymysql](https://pypi.org/project/pymysql/) have different ways to interpret the `host` part of the connection URL:

* With [mysqlclient](https://pypi.org/project/mysqlclient/) (`mysql+mysqldb://`), setting the host to `localhost` or leaving it empty causes the driver to attempt a local unix socket connection.

* In [pymysql](https://pypi.org/project/pymysql/) (`mysql://`), the driver will attempt a tcp connection in both cases. Specify a unix socket connection with the `unix_socket` option (eg `?unix_socket=/tmp/mysql.sock`)

To enable SSL, specify `?ssl=1` and the following options as required:

* `sslca`

* `sslcapath`

* `sslcert`

* `sslkey`

* `sslcipher`

These options correspond to the `ca`, `capath`, `cert`, `key` and `cipher` options used by [mysql_ssl_set](https://dev.mysql.com/doc/c-api/8.0/en/mysql-ssl-set.html).

Example configurations:

# MySQL: Network database connection

database = mysql://scott:tiger@localhost/mydatabase

# MySQL: unix socket connection

database = mysql://scott:tiger@/mydatabase?unix_socket=/tmp/mysql.sock

# MySQL with the MySQLdb driver (instead of pymysql)

database = mysql+mysqldb://scott:tiger@localhost/mydatabase

# MySQL with SSL/TLS enabled

database = mysql+mysqldb://scott:tiger@localhost/mydatabase?ssl=yes&sslca=/path/to/cert

### PostgreSQL connections[¶](https://ollycope.com/software/yoyo/latest/#postgresql-connections "Link to this heading")

The psycopg family of drivers will use a unix socket if the host is left empty (or the value of `PGHOST` if this is set in your environment). Otherwise it will attempt a tcp connection to the specified host.

To force a unix socket connection leave the host part of the URL empty and provide a `host` option that points to the directory containing the socket (eg `postgresql:///mydb?host=/path/to/socket/`).

The postgresql backends also allow a custom schema to be selected by specifying a `schema` option, eg `postgresql://…/mydatabase?schema=myschema`.

Example configurations:

database = postgresql://scott:tiger@localhost/mydatabase

# unix socket connection

database = postgresql://scott:tiger@/mydatabase

# unix socket at a non-standard location and port number

database = postgresql://scott:tiger@/mydatabase?host=/var/run/postgresql&port=5434

# PostgreSQL with psycopg 3 driver

database = postgresql+psycopg://scott:tiger@localhost/mydatabase

# Changing the default schema

database = postgresql://scott:tiger@/mydatabase?schema=some_schema

### SQLite connections[¶](https://ollycope.com/software/yoyo/latest/#sqlite-connections "Link to this heading")

The SQLite backend ignores everything in the connection URL except the database name, which should be a filename, or the special value `:memory:` for an in-memory database.

3 slashes are required to specify a relative path:

sqlite:///mydb.sqlite

and 4 for an absolute path on unix-like platforms:

sqlite:////home/user/mydb.sqlite

### Password security[¶](https://ollycope.com/software/yoyo/latest/#password-security "Link to this heading")

You can specify your database username and password either as part of the database connection string on the command line (exposing your database password in the process list) or in a configuration file where other users may be able to read it.

The `-p` or `--prompt-password` flag causes yoyo to prompt for a password, helping prevent your credentials from being leaked.

Migration files[¶](https://ollycope.com/software/yoyo/latest/#migration-files "Link to this heading")
-----------------------------------------------------------------------------------------------------

The migrations directory contains a series of migration scripts. Each migration script is a Python (`.py`) or SQL file (`.sql`).

The name of each file without the extension is used as the migration’s unique identifier. You may include migrations from multiple sources, but identifiers are assumed to be globally unique, so it’s wise to choose a unique prefix for you project (eg `<project-name>-0001-migration.sql`) or use the `yoyo new` command to generate a suitable filename.

Migrations scripts are run in dependency then filename order.

Each migration file is run in a single transaction where this is supported by the database.

Yoyo creates tables in your target database to track which migrations have been applied. By default these are:

* `_yoyo_migration`

* `_yoyo_log`

* `_yoyo_version`

* `yoyo_lock`

### Migrations as Python scripts[¶](https://ollycope.com/software/yoyo/latest/#migrations-as-python-scripts "Link to this heading")

A migration script written in Python has the following structure:

#

# file: migrations/0001_create_foo.py

#

from yoyo import step

 __depends__  = {"0000.initial-schema"}

steps = [
  step(
      "CREATE TABLE foo (id INT, bar VARCHAR(20), PRIMARY KEY (id))",
      "DROP TABLE foo",
  ),
  step(
      "ALTER TABLE foo ADD COLUMN baz INT NOT NULL"
  )
]

The `step` function may take up to 3 arguments:

* `apply`: an SQL query (or Python function, see below) to apply the migration step.

* `rollback`: (optional) an SQL query (or Python function) to rollback the migration step.

* `ignore_errors`: (optional, one of `"apply"`, `"rollback"` or `"all"`) causes yoyo to ignore database errors in either the apply stage, rollback stage or both.

#### Migration steps as Python functions[¶](https://ollycope.com/software/yoyo/latest/#migration-steps-as-python-functions "Link to this heading")

If SQL is not flexible enough, you may supply a Python function as either or both of the `apply` or `rollback` arguments of `step`. Each function should take a database connection as its only argument:

#

# file: migrations/0001_create_foo.py

#

from yoyo import step

def apply_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        # query to perform the migration
    )

def rollback_step(conn):
    cursor = conn.cursor()
    cursor.execute(
        # query to undo the above
    )

steps = [
  step(apply_step, rollback_step)
]

#### Dependencies[¶](https://ollycope.com/software/yoyo/latest/#dependencies "Link to this heading")

Migrations may declare dependencies on other migrations via the `__depends__` attribute:

#

# file: migrations/0002.modify-foo.py

#

 __depends__  = {'0000.initial-schema', '0001.create-foo'}

steps = [

# migration steps

]

If you use the `yoyo new` command the `__depends__` attribute will be auto populated for you.

### Migrations as SQL scripts[¶](https://ollycope.com/software/yoyo/latest/#migrations-as-sql-scripts "Link to this heading")

An SQL migration script files should be named `<migration-name>.sql` and contain the one or more SQL statements required to apply the migration.

--
-- file: migrations/0001.create-foo.sql
--

CREATE TABLE foo (id INT, bar VARCHAR(20), PRIMARY KEY (id));

SQL rollback steps should be saved in a separate file named `<migration-name>.rollback.sql`:

--
-- file: migrations/0001.create-foo.rollback.sql
--

DROP TABLE foo;

#### Dependencies[¶](https://ollycope.com/software/yoyo/latest/#id1 "Link to this heading")

A structured SQL comment may be used to specify dependencies as a space separated list:

-- depends: 0000.initial-schema 0001.create-foo

ALTER TABLE foo ADD baz INT;

### Post-apply hook[¶](https://ollycope.com/software/yoyo/latest/#post-apply-hook "Link to this heading")

It can be useful to have a script that is run after every successful migration. For example you could use this to update database permissions or re-create views.

To do this, create a special migration file called `post-apply.py` or `post-apply.sql`. This file should have the same format as any other migration file.

Configuration file[¶](https://ollycope.com/software/yoyo/latest/#configuration-file "Link to this heading")
-----------------------------------------------------------------------------------------------------------

Yoyo looks for a configuration file named `yoyo.ini` in the current working directory or any ancestor directory.

If no configuration file is found `yoyo` will prompt you to create one, populated from the current command line arguments.

Using a configuration file saves repeated typing, avoids your database username and password showing in process listings and lessens the risk of accidentally running migrations against the wrong database (ie by re-running an earlier `yoyo` entry in your command history when you have moved to a different directory).

If you do not want a config file to be loaded add the `--no-config-file` parameter to the command line options.

The configuration file may contain the following options:

[DEFAULT]

# List of migration source directories. "%(here)s" is expanded to the

# full path of the directory containing this ini file

sources = %(here)s/migrations %(here)s/lib/module/migrations

# Target database

database = postgresql://scott:tiger@localhost/mydb

# Verbosity level. Goes from 0 (least verbose) to 3 (most verbose)

verbosity = 3

# Disable interactive features

batch_mode = on

# Editor to use when starting new migrations

# "{}" is expanded to the filename of the new migration

editor = /usr/local/bin/vim -f {}

# An arbitrary command to run after a migration has been created

# "{}" is expanded to the filename of the new migration

post_create_command = hg add {}

# A prefix to use for generated migration filenames

prefix = myproject_

### Config file inheritance and includes[¶](https://ollycope.com/software/yoyo/latest/#config-file-inheritance-and-includes "Link to this heading")

The special `%inherit` and `%include` directives allow config file inheritance and inclusion:

#

# file: yoyo-defaults.ini

#

[DEFAULT]
sources = %(here)s/migrations

#

# file: yoyo.ini

#

[DEFAULT]

; Inherit settings from yoyo-defaults.ini
;
; Settings in inherited files are processed first and may be overridden by
; settings in this file
%inherit = yoyo-defaults.ini

; Include settings from yoyo-local.ini
;
; Included files are processed after this file and may override the settings
; in this file
%include = yoyo-local.ini

; Use '?' to avoid raising an error if the file does not exist
%inherit = ?yoyo-defaults.ini

database = sqlite:///%(here)s/mydb.sqlite

### Substitutions and environment variables[¶](https://ollycope.com/software/yoyo/latest/#substitutions-and-environment-variables "Link to this heading")

The special variable `%(here)s` will be substituted with the directory name of the config file.

Environment variables can be substituted with the same syntax, eg `%(HOME)s`.

Substitutions are case-insensitive so for example `%(HOME)s` and `%(home)s` will both refer to the same variable.

### Migration sources[¶](https://ollycope.com/software/yoyo/latest/#migration-sources "Link to this heading")

Yoyo reads migration scripts from the directories specified in the `sources` config option. Paths may include glob patterns, for example:

[DEFAULT]
sources =
 %(here)s/migrations
 %(here)s/src/*/migrations

You may also read migrations from installed python packages, by supplying a path in the special form `package:<package-name>:<path-to-migrations-dir>`, for example:

[DEFAULT]
sources = package:myapplication:data/migrations

Transactions[¶](https://ollycope.com/software/yoyo/latest/#transactions "Link to this heading")
-----------------------------------------------------------------------------------------------

Each migration runs in a separate transaction. Savepoints are used to isolate steps within each migration.

If an error occurs during a step and the step has `ignore_errors` set, then that individual step will be rolled back and execution will pick up from the next step. If `ignore_errors` is not set then the entire migration will be rolled back and execution stopped.

Note that some databases (eg MySQL) do not support rollback on DDL statements (eg `CREATE ...` and `ALTER ...` statements). For these databases you may need to manually intervene to reset the database state should errors occur in your migration.

Using `group` allows you to nest steps, giving you control of where rollbacks happen. For example:

group([
  step("ALTER TABLE employees ADD tax_code TEXT"),
  step("CREATE INDEX tax_code_idx ON employees (tax_code)")
], ignore_errors='all')
step("UPDATE employees SET tax_code='C' WHERE pay_grade < 4")
step("UPDATE employees SET tax_code='B' WHERE pay_grade >= 6")
step("UPDATE employees SET tax_code='A' WHERE pay_grade >= 8")

### Disabling transactions[¶](https://ollycope.com/software/yoyo/latest/#disabling-transactions "Link to this heading")

Disable transaction handling within a migration by setting `__transactional__ = False`, eg:

 __transactional__  = False

step("CREATE DATABASE mydb", "DROP DATABASE mydb")

Or for SQL migrations:

-- transactional: false

CREATE DATABASE mydb

This feature is only tested against the PostgreSQL and SQLite backends.

#### PostgreSQL[¶](https://ollycope.com/software/yoyo/latest/#postgresql "Link to this heading")

In PostgreSQL it is an error to run certain statements inside a transaction block. These include:

CREATE DATABASE ...
ALTER TYPE ... ADD VALUE

Using `__transactional__ = False` allows you to run these within a migration

#### SQLite[¶](https://ollycope.com/software/yoyo/latest/#sqlite "Link to this heading")

In SQLite, the default transactional behavior may prevent other tools from accessing the database for the duration of the migration. Using `__transactional__ = False` allows you to work around this limitation.

Calling Yoyo from Python code[¶](https://ollycope.com/software/yoyo/latest/#calling-yoyo-from-python-code "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

The following example shows how to apply migrations from inside python code:

from yoyo import read_migrations
from yoyo import get_backend

backend = get_backend('postgresql://myuser@localhost/mydatabase')
migrations = read_migrations('path/to/migrations')

with backend.lock():

    # Apply any outstanding migrations
    backend.apply_migrations(backend.to_apply(migrations))

    # Rollback all migrations
    backend.rollback_migrations(backend.to_rollback(migrations))

Adding custom backends[¶](https://ollycope.com/software/yoyo/latest/#adding-custom-backends "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

Backends are discovered using Python importlib.metadata entry points.

To add a custom backend, create a python package containing a subclass of `yoyo.backends.base.DatabaseBackend` and configure it in the package metadata (typically in `setup.cfg`), for example:

[options.entry_points]

yoyo.backends =
 mybackend = mypackage:MyBackend

Use the backend by specifying `'mybackend'` as the driver protocol:

.. code:: sh

 yoyo apply --database my_backend://...

Contributing[¶](https://ollycope.com/software/yoyo/latest/#contributing "Link to this heading")
-----------------------------------------------------------------------------------------------

### Report an issue[¶](https://ollycope.com/software/yoyo/latest/#report-an-issue "Link to this heading")

Use the yoyo-migrations [issue tracker](https://todo.sr.ht/~olly/yoyo) to report issues.

There is also a [mailing list](https://lists.sr.ht/~olly/yoyo) where you can post questions or suggestions.

### Pull requests[¶](https://ollycope.com/software/yoyo/latest/#pull-requests "Link to this heading")

Yoyo-migrations is developed on sourcehut and uses a mailing list to review commits for inclusion into the project.

To send commits to the mailing list:

1. Clone the repository: `hg clone https://hg.sr.ht/~olly/yoyo`

2. Take care to commit your work in logically separate changes. Use `hg commit -i` to commit your work in logically separate changes. Make sure each commit has a meaningful message.

3. When you are ready to send your commits, use `hg config --edit` to add the following lines to your user Mercurial configuration file:

> [extensions]
> patchbomb =
>
> [email]
> from = Your Name <you@example.org>
> method = smtp
>
> [smtp]
> host = mail.example.org
> port = 587
> tls = smtps
> username = you@example.org
>
>
> Then use `hg config --local` to add the following lines to the repository configuration file:
>
>
>
> [email]
> to = <~olly/yoyo@lists.sr.ht>

1. Run `hg mail -o` to send your commits by email. This command will send all your commits; if you want to send just a subset, refer to the [hg email docs](https://www.mercurial-scm.org/doc/hg.1.html#email).

For more detailed instructions, see here: [https://man.sr.ht/hg.sr.ht/email.md](https://man.sr.ht/hg.sr.ht/email.md)

### Mailing list[¶](https://ollycope.com/software/yoyo/latest/#id2 "Link to this heading")

The mailing list archives can be found here: [https://lists.sr.ht/~olly/yoyo](https://lists.sr.ht/~olly/yoyo).

Changelog[¶](https://ollycope.com/software/yoyo/latest/#changelog "Link to this heading")
-----------------------------------------------------------------------------------------

### 8.2.0 (released 2022-12-14)[¶](https://ollycope.com/software/yoyo/latest/#released-2022-12-14 "Link to this heading")

* Bugfix: prevent duplicate ‘BEGIN’ statements being issued with Postgresql backend. This adds a new `rollback_on_exit` argument to the `DatabaseBackend.transaction()` method and removes the `rollback` method from the returned `TransactionManager` object.

* Add support for Python 3.11

### 8.1.0 (released 2022-11-03)[¶](https://ollycope.com/software/yoyo/latest/#released-2022-11-03 "Link to this heading")

* Add a new `yoyo init` command

### 8.0.0 (released 2022-10-05)[¶](https://ollycope.com/software/yoyo/latest/#released-2022-10-05 "Link to this heading")

* Rewrite the topological sorting algorithm to provide a more stable sort order. Note that this may change the order in which migrations are applied.

* Add support for custom backends via setuptools entry points

* Add support for the Psycopg 3 PostgreSQL driver via the `postgresql+psycopg://` URL scheme

* Add support for Python 3.10

* Drop support for Python 3.6

### 7.3.2 (released 2021-05-23)[¶](https://ollycope.com/software/yoyo/latest/#released-2021-05-23 "Link to this heading")

* Bugfix: fix errors arising when migration code changes connection parameters, for example the schema search path in PostgreSQL. Yoyo now uses a separate database connection for running migrations than for updating its internal metadata tables.

* Bugfix: fix error when loading Python module based migrations, caused by changes to importlib in Python 3.8.10 and Python 3.9.5.

* Add support for arbitrary connection parameters to snowflake backend

### 7.3.1 (released 2021-01-18)[¶](https://ollycope.com/software/yoyo/latest/#released-2021-01-18 "Link to this heading")

* Add support for AWS Redshift (thanks to Daniele Pizzoni for the patch)

* Add a new `yoyo develop` command

* Bugfix: properly escape passwords containing forward slashes

### 7.2.1 (released 2020-11-05)[¶](https://ollycope.com/software/yoyo/latest/#released-2020-11-05 "Link to this heading")

* Bugfix: allow configuration values passed in from the environment to contain percent signs (thanks to Andrew Gates for the patch)

* Add support for `--prompt-password` argument to `break-lock` command

* Add support for Python 3.9 (no code changes)

* Drop support for Python 3.5 (no code changes)

### 7.2.0 (released 2020-07-17)[¶](https://ollycope.com/software/yoyo/latest/#released-2020-07-17 "Link to this heading")

* Bugfix: fixed environment variable interpolation in config file when variables are named in upper case

* Bugfix: reliability fixes for the command line script (thanks to Chris van Pelt for the patch)

* Bugfix: the newmigration script should now work for Windows users (thanks to Jimmy Laguna Montano for the patch)

* Add experimental support for the Snowflake database backend (thanks to Emmet Murphy for the patch)

### 7.1.2 (released 2020-06-16)[¶](https://ollycope.com/software/yoyo/latest/#released-2020-06-16 "Link to this heading")

* Bugfix: fix circular dependency detection bug introduced in v7.1.1

### 7.1.1 (released 2020-06-15)[¶](https://ollycope.com/software/yoyo/latest/#released-2020-06-15 "Link to this heading")

* Bugfix: command line tool no longer shows an error message if you don’t specify a command

* Bugfix: migrations are maintained in filename order wherever the dependency ordering allows it

### 7.1.0 (released 2020-06-08)[¶](https://ollycope.com/software/yoyo/latest/#released-2020-06-08 "Link to this heading")

* Add `yoyo list` command

* Add support for substituting environment variables in the config file ([https://bitbucket.org/ollyc/yoyo/issues/55/migrations-and-rollbacks-are-both-being](https://bitbucket.org/ollyc/yoyo/issues/55/migrations-and-rollbacks-are-both-being))

* Add support for a new %include directive in config files

* Bugfix: migrations are now grouped by source ([https://bitbucket.org/ollyc/yoyo/issues/54/migrations-and-rollbacks-are-both-being](https://bitbucket.org/ollyc/yoyo/issues/54/migrations-and-rollbacks-are-both-being))

* Bugfix: viewing migration source in interactive mode no longer raises an exception

### 7.0.2 (released 2020-03-09)[¶](https://ollycope.com/software/yoyo/latest/#released-2020-03-09 "Link to this heading")

* Bugfix: removed usage of f-strings to restore python 3.5 compatibility

### 7.0.1 (released 2020-02-18)[¶](https://ollycope.com/software/yoyo/latest/#released-2020-02-18 "Link to this heading")

* Bugfix: rolling back SQL file migrations now works correctly

* Support MySQL specific encryption options when connecting

* Bugfix: `yoyo new` script now always creates temporary files with the correct file extension

### 7.0.0 (released 2020-01-20)[¶](https://ollycope.com/software/yoyo/latest/#released-2020-01-20 "Link to this heading")

* Add support for Python 3.8

* Drop compatibility with Python 2.7 and Python 3.6

* Allow migrations to be specified as `.sql` files

* Load migrations as modules; this allows migration scripts to access the `__file__` attribute.

* Bugfix: the `--all` flag now works as expected with the `rollback` command

* Bugfix: fix an error when running under a non-default schema in PostgreSQL

### 6.1.0 (released 2019-02-13)[¶](https://ollycope.com/software/yoyo/latest/#released-2019-02-13 "Link to this heading")

* The `sources` configuration option can now contain glob patterns and references to migrations installed in python packages.

* Bugfix: rolling back a group of steps now works as expected (thanks to Jon Sorensen)

### 6.0.0 (released 2018-08-21)[¶](https://ollycope.com/software/yoyo/latest/#released-2018-08-21 "Link to this heading")

__This version introduces backwards incompatible changes__. Please read this file carefully before upgrading.

* Bugfix: now works on MySQL+utf8mb4 databases. This requires a new internal schema for recording applied migrations, and your database will be automatically updated when you first run this version. After upgrading, your database will no longer be compatible with older versions of yoyo migrations. (thanks to James Socol and others for the report and discussion of the implementation)

* Bugfix: The yoyo break-lock command is no longer broken

* All migration operations (`apply`, `rollback`, `mark`, `unmark`) are now logged in a table `_yoyo_log` (thanks to Matt Williams for the suggestion).

* The CLI script now displays the list of selected migrations before asking for final confirmation when in interactive mode.

* Added support for `__transactional__` flag in sqlite migrations

### 5.1.7 (released 2018-07-30)[¶](https://ollycope.com/software/yoyo/latest/#released-2018-07-30 "Link to this heading")

* Bugfix: fix uppercase letters being excluded from generated filenames (thanks to Romain Godefroy)

### 5.1.6 (released 2018-06-28)[¶](https://ollycope.com/software/yoyo/latest/#released-2018-06-28 "Link to this heading")

* Bugfix: fix problems running on Python 3 on Windows

### 5.1.5 (released 2018-06-13)[¶](https://ollycope.com/software/yoyo/latest/#released-2018-06-13 "Link to this heading")

* Bugfix: adding a `schema` parameter to PostgreSQL connection strings no longer raises an exception (thanks to Mohamed Habib for the report)

### 5.1.0 (released 2018-07-11)[¶](https://ollycope.com/software/yoyo/latest/#released-2018-07-11 "Link to this heading")

* `yoyo rollback` now only rolls back a single migration in batch mode ( unless a –revision or –all is specified) (thanks to [A A](https://bitbucket.org/linuxnotes/) for the idea and initial implementation)

* Added support for Oracle via cx_Oracle backend (thanks to Donald Sarratt)

* Added support for locking migration tables during operations to prevent conflicts if multiple yoyo processes run at the same time (thanks to Artimi NA for proposal and initial implementation)

* Removed dependency on python-slugify to avoid pulling in GPL’d code (thanks to Olivier Chédru)

* Added support for a `schema` parameter for PostgreSQL databases (thanks to Tobiáš Štancel)

* Added support for arbitrary keyword parameters in PostgreSQL URLs, allowing eg `sslmode=require` to be specified.

* Bugfix: relative paths are correctly resolved in the config file.

* Bugfix: fixed the ordering when applying migrations with the reapply command (thanks to Goohu)

### 5.0.5 (released 2017-01-12)[¶](https://ollycope.com/software/yoyo/latest/#released-2017-01-12 "Link to this heading")

* Added support for a `__transactional__ = False` flag in migration files, allowing migrations to run commands in PostgreSQL that raise errors if run inside a transaction block (eg “CREATE DATABASE”)

* Bugfix: fix the unix_socket option for mysql connections

### 5.0.4 (released 2016-09-04)[¶](https://ollycope.com/software/yoyo/latest/#released-2016-09-04 "Link to this heading")

* Bugfix: fixed crash when mutliple migrations have the same dependency (thanks to smotko for the report)

### 5.0.3 (released 2016-07-03)[¶](https://ollycope.com/software/yoyo/latest/#released-2016-07-03 "Link to this heading")

* Bugfix: fixed exception when creating a new migration interactively with yoyo new

### 5.0.2 (released 2016-06-21)[¶](https://ollycope.com/software/yoyo/latest/#released-2016-06-21 "Link to this heading")

* Added `DatabaseBackend.apply_migrations_only` and `run_post_hooks` methods. This allows python code that interfaces with yoyo to run migrations and post_hooks separately if required (thanks to Robi Wan for reporting this and discussing possible fixes)

* Bugfix: fix duplicate key error when using post-apply hooks (thanks to Robi Wan for the report)

* Bugfix: migration steps are no longer loaded multiple times if read_migrations is called more than once (thanks to Kyle McChesney for the report)

* Bugfix: make sure that the migration_table option is read from the config file (thanks to Frederik Holljen for the report and Manolo Micozzi for the fix)

### 5.0.1 (released 2015-11-13)[¶](https://ollycope.com/software/yoyo/latest/#released-2015-11-13 "Link to this heading")

* Bugfix: migration files are now sequentially named when using the prefix option (thanks to Igor Tsarev)

### 5.0.0 (released 2015-11-13)[¶](https://ollycope.com/software/yoyo/latest/#id3 "Link to this heading")

__This version introduces backwards incompatible changes__. Please read this file carefully before upgrading.

* The configuration file is now stored per-project, not per-migrations source directory. This makes it possible to share a migrations source directory across multiple projects.

* The api for calling yoyo programmatically has changed. Refer to the README for an up to date example of calling yoyo from python code.

* Improved url parsing

* Allow database uris containing usernames with the symbol ‘@’

* The command line option `--no-cache` has been renamed to `--no-config-file`. The old name is retained as an alias for backwards compatibility

* The database must now be supplied using the `--database/-d` command line flag. This makes it possible to change the database when calling yoyo without needing to respecify the migration directories.

* Added a –revision command line option. In the case of apply, this causes the specified migration to be applied, plus any dependencies. In the case of rollback, this removes the specified revision and any other migrations that depend upon it.

* Added ‘mark’ and ‘unmark’ commands to allow migrations to be marked in the database without actually running them

* Transaction handling has changed. Each migration now always runs in a single transaction, with individual steps running in nested transactions (using savepoints). The `transaction()` function is still available for backwards compatibility, but now creates a savepoint rather than a full transaction.

* The default MySQL driver has been changed to PyMySQL, for Python 3 compatbility reasons. MySQLdb can be used by specifying the ‘mysql+mysqldb://’ scheme.

* Errors encountered while creating the _yoyo_migrations table are now raised rather than being silently ignored (thanks to James Socol).

### Version 4.2.5[¶](https://ollycope.com/software/yoyo/latest/#version-4-2-5 "Link to this heading")

* Fix for pyscopg2 driver versions >=2.6

* Faster loading of migration scripts

* Dependencies between migrations can be added via the `__depends__` attribute

* Dropped support for python 2.6

### Version 4.2.4[¶](https://ollycope.com/software/yoyo/latest/#version-4-2-4 "Link to this heading")

* Fix for mismanaged 4.2.3 release

### Version 4.2.3[¶](https://ollycope.com/software/yoyo/latest/#version-4-2-3 "Link to this heading")

* Migrations are now datestamped with a UTC date (thanks to robi wan)

* Fixes for installation and use under python 3

### Version 4.2.2[¶](https://ollycope.com/software/yoyo/latest/#version-4-2-2 "Link to this heading")

* Migration scripts can start with `from yoyo import step, transaction`. This prevents linters (eg flake8) throwing errors over undefined names.

* Bugfix: functions declared in a migration file can access the script’s global namespace

### Version 4.2.1[¶](https://ollycope.com/software/yoyo/latest/#version-4-2-1 "Link to this heading")

* Bugfix for previous release, which omitted critical files

### Version 4.2.0[¶](https://ollycope.com/software/yoyo/latest/#version-4-2-0 "Link to this heading")

* Removed yoyo.migrate namespace package. Any code that uses the yoyo api directly needs have any imports modified, eg this:

from yoyo.migrate import read_migrations
from yoyo.migrate.connections import connect
Should be changed to this:

from yoyo import read_migrations
from yoyo.connections import connect

* Migrated from darcs to mercurial. Code is now hosted at [https://bitbucket.org/ollyc/yoyo](https://bitbucket.org/ollyc/yoyo)

* Bugfix: the migration_table option was not being passed to read_migrations, causing the value to be ignored

### Version 4.1.6[¶](https://ollycope.com/software/yoyo/latest/#version-4-1-6 "Link to this heading")

* Added windows support (thanks to Peter Shinners)

### Version 4.1.5[¶](https://ollycope.com/software/yoyo/latest/#version-4-1-5 "Link to this heading")

* Configure logging handlers so that the -v switch causes output to go to the console (thanks to Andrew Nelis).

* `-v` command line switch no longer takes an argument but may be specified multiple times instead (ie use `-vvv` instead of `-v3`). `--verbosity` retains the old behaviour.

### Version 4.1.4[¶](https://ollycope.com/software/yoyo/latest/#version-4-1-4 "Link to this heading")

* Bugfix for post apply hooks

### Version 4.1.3[¶](https://ollycope.com/software/yoyo/latest/#version-4-1-3 "Link to this heading")

* Changed default migration table name back to ‘_yoyo_migration’

### Version 4.1.2[¶](https://ollycope.com/software/yoyo/latest/#version-4-1-2 "Link to this heading")

* Bugfix for error when running in interactive mode

### Version 4.1.1[¶](https://ollycope.com/software/yoyo/latest/#version-4-1-1 "Link to this heading")

* Introduced configuration option for migration table name

### Version 4.1.0[¶](https://ollycope.com/software/yoyo/latest/#version-4-1-0 "Link to this heading")

* Introduced ability to run steps within a transaction (thanks to Ryan Williams for suggesting this functionality along with assorted bug fixes.)

* “post-apply” migrations can be run after every successful upward migration

* Other minor bugfixes and improvements

* Switched to <major>.<minor> version numbering convention

### Version 4[¶](https://ollycope.com/software/yoyo/latest/#version-4 "Link to this heading")

* Fixed problem installing due to missing manifest entry

### Version 3[¶](https://ollycope.com/software/yoyo/latest/#version-3 "Link to this heading")

* Use the console_scripts entry_point in preference to scripts=[] in setup.py, this provides better interoperability with buildout

### Version 2[¶](https://ollycope.com/software/yoyo/latest/#version-2 "Link to this heading")

* Fixed error when reading dburi from config file

### Version 1[¶](https://ollycope.com/software/yoyo/latest/#version-1 "Link to this heading")

* Initial release
