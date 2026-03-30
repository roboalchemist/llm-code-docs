# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/data-validation-cli/CLI_QUICK_REFERENCE.md

# Snowflake Data Validation CLI - Quick Reference

This quick reference guide provides a condensed overview of commands, configuration options, and common usage patterns for the Snowflake Data Validation CLI tool, designed for easy lookup during validation tasks.

---

## Installation

## Prerequisites

Before running the commands below, ensure that Python 3.10 or later and pip are installed on your system.

```bash
# Base installation
pip install snowflake-data-validation

# With source-specific drivers
pip install "snowflake-data-validation[sqlserver]"
pip install "snowflake-data-validation[teradata]"
pip install "snowflake-data-validation[redshift]"
```

---

## Command Structure

```bash
snowflake-data-validation <dialect> <command> [options]
# or
sdv <dialect> <command> [options]
```

**Dialects:** `sqlserver` | `teradata` | `redshift` | `snowflake`

---

## Common Commands

### `run-validation`

```bash
# SQL Server
sdv sqlserver run-validation --data-validation-config-file config.yaml

# Teradata
sdv teradata run-validation --data-validation-config-file config.yaml

# Redshift
sdv redshift run-validation --data-validation-config-file config.yaml

# Snowflake (Snowflake-to-Snowflake)
sdv snowflake run-validation --data-validation-config-file config.yaml
```

### `generate-validation-scripts`

```bash
sdv <dialect> generate-validation-scripts --data-validation-config-file config.yaml
```

### `run-async-validation`

```bash
sdv <dialect> run-async-validation --data-validation-config-file config.yaml
```

### `get-configuration-files`

```bash
sdv <dialect> get-configuration-files --templates-directory ./templates
```

### `auto-generated-configuration-file`

```bash
sdv <dialect> auto-generated-configuration-file
```

### `row-partitioning-helper`

```bash
sdv <dialect> row-partitioning-helper
```

Interactive command to partition large tables by rows for more efficient validation.

### `column-partitioning-helper`

```bash
sdv <dialect> column-partitioning-helper
```

Interactive command to partition wide tables by columns for more efficient validation.

---

## Configuration Template

This template provides the core structure for configuring data validation jobs, defining source and target connections, validation rules, and table-specific settings that control how data is compared between your source database and Snowflake.

```yaml
# GLOBAL
source_platform: SqlServer  # SqlServer | Teradata | Redshift | Snowflake
target_platform: Snowflake
output_directory_path: ./output
max_threads: auto  # "auto" or 1-32
target_database: teradataTargetDatabase # For Teradata sources only - specify target database

# SOURCE CONNECTION
source_connection:
  mode: credentials
  host: "hostname"
  port: 1433
  username: "user"
  password: "pass"
  database: "db"
  # SQL Server only:
  trust_server_certificate: "no"  # yes | no
  encrypt: "yes"  # yes | no | optional

# TARGET CONNECTION
target_connection:
  mode: name  # name | default
  name: "connection_name"  # if mode=name

# VALIDATION
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false
  max_failed_rows_number: 100
  exclude_metrics: false
  apply_metric_column_modifier: false

# COMPARISON
comparison_configuration:
  tolerance: 0.01  # 1% tolerance

# LOGGING (optional)
logging_configuration:
  level: INFO  # DEBUG | INFO | WARNING | ERROR | CRITICAL
  console_level: WARNING
  file_level: DEBUG

# MAPPINGS (optional)
database_mappings:
  source_db: target_db

schema_mappings:
  source_schema: target_schema

# TABLES
tables:
  - fully_qualified_name: database.schema.table1
    target_name: table1_target
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: []
    where_clause: ""
    target_where_clause: ""
    chunk_number: 0
    column_mappings: {}

# VIEWS
views:
  - fully_qualified_name: database.schema.view1
    target_name: view1_target
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [ID]
    target_index_column_list: [ID]
    where_clause: ""
    target_where_clause: ""
    chunk_number: 0
    column_mappings: {}
```

