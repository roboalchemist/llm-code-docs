# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/data-validation-cli/redshift_commands.md

# Amazon Redshift Commands Reference

## Overview

This page provides comprehensive reference documentation for Amazon Redshift-specific commands in the Snowflake Data Validation CLI. For SQL Server commands, see [SQL Server Commands Reference](sqlserver_commands.md). For Teradata commands, see [Teradata Commands Reference](teradata_commands.md). For Snowflake-to-Snowflake commands, see [Snowflake Commands Reference](snowflake_commands.md).

---

## Command Structure

All Amazon Redshift commands follow this consistent structure:

```bash
snowflake-data-validation redshift <command> [options]

# Or use the shorter alias
sdv redshift <command> [options]
```

Where `<command>` is one of:

* `run-validation` - Run synchronous validation
* `run-async-validation` - Run asynchronous validation
* `generate-validation-scripts` - Generate validation scripts
* `get-configuration-files` - Get configuration templates
* `auto-generated-configuration-file` - Interactive config generation
* `row-partitioning-helper` - Interactive row partitioning configuration
* `column-partitioning-helper` - Interactive column partitioning configuration

---

## Run Synchronous Validation

Validates data between Amazon Redshift and Snowflake in real-time.

### Syntax

```bash
snowflake-data-validation redshift run-validation \
  --data-validation-config-file /path/to/config.yaml \
  --log-level INFO
```

### Options

**`--data-validation-config-file, -dvf`** (required)

* **Type:** String (path)
* **Description:** Path to YAML configuration file containing validation settings
* **Example:** `--data-validation-config-file ./configs/redshift_validation.yaml`

**`--log-level, -ll`** (optional)

* **Type:** String
* **Valid Values:** DEBUG, INFO, WARNING, ERROR, CRITICAL
* **Default:** INFO
* **Description:** Logging level for validation execution
* **Example:** `--log-level DEBUG`

### Example Usage

```bash
# Basic validation
sdv redshift run-validation \
  --data-validation-config-file ./configs/redshift_validation.yaml

# Validation with debug logging
sdv redshift run-validation \
  --data-validation-config-file ./configs/redshift_validation.yaml \
  --log-level DEBUG

# Using full command name
snowflake-data-validation redshift run-validation \
  -dvf /opt/validations/prod_config.yaml \
  -ll INFO
```

### Use Cases

* Real-time validation during Redshift migration
* Pre-cutover validation checks
* Post-migration verification
* Continuous validation in CI/CD pipelines
* Data lake migration validation

---

## Run Asynchronous Validation

Performs validation using pre-generated metadata files without connecting to databases.

### Syntax

```bash
snowflake-data-validation redshift run-async-validation \
  --data-validation-config-file /path/to/config.yaml \
  --log-level INFO
```

### Options

**`--data-validation-config-file, -dvf`** (required)

* **Type:** String (path)
* **Description:** Path to YAML configuration file
* **Note:** Configuration must specify paths to pre-generated metadata files

**`--log-level, -ll`** (optional)

* **Type:** String
* **Valid Values:** DEBUG, INFO, WARNING, ERROR, CRITICAL
* **Default:** INFO
* **Description:** Logging level for validation execution
* **Example:** `--log-level DEBUG`

### Example Usage

```bash
# Run async validation
sdv redshift run-async-validation \
  --data-validation-config-file ./configs/async_validation.yaml

# Async validation with debug logging
sdv redshift run-async-validation \
  --data-validation-config-file ./configs/async_validation.yaml \
  --log-level DEBUG

# Using full command name
snowflake-data-validation redshift run-async-validation \
  -dvf /data/validations/async_config.yaml \
  -ll INFO
```

### Prerequisites

Before running async validation:

1. Generate validation scripts using `generate-validation-scripts`
2. Execute the generated scripts on Redshift and Snowflake databases
3. Save results to CSV/metadata files
4. Ensure metadata files are available in the configured paths

### Use Cases

