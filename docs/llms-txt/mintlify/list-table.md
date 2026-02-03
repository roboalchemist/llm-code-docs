# Source: https://www.mintlify.com/docs/create/list-table.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Lists and tables

> Format structured data with tables and lists.

## Lists

Lists follow the official [Markdown syntax](https://www.markdownguide.org/basic-syntax/#lists-1).

### Ordered list

To create an ordered list, add numbers followed by a period before list items.

1. First item
2. Second item
3. Third item
4. Fourth item

```mdx  theme={null}
1. First item
2. Second item
3. Third item
4. Fourth item
```

### Unordered list

To create an unordered list, add dashes (`-`), asterisks (`*`), or plus signs (`+`) before list items.

* First item
* Second item
* Third item
* Fourth item

```mdx  theme={null}
- First item
- Second item
- Third item
- Fourth item
```

### Nested list

Indent list items to nest them.

* First item
* Second item
  * Additional item
  * Additional item
* Third item

```mdx  theme={null}
- First item
- Second item
  - Additional item
  - Additional item
- Third item
```

## Tables

Tables follow the official [Markdown syntax](https://www.markdownguide.org/extended-syntax/#tables).

To add a table, use three or more hyphens (`---`) to create each column's header, and use pipes (`|`) to separate each column. For compatibility, you should also add a pipe on either end of the row.

| Property | Description                           |
| -------- | ------------------------------------- |
| Name     | Full name of user                     |
| Age      | Reported age                          |
| Joined   | Whether the user joined the community |

```mdx  theme={null}
| Property | Description                           |
| -------- | ------------------------------------- |
| Name     | Full name of user                     |
| Age      | Reported age                          |
| Joined   | Whether the user joined the community |
```

### Column alignment

Use colons in the separator row to align column content:

| Left aligned | Center aligned | Right aligned |
| :----------- | :------------: | ------------: |
| Left         |     Center     |         Right |
| Text         |      Text      |          Text |

```mdx  theme={null}
| Left aligned | Center aligned | Right aligned |
| :----------- | :------------: | ------------: |
| Left         | Center         | Right         |
| Text         | Text           | Text          |
```
