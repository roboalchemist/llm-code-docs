# Source: https://fly.io/docs/mpg/extensions/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Supported Postgres Extensions 

<figure class="flex justify-center">
<img src="/static/images/Managed_Postgres.png" class="w-full max-w-lg mx-auto" alt="Illustration by Annie Ruygt of a balloon doing a lot of tasks" />
</figure>

## [](#overview)[Overview] 

Fly.io Managed Postgres (MPG) clusters include all modules and extensions provided with the default Postgres 16 distribution. This includes commonly used tools and utilities like `pgcrypto`, `pg_stat_monitor`, and `citext`. The PostgreSQL Extensions page allows you to enable or disable trusted PostgreSQL extensions for your managed database cluster. Extensions add extra functionality to your database, such as new data types, functions, or capabilities.

By default the `plpgsql`, `pg_stat_monitor`, and `pgaudit` extensions are enabled and cannot be disabled.

## [](#using-the-extensions-page)[Using the Extensions Page] 

### [](#search-for-extensions)[Search for Extensions] 

-   Use the search bar to quickly find extensions by name or description

### [](#select-a-database)[Select a Database] 

-   Use the dropdown on the right to choose which database to manage
-   Extensions are enabled/disabled per database, not cluster-wide

### [](#enable-or-disable-extensions)[Enable or Disable Extensions] 

-   Click the toggle switch next to any extension to enable or disable it
-   Each extension displays its version number (e.g., v1.3) showing which version is installed when enabled, or which version will be installed when you enable it

### [](#additional-notes)[Additional notes] 

-   If your cluster is still initializing or otherwise degraded, you'll need to wait before managing extensions

## [](#supported-third-party-extensions)[Supported Third Party Extensions] 

Aside from the extensions bundled with the default Postgres distribution, we are working to support other commonly used third party extensions.

Currently only [Vector](https://github.com/pgvector/pgvector) and [PostGIS](https://postgis.net) are supported, both can be enabled from the Extensions page for your cluster. PostGIS can be enabled when creating a cluster, too:

-   Via the dashboard, check "Enable PostGIS" under the "Extensions" section
-   When creating a cluster via flyctl, pass the `--enable-postgis-support` flag:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PGcgYnVmZmVyZWQtcmVuZGVyaW5nPSJzdGF0aWMiPjxwYXRoIGQ9Ik05LjkxMiA4LjAzN2gyLjczMmMxLjI3NyAwIDIuMzE1LS45NjIgMi4zMTUtMi4yMzdhMi4zMjUgMi4zMjUgMCAwMC0yLjMxNS0yLjMxSDIuOTU5bTEwLjIyOCA5LjAxSDIuOTU5TTYuODAyIDhIMi45NTkiPjwvcGF0aD48cGF0aCBkPSJNMTEuMDgxIDYuNDY2TDkuNTMzIDguMDM3bDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==) [ Wrap text ]

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy00IGgtNCBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuMzUiPjxnIGJ1ZmZlcmVkLXJlbmRlcmluZz0ic3RhdGljIj48cGF0aCBkPSJNMTAuNTc2IDcuMjM5YzAtLjk5NS0uODItMS44MTUtMS44MTUtMS44MTVIMy4zMTVjLS45OTUgMC0xLjgxNS44Mi0xLjgxNSAxLjgxNXY1LjQ0NmMwIC45OTUuODIgMS44MTUgMS44MTUgMS44MTVoNS40NDZjLjk5NSAwIDEuODE1LS44MiAxLjgxNS0xLjgxNVY3LjIzOXoiPjwvcGF0aD48cGF0aCBkPSJNMTAuNTc2IDEwLjU3N2gyLjEwOUExLjgyNSAxLjgyNSAwIDAwMTQuNSA4Ljc2MVYzLjMxNUExLjgyNiAxLjgyNiAwIDAwMTIuNjg1IDEuNUg3LjIzOWMtLjk5NiAwLTEuODE1LjgxOS0xLjgxNiAxLjgxNXYxLjYxNyI+PC9wYXRoPjwvZz48L3N2Zz4=) [ Copy to clipboard ]

``` 
flyctl mpg create --enable-postgis-support
```

We plan on supporting additional third party extensions based on user feedback. If there's an extension you rely on or commonly use, please let us know!

## [](#supported-extensions)[Supported extensions] 