* Validating in environments with restricted database access
* Separating metadata extraction from validation
* Batch validation workflows
* Scheduled validation jobs
* When database connections are intermittent

---

## Generate Validation Scripts

Generates SQL scripts for Redshift and Snowflake metadata extraction.

### Syntax

```bash
snowflake-data-validation redshift generate-validation-scripts \
  --data-validation-config-file /path/to/config.yaml \
  --log-level DEBUG
```

### Options

**`--data-validation-config-file, -dvf`** (required)

* **Type:** String (path)
* **Description:** Path to YAML configuration file

**`--log-level, -ll`** (optional)

* **Type:** String
* **Valid Values:** DEBUG, INFO, WARNING, ERROR, CRITICAL
* **Default:** INFO
* **Description:** Logging level for script generation
* **Example:** `--log-level DEBUG`

### Example Usage

```bash
# Generate scripts
sdv redshift generate-validation-scripts \
  --data-validation-config-file ./configs/validation.yaml

# Generate scripts with debug logging
sdv redshift generate-validation-scripts \
  --data-validation-config-file ./configs/validation.yaml \
  --log-level DEBUG

# Using full command name
snowflake-data-validation redshift generate-validation-scripts \
  -dvf /opt/configs/script_generation.yaml \
  -ll INFO
```

### Output

The command generates SQL scripts in the output directory configured in your YAML file:

```text
<output_directory>/
├── redshift_schema_queries.sql
├── redshift_metrics_queries.sql
├── redshift_row_queries.sql
├── snowflake_schema_queries.sql
├── snowflake_metrics_queries.sql
└── snowflake_row_queries.sql
```

### Use Cases

* Generating scripts for execution by DBAs
* Compliance requirements for query review
* Environments where direct CLI database access is restricted
* Manual execution and validation workflows
* Separating metadata extraction from validation

---

## Get Configuration Templates

Retrieves Redshift configuration templates.

### Syntax

```bash
snowflake-data-validation redshift get-configuration-files \
  --templates-directory ./redshift-templates \
  --query-templates
```

### Options

**`--templates-directory, -td`** (optional)

* **Type:** String (path)
* **Default:** Current directory
* **Description:** Directory to save template files
* **Example:** `--templates-directory ./templates`

**`--query-templates`** (optional)

* **Type:** Flag (no value required)
* **Description:** Include J2 (Jinja2) query template files for advanced customization
* **Example:** `--query-templates`

### Example Usage

```bash
# Get basic templates in current directory
sdv redshift get-configuration-files

# Save templates to specific directory
sdv redshift get-configuration-files \
  --templates-directory ./my-project/redshift-templates

# Include query templates for customization
sdv redshift get-configuration-files \
  --templates-directory ./templates \
  --query-templates

# Using short flags
sdv redshift get-configuration-files -td ./templates --query-templates
```

### Output Files

**Without `--query-templates` flag:**

```text
<templates_directory>/
└── redshift_validation_template.yaml
```

**With `--query-templates` flag:**

```text
<templates_directory>/
├── redshift_validation_template.yaml
└── query_templates/
    ├── redshift_columns_metrics_query.sql.j2
    ├── redshift_row_count_query.sql.j2
    ├── redshift_compute_md5_sql.j2
    └── snowflake_columns_metrics_query.sql.j2
```

### Use Cases

* Starting a new Redshift validation project
* Learning Redshift-specific configuration options
* Customizing validation queries for Redshift
* Creating organization-specific templates

---

## Auto-Generate Configuration File

Interactive command for Redshift configuration generation.

### Syntax

```bash
snowflake-data-validation redshift auto-generated-configuration-file
```

### Options

This command has no command-line options. All input is provided through interactive prompts.

### Interactive Prompts

The command will prompt for the following information:

1. **Redshift host**

   * Hostname/endpoint of Redshift cluster
   * Example: `redshift-cluster.region.redshift.amazonaws.com`
2. **Redshift port** (default: 5439)

   * Port number for Redshift connection
   * Press Enter to accept default
