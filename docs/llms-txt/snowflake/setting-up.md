# Source: https://docs.snowflake.com/en/user-guide/snowflake-cortex/document-ai/setting-up.md

# Setting up Document AI

This topic describes setting up Document AI, including granting the necessary roles and privileges.

To work with Document AI:

* Prepare a warehouse, database, and schema to be used with Document AI.

  > Snowflake recommends creating a separate warehouse for Document AI to help you track costs; for example, the `doc_ai_wh` X-Small warehouse.
  > For more information, see [Determining optimal warehouse size for Document AI](cost-governance.md).
* Grant the required roles and privileges.

  > For more information, see Document AI access control.
  > For examples of granting roles and privileges, see Grant the required roles and privileges to Document AI users.
* Upload the documents for extraction to either an internal or external stage.

  > To create an [internal stage](../../data-load-local-file-system-create-stage.md), run the [CREATE STAGE](../../../sql-reference/sql/create-stage.md) command as shown in the following example:
  >
  > ```sqlsyntax
  > CREATE STAGE doc_ai_stage
  >   DIRECTORY = (ENABLE = TRUE)
  >   ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE');
  > ```
  >
  > To create an [external stage](../../data-load-overview.md),
  > run the [CREATE STAGE](../../../sql-reference/sql/create-stage.md) command as shown in [External stages](../../../sql-reference/sql/create-stage.md).

## Document AI access control

To provide a user full access to Document AI, you must do all of the following:

* Grant the SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR database role to an account role, and then grant the account role to users.
* Grant the privileges to prepare a Document AI model build.
* Grant the privileges to create processing pipelines and extract information using Document AI.

To learn more about the Snowflake privilege model, see [Overview of Access Control](../../security-access-control-overview.md) and
[Access control privileges](../../security-access-control-privileges.md).

The SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR database role enables creating Document AI model builds, working on
Document AI models, and using SQL to extract information and work on document processing pipelines.

### Additional notes

* Using the ACCOUNTADMIN role is not enough to have access to Document AI. You must grant the SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR
  database role and the required privileges to your account role.

  For example, you can create `doc_ai_role` account role and grant the SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR database role to the `doc_ai_role`
  role, or you can use an existing account role.
* You must grant the required privileges directly to your account role.

### Privileges to prepare a Document AI model build

To create a Document AI build, upload the documents, and test and evaluate the model, you must use a role that has the
following privileges:

| Privilege | Object |
| --- | --- |
| USAGE | Database that you plan to use with Document AI |
| USAGE | Warehouse that you plan to use with Document AI |
| OPERATE | Warehouse that you plan to use with Document AI |
| CREATE SNOWFLAKE.ML.DOCUMENT_INTELLIGENCE | Schema that you plan to use with Document AI |
| CREATE MODEL | Schema that you plan to use with Document AI |
| USAGE | Schema that you plan to use with Document AI |

### Privileges to create processing pipelines and extract information using Document AI

To create processing pipelines and extract information using Document AI, you must use a role that has all the
privileges required to prepare a Document AI build, listed above, and also the following privileges:

| Privilege | Object |
| --- | --- |
| CREATE STAGE | Schema that you plan to use with Document AI |
| CREATE STREAM | Schema that you plan to use with Document AI |
| CREATE TABLE | Schema that you plan to use with Document AI |
| CREATE TASK | Schema that you plan to use with Document AI |
| CREATE VIEW | Schema that you plan to use with Document AI |
| EXECUTE TASK | Account that you plan to use to create processing pipelines using tasks |

## Grant the required roles and privileges to Document AI users

The following example describes granting all the roles and privileges required to work with Document AI.

> **Note:**
>
> Before you grant the required roles and privileges, confirm that a warehouse, database, and schema for Document AI are prepared.

To create the `doc_ai_role` role and grant the SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR database role to this role, run the following commands:

```sqlexample
USE ROLE ACCOUNTADMIN;

CREATE ROLE doc_ai_role;
GRANT DATABASE ROLE SNOWFLAKE.DOCUMENT_INTELLIGENCE_CREATOR TO ROLE doc_ai_role;
```

To create a database, a schema, and an X-Small warehouse to use with Document AI, run the following commands:

```sqlexample
CREATE DATABASE doc_ai_db;
CREATE SCHEMA doc_ai_db.doc_ai_schema;
CREATE WAREHOUSE doc_ai_wh;
```

To grant warehouse usage and operating privileges to the `doc_ai_role` role, run the following commands:

```sqlexample
GRANT USAGE, OPERATE ON WAREHOUSE doc_ai_wh TO ROLE doc_ai_role;
```

To ensure that the `doc_ai_role` role can use the database and the schema, run the following commands:

```sqlexample
GRANT USAGE ON DATABASE doc_ai_db TO ROLE doc_ai_role;
GRANT USAGE ON SCHEMA doc_ai_db.doc_ai_schema TO ROLE doc_ai_role;
```

To ensure that the `doc_ai_role` role can create a stage to store the documents for extraction, run the following commands:

```sqlexample
GRANT CREATE STAGE ON SCHEMA doc_ai_db.doc_ai_schema TO ROLE doc_ai_role;
```

To ensure that the `doc_ai_role` role can create model builds (instances of the DOCUMENT_INTELLIGENCE class), run the following commands:

```sqlexample
GRANT CREATE SNOWFLAKE.ML.DOCUMENT_INTELLIGENCE ON SCHEMA doc_ai_db.doc_ai_schema TO ROLE doc_ai_role;
GRANT CREATE MODEL ON SCHEMA doc_ai_db.doc_ai_schema TO ROLE doc_ai_role;
```

To ensure that the `doc_ai_role` role can create [processing pipelines](extract-information.md), run the following commands:

```sqlexample
GRANT CREATE STREAM, CREATE TABLE, CREATE TASK, CREATE VIEW ON SCHEMA doc_ai_db.doc_ai_schema TO ROLE doc_ai_role;
GRANT EXECUTE TASK ON ACCOUNT TO ROLE doc_ai_role;
```

To grant the `doc_ai_role` role to the `doc_ai_user` user, run the following command:

```sqlexample
GRANT ROLE doc_ai_role TO USER doc_ai_user;
```
