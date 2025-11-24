# Source: https://flatfile.com/docs/reference/ffql.md

# Flatfile Query Language

> Learn how to filter data in Sheets with FFQL.

FFQL (Flatfile Query Language) is Flatfile's custom query language used for filtering data in [Sheets](/core-concepts/blueprints). It's logical, composable, and human-readable.

For example, to find records where the first name is "Bender":

```
first_name eq Bender
```

## Syntax

The basic syntax of FFQL is:

```
[field name] <operator> <value>
```

### Field Name

`field name` is optional and excluding a field name will search across all fields. For example: `eq "Planet Express"` will search across all fields for that value.

`field name` can be the field key or the field label.

Labels or values with spaces should be wrapped in quotes. For example: `name eq "Bender Rodriguez"`, or `"First Name" eq Bender`.

### Operators

FFQL operators are:

* `eq` - Equals (exact match)
* `ne` - Not Equal
* `lt` - Less Than
* `gt` - Greater Than
* `lte` - Less Than or Equal To
* `gte` - Greater Than or Equal To
* `like` - (Case Sensitive) Like
* `ilike` - (Case Insensitive) Like
* `contains` - Contains (for columns of type `string-list` and `enum-list`)

Both `like` and `ilike` support the following wildcards:

* `%` - Matches any number of characters
* `_` - Matches a single character

So, for instance, `like "Bender%"` would match "Bender Rodriguez" and "Bender Bending Rodriguez".

### Logical Operators

FFQL supports two logical operators:

* `and` - Returns rows meeting both conditions
* `or` - Returns rows meeting either conditions (inclusive)

### The `is` Operator

You can query for message statuses by using the `is` operator. For example: `is error` returns all the rows in an `error` state. `is valid` returns all the rows in a `valid` state. `first_name is error` returns the rows where First Name is in an `error` state.

### Escaping Quotes and Backslashes

When you need to include quotes or backslashes within quoted values, you can escape them using a backslash (`\`). Here are examples of how escaping works:

| Query              | Value           |
| ------------------ | --------------- |
| `"hello \" world"` | `hello " world` |
| `'hello \' world'` | `hello ' world` |
| `"hello world \\"` | `hello world \` |
| `"hello \ world"`  | `hello \ world` |
| `"hello \\ world"` | `hello \ world` |

For example, to search for a field containing a quote:

```
first_name eq "John \"Johnny\" Doe"
```

This would match a first name value of: `John "Johnny" Doe`

***

## Constructing Queries

Complex queries are possible using a combination of operators:

```
(
    email like "@gmail.com"
    and (
        "Subscription Status" eq "On-Hold"
        or "Subscription Status" eq "Pending"
    )
    and login_attempts gte 5
)
or is warning
```

This query would return all the rows that:

1. Have a Gmail email address,
2. Have a Subscription Status of "On-Hold" or "Pending",
3. And have more than 5 login attempts.

It will also include any rows that have a "Warning" message status.

***

## Usage

### Via search bar

From the search bar in a Workbook, prepend **filter:** to your FFQL query.

**type in search bar**

```
filter: first_name eq Bender and last_name eq Rodriguez
```

### Via API

FFQL queries can be passed to any [REST API](https://reference.flatfile.com/overview/welcome) endpoint that supports the `q` parameter.

Here's an example **cURL** request using the `sheets/<sheetId>/records` endpoint:

**Shell / cURL**

```bash
curl --location 'https://platform.flatfile.com/api/sheets/us_sh_12345678/records?q="Subscription Status" eq "On-Hold" or "Subscription Status" eq "Pending"' \
    --header 'Accept: */*' \
    --header 'Authorization: Bearer <bearer token>'
```

Make sure to [encode](https://en.wikipedia.org/wiki/URL_encoding) percent characters if you use them.
