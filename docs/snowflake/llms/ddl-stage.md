# Source: https://docs.snowflake.com/en/sql-reference/ddl-stage.md

# Data loading / unloading DDL

Stages and file formats are named database objects that can be used to simplify and streamline bulk loading data into and unloading data out of database tables.

Pipes are named database objects that define COPY statements for loading micro-batches of data using Snowpipe.

## Stage management

Snowflake supports two types of stages for storing data files used for loading/unloading:

* Internal stages store the files internally within Snowflake.
* External stages store the files in an external location (i.e. S3 bucket) that is referenced by the stage. An external stage specifies location and credential information, if required, for the S3 bucket.

Both external and internal stages can include file format and copy options.

* [CREATE STAGE](sql/create-stage.md)
* [CREATE STAGE … CLONE](sql/create-clone.md)
* [ALTER STAGE](sql/alter-stage.md)
* [DROP STAGE](sql/drop-stage.md)
* [DESCRIBE STAGE](sql/desc-stage.md)
* [SHOW STAGES](sql/show-stages.md)

## File format management

A file format encapsulates information, such as file type (CSV, JSON, etc.) and formatting options specific to each type, for data files used for bulk loading/unloading.

* [CREATE FILE FORMAT](sql/create-file-format.md)
* [CREATE FILE FORMAT … CLONE](sql/create-clone.md)
* [ALTER FILE FORMAT](sql/alter-file-format.md)
* [DROP FILE FORMAT](sql/drop-file-format.md)
* [DESCRIBE FILE FORMAT](sql/desc-file-format.md)
* [SHOW FILE FORMATS](sql/show-file-formats.md)

## Git repository management

A Snowflake [Git repository stage](../developer-guide/git/git-overview.md) represents a local Git repository in Snowflake.

* [CREATE GIT REPOSITORY](sql/create-git-repository.md)
* [ALTER GIT REPOSITORY](sql/alter-git-repository.md)
* [DROP GIT REPOSITORY](sql/drop-git-repository.md)
* [DESCRIBE GIT REPOSITORY](sql/desc-git-repository.md)
* [SHOW GIT BRANCHES](sql/show-git-branches.md)
* [SHOW GIT REPOSITORIES](sql/show-git-repositories.md)
* [SHOW GIT TAGS](sql/show-git-tags.md)

## Pipe management

A pipe encapsulates a single COPY statement for loading a set of data files from an ingestion queue into a table.

* [CREATE PIPE](sql/create-pipe.md)
* [ALTER PIPE](sql/alter-pipe.md)
* [DROP PIPE](sql/drop-pipe.md)
* [DESCRIBE PIPE](sql/desc-pipe.md)
* [SHOW PIPES](sql/show-pipes.md)
