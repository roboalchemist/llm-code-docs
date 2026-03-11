# Source: https://uptrace.dev/raw/features/querying/searching.md

# Searching Spans and Logs

> Search spans and logs using natural syntax with word filters, AND OR pipes, quoted phrases, and scoped field operators.

In addition to the SQL-like [query language](/features/querying/spans), Uptrace allows you to search spans and logs using a more concise and natural query language that makes finding specific data faster and more intuitive.

![Searching](/features/querying-spans/searching.png)

## Word Filters

The simplest query is a single word that must be found within the [search scope](#search-scope).

**Example:** The query `error` will match the following logs:

```text
err
error
ERROR
ERRor
an error just occurred
```

### Multiple Words (AND Logic)

When your query contains multiple words separated by spaces, **all words** must be found in the search scope.

**Example:** The query `error select` will match:

```text
error select
select error
an error has occurred when executing a select query
```

### Multiple Words (OR Logic)

To search for logs containing **any** of multiple words, separate them with the pipe character (`|`).

**Example:** The query `select|update` will match:

```text
select
update
select update
```

## Phrase Filters

To search for logs containing an exact phrase, enclose the phrase in double quotes (`"`). The phrase can contain any characters, including spaces, punctuation, and special characters.

**Example:** The query `"select query"` will match:

```text
an error has occurred when executing a select query
select query
```

But will **not** match:

```text
query select
selecting a query
```

## Regular Expression Filters

To search using regular expressions, prefix your expression with the tilde character (`~`).

**Example:** The query `~err` will match:

```text
err
error
an_err
some error
```

### Regular Expressions with Spaces

If your regular expression contains spaces, enclose it in backticks (```):

**Example:**

```text
~`\d{4} \w+`
```

## Negative Filters

To exclude logs containing specific words or phrases, prefix the term with a minus sign (`-`).

**Example:** The query `error -ssh` will find error logs that do **not** contain the word `ssh`.

### Combining Filters

You can combine multiple filter types in a single query:

**Example:** `error "database connection" -timeout ~\d{3}` will find logs that:

- Contain the word "error"
- Contain the exact phrase "database connection"
- Do not contain the word "timeout"
- Match the regular expression `\d{3}` (three digits)

## Search Scope

The search scope defines which attributes Uptrace searches when filtering spans and logs. By default, the search scope corresponds to your current grouping expression.

### Default Search Scopes

<table>
<thead>
  <tr>
    <th>
      Grouping Expression
    </th>
    
    <th>
      Search Scope
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        group by _group_id
      </code>
    </td>
    
    <td>
      <code>
        _display_name
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        group by service_name, host_name
      </code>
    </td>
    
    <td>
      <code>
        service_name
      </code>
      
      , <code>
        host_name
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        group by _group_id, service_name
      </code>
    </td>
    
    <td>
      <code>
        _display_name
      </code>
      
      , <code>
        service_name
      </code>
    </td>
  </tr>
</tbody>
</table>

### Custom Search Scopes

You can specify custom search scopes for any filter type by using the `attribute:value` syntax:

**Examples:**

```text
host_name:host1
service_name:"hello world"
~span_name:user.*
message:-"connection failed"
```

This allows you to search specific attributes regardless of your current grouping configuration.

## Filter Syntax Reference

<table>
<thead>
  <tr>
    <th>
      Filter Type
    </th>
    
    <th>
      Syntax
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Example
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      Word
    </td>
    
    <td>
      <code>
        word
      </code>
    </td>
    
    <td>
      Matches logs containing the word
    </td>
    
    <td>
      <code>
        error
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Multiple words (AND)
    </td>
    
    <td>
      <code>
        word1 word2
      </code>
    </td>
    
    <td>
      All words must be present
    </td>
    
    <td>
      <code>
        error database
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Multiple words (OR)
    </td>
    
    <td>
      <code>
        word1|word2
      </code>
    </td>
    
    <td>
      Any word must be present
    </td>
    
    <td>
      <code>
        error|warning
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Phrase
    </td>
    
    <td>
      <code>
        "phrase"
      </code>
    </td>
    
    <td>
      Exact phrase match
    </td>
    
    <td>
      <code>
        "connection timeout"
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Regular expression
    </td>
    
    <td>
      <code>
        ~pattern
      </code>
    </td>
    
    <td>
      Regex pattern match
    </td>
    
    <td>
      <code>
        ~\d{3}-\d{3}-\d{4}
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Regular expression with spaces
    </td>
    
    <td>
      <code>
        ~`pattern`
      </code>
    </td>
    
    <td>
      Regex with spaces
    </td>
    
    <td>
      <code>
        ~`error \d+`
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Negative filter
    </td>
    
    <td>
      <code>
        -term
      </code>
    </td>
    
    <td>
      Excludes logs with term
    </td>
    
    <td>
      <code>
        -debug
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      Scoped filter
    </td>
    
    <td>
      <code>
        attribute:value
      </code>
    </td>
    
    <td>
      Search specific attribute
    </td>
    
    <td>
      <code>
        host_name:prod-server
      </code>
    </td>
  </tr>
</tbody>
</table>

## Tips for Effective Searching

- **Case insensitive**: All text searches are case-insensitive by default
- **Partial matching**: Word filters match partial words (e.g., `err` matches `error`)
- **Combine filters**: Use multiple filter types together for precise results
- **Use quotes**: Always quote phrases and values containing spaces or special characters
- **Escape special characters**: In regex patterns, remember to escape special characters as needed
