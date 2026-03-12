# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/data-validation-cli/snowflake_commands.md

# Snowflake Commands Reference

## Overview

This page provides comprehensive reference documentation for Snowflake-to-Snowflake validation commands in the Snowflake Data Validation CLI. This feature enables validation between different Snowflake accounts, regions, or databases—useful for cross-account migrations, region migrations, or verifying data replication.

For other source platforms, see [SQL Server Commands Reference](sqlserver_commands.md), [Teradata Commands Reference](teradata_commands.md), or [Redshift Commands Reference](redshift_commands.md).

---

## Command Structure

All Snowflake commands follow this consistent structure:

```bash
snowflake-data-validation snowflake <command> [options]

# Or use the shorter alias
sdv snowflake <command> [options]
```

Where `<command>` is one of:

* `run-validation` - Run synchronous validation
* `run-async-validation` - Run asynchronous validation
* `generate-validation-scripts` - Generate validation scripts
* `get-configuration-files` - Get configuration templates
* `auto-generated-configuration-file` - Interactive config generation
* `row-partitioning-helper` - Interactive row partitioning configuration
* `column-partitioning-helper` - Interactive column partitioning configuration
* `source-validate` - Execute validation on source only and save results as Parquet files

---

## Run Synchronous Validation

Validates data between source and target Snowflake databases in real-time.

### Syntax

```bash
snowflake-data-validation snowflake run-validation \
  --data-validation-config-file /path/to/config.yaml \
  --log-level INFO
```

### Options

**`--data-validation-config-file, -dvf`** (required)

* **Type:** String (path)
* **Description:** Path to YAML configuration file containing validation settings
* **Example:** `--data-validation-config-file ./configs/snowflake_validation.yaml`

**`--log-level, -ll`** (optional)

* **Type:** String
* **Valid Values:** DEBUG, INFO, WARNING, ERROR, CRITICAL
* **Default:** INFO
* **Description:** Logging level for validation execution
* **Example:** `--log-level DEBUG`

### Example Usage

```bash
# Basic validation
sdv snowflake run-validation \
  --data-validation-config-file ./configs/snowflake_validation.yaml

# Validation with debug logging
sdv snowflake run-validation \
  --data-validation-config-file ./configs/snowflake_validation.yaml \
  --log-level DEBUG

# Using full command name
snowflake-data-validation snowflake run-validation \
  -dvf /opt/validations/prod_config.yaml \
  -ll INFO
```

### Use Cases

* Cross-account Snowflake migration validation
* Cross-region data replication verification
* Database copy validation within the same account
* Pre-cutover validation checks
* Post-migration verification
* Continuous validation in CI/CD pipelines

---

## Run Asynchronous Validation

Performs validation using pre-generated metadata files without connecting to databases.

### Syntax

```bash
snowflake-data-validation snowflake run-async-validation \
  --data-validation-config-file /path/to/config.yaml
```

### Options

**`--data-validation-config-file, -dvf`** (required)

* **Type:** String (path)
* **Description:** Path to YAML configuration file
* **Note:** Configuration must specify paths to pre-generated metadata files

### Example Usage

```bash
# Run async validation
sdv snowflake run-async-validation \
  --data-validation-config-file ./configs/async_validation.yaml

# Using full command name
snowflake-data-validation snowflake run-async-validation \
  -dvf /data/validations/async_config.yaml
```

### Prerequisites

Before running async validation:

1. Generate validation scripts using `generate-validation-scripts`
2. Execute the generated scripts on source and target Snowflake databases
3. Save results to metadata files
4. Ensure metadata files are available in the configured paths

### Use Cases

* Validating in environments with restricted database access
* Separating metadata extraction from validation
* Batch validation workflows
* Scheduled validation jobs
* When database connections are intermittent

---

## Source Validate

Executes validation queries on the source Snowflake database only and saves results as Parquet files for later comparison without needing source database access.

### Syntax

```bash
snowflake-data-validation snowflake source-validate \
  --data-validation-config-file /path/to/config.yaml \
  --log-level INFO
```

