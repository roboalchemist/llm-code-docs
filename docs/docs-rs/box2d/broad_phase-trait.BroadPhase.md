box2d::broad_phase
# Trait BroadPhase 
Source 

```
pub trait BroadPhase {
    // Required method
    fn run(&self, bodies: &Vec<Body>) -> Vec<(Body, Body)>;
}
```

## Required Methods§
Source
#### fn run(&self, bodies: &Vec<Body>) -> Vec<(Body, Body)>