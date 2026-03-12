# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-listing.md

# DROP LISTING

Removes the specified [listing](../../collaboration/collaboration-listings-about.md) from the system and immediately revokes access for all consumers.

> **Important:**
>
> Before dropping a listing, ensure that:
>
> * The listing is in state DRAFT or UNPUBLISH. For more information about changing listing states, see [ALTER LISTING](alter-listing.md).
> * Previously published listings are not mounted by any consumers.

See also:

> [CREATE LISTING](create-listing.md), [ALTER LISTING](alter-listing.md), [DESCRIBE LISTING](desc-listing.md), [SHOW LISTINGS](show-listings.md), [SHOW VERSIONS IN LISTING](show-versions-in-listing.md), [Listing manifest reference](../../progaccess/listing-manifest-reference.md)

## Syntax

```sqlsyntax
DROP LISTING <name>
```

## Parameters

`name`
:   The identifier of the listing to drop. If the identifier contains spaces, special characters, or mixed-case characters, the
    entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* Only the listing owner, the role with the OWNERSHIP privilege on the listing, has the privileges to drop a listing.
  Executing this command with any other role returns an error.
* Dropped listings cannot be recovered; they must be recreated.
* Dropping a listing automatically invokes the retirement process for all public and monetized listings.
  Additionally, for other listing types the listing is dropped immediately, and all consumer access automatically revoked.
* Provider account Listing Auto-Fulfillment (LAF) replication groups don’t get dropped when you drop a private listing. To resolve this issue after you drop a private listing, revoke the existing grants on the replication group and then drop the replication group. For example:

  ```sqlexample
  GRANT OWNERSHIP ON REPLICATION GROUP myrg TO ROLE accountadmin
  REVOKE CURRENT GRANTS;
  DROP REPLICATION GROUP myrg;
  ```

## Examples

> ```sqlexample
> DROP LISTING IF EXISTS MYLISTING
> ```
>
> ```output
> +----------------------------------+
> | status                           |
> |----------------------------------|
> | MYLISTING successfully dropped. |
> +----------------------------------+
> ```