---

## Table Configuration Examples

### Include All Columns

```yaml
- fully_qualified_name: db.schema.table
  use_column_selection_as_exclude_list: false
  column_selection_list: []
```

### Include Specific Columns

```yaml
- fully_qualified_name: db.schema.table
  use_column_selection_as_exclude_list: false
  column_selection_list:
    - column1
    - column2
    - column3
```

### Exclude Specific Columns

```yaml
- fully_qualified_name: db.schema.table
  use_column_selection_as_exclude_list: true
  column_selection_list:
    - audit_timestamp
    - internal_notes
```

### With Filtering

```yaml
- fully_qualified_name: db.schema.table
  use_column_selection_as_exclude_list: false
  column_selection_list: []
  where_clause: "status = 'ACTIVE' AND created_date >= '2024-01-01'"
  target_where_clause: "status = 'ACTIVE' AND created_date >= '2024-01-01'"
```

### With Column Mappings

```yaml
- fully_qualified_name: db.schema.table
  use_column_selection_as_exclude_list: false
  column_selection_list: []
  column_mappings:
    source_col1: target_col1
    source_col2: target_col2
```

### Large Table with Chunking

```yaml
- fully_qualified_name: db.schema.large_table
  use_column_selection_as_exclude_list: false
  column_selection_list: []
  index_column_list:
    - primary_key
  chunk_number: 50
  max_failed_rows_number: 500
```

---

## View Configuration Examples

Views are validated similarly to tables but are configured in a separate `views:` section. View validation creates temporary tables internally to materialize view schema for comparison.

### Basic View Validation

```yaml
views:
  - fully_qualified_name: db.schema.customer_view
    target_name: customer_view_target
    use_column_selection_as_exclude_list: false
    column_selection_list: []
```

### View with Column Selection

```yaml
views:
  - fully_qualified_name: db.schema.sales_summary_view
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - region
      - total_sales
      - sales_count
```

### View with Filtering

```yaml
views:
  - fully_qualified_name: db.schema.active_users_view
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    where_clause: status = 'ACTIVE'
    target_where_clause: status = 'ACTIVE'
```

### View with Column Mappings

```yaml
views:
  - fully_qualified_name: db.schema.legacy_report_view
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    column_mappings:
      old_col_name: new_col_name
      legacy_id: id
```

### Combined Tables and Views Configuration

```yaml
tables:
  - fully_qualified_name: db.schema.customers
    target_name: customers_target
    use_column_selection_as_exclude_list: false
    column_selection_list: []

views:
  - fully_qualified_name: db.schema.customer_summary_view
    target_name: customer_summary_view_target
    use_column_selection_as_exclude_list: false
    column_selection_list: []
```

---

## Connection Examples

### SQL Server

```yaml
source_connection:
  mode: credentials
  host: "sqlserver.company.com"
  port: 1433
  username: "sql_user"
  password: "sql_pass"
  database: "prod_db"
  trust_server_certificate: "no"
  encrypt: "yes"
```

### Teradata

```yaml
source_connection:
  mode: credentials
  host: "teradata.company.com"
  username: "td_user"
  password: "td_pass"
  database: "prod_db"
```

### Redshift

```yaml
source_connection:
  mode: credentials
  host: "cluster.region.redshift.amazonaws.com"
  port: 5439
  username: "rs_user"
  password: "rs_pass"
  database: "prod_db"
```

### Snowflake Target (Named) (See more info here: https://docs.snowflake.com/en/developer-guide/snowflake-cli/connecting/configure-connections)

```yaml
target_connection:
  mode: name
  name: "my_snowflake_connection"
```

### Snowflake Target (Default)

```yaml
target_connection:
  mode: default
```

### Snowflake Source (for Snowflake-to-Snowflake validation)

```yaml
source_connection:
  mode: name
  name: "my_source_snowflake_connection"
```

