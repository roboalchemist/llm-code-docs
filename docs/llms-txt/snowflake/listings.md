# Source: https://docs.snowflake.com/en/sql-reference/info-schema/listings.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/listings.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# LISTINGS view

This Account Usage view returns all the listings owned by the current account, including dropped listings. The information in this view has a latency of up to 3 hours.

## Columns

The following table provides definitions for the LISTINGS view columns.

| Column | Data type | Description |
| --- | --- | --- |
| GLOBAL_NAME | VARCHAR | The global name of the listing. |
| NAME | VARCHAR | The object name of the listing. |
| OWNER | VARCHAR | The name of the role that owns the listing. |
| CREATED_ON | TIMESTAMP_LTZ | The timestamp when the listing was created. |
| UPDATED_ON | TIMESTAMP_LTZ | The timestamp when the listing was last updated. |
| PUBLISHED_ON | TIMESTAMP_LTZ | The timestamp when the listing was published. |
| DELETED_ON | TIMESTAMP_LTZ | The timestamp when the listing was deleted. This value is NULL if the listing hasn’t been deleted. |
| TITLE | VARCHAR | The title of the listing. |
| SUBTITLE | VARCHAR | The subtitle of the listing. |
| DESCRIPTION | VARCHAR | The description of the listing. |
| LISTING_TERMS | OBJECT | The terms of service associated with the listing. |
| STATE | VARCHAR | The current state of the listing. |
| SHARE | VARCHAR | The name of the share associated with the listing. |
| APPLICATION_PACKAGE | VARCHAR | The name of the application package associated with the listing. This is only populated if `IS_APPLICATION` is true. |
| DATA_ATTRIBUTES | OBJECT | Data attributes associated with the listing. |
| CATEGORIES | VARCHAR | Categories associated with the listing. |
| PROFILE | VARCHAR | The profile attached to the external listing. |
| CUSTOMIZED_CONTACT_INFO | VARCHAR | Customized contact information associated with the listing. |
| COMMENT | VARCHAR | Comment associated with the listing, if any. |
| TARGETS | OBJECT | Targets consolidating external/organizational listings with regions. |
| AUTO_FULFILLMENT | OBJECT | Auto-fulfillment information associated with the listing. |
| IS_SHARE | BOOLEAN | Indicates whether this is a data share listing. |
| IS_APPLICATION | BOOLEAN | Indicates whether this is an application listing. |
| DISTRIBUTION | VARCHAR | The distribution of the listing. Possible values are `EXTERNAL` and `ORGANIZATION`. |
| ORGANIZATION_PROFILE_NAME | VARCHAR | The organization profile attached to the listing. |
| UNIFORM_LISTING_LOCATOR | VARCHAR | The uniform listing locator (ULL) of the listing. |
| APPROVER_CONTACT | VARCHAR | The approver contact information associated with the listing. |
| SUPPORT_CONTACT | VARCHAR | The support contact information associated with the listing. |
| RESHARING | OBJECT | Resharing configuration of the listing. |
