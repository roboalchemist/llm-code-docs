image
# Struct Limits 
Source 

```
#[non_exhaustive]pub struct Limits {
    pub max_image_width: Option<u32>,
    pub max_image_height: Option<u32>,
    pub max_alloc: Option<u64>,
}
```

## Fields (Non-exhaustive)§
§`max_image_width: Option<u32>`

The maximum allowed image width. This limit is strict. The default is no limit.
§`max_image_height: Option<u32>`

The maximum allowed image height. This limit is strict. The default is no limit.
§`max_alloc: Option<u64>`

The maximum allowed sum of allocations allocated by the decoder at any one time excluding
allocator overhead. This limit is non-strict by default and some decoders may ignore it.
The bytes required to store the output image count towards this value. The default is
512MiB.

## Implementations§