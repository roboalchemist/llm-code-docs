# Source: https://docs.pinot.apache.org/release-0.9.0/basics/indexing/range-index.md

# Source: https://docs.pinot.apache.org/release-0.10.0/basics/indexing/range-index.md

# Source: https://docs.pinot.apache.org/release-0.11.0/basics/indexing/range-index.md

# Source: https://docs.pinot.apache.org/release-0.12.0/basics/indexing/range-index.md

# Source: https://docs.pinot.apache.org/release-0.12.1/basics/indexing/range-index.md

# Source: https://docs.pinot.apache.org/release-1.0.0/basics/indexing/range-index.md

# Source: https://docs.pinot.apache.org/release-1.1.0/basics/indexing/range-index.md

# Source: https://docs.pinot.apache.org/release-1.2.0/basics/indexing/range-index.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/indexing/range-index.md

# Source: https://docs.pinot.apache.org/release-1.4.0/basics/indexing/range-index.md

# Source: https://docs.pinot.apache.org/basics/indexing/range-index.md

# Range index

Range indexing allows you to get better performance for queries that involve filtering over a range.

It would be useful for a query like the following:

```sql
SELECT COUNT(*) 
FROM baseballStats 
WHERE hits > 11
```

A range index is a variant of an [inverted index](https://docs.pinot.apache.org/basics/indexing/inverted-index), where instead of creating a mapping from values to columns, we create mapping of a range of values to columns. You can use the range index by setting the following config in the [table configuration](https://docs.pinot.apache.org/configuration-reference/table).

```javascript
{
    "tableIndexConfig": {
        "rangeIndexColumns": [
            "column_name",
            ...
        ],
        ...
    }
}
```

Range index is supported for dictionary encoded columns of any type as well as raw encoded columns of a numeric type. Note that the range index can also be used on a dictionary encoded time column using `STRING` type, since Pinot only supports datetime formats that are in lexicographical order.

{% hint style="info" %}
A good thumb rule is to use a range index when you want to apply range predicates on metric columns that have a very large number of unique values. This is because using an inverted index for such columns will create a very large index that is inefficient in terms of storage and performance.
{% endhint %}
