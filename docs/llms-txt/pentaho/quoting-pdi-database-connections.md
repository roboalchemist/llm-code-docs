# Source: https://docs.pentaho.com/pdia-data-integration/extracting-data-into-pdi/quoting-pdi-database-connections.md

# Quoting PDI database connections

Pentaho uses a database-specific quoting system. With this system, you can use any name or character that complies with the supported databases' naming conventions.

Both PUC and PDI contain a list of reserved words for most of the supported databases. Pentaho maintains a strict separation between the schema (the user or owner of a table) and the table name itself to correctly quote table or field names that contain one or more periods in them. Placing periods in table and field names is common practice in some ERP systems (for example, fields such as `V.A.T.`)

To avoid quoting-related errors, a rule stops the Pentaho software from performing quoting activity when there is a start or end quotation mark in the table or schema name. This allows you to specify the quoting mechanism yourself.
