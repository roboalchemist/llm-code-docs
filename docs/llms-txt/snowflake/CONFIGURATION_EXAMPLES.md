# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/data-validation-cli/CONFIGURATION_EXAMPLES.md

# Configuration File Examples

This document provides ready-to-use configuration examples for various validation scenarios. Copy and adapt these examples for your specific use case.

## Table of Contents

* SQL Server Examples
* Teradata Examples
* Redshift Examples
* Snowflake Examples
* Scenario-Based Examples
* View Validation Examples

---

## SQL Server Examples

### Example 1: Minimal SQL Server Configuration

Perfect for quick testing or simple validations.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./validation_output

source_connection:
  mode: credentials
  host: localhost
  port: 1433
  username: sa
  password: YourPassword123
  database: TestDB

target_connection:
  mode: default

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

tables:
  - fully_qualified_name: TestDB.dbo.Customers
    use_column_selection_as_exclude_list: false
    column_selection_list: []
```

### Example 2: Production SQL Server with SSL/TLS

Secure production setup with proper encryption settings.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: /data/validation/production
max_threads: 16

source_connection:
  mode: credentials
  host: sqlserver-prod.company.com
  port: 1433
  username: validation_user
  password: SecurePassword123!
  database: PRODUCTION_DB
  trust_server_certificate: "no"
  encrypt: "yes"

target_connection:
  mode: name
  name: snowflake_production

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 250

comparison_configuration:
  tolerance: 0.01

logging_configuration:
  level: INFO
  console_level: WARNING
  file_level: DEBUG

database_mappings:
  PRODUCTION_DB: PROD_SNOWFLAKE

schema_mappings:
  dbo: PUBLIC

tables:
  - fully_qualified_name: PRODUCTION_DB.dbo.Orders
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - order_id
    chunk_number: 20

  - fully_qualified_name: PRODUCTION_DB.dbo.Customers
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - ssn
      - credit_card_number
    index_column_list:
      - customer_id

  - fully_qualified_name: PRODUCTION_DB.dbo.Products
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - product_id
      - product_name
      - price
      - category
    where_clause: "is_active = 1"
    target_where_clause: "is_active = 1"
```

### Example 3: SQL Server Incremental Validation

Validate only recent changes using date filters.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./incremental_validation
max_threads: auto

source_connection:
  mode: credentials
  host: sqlserver.company.com
  port: 1433
  username: etl_user
  password: EtlPassword123
  database: DataWarehouse

target_connection:
  mode: name
  name: snowflake_dw

validation_configuration:
  schema_validation: false
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 100

comparison_configuration:
  tolerance: 0.001

tables:
  - fully_qualified_name: DataWarehouse.dbo.FactSales
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - transaction_id
    where_clause: "transaction_date >= DATEADD(day, -7, GETDATE())"
    target_where_clause: "transaction_date >= DATEADD(day, -7, CURRENT_TIMESTAMP)"
    chunk_number: 10

  - fully_qualified_name: DataWarehouse.dbo.DimCustomer
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    where_clause: "modified_date >= DATEADD(day, -7, GETDATE())"
    target_where_clause: "modified_date >= DATEADD(day, -7, CURRENT_TIMESTAMP)"
```

### Example 4: SQL Server with Column Mappings

Handle renamed columns during migration.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./validation_with_mappings
max_threads: 8

source_connection:
  mode: credentials
  host: legacy-sql.company.com
  port: 1433
  username: migration_user
  password: MigrationPass123
  database: LegacyDB

target_connection:
  mode: name
  name: snowflake_modernized

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true

tables:
  - fully_qualified_name: LegacyDB.dbo.CustomerMaster
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - cust_id
      - cust_name
      - cust_email
      - cust_phone
      - addr_line1
      - addr_line2
      - addr_city
      - addr_state
      - addr_zip
    index_column_list:
      - cust_id
    column_mappings:
      cust_id: customer_id
      cust_name: customer_name
      cust_email: email_address
      cust_phone: phone_number
      addr_line1: address_line_1
      addr_line2: address_line_2
      addr_city: city
      addr_state: state
      addr_zip: postal_code
```