---

## Validation Levels

| Level | Type | Description | Cost |
| --- | --- | --- | --- |
| **1** | Schema | Column names, types, nullability | Low |
| **2** | Metrics | Row counts, distinct values, min/max, avg | Medium |
| **3** | Row | Hash-based row comparison | High |

---

## Common CLI Options

| Option | Short | Description | Default |
| --- | --- | --- | --- |
| `--data-validation-config-file` | `-dvf` | Config file path | Required |
| `--log-level` | `-ll` | Log level | INFO |
| `--templates-directory` | `-td` | Template output dir | Current dir |
| `--query-templates` |  | Include query templates | false |
| `--output-directory` |  | Results directory | From config |

---

## Log Levels

* **DEBUG**: Detailed diagnostic information
* **INFO**: General informational messages
* **WARNING**: Warning messages
* **ERROR**: Error messages
* **CRITICAL**: Critical errors

---

## Configuration Field Reference

### Required Fields

* `source_platform`
* `target_platform`
* `output_directory_path`
* `source_connection`
* `target_connection`
* `tables` or `views` (at least one must have entries)

### Optional Fields

* `max_threads` (default: “auto”)
* `target_database` (required for Teradata)
* `validation_configuration`
* `comparison_configuration`
* `logging_configuration`
* `database_mappings`
* `schema_mappings`

---

## Table Configuration Fields

| Field | Required | Type | Description |
| --- | --- | --- | --- |
| `fully_qualified_name` | ✓ | String | Full table identifier |
| `use_column_selection_as_exclude_list` | ✓ | Boolean | Include/exclude mode |
| `column_selection_list` | ✓ | List | Columns to include/exclude |
| `index_column_list` |  | List | Primary key columns |
| `where_clause` |  | String | Source filter |
| `target_where_clause` |  | String | Target filter |
| `chunk_number` |  | Integer | Number of chunks (0=off) |
| `max_failed_rows_number` |  | Integer | Max failures to report |
| `column_mappings` |  | Dict | Source→Target mappings |
| `is_case_sensitive` |  | Boolean | Case-sensitive matching |

---

## View Configuration Fields

View configuration uses the same fields as table configuration. Views are defined in a separate `views:` section.

| Field | Required | Type | Description |
| --- | --- | --- | --- |
| `fully_qualified_name` | ✓ | String | Full view identifier |
| `use_column_selection_as_exclude_list` | ✓ | Boolean | Include/exclude mode |
| `column_selection_list` | ✓ | List | Columns to include/exclude |
| `index_column_list` |  | List | Index columns for row validation |
| `where_clause` |  | String | Source filter |
| `target_where_clause` |  | String | Target filter |
| `chunk_number` |  | Integer | Number of chunks (0=off) |
| `max_failed_rows_number` |  | Integer | Max failures to report |
| `column_mappings` |  | Dict | Source→Target mappings |
| `is_case_sensitive` |  | Boolean | Case-sensitive matching |
| `target_database` |  | String | Override target database |
| `target_schema` |  | String | Override target schema |
| `target_name` |  | String | Override target view name |

**Note:** Views use temporary tables internally to materialize the schema of the view for validation.

---

## Performance Tips

### For Large Tables

1. Enable chunking:

   ```yaml
   chunk_number: 100
   ```

2. Increase threads:

   ```yaml
   max_threads: 32
   ```

3. Filter data:

   ```yaml
   where_clause: "date >= '2024-01-01'"
   ```

4. Exclude large columns:

   ```yaml
   use_column_selection_as_exclude_list: true
   column_selection_list:
     - large_blob
     - large_text
   ```

5. Skip row validation initially:

   ```yaml
   validation_configuration:
     schema_validation: true
     metrics_validation: true
     row_validation: false  # Enable after initial validation
   ```

---

## Common Issues

### Connection Failed

```yaml
# SQL Server SSL issues
trust_server_certificate: "yes"
encrypt: "optional"
```

