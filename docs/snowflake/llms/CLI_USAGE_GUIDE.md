# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/data-validation-cli/CLI_USAGE_GUIDE.md

# Snowflake Data Validation CLI - Complete Usage Guide

## Overview

The Snowflake Data Validation CLI (`snowflake-data-validation` or `sdv`) is a comprehensive command-line tool for validating data migrations between source databases (SQL Server, Teradata, Amazon Redshift) and Snowflake. It provides multi-level validation strategies to ensure data consistency and quality.

### Key Features

* **Multi-Level Validation**: Schema, statistical metrics, and row-by-row data validation
* **Multiple Source Platforms**: SQL Server, Teradata, and Amazon Redshift
* **Tables and Views Validation**: Validate both tables and database views
* **Flexible Execution Modes**: Synchronous, asynchronous, and script generation
* **Comprehensive Configuration**: YAML-based configuration with extensive customization options
* **Detailed Reporting**: Comprehensive validation reports with mismatch information

---

## Prerequisites

Before installing the Snowflake Data Validation CLI, ensure you have the following prerequisites installed:

### System Requirements

* **Python**: Version 3.8 or higher
* **pip**: Latest version recommended
* **Operating System**: Linux, macOS, or Windows

### ODBC Drivers

The CLI requires appropriate ODBC drivers to be installed on your system for connecting to source databases. Install the ODBC driver that matches your source database dialect:

#### SQL Server ODBC Driver

For SQL Server as a source database, you need the **Microsoft ODBC Driver for SQL Server**.

**Recommended Version**: ODBC Driver 17 or 18 for SQL Server

**Installation Instructions:**

* **Linux**:

  ```bash
  # Ubuntu/Debian
  curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
  curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
  apt-get update
  ACCEPT_EULA=Y apt-get install -y msodbcsql18
  ```

* **macOS**:

  ```bash
  # Using Homebrew
  brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
  brew update
  HOMEBREW_ACCEPT_EULA=Y brew install msodbcsql18
  ```

* **Windows**:
  Download and install from [Microsoft’s official download page](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)

**Verification:**

```bash
# List available drivers (should show ODBC Driver 17 or 18 for SQL Server)
odbcinst -q -d
```

**Documentation**: [Microsoft ODBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/odbc/microsoft-odbc-driver-for-sql-server)

#### Teradata ODBC Driver

For Teradata as a source database, you need the **Teradata ODBC Driver**.

**Recommended Version**: Teradata ODBC Driver 17.20 or higher

**Installation Instructions:**

