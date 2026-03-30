flamescope::model
# Enum Profile 
Source 

```
pub enum Profile {
    Sampled {
        name: Cow<'static, str>,
        unit: ValueUnit,
        start_value: u64,
        end_value: u64,
        samples: Vec<Vec<usize>>,
        weights: Vec<u64>,
    },
    Evented {
        name: Cow<'static, str>,
        unit: ValueUnit,
        start_value: u64,
        end_value: u64,
        events: Vec<Event>,
    },
}
```

## Variants§
§
### Sampled