# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/data-validation-cli/teradata_commands.md

# Teradata Commands Reference

## Overview

This page provides comprehensive reference documentation for Teradata-specific commands in the Snowflake Data Validation CLI. For SQL Server commands, see [SQL Server Commands Reference](sqlserver_commands.md). For Amazon Redshift commands, see [Redshift Commands Reference](redshift_commands.md). For Snowflake-to-Snowflake commands, see [Snowflake Commands Reference](snowflake_commands.md).

---

## Command Structure

All Teradata commands follow this consistent structure:

```bash
snowflake-data-validation teradata <command> [options]

# Or use the shorter alias
sdv teradata <command> [options]
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

Validates data between Teradata and Snowflake in real-time.

### Syntax

```bash
snowflake-data-validation teradata run-validation \
  --data-validation-config-file /path/to/config.yaml \
  --log-level INFO
```

### Options

**`--data-validation-config-file, -dvf`** (required)

* **Type:** String (path)
* **Description:** Path to YAML configuration file containing validation settings
* **Example:** `--data-validation-config-file ./configs/teradata_validation.yaml`

**`--teradata-host`** (optional)

* **Type:** String
* **Description:** Teradata server hostname (overrides config file)
* **Example:** `--teradata-host teradata.company.com`

**`--teradata-username`** (optional)

* **Type:** String
* **Description:** Teradata username (overrides config file)
* **Example:** `--teradata-username my_user`

**`--teradata-password`** (optional)

* **Type:** String
* **Description:** Teradata password (overrides config file)
* **Example:** `--teradata-password my_password`

**`--teradata-database`** (optional)

* **Type:** String
* **Description:** Teradata database name (overrides config file)
* **Example:** `--teradata-database prod_db`

**`--snowflake-connection-name`** (optional)

* **Type:** String
* **Description:** Snowflake connection name
* **Example:** `--snowflake-connection-name prod_connection`

**`--output-directory`** (optional)

* **Type:** String (path)
* **Description:** Directory for validation results
* **Example:** `--output-directory ./validation_results`

**`--log-level, -ll`** (optional)

* **Type:** String
* **Valid Values:** DEBUG, INFO, WARNING, ERROR, CRITICAL
* **Default:** INFO
* **Description:** Logging level for validation execution
* **Example:** `--log-level DEBUG`

### Example Usage

```bash
# Basic validation using config file
sdv teradata run-validation \
  --data-validation-config-file ./configs/teradata_validation.yaml

# Validation with connection override
sdv teradata run-validation \
  --data-validation-config-file ./config.yaml \
  --teradata-host teradata.company.com \
  --teradata-username my_user \
  --teradata-password my_password \
  --output-directory ./validation_results

# Validation with debug logging
sdv teradata run-validation \
  --data-validation-config-file ./config.yaml \
  --log-level DEBUG

# Using full command name with all options
snowflake-data-validation teradata run-validation \
  -dvf /opt/validations/prod_config.yaml \
  --teradata-host td-prod.company.com \
  --teradata-database production_db \
  --snowflake-connection-name snowflake_prod \
  --output-directory /data/validation_results \
  -ll INFO
```

### Use Cases

* Real-time validation during Teradata migration
* Pre-cutover validation checks
* Post-migration verification
* Continuous validation in CI/CD pipelines
* Testing with temporary credentials

---

## Generate Validation Scripts

Generates SQL scripts for Teradata and Snowflake metadata extraction.

### Syntax

```bash
snowflake-data-validation teradata generate-validation-scripts \
  /path/to/config.yaml \
  --output-directory ./scripts
```

### Positional Arguments

**`config_file`** (required)

* **Type:** String (path)
* **Description:** Path to YAML configuration file
* **Example:** `./configs/validation.yaml`

### Options

**`--teradata-host`** (optional)

* **Type:** String
* **Description:** Teradata server hostname (overrides config file)
* **Example:** `--teradata-host teradata.company.com`

**`--teradata-username`** (optional)

* **Type:** String
* **Description:** Teradata username (overrides config file)
* **Example:** `--teradata-username script_generator`

**`--teradata-password`** (optional)

* **Type:** String
* **Description:** Teradata password (overrides config file)
* **Example:** `--teradata-password secure_password`

**`--teradata-database`** (optional)

* **Type:** String
* **Description:** Teradata database name (overrides config file)
* **Example:** `--teradata-database analytics_db`

**`--output-directory`** (optional)

* **Type:** String (path)
* **Description:** Directory for generated scripts
* **Example:** `--output-directory ./generated_scripts`

### Example Usage

```bash
# Basic script generation
sdv teradata generate-validation-scripts \
  ./configs/validation.yaml

