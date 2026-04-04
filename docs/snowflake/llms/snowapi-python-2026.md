# Source: https://docs.snowflake.com/en/release-notes/clients-drivers/snowapi-python-2026.md

# Snowflake Python APIs release notes for 2026

This article contains the release notes for the Snowflake Python APIs, including the following when applicable:

* Behavior changes
* New features
* Customer-facing bug fixes

See [Snowflake Python APIs: Managing Snowflake objects with Python](../../developer-guide/snowflake-python-api/snowflake-python-overview.md) for documentation.

## Version 1.12.0 (Feb 12, 2026)

### New features and updates

* Added support for setting (`set_tags`), unsetting (`unset_tags`), and fetching tag assignments (`get_tags`).
  Tagging support for specific resources is introduced in the following Snowflake server releases:

  * **10.3**: Alert, database, database role, dynamic table, event table, image repository, network policy, notebook, password policy, pipe,
    procedure, role, schema, stream, table, task, user, user-defined function, view, warehouse.
  * **10.4**: API integration, catalog integration, compute pool, function, iceberg table, notification integration, Streamlit.

### Bug fixes

* None.

## Version 1.11.0 (Jan 21, 2026)

### New features and updates

* The `DAGTask` object type now accepts custom objects with a `to_sql()` method as task definitions.
* The `UserDefinedFunction` object type now supports executing scalar UDFs using the `execute` method.

### Bug fixes

* Creating, fetching, and listing stored procedures that use a staged handler (where the `body` property is empty) no longer raises a `ValidationError`.
* Pydantic deprecation warnings related to `class-based config` and the `update_forward_refs`, `parse_obj`, and `_iter` methods no longer occur.
