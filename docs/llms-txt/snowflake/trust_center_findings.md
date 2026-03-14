# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/trust_center_findings.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/trust_center_findings.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# TRUST_CENTER_FINDINGS view

This Account Usage view shows security violations discovered by [Trust Center scanners](../../user-guide/trust-center/overview.md).

## Columns

| Column | Data Type | Description |
| --- | --- | --- |
| ID | NUMBER | System identifier of the account that had the finding. |
| PROVIDER_ID | VARCHAR | System identifier of the provider of the scanner package. |
| SCANNER_PACKAGE_ID | VARCHAR | System identifier of the scanner package. |
| SCANNER_ID | VARCHAR | System identifier of the scanner. |
| SEVERITY | VARCHAR | Severity of the finding, as assigned by the scanner [LOW, MEDIUM, HIGH, CRITICAL]. |
| STATE | VARCHAR | State of the finding [OPEN, RESOLVED, RESOLVED MANUALLY]. |
| CREATED_ON | TIMESTAMP_LTZ | The time at which the finding was initially created. |
| UPDATED_ON | TIMESTAMP_LTZ | The time at which the finding was last updated. |

## Usage notes

Latency for the view may be up to 60 minutes (1 hour).