# Script generation with connection override
sdv teradata generate-validation-scripts \
  ./config.yaml \
  --teradata-host teradata.company.com \
  --teradata-username script_user \
  --teradata-password script_password \
  --output-directory ./scripts

# Script generation to specific directory
sdv teradata generate-validation-scripts \
  /opt/configs/prod_validation.yaml \
  --output-directory /data/validation_scripts

# Using full command name
snowflake-data-validation teradata generate-validation-scripts \
  ./config.yaml \
  --teradata-database production_db \
  --output-directory ./generated_scripts
```

### Output

The command generates SQL scripts in the specified output directory:

```text
<output_directory>/
├── teradata_schema_queries.sql
├── teradata_metrics_queries.sql
├── teradata_row_queries.sql
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

## Run Asynchronous Validation

Performs validation using pre-generated metadata files without connecting to databases.

### Syntax

```bash
snowflake-data-validation teradata run-async-validation \
  /path/to/config.yaml \
  --output-directory ./validation_results
```

### Positional Arguments

**`config_file`** (required)

* **Type:** String (path)
* **Description:** Path to YAML configuration file
* **Example:** `./configs/async_validation.yaml`

### Options

**`--output-directory`** (optional)

* **Type:** String (path)
* **Description:** Directory containing metadata files generated from scripts
* **Example:** `--output-directory ./metadata_files`

### Example Usage

```bash
# Run async validation
sdv teradata run-async-validation \
  ./configs/async_validation.yaml

# Run async validation with specific metadata directory
sdv teradata run-async-validation \
  ./config.yaml \
  --output-directory ./validation_metadata

# Using full command name
snowflake-data-validation teradata run-async-validation \
  /opt/configs/validation.yaml \
  --output-directory /data/validation_metadata
```

### Prerequisites

Before running async validation:

1. Generate validation scripts using `generate-validation-scripts`
2. Execute the generated scripts on Teradata and Snowflake databases
3. Save results to CSV/metadata files
4. Ensure metadata files are available in the configured paths

### Use Cases

* Validating in environments with restricted database access
* Separating metadata extraction from validation
* Batch validation workflows
* Scheduled validation jobs
* When database connections are intermittent

---

## Get Configuration Templates

Retrieves Teradata configuration templates.

### Syntax

```bash
snowflake-data-validation teradata get-configuration-files \
  --templates-directory ./teradata-templates \
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
sdv teradata get-configuration-files

# Save templates to specific directory
sdv teradata get-configuration-files \
  --templates-directory ./my-project/teradata-templates

# Include query templates for customization
sdv teradata get-configuration-files \
  --templates-directory ./templates \
  --query-templates

# Using short flags
sdv teradata get-configuration-files -td ./templates --query-templates
```

### Output Files

**Without `--query-templates` flag:**

```text
<templates_directory>/
└── teradata_validation_template.yaml
```

**With `--query-templates` flag:**

```text
<templates_directory>/
├── teradata_validation_template.yaml
└── query_templates/
    ├── teradata_columns_metrics_query.sql.j2
    ├── teradata_row_count_query.sql.j2
    ├── teradata_compute_md5_sql.j2
    └── snowflake_columns_metrics_query.sql.j2
```

### Use Cases

* Starting a new Teradata validation project
* Learning Teradata-specific configuration options
* Customizing validation queries for Teradata
* Creating organization-specific templates

---

## Auto-Generate Configuration File

Interactive command for Teradata configuration generation.

### Syntax

```bash
snowflake-data-validation teradata auto-generated-configuration-file
```

### Options

This command has no command-line options. All input is provided through interactive prompts.

### Interactive Prompts

The command will prompt for the following information:

1. **Teradata host**

   * Hostname or IP address of Teradata server
   * Example: `teradata.company.com`
2. **Teradata username**

   * Authentication username
   * Example: `migration_user`
3. **Teradata password**

   * Authentication password (hidden input)
   * Not displayed on screen for security
4. **Teradata database**

   * Name of the database to validate
   * Example: `production_db`
