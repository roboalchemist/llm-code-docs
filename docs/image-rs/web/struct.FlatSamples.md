image
# Struct FlatSamples 
Source 

```
pub struct FlatSamples<Buffer> {
    pub samples: Buffer,
    pub layout: SampleLayout,
    pub color_hint: Option<ColorType>,
}
```

## Fields§
§`samples: Buffer`

Underlying linear container holding sample values.
§`layout: SampleLayout`

A `repr(C)` description of the layout of buffer samples.
§`color_hint: Option<ColorType>`

Supplementary color information.

You may keep this as `None` in most cases. This is NOT checked in `View` or other
converters. It is intended mainly as a way for types that convert to this buffer type to
attach their otherwise static color information. A dynamic image representation could
however use this to resolve representational ambiguities such as the order of RGB channels.

## Implementations§