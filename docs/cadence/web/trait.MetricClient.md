cadence
# Trait MetricClient 
Source 

```
pub trait MetricClient:
    Counted<i64>
    + Counted<i32>
    + Counted<u64>
    + Counted<u32>
    + CountedExt
    + Timed<u64>
    + Timed<Duration>
    + Timed<Vec<u64>>
    + Timed<Vec<Duration>>
    + Gauged<u64>
    + Gauged<f64>
    + Metered<u64>
    + Histogrammed<u64>
    + Histogrammed<f64>
    + Histogrammed<Duration>
    + Histogrammed<Vec<u64>>
    + Histogrammed<Vec<f64>>
    + Histogrammed<Vec<Duration>>
    + Distributed<u64>
    + Distributed<f64>
    + Distributed<Vec<u64>>
    + Distributed<Vec<f64>>
    + Setted<i64> { }
```

## Implementors§
Source§
### impl MetricClient for StatsdClient