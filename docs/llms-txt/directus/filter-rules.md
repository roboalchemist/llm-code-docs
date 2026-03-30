# Source: https://directus.io/docs/raw/guides/connect/filter-rules.md

# Filter Rules

> Learn about filter rules in Directus - available operators, filter syntax, relational fields, dynamic variables, logical operators, and functions parameters. Understand how to build complex filters for permissions, validations, and automations.

Filters are used in permissions, validations, and automations, as well as throughout the APIs and in extensions. All filters use standard syntax and operators which are described on this page.

## Available Operators

<table>
<thead>
  <tr>
    <th>
      Operator
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        _eq
      </code>
      
       <sup>
        <span>
          1
        </span>
      </sup>
    </td>
    
    <td>
      Equals
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _neq
      </code>
      
       <sup>
        <span>
          1
        </span>
      </sup>
    </td>
    
    <td>
      Doesn't equal
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _lt
      </code>
    </td>
    
    <td>
      Less than
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _lte
      </code>
    </td>
    
    <td>
      Less than or equal to
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _gt
      </code>
    </td>
    
    <td>
      Greater than
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _gte
      </code>
    </td>
    
    <td>
      Greater than or equal to
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _in
      </code>
    </td>
    
    <td>
      Is one of
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nin
      </code>
    </td>
    
    <td>
      Is not one of
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _null
      </code>
    </td>
    
    <td>
      Is <code>
        null
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nnull
      </code>
    </td>
    
    <td>
      Isn't <code>
        null
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _contains
      </code>
    </td>
    
    <td>
      Contains
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _ncontains
      </code>
    </td>
    
    <td>
      Doesn't contain
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _icontains
      </code>
    </td>
    
    <td>
      Contains (case-insensitive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nicontains
      </code>
    </td>
    
    <td>
      Doesn't contain (case-insensitive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _starts_with
      </code>
    </td>
    
    <td>
      Starts with
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _istarts_with
      </code>
    </td>
    
    <td>
      Starts with (case-insensitive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nstarts_with
      </code>
    </td>
    
    <td>
      Doesn't start with
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nistarts_with
      </code>
    </td>
    
    <td>
      Doesn't start with (case-insensitive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _ends_with
      </code>
    </td>
    
    <td>
      Ends with
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _iends_with
      </code>
    </td>
    
    <td>
      Ends with (case-insensitive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nends_with
      </code>
    </td>
    
    <td>
      Doesn't end with
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _niends_with
      </code>
    </td>
    
    <td>
      Doesn't end with (case-insensitive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _between
      </code>
    </td>
    
    <td>
      Is between two values (inclusive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nbetween
      </code>
    </td>
    
    <td>
      Is not between two values (inclusive)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _empty
      </code>
    </td>
    
    <td>
      Is empty (<code>
        null
      </code>
      
       or falsy)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nempty
      </code>
    </td>
    
    <td>
      Isn't empty (<code>
        null
      </code>
      
       or falsy)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _intersects
      </code>
      
       <sup>
        <span>
          2
        </span>
      </sup>
    </td>
    
    <td>
      Intersects a point
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nintersects
      </code>
      
       <sup>
        <span>
          2
        </span>
      </sup>
    </td>
    
    <td>
      Doesn't intersect a point
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _intersects_bbox
      </code>
      
       <sup>
        <span>
          2
        </span>
      </sup>
    </td>
    
    <td>
      Intersects a bounding box
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _nintersects_bbox
      </code>
      
       <sup>
        <span>
          2
        </span>
      </sup>
    </td>
    
    <td>
      Doesn't intersect a bounding box
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _regex
      </code>
      
       <sup>
        <span>
          3
        </span>
      </sup>
    </td>
    
    <td>
      Regular expression (escape backslashes)
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _some
      </code>
      
       <sup>
        <span>
          4
        </span>
      </sup>
    </td>
    
    <td>
      At least one related value is true
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        _none
      </code>
      
       <sup>
        <span>
          4
        </span>
      </sup>
    </td>
    
    <td>
      No related values are true
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

 Compared value is not strictly typed for numeric values, allowing comparisons between numbers and their string representations.<br />

<sup>
<span>

2

</span>
</sup>

 Only available on geometry fields.<br />

<sup>
<span>

3

</span>
</sup>

 Only available in validation permissions.<br />

<sup>
<span>

4

</span>
</sup>

 Only available on One to Many relationship fields.

## Filter Syntax

```json
{
  "field": {
    "operator": "value"
  }
}
```

The `field` can exist on the current collection or a relational collection.

The `operator` must be any valid filter operator such as 'equals' or 'contains'.

The `value` can be any fixed static value or one of the provided dynamic variables.

<example>

This filter checks the `title` field contains the case-sensitive substring 'Directus':

```json
{
  "title": {
    "_contains": "Directus"
  }
}
```

</example>

## Relational Fields

You can filter items based on related data by nesting field names in your query. This allows you to query items not just by their own fields, but also by values in related collections.

### Many-to-One

You can filter items with Many-to-One relations by specifying values of their respective fields.

<example>

For example, if you have an articles collection with a relational Many-to-One `author` field, you can filter articles based on the author's details—such as their `name`.

```json
{
  "author": {
      "name": {
        "_eq": "Rijk van Zanten"
      }
  }
}
```

</example>

### Many-to-Many

When using Many-to-Many relationships, a junction table will be created and the filter applies to the junction table itself. For
example, if you have a `books` collection, with a Many-to-Many relationship to authors of each book, the junction collection will
probably be named `books_authors` and have 3 fields : `id`, `books_id` and `authors_id`. To filter specific books
depending on their authors you must go through the junction table and the `authors_id` field :

```json
{
  "authors": {
    "authors_id": {
      "name": {
        "_eq": "Rijk van Zanten"
      }
    }
  }
}
```

### `_some` vs `_none` in One-to-Many and Many-to-Many

The `_some` and `_none` filter operators can be used for filtering One-to-Many and Many-to-Many relational fields in API queries. They allow you to filter items based on conditions applied to their related collections.

The `_some` operator matches items where at least one related item meets the condition.
By default, Directus will apply the `_some` operator when querying One-to-Many and Many-to-Many relational queries.

<example>

This filter matches all items where at least one related category has the name "Recipe":

```json
{
  "categories": {
    "_some": {
      "name": {
        "_eq": "Recipe"
      }
    }
  }
}
```

In the above, `categories` is the relational field in the collection. `_some` checks if at least one related category has the name "Recipe". If an item has one or more categories named "Recipe", it will be included in the result.

Since `_some` is applied by default, the below is equivalent:

```json
{
  "categories": {
    "name": {
      "_eq": "Recipe"
    }
  }
}
```

</example>

The `_none` operator matches items where none of the related items meet the condition.

<example>

This filter matches all items where none of the categories has the name "Recipe":

```json
{
  "categories": {
    "_none": {
      "name": {
        "_eq": "Recipe"
      }
    }
  }
}
```

In the above, `categories` is the relational field in the collection. `_none` checks if no related category has the name "Recipe". If an item has no categories named "Recipe", it will be included in the result.

</example>

## Dynamic Variables

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        $CURRENT_USER
      </code>
    </td>
    
    <td>
      The primary key of the currently authenticated user.
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        $CURRENT_ROLE
      </code>
    </td>
    
    <td>
      The primary key of the role for the currently authenticated user
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        $NOW
      </code>
    </td>
    
    <td>
      The current timestamp
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        $NOW(<adjustment>)
      </code>
    </td>
    
    <td>
      The current timestamp plus/minus a given distance, for example <code>
        $NOW(-1 year)
      </code>
      
      , <code>
        $NOW(+2 hours)
      </code>
    </td>
  </tr>
</tbody>
</table>

<example title="Examples">
<tabs>
<div className="pr-6" label="$CURRENT_USER">

```json
{
  "owner": {
    "_eq": "$CURRENT_USER"
  }
}
```

</div>

<div className="pr-6" label="$NOW">

```json
{
"datetime": {
  "_lte": "$NOW"
}
}
```

</div>
</tabs>
</example>

::

<example>

**Nested user and role variables in permissions**
When configuring permissions, `$CURRENT_USER` and `$CURRENT_ROLE` allow you to specify any related field, such as `$CURRENT_ROLE.name` or `$CURRENT_USER.avatar.filesize`.

</example>

## Logical Operators

You can group multiple rules using the `_and` or `_or` logical operators. Each logical operator holds an array of filter rules. Logical operators can be nested directly inside of each other, but not inside of other filter rules.

```json
{
  "_and": [
    {
      "field": {
        "operator": "value"
      }
    },
    {
      "field": {
        "operator": "value"
      }
    }
  ]
}
```

<example>

```json
{
  "_or": [
    {
      "_and": [
        {
          "user_created": {
            "_eq": "$CURRENT_USER"
          }
        },
        {
          "status": {
            "_in": ["published", "draft"]
          }
        }
      ]
    },
    {
      "_and": [
        {
          "user_created": {
            "_neq": "$CURRENT_USER"
          }
        },
        {
          "status": {
            "_in": ["published"]
          }
        }
      ]
    }
  ]
}
```

</example>

## Functions Parameters

<partial content="query-functions">



</partial>

<example>

```js
{
  _and: [
    {
      "year(published_date)": {
        _eq: 1968,
      },
    },
    {
      "month(published_date)": {
        _eq: 4,
      },
    },
  ],
},
```

</example>

## Follow Syntax

Filters allow you to query relations from collections directly.

For cases where you wish to query an indirect relation, such as `countries` to which `cities` have an M2O relation, you can use the `$FOLLOW(target-collection, relation-field)` syntax.

This is useful when there is a relation from the target collection to the current collection, but no relation field has been configured in the current collection to the target collection.

<example>

There exists both a `cities` and a `countries` collection. `cities` have an M2O relationship with `countries` via the `country_id` field. You can query `countries` via the fields of its related `cities` using the following:

```json
{
  "filter": {
    "name": "Germany",
    "$FOLLOW(cities, country_id)": {
        "name": "Berlin"
    }
  }
}
```

</example>