3. **Redshift username**

   * Authentication username
   * Example: `migration_user`
4. **Redshift password**

   * Authentication password (hidden input)
   * Not displayed on screen for security
5. **Redshift database**

   * Name of the database to validate
   * Example: `analytics_db`
6. **Redshift schema**

   * Schema name within the database
   * Example: `public`
7. **Output directory path**

   * Where to save validation results
   * Example: `./validation_results`

### Example Session

```bash
$ sdv redshift auto-generated-configuration-file

Redshift host: redshift-cluster.us-east-1.redshift.amazonaws.com
Redshift port [5439]:
Redshift username: migration_user
Redshift password: ********
Redshift database: analytics_db
Redshift schema: public
Output directory path: ./validation_results

Configuration file generated successfully: ./redshift_validation_config.yaml
```

### Generated Configuration

The command generates a basic YAML configuration file:

```yaml
source_platform: Redshift
target_platform: Snowflake
output_directory_path: ./validation_results

source_connection:
  mode: credentials
  host: redshift-cluster.us-east-1.redshift.amazonaws.com
  port: 5439
  username: migration_user
  password: "<hidden>"
  database: analytics_db

target_connection:
  mode: default

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

tables: []
```

### Next Steps After Generation

1. **Edit the configuration file** to add:

   * Target connection details (if not using default)
   * Tables to validate
   * Validation options
   * Column selections and mappings
2. **Review security settings:**

   * Consider using environment variables for passwords
   * Verify IAM authentication if applicable
3. **Add table configurations:**

   * Specify fully qualified table names
   * Configure column selections
   * Set up filtering where clauses
4. **Test the configuration:**

   ```bash
   sdv redshift run-validation \
     --data-validation-config-file ./redshift_validation_config.yaml
   ```

### Use Cases

* Quick setup for new Redshift users
* Generating baseline configurations
* Testing connectivity during setup
* Creating template configurations for teams

---

## Row Partitioning Helper

Interactive command to generate partitioned table configurations for large tables. This helper divides tables into smaller row partitions based on a specified column, enabling more efficient validation of large datasets.

### Syntax

```bash
snowflake-data-validation redshift row-partitioning-helper
```

### Options

This command has no command-line options. All input is provided through interactive prompts.

### How It Works

The table partitioning helper:

1. Reads an existing configuration file with table definitions
2. For each table, prompts whether to apply partitioning
3. If partitioning is enabled, collects partition parameters
4. Queries the source Redshift database to determine partition boundaries
5. Generates new table configurations with `WHERE` clauses for each partition
6. Saves the partitioned configuration to a new file

### Interactive Prompts

The command will prompt for the following information:

1. **Configuration file path**

   * Path to existing YAML configuration file
   * Example: `./configs/redshift_validation.yaml`
2. **For each table in the configuration:**

   a. **Apply partitioning?** (yes/no)

   * Whether to partition this specific table
   * Default: yes

   b. **Partition column** (if partitioning)

   * Column name used to divide the table
   * Should be indexed for performance
   * Example: `transaction_id`, `created_date`

   c. **Is partition column a string type?** (yes/no)

   * Determines quoting in generated WHERE clauses
   * Default: no (numeric)

   d. **Number of partitions**

   * How many partitions to create
   * Example: `10`, `50`, `100`

### Example Session

```bash
$ sdv redshift row-partitioning-helper

Generate a configuration file for Redshift table partitioning. This interactive
helper function processes each table in the configuration file, allowing users to
either skip partitioning or specify partitioning parameters for each table.

Configuration file path: ./configs/redshift_validation.yaml

Apply partitioning for public.fact_sales? [Y/n]: y
Write the partition column for public.fact_sales: sale_id
Is 'sale_id' column a string type? [y/N]: n
Write the number of partitions for public.fact_sales: 10

Apply partitioning for public.dim_customer? [Y/n]: n

Apply partitioning for public.transactions? [Y/n]: y
Write the partition column for public.transactions: transaction_date
Is 'transaction_date' column a string type? [y/N]: n
Write the number of partitions for public.transactions: 5

Table partitioning configuration file generated successfully!
```

