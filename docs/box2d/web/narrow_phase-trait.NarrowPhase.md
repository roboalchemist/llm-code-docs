box2d::narrow_phase
# Trait NarrowPhase 
Source 

```
pub trait NarrowPhase {
    // Required method
    fn run(&self, results: &Vec<(Body, Body)>) -> Vec<ColliderResult>;
}
```

## Required Methods§
Source
#### fn run(&self, results: &Vec<(Body, Body)>) -> Vec<ColliderResult>