This is a list of all bundled extensions included in MPG. Not all of these can be enabled at this time, but we are working on adding support for as many extensions as possible.

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMjAgMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+PHBhdGggZD0iTTExLjkxMiAxMC4wMzdoMi43MzJjMS4yNzcgMCAyLjMxNS0uOTYyIDIuMzE1LTIuMjM3YTIuMzE0IDIuMzE0IDAgMDAtMi4zMTUtMi4zMUg0Ljk1OU0xNS4xODcgMTQuNUg0Ljk1OU04LjgwMiAxMEg0Ljk1OSI+PC9wYXRoPjxwYXRoIGQ9Ik0xMy4wODEgOC40NjZsLTEuNTQ4IDEuNTcxIDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==)[Wrap text]

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Name                    Available               Description
  ----------------------- ----------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `adminpack`                                     Support toolpack for pgAdmin to provide additional functionality like remote management of server log files.

  `amcheck`                                       Provides functions to verify the logical consistency of the structure of indexes, such as B-trees. It's useful for detecting system catalog corruption and index corruption.

  `auth_delay`                                    Causes the server to pause briefly before reporting authentication failure, to make brute-force attacks on database passwords more difficult.

  `auto_explain`                                  Automatically logs execution plans of slow SQL statements. It helps in performance analysis by tracking down un-optimized queries in large applications that exceed a specified time threshold.

  `basebackup_to_shell`                           Adds a custom basebackup target called shell. This enables an administrator to make a base backup of a running PostgreSQL server to a shell archive.

  `basic-archive`                                 An archive module that copies completed WAL segment files to the specified directory. Can be used as a starting point for developing own archive module.

  `bloom`                                         Provides an index access method based on Bloom filters.\
                                                  A Bloom filter is a space-efficient data structure that is used to test whether an element is a member of a set.

  `btree_gin`             âœ"                     Provides GIN index operator classes with B-tree-like behavior. This allows you to use GIN indexes, which are typically used for full-text search, in situations where you might otherwise use a B-tree index, such as with integer or text data.

  `btree_gist`            âœ"                     Provides GiST (Generalized Search Tree) index operator classes that implement B-tree-like behavior. This allows you to use GiST indexes, which are typically used for multidimensional and non-scalar data, in situations where you might otherwise use a B-tree index, such as with integer or text data.

  `citext`                âœ"                     Provides a case-insensitive character string type, citext. Essentially, it internally calls lower when comparing values. Otherwise, it behaves almost exactly like text.

  `cube`                  âœ"                     Implements a data type cube for representing multidimensional cubes

  `dblink`                                        Provides functions to connect to other PostgreSQL databases from within a database session. This allows for queries to be run across multiple databases as if they were on the same server.

  `dict_int`              âœ"                     An example of an add-on dictionary template for full-text search. It's used to demonstrate how to create custom dictionaries in PostgreSQL.

  `dict_xsyn`                                     Example synonym full-text search dictionary. This dictionary type replaces words with groups of their synonyms, and so makes it possible to search for a word using any of its synonyms.

  `earthdistance`                                 This module provides two different approaches to calculating great circle distances on the surface of the Earth. The first one depends on the cube module. The second one is based on the built-in point data type, using longitude and latitude for the coordinates.

  `fuzzystrmatch`         âœ"                     Determine similarities and distance between strings

  `hstore`                âœ"                     Implements the hstore data type for storing sets of key/value pairs within a single PostgreSQL value.

  `intagg`                                        Integer aggregator and enumerator.

  `intarray`              âœ"                     Provides a number of useful functions and operators for manipulating null-free arrays of integers.

  `isn`                   âœ"                     Provides data types for the following international product numbering standards: EAN13, UPC, ISBN (books), ISMN (music), and ISSN (serials).

  `jsonb_plperl`                                  Transform between jsonb and plperl

  `lo`                    âœ"                     Provides support for managing Large Objects (also called LOs or BLOBs). This includes a data type lo and a trigger lo_manage.

  `ltree`                 âœ"                     Implements a data type ltree for representing labels of data stored in a hierarchical tree-like structure. Extensive facilities for searching through label trees are provided.

  `oldsnapshot`                                   Allows inspection of the server state that is used to implement old*snapshot*threshold.

  `pageinspect`                                   Provides functions that allow you to inspect the contents of database pages at a low level, which is useful for debugging purposes.

  `passwordcheck`                                 Checks users' passwords whenever they are set with CREATE ROLE or ALTER ROLE. If a password is considered too weak, it will be rejected and the command will terminate with an error.

  `pg_buffercache`                                Provides the set of functions for examining what's happening in the shared buffer cache in real time.

  `pg_freespacemap`                               Provides a means of examining the free space map (FSM), which PostgreSQL uses to track the locations of available space in tables and indexes. This can be useful for understanding space utilization and planning for maintenance operations.

  `pg_prewarm`                                    Provides a convenient way to load relation data into either the operating system buffer cache or the PostgreSQL buffer cache. This can be useful for reducing the time needed for a newly started database to reach its full performance potential by preloading frequently accessed data.

  `pg_stat_monitor`       âœ"                     A more advanced version of pg*stat*statements for tracking planning and execution statistics of all SQL statements executed by a server. Includes all columns available in pg*stat*statements plus provides additional ones.

  `pg_stat_statements`                            A module for tracking planning and execution statistics of all SQL statements executed by a server. Consider using an advanced version of pg*stat*statements - pg*stat*monitor

  `pg_surgery`                                    Provides various functions to perform surgery on a damaged relation. These functions are unsafe by design and using them may corrupt (or further corrupt) your database. Use them with caution and only as a last resort

  `pg_trgm`               âœ"                     Provides functions and operators for determining the similarity of alphanumeric text based on trigram matching. A trigram is a contiguous sequence of three characters. The extension can be used for text search and pattern matching operations.

  `pg_visibility`                                 Provides a way to examine the visibility map (VM) and the page-level visibility information of a table. It also provides functions to check the integrity of a visibility map and to force it to be rebuilt.

  `pg_walinspect`                                 Provides SQL functions that allow you to inspect the contents of write-ahead log of a running PostgreSQL database cluster at a low level, which is useful for debugging, analytical, reporting or educational purposes.

  `pgcrypto`              âœ"                     Provides cryptographic functions for PostgreSQL.

  `pgrowlocks`                                    Provides a function to show row locking information for a specified table.

  `pgstattuple`                                   Provides various functions to obtain tuple-level statistics. It offers detailed information about tables and indexes, such as the amount of free space and the number of live and dead tuples.

  `plpgsql`               âœ"                     PL/pgSQL procedural language

  `PostGIS`               âœ"                     Geographic information system extension for PostgreSQL

  `postgis_raster`        âœ"                     Raster data support for PostGIS

  `postgis_sfcgal`        âœ"                     SFCGAL support for PostGIS

  `postgis_topology`      âœ"                     Topology data support for PostGIS

  `postgres_fdw`                                  Provides a Foreign Data Wrapper (FDW) for accessing data in remote PostgreSQL servers. It allows a PostgreSQL database to interact with remote tables as if they were local.

  `seg`                   âœ"                     Implements a data type seg for representing line segments, or floating point intervals. seg can represent uncertainty in the interval endpoints, making it especially useful for representing laboratory measurements.

  `segpgsql`                                      SELinux-, label-based mandatory access control (MAC) security module. It can only be used on Linux 2.6.28 or higher with SELinux enabled.

  `spi`                                           Provides several workable examples of using the Server Programming Interface (SPI) and triggers.

  `sslinfo`                                       Provides information about the SSL certificate that the current client provided when connecting to PostgreSQL.

  `tablefunc`             âœ"                     Includes various functions that return tables (that is, multiple rows). These functions are useful both in their own right and as examples of how to write C functions that return multiple rows.

  `tcn`                   âœ"                     Provides a trigger function that notifies listeners of changes to any table on which it is attached.

  `test_decoding`                                 An SQL-based test/example module for WAL logical decoding

  `tsm_system_rows`       âœ"                     Provides the table sampling method SYSTEM_ROWS, which can be used in the TABLESAMPLE clause of a SELECT command.

  `tsm_system_time`       âœ"                     Provides the table sampling method SYSTEM_TIME, which can be used in the TABLESAMPLE clause of a SELECT command.

  `unaccent`              âœ"                     A text search dictionary that removes accents (diacritic signs) from lexemes. It's a filtering dictionary, which means its output is always passed to the next dictionary (if any). This allows accent-insensitive processing for full text search.

  `uuid-ossp`             âœ"                     Provides functions to generate universally unique identifiers (UUIDs) using one of several standard algorithms

  `vector`                âœ"                     vector data type and ivfflat and hnsw access methods
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fmpg%2Fextensions.html.md)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Supported+Postgres+Extensions%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fmpg%2Fextensions%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fmpg%2Fextensions.html.md%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Supported+Postgres+Extensions%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/mpg/extensions.html.md)