### Generated Output

The command generates partitioned table configurations with WHERE clauses:

```yaml
tables:
  # Original table partitioned into 10 segments
  - fully_qualified_name: public.fact_sales
    where_clause: "sale_id >= 1 AND sale_id < 100000"
    target_where_clause: "sale_id >= 1 AND sale_id < 100000"
    # ... other table settings preserved

  - fully_qualified_name: public.fact_sales
    where_clause: "sale_id >= 100000 AND sale_id < 200000"
    target_where_clause: "sale_id >= 100000 AND sale_id < 200000"
    # ... continues for each partition

  # Non-partitioned table preserved as-is
  - fully_qualified_name: public.dim_customer
    # ... original configuration
```

### Use Cases

* **Large table validation**: Break multi-billion row tables into manageable chunks
* **Parallel processing**: Enable concurrent validation of different partitions
* **Memory optimization**: Reduce memory footprint by processing smaller data segments
* **Incremental validation**: Validate specific data ranges independently
* **Performance tuning**: Optimize validation for tables with uneven data distribution

### Best Practices

1. **Choose appropriate partition columns:**

   * Use indexed columns for better query performance
   * Prefer columns with sequential values (IDs, timestamps)
   * Avoid columns with highly skewed distributions
2. **Determine optimal partition count:**

   * Consider table size and available resources
   * Start with 10-20 partitions for tables with 10M+ rows
   * Increase partitions for very large tables (100M+ rows)
3. **String vs numeric columns:**

   * Numeric columns are generally more efficient
   * String columns work but may have uneven distribution
4. **After partitioning:**

   * Review generated WHERE clauses
   * Adjust partition boundaries if needed
   * Test with a subset before full validation

---

## Column Partitioning Helper

Interactive command to generate partitioned table configurations for wide tables with many columns. This helper divides tables into smaller column partitions, enabling more efficient validation of tables with a large number of columns.

### Syntax

```bash
snowflake-data-validation redshift column-partitioning-helper
```

### Options

This command has no command-line options. All input is provided through interactive prompts.

### How It Works

The column partitioning helper:

1. Reads an existing configuration file with table definitions
2. For each table, prompts whether to apply column partitioning
3. If partitioning is enabled, collects the number of partitions
4. Queries the source Redshift database to retrieve all column names for the table
5. Divides the columns into the specified number of partitions
6. Generates new table configurations where each partition validates only a subset of columns
7. Saves the partitioned configuration to a new file

### Interactive Prompts

The command will prompt for the following information:

1. **Configuration file path**

   * Path to existing YAML configuration file
   * Example: `./configs/redshift_validation.yaml`
2. **For each table in the configuration:**

   a. **Apply column partitioning?** (yes/no)

   * Whether to partition this specific table by columns
   * Default: yes

   b. **Number of partitions** (if partitioning)

   * How many column partitions to create
   * Example: `3`, `5`, `10`

### Example Session

```bash
$ sdv redshift column-partitioning-helper

Generate a configuration file for Redshift column partitioning. This interactive
helper function processes each table in the configuration file, allowing users to
either skip column partitioning or specify column partitioning parameters for each table.

Configuration file path: ./configs/redshift_validation.yaml

Apply column partitioning for public.wide_table? [Y/n]: y
Write the number of partitions for public.wide_table: 5

Apply column partitioning for public.small_table? [Y/n]: n

Apply column partitioning for public.report_table? [Y/n]: y
Write the number of partitions for public.report_table: 3

Column partitioning configuration file generated successfully!
```

### Generated Output

The command generates partitioned table configurations with column subsets:

