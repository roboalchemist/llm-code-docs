# Coding Standards

Orpheus Development Papers - Coding Standards

This document is a work-in-progress and is subject to change.

Note: The standards defined in this document will likely differ from
what is actually seen in the Gazelle code. This document is the first
step in properly enforcing coding standards throughout the project.

## Table of Contents

1. Linting
2. File Formatting
3. Code Styling
   3.1 PHP and JavaScript
   3.2 CSS
   3.3 SQL
4. Naming Conventions
   4.1 Function names
   4.2 Variable names
   4.3 Class names
   4.4 SQL names
   4.5 Miscellaneous names
5. Comments
6. User Interface
7. Examples

## Linting

To help ensure adherence to this guide, we have setup linting for PHP and SCSS code.
They can be run through make:

```bash
make lint-php
make lint-css
```

These steps are also run on committing.

## File Formatting

- Spaces shall always be used for indentation. 4-space indents are used.
- Files shall be encoded in UTF-8.
- Files shall always use Unix-style line endings (LF). The program `dos2unix`
  will take care of this for you if you have files that use Windows-style
  line endings (CR+LF) or old Mac-style line endings (CR).
- Files must end with a new-line character. Use a proper editor that
  performs this automatically.
- File names for PHP, CSS, and JavaScript files may not contain spaces.

## Code Styling

### PHP and JavaScript

- All statement blocks, including functions, shall have the opening brace
  at the end of the same line with a space before the brace. (K&R style,
  with the exception of the opening brace in function definitions.)
- There shall be a space between a control structure statement (e.g. `if`,
  `elseif` in PHP, `for`) and the following parenthesis.
- PHP files shall not end with a trailing `?>`.
- There shall be a space around conditional operators.
- When using ternary operators, spaces shall be used around the operators.
- For PHP conditional blocks, `elseif` is to be used instead of `else if`.
- In loops and conditional blocks, there shall be braces even if there is
  only one statement.
- In loops and conditional blocks, the statement(s) shall be placed on
  separate lines.
- When opening a PHP statement, `<?php` shall be used instead of `<?`.
  Short tags are forbidden. When using `<?= ... ?>` there shall be spaces
  at either end of the block (so that it is easy to grab the contents in
  vim with e.g. `yE`).
- When declaring an array, the short syntax `[]` shall be used, instead
  of the longer `array()`.
- Any syntax as of PHP 7.3 is permitted. Trailing commas in lists are
  allowed and recommended.
- Use indents as appropriate to aid readability. When functions with
  many parameters are laid out over multiple lines, the subsequent lines
  are indented 4 characters (and not to the opening parenthesis above):

  ```php
  $result = someFunction(
      anotherFunc(1, 2, 3),
      yetAnotherFunc(4, 5 6),
  );
  ```

- Switch cases in index files shall not contain substantial code. The use
  of include statements is acceptable.
- When declaring JavaScript variables, `var` shall always be used.
- When manually type casting, whitespace should not be used between the
  cast operator and the variable.

### CSS

- `property: value;` pairs shall be separated by a space, and the value
  shall be followed by a semi-colon.
- Multiple, related CSS selectors with the same declarations shall appear
  on multiple lines to improve readability.
- The opening brace shall be on the same line as the last related
  selector with a space between the selector and the brace.

### SQL

- Long SQL queries shall be separated on multiple lines.
- Short SQL queries may be on a single line.
- All SQL keywords shall be uppercase. `count()`, `sum()`, `now()` are not
  keywords, they are functions.
- All queries that have external inputs shall use placeholders. Queries
  with arbitrary numbers of external inputs should use `placeholders()`.
- Aliases shall be used to refer to any columns whenever multiple tables are
  joined in an SQL query. They shall use the `tbl_name AS alias_name` syntax.
  Table aliases must be used for single-table queries (because one day a
  second table will be added to the query). Table aliases can be constructed
  from the first letter of each word in the name (`users_main` becomes `um`).
