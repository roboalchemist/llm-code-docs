# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/data-validation-cli/release_notes.md

# Release Notes - Snowflake Data Validation CLI

## Version 1.2.0 (January 2026)

### What’s New

* **View Validation:** Full support for validating database views alongside tables

  * Available only for SQL SERVER.
  * Configure views in a dedicated `views:` section in your YAML configuration
  * Supports all table configuration options including column selection, filtering, column mappings, and chunking
  * Override target database, schema, or view name with `target_database`, `target_schema`, and `target_name` options
  * Views are validated by creating temporary tables internally to materialize schema for comparison

### Usage Example

```yaml
# Views are configured similarly to tables
views:
  - fully_qualified_name: INVENTORY.dbo.INTEGRATION_TEST_VIEW_1
    target_name: INTEGRATION_TEST_VIEW_1
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [ORDERID]
    target_index_column_list: [ORDERID]
```

* **Snowflake to Snowflake Validation:** Full support for validating data between Snowflake instances.

---

## Version 1.0.2 (December 2025)

### What’s New

* **New Command:** `column-partitioning-helper` - Interactive helper to partition wide tables by columns for more efficient validation of tables with many columns

### Changes

* **Command Renamed:** `table-partitioning-helper` has been renamed to `row-partitioning-helper` for improved clarity on its purpose

---

## Version 1.0.1 (December 2025)

### What’s New

This release introduces an enhancement to improve the CLI user experience whenaccessing help documentation.

### Example

```bash
# These commands no longer create log files
sdv --help
sdv sqlserver --help
sdv sqlserver run-validation --help

# These commands still create log files normally
sdv sqlserver run-validation --data-validation-config-file config.yaml
```

---

## Documentation

For complete information about using the Snowflake Data Validation CLI, refer to:

* **[Documentation Index](index.md)** - Start here for navigation to all documentation
* **[CLI Usage Guide](CLI_USAGE_GUIDE.md)** - Comprehensive CLI documentation
* **[Quick Reference Guide](CLI_QUICK_REFERENCE.md)** - Fast lookup reference
* **[Configuration Examples](CONFIGURATION_EXAMPLES.md)** - Ready-to-use configuration examples
* **[SQL Server Commands](sqlserver_commands.md)** - SQL Server specific commands
* **[Teradata Commands](teradata_commands.md)** - Teradata specific commands
* **[Redshift Commands](redshift_commands.md)** - Redshift specific commands

---

## Support

If you encounter any issues or have questions:

* **Email:** [snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
* **Documentation:** [Full Documentation](https://github.com/snowflake-eng/migrations-data-validation)
* **Issues:** [GitHub Issues](https://github.com/snowflake-eng/migrations-data-validation/issues)