```yaml
tables:
  # Original table with 100 columns partitioned into 5 segments (20 columns each)
  - fully_qualified_name: public.wide_table
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - column_a
      - column_b
      - column_c
      # ... first 20 columns alphabetically

  - fully_qualified_name: public.wide_table
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - column_d
      - column_e
      - column_f
      # ... next 20 columns alphabetically
    # ... continues for each partition

  # Non-partitioned table preserved as-is
  - fully_qualified_name: public.small_table
    # ... original configuration
```

### Use Cases

* **Wide table validation**: Break tables with hundreds of columns into manageable chunks
* **Memory optimization**: Reduce memory footprint by validating fewer columns at a time
* **Parallel processing**: Enable concurrent validation of different column groups
* **Targeted validation**: Validate specific column groups independently
* **Performance tuning**: Optimize validation for tables with many LOB or complex columns

### Best Practices

1. **Determine optimal partition count:**

   * Consider the total number of columns in the table
   * For tables with 50+ columns, start with 3-5 partitions
   * For tables with 100+ columns, consider 5-10 partitions
2. **Column ordering:**

   * Columns are divided alphabetically
   * Related columns may end up in different partitions
3. **After partitioning:**

   * Review generated column lists
   * Verify all required columns are included
   * Test with a subset before full validation
4. **Combine with row partitioning:**

   * For very large, wide tables, consider using both row and column partitioning
   * First partition by columns, then apply row partitioning to each column partition if needed

---

## Amazon Redshift Connection Configuration

Redshift connections require specific configuration in the YAML file.

### Connection Example

```yaml
source_connection:
  mode: credentials
  host: "redshift-cluster.region.redshift.amazonaws.com"
  port: 5439
  username: "redshift_user"
  password: "secure_password"
  database: "source_database"
```

### Connection Fields

**`mode`** (required)

* **Type:** String
* **Valid Values:** `credentials`
* **Description:** Connection mode for Redshift

**`host`** (required)

* **Type:** String
* **Description:** Redshift cluster endpoint
* **Format:** `<cluster-name>.<cluster-id>.<region>.redshift.amazonaws.com`
* **Examples:**

  * `"redshift-cluster-1.abc123.us-east-1.redshift.amazonaws.com"`
  * `"analytics-cluster.xyz789.eu-west-1.redshift.amazonaws.com"`
  * `"data-warehouse.def456.ap-southeast-1.redshift.amazonaws.com"`

**`port`** (required)

* **Type:** Integer
* **Default:** 5439
* **Description:** Redshift port number
* **Note:** Use the port configured for your Redshift cluster

**`username`** (required)

* **Type:** String
* **Description:** Redshift authentication username
* **Example:** `"migration_admin"`

**`password`** (required)

* **Type:** String
* **Description:** Redshift authentication password
* **Security Note:** Consider using environment variables or IAM authentication

**`database`** (required)

* **Type:** String
* **Description:** Redshift database name
* **Example:** `"analytics_database"`

### Connection Examples

**Production Connection:**

```yaml
source_connection:
  mode: credentials
  host: "prod-cluster.abc123.us-east-1.redshift.amazonaws.com"
  port: 5439
  username: "prod_reader"
  password: "${REDSHIFT_PASSWORD}"  # From environment variable
  database: "production_db"
```

**Development Connection:**

```yaml
source_connection:
  mode: credentials
  host: "dev-cluster.xyz789.us-west-2.redshift.amazonaws.com"
  port: 5439
  username: "dev_user"
  password: "dev_password"
  database: "dev_database"
```

**Data Lake Migration Connection:**

```yaml
source_connection:
  mode: credentials
  host: "datalake-cluster.def456.us-east-1.redshift.amazonaws.com"
  port: 5439
  username: "migration_user"
  password: "${AWS_REDSHIFT_PASSWORD}"
  database: "datalake_db"
```

---

## Complete Amazon Redshift Examples

### Example 1: Basic Redshift Configuration

