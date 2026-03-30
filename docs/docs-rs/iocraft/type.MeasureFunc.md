iocraft
# Type Alias MeasureFunc 
Source 

```
pub type MeasureFunc = Box<dyn Fn(Size<Option<f32>>, Size<AvailableSpace>, &Style) -> Size<f32> + Send>;
```

## Aliased Type§

```
pub struct MeasureFunc(/* private fields */);
```