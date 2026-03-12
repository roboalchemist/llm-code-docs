# Source: https://docs.snowflake.com/en/sql-reference/functions/available_listings.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# AVAILABLE_LISTINGS

Returns all listings that are available for the consumer to discover and access.

## Syntax

```sqlsyntax
AVAILABLE_LISTINGS(
      [ IS_IMPORTED => { TRUE | FALSE | NULL } ]
      [ , IS_ORGANIZATION => { TRUE | FALSE | NULL } ]
      [ , IS_SHARED_WITH_ME => { TRUE | FALSE | NULL } ] )
```

## Arguments

You can optionally specify the following arguments to filter listings in this view.

> **Note:**
>
> Only one of the arguments can be `TRUE` at a time.

`IS_IMPORTED => { TRUE | FALSE | NULL }`
:   Set to `TRUE` to return only imported listings; set to `FALSE` or `NULL` to return all listings.

    Default: `NULL`.

`IS_ORGANIZATION => { TRUE | FALSE | NULL }`
:   Set to `TRUE` to return only organization listings; set to `FALSE` or `NULL` to return all listings.

    Default: `NULL`.

`IS_SHARED_WITH_ME => { TRUE | FALSE | NULL }`
:   Set to `TRUE` to return only listings that have been shared privately with the current account; set to `FALSE` or `NULL` to return all listings.

    Default: `NULL`.

## Output

The function returns the following columns:

| Column | Data type | Description |
| --- | --- | --- |
| GLOBAL_NAME | VARCHAR | The global name of the listing. |
| CREATED_ON | TIMESTAMP_LTZ | The timestamp when the listing was created. |
| TITLE | VARCHAR | The title of the listing. |
| SUBTITLE | VARCHAR | The subtitle of the listing. |
| DESCRIPTION | VARCHAR | The description of the listing. |
| IS_MONETIZED | BOOLEAN | Indicates whether the listing is monetized. |
| IS_BY_REQUEST | BOOLEAN | Indicates whether the listing is by request (personalized listing). |
| IS_LIMITED_TRIAL | BOOLEAN | Indicates whether the listing is limited trial. |
| IS_READY_FOR_IMPORT | BOOLEAN | Indicates whether the listing is ready for import. |
| IS_IMPORTED | BOOLEAN | Indicates whether the listing has been imported. |
| IS_APPLICATION | BOOLEAN | Indicates whether the listing is associated with an application. |
| IS_PRIVATE | BOOLEAN | Indicates whether the listing is private. |
| CATEGORIES | VARCHAR | Categories associated with the listing. |
| DATA_ATTRIBUTES | VARCHAR | Data attributes associated with the listing. |
| TERMS | VARCHAR | Terms of service for the listing. |
| RESOURCES | VARCHAR | Resources associated with the listing. |
| DISTRIBUTION | VARCHAR | The distribution of the listing. Possible values are `EXTERNAL` and `ORGANIZATION`. |
| UNIFORM_LISTING_LOCATOR | VARCHAR | The uniform listing locator (ULL) of the listing. |
| ORGANIZATION_PROFILE_NAME | VARCHAR | The organization profile attached to the listing, if any. |
| IS_DISCOVERY_ONLY | BOOLEAN | Indicates whether the listing is discovery only. |
| SUPPORT_CONTACT | VARCHAR | The support contact information associated with the listing. |
| REQUEST_APPROVAL_TYPE | VARCHAR | The request approval type of the listing. Incidates whether the consumer listing requests will be approved within or outside of Snowflake. |
| IS_CORTEX_KNOWLEDGE_EXTENSION | BOOLEAN | Indicates whether this listing has Cortex Search services attached. |
| PROVIDER_COMPANY_NAME | VARCHAR | The company name of the listing provider. |
| RESHARING | VARCHAR | Resharing configuration of the listing. |

## Examples

Retrieve all available listings in the current account:

```sqlexample
SELECT * FROM TABLE(<any_database>.INFORMATION_SCHEMA.AVAILABLE_LISTINGS());
```

Retrieve all available listings that have been imported by the current account:

```sqlexample
SELECT * FROM TABLE(<any_database>.INFORMATION_SCHEMA.AVAILABLE_LISTINGS(IS_IMPORTED => TRUE));
```

Retrieve all available organization listings in the current account:

```sqlexample
SELECT * FROM TABLE(<any_database>.INFORMATION_SCHEMA.AVAILABLE_LISTINGS(IS_ORGANIZATION => TRUE));
```

Retrieve all available listings that have been shared privately with the current account:

```sqlexample
SELECT * FROM TABLE(<any_database>.INFORMATION_SCHEMA.AVAILABLE_LISTINGS(IS_SHARED_WITH_ME => TRUE));
```