- The primary SQL keywords should be at the same indentation level:
  `SELECT`, `FROM`, `INNER JOIN`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`.
- The SQL keywords `INNER JOIN`, `RIGHT JOIN`, `LEFT JOIN` are at the same
  level as the `SELECT` statement. The `JOIN` abbreviation for `INNER JOIN`
  is not accepted. `NATURAL JOIN` is forbidden.
- Join clauses must be parenthesized: `a INNER JOIN b IN (a.foo = b.kek)`.
  When column names match, `USING` is preferred: `a INNER JOIN b USING (kek)`.
- The SQL keyword `AND` must be indented once from the `WHERE` (and similar)
  statements.
- `UPDATE` that updates multiple columns have one column per line. The `SET`
  clause is kept on the same line as the `UPDATE` statement, except in the
  case of a multi-table update against a derived table, where it sits on a
  line by itself.
- The "not equal to" operator `!=` must be used instead of `<>`.

### Naming Conventions for New Tables

(Legacy tables are exempt.)

- Names are always singular.
- The primary key is named `<table>_id`.
- Zero dates are forbidden.
- Numeric enums (`'0'`, `'1'`, `'2'`) are forbidden. Use descriptive names.

## Naming Conventions

Function, variable, and class names shall always be descriptive.

### Function Names

- PHP function names shall be written in `camelCase`.
- JavaScript function names shall be written in `camelCase` with a leading
  lowercase letter.

### Variable Names

- PHP variable names shall be written in `camelCase`.
- JavaScript global-scope variables shall be written in `camelCase` with a
  leading lowercase letter.
- JavaScript local-scope variables shall be written in
  `lowercase_with_underscores`.

### Class Names

- PHP class names shall be written in `CamelCase` with a leading uppercase
  letter.
- PHP class constants shall be written in `CamelCase` with a leading
  uppercase letter.
- PHP global constants shall be written in `ALL_CAPS`.
- PHP constants `true`, `false`, and `null` shall be written in all lowercase.

### SQL Names

- All SQL keywords shall be written in `UPPERCASE`.
- All SQL table names shall be written in `lowercase_with_underscores`.
- All legacy SQL column names shall be written in `CamelCase` with a leading
  uppercase letter.
- All new column names shall be written in `lowercase_with_underscores`.
- All automatically-incremented ID columns shall be named `<table>_id`,
  while other id columns shall have names like `collage_id`, `user_id`, etc.

## Comments

- Use C89-style `/* ... */` comments for multi-line comments.
- Use C99-style `// ...` comments for single-line comments.

## User Interface

- All button labels shall use sentence case.
- All table headings shall use sentence case.
- All text-based buttons shall use the `brackets` CSS class.
- Use common sense for design-related code. Microsoft's UI design guidelines
  explain when certain form input controls should be used over others to
  provide a familiar and intuitive interface. Refer to the following links
  for the most likely issues to encounter in web design:

  - <http://msdn.microsoft.com/en-us/library/windows/desktop/aa511452.aspx>
  - <http://msdn.microsoft.com/en-us/library/windows/desktop/aa511453.aspx>
  - <http://msdn.microsoft.com/en-us/library/windows/desktop/aa511488.aspx>
  - <http://msdn.microsoft.com/en-us/library/windows/desktop/aa511494.aspx>

## Examples

### PHP Examples

```php
if ($foo >= 0) {
    $someString = "this is a string $diffString with more text";
} elseif ($foo == 0) {
    // other things happen
} else {
    // more magic
}

function worksMagic($foo, $bar) {
    return $foo;
}

echo ($foo == true ? 'foo is true' : 'foo is false');

if ($foo == true) {
    // magic happens
}

/*
 * This is a good, multi-line comment.
 *
 * Please comment your code!
 */

// This is a good, single-line comment.
```

### CSS Examples

```html
<a href="foobar.php" style="font-weight: bold;">link text</a>
```

```css
.spellcheck {
    margin: 10px 0;
    font-size: 1.25em;
    font-weight: bold;
}

.linkbox .brackets:before,
.linkbox .brackets:after,
.top10_quantity_links .brackets:before,
.top10_quantity_links .brackets:after {
    color: #757575;
}
```

### SQL Examples

```sql
SELECT
    r.ID, e.EditionID, r.Title, r.Year, r.CatalogueNumber,
    l.Name AS Label, r.LabelID, r.Image, r.MusicBrainzID
FROM releases AS r
INNER JOIN editions AS e ON (e.ReleaseID = r.ID)
LEFT JOIN labels AS l ON (l.ID = r.LabelID)
WHERE r.ID IN (?, ?, ?)
ORDER BY e.EditionID, r.Year ASC
```

```sql
SELECT c.ID, c.Subject, cu.Unread, cu.Sticky,
    cu.ForwardedTo, cu2.UserID, cu.ReceivedDate AS Date
FROM pm_conversations AS c
LEFT JOIN pm_conversations_users AS cu
    ON (cu.ConvID = c.ID AND cu.UserID = '1')
LEFT JOIN pm_conversations_users AS cu2
    ON (cu2.ConvID = c.ID AND cu2.UserID != '1' AND cu2.ForwardedTo = 0)
LEFT JOIN users_main AS um ON (um.ID = cu2.UserID)
WHERE um.Username LIKE 'test'
    AND cu.InInbox = '1'
GROUP BY c.ID
ORDER BY cu.Sticky, Date DESC
LIMIT 25
```

```sql
SELECT RequestID AS ID, UserID FROM bookmarks_requests br
```
