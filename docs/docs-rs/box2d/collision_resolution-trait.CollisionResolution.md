box2d::collision_resolution
# Trait CollisionResolution 
Source 

```
pub trait CollisionResolution {
    // Required method
    fn resolve_collisions(&mut self, manifold: &Vec<Manifold>);
}
```

## Required Methods§
Source
#### fn resolve_collisions(&mut self, manifold: &Vec<Manifold>)