5. **Output directory path**

   * Where to save validation results
   * Example: `./validation_results`

### Example Session

```bash
$ sdv teradata auto-generated-configuration-file

Teradata host: teradata.company.com
Teradata username: migration_user
Teradata password: ********
Teradata database: production_db
Output directory path: ./validation_results

Configuration file generated successfully: ./teradata_validation_config.yaml
```

### Generated Configuration

The command generates a basic YAML configuration file:

```yaml
source_platform: Teradata
target_platform: Snowflake
output_directory_path: ./validation_results
target_database: PRODUCTION_DB

source_connection:
  mode: credentials
  host: teradata.company.com
  username: migration_user
  password: "<hidden>"
  database: production_db

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
2. **Add table configurations:**

   * Specify fully qualified table names
   * Configure column selections
   * Set up filtering where clauses
3. **Review Teradata-specific settings:**

   * Verify target_database is correctly set
   * Check schema mappings if needed
4. **Test the configuration:**

   ```bash
   sdv teradata run-validation \
     --data-validation-config-file ./teradata_validation_config.yaml
   ```

### Use Cases

* Quick setup for new Teradata users
* Generating baseline configurations
* Testing connectivity during setup
* Creating template configurations for teams

---

## Row Partitioning Helper

Interactive command to generate partitioned table configurations for large tables. This helper divides tables into smaller row partitions based on a specified column, enabling more efficient validation of large datasets.

### Syntax

```bash
snowflake-data-validation teradata row-partitioning-helper
```

### Options

This command has no command-line options. All input is provided through interactive prompts.

### How It Works

The table partitioning helper:

1. Reads an existing configuration file with table definitions
2. For each table, prompts whether to apply partitioning
3. If partitioning is enabled, collects partition parameters
4. Queries the source Teradata database to determine partition boundaries
5. Generates new table configurations with `WHERE` clauses for each partition
6. Saves the partitioned configuration to a new file

### Interactive Prompts

The command will prompt for the following information:

1. **Configuration file path**

   * Path to existing YAML configuration file
   * Example: `./configs/teradata_validation.yaml`
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
$ sdv teradata row-partitioning-helper

Generate a configuration file for Teradata table partitioning. This interactive
helper function processes each table in the configuration file, allowing users to
either skip partitioning or specify partitioning parameters for each table.

Configuration file path: ./configs/teradata_validation.yaml

Apply partitioning for enterprise_db.fact_sales? [Y/n]: y
Write the partition column for enterprise_db.fact_sales: sale_id
Is 'sale_id' column a string type? [y/N]: n
Write the number of partitions for enterprise_db.fact_sales: 10

Apply partitioning for enterprise_db.dim_customer? [Y/n]: n

Apply partitioning for enterprise_db.transactions? [Y/n]: y
Write the partition column for enterprise_db.transactions: transaction_date
Is 'transaction_date' column a string type? [y/N]: n
Write the number of partitions for enterprise_db.transactions: 5

Table partitioning configuration file generated successfully!
```

### Generated Output

The command generates partitioned table configurations with WHERE clauses:

```yaml
tables:
  # Original table partitioned into 10 segments
  - fully_qualified_name: enterprise_db.fact_sales
    where_clause: "sale_id >= 1 AND sale_id < 100000"
    target_where_clause: "sale_id >= 1 AND sale_id < 100000"
    # ... other table settings preserved

  - fully_qualified_name: enterprise_db.fact_sales
    where_clause: "sale_id >= 100000 AND sale_id < 200000"
    target_where_clause: "sale_id >= 100000 AND sale_id < 200000"
    # ... continues for each partition

  # Non-partitioned table preserved as-is
  - fully_qualified_name: enterprise_db.dim_customer
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
snowflake-data-validation teradata column-partitioning-helper
```

### Options

This command has no command-line options. All input is provided through interactive prompts.

### How It Works

The column partitioning helper:

1. Reads an existing configuration file with table definitions
2. For each table, prompts whether to apply column partitioning
3. If partitioning is enabled, collects the number of partitions
4. Queries the source Teradata database to retrieve all column names for the table
5. Divides the columns into the specified number of partitions
6. Generates new table configurations where each partition validates only a subset of columns
7. Saves the partitioned configuration to a new file

### Interactive Prompts

The command will prompt for the following information:

1. **Configuration file path**

   * Path to existing YAML configuration file
   * Example: `./configs/teradata_validation.yaml`
