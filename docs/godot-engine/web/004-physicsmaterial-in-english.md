# PhysicsMaterial in English

# PhysicsMaterial

Inherits:Resource<RefCounted<Object
Holds physics-related properties of a surface, namely its roughness and bounciness.

## Description

Holds physics-related properties of a surface, namely its roughness and bounciness. This class is used to apply these properties to a physics body.

## Properties

| bool | absorbent | false |
|---|---|---|
| float | bounce | 0.0 |
| float | friction | 1.0 |
| bool | rough | false |

bool
absorbent
false
float
bounce
float
friction
bool
rough
false

## Property Descriptions

boolabsorbent=false🔗

- voidset_absorbent(value:bool)
voidset_absorbent(value:bool)
- boolis_absorbent()
boolis_absorbent()
Iftrue, subtracts the bounciness from the colliding object's bounciness instead of adding it.
floatbounce=0.0🔗
- voidset_bounce(value:float)
voidset_bounce(value:float)
- floatget_bounce()
floatget_bounce()
The body's bounciness. Values range from0(no bounce) to1(full bounciness).
Note:Even withbounceset to1.0, some energy will be lost over time due to linear and angular damping. To have a physics body that preserves all its energy over time, setbounceto1.0, the body's linear damp mode toReplace(if applicable), its linear damp to0.0, its angular damp mode toReplace(if applicable), and its angular damp to0.0.
floatfriction=1.0🔗
- voidset_friction(value:float)
voidset_friction(value:float)
- floatget_friction()
floatget_friction()
The body's friction. Values range from0(frictionless) to1(maximum friction).
boolrough=false🔗
- voidset_rough(value:bool)
voidset_rough(value:bool)
- boolis_rough()
boolis_rough()
Iftrue, the physics engine will use the friction of the object marked as "rough" when two objects collide. Iffalse, the physics engine will use the lowest friction of all colliding objects instead. Iftruefor both colliding objects, the physics engine will use the highest friction.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
