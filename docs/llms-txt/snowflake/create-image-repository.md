# Source: https://docs.snowflake.com/en/sql-reference/sql/create-image-repository.md

# CREATE IMAGE REPOSITORY

Creates a new [image repository](../../developer-guide/snowpark-container-services/working-with-registry-repository.md) in the
current schema.

See also:
:   [DROP IMAGE REPOSITORY](drop-image-repository.md) , [SHOW IMAGE REPOSITORIES](show-image-repositories.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] IMAGE REPOSITORY [ IF NOT EXISTS ] <name>
  [ ENCRYPTION = ( TYPE = 'SNOWFLAKE_FULL' | TYPE = 'SNOWFLAKE_SSE' ) ]
```

## Required parameters

`name`
:   Specifies the identifier (that is, the name) for the image repository; it must be unique for the schema in which the repository is created.

    Quoted names for special characters or case-sensitive names are not supported. The same constraint also applies to database and
    schema names where you create an image repository. That is, database and schema names without quotes are valid when creating an
    image repository.

## Optional parameters

`ENCRYPTION = ( TYPE = 'SNOWFLAKE_FULL' | TYPE = 'SNOWFLAKE_SSE' )`
:   Specifies the type of encryption to use for binaries stored in the image repository. You cannot change the encryption type after you create the image repository.

    `TYPE = ...`
    :   Specifies the encryption type to use.

    > **Important:**
    >
    > If you require Tri-Secret Secure for security compliance, use the `SNOWFLAKE_FULL` encryption type for internal stages.
    > `SNOWFLAKE_SSE` does not support Tri-Secret Secure.

    Possible values are the following:

    * `SNOWFLAKE_FULL`: On-host (image registry host) and server-side encryption. Data is first encrypted by Snowflake’s image registry service before sending the data to cloud service provider storage (for example, Amazon S3) where your Snowflake account is hosted.

      Snowflake uses AES-GCM with a 128-bit encryption key by default.
      You can configure a 256-bit key by setting the [CLIENT_ENCRYPTION_KEY_SIZE](../parameters.md) parameter. All binaries are also automatically encrypted using AES-256 strong encryption on the server side.

      > **Note:**
      >
      > With SNOWFLAKE_FULL encryption, Snowflake might throttle requests against the public image repository API. This throttling is triggered only when Snowflake detects an unusually large number of parallel requests against the repository. Note that, the service creation will never be impacted.
    * `SNOWFLAKE_SSE`: Server-side encryption only. The binaries are encrypted by the cloud service provider (for example, Amazon S3) where your Snowflake account is hosted when they arrive on the image repository storage area.

    Default: `SNOWFLAKE_FULL`

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE IMAGE REPOSITORY | Schema |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

Create an image repository:

```sqlexample
CREATE OR REPLACE IMAGE REPOSITORY tutorial_repository;
```

Create an image repository with SNOWFLAKE_FULL encryption:

```sqlexample
CREATE OR REPLACE IMAGE REPOSITORY tutorial_repository
ENCRYPTION = (type = 'SNOWFLAKE_SSE');
```
