# Source: https://docs.oxla.com/sql-reference/comment-support.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Comment Support

## Overview

OXLA fully supports comments in your queries. Comments provide a way to add explanatory notes and improve the readability of queries, making it easier for developers and stakeholders to understand complex queries.

There are two types of comments in OXLA: **single-line** and **multi-line (block)**.

## Single Line Comments

A single-line comment in OXLA starts with two consecutive hyphens (--) and extends to the end of the line. These comments are used to annotate specific parts of a query, providing brief explanations or notes to assist in understanding the query.

**Syntax:**

```sql  theme={null}
-- This is an example single line comment
```

## Multi-Line (Block) Comments

OXLA also supports multi-line comments, often referred to as block comments. These comments begin with /\* and end with \*/, allowing for multi-line explanations or temporarily disabling sections of the query.

**Syntax:**

```sql  theme={null}
/*
This is an example multi-line comment.
It can span multiple lines and is useful for providing detailed explanations.
*/
```

## Comment Placement

In OXLA, single-line comments should always be placed at the end of the line they refer to, whereas multi-line comments can be positioned anywhere within the query.

**Example - Comment on Single Line:**

```sql  theme={null}
SELECT column1, column2 -- This is an example single line comment
FROM table_name;
```

**Example - Comment on Multiple Lines:**

```sql  theme={null}
SELECT /* comment 1 */ column1, column2
FROM table_name /* comment 2 */
WHERE column3 = 42 /* comment 3 */ ;
```

## Best Practices for Commenting

To maximize the benefits of comments in OXLA queries, follow these best practices:

<CardGroup cols={2}>
  <Card title="Be Concise" icon="square-1">
    Write clear and concise comments that provide meaningful insights into the specific parts of the query.
  </Card>

  <Card title="Update Comments During Code Changes" icon="square-2">
    Whenever the query is modified, update the associated comments to reflect the changes accurately.
  </Card>

  <Card title="Avoid Over-Commenting" icon="square-3">
    While comments are helpful, excessive commenting can clutter the code and reduce.
  </Card>
</CardGroup>