### Options

**`--data-validation-config-file, -dvf`** (required)

* **Type:** String (path)
* **Description:** Path to YAML configuration file

**`--log-level, -ll`** (optional)

* **Type:** String
* **Valid Values:** DEBUG, INFO, WARNING, ERROR, CRITICAL
* **Default:** INFO
* **Description:** Logging level for validation execution
* **Example:** `--log-level DEBUG`

### Example Usage

```bash
# Run source validation
sdv snowflake source-validate \
  --data-validation-config-file ./configs/snowflake_validation.yaml

# Source validation with debug logging
sdv snowflake source-validate \
  --data-validation-config-file ./configs/snowflake_validation.yaml \
  --log-level DEBUG

# Using full command name
snowflake-data-validation snowflake source-validate \
  -dvf /opt/configs/validation.yaml \
  -ll INFO
```

### Output

The command generates Parquet files in the configured output directory containing:

* Schema metadata from source tables
* Metrics data (row counts, statistics)
* Row-level data for comparison (if row validation is enabled)

### Use Cases

* **Offline validation**: Extract source data once, validate multiple times
* **Network-restricted environments**: Export data when source is accessible, validate later
* **Performance optimization**: Separate data extraction from comparison
* **Archival purposes**: Keep point-in-time snapshots of source metadata
* **Cross-environment validation**: Extract from production, validate in development

---

## Generate Validation Scripts

Generates SQL scripts for Snowflake metadata extraction that can be executed separately.

### Syntax

```bash
snowflake-data-validation snowflake generate-validation-scripts \
  --data-validation-config-file /path/to/config.yaml
```

### Options

**`--data-validation-config-file, -dvf`** (required)

* **Type:** String (path)
* **Description:** Path to YAML configuration file

### Example Usage

```bash
# Generate scripts
sdv snowflake generate-validation-scripts \
  --data-validation-config-file ./configs/validation.yaml

# Using full command name
snowflake-data-validation snowflake generate-validation-scripts \
  -dvf /opt/configs/script_generation.yaml
```

### Output

The command generates SQL scripts in the output directory configured in your YAML file:

```text
<output_directory>/
├── source_schema_queries.sql
├── source_metrics_queries.sql
├── source_row_queries.sql
├── target_schema_queries.sql
├── target_metrics_queries.sql
└── target_row_queries.sql
```

### Use Cases

* Generating scripts for execution by DBAs
* Compliance requirements for query review
* Environments where direct CLI database access is restricted
* Manual execution and validation workflows
* Separating metadata extraction from validation

---

## Get Configuration Templates

Retrieves Snowflake configuration templates for validation setup.

### Syntax

```bash
snowflake-data-validation snowflake get-configuration-files \
  --templates-directory ./snowflake-templates \
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
sdv snowflake get-configuration-files

# Save templates to specific directory
sdv snowflake get-configuration-files \
  --templates-directory ./my-project/snowflake-templates

# Include query templates for customization
sdv snowflake get-configuration-files \
  --templates-directory ./templates \
  --query-templates

# Using short flags
sdv snowflake get-configuration-files -td ./templates --query-templates
```

### Output Files

**Without `--query-templates` flag:**

```text
<templates_directory>/
└── snowflake_validation_template.yaml
```

**With `--query-templates` flag:**

```text
<templates_directory>/
├── snowflake_validation_template.yaml
└── query_templates/
    ├── snowflake_columns_metrics_query.sql.j2
    ├── snowflake_row_count_query.sql.j2
    └── snowflake_compute_md5_sql.j2
```

### Use Cases

* Starting a new Snowflake-to-Snowflake validation project
* Learning Snowflake-specific configuration options
* Customizing validation queries
* Creating organization-specific templates

---

## Auto-Generate Configuration File

Interactive command to generate a configuration file by prompting for Snowflake connection parameters.

### Syntax

```bash
snowflake-data-validation snowflake auto-generated-configuration-file
```

### Options

