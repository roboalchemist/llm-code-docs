image::flat
# Struct SampleLayout 
Source 

```
#[repr(C)]pub struct SampleLayout {
    pub channels: u8,
    pub channel_stride: usize,
    pub width: u32,
    pub width_stride: usize,
    pub height: u32,
    pub height_stride: usize,
}
```

## Fields§
§`channels: u8`

The number of channels in the color representation of the image.
§`channel_stride: usize`

Add this to an index to get to the sample in the next channel.
§`width: u32`

The width of the represented image.
§`width_stride: usize`

Add this to an index to get to the next sample in x-direction.
§`height: u32`

The height of the represented image.
§`height_stride: usize`

Add this to an index to get to the next sample in y-direction.

## Implementations§