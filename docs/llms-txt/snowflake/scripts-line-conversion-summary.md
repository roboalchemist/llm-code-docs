# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/general/getting-started/running-snowconvert/review-results/reports/assessment-report/scripts-line-conversion-summary.md

# SnowConvert AI - Scripts Line Conversion Summary

> **Note:**
>
> This section applies only to Teradata reports.

These fields are counted for the following Script files:

* BTEQ: .bteq, .btq
* FastLoad: .fload, .fl
* MultiLoad: .mload, .mld, ml
* TPump: .tpump, .tp
* TPT: .tpt

## Lines of Code

Represents the number of lines of code found in the Script files. This counting includes comments but does not include empty lines or lines with only whitespaces unless they are inside block comments or strings. Lines of code that were not recognized are counted as well.

### Samples

> **Note:**
>
> Samples of the SQL Conversion Summary [Lines of Code](sql-conversion-summary.md) also apply to Scripts Lines of Code.

```none
.RUN FILE 'myscript.txt'

.SET FORMAT ON;
```

**Expected Lines of Code:** 2

```none
DATABASE tduser;
```

**Expected lines of code:** 1

```none
.LAYOUT Something;

INSERT INTO myTable (
    myValue
)
VALUES (
    123
);
```

**Expected lines of code:** 7

```none
.logtable TheDatabase.tpumplog;
```

**Expected lines of code:** 1

```none
DEFINE JOB my_job
DESCRIPTION 'A description
goes here'
(
     DEFINE SCHEMA my_schema
     DESCRIPTION 'The schema' (value VARCHAR (10));

   STEP setup_tables
   (
      APPLY ('DELETE FROM &some.name;')
      TO OPERATOR (DDL_OPERATOR () );
   );
);
```

**Expected lines of code:** 12

#### CSV Associated Field Names

* ScriptTotalLoc

## LOC Conversion Percentage

This is the percentage of fully converted lines divided by the total lines of code. Unrecognized Lines of code count as not converted. Comments count as converted.

### Formula

```none
scripts_converted_lines_of_code / scripts_total_lines_of_code
```

#### Samples

> **Note:**
>
> Samples of the SQL Conversion Summary [LOC Conversion Percentage](sql-conversion-summary.md) also apply to Scripts Lines of Code.

#### CSV Associated Field Names

* ScriptTotalLoc

## Unrecognized Lines of Code

This is the number of lines of code that had an element that was not recognized.

### Samples

> **Note:**
>
> Samples of the SQL Conversion Summary [Unrecognized Lines of Code](sql-conversion-summary.md) also apply to Scripts Unrecognized Lines of Code.

#### CSV Associated Field Names

* ScriptsUnrecognizedElementsLOC
