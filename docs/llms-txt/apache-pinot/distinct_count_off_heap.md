# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinct_count_off_heap.md

# Source: https://docs.pinot.apache.org/functions-1/distinct_count_off_heap.md

# DISTINCT\_COUNT\_OFF\_HEAP

Returns the count of distinct values. The values are stored using off-heap memory.

## Signature

> DISTINCT\_COUNT\_OFF\_HEAP(col\[, params])

* `col` (required): Name of the column to aggregate on.
* `params` (optional): Semicolon-separated parameter key-value pairs:
  * `initialCapacity`: The initial capacity of the set for non-dictionary-encoded case (default *10000*).
  * `hashbits`: Number of bits for *murmur3*: *32*/*64*/*128* (default *64*)
* Example: `DISTINCT_COUNT_OFF_HEAP(col, 'initialCapacity=100000;hashbits=128')`

## Note

* For variable length data types such as `STRING` and `BYTES`, *murmur3* hash values are used to represent the values.
* Currently it only supports aggregate without group-by. For MV column, it only supports fixes lengh types.
