# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/postgresql-ssl-off.md

# PostgreSQL SSL Off

## Cause

This error means that your [PostgreSQL](/core-concepts/managed-databases/supported-databases/postgresql) client is configured to connect to without SSL, but PostgreSQL [Databases](/core-concepts/managed-databases/managing-databases/overview) on Aptible require SSL.

## Resolution

Many PostgreSQL clients allow enforcing SSL by appending `?ssl=true` to the default database connection URL provided by Aptible.

For some clients or libraries, it may be necessary to set this in the configuration code.

If you have questions about enabling SSL for your app's PostgreSQL library, please contact [Aptible Support](/how-to-guides/troubleshooting/aptible-support).