This command has no command-line options. All input is provided through interactive prompts.

### Interactive Prompts

The command will prompt for the following information:

1. **Snowflake Named Connection name**

   * Name of pre-configured Snowflake connection
   * Default: `default`
   * Example: `my_snowflake_connection`
2. **Snowflake database**

   * Name of the database to validate
   * Example: `PRODUCTION_DB`
3. **Snowflake schema**

   * Schema name within the database
   * Example: `PUBLIC`
4. **Output path for configuration file**

   * Where to save the generated YAML file
   * Example: `./configs/snowflake_config.yaml`

### Example Session

```bash
$ sdv snowflake auto-generated-configuration-file

Generating basic configuration file for Snowflake validation...
Please provide the following connection information:

Snowflake Named Connection name [default]: prod_connection
Snowflake database: PRODUCTION_DB
Snowflake schema: PUBLIC
Output path for the configuration file: ./configs/snowflake_validation.yaml

Configuration file generated successfully!
```

### Generated Configuration

The command generates a basic YAML configuration file:

```yaml
source_platform: Snowflake
target_platform: Snowflake
output_directory_path: ./validation_results

source_connection:
  mode: name
  name: prod_connection

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
2. **Review connection settings:**

   * Verify source and target connection names
   * Consider using environment variables for sensitive data
3. **Add table configurations:**

   * Specify fully qualified table names
   * Configure column selections
   * Set up filtering where clauses
4. **Test the configuration:**

   ```bash
   sdv snowflake run-validation \
     --data-validation-config-file ./configs/snowflake_validation.yaml
   ```

### Use Cases

* Quick setup for new Snowflake-to-Snowflake users
* Generating baseline configurations
* Testing connectivity during setup
* Creating template configurations for teams

---

## Row Partitioning Helper

Interactive command to generate partitioned table configurations for large tables. This helper divides tables into smaller row partitions based on a specified column, enabling more efficient validation of large datasets.

### Syntax

```bash
snowflake-data-validation snowflake row-partitioning-helper
```

### Options

This command has no command-line options. All input is provided through interactive prompts.

### How It Works

The row partitioning helper:

1. Reads an existing configuration file with table definitions
2. For each table, prompts whether to apply partitioning
3. If partitioning is enabled, collects partition parameters
4. Queries the source Snowflake database to determine partition boundaries
5. Generates new table configurations with `WHERE` clauses for each partition
6. Saves the partitioned configuration to a new file

### Interactive Prompts

The command will prompt for the following information:

1. **Configuration file path**

   * Path to existing YAML configuration file
   * Example: `./configs/snowflake_validation.yaml`
2. **For each table in the configuration:**

   a. **Apply partitioning?** (yes/no)

   * Whether to partition this specific table
   * Default: yes

   b. **Partition column** (if partitioning)

   * Column name used to divide the table
   * Should be indexed or clustered for performance
   * Example: `transaction_id`, `created_date`

   c. **Is partition column a string type?** (yes/no)

   * Determines quoting in generated WHERE clauses
   * Default: no (numeric)

   d. **Number of partitions**

   * How many partitions to create
   * Example: `10`, `50`, `100`

### Example Session

```bash
$ sdv snowflake row-partitioning-helper

Generate a configuration file for Snowflake table partitioning. This interactive
helper function processes each table in the configuration file, allowing users to
either skip partitioning or specify partitioning parameters for each table.

Configuration file path: ./configs/snowflake_validation.yaml

Apply partitioning for PROD_DB.PUBLIC.FACT_SALES? [Y/n]: y
Write the partition column for PROD_DB.PUBLIC.FACT_SALES: SALE_ID
Is 'SALE_ID' column a string type? [y/N]: n
Write the number of partitions for PROD_DB.PUBLIC.FACT_SALES: 10

Apply partitioning for PROD_DB.PUBLIC.DIM_CUSTOMER? [Y/n]: n

