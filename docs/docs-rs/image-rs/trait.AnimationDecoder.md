image
# Trait AnimationDecoder 
Source 

```
pub trait AnimationDecoder<'a> {
    // Required method
    fn into_frames(self) -> Frames<'a> ⓘ;

    // Provided method
    fn loop_count(&self) -> LoopCount { ... }
}
```

## Required Methods§