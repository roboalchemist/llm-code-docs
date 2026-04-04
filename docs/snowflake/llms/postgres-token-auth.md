# Source: https://docs.snowflake.com/en/user-guide/snowflake-postgres/postgres-token-auth.md

# Snowflake Token Authentication for Snowflake Postgres

Snowflake allows users to generate short-lived access tokens to use for logging into Snowflake Postgres instances. At the
instance level this is known as Snowflake authorization and is done with these three steps which are expanded upon below:

1. Enable Snowflake authorization for the Snowflake Postgres instance.
2. On the Snowflake Postgres instance, create mappings between Postgres users and Snowflake users.
3. Mapped Snowflake users then generate short-lived access tokens to use when logging into the Snowflake Postgres instance.

> **Note:**
>
> Snowflake Token Authentication for Snowflake Postgres is a separate feature from the
> [Snowflake OAuth](../oauth-snowflake-overview.md) and [Programmatic access tokens](../programmatic-access-tokens.md)
> Snowflake authentication methods.

## Enabling and disabling Snowflake Authorization on Snowflake Postgres instances

SnowsightSQL

To enable Snowflake authorization at instance creation time, enable the Snowflake auth option in the Snowflake Postgres
New instance dialogue when [Creating a new instance](postgres-create-instance.md).

To enable or disable Snowflake authorization for an existing instance:

1. In the navigation menu, select Postgres.
2. Select your instance.
3. In the Manage menu at the top right, select the Enable Snowflake auth or Disable Snowflake auth
   option from the instance’s Manage dropdown menu on its details page in the dashboard.
4. Select Enable or Disable on the presented confirmation dialogue.

Enabling and disabling Snowflake authorization for an instance is done with its AUTHENTICATION_AUTHORITY attribute.

To enable Snowflake authorization at instance creation time:

```sqlexample
CREATE POSTGRES INSTANCE {instance_name}
 SET AUTHENTICATION_AUTHORITY = POSTGRES_OR_SNOWFLAKE
 <other_options>;
```

To enable Snowflake authorization for existing instances:

```sqlexample
ALTER POSTGRES INSTANCE {instance_name}
 SET AUTHENTICATION_AUTHORITY = POSTGRES_OR_SNOWFLAKE
 <other_options>;
```

To disable Snowflake authorization for existing instances:

```sqlexample
ALTER POSTGRES INSTANCE {instance_name}
 SET AUTHENTICATION_AUTHORITY = POSTGRES
 <other_options>;
```

> **Important:**
>
> Disabling Snowflake authorization on an instance only prevents Snowflake users from creating new short-lived access tokens.
> Users with valid tokens can still establish new connections until the tokens expire, and existing connections will persist.
>
> After disabling Snowflake Authorization, Postgres users mapped to Snowflake users will not be able to use standard Postgres
> authentication until their mappings have been removed as described in Creating mappings between Postgres users and Snowflake users below.

## Creating mappings between Postgres users and Snowflake users

To create a mapping between a Postgres user and a Snowflake user log into your Postgres instance with the `snowflake_admin` user and run:

```postgresql
ALTER USER {postgres_user} SET snowflake_user = '{snowflake_user}';
```

The supplied `{postgres_user}` and `{snowflake_user}` names in the above statement will read as case-insensitive. If case-sensitivity
is required place the names in double-quotes. For example, to map a Postgres user named Casey to a Snowflake user of the same name:

```postgresql
ALTER USER "Casey" SET snowflake_user = '"Casey"';
```

To remove a mapping between a Postgres user and a Snowflake user log into your Postgres instance with the `snowflake_admin` user and run:

```postgres
ALTER USER {postgres_user} RESET snowflake_user;
```

To view which existing mappings between Postgres users and Snowflake users log into your Postgres instance with the `snowflake_admin` user
and query the SNOWFLAKE_AUTH.IDENTITY_MAPPING Postgres view view.

> **Note:**
>
> Postgres users with Snowflake user mappings can only log in with generated short-lived access tokens. They cannot connect with a Postgres
> password, and their Postgres passwords cannot be changed. To re-enable standard password login functionality for a given Postgres user, you
> must remove its mapping to a Snowflake user.

## Creating short-lived access tokens for mapped Snowflake users

Snowflake Postgres instance owners and Snowflake users with the USAGE privilege granted on a given instance can create short-lived access tokens
passwords themselves on a per-instance basis for instances that have Snowflake authorization enabled per the instructions above in
Enabling and disabling Snowflake Authorization on Snowflake Postgres instances.

SnowsightSQL

1. In the navigation menu, select Postgres.
2. Select your instance.
3. In the Manage menu at the top right, select Regenerate token.
4. In the presented Regenerate token dialogue enter the name of a Postgres user that has been mapped to your Snowflake user and select
   Acknowledge & continue.
5. Copy the presented short-lived access token or Postgres URI to use for establishing new connections to the Snowflake Postgres instance within the next
   15 minutes.

Use the [GENERATE_POSTGRES_ACCESS_TOKEN_FOR_USER](../../sql-reference/functions/generate_postgres_access_token_for_user.md) function.

## SNOWFLAKE_AUTH.IDENTITY_MAPPING Postgres view

This Snowflake Postgres view can be used to query a list of all mappings between Postgres users and Snowflake users on the instance.

> **Note:**
>
> This view is available to query only inside Snowflake Postgres instances and can not be queried directly from Snowflake.

### Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| postgres_role | name | The name of the mapped Postgres user |
| snowflake_identity | text | The snowflake user identity in USER:# form, where # is the mapped Snowflake user’s `user_id` value seen in the [USERS view](../../sql-reference/account-usage/users.md) view. |
