# Source: https://docs.snowflake.com/en/sql-reference/account-usage/contacts.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# CONTACTS view

This Account Usage view displays a row for each [contact](../../user-guide/contacts-using.md) in the account.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| CONTACT_ID | NUMBER | Internal/system-generated identifier of the contact. |
| CONTACT_NAME | VARCHAR | Name of the contact. |
| CONTACT_SCHEMA_ID | NUMBER | Internal/system-generated identifier of the schema in which the contact exists. |
| CONTACT_SCHEMA | VARCHAR | Name of the schema in which the contact exists. |
| CONTACT_DATABASE_ID | NUMBER | Internal/system-generated identifier of the database in which the contact exists. |
| CONTACT_DATABASE | VARCHAR | Name of the database in which the contact exists. |
| CONTACT_OWNER | VARCHAR | Name of the role that owns the contact. |
| CONTACT_OWNER_ROLE_TYPE | VARCHAR | Type of role that owns the object. Either ROLE, DATABASE_ROLE, or APPLICATION (if a Snowflake Native App owns the object).  Deleted contacts have a NULL value. |
| CONTACT_USERS | ARRAY | Array of Snowflake users to contact. |
| CONTACT_EMAIL_DISTRIBUTION_LIST | VARCHAR | Email address used to communicate with the contact. |
| CONTACT_URL | VARCHAR | URL used to communicate with the contact. |
| COMMENT | VARCHAR | Comments for the contact, if any. |
| CREATED | TIMESTAMP_LTZ | Date and time when the contact was created. |
| LAST_ALTERED | TIMESTAMP_LTZ | Date and time the object was last altered. |
| DELETED | TIMESTAMP_LTZ | Date and time when the contact was dropped or the date and time when its parent was dropped. |

## Usage notes

* Latency for the view is 2 hours.