2. **For each table in the configuration:**

   a. **Apply column partitioning?** (yes/no)

   * Whether to partition this specific table by columns
   * Default: yes

   b. **Number of partitions** (if partitioning)

   * How many column partitions to create
   * Example: `3`, `5`, `10`

### Example Session

```bash
$ sdv teradata column-partitioning-helper

Generate a configuration file for Teradata column partitioning. This interactive
helper function processes each table in the configuration file, allowing users to
either skip column partitioning or specify column partitioning parameters for each table.

Configuration file path: ./configs/teradata_validation.yaml

Apply column partitioning for enterprise_db.wide_table? [Y/n]: y
Write the number of partitions for enterprise_db.wide_table: 5

Apply column partitioning for enterprise_db.small_table? [Y/n]: n

Apply column partitioning for enterprise_db.report_table? [Y/n]: y
Write the number of partitions for enterprise_db.report_table: 3

Column partitioning configuration file generated successfully!
```

### Generated Output

The command generates partitioned table configurations with column subsets:

```yaml
tables:
  # Original table with 100 columns partitioned into 5 segments (20 columns each)
  - fully_qualified_name: enterprise_db.wide_table
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - column_a
      - column_b
      - column_c
      # ... first 20 columns alphabetically

  - fully_qualified_name: enterprise_db.wide_table
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - column_d
      - column_e
      - column_f
      # ... next 20 columns alphabetically
    # ... continues for each partition

  # Non-partitioned table preserved as-is
  - fully_qualified_name: enterprise_db.small_table
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

## Teradata Connection Configuration

Teradata connections require specific configuration in the YAML file.

### Connection Example

```yaml
source_connection:
  mode: credentials
  host: "teradata.company.com"
  username: "teradata_user"
  password: "secure_password"
  database: "source_database"
```

### Connection Fields

**`mode`** (required)

* **Type:** String
* **Valid Values:** `credentials`
* **Description:** Connection mode for Teradata

**`host`** (required)

* **Type:** String
* **Description:** Teradata hostname or IP address
* **Examples:**

  * `"teradata.company.com"`
  * `"td-prod.internal.company.net"`
  * `"192.168.1.50"`

**`username`** (required)

* **Type:** String
* **Description:** Teradata authentication username
* **Example:** `"migration_admin"`

**`password`** (required)

* **Type:** String
* **Description:** Teradata authentication password
* **Security Note:** Consider using environment variables

**`database`** (required)

* **Type:** String
* **Description:** Teradata database name
* **Example:** `"production_database"`

### Teradata-Specific Global Configuration

**`target_database`** (required for Teradata)

* **Type:** String
* **Description:** Target database name in Snowflake for Teradata validations
* **Example:** `target_database: PROD_DB`
* **Note:** This is required in the global configuration section, not the connection section

### Connection Examples

**Production Connection:**

```yaml
source_connection:
  mode: credentials
  host: "td-prod.company.com"
  username: "prod_reader"
  password: "${TERADATA_PASSWORD}"  # From environment variable
  database: "production_db"

target_database: PROD_SNOWFLAKE_DB
```

**Development Connection:**

```yaml
source_connection:
  mode: credentials
  host: "td-dev.company.local"
  username: "dev_user"
  password: "dev_password"
  database: "dev_database"

target_database: DEV_SNOWFLAKE_DB
```

**Multi-Database Setup:**

```yaml
source_connection:
  mode: credentials
  host: "teradata.company.com"
  username: "migration_user"
  password: "secure_password"
  database: "primary_db"

target_database: ENTERPRISE_DATA_DB

database_mappings:
  primary_db: ENTERPRISE_DATA_DB
  secondary_db: ANALYTICS_DB
```

---

## Complete Teradata Examples

### Example 1: Basic Teradata Configuration

```yaml
# Global configuration
source_platform: Teradata
target_platform: Snowflake
output_directory_path: ./validation_results
max_threads: auto
target_database: PROD_DB

# Source connection
source_connection:
  mode: credentials
  host: teradata.company.com
  username: teradata_user
  password: teradata_password
  database: prod_db

# Target connection
target_connection:
  mode: default

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

# Schema mappings
schema_mappings:
  prod_db: PUBLIC

# Tables configuration
tables:
  - fully_qualified_name: prod_db.sales_data
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - transaction_id

  - fully_qualified_name: prod_db.customer_master
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - ssn
      - credit_card