---

## Teradata Examples

### Example 5: Basic Teradata Configuration

Simple Teradata to Snowflake validation.

```yaml
source_platform: Teradata
target_platform: Snowflake
output_directory_path: ./teradata_validation
target_database: SNOWFLAKE_DB
max_threads: auto

source_connection:
  mode: credentials
  host: teradata.company.com
  username: td_user
  password: TeradataPass123
  database: PROD_DB

target_connection:
  mode: default

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

tables:
  - fully_qualified_name: PROD_DB.sales_data
    use_column_selection_as_exclude_list: false
    column_selection_list: []
```

### Example 6: Teradata Large-Scale Migration

Enterprise-scale Teradata migration validation.

```yaml
source_platform: Teradata
target_platform: Snowflake
output_directory_path: /opt/validation/teradata_migration
target_database: ENTERPRISE_DW
max_threads: 32

source_connection:
  mode: credentials
  host: teradata-prod.company.com
  username: validation_service
  password: SecureTdPassword!123
  database: ENTERPRISE_TD

target_connection:
  mode: name
  name: snowflake_enterprise

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 500
  exclude_metrics: false

comparison_configuration:
  tolerance: 0.005

logging_configuration:
  level: INFO
  console_level: ERROR
  file_level: DEBUG

schema_mappings:
  ENTERPRISE_TD: PUBLIC

tables:
  # Large fact table - high chunking
  - fully_qualified_name: ENTERPRISE_TD.fact_transactions
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - transaction_key
    chunk_number: 100
    max_failed_rows_number: 1000

  # Dimension table with exclusions
  - fully_qualified_name: ENTERPRISE_TD.dim_customer
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - ssn
      - tax_id
      - bank_account
    index_column_list:
      - customer_key
    chunk_number: 20

  # Filtered validation for current year only
  - fully_qualified_name: ENTERPRISE_TD.fact_sales
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - sale_key
    where_clause: "sale_date >= DATE '2024-01-01'"
    target_where_clause: "sale_date >= DATE '2024-01-01'"
    chunk_number: 50
```

### Example 7: Teradata Multi-Schema Validation

Validate multiple schemas with different settings.

```yaml
source_platform: Teradata
target_platform: Snowflake
output_directory_path: ./multi_schema_validation
target_database: MULTI_SCHEMA_DW
max_threads: 16

source_connection:
  mode: credentials
  host: teradata.company.com
  username: schema_validator
  password: ValidatorPass123
  database: DBC

target_connection:
  mode: name
  name: snowflake_multi_schema

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 200

comparison_configuration:
  tolerance: 0.01

schema_mappings:
  SALES_SCHEMA: SALES
  FINANCE_SCHEMA: FINANCE
  HR_SCHEMA: HUMAN_RESOURCES

tables:
  # Sales schema tables
  - fully_qualified_name: SALES_SCHEMA.orders
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - order_id

  - fully_qualified_name: SALES_SCHEMA.order_details
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - order_id
      - line_number

  # Finance schema tables
  - fully_qualified_name: FINANCE_SCHEMA.invoices
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - invoice_id
    chunk_number: 30

  # HR schema tables - exclude sensitive data
  - fully_qualified_name: HR_SCHEMA.employees
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - ssn
      - salary
      - bank_account
      - emergency_contact
    index_column_list:
      - employee_id
```

---

## Redshift Examples

### Example 8: Basic Redshift Configuration

Simple Redshift to Snowflake validation.

```yaml
source_platform: Redshift
target_platform: Snowflake
output_directory_path: ./redshift_validation
max_threads: auto

source_connection:
  mode: credentials
  host: redshift-cluster.us-east-1.redshift.amazonaws.com
  port: 5439
  username: redshift_user
  password: RedshiftPass123
  database: analytics

target_connection:
  mode: default

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

tables:
  - fully_qualified_name: public.events
    use_column_selection_as_exclude_list: false
    column_selection_list: []
```