Apply partitioning for PROD_DB.PUBLIC.TRANSACTIONS? [Y/n]: y
Write the partition column for PROD_DB.PUBLIC.TRANSACTIONS: TRANSACTION_DATE
Is 'TRANSACTION_DATE' column a string type? [y/N]: n
Write the number of partitions for PROD_DB.PUBLIC.TRANSACTIONS: 5

Table partitioning configuration file generated successfully!
```

### Generated Output

The command generates partitioned table configurations with WHERE clauses:

```yaml
tables:
  # Original table partitioned into 10 segments
  - fully_qualified_name: PROD_DB.PUBLIC.FACT_SALES
    where_clause: "SALE_ID >= 1 AND SALE_ID < 100000"
    target_where_clause: "SALE_ID >= 1 AND SALE_ID < 100000"
    # ... other table settings preserved

  - fully_qualified_name: PROD_DB.PUBLIC.FACT_SALES
    where_clause: "SALE_ID >= 100000 AND SALE_ID < 200000"
    target_where_clause: "SALE_ID >= 100000 AND SALE_ID < 200000"
    # ... continues for each partition

  # Non-partitioned table preserved as-is
  - fully_qualified_name: PROD_DB.PUBLIC.DIM_CUSTOMER
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

   * Use clustered columns for better query performance
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
snowflake-data-validation snowflake column-partitioning-helper
```

### Options

This command has no command-line options. All input is provided through interactive prompts.

### How It Works

The column partitioning helper:

1. Reads an existing configuration file with table definitions
2. For each table, prompts whether to apply column partitioning
3. If partitioning is enabled, collects the number of partitions
4. Queries the source Snowflake database to retrieve all column names for the table
5. Divides the columns into the specified number of partitions
6. Generates new table configurations where each partition validates only a subset of columns
7. Saves the partitioned configuration to a new file

### Interactive Prompts

The command will prompt for the following information:

1. **Configuration file path**

   * Path to existing YAML configuration file
   * Example: `./configs/snowflake_validation.yaml`
2. **For each table in the configuration:**

   a. **Apply column partitioning?** (yes/no)

   * Whether to partition this specific table by columns
   * Default: yes

   b. **Number of partitions** (if partitioning)

   * How many column partitions to create
   * Example: `3`, `5`, `10`

### Example Session

```bash
$ sdv snowflake column-partitioning-helper

Generate a configuration file for Snowflake column partitioning. This interactive
helper function processes each table in the configuration file, allowing users to
either skip column partitioning or specify column partitioning parameters for each table.

Configuration file path: ./configs/snowflake_validation.yaml

Apply column partitioning for PROD_DB.PUBLIC.WIDE_TABLE? [Y/n]: y
Write the number of partitions for PROD_DB.PUBLIC.WIDE_TABLE: 5

Apply column partitioning for PROD_DB.PUBLIC.SMALL_TABLE? [Y/n]: n

Apply column partitioning for PROD_DB.PUBLIC.REPORT_TABLE? [Y/n]: y
Write the number of partitions for PROD_DB.PUBLIC.REPORT_TABLE: 3

Column partitioning configuration file generated successfully!
```

### Generated Output

The command generates partitioned table configurations with column subsets:

```yaml
tables:
  # Original table with 100 columns partitioned into 5 segments (20 columns each)
  - fully_qualified_name: PROD_DB.PUBLIC.WIDE_TABLE
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - COLUMN_A
      - COLUMN_B
      - COLUMN_C
      # ... first 20 columns alphabetically

  - fully_qualified_name: PROD_DB.PUBLIC.WIDE_TABLE
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - COLUMN_D
      - COLUMN_E
      - COLUMN_F
      # ... next 20 columns alphabetically
    # ... continues for each partition

  # Non-partitioned table preserved as-is
  - fully_qualified_name: PROD_DB.PUBLIC.SMALL_TABLE
    # ... original configuration
