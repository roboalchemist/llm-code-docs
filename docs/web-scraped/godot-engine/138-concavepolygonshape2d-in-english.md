# ConcavePolygonShape2D in English

# ConcavePolygonShape2D
Inherits:Shape2D<Resource<RefCounted<Object
A 2D polyline shape used for physics collision.

## Description
A 2D polyline shape, intended for use in physics. Used internally inCollisionPolygon2Dwhen it's inCollisionPolygon2D.BUILD_SEGMENTSmode.
Being just a collection of interconnected line segments,ConcavePolygonShape2Dis the most freely configurable single 2D shape. It can be used to form polygons of any nature, or even shapes that don't enclose an area. However,ConcavePolygonShape2Disholloweven if the interconnected line segments do enclose an area, which often makes it unsuitable for physics or detection.
Note:When used for collision,ConcavePolygonShape2Dis intended to work with staticCollisionShape2Dnodes likeStaticBody2Dand will likely not behave well forCharacterBody2Ds orRigidBody2Ds in a mode other than Static.
Warning:Physics bodies that are small have a chance to clip through this shape when moving fast. This happens because on one frame, the physics body may be on the "outside" of the shape, and on the next frame it may be "inside" it.ConcavePolygonShape2Dis hollow, so it won't detect a collision.
Performance:Due to its complexity,ConcavePolygonShape2Dis the slowest 2D collision shape to check collisions against. Its use should generally be limited to level geometry. If the polyline is closed,CollisionPolygon2D'sCollisionPolygon2D.BUILD_SOLIDSmode can be used, which decomposes the polygon into convex ones; seeConvexPolygonShape2D's documentation for instructions.

## Properties

| PackedVector2Array | segments | PackedVector2Array() |

PackedVector2Array
segments
PackedVector2Array()

## Property Descriptions
PackedVector2Arraysegments=PackedVector2Array()🔗
- voidset_segments(value:PackedVector2Array)
voidset_segments(value:PackedVector2Array)
- PackedVector2Arrayget_segments()
PackedVector2Arrayget_segments()
The array of points that make up theConcavePolygonShape2D's line segments. The array (of length divisible by two) is naturally divided into pairs (one pair for each segment); each pair consists of the starting point of a segment and the endpoint of a segment.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedVector2Arrayfor more details.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.