### Out of Memory

```yaml
# Reduce parallelism
max_threads: 4

# Enable chunking
chunk_number: 50
```

### Tolerance for Numerical Differences

```yaml
# Increase tolerance
comparison_configuration:
  tolerance: 0.05  # 5%
```

### YAML Syntax Errors

* Use spaces, not tabs
* Quote special characters in YAML: :code:`password: "p@ssw0rd!"`
* If a string value starts or ends with a double quote, escape the double quotes “table #1”
* Escape quotes: `name = 'O''Brien'`

---

## Asynchronous Workflow

The asynchronous workflow allows you to decouple script generation from execution, which is useful when you need to run validation queries manually on the source database or when you have restricted access that requires scheduled execution.

1. Generate the validation scripts:

   ```bash
   sdv sqlserver generate-validation-scripts --data-validation-config-file config.yaml
   ```

2. Execute the generated scripts manually on your source database and save the results to CSV files in the output directory.
3. Run the async validation to compare the saved results:

   ```bash
   sdv sqlserver run-async-validation --data-validation-config-file config.yaml
   ```

---

## Example Workflows

### Basic Validation

1. Get the configuration templates:

   ```bash
   sdv sqlserver get-configuration-files
   ```

2. Edit the generated `config.yaml` file to configure your source and target connections, validation settings, and tables.
3. Run the validation:

   ```bash
   sdv sqlserver run-validation --data-validation-config-file config.yaml
   ```

### Interactive Setup

1. Generate a configuration file interactively by answering prompts:

   ```bash
   sdv sqlserver auto-generated-configuration-file
   ```

2. Run the validation using the generated configuration:

   ```bash
   sdv sqlserver run-validation --data-validation-config-file generated_config.yaml
   ```

### Debug Mode

To troubleshoot issues or get detailed execution information, run validation with debug logging:

```bash
sdv sqlserver run-validation \
  --data-validation-config-file config.yaml \
  --log-level DEBUG
```

### Large Table Partitioning

For validating very large tables, use the partitioning helper to divide tables into smaller segments:

1. Create a configuration file with your table definitions
2. Run the partitioning helper:

   ```bash
   sdv sqlserver row-partitioning-helper
   ```

3. Follow the prompts to specify partition columns and counts
4. Run validation with the partitioned configuration

---

## Output Files

Generated in `output_directory_path`:

* **Validation reports:** Schema, metrics, row comparison results
* **Log files:** `data_validation_YYYY-MM-DD_HH-MM-SS.log`
* **Difference files:** `differencesL1.csv`, `differencesL2.csv`
* **Generated scripts:** (when using `generate-validation-scripts`)

---

## Environment Variables

For Snowflake connections using default mode, configure:

```bash
export SNOWFLAKE_ACCOUNT="account_name"
export SNOWFLAKE_USER="username"
export SNOWFLAKE_PASSWORD="password"
export SNOWFLAKE_DATABASE="database"
export SNOWFLAKE_SCHEMA="schema"
export SNOWFLAKE_WAREHOUSE="warehouse"
export SNOWFLAKE_ROLE="role"
```

---

## Help Commands

```bash
# Main help
sdv --help

# Dialect-specific help
sdv sqlserver --help
sdv teradata --help
sdv redshift --help
sdv snowflake --help

# Command-specific help
sdv sqlserver run-validation --help
sdv sqlserver generate-validation-scripts --help
sdv sqlserver row-partitioning-helper --help
sdv sqlserver column-partitioning-helper --help
```

---

## Resources

* **Full Documentation:** <CLI_USAGE_GUIDE.md>
* **SQL Server Commands:** <sqlserver_commands.md>
* **Teradata Commands:** <teradata_commands.md>
* **Redshift Commands:** <redshift_commands.md>
* **Snowflake Commands:** <snowflake_commands.md>
* **Configuration Examples:** <CONFIGURATION_EXAMPLES.md>