```

### Example 2: Teradata Large-Scale Migration

```yaml
# Global configuration
source_platform: Teradata
target_platform: Snowflake
output_directory_path: /opt/validation/results
max_threads: 16
target_database: PROD_SNOWFLAKE

# Source connection
source_connection:
  mode: credentials
  host: td-prod.company.com
  username: migration_admin
  password: secure_password
  database: enterprise_db

# Target connection
target_connection:
  mode: name
  name: snowflake_enterprise

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 200
  exclude_metrics: false

# Comparison configuration
comparison_configuration:
  tolerance: 0.01

# Logging configuration
logging_configuration:
  level: INFO
  console_level: WARNING
  file_level: DEBUG

# Schema mappings
schema_mappings:
  enterprise_db: PUBLIC

# Tables configuration
tables:
  - fully_qualified_name: enterprise_db.fact_sales
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - sale_id
      - customer_id
      - product_id
      - sale_amount
      - sale_date
    index_column_list:
      - sale_id
    chunk_number: 50
    max_failed_rows_number: 500

  - fully_qualified_name: enterprise_db.dim_customer
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - internal_notes
      - audit_fields
    where_clause: "status = 'ACTIVE'"
    target_where_clause: "status = 'ACTIVE'"
    column_mappings:
      cust_key: customer_key
      cust_name: customer_name
```

### Example 3: Teradata Multi-Schema Validation

```yaml
source_platform: Teradata
target_platform: Snowflake
output_directory_path: /data/validation/multi_schema
max_threads: 24
target_database: MULTI_SCHEMA_DB

source_connection:
  mode: credentials
  host: teradata.company.com
  username: multi_schema_user
  password: password123
  database: main_db

target_connection:
  mode: default

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

comparison_configuration:
  tolerance: 0.005

schema_mappings:
  sales_schema: SALES
  finance_schema: FINANCE
  hr_schema: HUMAN_RESOURCES

tables:
  # Sales schema tables
  - fully_qualified_name: main_db.sales_schema.orders
    target_schema: SALES
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - order_id

  - fully_qualified_name: main_db.sales_schema.customers
    target_schema: SALES
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - customer_id

  # Finance schema tables
  - fully_qualified_name: main_db.finance_schema.transactions
    target_schema: FINANCE
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - internal_ref_number
    index_column_list:
      - transaction_id
    where_clause: "fiscal_year >= 2024"
    target_where_clause: "fiscal_year >= 2024"

  # HR schema tables
  - fully_qualified_name: main_db.hr_schema.employees
    target_schema: HUMAN_RESOURCES
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - ssn
      - salary
      - bank_account
    index_column_list:
      - employee_id
```

### Example 4: Teradata View Validation

Validate Teradata views alongside tables for comprehensive migration verification.

```yaml
source_platform: Teradata
target_platform: Snowflake
output_directory_path: ./teradata_view_validation
target_database: SNOWFLAKE_DW
max_threads: auto

source_connection:
  mode: credentials
  host: teradata.company.com
  username: td_validator
  password: TeradataPass123!
  database: DW_DB

target_connection:
  mode: name
  name: snowflake_dw

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true

schema_mappings:
  DW_DB: PUBLIC

# Tables to validate
tables:
  - fully_qualified_name: DW_DB.CUSTOMERS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [CUSTOMER_ID]
    target_index_column_list: [CUSTOMER_ID]

# Views to validate
views:
  # Basic view validation with sensitive column exclusion
  - fully_qualified_name: DW_DB.V_CUSTOMER_360
    target_name: V_CUSTOMER_360
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - SSN
      - CREDIT_SCORE
    index_column_list: [CUSTOMER_ID]
    target_index_column_list: [CUSTOMER_ID]

  # View with specific columns
  - fully_qualified_name: DW_DB.V_SALES_DASHBOARD
    target_name: V_SALES_DASHBOARD
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - REGION
      - QUARTER
      - TOTAL_SALES
      - ORDER_COUNT
      - AVG_ORDER_VALUE
    index_column_list: [REGION, QUARTER]
    target_index_column_list: [REGION, QUARTER]

  # View with filtering
  - fully_qualified_name: DW_DB.V_INVENTORY_STATUS
    target_name: V_INVENTORY_STATUS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [INVENTORY_ID]
    target_index_column_list: [INVENTORY_ID]
    where_clause: "status = 'ACTIVE'"
    target_where_clause: "status = 'ACTIVE'"

  # View with different target name
  - fully_qualified_name: DW_DB.V_LEGACY_REPORT
    target_database: MODERN_DW
    target_schema: ANALYTICS
    target_name: V_MODERNIZED_REPORT
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list: [REPORT_ID]
    target_index_column_list: [REPORT_ID]
    column_mappings:
      OLD_COL: NEW_COL