```

### Use Cases

* **Wide table validation**: Break tables with hundreds of columns into manageable chunks
* **Memory optimization**: Reduce memory footprint by validating fewer columns at a time
* **Parallel processing**: Enable concurrent validation of different column groups
* **Targeted validation**: Validate specific column groups independently
* **Performance tuning**: Optimize validation for tables with many VARIANT or complex columns

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

## Snowflake Connection Configuration

Snowflake connections support multiple modes for both source and target databases.

### Connection Modes

#### Option 1: Named Connection

Use a pre-configured Snowflake connection saved in your Snowflake connections file.

```yaml
source_connection:
  mode: name
  name: "my_source_connection"

target_connection:
  mode: name
  name: "my_target_connection"
```

**Fields:**

* **`mode`** (required): Must be `"name"`
* **`name`** (required): Name of the saved Snowflake connection

#### Option 2: Default Connection

Use the default Snowflake connection from your environment.

```yaml
source_connection:
  mode: default

target_connection:
  mode: default
```

**Fields:**

* **`mode`** (required): Must be `"default"`

#### Option 3: Credentials Mode (IPC Only)

> **Note:** The `credentials` mode is only available when using IPC (Inter-Process Communication) commands directly via CLI parameters, not in YAML configuration files. This mode is exclusive to the SnowConvert UI.

### Connection Examples

**Same Account, Different Databases:**

```yaml
source_connection:
  mode: name
  name: prod_connection

target_connection:
  mode: name
  name: prod_connection  # Same connection, different database specified in tables
```

**Cross-Account Validation:**

```yaml
source_connection:
  mode: name
  name: source_account_connection

target_connection:
  mode: name
  name: target_account_connection
```

**Cross-Region Migration:**

```yaml
source_connection:
  mode: name
  name: us_east_connection

target_connection:
  mode: name
  name: eu_west_connection
```

**Development to Production Comparison:**

```yaml
source_connection:
  mode: name
  name: dev_connection

target_connection:
  mode: name
  name: prod_connection
```

### Setting Up Named Connections

Snowflake connections are typically configured using the Snowflake CLI or SnowSQL configuration files.

**SnowSQL Configuration Example (`~/.snowsql/config`):**

```ini
[connections.prod_connection]
accountname = myaccount.us-east-1
username = my_user
password = my_password
dbname = PRODUCTION_DB
schemaname = PUBLIC
warehousename = COMPUTE_WH

[connections.dev_connection]
accountname = myaccount.us-east-1
username = my_user
password = my_password
dbname = DEVELOPMENT_DB
schemaname = PUBLIC
warehousename = DEV_WH
```

**Snowflake CLI Configuration Example (`~/.snowflake/connections.toml`):**

```toml
[prod_connection]
account = "myaccount.us-east-1"
user = "my_user"
password = "my_password"
database = "PRODUCTION_DB"
schema = "PUBLIC"
warehouse = "COMPUTE_WH"

[dev_connection]
account = "myaccount.us-east-1"
user = "my_user"
password = "my_password"
database = "DEVELOPMENT_DB"
schema = "PUBLIC"
warehouse = "DEV_WH"
```

---

## Complete Snowflake Examples

### Example 1: Basic Snowflake-to-Snowflake Configuration

```yaml
# Global configuration
source_platform: Snowflake
target_platform: Snowflake
output_directory_path: ./validation_results
max_threads: auto

# Source connection (development)
source_connection:
  mode: name
  name: dev_connection

# Target connection (production)
target_connection:
  mode: name
  name: prod_connection

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

# Tables to validate
tables:
  - fully_qualified_name: DEV_DB.PUBLIC.CUSTOMERS
    target_database: PROD_DB
    target_schema: PUBLIC
    target_name: CUSTOMERS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - CUSTOMER_ID

  - fully_qualified_name: DEV_DB.PUBLIC.ORDERS
    target_database: PROD_DB
    target_schema: PUBLIC
    target_name: ORDERS
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - INTERNAL_NOTES
      - AUDIT_LOG
```

### Example 2: Cross-Account Migration Validation

```yaml
# Global configuration
source_platform: Snowflake
target_platform: Snowflake
output_directory_path: /opt/validation/cross_account
max_threads: 16