```yaml
# Global configuration
source_platform: Redshift
target_platform: Snowflake
output_directory_path: ./validation_results
max_threads: auto

# Source connection
source_connection:
  mode: credentials
  host: redshift-cluster.us-east-1.redshift.amazonaws.com
  port: 5439
  username: redshift_user
  password: redshift_password
  database: analytics_db

# Target connection
target_connection:
  mode: name
  name: snowflake_analytics

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

# Tables to validate
tables:
  - fully_qualified_name: public.customers
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - customer_id

  - fully_qualified_name: public.orders
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - internal_notes
      - audit_log
```

### Example 2: Redshift Data Lake Migration

```yaml
# Global configuration
source_platform: Redshift
target_platform: Snowflake
output_directory_path: /data/validation/redshift_migration
max_threads: 16

# Source connection
source_connection:
  mode: credentials
  host: redshift-cluster.us-east-1.redshift.amazonaws.com
  port: 5439
  username: redshift_admin
  password: redshift_secure_password
  database: analytics_db

# Target connection
target_connection:
  mode: name
  name: snowflake_analytics

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 200
  exclude_metrics: false

# Comparison configuration
comparison_configuration:
  tolerance: 0.02

# Logging configuration
logging_configuration:
  level: INFO
  console_level: ERROR
  file_level: DEBUG

# Database mappings
database_mappings:
  analytics_db: ANALYTICS_PROD

# Schema mappings
schema_mappings:
  public: PUBLIC
  staging: STAGING

# Tables configuration
tables:
  # Large fact table with chunking
  - fully_qualified_name: public.fact_sales
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - sale_id
    chunk_number: 50
    max_failed_rows_number: 500

  # Dimension table with column mappings
  - fully_qualified_name: public.dim_customer
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - customer_key
      - customer_name
      - email
      - phone
      - address
    column_mappings:
      customer_key: cust_key
      customer_name: name
    is_case_sensitive: false

  # Filtered validation
  - fully_qualified_name: staging.incremental_load
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - load_timestamp
      - etl_batch_id
    where_clause: "load_date >= CURRENT_DATE - 7"
    target_where_clause: "load_date >= CURRENT_DATE - 7"
    chunk_number: 10
```

### Example 3: Redshift with Complex Filtering

```yaml
source_platform: Redshift
target_platform: Snowflake
output_directory_path: /opt/validation/redshift
max_threads: 24

source_connection:
  mode: credentials
  host: complex-cluster.us-west-2.redshift.amazonaws.com
  port: 5439
  username: validation_user
  password: secure_password
  database: enterprise_db

target_connection:
  mode: default

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 150

comparison_configuration:
  tolerance: 0.01

logging_configuration:
  level: INFO
  console_level: WARNING
  file_level: DEBUG

schema_mappings:
  public: PUBLIC

tables:
  # Time-based filtering
  - fully_qualified_name: public.transactions
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - transaction_id
      - customer_id
      - amount
      - transaction_date
      - status
    index_column_list:
      - transaction_id
    where_clause: "transaction_date >= '2024-01-01' AND status IN ('COMPLETED', 'PENDING')"
    target_where_clause: "transaction_date >= '2024-01-01' AND status IN ('COMPLETED', 'PENDING')"
    chunk_number: 30

  # Complex filtering with multiple conditions
  - fully_qualified_name: public.customer_activity
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - internal_score
      - risk_assessment
    where_clause: "last_activity_date >= DATEADD(month, -6, CURRENT_DATE) AND account_status = 'ACTIVE' AND total_purchases > 100"
    target_where_clause: "last_activity_date >= DATEADD(month, -6, CURRENT_DATE) AND account_status = 'ACTIVE' AND total_purchases > 100"
    index_column_list:
      - customer_id
    chunk_number: 20
    max_failed_rows_number: 100

  # Regional filtering
  - fully_qualified_name: public.sales_by_region
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    where_clause: "region IN ('US-EAST', 'US-WEST', 'EU') AND sale_date >= '2024-01-01'"
    target_where_clause: "region IN ('US-EAST', 'US-WEST', 'EU') AND sale_date >= '2024-01-01'"
    index_column_list:
      - sale_id
      - region
```

