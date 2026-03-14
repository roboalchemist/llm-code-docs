# Source: https://docs.snowflake.com/en/sql-reference/ddl-user-security.md

# User & security DDL

Snowflake provides a full set of SQL commands for managing users and security. These commands can only be executed by users who are granted roles that have the OWNERSHIP privilege on the managed object. This is usually restricted to the
ACCOUNTADMIN and SECURITYADMIN roles.

However, individual users are able to perform the following tasks for themselves:

* Change their password (only through the web interface).
* View their user information (via [DESCRIBE USER](sql/desc-user.md)).
* Change their default role, virtual warehouse, or namespace (via [ALTER USER](sql/alter-user.md)).
* Change their session parameters (via [ALTER SESSION](sql/alter-session.md)).

## User management

Each user with access to Snowflake is represented by a user object. A user object stores all of the information about the user, including their login name, password, and defaults (role, virtual warehouse, and namespace). Use the following
DDL commands to manage users in the system:

* [CREATE USER](sql/create-user.md)
* [ALTER USER](sql/alter-user.md)
* [DROP USER](sql/drop-user.md)
* [DESCRIBE USER](sql/desc-user.md)
* [SHOW USERS](sql/show-users.md)

## Role management

Snowflake uses roles to control access to objects in the system:

* Roles are granted access privileges for objects in the system (databases, tables, etc.).
* Roles are granted to users to enable them to create, modify, and use the objects for which the roles have privileges.
* Roles can be granted to other roles to support defining hierarchical access privileges.

Use the following DDL commands to manage roles in the system:

* [CREATE ROLE](sql/create-role.md)
* [ALTER ROLE](sql/alter-role.md)
* [DROP ROLE](sql/drop-role.md)
* [SHOW ROLES](sql/show-roles.md)

Use the following DDL commands to manage database roles in the system:

* [CREATE DATABASE ROLE](sql/create-database-role.md)
* [ALTER DATABASE ROLE](sql/alter-database-role.md)
* [DROP DATABASE ROLE](sql/drop-database-role.md)
* [SHOW DATABASE ROLES](sql/show-database-roles.md)

Use the following command to activate a primary role or secondary roles within a user session:

* [USE ROLE](sql/use-role.md)
* [USE SECONDARY ROLES](sql/use-secondary-roles.md)

## Object tagging management

Snowflake supports the following DDL to create and manage tags:

* [CREATE TAG](sql/create-tag.md)
* [ALTER TAG](sql/alter-tag.md)
* [ALTER <object>](sql/alter.md) (to set a tag on a Snowflake object)
* [SHOW TAGS](sql/show-tags.md)
* [DROP TAG](sql/drop-tag.md)
* [UNDROP TAG](sql/undrop-tag.md)

Note that Snowflake does not support the [describe](sql/desc.md) operation for the tag object.

## Access control management

Use the following commands to manage access control for objects by granting (and revoking) object privileges to roles and granting roles to users and other roles:

* [GRANT <privileges> … TO ROLE](sql/grant-privilege.md)
* [REVOKE <privileges> … FROM ROLE](sql/revoke-privilege.md)
* [GRANT <privilege> … TO SHARE](sql/grant-privilege-share.md)
* [REVOKE <privilege> … FROM SHARE](sql/revoke-privilege-share.md)
* [GRANT DATABASE ROLE … TO SHARE](sql/grant-database-role-share.md)
* [REVOKE DATABASE ROLE … FROM SHARE](sql/revoke-database-role-share.md)
* [GRANT OWNERSHIP](sql/grant-ownership.md)
* [GRANT ROLE](sql/grant-role.md)
* [GRANT DATABASE ROLE](sql/grant-database-role.md)
* [REVOKE ROLE](sql/revoke-role.md)
* [REVOKE DATABASE ROLE](sql/revoke-database-role.md)
* [SHOW GRANTS](sql/show-grants.md)

## Network policy management

A network policy supports restricting access to your account based on user IP address. Use the following commands to create, alter, or drop network policies:

* [ALTER NETWORK POLICY](sql/alter-network-policy.md)
* [CREATE NETWORK POLICY](sql/create-network-policy.md)
* [DESCRIBE NETWORK POLICY](sql/desc-network-policy.md)
* [DROP NETWORK POLICY](sql/drop-network-policy.md)
* [SHOW NETWORK POLICIES](sql/show-network-policies.md)

## Secret management

Snowflake supports the following DDL commands and operations to manage secrets:

* [CREATE SECRET](sql/create-secret.md)
* [ALTER SECRET](sql/alter-secret.md)
* [DROP SECRET](sql/drop-secret.md)
* [SHOW SECRETS](sql/show-secrets.md)
* [DESCRIBE SECRET](sql/desc-secret.md)

## Password policy management

Snowflake provides the following DDL commands to manage password policy objects:

* [CREATE PASSWORD POLICY](sql/create-password-policy.md)
* [ALTER PASSWORD POLICY](sql/alter-password-policy.md)
* [DROP PASSWORD POLICY](sql/drop-password-policy.md)
* [SHOW PASSWORD POLICIES](sql/show-password-policies.md)
* [DESCRIBE PASSWORD POLICY](sql/desc-password-policy.md)

## Session policy management

Snowflake provides the following DDL commands to manage session policy objects:

* [CREATE SESSION POLICY](sql/create-session-policy.md)
* [ALTER SESSION POLICY](sql/alter-session-policy.md)
* [DROP SESSION POLICY](sql/drop-session-policy.md)
* [SHOW SESSION POLICIES](sql/show-session-policies.md)
* [DESCRIBE SESSION POLICY](sql/desc-session-policy.md)

## Third-party integrations

An integration is a Snowflake object that provides an interface between Snowflake and third-party services. Use the following commands to create, alter, or drop integrations:

### API integrations

* [ALTER API INTEGRATION](sql/alter-api-integration.md)
* [CREATE API INTEGRATION](sql/create-api-integration.md)
* [DESCRIBE INTEGRATION](sql/desc-integration.md)
* [DROP INTEGRATION](sql/drop-integration.md)
* [SHOW INTEGRATIONS](sql/show-integrations.md)

### Notification integrations

* [ALTER NOTIFICATION INTEGRATION](sql/alter-notification-integration.md)
* [CREATE NOTIFICATION INTEGRATION](sql/create-notification-integration.md)
* [DESCRIBE NOTIFICATION INTEGRATION](sql/desc-notification-integration.md)
* [DROP INTEGRATION](sql/drop-integration.md)
* [SHOW NOTIFICATION INTEGRATIONS](sql/show-notification-integrations.md)

### Security integrations

* [ALTER SECURITY INTEGRATION](sql/alter-security-integration.md)
* [CREATE SECURITY INTEGRATION](sql/create-security-integration.md)
* [DESCRIBE INTEGRATION](sql/desc-integration.md)
* [DROP INTEGRATION](sql/drop-integration.md)
* [SHOW INTEGRATIONS](sql/show-integrations.md)
* [SHOW DELEGATED AUTHORIZATIONS](sql/show-delegated-authorizations.md)

### Storage integrations

* [ALTER STORAGE INTEGRATION](sql/alter-storage-integration.md)
* [CREATE STORAGE INTEGRATION](sql/create-storage-integration.md)
* [DESCRIBE INTEGRATION](sql/desc-integration.md)
* [DROP INTEGRATION](sql/drop-integration.md)
* [SHOW INTEGRATIONS](sql/show-integrations.md)
