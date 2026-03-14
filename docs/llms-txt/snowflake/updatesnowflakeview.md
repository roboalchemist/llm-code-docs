# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/updatesnowflakeview.md

# UpdateSnowflakeView 2025.10.9.21

## Bundle

com.snowflake.openflow.runtime | runtime-snowflake-processors-nar

## Description

Creates or replaces Snowflake views based on column mappings provided in the incoming FlowFile. The processor checks if the view exists and only recreates it if the definition has changed. The FlowFile content should contain JSON with column mappings, optional join configuration, and optional flatten configuration: { “columns”: [ { “source_field”: “customer_data:id”, “destination_column”: “customer_id”, “type”: “VARCHAR” }, { “source_field”: “f.value:order_amount”, “destination_column”: “order_amount”, “type”: “NUMBER” }, { “expression”: “SUM(f.value:order_amount::NUMBER)”, “destination_column”: “total_amount” }, { “expression”: “COUNT(\*)”, “destination_column”: “order_count” } ], “from”: { “table”: “raw_data”, “alias”: “rd”, “joins”: [ { “type”: “INNER”, “table”: “customers”, “alias”: “c”, “on”: “customer_data:id::VARCHAR = c.customer_id” } ] }, “flatten”: [ { “input”: “rd.orders”, “alias”: “f”, “path”: null } ], “where”: “active = true AND status =’VALID’”, “group_by”: [“customer_id”, “region”], “order_by”: [“order_amount DESC”, “customer_id ASC”] } Column configuration supports: - source_field: Simple field/column reference (supports JSON notation like “data:field” or table aliases like “t.column”) - expression: Complex SQL expression (e.g., “SUM(amount)”, “COUNT(\*)”) - destination_column: The output column name in the view (optional - auto-generated if not provided) - type: Snowflake data type for automatic type casting (VARCHAR, NUMBER, BOOLEAN, DATE, TIMESTAMP, etc.) Use either source_field OR expression, not both. When type is specified, automatic type casting is applied. When type is omitted, the expression is used as-is without casting. Flatten configuration supports: - input: The nested field/column to flatten (required) - alias: Alias for the flattened data (required) - path: Optional path within the nested structure The “from” section is required and specifies the source table and optional joins. Optional SQL clauses can be included: - where: WHERE clause condition (e.g., “active = true AND status =’VALID’”) - group_by: GROUP BY clause as an array of column names (e.g., [“customer_id”, “region”]) - order_by: ORDER BY clause as an array of column/expression with direction (e.g., [“order_amount DESC”, “customer_id ASC”])

## Tags

flatten, view

## Input Requirement

REQUIRED

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| Connection Pool | The connection pool to use to connect to Snowflake |
| Schema Name | The name of the schema where the view will be created |
| Secure | Whether to create a secure view. Secure views hide the view definition from unauthorized users. |
| View Name | The name of the view to create or update |

## Relationships

| Name | Description |
| --- | --- |
| failure | FlowFiles that failed to be processed |
| success | FlowFiles that were successfully processed |
| unchanged | FlowFiles where the view already exists and hasn’t changed |