### Example 4: Redshift View Validation

Validate Amazon Redshift views alongside tables for comprehensive migration verification.

```yaml
source_platform: Redshift
target_platform: Snowflake
output_directory_path: ./redshift_view_validation
max_threads: 12

source_connection:
  mode: credentials
  host: redshift-cluster.us-east-1.redshift.amazonaws.com
  port: 5439
  username: rs_validator
  password: RedshiftPass123!
  database: analytics

target_connection:
  mode: name
  name: snowflake_analytics

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 50

comparison_configuration:
  tolerance: 0.01

database_mappings:
  analytics: ANALYTICS_PROD

schema_mappings:
  public: PUBLIC
  reports: REPORTS

# Tables to validate
tables:
  - fully_qualified_name: public.CUSTOMERS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [CUSTOMER_ID]
    target_index_column_list: [CUSTOMER_ID]

# Views to validate
views:
  # View with column mappings
  - fully_qualified_name: reports.V_USER_ACTIVITY
    target_name: V_USER_ACTIVITY
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - USER_ID
      - LAST_LOGIN
      - SESSION_COUNT
      - TOTAL_DURATION
    index_column_list: [USER_ID]
    target_index_column_list: [USER_ID]
    column_mappings:
      USER_ID: USER_ID
      LAST_LOGIN: LAST_LOGIN_DATE
      SESSION_COUNT: SESSIONS
      TOTAL_DURATION: DURATION_MINUTES

  # View with date filtering
  - fully_qualified_name: reports.V_CONVERSION_FUNNEL
    target_name: V_CONVERSION_FUNNEL
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [EVENT_ID]
    target_index_column_list: [EVENT_ID]
    where_clause: "event_date >= CURRENT_DATE - 30"
    target_where_clause: "event_date >= CURRENT_DATE - 30"

  # View with composite index columns for row validation
  - fully_qualified_name: public.V_DAILY_METRICS
    target_name: V_DAILY_METRICS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [METRIC_DATE, METRIC_TYPE]
    target_index_column_list: [METRIC_DATE, METRIC_TYPE]

  # View with different target name
  - fully_qualified_name: reports.V_LEGACY_DASHBOARD
    target_database: MODERN_ANALYTICS
    target_schema: DASHBOARDS
    target_name: V_MODERN_DASHBOARD
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [DASHBOARD_ID]
    target_index_column_list: [DASHBOARD_ID]
```

**Note:** View validation creates temporary tables internally to materialize view data for comparison between Amazon Redshift and Snowflake.

---

## Troubleshooting Redshift Connections

### Issue: Connection Timeout

**Symptom:**

```sql
Connection timeout: Unable to connect to Redshift cluster
```

**Solutions:**

1. Verify the cluster endpoint and port:

   ```bash
   telnet redshift-cluster.region.redshift.amazonaws.com 5439
   ```

2. Check VPC security groups allow inbound connections on port 5439
3. Verify the cluster is publicly accessible (if connecting from outside VPC)
4. Check route tables and network ACLs
5. Verify the cluster is in “available” state in AWS console

### Issue: Authentication Failed

**Symptom:**

```sql
Authentication failed for user 'username'
```

**Solutions:**

1. Verify credentials are correct
2. Check user has necessary permissions:

   ```sql
   -- Grant read permissions
   GRANT SELECT ON ALL TABLES IN SCHEMA public TO migration_user;
   ```

3. Verify user account exists:

   ```sql
   SELECT usename FROM pg_user WHERE usename = 'migration_user';
   ```

4. Check if password has expired or needs to be reset

### Issue: Database Not Found

**Symptom:**

```sql
Database 'database_name' does not exist
```

**Solutions:**

1. Verify database name is correct (case-sensitive)
2. List available databases:

   ```sql
   SELECT datname FROM pg_database;
   ```

3. Ensure user has access to the database

### Issue: SSL/TLS Certificate Errors

**Symptom:**

```sql
SSL certificate verification failed
```

