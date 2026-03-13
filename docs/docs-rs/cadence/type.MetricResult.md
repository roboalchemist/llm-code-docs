cadence
# Type Alias MetricResult 
Source 

```
pub type MetricResult<T> = Result<T, MetricError>;
```

## Aliased Type§

```
pub enum MetricResult<T> {
    Ok(T),
    Err(MetricError),
}
```

## Variants§
§1.0.0
### Ok(T)