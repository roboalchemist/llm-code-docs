box2d::collision::collider
# Trait Collider 
Source 

```
pub trait Collider {
    // Required methods
    fn new(pair: (Body, Body)) -> Self;
    fn pair(&self) -> (Body, Body);
    fn colliding(&self) -> ColliderResult;
}
```

## Required Methods§
Source
#### fn new(pair: (Body, Body)) -> Self