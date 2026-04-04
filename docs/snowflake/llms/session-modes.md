# Source: https://docs.snowflake.com/en/migrations/snowconvert-docs/translation-references/teradata/session-modes.md

# SnowConvert AI - Teradata - Session Modes in Teradata

## Teradata session modes description

The Teradata database has different modes for running queries: ANSI Mode (rules based on the ANSI SQL: 2011 specifications) and TERA mode (rules defined by Teradata). Please review the following [Teradata documentation](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/SQL-Request-and-Transaction-Processing/Transaction-Processing/Transaction-Semantics-Differences-in-ANSI-and-Teradata-Session-Modes) for more information.

### Teradata mode for strings informative table

For strings, the Teradata Mode works differently. As it is explained in the following table based on the [Teradata documentation](https://docs.teradata.com/r/Enterprise_IntelliFlex_VMware/SQL-Request-and-Transaction-Processing/Transaction-Processing/Comparison-of-Transactions-in-ANSI-and-Teradata-Session-Modes):

| Feature | ANSI mode | Teradata mode |
| --- | --- | --- |
| Default attribute for character comparisons | CASESPECIFIC | NOT CASESPECIFIC |
| Default TRIM behavior | TRIM(BOTH FROM) | TRIM(BOTH FROM) |

#### Translation specification summary

| Mode | Column constraint values | Teradata behavior | SC expected behavior |
| --- | --- | --- | --- |
| ANSI Mode | CASESPECIFIC | CASESPECIFIC | No constraint added. |
|  | NOT CASESPECIFIC | CASESPECIFIC | Add `COLLATE 'en-cs'` in column definition. |
| Teradata Mode | CASESPECIFIC | CASESPECIFIC | In most cases, do not add COLLATE, and convert its usages of string comparison to `RTRIM( expression )` |
|  | NOT CASESPECIFIC | NOT CASESPECIFIC | In most cases, do not add COLLATE, and convert its usages of string comparison to `RTRIM(UPPER( expression ))` |

### Available translation specification options

* TERA Mode For Strings Comparison - NO COLLATE
* TERA Mode For Strings Comparison - COLLATE
* ANSI Mode For Strings Comparison - NO COLLATE
* ANSI Mode For Strings Comparison - COLLATE

## ANSI Mode For Strings Comparison - COLLATE

This section defines the translation specification for a string in ANSI mode with the use of COLLATE.

### Description

#### ANSI mode for string comparison and COLLATE usage

The ANSI mode string comparison will apply the COLLATE constraint to the columns or statements as required. The default case specification trim behavior may be taken into account.

Notice that in Teradata, the default case specification is ‘`CASESPECIFIC`’, the same default as in Snowflake ‘`case-sensitive'`. Thus, these cases will not be translated with a `COLLATE` because it will be redundant.

### Sample Source Patterns

#### Setup data

##### Teradata

```sql
 CREATE TABLE employees (
    employee_id INTEGER NOT NULL,
    first_name VARCHAR(50) NOT CASESPECIFIC,
    last_name VARCHAR(50) CASESPECIFIC,
    department VARCHAR(50)
);

INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (1, 'George', 'Snow', 'Sales');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (2, 'John', 'SNOW', 'Engineering');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (3, 'WIlle', 'SNOW', 'Human resources   ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (4, 'Marco', 'SnoW   ', 'EngineerinG');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (5, 'Mary', '   ', 'SaleS  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (6, 'GEORGE', '  ', 'sales  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (7, 'GEORGE   ', '  ', 'salEs  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (8, '    GeorgE   ', '  ', 'SalEs  ');
INSERT INTO employees (employee_id, first_name, last_name, department) VALUES (9, 'JOHN', '   SnoW', 'IT');
INSERT INTO employees (employee_id, first_name, last_name, department) VALUES (10, 'JOHN    ', 'snow', 'Finance   ');

CREATE TABLE departments (
    department_id INTEGER NOT NULL,
    department_name VARCHAR(50) NOT CASESPECIFIC,
    location VARCHAR(100) CASESPECIFIC,
    PRIMARY KEY (department_id)
);

INSERT INTO departments (department_id, department_name, location) VALUES (101, 'Information Technology', 'New York');
INSERT INTO departments (department_id, department_name, location) VALUES (102, 'Human Resources', 'Chicago');
INSERT INTO departments (department_id, department_name, location) VALUES (103, 'Sales', 'San Francisco');
INSERT INTO departments (department_id, department_name, location) VALUES (104, 'Finance', 'Boston');
```

##### Snowflake

```sql
 CREATE OR REPLACE TABLE employees (
    employee_id INTEGER NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/02/2025",  "domain": "no-domain-provided" }}'
;

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (1, 'George', 'Snow', 'Sales');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (2, 'John', 'SNOW', 'Engineering');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (3, 'WIlle', 'SNOW', 'Human resources   ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (4, 'Marco', 'SnoW   ', 'EngineerinG');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (5, 'Mary', '   ', 'SaleS  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (6, 'GEORGE', '  ', 'sales  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (7, 'GEORGE   ', '  ', 'salEs  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (8, '    GeorgE   ', '  ', 'SalEs  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (9, 'JOHN', '   SnoW', 'IT');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (10, 'JOHN    ', 'snow', 'Finance   ');

CREATE OR REPLACE TABLE departments (
    department_id INTEGER NOT NULL,
    department_name VARCHAR(50),
    location VARCHAR(100),
       PRIMARY KEY (department_id)
   )
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "07/02/2025",  "domain": "no-domain-provided" }}'
;

INSERT INTO departments (department_id, department_name, location)
VALUES (101, 'Information Technology', 'New York');

INSERT INTO departments (department_id, department_name, location)
VALUES (102, 'Human Resources', 'Chicago');

INSERT INTO departments (department_id, department_name, location)
VALUES (103, 'Sales', 'San Francisco');

INSERT INTO departments (department_id, department_name, location)
VALUES (104, 'Finance', 'Boston');
```

#### Comparison operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name = 'GEorge ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Snowflake

##### Query

```sql
 SELECT
    *
FROM
    employees
WHERE
    COLLATE(first_name, 'en-cs-rtrim') = RTRIM('George');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name = 'SNOW ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

##### Snowflake

##### Query

```sql
SELECT
 *
FROM
 employees
WHERE
 RTRIM(last_name) = RTRIM('SNOW ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

##### Case 3: CAST NOT CASESPECIFIC column to CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT * FROM employees WHERE first_name = 'George   ' (CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Snowflake

> **Note:**
>
> COLLATE ‘en-cs’ is required for functional equivalence.

##### Query

```sql
 SELECT
    *
FROM
    employees
WHERE
    COLLATE(first_name, 'en-cs-rtrim') = 'George   ' /*** SSC-FDM-TD0032 - CASESPECIFIC CLAUSE WAS REMOVED ***/;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Case 4: CAST CASESPECIFIC column to NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT * FROM employees WHERE first_name = 'GEorge   ' (NOT CASESPECIFIC) ;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |
| 7 | GEORGE |  | salEs |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(first_name) = RTRIM('GEorge   ' /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |
| 7 | GEORGE |  | salEs |

##### Case 5: CAST NOT CASESPECIFIC column to NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT * FROM employees WHERE first_name (NOT CASESPECIFIC)  = 'George    ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Snowflake

> **Note:**
>
> It requires COLLATE.

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   COLLATE(first_name /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/, 'en-cs-rtrim') = 'George    ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

#### LIKE operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name LIKE 'George';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Snowflake

##### Query

```sql
 SELECT *
FROM employees
WHERE COLLATE(first_name, 'en-cs-rtrim') LIKE 'George';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name LIKE 'Snow';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 2 | John | SNOW | Engineering |
| 3 | WIlle | SNOW | Human resources |

##### Snowflake

##### Query

```sql
 SELECT *
FROM employees
WHERE RTRIM(last_name) LIKE RTRIM('Snow');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 2 | John | SNOW | Engineering |
| 3 | WIlle | SNOW | Human resources |

##### Case 3: CAST NOT CASESPECIFIC column to CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name LIKE 'Mary' (CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 5 | Mary |  | SaleS |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   COLLATE(first_name, 'en-cs-rtrim') LIKE 'Mary' /*** SSC-FDM-TD0032 - CASESPECIFIC CLAUSE WAS REMOVED ***/;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 5 | Mary |  | SaleS |

##### Case 4: CAST CASESPECIFIC column to NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name LIKE 'SNO%' (NOT CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 2 | John | SNOW | Engineering |
| 3 | WIlle | SNOW | Human resources |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(last_name) LIKE RTRIM('SNO%' /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 2 | John | SNOW | Engineering |
| 3 | WIlle | SNOW | Human resources |

#### IN Operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name IN ('George   ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Snowflake

> **Note:**
>
> This case requires `COLLATE(`*`column_name`*`, 'en-cs-rtrim')`

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(first_name) IN (COLLATE('George   ', 'en-cs-rtrim'));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

> **Note:**
>
> For this case, the column does not have a column constraint, but the default constraint in Teradata ANSI mode is `CASESPECIFIC`.

##### Query

```sql
 SELECT *
FROM employees
WHERE department IN ('EngineerinG    ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 4 | Marco | SnoW | EngineerinG |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(department) IN (RTRIM('EngineerinG    '));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 4 | Marco | SnoW | EngineerinG |

#### ORDER BY clause

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT first_name
FROM employees
ORDER BY first_name;
```

##### Output

| first_name |
| --- |
| GeorgE |
| GEORGE |
| GEORGE |
| **George** |
| John |
| JOHN |
| JOHN |
| Marco |
| Mary |
| WIlle |

##### Snowflake

> **Warning:**
>
> Please review FDM. ***Pending to add.***

##### Query

```sql
 SELECT
   first_name
FROM
   employees
ORDER BY first_name;
```

##### Output

| first_name |
| --- |
| GeorgE |
| **George** |
| GEORGE |
| GEORGE |
| John |
| JOHN |
| JOHN |
| Marco |
| Mary |
| WIlle |

##### Case 2: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT last_name
FROM employees
ORDER BY last_name;
```

##### Output

| department |
| --- |
| EngineerinG |
| Engineering |
| Finance |
| Human resources |
| IT |
| SalEs |
| SaleS |
| Sales |
| salEs |
| sales |

##### Snowflake

##### Query

```sql
 SELECT
   last_name
FROM
   employees
ORDER BY last_name;
```

##### Output

| department |
| --- |
| EngineerinG |
| Engineering |
| Finance |
| Human resources |
| IT |
| SalEs |
| SaleS |
| Sales |
| salEs |
| sales |

#### GROUP BY clause

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT first_name
FROM employees
GROUP BY first_name;
```

##### Output

| first_name |
| --- |
| Mary |
| GeorgE |
| WIlle |
| **JOHN** |
| Marco |
| GEORGE |

##### Snowflake

> **Warning:**
>
> **The case or order may differ in output.**

> **Note:**
>
> `RTRIM` is required in selected columns.

##### Query

```sql
   SELECT
   first_name
  FROM
   employees
  GROUP BY first_name;
```

##### Output

| first_name |
| --- |
| **John** |
| Marco |
| **George** |
| GeorgE |
| WIlle |
| Mary |

##### Case 2: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT last_name
FROM employees
GROUP BY last_name;
```

##### Output

| last_name |
| --- |
| SnoW |
|  |
| SNOW |
| SnoW |
| Snow |
| snow |

##### Snowflake

> **Note:**
>
> *The order may differ.*

##### Query

```sql
 SELECT
   last_name
  FROM
   employees
  GROUP BY last_name;
```

##### Output

| first_name |
| --- |
| Snow |
| SNOW |
| SnoW |
|  |
| SnoW |
| snow |

#### HAVING clause

The HAVING clause will use the patterns in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Sample: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT first_name
FROM employees
GROUP BY first_name
HAVING first_name = 'Mary';
```

##### Output

```none
Mary
```

##### Snowflake

##### Query

```sql
 SELECT
  first_name
FROM
  employees
GROUP BY first_name
HAVING
   COLLATE(first_name, 'en-cs-rtrim') = 'Mary';
```

##### Output

```none
Mary
```

#### CASE WHEN statement

The `CASE WHEN` statement will use the patterns described in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Teradata

##### Query

```sql
 SELECT first_name,
      last_name,
      CASE
          WHEN department = 'EngineerinG' THEN 'Information Technology'
          WHEN first_name = '    GeorgE   ' THEN 'GLOBAL SALES'
          ELSE 'Other'
      END AS department_full_name
FROM employees
WHERE last_name = '';
```

##### Output

| first_name | last_name | department_full_name |
| --- | --- | --- |
| GEORGE |  | Other |
| Mary |  | Other |
| GeorgE |  | GLOBAL SALES |
| GEORGE |  | Other |

##### Snowflake

##### Query

```sql
    SELECT
   first_name,
   last_name,
   CASE
         WHEN RTRIM(department) = RTRIM('EngineerinG')
            THEN 'Information Technology'
         WHEN COLLATE(first_name, 'en-cs-rtrim')  = '    GeorgE   '
            THEN 'GLOBAL SALES'
       ELSE 'Other'
   END AS department_full_name
FROM
   employees
WHERE RTRIM(last_name) = RTRIM('');
```

##### Output

| first_name | last_name | department_full_name |
| --- | --- | --- |
| Mary |  | Other |
| GEORGE |  | Other |
| GEORGE |  | Other |
| GeorgE |  | GLOBAL SALES |

#### JOIN clause

> **Warning:**
>
> Simple scenarios with evaluation operations are supported.

The `JOIN` statement will use the patterns described in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Sample: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name
FROM
    employees e
JOIN
    departments d
ON
    e.department = d.department_name;
```

##### Output

| employee_id | first_name | last_name | department_name |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 10 | JOHN | snow | Finance |

##### Snowflake

> **Note:**
>
> `d.department_name` is `NOT CASESPECIFIC`, so it requires `COLLATE`.

##### Query

```sql
    SELECT
   e.employee_id,
   e.first_name,
   e.last_name,
   d.department_name
FROM
   employees e
JOIN
   departments d
ON COLLATE(e.department, 'en-cs-rtrim') = d.department_name;
```

##### Output

| employee_id | first_name | last_name | department_name |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 10 | JOHN | snow | Finance |

#### Related EWIs

[SSC-EWI-TD0007](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/teradataEWI.md): GROUP BY IS NOT EQUIVALENT IN TERADATA MODE

[SC-FDM-TD0032](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/teradataFDM.md) : [NOT] CASESPECIFIC CLAUSE WAS REMOVED

## ANSI Mode For Strings Comparison - NO COLLATE

This section defines the translation specification for a string in ANSI mode without the use of COLLATE.

### Description

#### ANSI mode for string comparison and NO COLLATE usages

The ANSI mode string comparison without the use of COLLATE will apply RTRIM and UPPER as needed. The default case specification trim behavior may be taken into account, so if a column does not have a case specification in Teradata ANSI mode, Teradata will have as default `CASESPECIFIC`.

### Sample Source Patterns

#### Setup data

##### Teradata

```sql
 CREATE TABLE employees (
    employee_id INTEGER NOT NULL,
    first_name VARCHAR(50) NOT CASESPECIFIC,
    last_name VARCHAR(50) CASESPECIFIC,
    department VARCHAR(50)
);

INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (1, 'George', 'Snow', 'Sales');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (2, 'John', 'SNOW', 'Engineering');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (3, 'WIlle', 'SNOW', 'Human resources   ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (4, 'Marco', 'SnoW   ', 'EngineerinG');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (5, 'Mary', '   ', 'SaleS  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (6, 'GEORGE', '  ', 'sales  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (7, 'GEORGE   ', '  ', 'salEs  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (8, '    GeorgE   ', '  ', 'SalEs  ');
INSERT INTO employees (employee_id, first_name, last_name, department) VALUES (9, 'JOHN', '   SnoW', 'IT');
INSERT INTO employees (employee_id, first_name, last_name, department) VALUES (10, 'JOHN    ', 'snow', 'Finance   ');

CREATE TABLE departments (
    department_id INTEGER NOT NULL,
    department_name VARCHAR(50) NOT CASESPECIFIC,
    location VARCHAR(100) CASESPECIFIC,
    PRIMARY KEY (department_id)
);

INSERT INTO departments (department_id, department_name, location) VALUES (101, 'Information Technology', 'New York');
INSERT INTO departments (department_id, department_name, location) VALUES (102, 'Human Resources', 'Chicago');
INSERT INTO departments (department_id, department_name, location) VALUES (103, 'Sales', 'San Francisco');
INSERT INTO departments (department_id, department_name, location) VALUES (104, 'Finance', 'Boston');
```

##### Snowflake

```sql
 CREATE OR REPLACE TABLE employees (
    employee_id INTEGER NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/30/2024",  "domain": "test" }}'
;

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (1, 'George', 'Snow', 'Sales');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (2, 'John', 'SNOW', 'Engineering');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (3, 'WIlle', 'SNOW', 'Human resources   ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (4, 'Marco', 'SnoW   ', 'EngineerinG');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (5, 'Mary', '   ', 'SaleS  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (6, 'GEORGE', '  ', 'sales  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (7, 'GEORGE   ', '  ', 'salEs  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (8, '    GeorgE   ', '  ', 'SalEs  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (9, 'JOHN', '   SnoW', 'IT');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (10, 'JOHN    ', 'snow', 'Finance   ');

CREATE OR REPLACE TABLE departments (
    department_id INTEGER NOT NULL,
    department_name VARCHAR(50),
    location VARCHAR(100),
       PRIMARY KEY (department_id)
   )
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/30/2024",  "domain": "test" }}'
;

INSERT INTO departments (department_id, department_name, location)
VALUES (101, 'Information Technology', 'New York');

INSERT INTO departments (department_id, department_name, location)
VALUES (102, 'Human Resources', 'Chicago');

INSERT INTO departments (department_id, department_name, location)
VALUES (103, 'Sales', 'San Francisco');

INSERT INTO departments (department_id, department_name, location)
VALUES (104, 'Finance', 'Boston');
```

#### Comparison operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name = 'George      ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Snowflake

##### Query

```sql
 SELECT
 *
FROM
employees
WHERE
RTRIM(first_name) = RTRIM('George      ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name = 'SNOW ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

##### Snowflake

##### Query

```sql
 SELECT
 *
FROM
employees
WHERE
 RTRIM(last_name) = RTRIM('SNOW ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

##### Case 3: CAST NOT CASESPECIFIC column to CASESPECIFIC and database mode is ANSI Mode

> **Warning:**
>
> The (`CASESPECIFIC`) overwrite the column constraint in the table definition.

##### Teradata

##### Query

```sql
 SELECT * FROM employees WHERE first_name = 'GEorge   ' (CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT * FROM workers
WHERE RTRIM(first_name) = RTRIM(UPPER('GEorge   '));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 6 | GEORGE |  | sales |

##### Case 4: CAST CASESPECIFIC column to NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT * FROM employees
WHERE last_name = 'SnoW   ' (NOT CASESPECIFIC) ;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 4 | Marco | SnoW | EngineerinG |

##### Snowflake

##### Query

```sql
 SELECT * FROM employees
WHERE RTRIM(last_name) = RTRIM('SnoW   ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 4 | Marco | SnoW | EngineerinG |

#### LIKE operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name LIKE 'Georg%';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Snowflake

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name LIKE 'Georg%';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name LIKE 'Snow';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Snowflake

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name LIKE 'Snow';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Case 3: CAST NOT CASESPECIFIC column to NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name LIKE 'George' (NOT CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   first_name ILIKE 'George' /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Case 4: CAST CASESPECIFIC column to NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name LIKE 'SNO%' (NOT CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 2 | John | SNOW | Engineering |
| 3 | WIlle | SNOW | Human resources |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   last_name LIKE 'SNO%' /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 2 | John | SNOW | Engineering |
| 3 | WIlle | SNOW | Human resources |

#### IN Operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name IN ('GEORGE   ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 6 | GEORGE |  | sales |
| 7 | GEORGE |  | salEs |

##### Snowflake

##### Query

```sql
 SELECT *
FROM employees
WHERE RTRIM(first_name) IN (RTRIM('GEORGE   '));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 6 | GEORGE |  | sales |
| 7 | GEORGE |  | salEs |

##### Case 2: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE department IN ('SaleS');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 5 | Mary |  | SaleS |

##### Snowflake

##### Query

```sql
 SELECT *
FROM employees
WHERE RTRIM(department) IN (RTRIM('SaleS'));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 5 | Mary |  | SaleS |

#### ORDER BY clause

> **Note:**
>
> **Notice that this functional equivalence can differ.**

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT department_name
FROM departments
ORDER BY department_name;
```

##### Output

| department |
| --- |
| EngineerinG |
| Engineering |
| Finance |
| Human resources |
| IT |
| SalEs |
| SaleS |
| Sales |
| salEs |
| sales |

##### Snowflake

> **Note:**
>
> **Please review FDM. The order differs in the order of insertion of data.**

##### Query

```sql
 SELECT
   department_name
FROM
   departments
ORDER BY
   UPPER(department_name);
```

##### Output

| department |
| --- |
| EngineerinG |
| Engineering |
| Finance |
| Human resources |
| IT |
| SalEs |
| SaleS |
| Sales |
| salEs |
| sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT last_name
FROM employees
ORDER BY last_name;
```

##### Output

| department |
| --- |
| Finance |
| Human Resources |
| Information Technology |
| Sales |

##### Snowflake

##### Query

```sql
 SELECT last_name
FROM employees
ORDER BY last_name;
```

##### Output

| department |
| --- |
| Finance |
| Human Resources |
| Information Technology |
| Sales |

#### GROUP BY clause

> **Warning:**
>
> **To ensure a functional equivalence, it is required to use the COLLATE expression.**
>
> Please review the [SSC-EWI-TD0007](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/teradataEWI.md) for more information.

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT first_name
FROM employees
GROUP BY first_name;
```

##### Output

| first_name |
| --- |
| Mary |
| GeorgE |
| WIlle |
| John |
| Marco |
| GEORGE |

##### Snowflake

##### Query

```sql
 SELECT
   first_name
FROM
   employees
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0007 - GROUP BY IS NOT EQUIVALENT IN TERADATA MODE ***/!!!
GROUP BY first_name;
```

##### Output

| FIRST_NAME |
| --- |
| George |
| John |
| WIlle |
| Marco |
| Mary |
| GEORGE |
| GEORGE |
| GeorgE |
| JOHN |
| JOHN |

##### Case 2: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT last_name
FROM employees
GROUP BY last_name;
```

##### Output

| last_name |
| --- |
| SnoW |
|  |
| SNOW |
| SnoW |
| Snow |
| snow |

##### Snowflake

##### Query

```sql
 SELECT
   last_name
FROM
   employees
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0007 - GROUP BY IS NOT EQUIVALENT IN TERADATA MODE ***/!!!
GROUP BY last_name;
```

##### Output

| last_name |
| --- |
| SnoW |
|  |
| SNOW |
| SnoW |
| Snow |
| snow |

#### HAVING clause

The HAVING clause will use the patterns in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Sample: Column constraint is NOT CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT first_name
FROM employees
GROUP BY first_name
HAVING first_name = 'GEORGE';
```

##### Output

```none
GEORGE
```

##### Snowflake

##### Query

```sql
 SELECT
   first_name
FROM
   employees
GROUP BY first_name
HAVING
   RTRIM(first_name) = RTRIM('GEORGE');
```

##### Output

```none
GEORGE
```

#### CASE WHEN statement

The `CASE WHEN` statement will use the patterns described in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Teradata

##### Query

```sql
 SELECT first_name,
      last_name,
      CASE
          WHEN department = 'SaleS  ' THEN 'GLOBAL SALES'
          WHEN first_name = 'GEORGE   ' THEN 'Department Full Name'
          ELSE 'Other'
      END AS department_full_name
FROM employees
WHERE last_name = '   ';
```

##### Output

| first_name | last_name | department_full_name |
| --- | --- | --- |
| GEORGE |  | Department Full Name |
| Mary |  | GLOBAL SALES |
| GeorgE |  | Other |
| GEORGE |  | Department Full Name |

##### Snowflake

##### Query

```sql
 SELECT
      first_name,
      last_name,
      CASE
            WHEN UPPER(RTRIM(department)) = UPPER(RTRIM('SaleS  '))
                  THEN 'GLOBAL SALES'
            WHEN UPPER(RTRIM(first_name)) = UPPER(RTRIM('GEORGE   '))
                  THEN 'Department Full Name'
          ELSE 'Other'
      END AS department_full_name
FROM
      employees
WHERE
      UPPER(RTRIM( last_name)) = UPPER(RTRIM('   '));
```

##### Output

| first_name | last_name | department_full_name |
| --- | --- | --- |
| GEORGE |  | Department Full Name |
| Mary |  | GLOBAL SALES |
| GeorgE |  | Other |
| GEORGE |  | Department Full Name |

#### JOIN clause

> **Warning:**
>
> Simple scenarios are supported.

The `JOIN` statement will use the patterns described in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Sample: Column constraint is CASESPECIFIC and database mode is ANSI Mode

##### Teradata

##### Query

```sql
 SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name
FROM
    employees e
JOIN
    departments d
ON
    e.department = d.department_name;
```

##### Output

| employee_id | first_name | last_name | department_name |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 10 | JOHN | snow | Finance |

##### Snowflake

##### Query

```sql
 SELECT
   e.employee_id,
   e.first_name,
   e.last_name,
   d.department_name
FROM
   employees e
JOIN
      departments d
ON RTRIM(e.department) = RTRIM(d.department_name);
```

##### Output

| employee_id | first_name | last_name | department_name |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 10 | JOHN | snow | Finance |

### Related EWIs

[SSC-EWI-TD0007](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/teradataEWI.md): GROUP BY IS NOT EQUIVALENT IN TERADATA MODE

## TERA Mode For Strings Comparison - COLLATE

This section defines the translation specification for string in Tera mode with the use of COLLATE.

### Description

#### Tera Mode for string comparison and COLLATE usage

The Tera Mode string comparison will apply the COLLATE constraint to the columns or statements as required. The default case specification trim behavior may be taken into account. The default case specification in Teradata for TERA mode is `NOT CASESPECIFIC`. Thus, the columns without case specification will have `COLLATE('en-ci')` constraints.

### Sample Source Patterns

#### Setup data

##### Teradata

```sql
 CREATE TABLE employees (
    employee_id INTEGER NOT NULL,
    first_name VARCHAR(50) NOT CASESPECIFIC,
    last_name VARCHAR(50) CASESPECIFIC,
    department VARCHAR(50)
);

INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (1, 'George', 'Snow', 'Sales');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (2, 'John', 'SNOW', 'Engineering');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (3, 'WIlle', 'SNOW', 'Human resources   ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (4, 'Marco', 'SnoW   ', 'EngineerinG');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (5, 'Mary', '   ', 'SaleS  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (6, 'GEORGE', '  ', 'sales  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (7, 'GEORGE   ', '  ', 'salEs  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (8, '    GeorgE   ', '  ', 'SalEs  ');
INSERT INTO employees (employee_id, first_name, last_name, department) VALUES (9, 'JOHN', '   SnoW', 'IT');
INSERT INTO employees (employee_id, first_name, last_name, department) VALUES (10, 'JOHN    ', 'snow', 'Finance   ');

CREATE TABLE departments (
    department_id INTEGER NOT NULL,
    department_name VARCHAR(50) NOT CASESPECIFIC,
    location VARCHAR(100) CASESPECIFIC,
    PRIMARY KEY (department_id)
);

INSERT INTO departments (department_id, department_name, location) VALUES (101, 'Information Technology', 'New York');
INSERT INTO departments (department_id, department_name, location) VALUES (102, 'Human Resources', 'Chicago');
INSERT INTO departments (department_id, department_name, location) VALUES (103, 'Sales', 'San Francisco');
INSERT INTO departments (department_id, department_name, location) VALUES (104, 'Finance', 'Boston');
```

##### Snowflake

```sql
 CREATE OR REPLACE TABLE employees (
    employee_id INTEGER NOT NULL,
    first_name VARCHAR(50) COLLATE 'en-ci',
    last_name VARCHAR(50),
    department VARCHAR(50) COLLATE 'en-ci'
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "11/01/2024",  "domain": "test" }}'
;

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (1, 'George', 'Snow', 'Sales');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (2, 'John', 'SNOW', 'Engineering');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (3, 'WIlle', 'SNOW', 'Human resources   ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (4, 'Marco', 'SnoW   ', 'EngineerinG');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (5, 'Mary', '   ', 'SaleS  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (6, 'GEORGE', '  ', 'sales  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (7, 'GEORGE   ', '  ', 'salEs  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (8, '    GeorgE   ', '  ', 'SalEs  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (9, 'JOHN', '   SnoW', 'IT');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (10, 'JOHN    ', 'snow', 'Finance   ');

CREATE OR REPLACE TABLE departments (
    department_id INTEGER NOT NULL,
    department_name VARCHAR(50) COLLATE 'en-ci',
    location VARCHAR(100),
       PRIMARY KEY (department_id)
   )
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "11/01/2024",  "domain": "test" }}'
;

INSERT INTO departments (department_id, department_name, location)
VALUES (101, 'Information Technology', 'New York');

INSERT INTO departments (department_id, department_name, location)
VALUES (102, 'Human Resources', 'Chicago');

INSERT INTO departments (department_id, department_name, location)
VALUES (103, 'Sales', 'San Francisco');

INSERT INTO departments (department_id, department_name, location)
VALUES (104, 'Finance', 'Boston');
```

#### Comparison operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name = 'GEorge ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT
 *
FROM
 employees
WHERE
 RTRIM(first_name) = RTRIM('GEorge ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name = 'SNOW ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

##### Snowflake

##### Query

```sql
SELECT
 *
FROM
 employees
WHERE
 RTRIM(last_name) = RTRIM('SNOW ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

##### Case 3: CAST NOT CASESPECIFIC column to CASESPECIFIC and database mode is TERA Mode

> **Note:**
>
> Notice that the following queries
>
> * `SELECT * FROM employees WHERE first_name = 'JOHN ' (CASESPECIFIC)`
> * `SELECT * FROM employees WHERE first_name (CASESPECIFIC) = 'JOHN '`
>
> will return the same values.

##### Teradata

##### Query

```sql
 SELECT * FROM employees WHERE first_name = 'JOHN   ' (CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 9 | JOHN | SnoW | IT |
| 10 | JOHN | snow | Finance |

##### Snowflake

##### Query

```sql
 SELECT
    *
FROM
    employees
WHERE
    COLLATE(first_name, 'en-cs-rtrim') = 'JOHN   ' /*** SSC-FDM-TD0032 - CASESPECIFIC CLAUSE WAS REMOVED ***/;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 9 | JOHN | SnoW | IT |
| 10 | JOHN | snow | Finance |

##### Case 4: CAST CASESPECIFIC column to NOT CASESPECIFIC and database mode is TERA Mode

> **Note:**
>
> CAST to a column on the left side of the comparison has priority.
>
> For example:
>
> * `SELECT * FROM employees WHERE last_name (NOT CASESPECIFIC) = 'snoW';` *will return **5 rows.***
> * `SELECT * FROM employees WHERE last_name = 'snoW' (NOT CASESPECIFIC);` *will return **0 rows** with this setup data.*

##### Teradata

##### Query

```sql
 SELECT * FROM employees WHERE last_name (NOT CASESPECIFIC)  = 'snoW' ;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 2 | John | SNOW | Engineering |
| 3 | WIlle | SNOW | Human resources |
| 4 | Marco | SnoW | EngineerinG |
| 10 | JOHN | snow | Finance |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   COLLATE(last_name /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/, 'en-ci-rtrim') = 'snoW' ;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 2 | John | SNOW | Engineering |
| 3 | WIlle | SNOW | Human resources |
| 4 | Marco | SnoW | EngineerinG |
| 10 | JOHN | snow | Finance |

#### LIKE operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name LIKE 'GeorgE';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(first_name) LIKE RTRIM('GeorgE');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name LIKE 'Snow';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(last_name) LIKE RTRIM('Snow');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Case 3: CAST NOT CASESPECIFIC column to CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name LIKE 'George' (CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Snowflake

##### Query

```sql
 SELECT
    *
FROM
    employees
WHERE
    COLLATE(first_name, 'en-cs-rtrim') LIKE 'George';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |

##### Case 4: CAST CASESPECIFIC column to NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name LIKE 'SNO%' (NOT CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(last_name) LIKE RTRIM('SNO%' /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

#### IN Operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name IN ('George   ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(first_name) IN (RTRIM('George   '));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Case 2: Column constraint is not defined and database mode is TERA Mode

> **Note:**
>
> In Tera mode, not defined case specification means `NOT CASESPECIFIC`.

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE department IN ('Sales    ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 5 | Mary |  | SaleS |
| 6 | GEORGE |  | sales |
| 7 | GEORGE |  | salEs |
| 8 | GeorgE |  | SalEs |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(department) IN (RTRIM('Sales    '));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 5 | Mary |  | SaleS |
| 6 | GEORGE |  | sales |
| 7 | GEORGE |  | salEs |
| 8 | GeorgE |  | SalEs |

##### Case 3: Column constraint is CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name IN ('SNOW   ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(last_name) IN (RTRIM('SNOW   '));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

#### ORDER BY clause

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT employee_id, first_name
FROM employees
ORDER BY employee_id, first_name;
```

##### Output

| employee_id | first_name |
| --- | --- |
| 1 | George |
| 2 | John |
| 3 | WIlle |
| 4 | Marco |
| 5 | Mary |
| 6 | GEORGE |
| 7 | GEORGE |
| 8 | GeorgE |
| 9 | JOHN |
| 10 | JOHN |

##### Snowflake

##### Query

```sql
 SELECT employee_id, first_name
FROM employees
ORDER BY employee_id, first_name;
```

##### Output

| employee_id | first_name |
| --- | --- |
| 1 | George |
| 2 | John |
| 3 | WIlle |
| 4 | Marco |
| 5 | Mary |
| 6 | GEORGE |
| 7 | GEORGE |
| 8 | GeorgE |
| 9 | JOHN |
| 10 | JOHN |

##### Case 2: Column constraint is CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT employee_id, last_name
FROM employees
ORDER BY employee_id, last_name;
```

##### Output

| employee_id | last_name |
| --- | --- |
| 1 | Snow |
| 2 | SNOW |
| 3 | SNOW |
| 4 | SnoW |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |
| 9 | SnoW |
| 10 | snow |

##### Snowflake

##### Query

```sql
 SELECT employee_id, last_name
FROM employees
ORDER BY employee_id, last_name;
```

##### Output

| employee_id | last_name |
| --- | --- |
| 1 | Snow |
| 2 | SNOW |
| 3 | SNOW |
| 4 | SnoW |
| 5 |  |
| 6 |  |
| 7 |  |
| 8 |  |
| 9 | SnoW |
| 10 | snow |

#### GROUP BY clause

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT first_name
FROM employees
GROUP BY first_name;
```

##### Output

| first_name |
| --- |
| Mary |
| GeorgE |
| WIlle |
| **JOHN** |
| Marco |
| **GEORGE** |

##### Snowflake

> **Warning:**
>
> Case specification in output may vary depending on the number of columns selected.

##### Query

```sql
 SELECT
   first_name
FROM
   employees
GROUP BY first_name;
```

##### Output

| first_name |
| --- |
| **John** |
| Marco |
| **George** |
| GeorgE |
| WIlle |
| Mary |

##### Case 2: Column constraint is CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT last_name
FROM employees
GROUP BY last_name;
```

##### Output

| last_name |
| --- |
| SnoW |
|  |
| SNOW |
| SnoW |
| Snow |
| snow |

##### Snowflake

##### Query

```sql
 SELECT
   last_name
FROM
   employees
GROUP BY last_name;
```

##### Output

| last_name |
| --- |
| SnoW |
|  |
| SNOW |
| SnoW |
| Snow |
| snow |

#### HAVING clause

The HAVING clause will use the patterns in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Sample: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

> **Note:**
>
> Case specification in output may vary depending on the number of columns selected. This is also related to the `GROUP BY` clause.

##### Query

```sql
 SELECT first_name
FROM employees
GROUP BY first_name
HAVING first_name = 'George  ';
```

##### Output

| employee_id | first_name |
| --- | --- |
| 7 | GEORGE |
| 1 | George |
| 6 | GEORGE |

##### Snowflake

##### Query

```sql
 SELECT
  employee_id,
  first_name
FROM
  employees
GROUP BY employee_id, first_name
HAVING
   RTRIM(first_name) = RTRIM('George  ');
```

##### Output

| employee_id | first_name |
| --- | --- |
| 7 | GEORGE |
| 1 | George |
| 6 | GEORGE |

#### CASE WHEN statement

The `CASE WHEN` statement will use the patterns described in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Teradata

##### Query

```sql
 SELECT first_name,
      last_name,
      CASE
          WHEN department = 'Engineering' THEN 'Information Technology'
          WHEN first_name = 'GeorgE' THEN 'GLOBAL SALES'
          ELSE 'Other'
      END AS department_full_name
FROM employees
WHERE last_name = '';
```

##### Output

| first_name | last_name | department_full_name |
| --- | --- | --- |
| GEORGE |  | GLOBAL SALES |
| Mary |  | Other |
| GeorgE |  | Other |
| GEORGE |  | GLOBAL SALES |

##### Snowflake

##### Query

```sql
 SELECT
   first_name,
   last_name,
   CASE
      WHEN RTRIM(department) = RTRIM('Engineering')
         THEN 'Information Technology'
      WHEN RTRIM(first_name) = RTRIM('GeorgE')
         THEN 'GLOBAL SALES'
      ELSE 'Other'
   END AS department_full_name
FROM
   employees
WHERE
   RTRIM( last_name) = RTRIM('');
```

##### Output

| first_name | last_name | department_full_name |
| --- | --- | --- |
| GEORGE |  | GLOBAL SALES |
| Mary |  | Other |
| GeorgE |  | Other |
| GEORGE |  | GLOBAL SALES |

#### JOIN clause

> **Warning:**
>
> Simple scenarios with evaluation operations are supported.

The `JOIN` statement will use the patterns described in:

* Evaluation of comparison operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Sample: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name
FROM
    employees e
JOIN
    departments d
ON
    e.department = d.department_name;
```

##### Output

| employee_id | first_name | last_name | department_name |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 3 | WIlle | SNOW | Human Resources |
| 5 | Mary |  | Sales |
| 6 | GEORGE |  | Sales |
| 7 | GEORGE |  | Sales |
| 8 | GeorgE |  | Sales |
| 10 | JOHN | snow | Finance |

##### Snowflake

##### Query

```sql
 SELECT
   e.employee_id,
   e.first_name,
   e.last_name,
   d.department_name
FROM
   employees e
JOIN
   departments d
ON RTRIM(e.department) = RTRIM(d.department_name);
```

##### Output

| employee_id | first_name | last_name | department_name |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 3 | WIlle | SNOW | Human Resources |
| 5 | Mary |  | Sales |
| 6 | GEORGE |  | Sales |
| 7 | GEORGE |  | Sales |
| 8 | GeorgE |  | Sales |
| 10 | JOHN | snow | Finance |

### Related EWIs

[SSC-EWI-TD0007](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/teradataFDM.md): GROUP BY REQUIRED COLLATE FOR CASE INSENSITIVE COLUMNS

[SC-FDM-TD0032](../../general/technical-documentation/issues-and-troubleshooting/functional-difference/teradataFDM.md) : [NOT] CASESPECIFIC CLAUSE WAS REMOVED

## TERA Mode For Strings Comparison - NO COLLATE

This section defines the translation specification for string in Tera mode without using COLLATE.

### Description

#### Tera Mode for string comparison and NO COLLATE usages

The Tera Mode string comparison without the use of COLLATE will apply `RTRIM` and `UPPER` as needed. The default case specification trim behavior may be taken into account.

### Sample Source Patterns

#### Setup data

##### Teradata

```sql
 CREATE TABLE employees (
    employee_id INTEGER NOT NULL,
    first_name VARCHAR(50) NOT CASESPECIFIC,
    last_name VARCHAR(50) CASESPECIFIC,
    department VARCHAR(50)
);

INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (1, 'George', 'Snow', 'Sales');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (2, 'John', 'SNOW', 'Engineering');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (3, 'WIlle', 'SNOW', 'Human resources   ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (4, 'Marco', 'SnoW   ', 'EngineerinG');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (5, 'Mary', '   ', 'SaleS  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (6, 'GEORGE', '  ', 'sales  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (7, 'GEORGE   ', '  ', 'salEs  ');
INSERT INTO employees(employee_id, first_name, last_name, department) VALUES (8, '    GeorgE   ', '  ', 'SalEs  ');
INSERT INTO employees (employee_id, first_name, last_name, department) VALUES (9, 'JOHN', '   SnoW', 'IT');
INSERT INTO employees (employee_id, first_name, last_name, department) VALUES (10, 'JOHN    ', 'snow', 'Finance   ');

CREATE TABLE departments (
    department_id INTEGER NOT NULL,
    department_name VARCHAR(50) NOT CASESPECIFIC,
    location VARCHAR(100) CASESPECIFIC,
    PRIMARY KEY (department_id)
);

INSERT INTO departments (department_id, department_name, location) VALUES (101, 'Information Technology', 'New York');
INSERT INTO departments (department_id, department_name, location) VALUES (102, 'Human Resources', 'Chicago');
INSERT INTO departments (department_id, department_name, location) VALUES (103, 'Sales', 'San Francisco');
INSERT INTO departments (department_id, department_name, location) VALUES (104, 'Finance', 'Boston');
```

##### Snowflake

```sql
 CREATE OR REPLACE TABLE employees (
    employee_id INTEGER NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50)
)
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/30/2024",  "domain": "test" }}'
;

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (1, 'George', 'Snow', 'Sales');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (2, 'John', 'SNOW', 'Engineering');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (3, 'WIlle', 'SNOW', 'Human resources   ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (4, 'Marco', 'SnoW   ', 'EngineerinG');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (5, 'Mary', '   ', 'SaleS  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (6, 'GEORGE', '  ', 'sales  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (7, 'GEORGE   ', '  ', 'salEs  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (8, '    GeorgE   ', '  ', 'SalEs  ');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (9, 'JOHN', '   SnoW', 'IT');

INSERT INTO employees (employee_id, first_name, last_name, department)
VALUES (10, 'JOHN    ', 'snow', 'Finance   ');

CREATE OR REPLACE TABLE departments (
    department_id INTEGER NOT NULL,
    department_name VARCHAR(50),
    location VARCHAR(100),
       PRIMARY KEY (department_id)
   )
COMMENT = '{ "origin": "sf_sc", "name": "snowconvert", "version": {  "major": 0,  "minor": 0,  "patch": "0" }, "attributes": {  "component": "teradata",  "convertedOn": "10/30/2024",  "domain": "test" }}'
;

INSERT INTO departments (department_id, department_name, location)
VALUES (101, 'Information Technology', 'New York');

INSERT INTO departments (department_id, department_name, location)
VALUES (102, 'Human Resources', 'Chicago');

INSERT INTO departments (department_id, department_name, location)
VALUES (103, 'Sales', 'San Francisco');

INSERT INTO departments (department_id, department_name, location)
VALUES (104, 'Finance', 'Boston');
```

#### Comparison operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

This example demonstrates the usage of a column set up as `NOT CASESPECIFIC` as it is a `first_name` column. Even when asking for the string `'GEorge',` the query execution will retrieve results in Teradata because the case specification is not considered.

To emulate this scenario in Snowflake, there are implemented two functions: `RTRIM(UPPER(string_evaluation))`, `UPPER` is required in this scenario because the string does not review the case specification.

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name = 'GEorge ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT
 *
FROM
 employees
WHERE
 RTRIM(UPPER(first_name)) = RTRIM(UPPER('GEorge '));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is TERA Mode

For this example, the column constraint is `CASESPECIFIC`, for which the example does not retrieve rows in Teradata because ‘`Snow`’ is not equal to ‘`SNOW`’.

In Snowflake, the resulting migration points only to the use of the `RTRIM` function since the case specification is important.

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name = 'SNOW ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

##### Snowflake

##### Query

```sql
SELECT
 *
FROM
 employees
WHERE
 RTRIM(last_name) = RTRIM('SNOW ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 3 | WIlle | SNOW | Human resources |
| 2 | John | SNOW | Engineering |

##### Case 3: CAST CASESPECIFIC column to NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

> **Warning:**
>
> The (`CASESPECIFIC`) overrides the column constraint in the table definition.

##### Query

```sql
 SELECT * FROM employees WHERE first_name = 'GEORGE   ' (CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 6 | GEORGE |  | sales |

##### Snowflake

> **Note:**
>
> RTRIM is required on the left side, and RTRIM is required on the right side.

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(first_name) = RTRIM('GEORGE   ' /*** SSC-FDM-TD0032 - CASESPECIFIC CLAUSE WAS REMOVED ***/);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 6 | GEORGE |  | sales |

##### Case 4: CAST NOT CASESPECIFIC column to NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT * FROM employees WHERE first_name = 'GEorge   ' (NOT CASESPECIFIC) ;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   UPPER(RTRIM(first_name)) = UPPER(RTRIM('GEorge   ' /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Case 5: Blank spaces case. Column constraint is NOT CASESPECIFIC, database mode is TERA Mode, and using equal operation

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name = '   ';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 5 | Mary |  | SaleS |
| 8 | GeorgE |  | SalEs |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   RTRIM(last_name) = RTRIM('   ');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 5 | Mary |  | SaleS |
| 8 | GeorgE |  | SalEs |
| 6 | GEORGE |  | sales |

#### LIKE operation

> **Note:**
>
> This operation works differently from another one. Blank spaces must be the same quantity to retrieve information.

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

This example is expected to display one row because the case specification is not relevant.

> **Note:**
>
> In Snowflake, the migration uses the [ILIKE](https://docs.snowflake.com/en/sql-reference/functions/ilike) operation. This performs a case-insensitive comparison.

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name LIKE 'GeorgE';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name ILIKE 'GeorgE';
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name LIKE 'Snow';
```

##### Output

| first_name | last_name | department |
| --- | --- | --- |
| George | Snow | Sales |
| Jonh | Snow | Engineering |

##### Snowflake

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name LIKE 'Snow';
```

##### Output

| first_name | last_name | department |
| --- | --- | --- |
| George | Snow | Sales |
| Jonh | Snow | Engineering |

##### Case 3: CAST CASESPECIFIC column to NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name LIKE 'George' (NOT CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   first_name ILIKE 'George' /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Case 4: CAST NOT CASESPECIFIC column to NOT CASESPECIFIC and database mode is ANSI Mode

> **Note:**
>
> This case requires the translation to `ILIKE`.

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name LIKE 'GE%' (NOT CASESPECIFIC);
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT
   *
FROM
   employees
WHERE
   first_name ILIKE 'GE%' /*** SSC-FDM-TD0032 - NOT CASESPECIFIC CLAUSE WAS REMOVED ***/;
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

#### IN Operation

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE first_name IN ('GeorgE');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Snowflake

##### Query

```sql
 SELECT *
FROM employees
WHERE RTRIM(UPPER(first_name)) IN (RTRIM(UPPER('GeorgE')));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 7 | GEORGE |  | salEs |
| 1 | George | Snow | Sales |
| 6 | GEORGE |  | sales |

##### Case 2: Column constraint is CASESPECIFIC and database mode is TERA Mode

For this example, the usage of the UPPER function is not required since, in the Teradata database, the case specification is relevant to the results.

##### Teradata

##### Query

```sql
 SELECT *
FROM employees
WHERE last_name IN ('SnoW');
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 4 | Marco | SnoW | EngineerinG |

##### Snowflake

##### Query

```sql
 SELECT *
FROM employees
WHERE RTRIM(last_name) IN (RTRIM('SnoW'));
```

##### Output

| employee_id | first_name | last_name | department |
| --- | --- | --- | --- |
| 4 | Marco | SnoW | EngineerinG |

#### ORDER BY clause

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

> **Danger:**
>
> **Notice that this output order can differ.**

##### Teradata

##### Query

```sql
 SELECT department
FROM employees
ORDER BY department;
```

##### Output

| department |
| --- |
| EngineerinG |
| Engineering |
| Finance |
| Human resources |
| IT |
| sales |
| SalEs |
| Sales |
| SaleS |
| salEs |

##### Snowflake

##### Query

```sql
 SELECT department
FROM employees
ORDER BY UPPER(department);
```

##### Output

| department |
| --- |
| EngineerinG |
| Engineering |
| Finance |
| Human resources |
| IT |
| sales |
| SalEs |
| Sales |
| SaleS |
| salEs |

##### Case 2: Column constraint is CASESPECIFIC and database mode is TERA Mode

> **Danger:**
>
> **Notice that this output can differ in order.**

##### Teradata

##### Query

```sql
 SELECT last_name
FROM employees
ORDER BY last_name;
```

##### Output

| last_name |
| --- |
|  |
|  |
|  |
|  |
| SnoW |
| SNOW |
| SNOW |
| SnoW |
| Snow |
| snow |

##### Snowflake

##### Query

```sql
 SELECT last_name
FROM employees
ORDER BY last_name;
```

##### Output

| last_name |
| --- |
|  |
|  |
|  |
|  |
| SnoW |
| SNOW |
| SNOW |
| SnoW |
| Snow |
| snow |

#### GROUP BY clause

> **Warning:**
>
> **Notice that this output can differ. To ensure a functional equivalence, it is required to use the COLLATE expression.**
>
> Please review the SSC-EWI-TD0007 for more information.
>
> *The following might be a workaround without `collate`:*
>
> `SELECT RTRIM(UPPER(first_name))`
>
> `FROM employees`
>
> `GROUP BY RTRIM(UPPER(first_name));`

**About the column behavior**

> **Danger:**
>
> Please review the insertion of data in Snowflake. Snowflake does allow the insertion of values as ‘`GEORGE`’ and ‘`georges`’ without showing errors because the case specification is not bound explicitly with the column.

Assume a table and data as follows:

```sql
 CREATE TABLE students (
   first_name VARCHAR(50) NOT CASESPECIFIC
);

INSERT INTO students(first_name) VALUES ('George');
INSERT INTO students(first_name) VALUES ('   George');
```

Notice that this sample does not allow inserting values with upper and lower case letters in the `NOT CASESPECIFIC` column because it takes it as the same value. Because the column does not supervise the case specification, the ‘GEORGE’ and ‘george’ values are checked as the same information.

The following rows are taken as ***duplicated row errors***:

```sql
 INSERT INTO students(first_name) VALUES ('GEORGE');
INSERT INTO students(first_name) VALUES ('GeorGe');
INSERT INTO students(first_name) VALUES ('George  ');
INSERT INTO students(first_name) VALUES ('GeOrge');
INSERT INTO students(first_name) VALUES ('GEorge');
INSERT INTO students(first_name) VALUES ('George');
```

##### Case 1: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT first_name
FROM employees
GROUP BY first_name;
```

##### Output

| first_name |
| --- |
| Mary |
| GeorgE |
| WIlle |
| JOHN |
| Marco |
| GEORGE |

##### Snowflake

##### Query

```sql
 SELECT
   first_name
FROM
   employees
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0007 - GROUP BY IS NOT EQUIVALENT IN TERADATA MODE ***/!!!
GROUP BY first_name;
```

##### Output

| first_name |
| --- |
| George |
| John |
| WIlle |
| Marco |
| Mary |
| GEORGE |
| GEORGE |
| GeorgE |
| JOHN |
| JOHN |

##### Case 2: Column constraint is CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT last_name
FROM employees
GROUP BY last_name;
```

##### Output

| last_name |
| --- |
| SnoW |
|  |
| SNOW |
| SnoW |
| Snow |
| snow |

##### Snowflake

##### Query

```sql
 SELECT
   last_name
FROM
   employees
!!!RESOLVE EWI!!! /*** SSC-EWI-TD0007 - GROUP BY IS NOT EQUIVALENT IN TERADATA MODE ***/!!!
GROUP BY last_name;
```

##### Output

| last_name |
| --- |
| SnoW |
| SNOW |
| SnoW |
|  |
|  |
| Snow |
| snow |

#### HAVING clause

The HAVING clause will use the patterns in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Sample: Column constraint is CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT last_name
FROM employees
GROUP BY last_name
HAVING last_name = 'Snow';
```

##### Output

| last_name |
| --- |
| Snow |

##### Snowflake

##### Query

```sql
 SELECT last_name
FROM employees
GROUP BY last_name
HAVING RTRIM(last_name) = RTRIM('Snow');
```

##### Output

| last_name |
| --- |
| Snow |

#### CASE WHEN statement

The `CASE WHEN` statement will use the patterns described in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Teradata

##### Query

```sql
 SELECT first_name,
      last_name,
      CASE
          WHEN department = 'EngineerinG' THEN 'Information Technology'
          WHEN last_name = 'SNOW' THEN 'GLOBAL COOL SALES'
          ELSE 'Other'
      END AS department_full_name
FROM employees;
```

##### Output

| first_name | last_name | department_full_name |
| --- | --- | --- |
| GEORGE |  | Other |
| JOHN | SnoW | Other |
| Mary |  | Other |
| JOHN | snow | Other |
| WIlle | SNOW | GLOBAL COOL SALES |
| George | Snow | Other |
| GeorgE |  | Other |
| GEORGE |  | Other |
| Marco | SnoW | Information Technology |
| John | SNOW | Information Technology |

##### Snowflake

##### Query

```sql
 SELECT
   first_name,
   last_name,
   CASE
      WHEN UPPER(RTRIM(department)) = UPPER(RTRIM('EngineerinG'))
         THEN 'Information Technology'
      WHEN RTRIM(last_name) = RTRIM('SNOW')
         THEN 'GLOBAL COOL SALES'
      ELSE 'Other'
   END AS department_full_name
FROM
   employees;
```

##### Output

| first_name | last_name | department_full_name |
| --- | --- | --- |
| GEORGE |  | Other |
| JOHN | SnoW | Other |
| Mary |  | Other |
| JOHN | snow | Other |
| WIlle | SNOW | GLOBAL COOL SALES |
| George | Snow | Other |
| GeorgE |  | Other |
| GEORGE |  | Other |
| Marco | SnoW | Information Technology |
| John | SNOW | Information Technology |

#### JOIN clause

> **Warning:**
>
> Simple scenarios are supported.

The `JOIN` statement will use the patterns described in:

* Evaluation operations.

  * For example: `=, !=, <, >.`
* LIKE operation.
* IN Operation.
* CAST to evaluation operation.
* CAST to LIKE operation.

The following sample showcases a pattern with evaluation operation.

##### Sample: Column constraint is NOT CASESPECIFIC and database mode is TERA Mode

##### Teradata

##### Query

```sql
 SELECT
    e.employee_id,
    e.first_name,
    e.last_name,
    d.department_name
FROM
    employees e
JOIN
    departments d
ON
    e.department = d.department_name;
```

##### Output

| employee_id | first_name | last_name | department_name |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 3 | WIlle | SNOW | Human Resources |
| 5 | Mary |  | Sales |
| 6 | GEORGE |  | Sales |
| 7 | GEORGE |  | Sales |
| 8 | GeorgE |  | Sales |
| 10 | JOHN | snow | Finance |

##### Snowflake

##### Query

```sql
 SELECT
   e.employee_id,
   e.first_name,
   e.last_name,
   d.department_name
FROM
   employees e
JOIN
   departments d
ON UPPER(RTRIM(e.department)) = UPPER(RTRIM(d.department_name));
```

##### Output

| employee_id | first_name | last_name | department_name |
| --- | --- | --- | --- |
| 1 | George | Snow | Sales |
| 3 | WIlle | SNOW | Human Resources |
| 5 | Mary |  | Sales |
| 6 | GEORGE |  | Sales |
| 7 | GEORGE |  | Sales |
| 8 | GeorgE |  | Sales |
| 10 | JOHN | snow | Finance |

### Known Issues

1. there are some mode-specific SQL statement restrictions: `BEGIN TRANSACTION`, `END TRANSACTION`, `COMMIT [WORK]`.
2. Data insertion may differ in Snowflake since the case specification is not bound to the column declaration.
3. `GROUP BY` may differ in order, but group the correct values.
4. `ORDER BY` behaves differently in Snowflake.
5. If a function has a TRIM() from the source code, this workaround will add the required functions to the source code. So, RTRIM will be applied to the TRIM() source function.

### Related EWIs

[SSC-EWI-TD0007](../../general/technical-documentation/issues-and-troubleshooting/conversion-issues/teradataEWI.md): GROUP BY IS NOT EQUIVALENT IN TERADATA MODE