### Example 9: Redshift Data Lake Migration

Validate Redshift data lake migration to Snowflake.

```yaml
source_platform: Redshift
target_platform: Snowflake
output_directory_path: /data/validation/redshift_datalake
max_threads: 24

source_connection:
  mode: credentials
  host: datalake-cluster.us-west-2.redshift.amazonaws.com
  port: 5439
  username: datalake_validator
  password: SecureRedshiftPass!123
  database: datalake

target_connection:
  mode: name
  name: snowflake_datalake

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 500

comparison_configuration:
  tolerance: 0.02

logging_configuration:
  level: INFO
  console_level: WARNING
  file_level: DEBUG

database_mappings:
  datalake: DATALAKE_PROD

schema_mappings:
  public: PUBLIC
  staging: STAGING
  analytics: ANALYTICS

tables:
  # Raw data staging
  - fully_qualified_name: staging.raw_events
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - event_id
    chunk_number: 80
    max_failed_rows_number: 1000

  # Analytics tables
  - fully_qualified_name: analytics.user_sessions
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - session_id
    where_clause: "session_date >= CURRENT_DATE - 30"
    target_where_clause: "session_date >= CURRENT_DATE - 30"
    chunk_number: 40

  - fully_qualified_name: analytics.aggregated_metrics
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - metric_id
      - date_key
    chunk_number: 20

  # Public schema - exclude system columns
  - fully_qualified_name: public.customer_360
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - _sys_created_at
      - _sys_modified_at
      - _sys_user_id
    index_column_list:
      - customer_id
    chunk_number: 50
```

### Example 10: Redshift with Complex Filtering

Advanced filtering and column selection for Redshift.

```yaml
source_platform: Redshift
target_platform: Snowflake
output_directory_path: ./complex_validation
max_threads: 16

source_connection:
  mode: credentials
  host: analytics-cluster.region.redshift.amazonaws.com
  port: 5439
  username: validator
  password: ComplexPass123!
  database: analytics_db

target_connection:
  mode: name
  name: snowflake_analytics

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 100

comparison_configuration:
  tolerance: 0.01

tables:
  # Complex WHERE clause with multiple conditions
  - fully_qualified_name: public.transactions
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - transaction_id
      - customer_id
      - amount
      - transaction_date
      - status
      - payment_method
    index_column_list:
      - transaction_id
    where_clause: "status IN ('completed', 'settled') AND amount > 100 AND transaction_date >= '2024-01-01' AND payment_method != 'test'"
    target_where_clause: "status IN ('completed', 'settled') AND amount > 100 AND transaction_date >= '2024-01-01' AND payment_method != 'test'"
    chunk_number: 30

  # Date-based partitioned validation
  - fully_qualified_name: public.daily_metrics
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - metric_date
      - metric_id
    where_clause: "metric_date >= DATE_TRUNC('month', CURRENT_DATE)"
    target_where_clause: "metric_date >= DATE_TRUNC('month', CURRENT_DATE)"
    chunk_number: 10

  # Selective column validation with mappings
  - fully_qualified_name: public.legacy_customers
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - cust_no
      - full_name
      - email_addr
      - phone_num
      - signup_dt
    index_column_list:
      - cust_no
    column_mappings:
      cust_no: customer_number
      full_name: customer_name
      email_addr: email
      phone_num: phone
      signup_dt: signup_date
```

---

## Snowflake Examples

### Example 10.1: Basic Snowflake-to-Snowflake Configuration

Simple Snowflake-to-Snowflake validation for cross-account or cross-database migration.

```yaml
source_platform: Snowflake
target_platform: Snowflake
output_directory_path: ./snowflake_validation
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
  row_validation: false

tables:
  - fully_qualified_name: SOURCE_DB.PUBLIC.CUSTOMERS
    target_database: TARGET_DB
    target_schema: PUBLIC
    target_name: CUSTOMERS
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - CUSTOMER_ID
```

