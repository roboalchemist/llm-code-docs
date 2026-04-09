iced
# Type Alias Renderer 
Source 

```
pub type Renderer = Renderer<Renderer, Renderer>;
```

## Aliased Type§

```
pub enum Renderer {
    Primary(Renderer),
    Secondary(Renderer),
}
```

## Variants§
§
### Primary(Renderer)