```

**Note:** View validation creates temporary tables internally to materialize view data for comparison between Teradata and Snowflake.

---

## Troubleshooting Teradata Connections

### Issue: Connection Timeout

**Symptom:**

```sql
Connection timeout: Unable to connect to Teradata
```

**Solutions:**

1. Verify the host and network connectivity:

   ```bash
   telnet teradata.company.com 1025
   ```

2. Check firewall rules allow Teradata connections
3. Verify Teradata server is running
4. Test connection with Teradata SQL Assistant or other client tools

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
   GRANT SELECT ON database_name TO migration_user;
   ```

3. Verify user account is not locked
4. Check password hasn’t expired

### Issue: Database Not Found

**Symptom:**

```sql
Database 'database_name' does not exist
```

**Solutions:**

1. Verify database name is correct (case-sensitive)
2. Check user has access to the database:

   ```sql
   DATABASE database_name;
   SHOW TABLES;
   ```

3. Ensure database exists and is accessible

### Issue: Target Database Configuration Missing

**Symptom:**

```sql
target_database configuration is required for Teradata validations
```

**Solution:**

Add `target_database` to global configuration:

```yaml
source_platform: Teradata
target_platform: Snowflake
target_database: TARGET_DB_NAME  # Add this line
```

### Issue: Schema Mapping Errors

**Symptom:**

```sql
Schema not found in target
```

**Solution:**

Add schema mappings in configuration:

```yaml
schema_mappings:
  source_schema: TARGET_SCHEMA
  prod_db: PUBLIC
```

---

## Best Practices for Teradata

### Configuration

1. **Always specify target_database:**

   ```yaml
   target_database: SNOWFLAKE_DB_NAME
   ```

2. **Use schema mappings:**

   ```yaml
   schema_mappings:
     teradata_schema: snowflake_schema
   ```

3. **Handle case sensitivity:**

   ```yaml
   tables:
     - fully_qualified_name: db.schema.TABLE_NAME
       is_case_sensitive: true
   ```

### Security

1. **Use environment variables for passwords:**

   ```yaml
   source_connection:
     password: "${TERADATA_PASSWORD}"
   ```

2. **Use read-only accounts:**

   ```sql
   CREATE USER migration_reader AS PASSWORD = secure_password;
   GRANT SELECT ON database_name TO migration_reader;
   ```

3. **Restrict column access for sensitive data:**

   ```yaml
   tables:
     - fully_qualified_name: sensitive_table
       use_column_selection_as_exclude_list: true
       column_selection_list:
         - ssn
         - credit_card
         - salary
   ```

### Performance

1. **Enable chunking for large tables:**

   ```yaml
   tables:
     - fully_qualified_name: large_table
       chunk_number: 100
   ```

2. **Use WHERE clauses to filter data:**

   ```yaml
   tables:
     - fully_qualified_name: transactions
       where_clause: "transaction_date >= DATE '2024-01-01'"
   ```

3. **Optimize thread count:**

   ```yaml
   max_threads: 16  # Adjust based on Teradata server capacity
   ```

4. **Exclude unnecessary metrics for very large tables:**

   ```yaml
   validation_configuration:
     exclude_metrics: true  # Excludes avg, sum, stddev, variance
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

3. **Enable row validation for critical tables:**

   ```yaml
   tables:
     - fully_qualified_name: critical_fact_table
       # Row validation will be performed

   validation_configuration:
     row_validation: true
   ```

---

## See Also

* [Main CLI Usage Guide](CLI_USAGE_GUIDE.md)
* [SQL Server Commands Reference](sqlserver_commands.md)
* [Redshift Commands Reference](redshift_commands.md)
* [Snowflake Commands Reference](snowflake_commands.md)
* [Configuration Examples](CONFIGURATION_EXAMPLES.md)
* [Quick Reference Guide](CLI_QUICK_REFERENCE.md)