### Example 10.2: Cross-Account Migration Validation

Enterprise-scale Snowflake cross-account migration validation.

```yaml
source_platform: Snowflake
target_platform: Snowflake
output_directory_path: /opt/validation/cross_account
max_threads: 24

source_connection:
  mode: name
  name: account_a_connection

target_connection:
  mode: name
  name: account_b_connection

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 300

comparison_configuration:
  tolerance: 0.01

logging_configuration:
  level: INFO
  console_level: WARNING
  file_level: DEBUG

database_mappings:
  ANALYTICS_A: ANALYTICS_B

schema_mappings:
  RAW: RAW_DATA
  STAGING: STAGING_DATA

tables:
  # Large fact table with chunking
  - fully_qualified_name: ANALYTICS_A.RAW.FACT_TRANSACTIONS
    target_database: ANALYTICS_B
    target_schema: RAW_DATA
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - TRANSACTION_ID
    chunk_number: 50
    max_failed_rows_number: 500

  # Dimension table with exclusions
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

### Example 10.3: Cross-Region Replication Validation

Validate data replication between Snowflake regions.

```yaml
source_platform: Snowflake
target_platform: Snowflake
output_directory_path: /data/validation/region_replication
max_threads: 16

source_connection:
  mode: name
  name: us_east_connection

target_connection:
  mode: name
  name: eu_west_connection

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 150

comparison_configuration:
  tolerance: 0.005

tables:
  # Recent transactions
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

  # Reference table
  - fully_qualified_name: GLOBAL_DB.REPLICATION.CURRENCIES
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - CURRENCY_CODE
```

### Example 10.4: Database Copy Validation

Validate a database copy within the same Snowflake account.

```yaml
source_platform: Snowflake
target_platform: Snowflake
output_directory_path: ./db_copy_validation
max_threads: auto

source_connection:
  mode: name
  name: prod_connection

target_connection:
  mode: name
  name: prod_connection

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

comparison_configuration:
  tolerance: 0.001

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

---

## Scenario-Based Examples

### Example 11: Development Environment - Fast Validation

Quick validation for development with minimal overhead.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./dev_validation
max_threads: 4

source_connection:
  mode: credentials
  host: localhost
  port: 1433
  username: dev_user
  password: DevPass123
  database: DevDB
  trust_server_certificate: "yes"
  encrypt: "no"

target_connection:
  mode: default

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false  # Skip for speed

comparison_configuration:
  tolerance: 0.05  # More lenient

logging_configuration:
  level: WARNING  # Less verbose

tables:
  - fully_qualified_name: DevDB.dbo.TestTable1
    use_column_selection_as_exclude_list: false
    column_selection_list: []

  - fully_qualified_name: DevDB.dbo.TestTable2
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    where_clause: "id <= 1000"  # Limit rows for speed
    target_where_clause: "id <= 1000"
```

### Example 12: Staging Environment - Comprehensive Testing

Thorough validation for staging environment.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: /staging/validation
max_threads: 12

source_connection:
  mode: credentials
  host: sqlserver-staging.company.com
  port: 1433
  username: staging_validator
  password: StagingPass123!
  database: STAGING_DB
  trust_server_certificate: "no"
  encrypt: "yes"

target_connection:
  mode: name
  name: snowflake_staging

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 200

comparison_configuration:
  tolerance: 0.01

logging_configuration:
  level: INFO
  console_level: INFO
  file_level: DEBUG

tables:
  - fully_qualified_name: STAGING_DB.dbo.Orders
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - order_id
    chunk_number: 15

  - fully_qualified_name: STAGING_DB.dbo.Customers
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - customer_id
    chunk_number: 10
```

### Example 13: Production - Maximum Performance

Optimized for large-scale production validation.

