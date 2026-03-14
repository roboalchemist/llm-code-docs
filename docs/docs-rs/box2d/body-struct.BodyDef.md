box2d::body
# Struct BodyDef 
Source 

```
pub struct BodyDef {
    pub shape: Shape,
    pub body_type: BodyType,
    pub position: Vec2,
    pub velocity: Vec2,
    pub restitution: f32,
    pub mass: f32,
    pub gravity_scale: f32,
}
```

## Fields§
§`shape: Shape`§`body_type: BodyType`§`position: Vec2`§`velocity: Vec2`§`restitution: f32`§`mass: f32`§`gravity_scale: f32`
## Auto Trait Implementations§
§
### impl Freeze for BodyDef