# Source connection (Account A)
source_connection:
  mode: name
  name: account_a_connection

# Target connection (Account B)
target_connection:
  mode: name
  name: account_b_connection

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 200

# Comparison configuration
comparison_configuration:
  tolerance: 0.01

# Logging configuration
logging_configuration:
  level: INFO
  console_level: WARNING
  file_level: DEBUG

# Database mappings (if names differ between accounts)
database_mappings:
  ANALYTICS_A: ANALYTICS_B
  WAREHOUSE_A: WAREHOUSE_B

# Schema mappings
schema_mappings:
  RAW: RAW_DATA
  STAGING: STAGING_DATA

# Tables configuration
tables:
  - fully_qualified_name: ANALYTICS_A.RAW.FACT_SALES
    target_database: ANALYTICS_B
    target_schema: RAW_DATA
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - SALE_ID
    chunk_number: 50
    max_failed_rows_number: 500

  - fully_qualified_name: ANALYTICS_A.RAW.DIM_CUSTOMER
    target_database: ANALYTICS_B
    target_schema: RAW_DATA
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - INTERNAL_SCORE
      - RISK_RATING
    where_clause: "STATUS = 'ACTIVE'"
    target_where_clause: "STATUS = 'ACTIVE'"
    column_mappings:
      CUST_KEY: CUSTOMER_KEY
      CUST_NAME: CUSTOMER_NAME
```

### Example 3: Cross-Region Replication Validation

```yaml
# Global configuration
source_platform: Snowflake
target_platform: Snowflake
output_directory_path: /data/validation/region_replication
max_threads: 24

# Source connection (US East)
source_connection:
  mode: name
  name: us_east_connection

# Target connection (EU West)
target_connection:
  mode: name
  name: eu_west_connection

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 150

# Comparison configuration
comparison_configuration:
  tolerance: 0.005

# Tables configuration
tables:
  # Large fact table with chunking
  - fully_qualified_name: GLOBAL_DB.REPLICATION.TRANSACTIONS
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - TRANSACTION_ID
      - CUSTOMER_ID
      - AMOUNT
      - TRANSACTION_DATE
      - STATUS
    index_column_list:
      - TRANSACTION_ID
    where_clause: "TRANSACTION_DATE >= DATEADD(day, -7, CURRENT_DATE())"
    target_where_clause: "TRANSACTION_DATE >= DATEADD(day, -7, CURRENT_DATE())"
    chunk_number: 30

  # Dimension table
  - fully_qualified_name: GLOBAL_DB.REPLICATION.PRODUCTS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - PRODUCT_ID

  # Reference table
  - fully_qualified_name: GLOBAL_DB.REPLICATION.CURRENCIES
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - CURRENCY_CODE
```

### Example 4: Database Copy Validation

```yaml
# Validate a database copy within the same account
source_platform: Snowflake
target_platform: Snowflake
output_directory_path: ./db_copy_validation
max_threads: auto

# Use the same connection for both
source_connection:
  mode: name
  name: prod_connection

target_connection:
  mode: name
  name: prod_connection

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

# Comparison configuration
comparison_configuration:
  tolerance: 0.001

# Tables to validate (source DB vs copied DB)
tables:
  - fully_qualified_name: ORIGINAL_DB.PUBLIC.USERS
    target_database: COPIED_DB
    target_schema: PUBLIC
    target_name: USERS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - USER_ID

  - fully_qualified_name: ORIGINAL_DB.PUBLIC.EVENTS
    target_database: COPIED_DB
    target_schema: PUBLIC
    target_name: EVENTS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - EVENT_ID
    chunk_number: 20
```

### Example 5: Snowflake View Validation

Validate Snowflake views alongside tables for comprehensive data verification.

```yaml
source_platform: Snowflake
target_platform: Snowflake
output_directory_path: ./snowflake_view_validation
max_threads: auto

source_connection:
  mode: name
  name: source_connection

target_connection:
  mode: name
  name: target_connection

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 50