```yaml
source_platform: Teradata
target_platform: Snowflake
output_directory_path: /prod/validation
target_database: PROD_SNOWFLAKE
max_threads: 32  # Maximum parallelization

source_connection:
  mode: credentials
  host: teradata-prod.company.com
  username: prod_validator
  password: SecureProdPass!123
  database: PROD_TD

target_connection:
  mode: name
  name: snowflake_prod

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 1000
  exclude_metrics: false

comparison_configuration:
  tolerance: 0.001  # Strict tolerance

logging_configuration:
  level: INFO
  console_level: ERROR  # Minimal console output
  file_level: DEBUG  # Detailed file logging

tables:
  # Massive fact table - heavy chunking
  - fully_qualified_name: PROD_TD.fact_transactions
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - transaction_key
    chunk_number: 200  # Maximum chunking
    max_failed_rows_number: 5000

  # Other tables...
  - fully_qualified_name: PROD_TD.fact_sales
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - sale_key
    chunk_number: 150
```

### Example 14: PII-Compliant Validation

Exclude sensitive personally identifiable information.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./pii_compliant_validation
max_threads: auto

source_connection:
  mode: credentials
  host: sqlserver.company.com
  port: 1433
  username: compliance_validator
  password: CompliancePass123!
  database: CustomerDB

target_connection:
  mode: name
  name: snowflake_customer

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 100

comparison_configuration:
  tolerance: 0.01

tables:
  - fully_qualified_name: CustomerDB.dbo.Customers
    use_column_selection_as_exclude_list: true
    column_selection_list:
      # Exclude all PII columns
      - ssn
      - tax_id
      - date_of_birth
      - drivers_license
      - passport_number
      - credit_card_number
      - bank_account_number
      - email_address
      - phone_number
      - home_address
      - mailing_address
    index_column_list:
      - customer_id

  - fully_qualified_name: CustomerDB.dbo.Transactions
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - credit_card_last4
      - account_number
      - routing_number
    index_column_list:
      - transaction_id
```

### Example 15: Migration Cutover Validation

Final validation before production cutover.

```yaml
source_platform: Redshift
target_platform: Snowflake
output_directory_path: /cutover/validation
max_threads: 32

source_connection:
  mode: credentials
  host: redshift-prod.amazonaws.com
  port: 5439
  username: cutover_validator
  password: CutoverPass123!
  database: production

target_connection:
  mode: name
  name: snowflake_production_new

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 0  # Zero tolerance for cutover

comparison_configuration:
  tolerance: 0.0001  # Extremely strict

logging_configuration:
  level: DEBUG  # Maximum detail
  console_level: INFO
  file_level: DEBUG

# Validate ALL tables
tables:
  - fully_qualified_name: public.customers
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - customer_id
    chunk_number: 50

  - fully_qualified_name: public.orders
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - order_id
    chunk_number: 100

  - fully_qualified_name: public.order_items
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - order_id
      - item_id
    chunk_number: 150

  - fully_qualified_name: public.products
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - product_id
    chunk_number: 20

  - fully_qualified_name: public.inventory
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - inventory_id
    chunk_number: 30
```

### Example 16: Continuous Validation - Daily Incremental

Daily validation of incremental loads.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: /daily/validation
max_threads: 16

source_connection:
  mode: credentials
  host: sqlserver.company.com
  port: 1433
  username: daily_validator
  password: DailyPass123!
  database: ETL_DB

target_connection:
  mode: name
  name: snowflake_daily

validation_configuration:
  schema_validation: false  # Skip schema check for daily runs
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 100

comparison_configuration:
  tolerance: 0.01

logging_configuration:
  level: INFO
  console_level: WARNING
  file_level: INFO

tables:
  # Validate only yesterday's data
  - fully_qualified_name: ETL_DB.dbo.DailyTransactions
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - transaction_id
    where_clause: "CAST(created_date AS DATE) = CAST(DATEADD(day, -1, GETDATE()) AS DATE)"
    target_where_clause: "CAST(created_date AS DATE) = CAST(DATEADD(day, -1, CURRENT_TIMESTAMP) AS DATE)"
    chunk_number: 10

  - fully_qualified_name: ETL_DB.dbo.DailyOrders
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - order_id
    where_clause: "CAST(order_date AS DATE) = CAST(DATEADD(day, -1, GETDATE()) AS DATE)"
    target_where_clause: "CAST(order_date AS DATE) = CAST(DATEADD(day, -1, CURRENT_TIMESTAMP) AS DATE)"
    chunk_number: 5
```