**Solutions:**

1. Verify SSL is required for the cluster
2. Check AWS Redshift SSL/TLS settings
3. Ensure you’re using the correct endpoint (not VPC endpoint)

### Issue: Network/VPC Configuration

**Symptom:**

```sql
Connection refused or network unreachable
```

**Solutions:**

1. **Check cluster publicly accessible setting:**

   * In AWS Console, verify “Publicly accessible” is enabled if connecting externally
2. **Verify VPC security group rules:**

   * Inbound rule: Type = Custom TCP, Port = 5439, Source = Your IP
3. **Check VPC route table:**

   * Ensure proper routing to internet gateway (for public access)
4. **Verify VPC Network ACLs:**

   * Allow inbound/outbound traffic on port 5439

---

## Best Practices for Amazon Redshift

### Security

1. **Use IAM authentication when possible:**

   ```yaml
   # Note: IAM authentication setup requires additional AWS configuration
   source_connection:
     mode: credentials
     host: "cluster.region.redshift.amazonaws.com"
     # Use temporary credentials from IAM
   ```

2. **Store passwords securely:**

   ```yaml
   source_connection:
     password: "${REDSHIFT_PASSWORD}"  # From environment variable
   ```

3. **Use read-only accounts:**

   ```sql
   CREATE USER migration_reader WITH PASSWORD 'secure_password';
   GRANT USAGE ON SCHEMA public TO migration_reader;
   GRANT SELECT ON ALL TABLES IN SCHEMA public TO migration_reader;
   ```

4. **Restrict VPC access:**

   * Configure security groups to allow access only from specific IPs
   * Use VPC endpoints for internal AWS connectivity

### Performance

1. **Enable chunking for large tables:**

   ```yaml
   tables:
     - fully_qualified_name: large_table
       chunk_number: 50
   ```

2. **Use WHERE clauses to filter data:**

   ```yaml
   tables:
     - fully_qualified_name: transactions
       where_clause: "transaction_date >= CURRENT_DATE - 30"
   ```

3. **Optimize thread count:**

   ```yaml
   max_threads: 16  # Adjust based on cluster size
   ```

4. **Consider cluster size and workload:**

   * Run validations during off-peak hours
   * Monitor cluster performance during validation

### Data Quality

1. **Handle distribution and sort keys:**

   * Be aware that Redshift distribution/sort keys may affect data ordering
   * Use appropriate index columns that match distribution keys
2. **Start with schema validation:**

   ```yaml
   validation_configuration:
     schema_validation: true
     metrics_validation: false
     row_validation: false
   ```

3. **Progress to metrics validation:**

   ```yaml
   validation_configuration:
     schema_validation: true
     metrics_validation: true
     row_validation: false
   ```

4. **Enable row validation selectively:**

   ```yaml
   validation_configuration:
     row_validation: true

   tables:
     - fully_qualified_name: critical_fact_table
       # Row validation enabled for this table
   ```

### AWS-Specific Considerations

1. **Monitor cluster performance:**

   * Use AWS CloudWatch metrics during validation
   * Monitor query performance and WLM queues
2. **Consider cluster maintenance windows:**

   * Avoid running validations during maintenance windows
   * Check cluster status before starting validation
3. **Use appropriate cluster endpoints:**

   * Use cluster endpoint for direct connections
   * Use VPC endpoint for internal AWS connectivity
4. **Handle AWS region-specific configurations:**

   ```yaml
   source_connection:
     host: "cluster.us-east-1.redshift.amazonaws.com"  # Specify correct region
   ```

---

## See Also

* [Main CLI Usage Guide](CLI_USAGE_GUIDE.md)
* [SQL Server Commands Reference](sqlserver_commands.md)
* [Teradata Commands Reference](teradata_commands.md)
* [Snowflake Commands Reference](snowflake_commands.md)
* [Configuration Examples](CONFIGURATION_EXAMPLES.md)
* [Quick Reference Guide](CLI_QUICK_REFERENCE.md)