comparison_configuration:
  tolerance: 0.01

# Tables to validate
tables:
  - fully_qualified_name: ANALYTICS_DB.PUBLIC.CUSTOMERS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [CUSTOMER_ID]
    target_index_column_list: [CUSTOMER_ID]

# Views to validate
views:
  # Basic view validation
  - fully_qualified_name: ANALYTICS_DB.PUBLIC.V_CUSTOMER_SUMMARY
    target_name: V_CUSTOMER_SUMMARY
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [CUSTOMER_ID]
    target_index_column_list: [CUSTOMER_ID]

  # View with specific columns
  - fully_qualified_name: ANALYTICS_DB.PUBLIC.V_SALES_METRICS
    target_name: V_SALES_METRICS
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - REGION
      - TOTAL_SALES
      - ORDER_COUNT
      - AVG_ORDER_VALUE
    index_column_list: [REGION, PERIOD]
    target_index_column_list: [REGION, PERIOD]

  # View with filtering
  - fully_qualified_name: ANALYTICS_DB.PUBLIC.V_ACTIVE_USERS
    target_name: V_ACTIVE_USERS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [USER_ID]
    target_index_column_list: [USER_ID]
    where_clause: "LAST_LOGIN >= DATEADD(day, -30, CURRENT_DATE())"
    target_where_clause: "LAST_LOGIN >= DATEADD(day, -30, CURRENT_DATE())"

  # View with different target name
  - fully_qualified_name: ANALYTICS_DB.PUBLIC.V_LEGACY_REPORT
    target_database: MODERN_DB
    target_schema: REPORTS
    target_name: V_MODERNIZED_REPORT
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [REPORT_ID]
    target_index_column_list: [REPORT_ID]
    column_mappings:
      OLD_COL: NEW_COL
