cadence::ext
# Enum MetricValue 
Source 

```
pub enum MetricValue {
    Signed(i64),
    PackedSigned(Vec<i64>),
    Unsigned(u64),
    PackedUnsigned(Vec<u64>),
    Float(f64),
    PackedFloat(Vec<f64>),
}
```

## Variants§
§
### Signed(i64)