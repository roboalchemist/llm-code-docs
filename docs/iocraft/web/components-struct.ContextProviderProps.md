iocraft::components
# Struct ContextProviderProps 
Source 

```
#[non_exhaustive]pub struct ContextProviderProps<'a> {
    pub children: Vec<AnyElement<'a>>,
    pub value: Option<Context<'a>>,
}
```

## Fields (Non-exhaustive)§
§`children: Vec<AnyElement<'a>>`

The children of the component.
§`value: Option<Context<'a>>`

The context to provide to the children.

## Trait Implementations§