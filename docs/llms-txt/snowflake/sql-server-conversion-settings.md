# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/running-snowconvert/conversion/sql-server-conversion-settings.md

# SnowConvert AI - SQL Server Conversion Settings

This topic applies to the following sources:

* SQL Server
* Azure Synapse Analytics

Before conversion, you use SnowConvert AI to extract database objects from your source system to prepare them for
the conversion process. For more information, see [SnowConvert AI: Data Extraction](../../../user-guide/extraction.md).

## General conversion settings

1. **Comment objects with missing dependencies:** Flag to indicate whether to comment on nodes that have missing dependencies.
2. **Set encoding of the input files:** Check [General Conversion Settings](general-conversion-settings.md) for more details.

> **Note:**
>
> To review the Settings that apply to all supported languages, go to the following [article](general-conversion-settings.md).

## DB objects names settings

1. **Schema:** The string value specifies the custom schema name to apply. If not specified, the original database name will be used. Example: DB1.**myCustomSchema**.Table1.
2. **Database:** The string value specifies the custom database name to apply. Example: **MyCustomDB**.PUBLIC.Table1.
3. **Default:** None of the above settings will be used in the objects names.

## Prepare Code Settings

### **Description**

**Prepare my code:** Flag to indicate whether the input code should be processed before parsing and transformation. This can be useful to improve the parsing process. By default, it’s set to FALSE.

Splits the input code top-level objects into multiple files. The containing folders would be organized as follows:

Copy

```none
└───A new folder named ''[input_folder_name]_Processed''
    └───Top-level object type
        └───Schema name
```

### **Example**

#### **Input**

```none
├───in
│       script_name.sql
```

#### **Output**

Assume that the name of the files is the name of the top-level objects in the input files.

```none
├───in_Processed
    ├───procedure
    │   └───dbo
    │           A_PROCEDURE.sql
    │           ANOTHER_PROCEDURE.sql
    │           YET_ANOTHER_PROCEDURE.sql
    │
    └───table
        └───dbo
                MY_TABLE.sql
                ADDITIONAL_TABLE.sql
                THIRD_TABLE.sql
```

### Requirements

We highly recommend using [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16) to obtain the script.

## Stored Procedures Target Languages Settings

On this page, you can choose whether stored procedures are migrated to JavaScript embedded in Snow SQL, or to Snowflake Scripting. The default option is Snowflake Scripting.

**Reset Settings:** The reset settings option appears on every page. If you’ve made changes, you can reset SnowConvert AI to its original default settings.

## **Next steps for SQL Server databases**

For SQL Server databases, you can use SnowConvert AI to complete the following tasks after conversion:

* [Deployment](../../../user-guide/deployment.md)
* [Data migration](../../../user-guide/data-migration.md)
* [Data validation](../../../user-guide/data-validation.md)