---

## View Validation Examples

### Example 17: Basic View Validation

Validate database views alongside tables for comprehensive migration verification.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./view_validation
max_threads: auto

source_connection:
  mode: credentials
  host: sqlserver.company.com
  port: 1433
  username: view_validator
  password: ViewPass123!
  database: ReportingDB
  trust_server_certificate: "no"
  encrypt: "yes"

target_connection:
  mode: name
  name: snowflake_reporting

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

views:
  - fully_qualified_name: ReportingDB.dbo.customer_summary
    use_column_selection_as_exclude_list: false
    column_selection_list: []

  - fully_qualified_name: ReportingDB.dbo.sales_by_region
    use_column_selection_as_exclude_list: false
    column_selection_list: []

  - fully_qualified_name: ReportingDB.dbo.monthly_revenue
    use_column_selection_as_exclude_list: false
    column_selection_list: []
```

### Example 18: Combined Tables and Views Validation

Validate both tables and views in a single configuration.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./combined_validation
max_threads: 16

source_connection:
  mode: credentials
  host: sqlserver.company.com
  port: 1433
  username: migration_user
  password: MigrationPass123!
  database: AnalyticsDB
  trust_server_certificate: "no"
  encrypt: "yes"

target_connection:
  mode: name
  name: snowflake_analytics

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 100

comparison_configuration:
  tolerance: 0.01

# Base tables
tables:
  - fully_qualified_name: AnalyticsDB.dbo.customers
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - customer_id

  - fully_qualified_name: AnalyticsDB.dbo.orders
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - order_id
    chunk_number: 20

  - fully_qualified_name: AnalyticsDB.dbo.products
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - product_id

# Derived views
views:
  - fully_qualified_name: AnalyticsDB.dbo.vw_customer_orders
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - customer_id
      - order_id

  - fully_qualified_name: AnalyticsDB.dbo.vw_product_sales
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - product_id
      - product_name
      - total_quantity
      - total_revenue
    index_column_list:
      - product_id

  - fully_qualified_name: AnalyticsDB.dbo.vw_monthly_summary
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    where_clause: "year >= 2024"
    target_where_clause: "year >= 2024"
```

### Example 19: Teradata View Validation

Validate Teradata views migrated to Snowflake.

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
  row_validation: false

schema_mappings:
  DW_DB: PUBLIC

views:
  - fully_qualified_name: DW_DB.v_customer_360
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - ssn
      - credit_score
    # Exclude sensitive columns

  - fully_qualified_name: DW_DB.v_sales_dashboard
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - region
      - quarter
      - total_sales
      - order_count
      - avg_order_value

  - fully_qualified_name: DW_DB.v_inventory_status
    use_column_selection_as_exclude_list: false
    column_selection_list: []
```

### Example 20: Redshift View Validation with Column Mappings

Validate Redshift views with column name changes.

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

views:
  - fully_qualified_name: reports.v_user_activity
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - user_id
      - last_login
      - session_count
      - total_duration
    index_column_list:
      - user_id
    column_mappings:
      user_id: USER_ID
      last_login: LAST_LOGIN_DATE
      session_count: SESSIONS
      total_duration: DURATION_MINUTES

  - fully_qualified_name: reports.v_conversion_funnel
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    where_clause: "event_date >= CURRENT_DATE - 30"
    target_where_clause: "event_date >= CURRENT_DATE - 30"

  - fully_qualified_name: public.v_daily_metrics
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - metric_date
      - metric_type
```