```

**Note:** View validation creates temporary tables internally to materialize view data for comparison between source and target Snowflake databases.

---

## Troubleshooting Snowflake Connections

### Issue: Connection Not Found

**Symptom:**

```sql
Connection 'connection_name' not found
```

**Solutions:**

1. Verify the connection name is correct:

   ```bash
   # List available connections using Snowflake CLI
   snow connection list
   ```

2. Check your Snowflake connections configuration file
3. Ensure the connection file has proper permissions
4. Verify the connection name matches exactly (case-sensitive)

### Issue: Authentication Failed

**Symptom:**

```sql
Authentication failed for user 'username'
```

**Solutions:**

1. Verify credentials are correct
2. Check if using correct authentication method:

   * Password authentication
   * Key pair authentication
   * SSO/OAuth
3. Verify user has necessary permissions:

   ```sql
   -- Grant read permissions
   GRANT USAGE ON DATABASE database_name TO ROLE my_role;
   GRANT USAGE ON SCHEMA database_name.schema_name TO ROLE my_role;
   GRANT SELECT ON ALL TABLES IN SCHEMA database_name.schema_name TO ROLE my_role;
   ```

4. Check if account is correct (including region suffix)

### Issue: Database/Schema Not Found

**Symptom:**

```sql
Database 'DATABASE_NAME' does not exist or not authorized
```

**Solutions:**

1. Verify database/schema names are correct (case-sensitive in Snowflake)
2. Check user has access to the database:

   ```sql
   USE DATABASE database_name;
   USE SCHEMA schema_name;
   SHOW TABLES;
   ```

3. Verify the warehouse is running:

   ```sql
   ALTER WAREHOUSE my_warehouse RESUME;
   ```

### Issue: Cross-Account Access Denied

**Symptom:**

```sql
Access denied to account 'account_name'
```

**Solutions:**

1. Verify both accounts have correct connection configurations
2. Check if data sharing is properly configured between accounts
3. Verify network policies allow cross-account connections
4. Ensure both connections use appropriate credentials

### Issue: Timeout Errors

**Symptom:**

```sql
Query timeout: Operation did not complete within the specified time
```

**Solutions:**

1. Increase warehouse size:

   ```sql
   ALTER WAREHOUSE my_warehouse SET WAREHOUSE_SIZE = 'LARGE';
   ```

2. Enable chunking for large tables:

   ```yaml
   tables:
     - fully_qualified_name: large_table
       chunk_number: 50
   ```

3. Add WHERE clauses to limit data:

   ```yaml
   tables:
     - fully_qualified_name: large_table
       where_clause: "CREATED_DATE >= DATEADD(month, -1, CURRENT_DATE())"
   ```

4. Reduce thread count if warehouse is overloaded:

   ```yaml
   max_threads: 8
   ```

---

## Best Practices for Snowflake-to-Snowflake Validation

### Connection Management

1. **Use named connections:**

   ```yaml
   source_connection:
     mode: name
     name: source_account
   ```

2. **Store credentials securely:**

   * Use Snowflake CLI connection configuration
   * Leverage key pair authentication for production
   * Avoid hardcoding passwords
3. **Use appropriate roles:**

   ```sql
   -- Create a read-only role for validation
   CREATE ROLE validation_reader;
   GRANT USAGE ON DATABASE db_name TO ROLE validation_reader;
   GRANT USAGE ON ALL SCHEMAS IN DATABASE db_name TO ROLE validation_reader;
   GRANT SELECT ON ALL TABLES IN DATABASE db_name TO ROLE validation_reader;
   ```

### Performance Optimization

1. **Size warehouses appropriately:**

   ```sql
   -- Use larger warehouse for big validations
   ALTER WAREHOUSE validation_wh SET WAREHOUSE_SIZE = 'MEDIUM';
   ```

2. **Enable chunking for large tables:**

   ```yaml
   tables:
     - fully_qualified_name: large_table
       chunk_number: 50
   ```

3. **Use WHERE clauses to filter data:**

   ```yaml
   tables:
     - fully_qualified_name: transactions
       where_clause: "TRANSACTION_DATE >= CURRENT_DATE() - 30"
   ```

4. **Optimize thread count:**

   ```yaml
   max_threads: 16  # Adjust based on warehouse capacity
   ```

5. **Consider time-based filtering for incremental validation:**

   ```yaml
   tables:
     - fully_qualified_name: events
       where_clause: "EVENT_TIMESTAMP >= '2024-01-01'"
       target_where_clause: "EVENT_TIMESTAMP >= '2024-01-01'"
   ```

### Data Quality

1. **Start with schema validation:**

   ```yaml
   validation_configuration:
     schema_validation: true
     metrics_validation: false
     row_validation: false
   ```

2. **Progress to metrics validation:**

   ```yaml
   validation_configuration:
     schema_validation: true
     metrics_validation: true
     row_validation: false
   ```

3. **Enable row validation selectively:**

   ```yaml
   validation_configuration:
     row_validation: true

   tables:
     - fully_qualified_name: critical_fact_table
       # Row validation enabled for critical tables
   ```

### Cross-Account/Region Considerations

1. **Account for replication lag:**

   * Allow time for replication to complete before validation
   * Use time-based filters that account for lag
2. **Handle naming differences:**

   ```yaml
   database_mappings:
     SOURCE_DB: TARGET_DB

   schema_mappings:
     SOURCE_SCHEMA: TARGET_SCHEMA
   ```

3. **Monitor costs:**

   * Cross-region data transfer incurs costs
   * Schedule validations during off-peak hours
   * Use sampling for initial validation
4. **Use appropriate tolerance:**

   ```yaml
   comparison_configuration:
     tolerance: 0.01  # Allow for minor differences
   ```

---

## See Also

* [Main CLI Usage Guide](CLI_USAGE_GUIDE.md)
* [SQL Server Commands Reference](sqlserver_commands.md)
* [Teradata Commands Reference](teradata_commands.md)
* [Redshift Commands Reference](redshift_commands.md)
* [Configuration Examples](CONFIGURATION_EXAMPLES.md)
* [Quick Reference Guide](CLI_QUICK_REFERENCE.md)
