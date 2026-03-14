druid

# Struct PaintCtx

Source

```
pub struct PaintCtx<'a, 'b, 'c> {
    pub render_ctx: &'a mut Piet<'c>,
    /* private fields */
}
```

## Fields§

§`render_ctx: &'a mut Piet<'c>`

The render context for actually painting.

## Implementations§
