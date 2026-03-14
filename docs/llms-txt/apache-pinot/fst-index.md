# Source: https://docs.pinot.apache.org/release-1.2.0/basics/indexing/fst-index.md

# Source: https://docs.pinot.apache.org/release-1.3.0/basics/indexing/fst-index.md

# Source: https://docs.pinot.apache.org/release-1.4.0/basics/indexing/fst-index.md

# Source: https://docs.pinot.apache.org/basics/indexing/fst-index.md

# FST index

The FST index supports regex queries on text. Decreases on-disk index by 4-6 times.

* Only supports regex queries
* Only supported on stored or completed Pinot segments (no consuming segments).
* Only supported on dictionary-encoded columns.
* Works better for prefix queries

{% hint style="info" %}
**Note:** Lucene is case sensitive as such when using FST index based column(s) in query, user needs to ensure this is taken into account. For e.g `Select * from table T where colA LIKE %Value%` which has a FST index on colA will only return rows containing string "Value" but not "value".
{% endhint %}

For more information on the FST construction and code, see [Lucene documentation](https://lucene.apache.org/core/9_10_0/core/org/apache/lucene/util/fst/FST.html).

## Enable the FST index

To enable the FST index on a dictionary-encoded column, include the following configuration:

```javascript
"fieldConfigList":[
{
"name":"text_col_1",
"encodingType":"DICTIONARY",
"indexType":"FST"
}
]
```

The FST index generates one FST index file (`.lucene.fst)`. If the inverted index is enabled, this is further able to take advantage of that.

## Case-insensitive FST index (IFST)

The case-insensitive FST index (IFST) provides the same functionality as the standard FST index but with case-insensitive matching. This eliminates the need to handle case sensitivity manually in queries.

* Supports case-insensitive regex queries
* Only supported on stored or completed Pinot segments (no consuming segments).
* Only supported on dictionary-encoded columns.
* Works better for prefix queries with case-insensitive matching

### Enable the case-insensitive FST index

To enable the case-insensitive FST index on a dictionary-encoded column, include the following configuration:

```javascript
{
  "fieldConfigList": [
    {
      "name": "notes",
      "encodingType": "DICTIONARY",
      "indexes": {
        "ifst": {
          "enabled": true
        }
      }
    }
  ]
}
```

The case-insensitive FST index generates one FST index file (`.lucene.ifst`) and provides case-insensitive matching for regex queries without requiring manual case handling in your queries.

For more information about enabling the FST index, see ways to [enable indexes](https://docs.pinot.apache.org/basics/indexing/..#enabling-indexes).
