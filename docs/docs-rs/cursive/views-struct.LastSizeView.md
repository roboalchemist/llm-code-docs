cursive::views
# Struct LastSizeView 
Source 

```
pub struct LastSizeView<T> {
    pub view: T,
    pub size: XY<usize>,
}
```

## Fields§
§`view: T`

Wrapped view.
§`size: XY<usize>`

Cached size from the last layout() call.

## Implementations§