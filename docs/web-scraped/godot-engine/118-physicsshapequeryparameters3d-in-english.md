# PhysicsShapeQueryParameters3D in English

# PhysicsShapeQueryParameters3D
Inherits:RefCounted<Object
Provides parameters forPhysicsDirectSpaceState3D's methods.

## Description
By changing various properties of this object, such as the shape, you can configure the parameters forPhysicsDirectSpaceState3D's methods.

## Properties

| bool | collide_with_areas | false |
|---|---|---|
| bool | collide_with_bodies | true |
| int | collision_mask | 4294967295 |
| Array[RID] | exclude | [] |
| float | margin | 0.0 |
| Vector3 | motion | Vector3(0,0,0) |
| Resource | shape |  |
| RID | shape_rid | RID() |
| Transform3D | transform | Transform3D(1,0,0,0,1,0,0,0,1,0,0,0) |

bool
collide_with_areas
false
bool
collide_with_bodies
true
collision_mask
4294967295
Array[RID]
exclude
float
margin
Vector3
motion
Vector3(0,0,0)
Resource
shape
shape_rid
RID()
Transform3D
transform
Transform3D(1,0,0,0,1,0,0,0,1,0,0,0)

## Property Descriptions
boolcollide_with_areas=false🔗
- voidset_collide_with_areas(value:bool)
voidset_collide_with_areas(value:bool)
- boolis_collide_with_areas_enabled()
boolis_collide_with_areas_enabled()
Iftrue, the query will takeArea3Ds into account.
boolcollide_with_bodies=true🔗
- voidset_collide_with_bodies(value:bool)
voidset_collide_with_bodies(value:bool)
- boolis_collide_with_bodies_enabled()
boolis_collide_with_bodies_enabled()
Iftrue, the query will takePhysicsBody3Ds into account.
intcollision_mask=4294967295🔗
- voidset_collision_mask(value:int)
voidset_collision_mask(value:int)
- intget_collision_mask()
intget_collision_mask()
The physics layers the query will detect (as a bitmask). By default, all collision layers are detected. SeeCollision layers and masksin the documentation for more information.
Array[RID]exclude=[]🔗
- voidset_exclude(value:Array[RID])
voidset_exclude(value:Array[RID])
- Array[RID]get_exclude()
Array[RID]get_exclude()
The list of objectRIDs that will be excluded from collisions. UseCollisionObject3D.get_rid()to get theRIDassociated with aCollisionObject3D-derived node.
Note:The returned array is copied and any changes to it will not update the original property value. To update the value you need to modify the returned array, and then assign it to the property again.
floatmargin=0.0🔗
- voidset_margin(value:float)
voidset_margin(value:float)
- floatget_margin()
floatget_margin()
The collision margin for the shape.
Vector3motion=Vector3(0,0,0)🔗
- voidset_motion(value:Vector3)
voidset_motion(value:Vector3)
- Vector3get_motion()
Vector3get_motion()
The motion of the shape being queried for.
Resourceshape🔗
- voidset_shape(value:Resource)
voidset_shape(value:Resource)
- Resourceget_shape()
Resourceget_shape()
TheShape3Dthat will be used for collision/intersection queries. This stores the actual reference which avoids the shape to be released while being used for queries, so always prefer using this overshape_rid.
RIDshape_rid=RID()🔗
- voidset_shape_rid(value:RID)
voidset_shape_rid(value:RID)
- RIDget_shape_rid()
RIDget_shape_rid()
The queried shape'sRIDthat will be used for collision/intersection queries. Use this overshapeif you want to optimize for performance using the Servers API:
```
var shape_rid = PhysicsServer3D.sphere_shape_create()
var radius = 2.0
PhysicsServer3D.shape_set_data(shape_rid, radius)

var params = PhysicsShapeQueryParameters3D.new()
params.shape_rid = shape_rid

# Execute physics queries here...

# Release the shape when done with physics queries.
PhysicsServer3D.free_rid(shape_rid)
```
```
RID shapeRid = PhysicsServer3D.SphereShapeCreate();
float radius = 2.0f;
PhysicsServer3D.ShapeSetData(shapeRid, radius);

var params = new PhysicsShapeQueryParameters3D();
params.ShapeRid = shapeRid;

// Execute physics queries here...

// Release the shape when done with physics queries.
PhysicsServer3D.FreeRid(shapeRid);
```
Transform3Dtransform=Transform3D(1,0,0,0,1,0,0,0,1,0,0,0)🔗
- voidset_transform(value:Transform3D)
voidset_transform(value:Transform3D)
- Transform3Dget_transform()
Transform3Dget_transform()
The queried shape's transform matrix.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.