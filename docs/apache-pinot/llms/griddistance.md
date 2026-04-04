# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/griddistance.md

# Source: https://docs.pinot.apache.org/functions-1/griddistance.md

# GridDistance

Computes the H3 grid distance between two H3 indexes.

## Signature

> h3\_gridDistance(h3Index1, h3Index2)

## Usage Examples

```sql
SELECT h3_gridDistance(0x8928308280fffff, 0x8928308283fffff) AS distance
FROM ignoreMe;
```

| distance |
| -------- |
| 2        |

{% hint style="info" %}
The H3 grid distance is only defined for H3 indexes of the same resolution. If the indexes are not at the same resolution, the function will return an error.
{% endhint %}