### Example 21: View Validation with Different Target Names

Validate views when source and target view names differ.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./renamed_view_validation
max_threads: auto

source_connection:
  mode: credentials
  host: legacy-sql.company.com
  port: 1433
  username: migration_user
  password: MigrationPass123!
  database: LegacyDB
  trust_server_certificate: "yes"
  encrypt: "optional"

target_connection:
  mode: name
  name: snowflake_modernized

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: false

views:
  # Legacy view renamed in Snowflake
  - fully_qualified_name: LegacyDB.dbo.vw_cust_master
    target_database: MODERN_DB
    target_schema: ANALYTICS
    target_name: CUSTOMER_MASTER_VIEW
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - cust_id
      - cust_name
      - cust_type
      - region
    column_mappings:
      cust_id: CUSTOMER_ID
      cust_name: CUSTOMER_NAME
      cust_type: CUSTOMER_TYPE

  # View with schema change only
  - fully_qualified_name: LegacyDB.dbo.vw_sales_summary
    target_schema: SALES
    use_column_selection_as_exclude_list: false
    column_selection_list: []

  # View with database change only
  - fully_qualified_name: LegacyDB.reports.vw_quarterly_report
    target_database: REPORTING_DB
    use_column_selection_as_exclude_list: false
    column_selection_list: []
```

### Example 22: Large View Validation with Chunking

Validate large views with chunking for better performance.

```yaml
source_platform: SqlServer
target_platform: Snowflake
output_directory_path: ./large_view_validation
max_threads: 32

source_connection:
  mode: credentials
  host: sqlserver-prod.company.com
  port: 1433
  username: prod_validator
  password: ProdPass123!
  database: DataWarehouse
  trust_server_certificate: "no"
  encrypt: "yes"

target_connection:
  mode: name
  name: snowflake_dw

validation_configuration:
  schema_validation: true
  metrics_validation: true
  row_validation: true
  max_failed_rows_number: 500

comparison_configuration:
  tolerance: 0.005

views:
  # Large aggregated view with chunking
  - fully_qualified_name: DataWarehouse.dbo.vw_transaction_history
    use_column_selection_as_exclude_list: false
    column_selection_list: []
    index_column_list:
      - transaction_id
    chunk_number: 50
    max_failed_rows_number: 1000
    where_clause: "transaction_date >= '2024-01-01'"
    target_where_clause: "transaction_date >= '2024-01-01'"

  # Customer analytics view
  - fully_qualified_name: DataWarehouse.dbo.vw_customer_analytics
    use_column_selection_as_exclude_list: true
    column_selection_list:
      - internal_score
      - risk_flag
    index_column_list:
      - customer_id
    chunk_number: 25

  # Time-series metrics view
  - fully_qualified_name: DataWarehouse.dbo.vw_hourly_metrics
    use_column_selection_as_exclude_list: false
    column_selection_list:
      - metric_hour
      - metric_type
      - value
      - count
    index_column_list:
      - metric_hour
      - metric_type
    chunk_number: 100
    where_clause: "metric_hour >= DATEADD(month, -3, GETDATE())"
    target_where_clause: "metric_hour >= DATEADD(month, -3, CURRENT_TIMESTAMP)"
```

---

## Tips for Adapting These Examples

1. **Replace connection details** with your actual database credentials
2. **Update table names** to match your schema
3. **Adjust `max_threads`** based on your system resources
4. **Modify `chunk_number`** based on table sizes
5. **Set appropriate `tolerance`** based on your data characteristics
6. **Customize `where_clause`** for your filtering needs
7. **Add/remove columns** in `column_selection_list` as needed
8. **Update `column_mappings`** if column names differ

## Security Best Practices

* **Never commit** configuration files with real passwords to version control
* Use **environment variables** for sensitive data
* Consider **secret management** tools (AWS Secrets Manager, Azure Key Vault, etc.)
* Use **least privilege** database accounts for validation
* **Encrypt** configuration files containing sensitive information
