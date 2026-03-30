# Source: https://clickhouse.ferndocs.com/cloud/guides/data-masking.md

---
slug: /cloud/guides/data-masking
sidebar_label: Data masking
title: Data masking in ClickHouse
description: A guide to data masking in ClickHouse
keywords:
  - data masking
doc_type: guide
---

Data masking is a technique used for data protection, in which the original data is replaced with a version of the data which maintains its format and structure while removing any personally identifiable information (PII) or sensitive information.

This guide shows you how you can mask data in ClickHouse.

## Use string replacement functions [#using-string-functions]

For basic data masking use cases, the `replace` family of functions offers a convenient way to mask data:

| Function                                                                                 | Description                                                                                                                                            |
|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [`replaceOne`](/sql-reference/functions/string-replace-functions#replaceOne)             | Replaces the first occurrence of a pattern in a haystack string with the provided replacement string.                                                  |
| [`replaceAll`](/sql-reference/functions/string-replace-functions#replaceAll)             | Replaces all occurrences of a pattern in a haystack string with the provided replacement string.                                                       |
| [`replaceRegexpOne`](/sql-reference/functions/string-replace-functions#replaceRegexpOne) | Replaces the first occurrence of a substring matching a regular expression pattern (in re2 syntax) in a haystack with the provided replacement string. |
| [`replaceRegexpAll`](/sql-reference/functions/string-replace-functions#replaceRegexpAll) | Replaces all occurrences of a substring matching a regular expression pattern (in re2 syntax) in a haystack with the provided replacement string.      |

For example, you can replace the name "John Smith" with a placeholder `[CUSTOMER_NAME]` using the `replaceOne` function:

```sql title="Query"
SELECT replaceOne(
    'Customer John Smith called about his account',
    'John Smith',
    '[CUSTOMER_NAME]'
) AS anonymized_text;
```

```response title="Response"
┌─anonymized_text───────────────────────────────────┐
│ Customer [CUSTOMER_NAME] called about his account │
└───────────────────────────────────────────────────┘
```

More generically, you can use the `replaceRegexpOne` to replace any customer name:

```sql title="Query"
SELECT 
    replaceRegexpAll(
        'Customer John Smith called. Later, Mary Johnson and Bob Wilson also called.',
        '\\b[A-Z][a-z]+ [A-Z][a-z]+\\b',
        '[CUSTOMER_NAME]'
    ) AS anonymized_text;
```

```response title="Response"
┌─anonymized_text───────────────────────────────────────────────────────────────────────┐
│ [CUSTOMER_NAME] Smith called. Later, [CUSTOMER_NAME] and [CUSTOMER_NAME] also called. │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

Or you could mask a social security number, leaving only the last 4 digits using the `replaceRegexpAll` function.

```sql title="Query"
SELECT replaceRegexpAll(
    'SSN: 123-45-6789',
    '(\d{3})-(\d{2})-(\d{4})',
    'XXX-XX-\3'
) AS masked_ssn;
```

In the query above `\3` is used to substitute the third capture group into the resulting string, which produces:

```response title="Response"
┌─masked_ssn───────┐
│ SSN: XXX-XX-6789 │
└──────────────────┘
```

## Create masked `VIEW`s [#masked-views]

A [`VIEW`](/sql-reference/statements/create/view) can be used in conjunction with the aforementioned string functions to apply transformations to columns containing sensitive data, before they are presented to the user. 
In this way, the original data remains unchanged, and users querying the view see only the masked data.

To demonstrate, let's imagine that we have a table which stores records of customer orders.
We want to make sure that a group of employees can view the information, but we don't want them to see the full information of the customers.

Run the query below to create an example table `orders` and insert some fictional customer order records into it:

```sql
CREATE TABLE orders (
    user_id UInt32,
    name String,
    email String,
    phone String,
    total_amount Decimal(10,2),
    order_date Date,
    shipping_address String
)
ENGINE = MergeTree()
ORDER BY user_id;

INSERT INTO orders VALUES
    (1001, 'John Smith', 'john.smith@gmail.com', '555-123-4567', 299.99, '2024-01-15', '123 Main St, New York, NY 10001'),
    (1002, 'Sarah Johnson', 'sarah.johnson@outlook.com', '555-987-6543', 149.50, '2024-01-16', '456 Oak Ave, Los Angeles, CA 90210'),
    (1003, 'Michael Brown', 'mbrown@company.com', '555-456-7890', 599.00, '2024-01-17', '789 Pine Rd, Chicago, IL 60601'),
    (1004, 'Emily Rogers', 'emily.rogers@yahoo.com', '555-321-0987', 89.99, '2024-01-18', '321 Elm St, Houston, TX 77001'),
    (1005, 'David Wilson', 'dwilson@email.net', '555-654-3210', 449.75, '2024-01-19', '654 Cedar Blvd, Phoenix, AZ 85001');
```

Create a view called `masked_orders`:

```sql
CREATE VIEW masked_orders AS
SELECT
    user_id,
    replaceRegexpOne(name, '^([A-Za-z]+)\\s+(.*)$', '\\1 ****') AS name,
    replaceRegexpOne(email, '^(.{0})[^@]*(@.*)$', '\\1****\\2') AS email,
    replaceRegexpOne(phone, '^(\\d{3})-(\\d{3})-(\\d{4})$', '\\1-***-\\3') AS phone,
    total_amount,
    order_date,
    replaceRegexpOne(shipping_address, '^[^,]+,\\s*(.*)$', '*** \\1') AS shipping_address
FROM orders;
```

In the `SELECT` clause of the view creation query above, we define transformations using the `replaceRegexpOne` on the `name`, `email`, `phone` and `shipping_address` fields, which are the fields containing sensitive information that we wish to partially mask.

Select the data from the view:

```sql title="Query"
SELECT * FROM masked_orders
```

```response title="Response"
┌─user_id─┬─name─────────┬─email──────────────┬─phone────────┬─total_amount─┬─order_date─┬─shipping_address──────────┐
│    1001 │ John ****    │ jo****@gmail.com   │ 555-***-4567 │       299.99 │ 2024-01-15 │ *** New York, NY 10001    │
│    1002 │ Sarah ****   │ sa****@outlook.com │ 555-***-6543 │        149.5 │ 2024-01-16 │ *** Los Angeles, CA 90210 │
│    1003 │ Michael **** │ mb****@company.com │ 555-***-7890 │          599 │ 2024-01-17 │ *** Chicago, IL 60601     │
│    1004 │ Emily ****   │ em****@yahoo.com   │ 555-***-0987 │        89.99 │ 2024-01-18 │ *** Houston, TX 77001     │
│    1005 │ David ****   │ dw****@email.net   │ 555-***-3210 │       449.75 │ 2024-01-19 │ *** Phoenix, AZ 85001     │
└─────────┴──────────────┴────────────────────┴──────────────┴──────────────┴────────────┴───────────────────────────┘
```

Notice that the data returned from the view is partially masked, obfuscating the sensitive information.
You can also create multiple views, with differing levels of obfuscation depending on the level of privileged access to information the viewer has.

To ensure that users are only able to access the view returning the masked data, and not the table with the original unmasked data, you should use [Role Based Access Control](/cloud/security/console-roles) to ensure that specific roles only have grants to select from the view.

First create the role:

```sql
CREATE ROLE masked_orders_viewer;
```

Next grant `SELECT` privileges on the view to the role:

```sql
GRANT SELECT ON masked_orders TO masked_orders_viewer;
```

Because ClickHouse roles are additive, you must ensure that users who should only see the masked view do not have any `SELECT` privilege on the base table via any role.

As such, you should explicitly revoke base-table access to be safe:

```sql
REVOKE SELECT ON orders FROM masked_orders_viewer;
```

Finally, assign the role to the appropriate users:

```sql
GRANT masked_orders_viewer TO your_user;
```

This ensures that users with the `masked_orders_viewer` role are only able to see
the masked data from the view and not the original unmasked data from the table.

## Use `MATERIALIZED` columns and column-level access restrictions [#materialized-ephemeral-column-restrictions]

In cases where you don't want to create a separate view, you can store masked versions of your data alongside the original data.
To do so, you can use [materialized columns](/sql-reference/statements/create/table#materialized).
Values of such columns are automatically calculated according to the specified materialized expression when rows are inserted,
and we can use them to create new columns with masked versions of the data.

Taking the example before, instead of creating a separate `VIEW` for the masked data, we'll now create masked columns using `MATERIALIZED`:

```sql
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    user_id UInt32,
    name String,
    name_masked String MATERIALIZED replaceRegexpOne(name, '^([A-Za-z]+)\\s+(.*)$', '\\1 ****'),
    email String,
    email_masked String MATERIALIZED replaceRegexpOne(email, '^(.{0})[^@]*(@.*)$', '\\1****\\2'),
    phone String,
    phone_masked String MATERIALIZED replaceRegexpOne(phone, '^(\\d{3})-(\\d{3})-(\\d{4})$', '\\1-***-\\3'),
    total_amount Decimal(10,2),
    order_date Date,
    shipping_address String,
    shipping_address_masked String MATERIALIZED replaceRegexpOne(shipping_address, '^[^,]+,\\s*(.*)$', '*** \\1')
)
ENGINE = MergeTree()
ORDER BY user_id;

INSERT INTO orders VALUES
    (1001, 'John Smith', 'john.smith@gmail.com', '555-123-4567', 299.99, '2024-01-15', '123 Main St, New York, NY 10001'),
    (1002, 'Sarah Johnson', 'sarah.johnson@outlook.com', '555-987-6543', 149.50, '2024-01-16', '456 Oak Ave, Los Angeles, CA 90210'),
    (1003, 'Michael Brown', 'mbrown@company.com', '555-456-7890', 599.00, '2024-01-17', '789 Pine Rd, Chicago, IL 60601'),
    (1004, 'Emily Rogers', 'emily.rogers@yahoo.com', '555-321-0987', 89.99, '2024-01-18', '321 Elm St, Houston, TX 77001'),
    (1005, 'David Wilson', 'dwilson@email.net', '555-654-3210', 449.75, '2024-01-19', '654 Cedar Blvd, Phoenix, AZ 85001');
```

If you now run the following select query, you will see that the masked data is 'materialized' at insert time and stored alongside the original, unmasked data.
It is necessary to explicitly select the masked columns as ClickHouse doesn't automatically include materialized columns in `SELECT *` queries by default.

```sql title="Query"
SELECT
    *,
    name_masked,
    email_masked,
    phone_masked,
    shipping_address_masked
FROM orders
ORDER BY user_id ASC
```

```response title="Response"
   ┌─user_id─┬─name──────────┬─email─────────────────────┬─phone────────┬─total_amount─┬─order_date─┬─shipping_address───────────────────┬─name_masked──┬─email_masked───────┬─phone_masked─┬─shipping_address_masked────┐
1. │    1001 │ John Smith    │ john.smith@gmail.com      │ 555-123-4567 │       299.99 │ 2024-01-15 │ 123 Main St, New York, NY 10001    │ John ****    │ jo****@gmail.com   │ 555-***-4567 │ **** New York, NY 10001    │
2. │    1002 │ Sarah Johnson │ sarah.johnson@outlook.com │ 555-987-6543 │        149.5 │ 2024-01-16 │ 456 Oak Ave, Los Angeles, CA 90210 │ Sarah ****   │ sa****@outlook.com │ 555-***-6543 │ **** Los Angeles, CA 90210 │
3. │    1003 │ Michael Brown │ mbrown@company.com        │ 555-456-7890 │          599 │ 2024-01-17 │ 789 Pine Rd, Chicago, IL 60601     │ Michael **** │ mb****@company.com │ 555-***-7890 │ **** Chicago, IL 60601     │
4. │    1004 │ Emily Rogers  │ emily.rogers@yahoo.com    │ 555-321-0987 │        89.99 │ 2024-01-18 │ 321 Elm St, Houston, TX 77001      │ Emily ****   │ em****@yahoo.com   │ 555-***-0987 │ **** Houston, TX 77001     │
5. │    1005 │ David Wilson  │ dwilson@email.net         │ 555-654-3210 │       449.75 │ 2024-01-19 │ 654 Cedar Blvd, Phoenix, AZ 85001  │ David ****   │ dw****@email.net   │ 555-***-3210 │ **** Phoenix, AZ 85001     │
   └─────────┴───────────────┴───────────────────────────┴──────────────┴──────────────┴────────────┴────────────────────────────────────┴──────────────┴────────────────────┴──────────────┴────────────────────────────┘
```

To ensure that users are only able to access columns containing the masked data, you can again use [Role Based Access Control](/cloud/security/console-roles) to ensure that specific roles only have grants to select on masked columns from `orders`.

Recreate the role that we made previously:

```sql
DROP ROLE IF EXISTS masked_order_viewer;
CREATE ROLE masked_order_viewer;
```

Next, grant `SELECT` permission to the `orders` table:

```sql
GRANT SELECT ON orders TO masked_data_reader;
```

Revoke access to any sensitive columns:

```sql
REVOKE SELECT(name) ON orders FROM masked_data_reader;
REVOKE SELECT(email) ON orders FROM masked_data_reader;
REVOKE SELECT(phone) ON orders FROM masked_data_reader;
REVOKE SELECT(shipping_address) ON orders FROM masked_data_reader;
```

Finally, assign the role to the appropriate users:

```sql
GRANT masked_orders_viewer TO your_user;
```

In the case where you want to store only the masked data in the `orders` table,
you can mark the sensitive unmasked columns as [`EPHEMERAL`](/sql-reference/statements/create/table#ephemeral),
which will ensure that columns of this type are not stored in the table.

```sql
DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    user_id UInt32,
    name String EPHEMERAL,
    name_masked String MATERIALIZED replaceRegexpOne(name, '^([A-Za-z]+)\\s+(.*)$', '\\1 ****'),
    email String EPHEMERAL,
    email_masked String MATERIALIZED replaceRegexpOne(email, '^(.{2})[^@]*(@.*)$', '\\1****\\2'),
    phone String EPHEMERAL,
    phone_masked String MATERIALIZED replaceRegexpOne(phone, '^(\\d{3})-(\\d{3})-(\\d{4})$', '\\1-***-\\3'),
    total_amount Decimal(10,2),
    order_date Date,
    shipping_address String EPHEMERAL,
    shipping_address_masked String MATERIALIZED replaceRegexpOne(shipping_address, '^([^,]+),\\s*(.*)$', '*** \\2')
)
ENGINE = MergeTree()
ORDER BY user_id;

INSERT INTO orders (user_id, name, email, phone, total_amount, order_date, shipping_address) VALUES
    (1001, 'John Smith', 'john.smith@gmail.com', '555-123-4567', 299.99, '2024-01-15', '123 Main St, New York, NY 10001'),
    (1002, 'Sarah Johnson', 'sarah.johnson@outlook.com', '555-987-6543', 149.50, '2024-01-16', '456 Oak Ave, Los Angeles, CA 90210'),
    (1003, 'Michael Brown', 'mbrown@company.com', '555-456-7890', 599.00, '2024-01-17', '789 Pine Rd, Chicago, IL 60601'),
    (1004, 'Emily Rogers', 'emily.rogers@yahoo.com', '555-321-0987', 89.99, '2024-01-18', '321 Elm St, Houston, TX 77001'),
    (1005, 'David Wilson', 'dwilson@email.net', '555-654-3210', 449.75, '2024-01-19', '654 Cedar Blvd, Phoenix, AZ 85001');
```

If we run the same query as before, you'll now see that only the materialized masked data was inserted into the table:

```sql title="Query"
SELECT
    *,
    name_masked,
    email_masked,
    phone_masked,
    shipping_address_masked
FROM orders
ORDER BY user_id ASC
```

```response title="Response"
   ┌─user_id─┬─total_amount─┬─order_date─┬─name_masked──┬─email_masked───────┬─phone_masked─┬─shipping_address_masked───┐
1. │    1001 │       299.99 │ 2024-01-15 │ John ****    │ jo****@gmail.com   │ 555-***-4567 │ *** New York, NY 10001    │
2. │    1002 │        149.5 │ 2024-01-16 │ Sarah ****   │ sa****@outlook.com │ 555-***-6543 │ *** Los Angeles, CA 90210 │
3. │    1003 │          599 │ 2024-01-17 │ Michael **** │ mb****@company.com │ 555-***-7890 │ *** Chicago, IL 60601     │
4. │    1004 │        89.99 │ 2024-01-18 │ Emily ****   │ em****@yahoo.com   │ 555-***-0987 │ *** Houston, TX 77001     │
5. │    1005 │       449.75 │ 2024-01-19 │ David ****   │ dw****@email.net   │ 555-***-3210 │ *** Phoenix, AZ 85001     │
   └─────────┴──────────────┴────────────┴──────────────┴────────────────────┴──────────────┴───────────────────────────┘
```

## Use query masking rules for log data [#use-query-masking-rules]

For users of ClickHouse OSS wishing to mask log data specifically, you can make use of [query masking rules](/operations/server-configuration-parameters/settings#query_masking_rules) (log masking) to mask data.

To do so, you can define regular expression-based masking rules in the server configuration.
These rules are applied to queries and all log messages before they are stored in server logs or system tables (such as `system.query_log`, `system.text_log`, and `system.processes`).

This helps prevent sensitive data from leaking into **logs** only.
Note that it does not mask data in query results.

For example, to mask a social security number, you could add the following rule to your [server configuration](/operations/configuration-files):

```yaml
<query_masking_rules>
    <rule>
        <name>hide SSN</name>
        <regexp>(^|\D)\d{3}-\d{2}-\d{4}($|\D)</regexp>
        <replace>000-00-0000</replace>
    </rule>
</query_masking_rules>
```