1. Download the Teradata Tools and Utilities (TTU) package from [Teradata Downloads](https://downloads.teradata.com/)
2. Select your operating system and download the appropriate installer
3. Run the installer and select “ODBC Driver” during installation
4. Configure the driver according to Teradata’s documentation

**Note**: You may need to create a Teradata account to access the download page.

**Configuration:**
After installation, you may need to configure the ODBC driver:

* **Linux/macOS**: Edit `/etc/odbc.ini` and `/etc/odbcinst.ini`
* **Windows**: Use the ODBC Data Source Administrator

**Documentation**: [Teradata ODBC Driver Documentation](https://downloads.teradata.com/download/connectivity/odbc-driver/linux)

#### Amazon Redshift ODBC Driver

For Amazon Redshift as a source database, you need the **Amazon Redshift ODBC Driver** or a **PostgreSQL ODBC Driver** (since Redshift is PostgreSQL-compatible).

**Option 1: Amazon Redshift ODBC Driver (Recommended)**

**Recommended Version**: Amazon Redshift ODBC Driver 2.x

**Installation Instructions:**

* Download from [Amazon Redshift ODBC Driver Download](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-odbc-connection.html)
* Choose your operating system and architecture
* Follow the installation wizard

**Option 2: PostgreSQL ODBC Driver (Alternative)**

* **Linux**:

  ```bash
  # Ubuntu/Debian
  sudo apt-get install odbc-postgresql

  # RHEL/CentOS/Fedora
  sudo yum install postgresql-odbc
  ```

* **macOS**:

  ```bash
  # Using Homebrew
  brew install psqlodbc
  ```

* **Windows**:
  Download from [PostgreSQL ODBC Driver](https://www.postgresql.org/ftp/odbc/versions/)

**Verification:**

```bash
# List available drivers (should show Amazon Redshift or PostgreSQL drivers)
odbcinst -q -d
```

**Documentation**: [Amazon Redshift ODBC Driver Documentation](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-odbc-connection.html)

### Additional Tools (Optional)

* **unixODBC** (Linux/macOS): Required for ODBC driver management

  ```bash
  # Ubuntu/Debian
  sudo apt-get install unixodbc unixodbc-dev

  # macOS
  brew install unixodbc

  # RHEL/CentOS/Fedora
  sudo yum install unixODBC unixODBC-devel
  ```

### Network Access

Ensure your environment has network access to:

* Source database (SQL Server, Teradata, or Redshift)
* Snowflake account
* Package repositories (for pip installation)

---

## Installation

### Base Installation

```bash
pip install snowflake-data-validation
```

### Source-Specific Installation

Install with the appropriate database driver for your source system:

```bash
# For SQL Server as source
pip install "snowflake-data-validation[sqlserver]"

# For Teradata as source
pip install "snowflake-data-validation[teradata]"

# For Amazon Redshift as source
pip install "snowflake-data-validation[redshift]"

# For development with all drivers
pip install "snowflake-data-validation[all]"
```

### Post-Installation Verification

After installation, verify the CLI is correctly installed:

```bash
# Check version
snowflake-data-validation --version

# Or using the alias
sdv --version

# Verify ODBC drivers are accessible
odbcinst -q -d
```

---

## Quick Start

### 1. Generate a Configuration Template

```bash
# Get SQL Server configuration templates
snowflake-data-validation sqlserver get-configuration-files

# Get Teradata configuration templates
snowflake-data-validation teradata get-configuration-files

# Get Redshift configuration templates
snowflake-data-validation redshift get-configuration-files
```

### 2. Auto-Generate Configuration from Connection

```bash
# Interactive configuration generation for SQL Server
snowflake-data-validation sqlserver auto-generated-configuration-file

# Interactive configuration generation for Teradata
snowflake-data-validation teradata auto-generated-configuration-file

# Interactive configuration generation for Redshift
snowflake-data-validation redshift auto-generated-configuration-file
```

### 3. Run Validation

```bash
# Run synchronous validation
snowflake-data-validation sqlserver run-validation \
  --data-validation-config-file ./config/validation_config.yaml
```

---

## Best Practices & Guidance

This section provides strategic guidance on how to approach data validation effectively, minimize resource consumption, and identify issues early.

### Incremental Validation Approach

> **Note:**
>
> Always start small and scale up incrementally. Running full validation on large datasets immediately can:
>
> * Consume significant compute resources on both source and target systems
> * Take hours or days to complete
> * Make troubleshooting difficult if issues are found
> * Impact production systems if run during business hours

### Recommended Validation Strategy

Follow this proven approach to ensure efficient and effective validation:

#### Phase 1: Start with a Sample Dataset

**Goal**: Verify configuration and establish baseline

**Approach**:

* Test with 1-2 small tables first (< 100,000 rows)
* Choose tables with diverse data types to validate type mapping
* Verify connectivity and authentication work correctly
* Confirm output format meets your needs

**Example Configuration**:

```yaml
tables:
  - source_table_name: "small_reference_table"
    target_table_name: "small_reference_table"
    source_schema_name: "dbo"
    target_schema_name: "PUBLIC"
    target_database_name: "MIGRATION_DB"
    where_clause: "reference_id <= 1000"  # Limit to first 1000 rows on source
    target_where_clause: "reference_id <= 1000"  # Limit to first 1000 rows on target
    validations:
      - validation_type: "row_count"
      - validation_type: "column_level"
```

**What to Verify**:

* ✅ Connection to both source and target successful
* ✅ Schema validation passes
* ✅ Row count matches
* ✅ Data types mapped correctly
* ✅ Validation report generated successfully

**Understanding `where_clause` vs `target_where_clause`**:

The tool provides two filtering options:

* **`where_clause`**: Applied **only** to the **source** table

  ```yaml
  where_clause: "ProductID <= 45"  # Filters only the source table
  ```

* **`target_where_clause`**: Applied **only** to the **target** table (Snowflake)

  ```yaml
  target_where_clause: "ProductID <= 45"  # Filters only the target table
  ```

**Common Usage Patterns**:

```yaml
# Pattern 1: Apply same filter to both source and target
tables:
  - source_table_name: "products"
    where_clause: "ProductID <= 100"           # Filter source
    target_where_clause: "ProductID <= 100"     # Filter target with same condition
    validations:
      - validation_type: "row_count"
      - validation_type: "column_level"

# Pattern 2: Different filters for source and target
# Useful when target has additional test data to exclude
tables:
  - source_table_name: "products"
    where_clause: "ProductID <= 100"                    # Filter source
    target_where_clause: "ProductID <= 100 AND ProductID != 5"  # Exclude test data in target
    validations:
      - validation_type: "row_count"
      - validation_type: "column_level"

# Pattern 3: Filter only source (validate all target data)
tables:
  - source_table_name: "products"
    where_clause: "ProductID <= 100"  # Only validate subset from source
    # No target_where_clause - validates all matching rows in target
    validations:
      - validation_type: "row_count"
```

#### Phase 2: Verify Small Subsets of Production Tables

**Goal**: Test against actual production data patterns with limited scope

**Approach**:

* Select a subset of rows from production tables (10,000 - 100,000 rows)
* Use `where_clause` and `target_where_clause` to restrict data
* Focus on recent data or specific partitions
* Validate critical business columns first

**Example Configuration**:

```yaml
tables:
  - source_table_name: "large_transactions_table"
    target_table_name: "large_transactions_table"
    source_schema_name: "sales"
    target_schema_name: "SALES"
    target_database_name: "MIGRATION_DB"
    where_clause: "transaction_date >= '2024-01-01' AND transaction_date < '2024-02-01'"
    target_where_clause: "transaction_date >= '2024-01-01' AND transaction_date < '2024-02-01'"
    validations:
      - validation_type: "row_count"
      - validation_type: "column_level"
        columns_to_validate:
          - "transaction_id"
          - "amount"
          - "customer_id"
          - "transaction_date"
```

**Key Points**:

* 🎯 Use date ranges or ID ranges to limit scope
* 🎯 Test different data patterns (recent vs. historical, high-volume dates)
* 🎯 Validate critical business columns before validating all columns

#### Phase 3: Partition-Based Validation for Large Tables

**Goal**: Validate large tables efficiently using partitioning strategy

**⚠️ IMPORTANT**: For tables with millions or billions of rows, validating the entire table at once is:

* Resource-intensive (high compute costs)
* Time-consuming (can take hours/days)
* Risky (harder to identify specific issue patterns)

**Recommended Approach for Large Tables**:

**Strategy 1: Date-Based Partitioning**

Validate data in chunks based on date ranges:

```yaml
# Validation 1: January 2024
tables:
  - source_table_name: "orders"
    target_table_name: "orders"
    source_schema_name: "dbo"
    target_schema_name: "PUBLIC"
    target_database_name: "MIGRATION_DB"
    where_clause: "order_date >= '2024-01-01' AND order_date < '2024-02-01'"
    target_where_clause: "order_date >= '2024-01-01' AND order_date < '2024-02-01'"
    validations:
      - validation_type: "row_count"
      - validation_type: "column_level"

# Validation 2: February 2024
# Create separate config with:
# where_clause: "order_date >= '2024-02-01' AND order_date < '2024-03-01'"
# target_where_clause: "order_date >= '2024-02-01' AND order_date < '2024-03-01'"
```

**Strategy 2: Modulo-Based Sampling**

Use modulo arithmetic to sample evenly distributed rows:

```yaml
tables:
  - source_table_name: "customers"
    target_table_name: "customers"
    source_schema_name: "dbo"
    target_schema_name: "PUBLIC"
    target_database_name: "MIGRATION_DB"
    where_clause: "customer_id % 100 = 0"  # 1% sample - evenly distributed
    target_where_clause: "customer_id % 100 = 0"
    validations:
      - validation_type: "row_count"
      - validation_type: "column_level"
```

**Strategy 3: Statistical Sampling**

For very large tables (> 100M rows), validate representative samples:

```yaml
tables:
  - source_table_name: "clickstream_events"
    target_table_name: "clickstream_events"
    source_schema_name: "dbo"
    target_schema_name: "PUBLIC"
    target_database_name: "MIGRATION_DB"
    where_clause: "event_id % 10000 = 0"  # ~0.01% sample - statistically distributed
    target_where_clause: "event_id % 10000 = 0"
    validations:
      # First: Validate aggregates and row count (fast)
      - validation_type: "row_count"
      - validation_type: "aggregate_metrics"

      # Second: Validate a statistical sample of rows
      - validation_type: "column_level"
```

**Strategy 4: Progressive Partition Validation**

Validate multiple partitions progressively:

```yaml
# config_q1.yaml - Validate Q1 2024
tables:
  - source_table_name: "orders"
    target_table_name: "orders"
    where_clause: "order_date >= '2024-01-01' AND order_date < '2024-04-01'"
    target_where_clause: "order_date >= '2024-01-01' AND order_date < '2024-04-01'"
    validations:
      - validation_type: "row_count"
      - validation_type: "column_level"

# config_q2.yaml - Validate Q2 2024 (run after Q1 passes)
tables:
  - source_table_name: "orders"
    target_table_name: "orders"
    where_clause: "order_date >= '2024-04-01' AND order_date < '2024-07-01'"
    target_where_clause: "order_date >= '2024-04-01' AND order_date < '2024-07-01'"
    validations:
      - validation_type: "row_count"
      - validation_type: "column_level"
```

```bash
# Validate Q1 2024
sdv sqlserver run-validation --data-validation-config-file config_q1.yaml

# If Q1 passes, validate Q2 2024
sdv sqlserver run-validation --data-validation-config-file config_q2.yaml

# Continue for remaining quarters
```

#### Phase 4: Full Validation

**Goal**: Complete comprehensive validation after successful subset testing

**When to Run Full Validation**:

* ✅ Sample validations pass successfully
* ✅ Subset validations show no data quality issues
* ✅ You have allocated sufficient time and compute resources
* ✅ Preferably during off-peak hours

**Considerations**:

* Use **asynchronous validation** for large datasets to avoid timeouts
* Consider using **script generation mode** to run validations in parallel
* Monitor resource consumption on both source and target systems
* Plan for validation to run during maintenance windows

**Example**:

```bash
# Generate scripts for parallel execution
sdv sqlserver generate-validation-scripts \
  --data-validation-config-file full_validation_config.yaml \
  --output-directory ./validation_scripts

# Review generated scripts and execute in parallel or scheduled
```

### Performance Optimization Tips

#### 1. Use Appropriate Validation Types

Not all tables need all validation types:

```yaml
# For reference/lookup tables (small, static)
validations:
  - validation_type: "schema"
  - validation_type: "row_count"
  - validation_type: "column_level"  # Full validation OK

# For large transaction tables
validations:
  - validation_type: "schema"
  - validation_type: "row_count"
  - validation_type: "aggregate_metrics"  # Use aggregates instead of row-by-row
```

#### 2. Prioritize Critical Columns

For large tables, validate critical business columns first:

```yaml
validations:
  - validation_type: "column_level"
    columns_to_validate:
      # Start with business-critical columns
      - "customer_id"
      - "transaction_amount"
      - "transaction_date"
      # Add more columns after initial validation succeeds
```

#### 3. Leverage Partitioning Metadata

If your tables are partitioned, validate partition by partition:

```yaml
# Config 1: Validate partition 1
tables:
  - source_table_name: "orders"
    target_table_name: "orders"
    where_clause: "partition_key = '2024-01'"
    target_where_clause: "partition_key = '2024-01'"
    validations:
      - validation_type: "row_count"
      - validation_type: "column_level"

# Config 2: Validate partition 2
tables:
  - source_table_name: "orders"
    target_table_name: "orders"
    where_clause: "partition_key = '2024-02'"
    target_where_clause: "partition_key = '2024-02'"
    validations:
      - validation_type: "row_count"
      - validation_type: "column_level"
```

#### 4. Use Asynchronous Validation for Production

For production environments, use asynchronous validation:

```bash
# Async validation returns immediately, processes in Snowflake
sdv sqlserver run-async-validation \
  --data-validation-config-file config.yaml \
  --poll-interval 30 \
  --max-wait-time 3600
```

### Cost and Resource Management

#### Estimate Query Costs

**Before running validation on large tables**:

1. **Estimate row counts**:

   ```sql
   -- Source
   SELECT COUNT(*) FROM source_table WHERE <partition_filter>;

   -- Target
   SELECT COUNT(*) FROM target_table WHERE <partition_filter>;
   ```

2. **Estimate data volume**:

   ```sql
   -- Check table size
   SELECT
       table_name,
       row_count,
       bytes,
       bytes / (1024*1024*1024) as size_gb
   FROM information_schema.tables
   WHERE table_name = 'your_table';
   ```

3. **Start with small partitions**: If estimated size > 10 GB, break into smaller chunks

#### Compute Warehouse Sizing (Snowflake)

* **Small tables (< 1M rows)**: XS or S warehouse
* **Medium tables (1M - 10M rows)**: S or M warehouse
* **Large tables (> 10M rows)**: M or L warehouse, use partitioning
* **Very large tables (> 100M rows)**: L or XL warehouse, mandatory partitioning

### Common Pitfalls to Avoid

| ❌ Don’t Do This | ✅ Do This Instead |
| --- | --- |
| Validate entire 1B row table at once | Validate in partitions of 10M-100M rows |
| Run validation during business hours on production | Schedule during off-peak hours or use read replicas |
| Skip sample testing and go straight to full validation | Always validate samples first |
| Use same configuration for all table sizes | Tailor validation strategy to table size |
| Validate all columns for all tables | Prioritize critical columns, especially for large tables |
| Ignore resource consumption | Monitor and set appropriate compute resources |

### Validation Checklist

Use this checklist to ensure you’re following best practices:

**Before Starting**:

* [ ] ODBC drivers installed and tested
* [ ] Connectivity to source and target verified
* [ ] Configuration template generated
* [ ] Test credentials have appropriate read permissions

**Initial Testing** (Phase 1):

* [ ] Selected 1-2 small tables for initial test
* [ ] Configuration file created and reviewed
* [ ] Sample validation executed successfully
* [ ] Validation report reviewed and understood

**Subset Validation** (Phase 2):

* [ ] Identified subset of production data to validate
* [ ] Used `where_clause` and `target_where_clause` to restrict rows
* [ ] Validated 10,000 - 100,000 rows successfully
* [ ] Reviewed results for any data quality issues

**Large Table Strategy** (Phase 3):

* [ ] Identified tables > 10M rows
* [ ] Chosen partitioning strategy (date, ID range, modulo)
* [ ] Estimated compute costs for validation
* [ ] Tested validation on 1-2 partitions first
* [ ] Documented partition validation schedule

**Production Validation** (Phase 4):

* [ ] All subset validations passed
* [ ] Resource allocation planned (compute, time)
* [ ] Validation scheduled during maintenance window
* [ ] Using asynchronous or script generation mode
* [ ] Monitoring plan in place

### Example: Complete Validation Strategy

Here’s a complete example of validating a large e-commerce database:

**Day 1: Initial Setup and Small Tables**

```bash
# Test with small reference tables
sdv sqlserver run-validation --data-validation-config-file config_small_tables.yaml
# Tables: product_categories (1K rows), payment_types (50 rows)
```

**Day 2: Subset of Medium Tables**

```bash
# Test with recent data from medium tables
sdv sqlserver run-validation --data-validation-config-file config_subset_medium.yaml
# Tables: customers WHERE created_date >= '2024-01-01' (50K rows)
#         products WHERE product_id <= 10000 (10K rows)
```

**Day 3: Partition Strategy for Large Tables**

```bash
# Validate one month of orders
sdv sqlserver run-validation --data-validation-config-file config_orders_jan2024.yaml
# Table: orders WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31' (500K rows)
```

**Day 4-5: Progressive Partition Validation**

```bash
# Generate scripts for all partitions
sdv sqlserver generate-validation-scripts \
  --data-validation-config-file config_all_partitions.yaml \
  --output-directory ./scripts

# Review and execute scripts for each partition
```

**Day 6: Full Validation (Off-Peak)**

```bash
# Run complete validation during weekend maintenance window
sdv sqlserver run-async-validation \
  --data-validation-config-file config_full_validation.yaml \
  --poll-interval 60 \
  --max-wait-time 28800  # 8 hours
```

---

## CLI Commands

### Command Structure

All commands follow this consistent structure:

```bash
snowflake-data-validation <source_dialect> <command> [options]

# Or use the shorter alias
sdv <source_dialect> <command> [options]
```

Where:

* `<source_dialect>` is one of: `sqlserver`, `teradata`, `redshift`, `snowflake`.
* `<command>` is one of:

  * `run-validation` - Run synchronous validation
  * `run-async-validation` - Run asynchronous validation
  * `generate-validation-scripts` - Generate validation scripts
  * `get-configuration-files` - Get configuration templates
  * `auto-generated-configuration-file` - Interactive config generation

### Global Options

These options can be used with the CLI without specifying a source dialect or command:

#### Check Version

Display the current installed version of the Snowflake Data Validation CLI:

```bash
# Using full command name
snowflake-data-validation --version

# Using the alias
sdv --version
```

**Output Example:**

```text
snowflake-data-validation 1.2.3
```

**Use Cases:**

* Verify successful installation
* Check which version is currently installed
* Confirm version before reporting issues
* Ensure compatibility with documentation

#### Help

Display general help information:

```bash
# General help
snowflake-data-validation --help
sdv --help

# Command-specific help
sdv sqlserver --help
sdv teradata run-validation --help
sdv redshift generate-validation-scripts --help
```

### Dialect-Specific Command References

For detailed command documentation specific to your source database, see the following pages:

* **[SQL Server Commands Reference](sqlserver_commands.md)** - Complete command reference for SQL Server migrations
* **[Teradata Commands Reference](teradata_commands.md)** - Complete command reference for Teradata migrations
* **[Amazon Redshift Commands Reference](redshift_commands.md)** - Complete command reference for Redshift migrations
* **[Snowflake Commands Reference](snowflake_commands.md)** - Complete command reference for Snowflake-to-Snowflake migrations

Each page provides:

* Detailed syntax for all commands
* Complete option descriptions with examples
* Connection configuration specifics
* Dialect-specific examples
* Troubleshooting tips for that platform
* Best practices for that database type

---

### SQL Server Commands

For complete SQL Server command documentation, see [SQL Server Commands Reference](sqlserver_commands.md).

**Quick Links:**

* [Run Synchronous Validation](sqlserver_commands.md)
* [Run Asynchronous Validation](sqlserver_commands.md)
* [Generate Validation Scripts](sqlserver_commands.md)
* [Get Configuration Templates](sqlserver_commands.md)
* [Auto-Generate Configuration File](sqlserver_commands.md)
* [Connection Configuration](sqlserver_commands.md)
* [Troubleshooting](sqlserver_commands.md)

#### Common Commands

**Run Validation:**

```bash
sdv sqlserver run-validation \
  --data-validation-config-file ./configs/sqlserver_validation.yaml
```

**Generate Scripts:**

```bash
sdv sqlserver generate-validation-scripts \
  --data-validation-config-file /path/to/config.yaml
```

**Get Templates:**

```bash
sdv sqlserver get-configuration-files \
  --templates-directory ./templates
```

For complete documentation, see [SQL Server Commands Reference](sqlserver_commands.md).

---

### Teradata Commands

For complete Teradata command documentation, see [Teradata Commands Reference](teradata_commands.md).

**Quick Links:**

* [Run Synchronous Validation](teradata_commands.md)
* [Run Asynchronous Validation](teradata_commands.md)
* [Generate Validation Scripts](teradata_commands.md)
* [Get Configuration Templates](teradata_commands.md)
* [Auto-Generate Configuration File](teradata_commands.md)
* [Connection Configuration](teradata_commands.md)
* [Troubleshooting](teradata_commands.md)

#### Common Commands

**Run Validation:**

```bash
sdv teradata run-validation \
  --data-validation-config-file ./configs/teradata_validation.yaml
```

**Generate Scripts:**

```bash
sdv teradata generate-validation-scripts \
  ./config.yaml \
  --output-directory ./scripts
```

**Get Templates:**

```bash
sdv teradata get-configuration-files \
  --templates-directory ./templates
```

For complete documentation, see [Teradata Commands Reference](teradata_commands.md).

---

### Amazon Redshift Commands

For complete Amazon Redshift command documentation, see [Redshift Commands Reference](redshift_commands.md).

**Quick Links:**

* [Run Synchronous Validation](redshift_commands.md)
* [Run Asynchronous Validation](redshift_commands.md)
* [Generate Validation Scripts](redshift_commands.md)
* [Get Configuration Templates](redshift_commands.md)
* [Auto-Generate Configuration File](redshift_commands.md)
* [Connection Configuration](redshift_commands.md)
* [Troubleshooting](redshift_commands.md)

#### Common Commands

**Run Validation:**

```bash
sdv redshift run-validation \
  --data-validation-config-file ./configs/redshift_validation.yaml
```

**Generate Scripts:**

```bash
sdv redshift generate-validation-scripts \
  --data-validation-config-file /path/to/config.yaml
```

**Get Templates:**

```bash
sdv redshift get-configuration-files \
  --templates-directory ./templates
```

For complete documentation, see [Redshift Commands Reference](redshift_commands.md).

---

### Snowflake Commands

For complete Snowflake-to-Snowflake command documentation, see [Snowflake Commands Reference](snowflake_commands.md).

**Quick Links:**

* [Run Synchronous Validation](snowflake_commands.md)
* [Run Asynchronous Validation](snowflake_commands.md)
* [Source Validate](snowflake_commands.md)
* [Generate Validation Scripts](snowflake_commands.md)
* [Get Configuration Templates](snowflake_commands.md)
* [Auto-Generate Configuration File](snowflake_commands.md)
* [Connection Configuration](snowflake_commands.md)
* [Troubleshooting](snowflake_commands.md)

#### Common Commands

**Run Validation:**

```bash
sdv snowflake run-validation \
  --data-validation-config-file ./configs/snowflake_validation.yaml
```

**Generate Scripts:**

```bash
sdv snowflake generate-validation-scripts \
  --data-validation-config-file /path/to/config.yaml
```

**Get Templates:**

```bash
sdv snowflake get-configuration-files \
  --templates-directory ./templates
```

For complete documentation, see [Snowflake Commands Reference](snowflake_commands.md).

---

## Configuration File Reference

### Global Configuration

The global configuration section defines the overall behavior of the validation process.

```yaml
# Platform configuration
source_platform: SqlServer  # Options: SqlServer, Teradata, Redshift, Snowflake
target_platform: Snowflake  # Currently only Snowflake is supported

# Output configuration
output_directory_path: /path/to/output/directory

# Threading configuration
max_threads: auto  # Options: "auto" or positive integer (1-32)

# Teradata-specific configuration (required only for Teradata)
target_database: TARGET_DB_NAME

# Directory path for source validation file
source_validation_files_path: /path/to/source_validation_file/directory

# Directory path for target validation file
target_validation_files_path: /path/to/target_validation_file/directory
```

#### Platform Configuration Options

**`source_platform`** (required)

* **Type:** String
* **Valid Values:** `SqlServer`, `Teradata`, `Redshift`, `Snowflake`
* **Description:** The source database platform for validation
* **Example:** `source_platform: SqlServer`

**`target_platform`** (required)

* **Type:** String
* **Valid Values:** `Snowflake`
* **Description:** The target database platform (currently only Snowflake is supported)
* **Example:** `target_platform: Snowflake`

**`output_directory_path`** (required)

* **Type:** String (path)
* **Description:** Directory where validation results, logs, and reports will be saved
* **Example:** `output_directory_path: /home/user/validation_output`

**`max_threads`** (optional)

* **Type:** String or Integer
* **Valid Values:** `"auto"` or positive integer (1-32)
* **Default:** `"auto"`
* **Description:** Controls parallelization for validation operations

  * `"auto"`: Automatically detects optimal thread count based on CPU cores
  * Integer value: Specifies exact number of threads to use
* **Examples:**

  ```yaml
  max_threads: auto        # Auto-detect optimal threads
  max_threads: 4           # Use exactly 4 threads
  max_threads: 16          # Use 16 threads
  ```

**`target_database`** (required for Teradata only)

* **Type:** String
* **Description:** Target database name in Snowflake for Teradata validations
* **Example:** `target_database: PROD_DB`

**`source_validation_files_path`** (optional)

* **Type:** String (path)
* **Description:** Path to the directory containing the source validation files.
* **Example:** `source_validation_files_path: /path/to/source_validation_file/directory`

**`target_validation_files_path`** (optional)

* **Type:** String (path)
* **Description:** Path to the directory containing the target validation files.
* **Example:** `target_validation_files_path: /path/to/targetvalidation_file/directory`

---

### Connection Configuration

Define how to connect to source and target databases.

#### Source Connection Configuration

##### SQL Server Source Connection

```yaml
source_connection:
  mode: credentials
  host: "sqlserver.company.com"
  port: 1433
  username: "sqlserver_user"
  password: "secure_password"
  database: "source_database"
  trust_server_certificate: "no"   # Optional: yes/no
  encrypt: "yes"                   # Optional: yes/no/optional
```

**Connection Fields:**

* **`mode`** (required)

  * **Type:** String
  * **Valid Values:** `credentials`
  * **Description:** Connection mode for SQL Server
* **`host`** (required)

  * **Type:** String
  * **Description:** SQL Server hostname or IP address
  * **Example:** `"sqlserver.company.com"` or `"192.168.1.100"`
* **`port`** (required)

  * **Type:** Integer
  * **Default:** 1433
  * **Description:** SQL Server port number
* **`username`** (required)

  * **Type:** String
  * **Description:** SQL Server authentication username
* **`password`** (required)

  * **Type:** String
  * **Description:** SQL Server authentication password
  * **Security Note:** Consider using environment variables or secret management
* **`database`** (required)

  * **Type:** String
  * **Description:** SQL Server database name
* **`trust_server_certificate`** (optional)

  * **Type:** String
  * **Valid Values:** `"yes"`, `"no"`
  * **Default:** `"no"`
  * **Description:** Whether to trust the server certificate for SSL/TLS connections
* **`encrypt`** (optional)

  * **Type:** String
  * **Valid Values:** `"yes"`, `"no"`, `"optional"`
  * **Default:** `"yes"`
  * **Description:** Connection encryption setting

##### Teradata Source Connection

```yaml
source_connection:
  mode: credentials
  host: "teradata.company.com"
  username: "teradata_user"
  password: "secure_password"
  database: "source_database"
```

**Connection Fields:**

* **`mode`** (required)

  * **Type:** String
  * **Valid Values:** `credentials`
* **`host`** (required)

  * **Type:** String
  * **Description:** Teradata hostname or IP address
* **`username`** (required)

  * **Type:** String
  * **Description:** Teradata authentication username
* **`password`** (required)

  * **Type:** String
  * **Description:** Teradata authentication password
* **`database`** (required)

  * **Type:** String
  * **Description:** Teradata database name

##### Amazon Redshift Source Connection

```yaml
source_connection:
  mode: credentials
  host: "redshift-cluster.region.redshift.amazonaws.com"
  port: 5439
  username: "redshift_user"
  password: "secure_password"
  database: "source_database"
```

**Connection Fields:**

* **`mode`** (required)

  * **Type:** String
  * **Valid Values:** `credentials`
* **`host`** (required)

  * **Type:** String
  * **Description:** Redshift cluster endpoint
* **`port`** (required)

  * **Type:** Integer
  * **Default:** 5439
  * **Description:** Redshift port number
* **`username`** (required)

  * **Type:** String
  * **Description:** Redshift authentication username
* **`password`** (required)

  * **Type:** String
  * **Description:** Redshift authentication password
* **`database`** (required)

  * **Type:** String
  * **Description:** Redshift database name

#### Target Connection (Snowflake)

Snowflake connections support three modes: `name`, `default`, and `credentials` (IPC only and SnowConvert exclusive).

##### Option 1: Named Connection

Use a pre-configured Snowflake connection saved in your Snowflake connections file.

```yaml
target_connection:
  mode: name
  name: "my_snowflake_connection"
```

**Fields:**

* **`mode`** (required): Must be `"name"`
* **`name`** (required): Name of the saved Snowflake connection

##### Option 2: Default Connection

Use the default Snowflake connection from your environment.

```yaml
target_connection:
  mode: default
```

**Fields:**

* **`mode`** (required): Must be `"default"`

##### Option 3: Credentials Mode (IPC Only)

> **Note:** The `credentials` mode is only available when using IPC (Inter-Process Communication) commands directly via CLI parameters, not in YAML configuration files. This mode is exclusive to the SnowConvert UI.

---

### Validation Configuration

Controls which validation levels are executed.

```yaml
validation_configuration:
  schema_validation: true          # Level 1: Schema validation
  metrics_validation: true         # Level 2: Statistical metrics validation
  row_validation: false            # Level 3: Row-level data validation
  max_failed_rows_number: 100      # Maximum failed rows to report (applies only for row validation)
  exclude_metrics: false           # Exclude statistical metrics from validation
  apply_metric_column_modifier: false  # Apply column modifiers for metrics
  custom_templates_path: /path/to/templates  # Optional: Custom query templates
```

**Validation Options:**

* **`schema_validation`** (optional)

  * **Type:** Boolean
  * **Default:** `true`
  * **Description:** Validates table and column schema consistency
  * **Checks:**

    * Column names match between source and target
    * Data types are compatible
    * Column nullability settings
    * Primary key definitions
* **`metrics_validation`** (optional)

  * **Type:** Boolean
  * **Default:** `true`
  * **Description:** Validates statistical metrics for each column
  * **Checks:**

    * Row counts
    * Distinct value counts
    * Null value counts
    * Min/max values
    * Average, sum, standard deviation (for numeric columns)
* **`row_validation`** (optional)

  * **Type:** Boolean
  * **Default:** `false`
  * **Description:** Validates data at the row level using hash-based comparison

    * **Note:** Requires index columns for row identification. If not specified in the configuration, the tool attempts to auto-detect them from primary keys.
  * **Warning:** This is the most resource-intensive validation level
  * **Checks:**

    * MD5 hash comparison of row chunks
    * Identifies specific rows with differences
* **`max_failed_rows_number`** (optional)

  * **Type:** Integer
  * **Default:** 100
  * **Minimum:** 1
  * **Description:** Maximum number of failed rows to report per table
  * **Example:** `max_failed_rows_number: 250`
* **`exclude_metrics`** (optional)

  * **Type:** Boolean
  * **Default:** `false`
  * **Description:** When `true`, excludes certain statistical metrics (avg, sum, stddev, variance) from validation
  * **Use Case:** Useful for large tables where statistical calculations might cause an overflow.
* **`apply_metric_column_modifier`** (optional)

  * **Type:** Boolean
  * **Default:** `true`
  * **Description:** Applies column modifiers defined in metric templates
  * **Use Case:** Advanced users with custom metric calculations
* **`custom_templates_path`** (optional)

  * **Type:** String (path)
  * **Description:** Path to directory containing custom Jinja2 query templates
  * **Example:** `custom_templates_path: /opt/validation/custom_templates`

---

### Table Configuration

Defines which tables to validate and how to validate them.

```yaml
tables:
  # Table 1: Include specific columns
  - fully_qualified_name: database.schema.table1
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - customer_id
      - customer_name
      - email
    index_column_list:
      - customer_id
    where_clause: "status = 'ACTIVE'"
    target_where_clause: "status = 'ACTIVE'"
    is_case_sensitive: false
    chunk_number: 10
    max_failed_rows_number: 50
    column_mappings:
      customer_id: cust_id
      customer_name: name

  # Table 2: Exclude specific columns
  - fully_qualified_name: database.schema.table2
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - audit_timestamp
      - created_by
      - modified_by
    index_column_list: []

  # Table 3: Simple configuration
  - fully_qualified_name: database.schema.table3
    use_column_selection_as_exclude_list: false
    column_selection_list: []
```

**Table Configuration Fields:**

* **`fully_qualified_name`** (required)

  * **Type:** String
  * **Format:** `database.schema.table` or `schema.table`
  * **Description:** Full table identifier in the source database
  * **Examples:**

    ```yaml
    fully_qualified_name: my_database.dbo.customers
    fully_qualified_name: public.orders  # For Redshift
    ```

* **`target_database`** (optional)

  * **Type:** String
  * **Default:** Source database name from fully_qualified_name field
  * **Description:** Target database name if different from source database name
  * **Example:**

    ```yaml
    target_database: target_database_name
    ```

* **`target_schema`** (optional)

  * **Type:** String
  * **Default:** Source schema name from fully_qualified_name field
  * **Description:** Target schema name if different from source schema name
  * **Example:**

    ```yaml
    target_schema: target_schema_name
    ```

* **`target_name`** (optional)

  * **Type:** String
  * **Default:** Source table name from fully_qualified_name field
  * **Description:** Target table name if different from source table name
  * **Example:**

    ```yaml
    target_name: customers_new
    ```

* **`use_column_selection_as_exclude_list`** (required)

  * **Type:** Boolean
  * **Description:** Determines how `column_selection_list` is interpreted

    * `false`: Include only the specified columns
    * `true`: Exclude the specified columns (include all others)
  * **Examples:**

    ```yaml
    # Include only these columns
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - id
      - name
      - email

    # Exclude these columns (include all others)
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - internal_notes
      - audit_timestamp
    ```

* **`column_selection_list`** (required)

  * **Type:** List of strings
  * **Description:** List of column names to include or exclude
  * **Note:** Use an empty list `[]` to include all columns
* **`index_column_list`** (optional)

  * **Type:** List of strings
  * **Default:** Auto-detected from primary keys
  * **Description:** Columns to use as unique identifiers for row validation
  * **Use Case:** Specify when the table doesn’t have a primary key or you want to use different columns
  * **Example:**

    ```yaml
    index_column_list:
      - customer_id
      - order_date
    ```

* **`target_index_column_list`** (optional)

  * **Type:** List of strings
  * **Description:** Index columns in the target table (if different from source)
  * **Note:** Automatically derived from `column_mappings` if not specified
* **`where_clause`** (optional)

  * **Type:** String
  * **Default:** `""` (empty, no filter)
  * **Description:** SQL WHERE clause to filter source data (without “WHERE” keyword)
  * **Examples:**

    ```yaml
    where_clause: "created_date >= '2024-01-01'"
    where_clause: "status IN ('ACTIVE', 'PENDING') AND region = 'US'"
    where_clause: "amount > 1000 AND customer_type = 'PREMIUM'"
    ```

* **`target_where_clause`** (optional)

  * **Type:** String
  * **Default:** `""` (empty, no filter)
  * **Description:** SQL WHERE clause to filter target data
  * **Best Practice:** Should match `where_clause` to ensure consistent comparison
  * **Example:**

    ```yaml
    target_where_clause: "created_date >= '2024-01-01'"
    ```

* **`is_case_sensitive`** (optional)

  * **Type:** Boolean
  * **Default:** `false`
  * **Description:** Whether column name matching should be case-sensitive
* **`chunk_number`** (optional)

  * **Type:** Integer
  * **Default:** 0 (no chunking)
  * **Minimum:** 0
  * **Description:** Number of chunks to split row validation into
  * **Use Case:** Large tables benefit from chunking for better performance
  * **Example:**

    ```yaml
    chunk_number: 20  # Split into 20 chunks for parallel processing
    ```

* **`max_failed_rows_number`** (optional)

  * **Type:** Integer
  * **Minimum:** 1
  * **Description:** Maximum failed rows to report for this specific table
  * **Note:** Overrides the global `max_failed_rows_number` setting
* **`column_mappings`** (optional)

  * **Type:** Dictionary (key-value pairs)
  * **Description:** Maps source column names to target column names when they differ
  * **Format:** `source_column_name: target_column_name`
  * **Example:**

    ```yaml
    column_mappings:
      cust_id: customer_id
      cust_name: customer_name
      addr: address
    ```

* **`exclude_metrics`** (optional)

  * **Type:** Boolean
  * **Description:** Exclude metrics validation for this specific table
  * **Note:** Overrides the global `exclude_metrics` setting
* **`apply_metric_column_modifier`** (optional)

  * **Type:** Boolean
  * **Description:** Apply column modifiers for this specific table
  * **Note:** Overrides the global `apply_metric_column_modifier` setting

---

### View Configuration

Views are validated similarly to tables but are configured in a separate `views:` section. View validation creates temporary tables internally to materialize view schema for comparison between source and target systems.

```yaml
views:
  # View 1: Basic view validation
  - fully_qualified_name: database.schema.customer_summary_view
    target_name: customer_summary_view_target
    use_column_selection_as_exclude_list: false
    column_selection_list: []

  # View 2: View with specific columns and filtering
  - fully_qualified_name: database.schema.sales_report_view
    target_name: sales_report_view_target
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - region
      - total_sales
      - order_count
    where_clause: "fiscal_year = 2024"
    target_where_clause: "fiscal_year = 2024"
    column_mappings:
      region_code: region
```

**View Configuration Fields:**

View configuration uses the same fields as table configuration, with the following key points:

* **`fully_qualified_name`** (required)

  * **Type:** String
  * **Format:** `database.schema.view` or `schema.view`
  * **Description:** Full view identifier in the source database
  * **Examples:**

    ```yaml
    fully_qualified_name: my_database.dbo.customer_summary_view
    fully_qualified_name: public.sales_report_view  # For Redshift
    ```

* **`target_database`** (optional)

  * **Type:** String
  * **Default:** Source database name from fully_qualified_name field
  * **Description:** Target database name if different from source database name
* **`target_schema`** (optional)

  * **Type:** String
  * **Default:** Source schema name from fully_qualified_name field
  * **Description:** Target schema name if different from source schema name
* **`target_name`** (optional)

  * **Type:** String
  * **Default:** Source view name from fully_qualified_name field
  * **Description:** Target view name if different from source view name
* **`use_column_selection_as_exclude_list`** (required)

  * **Type:** Boolean
  * **Description:** Determines how `column_selection_list` is interpreted

    * `false`: Include only the specified columns
    * `true`: Exclude the specified columns (include all others)
* **`column_selection_list`** (required)

  * **Type:** List of strings
  * **Description:** List of column names to include or exclude
  * **Note:** Use an empty list `[]` to include all columns
* **`index_column_list`** (optional)

  * **Type:** List of strings
  * **Description:** Columns to use as unique identifiers for row validation
  * **Use Case:** Required when row validation is enabled
* **`where_clause`** (optional)

  * **Type:** String
  * **Default:** `""` (empty, no filter)
  * **Description:** SQL WHERE clause to filter source data (without “WHERE” keyword)
* **`target_where_clause`** (optional)

  * **Type:** String
  * **Default:** `""` (empty, no filter)
  * **Description:** SQL WHERE clause to filter target data
* **`column_mappings`** (optional)

  * **Type:** Dictionary (key-value pairs)
  * **Description:** Maps source column names to target column names when they differ
* **`chunk_number`** (optional)

  * **Type:** Integer
  * **Default:** 0 (no chunking)
  * **Description:** Number of chunks to split row validation into
* **`max_failed_rows_number`** (optional)

  * **Type:** Integer
  * **Description:** Maximum failed rows to report for this specific view
* **`is_case_sensitive`** (optional)

  * **Type:** Boolean
  * **Default:** `false`
  * **Description:** Whether column name matching should be case-sensitive

**How View Validation Works:**

1. The CLI creates temporary tables from view definitions in both source and target systems
2. Data is extracted from the views into these temporary tables
3. Validation is performed on the temporary tables
4. Temporary tables are cleaned up after validation completes

**Best Practices for View Validation:**

1. **Use filtering for large views:** Apply `where_clause` and `target_where_clause` to limit data volume
2. **Test with small subsets first:** Start with filtered validation before full view validation
3. **Consider view complexity:** Complex views with many joins may take longer to validate
4. **Monitor resource usage:** Views that materialize large datasets consume significant memory

---

### Comparison Configuration

Controls comparison behavior and tolerance levels.

```yaml
comparison_configuration:
  tolerance: 0.01  # 1% tolerance for statistical comparisons
```

**Comparison Options:**

* **`tolerance`** (optional)

  * **Type:** Float
  * **Default:** 0.001 (0.1%)
  * **Description:** Acceptable tolerance for statistical metric differences
  * **Use Case:** Allows for small differences due to rounding or data type conversions
  * **Examples:**

    ```yaml
    tolerance: 0.001   # 0.1% tolerance (very strict)
    tolerance: 0.01    # 1% tolerance (recommended)
    tolerance: 0.05    # 5% tolerance (lenient)
    ```

---

### Logging Configuration

Controls logging behavior for validation operations.

```yaml
logging_configuration:
  level: INFO              # Overall logging level
  console_level: WARNING   # Console-specific level
  file_level: DEBUG        # File-specific level
```

**Logging Options:**

* **`level`** (optional)

  * **Type:** String
  * **Valid Values:** `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
  * **Default:** `INFO`
  * **Description:** Default logging level for all loggers
  * **Level Descriptions:**

    * `DEBUG`: Detailed diagnostic information
    * `INFO`: General informational messages
    * `WARNING`: Warning messages for potentially problematic situations
    * `ERROR`: Error messages for serious issues
    * `CRITICAL`: Critical errors that may cause application failure
* **`console_level`** (optional)

  * **Type:** String
  * **Valid Values:** `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
  * **Default:** Same as `level`
  * **Description:** Logging level for console output
  * **Use Case:** Set to `WARNING` or `ERROR` to reduce console noise
* **`file_level`** (optional)

  * **Type:** String
  * **Valid Values:** `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
  * **Default:** Same as `level`
  * **Description:** Logging level for file output
  * **Use Case:** Set to `DEBUG` for detailed file logs while keeping console clean

**Example Configurations:**

```yaml
# Verbose logging for troubleshooting
logging_configuration:
  level: DEBUG
  console_level: DEBUG
  file_level: DEBUG

# Production-friendly logging
logging_configuration:
  level: INFO
  console_level: WARNING
  file_level: INFO

# Minimal console output with detailed file logs
logging_configuration:
  level: INFO
  console_level: ERROR
  file_level: DEBUG
```

**Note:** CLI `--log-level` parameter overrides configuration file settings.

---

### Database and Schema Mappings

Map source database/schema names to target names when they differ.

```yaml
database_mappings:
  source_db1: target_db1
  source_db2: target_db2
  legacy_database: modern_database

schema_mappings:
  dbo: public
  source_schema: target_schema
  old_schema: new_schema
```

**Mapping Options:**

* **`database_mappings`** (optional)

  * **Type:** Dictionary
  * **Description:** Maps source database names to target database names
  * **Use Case:** When database names differ between source and Snowflake
  * **Example:**

    ```yaml
    database_mappings:
      PROD_SQL: PROD_SNOWFLAKE
      DEV_SQL: DEV_SNOWFLAKE
    ```

* **`schema_mappings`** (optional)

  * **Type:** Dictionary
  * **Description:** Maps source schema names to target schema names
  * **Use Case:** When schema names differ between source and Snowflake
  * **Example:**

    ```yaml
    schema_mappings:
      dbo: PUBLIC
      sales: SALES_DATA
      hr: HUMAN_RESOURCES
    ```

---

## Complete Configuration Examples

### Example 1: SQL Server to Snowflake - Basic Validation

```yaml
# Global configuration
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./validation_results
max_threads: auto

# Source connection
source_connection:
  mode: credentials
  host: sqlserver.company.com
  port: 1433
  username: sql_user
  password: sql_password
  database: production_db
  trust_server_certificate: "no"
  encrypt: "yes"

# Target connection
target_connection:
  mode: name
  name: snowflake_prod

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

# Comparison configuration
comparison_configuration:
  tolerance: 0.01

# Tables to validate
tables:
  - fully_qualified_name: production_db.dbo.customers
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - customer_id

  - fully_qualified_name: production_db.dbo.orders
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - internal_notes
      - audit_log
    where_clause: "order_date >= '2024-01-01'"
    target_where_clause: "order_date >= '2024-01-01'"
```

### Example 2: Teradata to Snowflake - Comprehensive Validation

```yaml
# Global configuration
source_platform: Teradata
target_platform: Snowflake
output_directory_path: /opt/validation/results
max_threads: 8
target_database: PROD_SNOWFLAKE

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
  row_validation: true
  max_failed_rows_number: 100
  exclude_metrics: false
  apply_metric_column_modifier: false

# Comparison configuration
comparison_configuration:
  tolerance: 0.005

# Logging configuration
logging_configuration:
  level: INFO
  console_level: WARNING
  file_level: DEBUG

# Schema mappings
schema_mappings:
  prod_db: PUBLIC

# Tables configuration
tables:
  - fully_qualified_name: prod_db.sales_data
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - transaction_id
      - customer_id
      - amount
      - transaction_date
    index_column_list:
      - transaction_id
    chunk_number: 10
    max_failed_rows_number: 50

  - fully_qualified_name: prod_db.customer_master
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - ssn
      - credit_card
    where_clause: "status = 'ACTIVE'"
    target_where_clause: "status = 'ACTIVE'"
    column_mappings:
      cust_id: customer_id
      cust_name: customer_name
```

### Example 3: Redshift to Snowflake - Advanced Configuration

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
  - fully_qualified_name: analytics_db.public.fact_sales
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - sale_id
    chunk_number: 50
    max_failed_rows_number: 500

  # Dimension table with column mappings
  - fully_qualified_name: analytics_db.public.dim_customer
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
  - fully_qualified_name: analytics_db.staging.incremental_load
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - load_timestamp
      - etl_batch_id
    where_clause: "load_date >= CURRENT_DATE - 7"
    target_where_clause: "load_date >= CURRENT_DATE - 7"
    chunk_number: 10
```

### Example 4: Minimal Configuration

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./output

source_connection:
  mode: credentials
  host: localhost
  port: 1433
  username: sa
  password: password
  database: test_db

target_connection:
  mode: default

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

tables:
  - fully_qualified_name: test_db.dbo.test_table
    use_column_selection_as_exclude_list: false
    column_selection_list: []
```

### Example 5: View Validation Configuration

```yaml
# Global configuration
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./view_validation_results
max_threads: auto

# Source connection
source_connection:
  mode: credentials
  host: sqlserver.company.com
  port: 1433
  username: sql_user
  password: sql_password
  database: production_db
  trust_server_certificate: "no"
  encrypt: "yes"

# Target connection
target_connection:
  mode: name
  name: snowflake_prod

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

# Views to validate
views:
  # Basic view validation
  - fully_qualified_name: production_db.dbo.customer_summary_view
    use_column_selection_as_exclude_list: false
    column_selection_list: []

  # View with specific columns
  - fully_qualified_name: production_db.dbo.sales_metrics_view
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - region
      - total_sales
      - order_count
      - avg_order_value

  # View with filtering and column mappings
  - fully_qualified_name: production_db.dbo.active_orders_view
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    where_clause: "order_date >= '2024-01-01'"
    target_where_clause: "order_date >= '2024-01-01'"
    column_mappings:
      ord_id: order_id
      cust_id: customer_id
```

### Example 6: Combined Tables and Views Validation

```yaml
# Global configuration
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./combined_validation
max_threads: 16

# Source connection
source_connection:
  mode: credentials
  host: sqlserver.company.com
  port: 1433
  username: validator_user
  password: secure_password
  database: analytics_db
  trust_server_certificate: "no"
  encrypt: "yes"

# Target connection
target_connection:
  mode: name
  name: snowflake_analytics

# Validation configuration
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 100

# Comparison configuration
comparison_configuration:
  tolerance: 0.01

# Tables to validate
tables:
  - fully_qualified_name: analytics_db.dbo.customers
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - customer_id

  - fully_qualified_name: analytics_db.dbo.orders
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - order_id
    chunk_number: 20

# Views to validate
views:
  - fully_qualified_name: analytics_db.dbo.customer_order_summary
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - customer_id

  - fully_qualified_name: analytics_db.dbo.monthly_sales_report
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - month
      - year
      - total_sales
      - total_orders
```

---

## Advanced Usage

### Working with Large Tables

For large tables, consider these optimization strategies:

#### Enable Chunking

```yaml
tables:
  - fully_qualified_name: database.schema.large_table
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    chunk_number: 100  # Split into 100 chunks
    index_column_list:
      - primary_key_column
```

#### Increase Thread Count

```yaml
max_threads: 32  # Use maximum threads for parallel processing
```

#### 3. Filter Data

```yaml
tables:
  - fully_qualified_name: database.schema.large_table
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    where_clause: "created_date >= '2024-01-01' AND region = 'US'"
    target_where_clause: "created_date >= '2024-01-01' AND region = 'US'"
```

#### Selective Column Validation

```yaml
tables:
  - fully_qualified_name: database.schema.large_table
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - large_text_column
      - large_binary_column
      - xml_column
```

### Using Custom Query Templates

For advanced users, you can provide custom Jinja2 templates:

```yaml
validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  custom_templates_path: /opt/custom_templates
```

Custom template directory structure:

```text
/opt/custom_templates/
├── sqlserver_columns_metrics_query.sql.j2
├── sqlserver_row_count_query.sql.j2
├── sqlserver_compute_md5_sql.j2
└── snowflake_columns_metrics_query.sql.j2
```

### Asynchronous Validation Workflow

For environments with restricted database access or long-running validations:

#### Step 1: Generate Scripts

```bash
sdv sqlserver generate-validation-scripts \
  --data-validation-config-file config.yaml
```

This generates SQL scripts in the output directory.

#### Step 2: Execute Scripts Manually

Execute the generated scripts on source and target databases, saving results to CSV files.

#### Step 3: Run Async Validation

```bash
sdv sqlserver run-async-validation \
  --data-validation-config-file config.yaml
```

This compares the pre-generated metadata files.

### CI/CD Integration

Integrate validation into your deployment pipeline:

```bash
#!/bin/bash
# validate_migration.sh

CONFIG_FILE="./configs/validation_config.yaml"
LOG_LEVEL="INFO"

# Run validation
sdv sqlserver run-validation \
  --data-validation-config-file "$CONFIG_FILE" \
  --log-level "$LOG_LEVEL"

# Check exit code
if [ $? -eq 0 ]; then
  echo "✓ Validation passed successfully"
  exit 0
else
  echo "✗ Validation failed"
  exit 1
fi
```

### Handling Multiple Environments

Create separate configuration files for each environment:

```bash
configs/
├── dev_validation.yaml
├── staging_validation.yaml
└── prod_validation.yaml
```

Run validation for specific environment:

```bash
# Development
sdv sqlserver run-validation --data-validation-config-file configs/dev_validation.yaml

# Staging
sdv sqlserver run-validation --data-validation-config-file configs/staging_validation.yaml

# Production
sdv sqlserver run-validation --data-validation-config-file configs/prod_validation.yaml
```

---

## Validation Reports

### Overview

The Snowflake Data Validation tool generates comprehensive CSV reports that document the results of data migration validations between source and target databases. These reports help identify discrepancies in schema, metrics, and row-level data.

### Report Types

The validation tool generates different types of reports based on the validation levels configured:

#### 1. Main Validation Report (`validation_report.csv`)

This consolidated report contains results from schema and metrics validations for all tables.

#### 2. Row Validation Reports (per table)

Separate reports generated for each table when row validation is enabled, containing detailed row-level comparison results.

---

### Main Validation Report Structure

The main validation report contains the following columns:

| Column Name | Description |
| --- | --- |
| **VALIDATION_TYPE** | Type of validation performed: `SCHEMA VALIDATION` or `METRICS VALIDATION` |
| **TABLE** | Fully qualified name of the table being validated (e.g., `database.schema.table`) |
| **COLUMN_VALIDATED** | Name of the column being validated (or table-level attribute for schema validation) |
| **EVALUATION_CRITERIA** | The specific property being compared (e.g., `DATA_TYPE`, `NULLABLE`, `ROW_COUNT`, `min`, `max`) |
| **SOURCE_VALUE** | The value from the source database |
| **SNOWFLAKE_VALUE** | The value from the target (Snowflake) database |
| **STATUS** | Validation result status (see Status Values section below) |
| **COMMENTS** | Additional context or explanation for the validation result |

---

### Validation Types Explained

#### Schema Validation

Compares structural metadata between source and target tables:

* **Column existence**: Ensures columns present in source exist in target
* **Data types**: Validates column data types match (with configurable mappings)
* **Nullability**: Checks if NULL constraints match between source and target
* **Primary keys**: Verifies primary key definitions
* **Column precision/scale**: Validates numeric precision and scale values
* **Character length**: Compares VARCHAR/CHAR column lengths

**Example Schema Validation Row:**

```text
SCHEMA VALIDATION,mydb.myschema.customers,customer_id,DATA_TYPE,INT,NUMBER,FAILURE,"Data type mismatch detected"
```

#### Metrics Validation

Compares statistical metrics calculated on column data:

* **Row count**: Total number of rows in the table
* **min**: Minimum value in numeric/date columns
* **max**: Maximum value in numeric/date columns
* **count**: Count of non-null values
* **count_distinct**: Number of distinct values
* **avg**, **sum**, **stddev**, **variance**: Statistical measures (can be excluded via configuration)

**Example Metrics Validation Row:**

```text
METRICS VALIDATION,mydb.myschema.orders,order_date,max,2024-12-31,2024-12-31,SUCCESS,""
```

#### Row Validation

Generates separate per-table reports comparing actual row data using MD5 checksums to detect differences.

---

### Row Validation Report Structure

Row validation reports have a different structure focused on identifying specific rows with differences:

| Column Name | Description |
| --- | --- |
| **ROW_NUMBER** | Sequential row number in the report |
| **TABLE_NAME** | Fully qualified table name |
| **RESULT** | Outcome of the row comparison (see Result Values below) |
| **[INDEX_COLUMNS]_SOURCE** | Primary key/index column values from source |
| **[INDEX_COLUMNS]_TARGET** | Primary key/index column values from target |
| **SOURCE_QUERY** | SQL query to retrieve the row from source database |
| **TARGET_QUERY** | SQL query to retrieve the row from target database |

---

### Status Values

The **STATUS** column in the main validation report can have the following values:

| Status | Meaning |
| --- | --- |
| **SUCCESS** | Validation passed - values match between source and target |
| **FAILURE** | Validation failed - values differ between source and target |
| **WARNING** | Potential issue detected that may require attention |
| **NOT_FOUND_SOURCE** | Element exists in target but not in source |
| **NOT_FOUND_TARGET** | Element exists in source but not in target |

---

### Result Values (Row Validation)

The **RESULT** column in row validation reports can have the following values:

| Result | Meaning |
| --- | --- |
| **SUCCESS** | Row data matches between source and target |
| **FAILURE** | Row data differs between source and target (MD5 checksum mismatch) |
| **NOT_FOUND_SOURCE** | Row exists in target but not in source |
| **NOT_FOUND_TARGET** | Row exists in source but not in target |

---

### Understanding Validation Results

#### Interpreting Schema Validation Results

**Success Scenario:**

* All columns exist in both source and target
* Data types match (considering configured type mappings)
* Nullability constraints are consistent
* All structural attributes align

**Common Failure Scenarios:**

1. **Data Type Mismatch**

   * Source: `VARCHAR(50)`, Target: `VARCHAR(100)`
   * Status: May be SUCCESS if within tolerance, or FAILURE if strict matching is required
2. **Missing Column**

   * Source has column `phone_number`, target does not
   * Status: NOT_FOUND_TARGET
3. **Nullability Difference**

   * Source: `NOT NULL`, Target: `NULL`
   * Status: FAILURE

#### Interpreting Metrics Validation Results

**Success Scenario:**

* Row counts match exactly
* Statistical metrics are within configured tolerance (default: 0.1%)
* All calculated metrics align between source and target

**Common Failure Scenarios:**

1. **Row Count Mismatch**

   * Source: 10,000 rows, Target: 9,998 rows
   * Status: FAILURE
   * Action: Investigate missing rows
2. **Min/Max Value Differences**

   * Source max date: `2024-12-31`, Target max date: `2024-12-30`
   * Status: FAILURE
   * Action: Check for incomplete data migration
3. **Statistical Variance**

   * Source count_distinct: 1,000, Target count_distinct: 995
   * Status: FAILURE (if beyond tolerance)
   * Action: Investigate potential duplicates or missing values

#### Interpreting Row Validation Results

**Success Scenario:**

* All rows in source have matching rows in target (by MD5 checksum)
* No orphaned rows in either database
* Primary key values align correctly

**Common Failure Scenarios:**

1. **Row Content Mismatch**

   * Same primary key, different column values
   * Result: FAILURE
   * Action: Use provided SQL queries to investigate specific differences
2. **Missing Rows**

   * Row exists in source but not in target
   * Result: NOT_FOUND_TARGET
   * Action: Check migration completeness
3. **Extra Rows**

   * Row exists in target but not in source
   * Result: NOT_FOUND_SOURCE
   * Action: Investigate unexpected data in target

---

### Using the Reports

#### Quick Assessment

1. **Filter by STATUS column**: Focus on `FAILURE`, `WARNING`, `NOT_FOUND_SOURCE`, and `NOT_FOUND_TARGET` rows
2. **Group by VALIDATION_TYPE**: Assess schema issues separately from metrics issues
3. **Group by TABLE**: Identify which tables have the most issues

#### Investigating Failures

**For Schema Validation:**

1. Review the `EVALUATION_CRITERIA` to understand what attribute failed
2. Compare `SOURCE_VALUE` vs `SNOWFLAKE_VALUE`
3. Check if differences are acceptable (e.g., VARCHAR size increase)
4. Update type mappings or schema definitions if needed

**For Metrics Validation:**

1. Review the metric that failed (e.g., `row_count`, `max`, `min`)
2. Calculate the difference magnitude
3. Determine if within acceptable business tolerance
4. Use the detailed queries to investigate source of discrepancy

**For Row Validation:**

1. Open the table-specific row validation report
2. Identify rows with `FAILURE` status
3. Use the provided `SOURCE_QUERY` and `TARGET_QUERY` to retrieve actual row data
4. Compare column-by-column to identify specific field differences
5. Investigate why values differ (data type conversion, truncation, transformation)

---

### Configuration Options Affecting Reports

#### Tolerance Settings

The `comparison_configuration.tolerance` setting affects metrics validation:

```yaml
comparison_configuration:
  tolerance: 0.01  # 1% tolerance for numeric comparisons
```

* Values within tolerance are marked as SUCCESS
* Values beyond tolerance are marked as FAILURE

#### Validation Levels

Control which validations run and therefore which reports are generated:

```yaml
validation_configuration:
  schema_validation: true    # Validates table/column structure
  metrics_validation: true   # Validates statistical metrics
  row_validation: false      # Validates individual row data (resource intensive)
```

#### Excluded Metrics

Exclude specific metrics from validation:

```yaml
validation_configuration:
  exclude_metrics: true  # Excludes avg, sum, stddev, variance
```

#### Maximum Failed Rows

Limit the number of failed rows reported in row validation:

```yaml
validation_configuration:
  max_failed_rows_number: 100  # Report up to 100 failed rows per table
```

---

### Report File Locations

Reports are generated in the configured output directory:

```text
<output_directory_path>/
├── <timestamp>_validation_report.csv          # Main consolidated report
├── <timestamp>_database.schema.table1_1.csv   # Row validation for table1
├── <timestamp>_database.schema.table2_2.csv   # Row validation for table2
└── data_validation_<timestamp>.log            # Detailed execution log
```

**File naming convention:**

* Timestamp format: `YYYY-MM-DD_HH-MM-SS`
* Row validation reports include table name and unique ID to prevent collisions

---

### Best Practices

1. **Start with Schema Validation**: Ensure structural alignment before validating data
2. **Use Appropriate Tolerance**: Set realistic tolerance thresholds for metrics validation
3. **Selective Row Validation**: Enable row validation only for critical tables (resource intensive)
4. **Iterative Approach**: Fix schema issues first, then metrics, then row-level differences
5. **Document Acceptable Differences**: Some type conversions or value transformations may be expected
6. **Automate Report Analysis**: Use scripts to parse CSV reports and flag critical issues
7. **Preserve Reports**: Archive validation reports for audit trails and compliance

---

### Troubleshooting Report Issues

#### All Validations Showing FAILURE

**Possible Causes:**

* Incorrect database/schema mappings in configuration
* Type mapping file not loaded correctly
* Connection to wrong target database

**Solution:** Verify `database_mappings`, `schema_mappings`, and connection settings

#### Row Validation Shows All NOT_FOUND_TARGET

**Possible Causes:**

* Target table empty or not migrated yet
* Incorrect target table name
* Primary key/index columns mismatch

**Solution:** Verify target table exists and contains data, check column mappings

#### Metrics Validation Shows Large Differences

**Possible Causes:**

* Incomplete data migration
* Data type conversion issues causing value changes
* Filter/WHERE clause differences between source and target queries

**Solution:** Review migration logs, verify row counts first, check data transformations

#### Report File Not Generated

**Possible Causes:**

* Output directory doesn’t exist or lacks write permissions
* Validation configuration has all levels set to false
* Application crashed before report generation

**Solution:** Check output path permissions, review logs for errors, enable at least one validation level

---

## Troubleshooting

### Common Issues and Solutions

#### Issue: “Configuration file not found”

**Symptom:**

```sql
Configuration file not found: ./config.yaml
```

**Solution:**

* Verify the file path is correct
* Use absolute paths: `/home/user/configs/validation.yaml`
* Check file permissions

#### Issue: “Connection error”

**Symptom:**

```sql
Connection error: Unable to connect to database
```

**Solutions:**

1. **Verify connection parameters:**

   ```yaml
   source_connection:
     host: correct-hostname.com  # Verify hostname
     port: 1433                  # Verify port
     username: valid_user        # Verify username
     password: correct_password  # Verify password
   ```

2. **Check network connectivity:**

   ```bash
   # Test connection to SQL Server
   telnet sqlserver.company.com 1433

   # Test connection to Teradata
   telnet teradata.company.com 1025

   # Test connection to Redshift
   telnet redshift-cluster.amazonaws.com 5439
   ```

3. **Verify firewall rules** allow connections from your machine
4. **For SQL Server SSL issues:**

   ```yaml
   source_connection:
     trust_server_certificate: "yes"  # Try this if SSL errors occur
     encrypt: "optional"
   ```

#### Issue: “Invalid parameter”

**Symptom:**

```sql
Invalid parameter: max_threads must be 'auto' or a positive integer
```

**Solution:**

```yaml
# Correct
max_threads: auto
max_threads: 4

# Incorrect
max_threads: "4"      # Remove quotes
max_threads: 0        # Must be positive
max_threads: -1       # Must be positive
```

#### Issue: “Table not found”

**Symptom:**

```sql
Table not found: database.schema.table_name
```

**Solutions:**

1. **Verify fully qualified name:**

   ```yaml
   # For SQL Server and Teradata
   fully_qualified_name: database_name.schema_name.table_name

   # For Redshift (no database in FQN)
   fully_qualified_name: schema_name.table_name
   ```

2. **Check case sensitivity:**

   ```yaml
   tables:
     - fully_qualified_name: MyDatabase.MySchema.MyTable
       is_case_sensitive: true  # Match exact case
   ```

3. **Verify table exists in source database**

#### Issue: “YAML formatting error”

**Symptom:**

```sql
Error in the format of config.yaml
```

**Solutions:**

1. **Check indentation (use spaces, not tabs)**

   ```yaml
   # Correct
   tables:
     - fully_qualified_name: db.schema.table
       column_selection_list:
         - column1
         - column2
   ```

   Incorrect example (mixed indentation with tabs):

   ```text
   tables:
    - fully_qualified_name: db.schema.table
      column_selection_list:
        - column1
   ```

2. **Quote special characters:**

   ```yaml
   password: "p@ssw0rd!"    # Quote passwords with special chars
   where_clause: "name = 'O''Brien'"  # Escape quotes
   ```

3. **Validate YAML syntax** using online validators or:

   ```bash
   python -c "import yaml; yaml.safe_load(open('config.yaml'))"
   ```

#### Issue: “Validation fails with tolerance errors”

**Symptom:**

```sql
Metrics validation failed: Difference exceeds tolerance
```

**Solution:**
Adjust tolerance in configuration:

```yaml
comparison_configuration:
  tolerance: 0.05  # Increase to 5% tolerance
```

#### Issue: “Out of memory errors with large tables”

**Solutions:**

1. **Enable chunking:**

   ```yaml
   tables:
     - fully_qualified_name: large_table
       chunk_number: 100  # Process in smaller chunks
   ```

2. **Reduce thread count:**

   ```yaml
   max_threads: 4  # Use fewer threads
   ```

3. **Filter data:**

   ```yaml
   tables:
     - fully_qualified_name: large_table
       where_clause: "created_date >= '2024-01-01'"
   ```

4. **Exclude large columns:**

   ```yaml
   tables:
     - fully_qualified_name: large_table
       use_column_selection_as_exclude_list: true
       column_selection_list:
         - large_blob_column
         - large_text_column
   ```

### Getting Help

1. **Check logs:** Review log files in the output directory
2. **Enable debug logging:**

   ```bash
   sdv sqlserver run-validation \
     --data-validation-config-file config.yaml \
     --log-level DEBUG
   ```

3. **Review validation reports** in the output directory
4. **Consult documentation:** [Full Documentation](https://github.com/snowflake-eng/migrations-data-validation)
5. **Report issues:** Email us at:[snowconvert-support@snowflake.com](mailto:snowconvert-support%40snowflake.com)
